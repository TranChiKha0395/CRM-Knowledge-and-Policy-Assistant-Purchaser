import argparse
import csv
import datetime
import os
from pathlib import Path
import subprocess
import sys


def audit_shared_repo_isolation(repo_root: Path):
    forbidden_sealed_files = []
    for p in repo_root.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        if "sealed" in p.name.lower() and p.name not in {
            "g1_sealed_acl_audit_runner.py",
            "g1_sealed_acl_audit_CKPA-79.log",
            "CKPA-79_Bien_Ban_Kiem_Toan_ACL_Sealed_Va_Chot_Bao_Mat_G1.md",
        }:
            forbidden_sealed_files.append(str(p.relative_to(repo_root)))

    guard_proc = subprocess.run(
        [sys.executable, "scripts/ci_purchaser_guard.py"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    guard_passed = guard_proc.returncode == 0
    guard_output = (guard_proc.stdout or guard_proc.stderr).strip()

    corpus_path = repo_root / "data/g1/full/Policy_Corpus_G1_Full.csv"
    sealed_marked_rows = 0
    if corpus_path.exists():
        with corpus_path.open(encoding="utf-8-sig") as f:
            for row in csv.DictReader(f):
                val = " ".join(str(v) for v in row.values()).lower()
                if "sealed_100" in val or "sealed-eval-repo" in val:
                    sealed_marked_rows += 1

    return {
        "forbidden_sealed_files": forbidden_sealed_files,
        "guard_passed": guard_passed,
        "guard_output": guard_output,
        "sealed_marked_rows": sealed_marked_rows,
        "part1_passed": len(forbidden_sealed_files) == 0 and guard_passed and sealed_marked_rows == 0,
    }


def main():
    parser = argparse.ArgumentParser(description="CKPA-79 No-Mock Sealed Repo ACL & G1 Security Sign-Off Audit")
    parser.add_argument("--strict-external", action="store_true", help="Fail if external sealed-eval-repo ACL export is missing")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    repo_root = Path(".").resolve()
    p1 = audit_shared_repo_isolation(repo_root)

    sealed_repo_url = os.getenv("CKPA_SEALED_REPO_URL", "").strip()
    sealed_acl_log_path = os.getenv("CKPA_SEALED_ACL_LOG_PATH", "").strip()

    if sealed_acl_log_path and Path(sealed_acl_log_path).exists():
        raw_text = Path(sealed_acl_log_path).read_text(encoding="utf-8", errors="replace")
        s2_s3_hits = [
            line.strip()
            for line in raw_text.splitlines()
            if any(k in line.lower() for k in ("s2", "quoc hung", "s3", "yen nhi"))
            and any(a in line.lower() for a in ("read", "clone", "pull", "download", "admin", "write"))
        ]
        if len(s2_s3_hits) == 0:
            part2_status = "PASS_VERIFIED_ZERO_S2_S3_ACCESS"
            part2_detail = f"Verified real external ACL/audit log ({sealed_acl_log_path}): 0 Read/Clone events for S2/S3."
        else:
            part2_status = "FAIL_UNAUTHORIZED_S2_S3_ACCESS_DETECTED"
            part2_detail = f"Detected {len(s2_s3_hits)} unauthorized S2/S3 access records in {sealed_acl_log_path}."
    else:
        part2_status = "BLOCKED_EXTERNAL_REPO_ACCESS"
        part2_detail = (
            f"sealed-eval-repo ({sealed_repo_url if sealed_repo_url else 'URL_NOT_CONFIGURED'}) is isolated in SUB03 outside this repository; "
            "synthetic access logs prohibited per No-Mock policy. Awaiting real GitHub/Storage ACL & audit log export from [S4] Quy Hai / [S5] Ngoc Duy."
        )

    out_dir = Path("security/g1")
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_sealed_acl_audit_CKPA-79.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 SEALED-EVAL-REPO ACL & SECURITY SIGN-OFF AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-79 (Parent: CKPA-44 | Blocks: CKPA-80 | Relates: CKPA-77)",
        "RFP Traceability : Sec 8, Sec 11, SEC 01, SEC 02, SEC 06, SEC 08 | Gate Criteria: G1-AC04, G1-AC07",
        f"Execution Time   : {timestamp}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 1] SHARED REPOSITORY ISOLATION & 0% PII GUARD AUDIT (REAL LOCAL EXECUTION)",
        f"  - Forbidden Sealed Files in Shared Repo   : {len(p1['forbidden_sealed_files'])} ({p1['forbidden_sealed_files']})",
        f"  - Sealed Cases Leaked into G1 Corpus CSV  : {p1['sealed_marked_rows']}",
        f"  - Purchaser CI Guard Execution            : {'PASS' if p1['guard_passed'] else 'FAIL'}",
        f"  - CI Guard Output                         : {p1['guard_output']}",
        f"  - Part 1 Verdict                          : {'PASSED' if p1['part1_passed'] else 'FAILED'}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 2] EXTERNAL ISOLATED REPO (sealed-eval-repo / SUB03) ACL & READ/CLONE LOG AUDIT (NO-MOCK)",
        "  - Zero-Access Enforced Subjects (SoD)     : [S2] Quoc Hung (Integration), [S3] Yen Nhi (Retrieval/App)",
        "  - Authorized Custodians                   : [S4] Quy Hai (Quality Lead), [P5] Anh Khoa (Privacy & Security Owner)",
        f"  - External ACL Log Verification Status    : [{part2_status}]",
        f"  - Detail                                  : {part2_detail}",
        "---------------------------------------------------------------------------------------------------------",
        f"OVERALL GATE G1 SEALED ACL VERDICT        : PART1={'PASSED' if p1['part1_passed'] else 'FAILED'} | PART2={part2_status} (ZERO MOCK DATA USED)",
    ]

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Da ghi log kiem toan CKPA-79: {log_path}")

    if args.strict_external and part2_status != "PASS_VERIFIED_ZERO_S2_S3_ACCESS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()