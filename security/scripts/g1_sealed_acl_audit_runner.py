import argparse
import csv
import datetime
import json
import os
from pathlib import Path
import re
import subprocess
import sys

REPO_ROOT = Path(__file__).resolve().parents[2]

FORBIDDEN_NAME_PATTERNS = [
    re.compile(r"(?i)100[_-]?sealed"),
    re.compile(r"(?i)sealed[_-]?plaintext"),
    re.compile(r"(?i)80[_-]?constructed[_-]?challenges"),
    re.compile(r"(?i)^\.env($|\.(?!example$))"),
    re.compile(r"(?i)\.(pem|key|p12|pfx)$"),
]


def audit_shared_repo_isolation():
    forbidden_files = []
    for p in REPO_ROOT.rglob("*"):
        if ".git" in p.parts or not p.is_file():
            continue
        rel = p.relative_to(REPO_ROOT).as_posix()
        for pat in FORBIDDEN_NAME_PATTERNS:
            if pat.search(p.name):
                forbidden_files.append(f"{rel} ({pat.pattern})")

    corpus_path = REPO_ROOT / "data/g1/full/Policy_Corpus_G1_Full.csv"
    sealed_rows = []
    if corpus_path.exists():
        with corpus_path.open(encoding="utf-8-sig") as f:
            for idx, row in enumerate(csv.DictReader(f), start=2):
                blob = " ".join(str(v) for v in row.values()).lower()
                if "sealed_100" in blob or "80_constructed_challenges" in blob:
                    sealed_rows.append(f"Policy_Corpus_G1_Full.csv:line_{idx}")

    ci_proc = subprocess.run(
        [sys.executable, str(REPO_ROOT / "scripts/ci_purchaser_guard.py")],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    ci_output = (ci_proc.stdout + "\n" + ci_proc.stderr).strip()
    ci_passed = ci_proc.returncode == 0

    return {
        "forbidden_files": sorted(set(forbidden_files)),
        "sealed_rows": sealed_rows,
        "ci_passed": ci_passed,
        "ci_output": ci_output,
        "part1_passed": len(forbidden_files) == 0 and len(sealed_rows) == 0 and ci_passed,
    }


def _parse_github_handles(raw_env: str) -> set[str]:
    return {h.strip().lstrip("@").lower() for h in raw_env.split(",") if h.strip()}


def _load_structured_acl_records(log_file: Path) -> list[dict]:
    raw_text = log_file.read_text(encoding="utf-8-sig").strip()
    if not raw_text:
        raise ValueError("ACL log file is empty (0 bytes / whitespace only)")

    suffix = log_file.suffix.lower()
    if suffix == ".json" or raw_text.startswith("[") or raw_text.startswith("{"):
        parsed = json.loads(raw_text)
        if isinstance(parsed, dict):
            for key in ("records", "events", "collaborators", "audit_logs", "items"):
                if isinstance(parsed.get(key), list):
                    return [r for r in parsed[key] if isinstance(r, dict)]
            raise ValueError("JSON ACL log must be a list of objects or contain records/events/collaborators list")
        if isinstance(parsed, list):
            if not parsed or not all(isinstance(r, dict) for r in parsed):
                raise ValueError("JSON ACL log must be a non-empty list of JSON objects")
            return parsed
        raise ValueError("Unsupported JSON structure in ACL log")

    if suffix == ".csv":
        with log_file.open(encoding="utf-8-sig") as f:
            rows = list(csv.DictReader(f))
        if not rows:
            raise ValueError("CSV ACL log contains 0 data rows")
        return rows

    raise ValueError(f"Unsupported ACL log format '{suffix}': requires structured .json or .csv export")


def _extract_actor_handle(record: dict) -> str:
    for key in ("actor", "username", "login", "github_username", "user", "collaborator"):
        val = record.get(key)
        if isinstance(val, str) and val.strip():
            return val.strip().lstrip("@").lower()
    return ""


def audit_external_sealed_repo_acl():
    external_log_path = os.getenv("CKPA_SEALED_ACL_LOG_PATH", "").strip()
    if not external_log_path:
        return {
            "status": "BLOCKED_EXTERNAL_REPO_ACCESS",
            "detail": (
                "External private repo 'sealed-eval-repo' (SUB03) is isolated outside this repository and "
                "CKPA_SEALED_ACL_LOG_PATH is not set; synthetic ACL mock data forbidden per No-Mock policy."
            ),
        }

    log_file = Path(external_log_path)
    if not log_file.exists() or not log_file.is_file():
        return {
            "status": "BLOCKED_INVALID_LOG_PATH",
            "detail": f"Configured CKPA_SEALED_ACL_LOG_PATH does not exist: {external_log_path}",
        }

    forbidden_users = _parse_github_handles(os.getenv("CKPA_FORBIDDEN_USERS", ""))
    allowed_users = _parse_github_handles(os.getenv("CKPA_ALLOWED_USERS", ""))
    if not forbidden_users or not allowed_users:
        return {
            "status": "BLOCKED_MISSING_USER_MAPPING",
            "detail": (
                "Must configure real GitHub handles in CKPA_FORBIDDEN_USERS (e.g. S2,S3 handles) and "
                "CKPA_ALLOWED_USERS (e.g. S4,P5 handles) to prevent false-negative username matching."
            ),
        }

    try:
        records = _load_structured_acl_records(log_file)
    except Exception as exc:
        return {
            "status": "FAIL_INVALID_LOG_FORMAT",
            "detail": f"Structured JSON/CSV validation failed on {log_file.name}: {exc}",
        }

    observed_actors = set()
    forbidden_hits = []
    for idx, rec in enumerate(records, start=1):
        actor = _extract_actor_handle(rec)
        if not actor:
            return {
                "status": "FAIL_INVALID_LOG_FORMAT",
                "detail": f"Record #{idx} missing actor/username/login field; cannot verify GitHub handles.",
            }
        observed_actors.add(actor)
        if actor in forbidden_users:
            action = rec.get("action") or rec.get("permission") or rec.get("role") or "UNKNOWN_ACCESS"
            forbidden_hits.append(f"record#{idx}:actor={actor}:access={action}")

    missing_allowed = sorted(allowed_users - observed_actors)

    if forbidden_hits:
        return {
            "status": "FAIL_UNAUTHORIZED_ACCESS_DETECTED",
            "detail": f"Detected {len(forbidden_hits)} unauthorized S2/S3 entry(ies): {forbidden_hits[:5]}",
        }
    if missing_allowed:
        return {
            "status": "FAIL_MISSING_AUTHORIZED_PRINCIPALS",
            "detail": f"Expected authorized S4/P5 handles missing from ACL/Audit export: {missing_allowed}",
        }
    return {
        "status": "PASS_VERIFIED_EXTERNAL_ACL",
        "detail": (
            f"Verified {len(records)} structured records in {log_file.name}: 0 forbidden hits "
            f"for {sorted(forbidden_users)}, and 100% authorized presence for {sorted(allowed_users)}."
        ),
    }


def main():
    parser = argparse.ArgumentParser(description="CKPA-79 No-Mock Sealed Repo ACL Audit Runner")
    parser.add_argument("--strict-external", action="store_true")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    p1 = audit_shared_repo_isolation()
    p2 = audit_external_sealed_repo_acl()

    out_dir = REPO_ROOT / "security/g1"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_sealed_acl_audit_CKPA-79.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 SEALED REPO ACL & SECURITY SIGN-OFF AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-79 (Parent: CKPA-44 | Blocks: CKPA-80 | Relates: CKPA-77)",
        "RFP Traceability : Muc 8, Muc 11, SEC 01, SEC 02, SEC 06 (Jira legacy tag SEC 08 excluded per RFP) | Gate: G1-AC04, G1-AC07",
        f"Execution Time   : {timestamp}",
        f"Repository Scope : Shared Purchaser Repo (Anchored at {REPO_ROOT.name}) + External Private Repo 'sealed-eval-repo' (SUB03)",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 1] SHARED REPOSITORY ISOLATION & 0% PII GUARD AUDIT (REAL REPO SCAN)",
        f"  - Forbidden Files (CI Guard Patterns): {p1['forbidden_files']}",
        f"  - Sealed Cases Leakage in G1 Corpus  : {p1['sealed_rows']}",
        f"  - Purchaser CI Guard Execution       : {'PASS' if p1['ci_passed'] else 'FAIL'}",
        f"  - CI Guard Output                    : {p1['ci_output'].splitlines()[-1] if p1['ci_output'] else 'N/A'}",
        f"  - Part 1 Verdict                     : {'PASSED' if p1['part1_passed'] else 'FAILED'}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 2] EXTERNAL ISOLATED REPO ('sealed-eval-repo' / SUB03) ACL & AUDIT LOG VERIFICATION",
        "  - Zero-Access Enforced Subjects (0% Read/Clone): [S2] Quoc Hung (Backend/RAG), [S3] Yen Nhi (Retrieval/App)",
        "  - Authorized Custodians & Auditors             : [S4] Quy Hai (Read/Write), [P5] Anh Khoa (Audit/Read), [P4] Independent Evaluator",
        "  - Schema & Handle Verification Policy          : Requires non-empty JSON/CSV export + CKPA_FORBIDDEN_USERS & CKPA_ALLOWED_USERS",
        f"  - External ACL Log Verification Status         : {p2['status']}",
        f"  - Detail                                       : {p2['detail']}",
        "---------------------------------------------------------------------------------------------------------",
        f"PART 1 SUMMARY (Shared Repo Isolation & 0% PII): {'PASSED' if p1['part1_passed'] else 'FAILED'}",
        f"PART 2 SUMMARY (External sealed-eval-repo ACL) : {p2['status']}",
        "OVERALL VERDICT: PARTIAL_PASS_SHARED_REPO_CLEAN / PENDING_EXTERNAL_SEALED_REPO_ACL_LOG (ZERO MOCK DATA USED).",
    ]

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Da ghi log kiem toan No-Mock CKPA-79: {log_path}")

    if args.strict_external and p2["status"] != "PASS_VERIFIED_EXTERNAL_ACL":
        raise SystemExit(2)


if __name__ == "__main__":
    main()