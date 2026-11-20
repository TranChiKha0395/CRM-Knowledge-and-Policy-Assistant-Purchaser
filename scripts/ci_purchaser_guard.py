"""Purchaser Repository Automated Guardrails (SoD, 0% PII, Secrets, CSV/G1 Contracts, Docs).

Checks enforced on every PR/push in CRM-Knowledge-and-Policy-Assistant-Purchaser:
1. Chinese Wall / SoD: blocks forbidden files (100 Sealed plaintext, 80 Challenges, .env, keys).
2. Secret Scan: blocks leaked tokens/keys (GitHub PAT, Atlassian token, AWS key, PEM headers).
3. SEC 02 / SEC 06: scans text/data files for unauthorized Vietnamese PII (phone, personal email, CCCD, MST).
4. DAT 01 / DEL 01 / KNW 03: verifies UTF-8 CSV column contracts (exact 21/23 headers), max 6,000 Unicode chars,
   enum values, +07:00 timestamps, 6-dim DAT 04 scope on G1 corpus, and Sealed redaction.
5. G1-AC01 / DAT 08: verifies SHA-256 checksums and repo-relative source_uri in G1 manifest CSVs.
6. Docs Integrity: verifies relative links in READMEs and blocks banned legacy strings.
"""

from __future__ import annotations

import csv
import hashlib
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
}

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(?i)100[_-]?sealed"),
    re.compile(r"(?i)sealed[_-]?plaintext"),
    re.compile(r"(?i)80[_-]?constructed[_-]?challenges"),
    re.compile(r"(?i)^\.env($|\.(?!example$))"),
    re.compile(r"(?i)\.(pem|key|p12|pfx)$"),
]

SECRET_PATTERNS = {
    "GITHUB_TOKEN": re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9_]{20,}\b|\bgithub_pat_[A-Za-z0-9_]{20,}\b"),
    "ATLASSIAN_TOKEN": re.compile(r"\bATATT3x[A-Za-z0-9_\-=]{20,}\b"),
    "AWS_ACCESS_KEY": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "PRIVATE_KEY_HEADER": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
}

PII_PATTERNS = {
    "VN_PHONE": re.compile(r"(?:\+84|0)(?:3|5|7|8|9)(?:[ .-]?[0-9]){8}\b"),
    "PERSONAL_EMAIL": re.compile(
        r"[a-zA-Z0-9_.+-]+@(?:gmail\.com|yahoo\.com|hotmail\.com|outlook\.com)\b",
        re.IGNORECASE,
    ),
    "CCCD_12_DIGITS": re.compile(r"\b0\d{11}\b"),
    "MST_10_DIGITS": re.compile(
        r"(?i)(?:mst|ma[_\s-]*so[_\s-]*thue|tax[_\s-]*id)[:\s#-]*\d{10}\b"
    ),
}

SCAN_EXTENSIONS = {".csv", ".json", ".md", ".txt", ".yaml", ".yml"}
MAX_PASSAGE_CHARS = 6000

PASSAGES_CSV_COLUMNS = [
    "passage_id", "document_id", "document_version_id", "title", "content", "source_ref",
    "page_number", "clause_ref", "language", "owner", "approver", "recorded_at", "published_at",
    "effective_from", "effective_to", "scope", "audience", "status", "supersedes",
    "has_essential_attachments", "record_action",
]

CRITICAL_FIELDS_CSV_COLUMNS = [
    "field_id", "policy_id", "policy_version_id", "document_version_id", "field_name", "field_type",
    "operator", "value", "unit", "currency", "approval_role", "time_limit", "exception_condition",
    "required_documents", "effective_from", "effective_to", "scope", "audience", "source_clause",
    "owner", "approver", "status", "record_action",
]

VALID_STATUSES = {"draft", "owner_reviewed", "approved", "scheduled", "effective", "superseded", "withdrawn"}
VALID_FIELD_TYPES = {"number", "currency", "duration", "role", "document_list", "boolean", "text_rule"}
VALID_OPERATORS = {"<=", "<", ">=", ">", "==", "in", "between", "required"}
VALID_ACTIONS = {"upsert", "tombstone"}
VALID_ROLES = {
    "reader", "steward", "policy_owner", "referral_handler",
    "administrator", "privacy_security_owner", "independent_evaluator",
}
REQUIRED_SCOPE_DIMS = ("company:", "branch:", "role:", "customer_group:", "product:", "transaction_scope:")
BANNED_DOC_PATTERNS = [
    re.compile(r"work-packages", re.IGNORECASE),
    re.compile(r"pm-schedule-tien", re.IGNORECASE),
    re.compile(r"p95\s*(?:<=|≤)\s*8\s*s\b", re.IGNORECASE),
    re.compile(r"\b8\s*giây\b", re.IGNORECASE),
]


def iter_repo_files(root: Path) -> list[Path]:
    result: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            result.append(Path(dirpath) / fname)
    return sorted(result)


def check_forbidden_files(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        rel = path.relative_to(ROOT).as_posix()
        for pat in FORBIDDEN_NAME_PATTERNS:
            if pat.search(path.name):
                errors.append(
                    f"[FORBIDDEN_FILE] {rel} violates Chinese Wall / secret guardrail ({pat.pattern})"
                )
    return errors


def check_secrets_and_pii(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("scripts/"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for kind, pat in SECRET_PATTERNS.items():
                if pat.search(line):
                    errors.append(f"[SECRET_LEAK] {rel}:{line_no} [{kind}]")
            for kind, pat in PII_PATTERNS.items():
                for match in pat.findall(line):
                    errors.append(f"[PII_HIT] {rel}:{line_no} [{kind}] -> {match}")
    return errors


def _validate_common_row_fields(
    rel: str, idx: int, row: dict[str, str], is_g1: bool, errors: list[str]
) -> None:
    status = (row.get("status") or "").strip()
    if status and status not in VALID_STATUSES:
        errors.append(f"[CSV_ENUM] {rel}:{idx}: invalid status '{status}'")

    action = (row.get("record_action") or "").strip()
    if action and action not in VALID_ACTIONS:
        errors.append(f"[CSV_ENUM] {rel}:{idx}: invalid record_action '{action}'")

    audience = row.get("audience") or ""
    for role in audience.split(","):
        r = role.strip()
        if r and r not in VALID_ROLES:
            errors.append(f"[CSV_ENUM] {rel}:{idx}: invalid audience role '{r}'")

    if is_g1:
        scope = row.get("scope") or ""
        for dim in REQUIRED_SCOPE_DIMS:
            if dim not in scope:
                errors.append(f"[DAT04_SCOPE] {rel}:{idx}: missing scope dimension '{dim}'")
        eff_from = (row.get("effective_from") or "").strip()
        if eff_from and not eff_from.endswith("+07:00"):
            errors.append(f"[OPS03_TZ] {rel}:{idx}: effective_from '{eff_from}' must end with +07:00")


def check_csv_contracts(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".csv":
            continue
        rel = path.relative_to(ROOT).as_posix()
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as fp:
                reader = csv.DictReader(fp)
                headers = reader.fieldnames or []
                rows = list(reader)
        except Exception as exc:
            errors.append(f"[CSV_READ_ERROR] {rel}: {exc}")
            continue

        lower_name = path.name.lower()
        is_fixture = "fixture" in lower_name
        is_g1 = rel.startswith("data/g1/")

        if ("policy_corpus" in lower_name or lower_name.startswith("passages")) and not is_fixture:
            if headers != PASSAGES_CSV_COLUMNS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: passages header mismatch (got {len(headers)} cols)"
                )
            for idx, row in enumerate(rows, 2):
                content = row.get("content") or ""
                if len(content) > MAX_PASSAGE_CHARS:
                    errors.append(
                        f"[PASSAGE_TOO_LONG] {rel}:{idx}: {len(content)} > {MAX_PASSAGE_CHARS} Unicode chars"
                    )
                _validate_common_row_fields(rel, idx, row, is_g1, errors)

        if "critical_fields" in lower_name and not is_fixture:
            if headers != CRITICAL_FIELDS_CSV_COLUMNS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: critical_fields header mismatch (got {len(headers)} cols)"
                )
            for idx, row in enumerate(rows, 2):
                ftype = (row.get("field_type") or "").strip()
                op = (row.get("operator") or "").strip()
                if ftype and ftype not in VALID_FIELD_TYPES:
                    errors.append(f"[CSV_ENUM] {rel}:{idx}: invalid field_type '{ftype}'")
                if op and op not in VALID_OPERATORS:
                    errors.append(f"[CSV_ENUM] {rel}:{idx}: invalid operator '{op}'")
                _validate_common_row_fields(rel, idx, row, is_g1, errors)

        if "Partition" in headers and "Question_VN" in headers:
            for idx, row in enumerate(rows, 2):
                part = (row.get("Partition") or "").upper()
                q = row.get("Question_VN") or ""
                if "SEAL" in part and "HIDDEN" not in q.upper():
                    errors.append(
                        f"[SEALED_LEAK] {rel}:{idx}: SEALED row appears unredacted!"
                    )

    return errors


def _sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_g1_manifests(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if not (path.name.startswith("Source_URI_And_Checksum_Manifest_") and path.suffix.lower() == ".csv"):
            continue
        rel = path.relative_to(ROOT).as_posix()
        folder = path.parent
        pas_candidates = list(folder.glob("Policy_Corpus_*.csv"))
        cf_candidates = list(folder.glob("Critical_Fields_*.csv"))
        if not pas_candidates or not cf_candidates:
            errors.append(f"[MANIFEST] {rel}: missing paired Policy_Corpus_*.csv or Critical_Fields_*.csv")
            continue

        with pas_candidates[0].open("r", encoding="utf-8-sig", newline="") as fp:
            pas_by_id = {r["passage_id"]: r for r in csv.DictReader(fp)}
        with cf_candidates[0].open("r", encoding="utf-8-sig", newline="") as fp:
            cf_by_id = {r["field_id"]: r for r in csv.DictReader(fp)}
        with path.open("r", encoding="utf-8-sig", newline="") as fp:
            man_rows = list(csv.DictReader(fp))

        expected = len(pas_by_id) + len(cf_by_id)
        if len(man_rows) != expected:
            errors.append(f"[MANIFEST] {rel}: row count {len(man_rows)} != expected {expected}")

        for idx, m in enumerate(man_rows, 2):
            src_uri = (m.get("source_uri") or "").strip()
            if not src_uri or not (ROOT / src_uri).exists() or m.get("source_uri_exists") != "true":
                errors.append(f"[MANIFEST_URI] {rel}:{idx}: missing source_uri '{src_uri}'")
                continue
            rtype = m.get("record_type")
            rid = m.get("record_id") or ""
            if rtype == "passage" and rid in pas_by_id:
                p = pas_by_id[rid]
                calc = _sha256_text(
                    f"{p['passage_id']}|{p['document_id']}|{p['document_version_id']}|"
                    f"{p['clause_ref']}|{p['content']}|{p['scope']}|{p['status']}"
                )
                if calc != m.get("sha256_checksum"):
                    errors.append(f"[MANIFEST_HASH] {rel}:{idx}: SHA-256 mismatch for {rid}")
            elif rtype == "critical_field" and rid in cf_by_id:
                c = cf_by_id[rid]
                calc = _sha256_text(
                    f"{c['field_id']}|{c['policy_id']}|{c['policy_version_id']}|{c['field_type']}|"
                    f"{c['operator']}|{c['value']}|{c['unit']}|{c['currency']}|{c['approval_role']}|{c['status']}"
                )
                if calc != m.get("sha256_checksum"):
                    errors.append(f"[MANIFEST_HASH] {rel}:{idx}: SHA-256 mismatch for {rid}")
            else:
                errors.append(f"[MANIFEST_REF] {rel}:{idx}: unknown record_type/record_id ({rtype}/{rid})")
    return errors


def check_docs() -> list[str]:
    errors: list[str] = []
    link_re = re.compile(r"!?\[[^\]]*\]\(([^)\r\n]+)\)")
    for rel_doc in ("README.md", "data/g1/README.md"):
        doc_path = ROOT / rel_doc
        if not doc_path.exists():
            continue
        text = doc_path.read_text(encoding="utf-8", errors="replace")
        for pat in BANNED_DOC_PATTERNS:
            if pat.search(text):
                errors.append(f"[DOCS_BANNED] {rel_doc}: matches legacy pattern '{pat.pattern}'")
        for m in link_re.finditer(text):
            target = m.group(1).strip().split()[0]
            if target.startswith(("#", "http://", "https://", "mailto:", "tel:")):
                continue
            clean_target = target.split("#", 1)[0].split("?", 1)[0]
            if not (doc_path.parent / clean_target).exists():
                errors.append(f"[DOCS_LINK] {rel_doc}: broken relative link -> {target}")
    return errors


def main() -> int:
    files = iter_repo_files(ROOT)
    errors: list[str] = []
    errors.extend(check_forbidden_files(files))
    errors.extend(check_secrets_and_pii(files))
    errors.extend(check_csv_contracts(files))
    errors.extend(check_g1_manifests(files))
    errors.extend(check_docs())

    print(f"Purchaser CI Guard scanned {len(files)} file(s).")
    if errors:
        print(f"FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PASSED: 0 forbidden files, 0 secrets/PII, CSV/Manifest contracts & docs OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
