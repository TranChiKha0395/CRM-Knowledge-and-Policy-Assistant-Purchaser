r"""Purchaser Repository Automated Guardrails (SoD, 0% PII, Domain, Anti-Mock, CSV Schema, Links).

Enforced on every PR/push in CRM-Knowledge-and-Policy-Assistant-Purchaser:
1. Chinese Wall & Binary Ban: blocks 100 Sealed plaintext, 80 Challenges, secrets, and binary Office/PDF/archive files.
2. UTF-8 Hygiene: blocks UTF-8 BOM (\ufeff) across tracked text/code/data files.
3. SEC 02 / Hygiene: scans for Vietnamese PII, leftover [cite:], legacy IDs (CKPAOLD, SQUAD, [A1..D2]),
   inline LaTeX ($\rightarrow$, $\le$, $\ge$), and hardcoded local machine paths (file:///C:/, C:\\Users\\, /Users/).
4. SongNhat Domain Guard: blocks hallucinated e-commerce policy family mappings (e.g. POL-001 -> Doi tra, POL-002 -> Bao hanh, POL-003 -> Van chuyen).
5. Anti-Mock UAT Guard: flags periodic copy-paste score synthesis in UAT evaluation CSVs.
6. Markdown Relative Link Integrity: ensures all repo-relative Markdown links resolve to existing files.
7. DAT 01 / Muc 2: verifies exact UTF-8 CSV column contracts (21 cols Passages, 23 cols Critical Fields),
   max 6,000 Unicode chars, Sealed redaction, and G1 SHA-256 manifest integrity.
"""

from __future__ import annotations

import csv
import hashlib
import os
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent.parent

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    "node_modules",
}

SCRIPT_PREFIXES = ("scripts/", "security/scripts/", "data/g1/scripts/")

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(?i)100[_-]?sealed"),
    re.compile(r"(?i)sealed[_-]?plaintext"),
    re.compile(r"(?i)80[_-]?constructed[_-]?challenges"),
    re.compile(r"(?i)^\.env($|\.(?!example$))"),
    re.compile(r"(?i)\.(pem|key|p12|pfx)$"),
    re.compile(r"(?i)\.(docx|doc|xlsx|xls|pptx|ppt|pdf|zip|rar|7z|exe|dll)$"),
]

PII_PATTERNS = {
    "VN_PHONE": re.compile(r"(?<![\d:])(?:\+84|0)(?:3|5|7|8|9)(?:[ .-]?[0-9]){8}\b"),
    "UNAUTHORIZED_EMAIL": re.compile(
        r"[a-zA-Z0-9_.+-]+@(?!(?:songnhat\.vn|example\.com)\b)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        re.IGNORECASE,
    ),
    "CCCD_12_DIGITS": re.compile(r"\b0\d{11}\b"),
    "MST_10_DIGITS": re.compile(
        r"(?i)(?:mst|ma[_\s-]*so[_\s-]*thue|tax[_\s-]*id)[:\s#-]*\d{10}\b"
    ),
}

AI_ARTIFACT_PATTERN = re.compile(r"\[cite\s*:\s*[\d,\s]+\]", re.IGNORECASE)
LEGACY_ID_PATTERN = re.compile(r"\bCKPAOLD\b|\bSQUAD\b|\[(?:A[1-3]|B[1-3]|C[1-2]|D[1-2])\]")
INLINE_LATEX_PATTERN = re.compile(
    r"\$\s*\\(?:rightarrow|leftarrow|Rightarrow|Leftarrow|ge|le|geq|leq|neq|times|cdot)\b"
)
LOCAL_PATH_PATTERN = re.compile(
    r"file:///[A-Za-z]:/|[A-Za-z]:\\Users\\|(?<![A-Za-z0-9_])/Users/[A-Za-z0-9_.-]+/"
)
HALLUCINATED_DOMAIN_TEXT_PATTERN = re.compile(
    r"(?i)chính\s+sách\s+vận\s+chuyển|chính\s+sách\s+đổi\s+trả\s*(?:&|và)\s*hoàn\s+tiền|họ\s*1\s*\(\s*đổi\s+trả\s*\)|họ\s*3\s*\(\s*vận\s+chuyển\s*\)"
)

POLICY_FAMILY_KEYWORDS = {
    "POL-001": ("báo giá", "thương mại", "chiết khấu", "phê duyệt", "quotation", "commercial"),
    "POL-002": ("khách hàng", "dữ liệu", "thông tin", "customer", "pii", "bảo mật"),
    "POL-003": ("bảo hành", "sửa chữa", "rma", "kỹ thuật", "warranty"),
}

SCAN_EXTENSIONS = {".csv", ".json", ".log", ".md", ".tsv", ".txt", ".yaml", ".yml"}
BOM_CHECK_EXTENSIONS = SCAN_EXTENSIONS | {".py", ".sh"}
MD_LINK_PATTERN = re.compile(r"!?\[[^\]]*\]\(([^)\r\n]+)\)")

PASSAGES_EXPECTED_HEADERS = [
    "passage_id",
    "document_id",
    "document_version_id",
    "title",
    "content",
    "source_ref",
    "page_number",
    "clause_ref",
    "language",
    "owner",
    "approver",
    "recorded_at",
    "published_at",
    "effective_from",
    "effective_to",
    "scope",
    "audience",
    "status",
    "supersedes",
    "has_essential_attachments",
    "record_action",
]

CRITICAL_FIELDS_EXPECTED_HEADERS = [
    "field_id",
    "policy_id",
    "policy_version_id",
    "document_version_id",
    "field_name",
    "field_type",
    "operator",
    "value",
    "unit",
    "currency",
    "approval_role",
    "time_limit",
    "exception_condition",
    "required_documents",
    "effective_from",
    "effective_to",
    "scope",
    "audience",
    "source_clause",
    "owner",
    "approver",
    "status",
    "record_action",
]

MAX_PASSAGE_CHARS = 6000


def iter_repo_files(root: Path) -> list[Path]:
    result: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for fname in filenames:
            result.append(Path(dirpath) / fname)
    return sorted(result)


def check_forbidden_files(files: list[Path], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in files:
        rel = path.relative_to(root).as_posix()
        for pat in FORBIDDEN_NAME_PATTERNS:
            if pat.search(path.name):
                errors.append(
                    f"[FORBIDDEN_FILE] {rel} violates Chinese Wall / binary / secret guardrail ({pat.pattern})"
                )
    return errors


def check_utf8_bom(files: list[Path], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in BOM_CHECK_EXTENSIONS:
            continue
        try:
            with path.open("rb") as fp:
                prefix = fp.read(3)
        except OSError:
            continue
        if prefix == b"\xef\xbb\xbf":
            rel = path.relative_to(root).as_posix()
            errors.append(f"[UTF8_BOM] {rel} starts with UTF-8 BOM (save as plain UTF-8 without BOM)")
    return errors


def check_pii_and_artifacts(files: list[Path], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        rel = path.relative_to(root).as_posix()
        if rel.startswith(SCRIPT_PREFIXES):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        in_code_fence = False
        for line_no, line in enumerate(text.splitlines(), 1):
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_fence = not in_code_fence
            for kind, pat in PII_PATTERNS.items():
                for match in pat.findall(line):
                    errors.append(f"[PII_HIT] {rel}:{line_no} [{kind}] -> {match}")
            for art in AI_ARTIFACT_PATTERN.findall(line):
                errors.append(f"[AI_ARTIFACT] {rel}:{line_no} leftover citation tag -> {art}")
            for leg in LEGACY_ID_PATTERN.findall(line):
                errors.append(f"[LEGACY_ID] {rel}:{line_no} forbidden legacy identifier -> {leg}")
            for ltx in INLINE_LATEX_PATTERN.findall(line):
                errors.append(f"[INLINE_LATEX] {rel}:{line_no} forbidden inline LaTeX -> {ltx}")
            for lpath in LOCAL_PATH_PATTERN.findall(line):
                errors.append(
                    f"[LOCAL_PATH] {rel}:{line_no} hardcoded local machine path -> {lpath} (use repo-relative path)"
                )
            for dom in HALLUCINATED_DOMAIN_TEXT_PATTERN.findall(line):
                errors.append(
                    f"[WRONG_DOMAIN] {rel}:{line_no} hallucinated non-SongNhat policy domain -> '{dom}'"
                )

            if path.suffix.lower() == ".md" and not in_code_fence:
                for m in MD_LINK_PATTERN.finditer(line):
                    raw_target = m.group(1).strip().split()[0].strip("<>")
                    if not raw_target or raw_target.startswith(
                        ("#", "http://", "https://", "mailto:", "tel:", "conversation:", "file:")
                    ):
                        continue
                    clean_rel = unquote(raw_target.split("#")[0].split("?")[0]).strip()
                    if not clean_rel:
                        continue
                    resolved = (path.parent / clean_rel).resolve()
                    if not resolved.exists():
                        errors.append(
                            f"[BROKEN_LINK] {rel}:{line_no} relative link target does not exist -> {raw_target}"
                        )
    return errors


def _check_policy_family_mapping(rel: str, headers: list[str], rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if "Policy_Family" not in headers or "Policy_Family_Name" not in headers:
        return errors
    for idx, row in enumerate(rows, 2):
        fam = (row.get("Policy_Family") or "").strip().upper()
        fam_name = (row.get("Policy_Family_Name") or "").strip()
        if fam in POLICY_FAMILY_KEYWORDS and fam_name:
            lower_name = fam_name.lower()
            if not any(kw in lower_name for kw in POLICY_FAMILY_KEYWORDS[fam]):
                errors.append(
                    f"[WRONG_DOMAIN] {rel}:{idx}: {fam} mapped to invalid domain '{fam_name}' "
                    f"(expected SongNhat {fam} domain)"
                )
    return errors


def _check_synthetic_uat_scores(rel: str, headers: list[str], rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if len(rows) < 25:
        return errors
    score_cols = [h for h in headers if h.endswith("_Score") or h in ("Consensus_Note", "P4_UX_Observation_And_Feedback")]
    if len(score_cols) < 2:
        return errors
    signatures = [tuple((r.get(c) or "").strip() for c in score_cols) for r in rows]
    counts = Counter(signatures)
    top3_total = sum(cnt for _, cnt in counts.most_common(3))
    if len(counts) <= 4 and (top3_total / len(rows)) >= 0.85:
        errors.append(
            f"[NO_MOCK_VIOLATION] {rel}: {top3_total}/{len(rows)} rows repeat only {len(counts)} identical "
            f"score/comment templates — synthetic/mock UAT data is strictly prohibited!"
        )
    return errors


def check_csv_contracts(files: list[Path], root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".csv":
            continue
        rel = path.relative_to(root).as_posix()
        try:
            with path.open("r", encoding="utf-8-sig", newline="") as fp:
                reader = csv.DictReader(fp)
                headers = list(reader.fieldnames or [])
                rows = list(reader)
        except Exception as exc:
            errors.append(f"[CSV_READ_ERROR] {rel}: {exc}")
            continue

        lower_name = path.name.lower()
        is_fixture = "fixture" in lower_name

        if "policy_corpus" in lower_name or "passages" in lower_name:
            if headers != PASSAGES_EXPECTED_HEADERS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: header mismatch with 21-column PASSAGES_CSV_COLUMNS (got {len(headers)} cols)"
                )
            if not is_fixture:
                for idx, row in enumerate(rows, 2):
                    content = row.get("content") or ""
                    if len(content) > MAX_PASSAGE_CHARS:
                        errors.append(
                            f"[PASSAGE_TOO_LONG] {rel}:{idx}: {len(content)} > {MAX_PASSAGE_CHARS} Unicode chars"
                        )

        if "critical_fields" in lower_name or "criticalfields" in lower_name:
            if headers != CRITICAL_FIELDS_EXPECTED_HEADERS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: header mismatch with 23-column CRITICAL_FIELDS_CSV_COLUMNS (got {len(headers)} cols)"
                )

        if ("Partition" in headers or "Provisional_Partition" in headers) and "Question_VN" in headers:
            for idx, row in enumerate(rows, 2):
                part = (row.get("Partition") or "").upper()
                prov = (row.get("Provisional_Partition") or "").upper()
                if "SEAL" in part or "SEAL" in prov:
                    q_val = (row.get("Question_VN") or "").upper()
                    if "HIDDEN" not in q_val and "REDACTED" not in q_val:
                        errors.append(
                            f"[SEALED_LEAK] {rel}:{idx}: SEALED row Question_VN appears unredacted!"
                        )
                    for sensitive_col in ("Gold_Clause_IDs", "Gold_Critical_Field_IDs", "Expected_Behavior"):
                        if sensitive_col in headers:
                            val = (row.get(sensitive_col) or "").upper()
                            if val and not any(tag in val for tag in ("HIDDEN", "REDACTED", "[LOCKED")):
                                errors.append(
                                    f"[SEALED_LEAK] {rel}:{idx}: SEALED row column '{sensitive_col}' appears unredacted!"
                                )

        if not is_fixture:
            errors.extend(_check_policy_family_mapping(rel, headers, rows))
            if rel.startswith("uat/"):
                errors.extend(_check_synthetic_uat_scores(rel, headers, rows))

    return errors


def _sha256_utf8(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def check_g1_manifests(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    bundles = [
        (
            "Family1",
            root / "data/g1/family1/Policy_Corpus_Family1.csv",
            root / "data/g1/family1/Critical_Fields_Family1.csv",
            root / "data/g1/family1/Source_URI_And_Checksum_Manifest_Family1.csv",
        ),
        (
            "FullG1",
            root / "data/g1/full/Policy_Corpus_G1_Full.csv",
            root / "data/g1/full/Critical_Fields_G1_Full.csv",
            root / "data/g1/full/Source_URI_And_Checksum_Manifest_G1_Full.csv",
        ),
    ]
    for label, pas_path, cf_path, man_path in bundles:
        if not (pas_path.exists() and cf_path.exists() and man_path.exists()):
            continue
        with pas_path.open("r", encoding="utf-8", newline="") as fp:
            pas_by_id = {r["passage_id"]: r for r in csv.DictReader(fp)}
        with cf_path.open("r", encoding="utf-8", newline="") as fp:
            cf_by_id = {r["field_id"]: r for r in csv.DictReader(fp)}
        with man_path.open("r", encoding="utf-8", newline="") as fp:
            man_rows = list(csv.DictReader(fp))
        if len(man_rows) != len(pas_by_id) + len(cf_by_id):
            errors.append(
                f"[G1_MANIFEST] {label}: manifest count {len(man_rows)} != {len(pas_by_id) + len(cf_by_id)}"
            )
        for idx, m in enumerate(man_rows, 2):
            src_rel = (m.get("source_uri") or "").replace("\\", "/")
            if not src_rel or not (root / src_rel).exists():
                errors.append(f"[G1_MANIFEST] {label} row {idx}: missing source_uri -> {src_rel}")
            rec_id = m.get("record_id") or ""
            if m.get("record_type") == "passage" and rec_id in pas_by_id:
                p = pas_by_id[rec_id]
                calc = _sha256_utf8(
                    f"{p['passage_id']}|{p['document_id']}|{p['document_version_id']}|"
                    f"{p['clause_ref']}|{p['content']}|{p['scope']}|{p['status']}"
                )
                if calc != m.get("sha256_checksum"):
                    errors.append(f"[G1_MANIFEST] {label} {rec_id}: SHA-256 mismatch")
            elif m.get("record_type") == "critical_field" and rec_id in cf_by_id:
                c = cf_by_id[rec_id]
                calc = _sha256_utf8(
                    f"{c['field_id']}|{c['policy_id']}|{c['policy_version_id']}|{c['field_type']}|"
                    f"{c['operator']}|{c['value']}|{c['unit']}|{c['currency']}|{c['approval_role']}|{c['status']}"
                )
                if calc != m.get("sha256_checksum"):
                    errors.append(f"[G1_MANIFEST] {label} {rec_id}: SHA-256 mismatch")
    return errors


def _write_step_summary(scanned_count: int, errors: list[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = ["## Purchaser Repo Guardrails Summary\n"]
    lines.append(f"- **Files scanned:** `{scanned_count}`")
    if not errors:
        lines.append("- **Verdict:** **PASS (0 violations)**\n")
    else:
        lines.append(f"- **Verdict:** **FAIL ({len(errors)} violation(s) — cần sửa trước khi merge)**\n")
        lines.append("### Danh sách lỗi cần khắc phục")
        for err in errors[:50]:
            lines.append(f"- `{err}`")
        if len(errors) > 50:
            lines.append(f"- ... và `{len(errors) - 50}` lỗi khác.")
    with open(summary_path, "a", encoding="utf-8") as fp:
        fp.write("\n".join(lines) + "\n")


def run_all_checks(root: Path = ROOT) -> tuple[int, list[str]]:
    files = iter_repo_files(root)
    errors: list[str] = []
    errors.extend(check_forbidden_files(files, root))
    errors.extend(check_utf8_bom(files, root))
    errors.extend(check_pii_and_artifacts(files, root))
    errors.extend(check_csv_contracts(files, root))
    errors.extend(check_g1_manifests(root))
    return len(files), errors


def main() -> int:
    scanned_count, errors = run_all_checks(ROOT)
    _write_step_summary(scanned_count, errors)

    print(f"Purchaser CI Guard scanned {scanned_count} file(s).")
    if errors:
        print(f"FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print(
        "PASSED: 0 forbidden/BOM files, 0 PII/AI/LaTeX/legacy/local-path hits, "
        "SongNhat domain & No-Mock OK, exact 21/23 CSV schemas & G1 SHA-256 manifests verified."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
