import argparse
import csv
import datetime
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

REPO_ROOT = Path(__file__).resolve().parents[2]

LIVE_TEST_MATRIX = [
    {
        "tc_id": "TC-RBAC-01",
        "title": "Vertical Escalation & Cross-BU Isolation",
        "role": "reader",
        "token_env": "CKPA_READER_BEARER_TOKEN",
        "endpoint": "/api/v1/answer/query",
        "method": "POST",
        "expected_status": 403,
        "require_non_empty_body": False,
    },
    {
        "tc_id": "TC-CACHE-02",
        "title": "Cache Authorization Bypass (Steward Warm -> Reader Hit)",
        "role": "steward->reader",
        "warmup_token_env": "CKPA_STEWARD_BEARER_TOKEN",
        "token_env": "CKPA_READER_BEARER_TOKEN",
        "warmup_endpoint": "/api/v1/answer/query",
        "endpoint": "/api/v1/answer/query",
        "method": "POST",
        "expected_status": 403,
        "require_non_empty_body": False,
    },
    {
        "tc_id": "TC-REV-03",
        "title": "Post-Revocation Stale Access (Withdraw -> Reader Query)",
        "role": "policy_owner->reader",
        "warmup_token_env": "CKPA_POLICY_OWNER_BEARER_TOKEN",
        "token_env": "CKPA_READER_BEARER_TOKEN",
        "warmup_endpoint": "/api/v1/policies/POL-001/withdraw",
        "endpoint": "/api/v1/answer/query",
        "method": "POST",
        "expected_status": 403,
        "require_non_empty_body": False,
    },
    {
        "tc_id": "TC-LOG-04",
        "title": "Audit Log Redaction & Zero Sensitive Leakage",
        "role": "administrator",
        "token_env": "CKPA_ADMIN_BEARER_TOKEN",
        "endpoint": "/api/v1/audit/logs?limit=10",
        "method": "GET",
        "expected_status": 200,
        "require_non_empty_body": True,
    },
]


def verify_g1_corpus_prerequisites(repo_root: Path = REPO_ROOT):
    corpus_path = repo_root / "data/g1/full/Policy_Corpus_G1_Full.csv"
    if not corpus_path.exists():
        raise FileNotFoundError(f"Missing required G1 corpus: {corpus_path}")

    allowed_policies = set()
    allowed_statuses = set()
    with corpus_path.open(encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            src = (row.get("source_ref") or "").strip()
            if src:
                allowed_policies.add(src.split("/")[0].split("#")[0].strip())
            st = (row.get("status") or "").strip()
            if st:
                allowed_statuses.add(st)

    required_policies = {"POL-001", "POL-002", "POL-003"}
    if not required_policies.issubset(allowed_policies):
        raise ValueError(f"Corpus missing expected G1 policies {required_policies}: found {allowed_policies}")

    return sorted(allowed_policies), sorted(allowed_statuses)


def _http_call(url: str, method: str, token: str, payload: dict | None = None):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.status, resp.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as err:
        return err.code, err.read().decode("utf-8", errors="replace")


def execute_live_probe(base_url: str, tc: dict):
    if not base_url:
        return {
            "status": "BLOCKED_NO_STAGING_ENDPOINT",
            "detail": "CKPA_STAGING_API_BASE_URL not configured; No-Mock policy forbids synthetic API results.",
        }

    token = os.getenv(tc["token_env"], "").strip()
    if not token:
        return {
            "status": "BLOCKED_MISSING_CREDENTIAL",
            "detail": f"Missing environment credential {tc['token_env']}.",
        }

    # Build AnswerQueryRequest conforming strictly to DAT 04 6D scope contract
    query_payload = {
        "query": "Chinh sach chiet khau dai ly cap 1 ap dung muc nao?",
        "scope": "bu=Commercial|region=VN|product_line=CRM_Core|channel=Direct|customer_segment=Enterprise|effective_date=2026-11-24",
    }

    if "warmup_token_env" in tc:
        warmup_token = os.getenv(tc["warmup_token_env"], "").strip()
        if not warmup_token:
            return {
                "status": "BLOCKED_MISSING_PREREQUISITE_CREDENTIAL",
                "detail": f"Missing step-1 credential {tc['warmup_token_env']}.",
            }
        step1_payload = {} if tc["warmup_endpoint"].endswith("/withdraw") else query_payload
        status1, body1 = _http_call(base_url.rstrip("/") + tc["warmup_endpoint"], "POST", warmup_token, step1_payload)
        if not (200 <= status1 < 300):
            return {
                "status": "FAIL_STEP1_FAILED",
                "detail": f"Step 1 ({tc['warmup_endpoint']}) returned HTTP {status1} (expected 2xx); body={body1[:160]}",
            }

    target_payload = query_payload if tc["method"] == "POST" else None
    target_status, target_body = _http_call(base_url.rstrip("/") + tc["endpoint"], tc["method"], token, target_payload)

    forbidden_markers = ["POL-002_CONFIDENTIAL_BODY", "SECRET_DISCOUNT_TIER_99", "BEGIN PRIVATE KEY"]
    leaked = [m for m in forbidden_markers if m in target_body]
    if leaked:
        return {
            "status": "FAIL_LEAKAGE_DETECTED",
            "detail": f"HTTP {target_status} leaked restricted markers: {leaked}",
        }

    expected_status = tc["expected_status"]
    if target_status != expected_status:
        return {
            "status": "FAIL_UNEXPECTED_STATUS",
            "detail": f"Expected HTTP {expected_status}, got HTTP {target_status}; body={target_body[:160]}",
        }

    if tc.get("require_non_empty_body") and not target_body.strip():
        return {
            "status": "FAIL_EMPTY_AUDIT_BODY",
            "detail": f"HTTP {target_status} returned empty body for {tc['endpoint']}; cannot verify audit log redaction.",
        }

    return {
        "status": "PASS_VERIFIED",
        "detail": f"Live API verified HTTP {target_status} (expected {expected_status}) with 0 restricted leakage.",
    }


def compute_overall_verdict(part1_passed: bool, passed_count: int, failed_count: int, blocked_count: int) -> str:
    if not part1_passed or failed_count > 0:
        return "FAIL"
    if blocked_count == 0 and passed_count > 0:
        return "PASS"
    if part1_passed and blocked_count > 0:
        return "PARTIAL_PASS"
    return "BLOCKED"


def main():
    parser = argparse.ArgumentParser(description="CKPA-70 No-Mock RBAC/Cache/Revocation/Audit Audit Runner")
    parser.add_argument("--strict-live", action="store_true", help="Exit non-zero if any live check is blocked or failed")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    base_url = os.getenv("CKPA_STAGING_API_BASE_URL", "").strip()

    try:
        policies, statuses = verify_g1_corpus_prerequisites()
        part1_passed = True
        part1_error = ""
    except Exception as exc:
        policies, statuses = [], []
        part1_passed = False
        part1_error = str(exc)

    results = []
    for tc in LIVE_TEST_MATRIX:
        outcome = execute_live_probe(base_url, tc)
        results.append({**tc, **outcome})

    passed_count = sum(1 for r in results if r["status"] == "PASS_VERIFIED")
    failed_count = sum(1 for r in results if r["status"].startswith("FAIL_"))
    blocked_count = sum(1 for r in results if r["status"].startswith("BLOCKED_"))
    overall = compute_overall_verdict(part1_passed, passed_count, failed_count, blocked_count)

    out_dir = REPO_ROOT / "security/g1"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_rbac_failclosed_audit_CKPA-70.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 RBAC / CACHE / FAIL-CLOSED AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-70 (Parent: CKPA-44 | Relates: CKPA-80, CKPA-57)",
        "RFP Traceability : Muc 8, Muc 11, SEC 01, SEC 02, SEC 06, DAT 04, KNW 03 | Gate: G1-AC04, G1-AC07",
        f"Execution Time   : {timestamp}",
        f"Target Base URL  : {base_url if base_url else 'NOT_CONFIGURED (CKPA_STAGING_API_BASE_URL unset)'}",
        f"Policy Mode      : STRICT_NO_MOCK (0% simulated HTTP responses)",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 1] REAL G1 CORPUS & METADATA PREREQUISITE VERIFICATION (data/g1/full/Policy_Corpus_G1_Full.csv)",
        f"  - Corpus Verification Status : {'PASS' if part1_passed else 'FAIL (' + part1_error + ')'}",
        f"  - Verified Policies          : {policies}",
        f"  - Verified Statuses          : {statuses}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 2] LIVE STAGING API SECURITY PROBES (RBAC / CACHE ISOLATION / REVOCATION / AUDIT LOG REDACTION)",
    ]
    for r in results:
        lines.append(
            f"  - {r['tc_id']} | Role: {r['role']:<20} | {r['method']} {r['endpoint']:<32} | Expected: {r['expected_status']} | Status: {r['status']} | {r['detail']}"
        )

    lines.extend([
        "---------------------------------------------------------------------------------------------------------",
        f"PART 1 SUMMARY : {'PASS' if part1_passed else 'FAIL'}",
        f"PART 2 SUMMARY : {passed_count}/{len(results)} PASS_VERIFIED, {failed_count}/{len(results)} FAIL, {blocked_count}/{len(results)} BLOCKED",
        f"OVERALL VERDICT: {overall}",
    ])

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Da ghi log kiem toan No-Mock CKPA-70 (OVERALL={overall}): {log_path}")

    if overall == "FAIL":
        raise SystemExit(1)
    if args.strict_live and overall != "PASS":
        raise SystemExit(2)


if __name__ == "__main__":
    main()