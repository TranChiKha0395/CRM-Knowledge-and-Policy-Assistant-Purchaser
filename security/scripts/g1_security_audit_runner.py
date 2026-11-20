"""
CKPA-47 | CRM-G1-SUB02 | G1-AC07
SCRM Gate G1 PII Security Audit Runner
Owner: [P5] Nguyen Anh Khoa (Privacy & Security Owner)
Ref: SEC 02, SEC 06, DAT 07, Muc 9 (G1), Annex C
"""

import datetime
import os
import re
import subprocess
import sys

# Regex patterns aligned with backend/src/shared/pii_guard.py
PII_PATTERNS = {
    "VN_PHONE": re.compile(r"(?:\+84|0)(?:3|5|7|8|9)(?:[ -. ]?\d){8}\b"),
    "EMAIL": re.compile(r"[a-zA-Z0-9_.+-]+@(?!(?:songnhat\.vn|example\.com)\b)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"),
    "CCCD_12_DIGITS": re.compile(r"\b0\d{11}\b"),
    "MST_10_DIGITS": re.compile(r"(?i)(?:mst|ma[_\s-]*so[_\s-]*thue|tax[_\s-]*id)[:\s#-]*\d{10}\b"),
}

EXCLUDE_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", "dist", "build"
}
EXCLUDE_FILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "g1_pii_audit_CKPA-47.log"
}
TARGET_EXTENSIONS = (".csv", ".json", ".md", ".txt", ".yaml", ".yml")


def get_git_info():
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], stderr=subprocess.DEVNULL
        ).decode().strip()
        return branch, sha
    except Exception:
        return "unknown-branch", "unknown-sha"


def collect_files(root_dir="."):
    collected = []
    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for f in files:
            if f in EXCLUDE_FILES:
                continue
            if f.lower().endswith(TARGET_EXTENSIONS):
                rel_path = os.path.relpath(os.path.join(current_root, f), root_dir).replace("\\", "/")
                collected.append(rel_path)
    return sorted(collected)


def run_audit(root_dir=".", log_path="scripts/security/g1_pii_audit_CKPA-47.log"):
    branch, sha = get_git_info()
    tz_vn = datetime.timezone(datetime.timedelta(hours=7))
    ts = datetime.datetime.now(tz_vn).strftime("%Y-%m-%d %H:%M:%S UTC+7")
    files = collect_files(root_dir)
    hits = []

    for f in files:
        with open(f, encoding="utf-8", errors="ignore") as fp:
            for i, line in enumerate(fp, 1):
                for kind, pattern in PII_PATTERNS.items():
                    for m in pattern.findall(line):
                        hits.append((f, i, kind, m))

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 PII SECURITY AUDIT LOG ===",
        "Jira Issue     : CKPA-47 (CRM-G1-SUB02 | G1-AC07)",
        "Auditor        : [P5] Nguyen Anh Khoa (Privacy & Security Owner)",
        f"Timestamp      : {ts}",
        f"Git Branch     : {branch}",
        f"Git Commit SHA : {sha}",
        f"Scanned Files  : {len(files)}",
        f"Total PII Hits : {len(hits)}",
        "--- Detailed Hits ---",
    ]
    if hits:
        for f, i, kind, m in hits:
            lines.append(f"  [HIT] {f}:line {i} [{kind}] -> {m}")
    else:
        lines.append("  No unauthorized PII detected (0% PII).")

    lines.append("--- Scanned Files Inventory ---")
    for idx, f in enumerate(files, 1):
        lines.append(f"  {idx:03d}. {f}")

    out_dir = os.path.dirname(log_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(log_path, "w", encoding="utf-8") as lf:
        lf.write("\n".join(lines) + "\n")

    print("\n".join(lines))
    return 0 if len(hits) == 0 else 1


if __name__ == "__main__":
    sys.exit(run_audit())