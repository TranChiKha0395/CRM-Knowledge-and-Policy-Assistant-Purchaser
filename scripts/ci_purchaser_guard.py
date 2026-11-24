"""Purchaser Repository Automated Guardrails (SoD, 0% PII, CSV Schema, AI Artifacts).

Checks enforced on every PR/push in CRM-Knowledge-and-Policy-Assistant-Purchaser:
1. Chinese Wall / SoD: blocks forbidden files (100 Sealed plaintext, 80 Challenges, .env secrets).
2. SEC 02 / SEC 06: scans text/data/log files for unauthorized Vietnamese PII (phone, CCCD, non-SongNhat email, MST)
   and leftover AI citation artifacts ([cite: ...]).
3. DAT 01 / Mục 2: verifies exact UTF-8 CSV column contracts (21 cols Passages, 23 cols Critical Fields, including fixtures)
   and max 6,000 Unicode characters per passage.
4. Partition redaction: ensures any SEALED row (in Partition or Provisional_Partition) is strictly redacted.
"""

from __future__ import annotations

import csv
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

SCRIPT_PREFIXES = ("scripts/", "security/scripts/", "data/g1/scripts/")

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(?i)100[_-]?sealed"),
    re.compile(r"(?i)sealed[_-]?plaintext"),
    re.compile(r"(?i)80[_-]?constructed[_-]?challenges"),
    re.compile(r"(?i)^\.env($|\.(?!example$))"),
    re.compile(r"(?i)\.(pem|key|p12|pfx)$"),
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

SCAN_EXTENSIONS = {".csv", ".json", ".log", ".md", ".tsv", ".txt", ".yaml", ".yml"}

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


def check_pii_and_artifacts(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith(SCRIPT_PREFIXES):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for kind, pat in PII_PATTERNS.items():
                for match in pat.findall(line):
                    errors.append(f"[PII_HIT] {rel}:{line_no} [{kind}] -> {match}")
            for art in AI_ARTIFACT_PATTERN.findall(line):
                errors.append(f"[AI_ARTIFACT] {rel}:{line_no} leftover citation tag -> {art}")
    return errors


def check_csv_contracts(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() != ".csv":
            continue
        rel = path.relative_to(ROOT).as_posix()
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

    return errors


def main() -> int:
    files = iter_repo_files(ROOT)
    errors: list[str] = []
    errors.extend(check_forbidden_files(files))
    errors.extend(check_pii_and_artifacts(files))
    errors.extend(check_csv_contracts(files))

    print(f"Purchaser CI Guard scanned {len(files)} file(s).")
    if errors:
        print(f"FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PASSED: 0 forbidden files, 0 PII/AI-artifact hits, exact 21/23 CSV schemas & Sealed redaction OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
