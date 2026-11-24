"""
CKPA-47 | CRM-G1-SUB02 | G1-AC07
SCRM Gate G1 PII Security Audit Runner (Purchaser Repository)
Owner: [P5] Nguyen Anh Khoa (Privacy & Security Owner)
Ref: SEC 02, SEC 06, DAT 07, Muc 9 (G1), Annex C
"""

import datetime
import os
from pathlib import Path
import re
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]

PII_PATTERNS = {
    "VN_PHONE": re.compile(r"(?<![\d:])(?:\+84|0)(?:3|5|7|8|9)(?:[ .-]?\d){8}\b"),
    "EMAIL": re.compile(
        r"[a-zA-Z0-9_.+-]+@(?!(?:songnhat\.vn|example\.com)\b)[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+",
        re.IGNORECASE,
    ),
    "CCCD_12_DIGITS": re.compile(r"\b0\d{11}\b"),
    "MST_10_DIGITS": re.compile(r"(?i)(?:mst|ma[_\s-]*so[_\s-]*thue|tax[_\s-]*id)[:\s#-]*\d{10}\b"),
}

EXCLUDE_DIRS = {
    ".git", ".venv", "venv", "node_modules", "__pycache__", ".pytest_cache", "dist", "build", "scripts"
}
EXCLUDE_REL_PREFIXES = (
    "scripts/",
    "security/scripts/",
    "data/g1/scripts/",
)
EXCLUDE_FILES = {
    "package-lock.json", "yarn.lock", "pnpm-lock.yaml", "g1_pii_audit_CKPA-47.log"
}
TARGET_EXTENSIONS = (".csv", ".json", ".log", ".md", ".tsv", ".txt", ".yaml", ".yml")


def get_git_info(root_dir: Path):
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "--short", "HEAD"], cwd=root_dir, stderr=subprocess.DEVNULL
        ).decode().strip()
        branch = subprocess.check_output(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=root_dir, stderr=subprocess.DEVNULL
        ).decode().strip()
        return branch, sha
    except Exception:
        return "unknown-branch", "unknown-sha"


def collect_files(root_dir: Path = REPO_ROOT):
    collected = []
    for current_root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS and not d.startswith(".")]
        for f in files:
            if f in EXCLUDE_FILES:
                continue
            if f.lower().endswith(TARGET_EXTENSIONS):
                full_p = Path(current_root) / f
                rel_path = full_p.relative_to(root_dir).as_posix()
                if rel_path.startswith(EXCLUDE_REL_PREFIXES):
                    continue
                collected.append(rel_path)
    return sorted(collected)


def run_audit(root_dir: Path = REPO_ROOT, log_rel_path: str = "security/g1/g1_pii_audit_CKPA-47.log"):
    root_dir = Path(root_dir).resolve()
    branch, sha = get_git_info(root_dir)
    tz_vn = datetime.timezone(datetime.timedelta(hours=7))
    ts = datetime.datetime.now(tz_vn).strftime("%Y-%m-%d %H:%M:%S UTC+7")
    files = collect_files(root_dir)
    hits = []

    for rel_f in files:
        full_path = root_dir / rel_f
        with full_path.open(encoding="utf-8-sig", errors="replace") as fp:
            for i, line in enumerate(fp, 1):
                for kind, pattern in PII_PATTERNS.items():
                    for m in pattern.findall(line):
                        hits.append((rel_f, i, kind, m))

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 PII SECURITY AUDIT LOG (PURCHASER REPO) ===",
        "Jira Issue     : CKPA-47 (CRM-G1-SUB02 | G1-AC07)",
        "Repository     : CRM-Knowledge-and-Policy-Assistant-Purchaser",
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
        lines.append("  No unauthorized PII detected across Purchaser G0/G1 repository (0% PII).")

    lines.append("--- Scanned Files Inventory ---")
    for idx, f in enumerate(files, 1):
        lines.append(f"  {idx:03d}. {f}")

    log_path = root_dir / log_rel_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

    print("\n".join(lines[:15]))
    print(f"[OK] Scanned {len(files)} files, {len(hits)} PII hits -> {log_path}")
    return 0 if len(hits) == 0 else 1


if __name__ == "__main__":
    sys.exit(run_audit())
