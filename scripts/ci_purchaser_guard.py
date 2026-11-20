"""Purchaser Repository Automated Guardrails (SoD, 0% PII, CSV Schema).

Checks enforced on every PR/push in CRM-Knowledge-and-Policy-Assistant-Purchaser:
1. Chinese Wall / SoD: blocks forbidden files (100 Sealed plaintext, 80 Challenges, .env secrets).
2. SEC 02 / SEC 06: scans text/data files for unauthorized Vietnamese PII (phone, CCCD, personal email, MST).
3. DAT 01 / Mục 2: verifies UTF-8 CSV column contracts (21 cols Passages, 23 cols Critical Fields)
   and max 6,000 Unicode characters per passage.
4. Partition redaction: ensures any SEALED row in committed CSVs is redacted (no plaintext questions).
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

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(?i)100[_-]?sealed"),
    re.compile(r"(?i)sealed[_-]?plaintext"),
    re.compile(r"(?i)80[_-]?constructed[_-]?challenges"),
    re.compile(r"(?i)^\.env($|\.(?!example$))"),
    re.compile(r"(?i)\.(pem|key|p12|pfx)$"),
]

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
PASSAGES_EXPECTED_COLS = 21
CRITICAL_FIELDS_EXPECTED_COLS = 23
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


def check_pii(files: list[Path]) -> list[str]:
    errors: list[str] = []
    for path in files:
        if path.suffix.lower() not in SCAN_EXTENSIONS:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if rel.startswith("scripts/"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for line_no, line in enumerate(text.splitlines(), 1):
            for kind, pat in PII_PATTERNS.items():
                for match in pat.findall(line):
                    errors.append(f"[PII_HIT] {rel}:{line_no} [{kind}] -> {match}")
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
                headers = reader.fieldnames or []
                rows = list(reader)
        except Exception as exc:
            errors.append(f"[CSV_READ_ERROR] {rel}: {exc}")
            continue

        lower_name = path.name.lower()
        if (
            "policy_corpus" in lower_name or lower_name.startswith("passages")
        ) and "fixture" not in lower_name:
            if len(headers) != PASSAGES_EXPECTED_COLS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: expected {PASSAGES_EXPECTED_COLS} columns, got {len(headers)}"
                )
            for idx, row in enumerate(rows, 2):
                content = row.get("content") or ""
                if len(content) > MAX_PASSAGE_CHARS:
                    errors.append(
                        f"[PASSAGE_TOO_LONG] {rel}:{idx}: {len(content)} > {MAX_PASSAGE_CHARS} Unicode chars"
                    )

        if (
            "critical_fields" in lower_name and "fixture" not in lower_name
        ):
            if len(headers) != CRITICAL_FIELDS_EXPECTED_COLS:
                errors.append(
                    f"[CSV_SCHEMA] {rel}: expected {CRITICAL_FIELDS_EXPECTED_COLS} columns, got {len(headers)}"
                )

        if "Partition" in headers and "Question_VN" in headers:
            for idx, row in enumerate(rows, 2):
                part = (row.get("Partition") or "").upper()
                q = row.get("Question_VN") or ""
                if "SEAL" in part and "HIDDEN" not in q.upper():
                    errors.append(
                        f"[SEALED_LEAK] {rel}:{idx}: SEALED row appears unredacted!"
                    )

    return errors


def main() -> int:
    files = iter_repo_files(ROOT)
    errors: list[str] = []
    errors.extend(check_forbidden_files(files))
    errors.extend(check_pii(files))
    errors.extend(check_csv_contracts(files))

    print(f"Purchaser CI Guard scanned {len(files)} file(s).")
    if errors:
        print(f"FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PASSED: 0 forbidden files, 0 PII hits, CSV contracts & Sealed redaction OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
