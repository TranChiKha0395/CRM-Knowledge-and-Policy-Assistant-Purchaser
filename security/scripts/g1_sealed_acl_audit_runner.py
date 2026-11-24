import argparse
import csv
import datetime
import hashlib
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

REQUIRED_LOG_FIELDS = {"record_type", "repository", "actor", "permission_or_action", "outcome"}
WRITE_PERMISSIONS = {"write", "maintain", "admin"}
READ_OR_AUDIT_PERMISSIONS = {"read", "triage", "audit", "write", "maintain", "admin"}
DENIED_OUTCOMES = {"denied", "blocked", "forbidden", "rejected", "403"}
ALLOWED_OUTCOMES = {"allowed", "granted", "success", "active", "200"}


def audit_shared_repo_isolation(repo_root: Path = REPO_ROOT):
    forbidden_files = []
    symlink_violations = []
    sealed_content_hits = []

    required_corpus = repo_root / "data/g1/full/Policy_Corpus_G1_Full.csv"
    corpus_exists = required_corpus.exists() and required_corpus.is_file()

    for p in repo_root.rglob("*"):
        if ".git" in p.parts:
            continue
        rel = p.relative_to(repo_root).as_posix()

        if p.is_symlink():
            try:
                target = p.resolve()
                if not str(target).startswith(str(repo_root.resolve())):
                    symlink_violations.append(f"{rel} -> {target}")
            except Exception as exc:
                symlink_violations.append(f"{rel} (broken symlink: {exc})")
            continue

        if not p.is_file():
            continue

        for pat in FORBIDDEN_NAME_PATTERNS:
            if pat.search(p.name):
                forbidden_files.append(f"{rel} ({pat.pattern})")

        is_governance_spec = rel.startswith("policy/") or rel.endswith("_Matrix.csv") or rel.endswith("_Checklist.csv")
        if not is_governance_spec and p.suffix.lower() in {".csv", ".json", ".txt", ".tsv"}:
            try:
                with p.open(encoding="utf-8-sig", errors="replace") as f:
                    for idx, line in enumerate(f, start=1):
                        low = line.lower()
                        if "sealed_100" in low or "80_constructed_challenges" in low:
                            if "hidden" not in low and "redacted" not in low:
                                sealed_content_hits.append(f"{rel}:line_{idx}")
            except Exception as exc:
                sealed_content_hits.append(f"{rel}:read_error({exc})")

    ci_script = repo_root / "scripts/ci_purchaser_guard.py"
    if not ci_script.exists():
        ci_passed = False
        ci_output = "FAIL: scripts/ci_purchaser_guard.py not found"
    else:
        ci_proc = subprocess.run(
            [sys.executable, str(ci_script)],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        ci_output = (ci_proc.stdout + "\n" + ci_proc.stderr).strip()
        ci_passed = (ci_proc.returncode == 0) and ("PASSED:" in ci_output)

    part1_passed = (
        corpus_exists
        and len(forbidden_files) == 0
        and len(symlink_violations) == 0
        and len(sealed_content_hits) == 0
        and ci_passed
    )

    return {
        "corpus_exists": corpus_exists,
        "forbidden_files": sorted(set(forbidden_files)),
        "symlink_violations": sorted(set(symlink_violations)),
        "sealed_content_hits": sorted(set(sealed_content_hits)),
        "ci_passed": ci_passed,
        "ci_output": ci_output,
        "part1_passed": part1_passed,
    }


def _parse_handles(raw_env: str) -> set[str]:
    return {h.strip().lstrip("@").lower() for h in raw_env.split(",") if h.strip()}


def _load_structured_acl_records(log_file: Path) -> tuple[list[dict], str]:
    raw_bytes = log_file.read_bytes()
    if not raw_bytes.strip():
        raise ValueError("ACL export file is empty (0 bytes / whitespace only)")
    sha256_digest = hashlib.sha256(raw_bytes).hexdigest()
    raw_text = raw_bytes.decode("utf-8-sig").strip()

    suffix = log_file.suffix.lower()
    if suffix == ".json" or raw_text.startswith("[") or raw_text.startswith("{"):
        parsed = json.loads(raw_text)
        if isinstance(parsed, dict):
            for key in ("records", "events", "collaborators", "audit_logs", "items"):
                if isinstance(parsed.get(key), list):
                    records = [r for r in parsed[key] if isinstance(r, dict)]
                    break
            else:
                raise ValueError("JSON ACL export must contain a list of record objects")
        elif isinstance(parsed, list):
            if not parsed or not all(isinstance(r, dict) for r in parsed):
                raise ValueError("JSON ACL export must be a non-empty list of objects")
            records = parsed
        else:
            raise ValueError("Unsupported JSON root type")
    elif suffix == ".csv":
        with log_file.open(encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)
            headers = set(reader.fieldnames or [])
            missing_headers = sorted(REQUIRED_LOG_FIELDS - headers)
            if missing_headers:
                raise ValueError(f"CSV missing required headers: {missing_headers}")
            records = list(reader)
        if not records:
            raise ValueError("CSV ACL export contains 0 data rows")
    else:
        raise ValueError(f"Unsupported file format '{suffix}': requires structured .json or .csv export")

    return records, sha256_digest


def audit_external_sealed_repo_acl():
    external_log_path = os.getenv("CKPA_SEALED_ACL_LOG_PATH", "").strip()
    if not external_log_path:
        return {
            "status": "BLOCKED",
            "code": "BLOCKED_EXTERNAL_REPO_ACCESS",
            "sha256": "N/A",
            "source_file": "NOT_PROVIDED",
            "detail": (
                "External private repo 'sealed-eval-repo' (SUB03) is isolated outside this repository and "
                "CKPA_SEALED_ACL_LOG_PATH is not set; synthetic mock data forbidden per No-Mock policy."
            ),
        }

    log_file = Path(external_log_path)
    if not log_file.exists() or not log_file.is_file():
        return {
            "status": "BLOCKED",
            "code": "BLOCKED_INVALID_LOG_PATH",
            "sha256": "N/A",
            "source_file": external_log_path,
            "detail": f"Configured CKPA_SEALED_ACL_LOG_PATH does not exist: {external_log_path}",
        }

    forbidden_users = _parse_handles(os.getenv("CKPA_FORBIDDEN_USERS", ""))
    s4_users = _parse_handles(os.getenv("CKPA_S4_USERS", ""))
    p5_users = _parse_handles(os.getenv("CKPA_P5_USERS", ""))
    extra_approved = _parse_handles(os.getenv("CKPA_EXTRA_APPROVED_USERS", ""))
    expected_repo = os.getenv("CKPA_EXPECTED_SEALED_REPO", "sealed-eval-repo").strip().lower()

    if not forbidden_users or not s4_users or not p5_users:
        return {
            "status": "BLOCKED",
            "code": "BLOCKED_MISSING_USER_MAPPING",
            "sha256": "N/A",
            "source_file": log_file.name,
            "detail": (
                "Must set real GitHub handles via CKPA_FORBIDDEN_USERS (S2,S3), CKPA_S4_USERS (S4), "
                "and CKPA_P5_USERS (P5) before validating external ACL export."
            ),
        }

    approved_all = s4_users | p5_users | extra_approved

    try:
        records, sha256_digest = _load_structured_acl_records(log_file)
    except Exception as exc:
        return {
            "status": "FAIL",
            "code": "FAIL_INVALID_LOG_FORMAT",
            "sha256": "N/A",
            "source_file": log_file.name,
            "detail": f"Structured JSON/CSV validation failed: {exc}",
        }

    seen_signatures = set()
    s4_valid_write = set()
    p5_valid_read = set()
    violations = []

    for idx, rec in enumerate(records, start=1):
        missing = sorted(f for f in REQUIRED_LOG_FIELDS if not str(rec.get(f, "")).strip())
        if missing:
            return {
                "status": "FAIL",
                "code": "FAIL_MISSING_REQUIRED_FIELDS",
                "sha256": sha256_digest,
                "source_file": log_file.name,
                "detail": f"Record #{idx} missing required fields: {missing}",
            }

        rec_type = str(rec["record_type"]).strip().lower()
        repo_name = str(rec["repository"]).strip().lower()
        actor = str(rec["actor"]).strip().lstrip("@").lower()
        perm_or_act = str(rec["permission_or_action"]).strip().lower()
        outcome = str(rec["outcome"]).strip().lower()
        source_grant = str(rec.get("grant_source", "direct")).strip().lower()

        sig = (rec_type, repo_name, actor, perm_or_act, outcome, source_grant, str(rec.get("timestamp", "")))
        if sig in seen_signatures:
            return {
                "status": "FAIL",
                "code": "FAIL_DUPLICATE_RECORDS",
                "sha256": sha256_digest,
                "source_file": log_file.name,
                "detail": f"Duplicate record detected at row #{idx}: {sig}",
            }
        seen_signatures.add(sig)

        if repo_name != expected_repo and not repo_name.endswith("/" + expected_repo):
            violations.append(f"row#{idx}:wrong_repo({repo_name}!={expected_repo})")
            continue

        if rec_type in {"collaborator", "team_permission", "org_inherited_permission"}:
            if outcome in ALLOWED_OUTCOMES:
                if actor in forbidden_users:
                    violations.append(f"row#{idx}:forbidden_user_has_permission(actor={actor},perm={perm_or_act},via={source_grant})")
                elif actor not in approved_all:
                    violations.append(f"row#{idx}:unapproved_principal(actor={actor},perm={perm_or_act},via={source_grant})")
                else:
                    if actor in s4_users and perm_or_act in WRITE_PERMISSIONS:
                        s4_valid_write.add(actor)
                    if actor in p5_users and perm_or_act in READ_OR_AUDIT_PERMISSIONS:
                        p5_valid_read.add(actor)
        elif rec_type == "audit_event":
            if actor in forbidden_users and outcome in ALLOWED_OUTCOMES:
                violations.append(f"row#{idx}:forbidden_user_succeeded_action(actor={actor},action={perm_or_act})")
            elif actor not in approved_all and outcome in ALLOWED_OUTCOMES:
                violations.append(f"row#{idx}:unapproved_user_succeeded_action(actor={actor},action={perm_or_act})")
        else:
            violations.append(f"row#{idx}:unknown_record_type({rec_type})")

    if violations:
        return {
            "status": "FAIL",
            "code": "FAIL_ACL_POLICY_VIOLATION",
            "sha256": sha256_digest,
            "source_file": log_file.name,
            "detail": f"Detected {len(violations)} ACL/Audit violation(s): {violations[:5]}",
        }

    if s4_valid_write != s4_users:
        return {
            "status": "FAIL",
            "code": "FAIL_INSUFFICIENT_S4_PERMISSION",
            "sha256": sha256_digest,
            "source_file": log_file.name,
            "detail": f"Missing required Read/Write permission for S4 handles: {sorted(s4_users - s4_valid_write)}",
        }

    if p5_valid_read != p5_users:
        return {
            "status": "FAIL",
            "code": "FAIL_INSUFFICIENT_P5_PERMISSION",
            "sha256": sha256_digest,
            "source_file": log_file.name,
            "detail": f"Missing required Audit/Read permission for P5 handles: {sorted(p5_users - p5_valid_read)}",
        }

    return {
        "status": "PASS",
        "code": "PASS_VERIFIED_EXTERNAL_ACL",
        "sha256": sha256_digest,
        "source_file": log_file.name,
        "detail": (
            f"Verified {len(records)} unique records in '{log_file.name}' (repo={expected_repo}): "
            f"0 unauthorized access for {sorted(forbidden_users)}, verified S4 Write {sorted(s4_valid_write)} "
            f"& P5 Audit/Read {sorted(p5_valid_read)}."
        ),
    }


def compute_overall_verdict(p1_passed: bool, p2_status: str) -> str:
    if not p1_passed or p2_status == "FAIL":
        return "FAIL"
    if p2_status == "PASS":
        return "PASS"
    if p1_passed and p2_status == "BLOCKED":
        return "PARTIAL_PASS"
    return "BLOCKED"


def main():
    parser = argparse.ArgumentParser(description="CKPA-79 No-Mock Sealed Repo ACL Audit Runner")
    parser.add_argument("--strict-external", action="store_true")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    p1 = audit_shared_repo_isolation()
    p2 = audit_external_sealed_repo_acl()
    overall = compute_overall_verdict(p1["part1_passed"], p2["status"])

    out_dir = REPO_ROOT / "security/g1"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_sealed_acl_audit_CKPA-79.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 SEALED REPO ACL & SECURITY SIGN-OFF AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-79 (Parent: CKPA-44 | Blocks: CKPA-80 | Relates: CKPA-77)",
        "RFP Traceability : Muc 8, Muc 11, SEC 01, SEC 02, SEC 06 (Jira legacy tag SEC 08 excluded per RFP) | Gate: G1-AC04, G1-AC07",
        f"Execution Time   : {timestamp}",
        f"Repository Scope : Shared Purchaser Repo ({REPO_ROOT.name}) + External Private Repo 'sealed-eval-repo' (SUB03)",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 1] SHARED REPOSITORY ISOLATION & 0% PII GUARD AUDIT (REAL REPO SCAN)",
        f"  - Required G1 Corpus Present         : {p1['corpus_exists']}",
        f"  - Forbidden Files (CI Guard Patterns): {p1['forbidden_files']}",
        f"  - External Symlink Violations        : {p1['symlink_violations']}",
        f"  - Unredacted Sealed Content Hits     : {p1['sealed_content_hits']}",
        f"  - Purchaser CI Guard Execution       : {'PASS' if p1['ci_passed'] else 'FAIL'}",
        f"  - CI Guard Output                    : {p1['ci_output'].splitlines()[-1] if p1['ci_output'] else 'N/A'}",
        f"  - Part 1 Status                      : {'PASS' if p1['part1_passed'] else 'FAIL'}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 2] EXTERNAL ISOLATED REPO ('sealed-eval-repo' / SUB03) ACL & AUDIT LOG VERIFICATION",
        "  - Zero-Access Enforced Subjects (0% Read/Clone): [S2] Quoc Hung (Backend/RAG), [S3] Yen Nhi (Retrieval/App)",
        "  - Authorized Custodians & Auditors             : [S4] Quy Hai (Read/Write), [P5] Anh Khoa (Audit/Read), [P4] Independent Evaluator",
        f"  - External Export Source File                  : {p2['source_file']}",
        f"  - External Export SHA-256                      : {p2['sha256']}",
        f"  - Part 2 Status                                : {p2['status']} ({p2['code']})",
        f"  - Detail                                       : {p2['detail']}",
        "---------------------------------------------------------------------------------------------------------",
        f"PART 1 SUMMARY : {'PASS' if p1['part1_passed'] else 'FAIL'}",
        f"PART 2 SUMMARY : {p2['status']} ({p2['code']})",
        f"OVERALL VERDICT: {overall}",
    ]

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Da ghi log kiem toan No-Mock CKPA-79 (OVERALL={overall}): {log_path}")

    if overall == "FAIL":
        raise SystemExit(1)
    if args.strict_external and overall != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()