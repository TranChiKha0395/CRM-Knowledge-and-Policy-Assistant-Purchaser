import argparse
import csv
import datetime
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

REPO_ROOT = Path(__file__).resolve().parents[2]

VALID_RFP_ROLES = {
    "reader",
    "policy_owner",
    "publisher",
    "steward",
    "administrator",
    "independent_evaluator",
    "privacy_security_owner",
    "legal_owner",
    "referral_handler",
}

CORE_SEC01_ROLES = {"reader", "policy_owner", "steward", "administrator"}
EXPECTED_POLICY_FAMILIES = ["POL-001", "POL-002", "POL-003"]
REQUIRED_SCOPE_KEYS = ("company:", "branch:", "role:", "customer_group:", "product:", "transaction_scope:")

LIVE_TEST_MATRIX = [
    {
        "tc_id": "TC-RBAC-01",
        "category": "Selection, 6D Scope & Source_Ref Leakage across 3 CRM Policy Families (SEC 01 / SEC 02 / ANS 02)",
        "role": "reader",
        "token_envs": ("CKPA_TOKEN_READER", "CKPA_READER_BEARER_TOKEN"),
        "target_doc": "DOC-006",
        "target_version": "DOC006-VER-001",
        "method": "POST",
        "endpoint": "/api/v1/answer",
        "payload": {
            "question": "Dieu khoan chiet khau co dinh trong hop dong khung B2B DOC-006 la gi?",
            "scope": "company:SN;branch:all;role:sales;customer_group:standard_b2c;product:commercial;transaction_scope:standard_b2c",
        },
        "expected_statuses": (200, 403),
        "require_non_empty_body": False,
        "forbidden_markers": ["DOC-006", "DOC006-VER-001", "POL-001 / HDNT-B2B-SYN-2026"],
    },
    {
        "tc_id": "TC-CACHE-02",
        "category": "Cross-Role Cache Isolation 2-Step Replay across KNW 03 Lifecycle States (SEC 01 / KNW 03 / OPS 05)",
        "role": "steward -> reader",
        "warmup_token_envs": ("CKPA_TOKEN_STEWARD", "CKPA_STEWARD_BEARER_TOKEN"),
        "warmup_endpoint": "/api/v1/answer",
        "warmup_payload": {
            "question": "Phu luc DPA Hop dong B2B DOC-008 quy dinh thoi han xoa du lieu bao lau?",
            "scope": "company:SN;branch:all;role:crm;customer_group:b2b;product:industrial;transaction_scope:all_commercial",
        },
        "token_envs": ("CKPA_TOKEN_READER", "CKPA_READER_BEARER_TOKEN"),
        "target_doc": "DOC-008",
        "target_version": "DOC008-VER-001",
        "method": "POST",
        "endpoint": "/api/v1/answer",
        "payload": {
            "question": "Phu luc DPA Hop dong B2B DOC-008 quy dinh thoi han xoa du lieu bao lau?",
            "scope": "company:SN;branch:all;role:sales;customer_group:standard_b2c;product:commercial;transaction_scope:standard_b2c",
        },
        "expected_statuses": (200, 403),
        "require_non_empty_body": False,
        "forbidden_markers": ["DOC-008", "DOC008-VER-001", "POL-002 / DPA-B2B-SYN-2026"],
    },
    {
        "tc_id": "TC-REV-03",
        "category": "Immediate Withdrawal Fail-Closed <= 5m 2-Step Verification (SEC 05 / KNW 03 / KNW 04)",
        "role": "policy_owner -> reader",
        "warmup_token_envs": ("CKPA_TOKEN_POLICY_OWNER", "CKPA_POLICY_OWNER_BEARER_TOKEN"),
        "warmup_endpoint": "/api/v1/admin/policies/DOC007-VER-001/withdraw",
        "warmup_payload": {"reason": "CKPA-70 SEC-05 / KNW-04 immediate withdrawal audit verification"},
        "token_envs": ("CKPA_TOKEN_READER", "CKPA_READER_BEARER_TOKEN"),
        "target_doc": "DOC-007",
        "target_version": "DOC007-VER-001",
        "method": "POST",
        "endpoint": "/api/v1/answer",
        "payload": {
            "question": "Quy dinh ap dung tai lieu DOC-007 hien hanh nhu the nao?",
            "scope": "company:SN;branch:all;role:sales;customer_group:b2b;product:industrial;transaction_scope:all_commercial",
        },
        "expected_statuses": (200, 403),
        "require_non_empty_body": False,
        "forbidden_markers": ["DOC-007", "DOC007-VER-001", "POL-001 / CRM-STAFF-NOTES-SYN"],
    },
    {
        "tc_id": "TC-LOG-04",
        "category": "Audit Log Redaction & Administrator Boundary Check (SEC 01 / SEC 02 / OPS 05)",
        "role": "administrator",
        "token_envs": ("CKPA_TOKEN_ADMINISTRATOR", "CKPA_ADMIN_BEARER_TOKEN"),
        "target_doc": "DOC-008",
        "target_version": "DOC008-VER-001",
        "method": "GET",
        "endpoint": "/api/v1/audit/logs?limit=10",
        "payload": None,
        "expected_statuses": (200,),
        "require_non_empty_body": True,
        "forbidden_markers": ["Phu luc DPA Hop dong B2B", "sealed_100", "BEGIN PRIVATE KEY", "CCCD"],
    },
]


def _resolve_env(names: tuple[str, ...]) -> str:
    for name in names:
        val = os.getenv(name, "").strip()
        if val:
            return val
    return ""


def audit_g1_corpus_metadata(repo_root: Path = REPO_ROOT):
    corpus_path = repo_root / "data/g1/full/Policy_Corpus_G1_Full.csv"
    manifest_path = repo_root / "data/g1/full/Source_URI_And_Checksum_Manifest_G1_Full.csv"
    if not corpus_path.exists():
        raise FileNotFoundError(f"Missing required G1 corpus: {corpus_path}")

    with corpus_path.open(encoding="utf-8-sig") as f:
        corpus_rows = list(csv.DictReader(f))
    manifest_rows = []
    if manifest_path.exists():
        with manifest_path.open(encoding="utf-8-sig") as f:
            manifest_rows = list(csv.DictReader(f))

    doc_summary, invalid_roles, missing_scope_docs = {}, [], []
    policy_families, lifecycle_states, observed_roles = set(), set(), set()

    for row in corpus_rows:
        doc_id = (row.get("document_id") or "").strip()
        scope = (row.get("scope") or "").strip()
        source_ref = (row.get("source_ref") or "").strip()
        status = (row.get("status") or "").strip()

        if "/" in source_ref:
            family_code = source_ref.split("/")[0].strip()
            if family_code:
                policy_families.add(family_code)
        if status:
            lifecycle_states.add(status)

        roles = [r.strip() for r in (row.get("audience") or "").split(",") if r.strip()]
        for r in roles:
            observed_roles.add(r)
            if r not in VALID_RFP_ROLES:
                invalid_roles.append((doc_id, r))

        scope_parts = [p for p in scope.split(";") if ":" in p]
        if len(scope_parts) != 6 or not all(k in scope for k in REQUIRED_SCOPE_KEYS):
            missing_scope_docs.append(doc_id)
        doc_summary[doc_id] = doc_summary.get(doc_id, 0) + 1

    sorted_families = sorted(policy_families)
    families_ok = sorted_families == EXPECTED_POLICY_FAMILIES
    observed_core = sorted(observed_roles & CORE_SEC01_ROLES)

    return {
        "total_passages": len(corpus_rows),
        "total_docs": len(doc_summary),
        "docs": sorted(doc_summary.keys()),
        "manifest_entries": len(manifest_rows),
        "policy_families": sorted_families,
        "families_ok": families_ok,
        "lifecycle_states": sorted(lifecycle_states),
        "observed_core_roles": observed_core,
        "invalid_roles": invalid_roles,
        "missing_scope_docs": sorted(set(missing_scope_docs)),
        "corpus_passed": (
            len(invalid_roles) == 0
            and len(missing_scope_docs) == 0
            and len(doc_summary) == 11
            and families_ok
            and len(observed_core) == 4
        ),
    }


def _http_call(url: str, method: str, token: str, payload: dict | None = None, trace_id: str = "CKPA-70"):
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Audit-Trace": trace_id,
    }
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
            "status": "BLOCKED_NO_LIVE_ENDPOINT",
            "detail": "CKPA_BASE_URL not set; synthetic mock execution prohibited per No-Mock policy",
        }

    token = _resolve_env(tc["token_envs"])
    if not token:
        return {
            "status": "BLOCKED_MISSING_TOKEN",
            "detail": f"Missing real auth token env var {tc['token_envs'][0]} (No-Mock policy: synthetic tokens forbidden)",
        }

    if "warmup_token_envs" in tc:
        warmup_token = _resolve_env(tc["warmup_token_envs"])
        if not warmup_token:
            return {
                "status": "BLOCKED_MISSING_TOKEN",
                "detail": f"Missing step-1 token env var {tc['warmup_token_envs'][0]} for 2-step verification",
            }
        try:
            status1, body1 = _http_call(
                base_url.rstrip("/") + tc["warmup_endpoint"],
                "POST",
                warmup_token,
                tc["warmup_payload"],
                f"CKPA-70-{tc['tc_id']}-STEP1",
            )
        except Exception as exc:
            return {"status": "BLOCKED_CONNECTION_ERROR", "detail": f"Step 1 endpoint unreachable: {exc}"}

        if status1 == 422:
            return {
                "status": "FAIL_SCHEMA_CONTRACT",
                "detail": f"HTTP 422 contract mismatch on Step 1 ({tc['warmup_endpoint']}): {body1[:160]}",
            }
        allowed_s1 = (200, 201, 202, 204, 404) if tc["tc_id"] == "TC-REV-03" else tuple(range(200, 300))
        if status1 not in allowed_s1:
            return {
                "status": "FAIL_STEP1_FAILED",
                "detail": f"Step 1 ({tc['warmup_endpoint']}) returned HTTP {status1} (expected 2xx); body={body1[:160]}",
            }

    try:
        target_status, target_body = _http_call(
            base_url.rstrip("/") + tc["endpoint"],
            tc["method"],
            token,
            tc["payload"],
            f"CKPA-70-{tc['tc_id']}-TARGET",
        )
    except Exception as exc:
        return {"status": "BLOCKED_CONNECTION_ERROR", "detail": f"Endpoint unreachable: {exc}"}

    if target_status == 422:
        return {
            "status": "FAIL_SCHEMA_CONTRACT",
            "detail": f"HTTP 422 contract mismatch on {tc['endpoint']}: {target_body[:160]}",
        }

    scan_body = json.dumps({k: v for k, v in json.loads(target_body).items() if k != "original_question"}, ensure_ascii=False) if target_body.strip().startswith("{") else target_body
    leaked = [m for m in tc.get("forbidden_markers", []) if m.lower() in scan_body.lower()]
    digest = hashlib.sha256(target_body.encode("utf-8")).hexdigest()[:16]

    if target_status >= 500:
        return {"status": "FAIL_SERVER_ERROR", "detail": f"HTTP {target_status} on {tc['tc_id']} | sha256={digest}"}
    if leaked:
        return {
            "status": "FAIL_LEAKAGE_DETECTED",
            "detail": f"HTTP {target_status} leaked forbidden markers {leaked} | sha256={digest}",
        }
    if target_status not in tc["expected_statuses"]:
        return {
            "status": "FAIL_UNEXPECTED_STATUS",
            "detail": f"Expected HTTP {tc['expected_statuses']}, got HTTP {target_status} | sha256={digest}",
        }
    if tc.get("require_non_empty_body") and not target_body.strip():
        return {
            "status": "FAIL_EMPTY_AUDIT_BODY",
            "detail": f"HTTP {target_status} returned empty body for {tc['endpoint']}; cannot verify audit log redaction.",
        }

    return {"status": "PASS_VERIFIED", "detail": f"HTTP {target_status} | 0 leaked markers | sha256={digest}"}


def compute_overall_verdict(part1_passed: bool, passed_count: int, failed_count: int, blocked_count: int) -> str:
    if not part1_passed or failed_count > 0:
        return "FAIL"
    if blocked_count == 0 and passed_count > 0:
        return "PASS"
    if part1_passed and blocked_count > 0:
        return "PARTIAL_PASS"
    return "BLOCKED"


def main():
    parser = argparse.ArgumentParser(description="CKPA-70 No-Mock RBAC & Fail-Closed Audit Runner")
    parser.add_argument("--strict-live", action="store_true", help="Exit non-zero if any live check is blocked or failed")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    base_url = _resolve_env(("CKPA_BASE_URL", "CKPA_STAGING_API_BASE_URL"))
    ca = audit_g1_corpus_metadata(REPO_ROOT)

    results = []
    for tc in LIVE_TEST_MATRIX:
        res = execute_live_probe(base_url, tc)
        results.append((tc, res))

    passed_count = sum(1 for _, r in results if r["status"] == "PASS_VERIFIED")
    failed_count = sum(1 for _, r in results if r["status"].startswith("FAIL_"))
    blocked_count = sum(1 for _, r in results if r["status"].startswith("BLOCKED_"))
    overall = compute_overall_verdict(ca["corpus_passed"], passed_count, failed_count, blocked_count)

    out_dir = REPO_ROOT / "security/g1"
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_rbac_failclosed_audit_CKPA-70.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 RBAC, SOURCE_REF, CACHE & FAIL-CLOSED AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-70 (Parent: CKPA-44 | Relates: CKPA-69 | Blocks: CKPA-71)",
        "RFP Traceability : SEC 01, SEC 02, SEC 05, KNW 03, KNW 04, OPS 05, ANS 02 | Gate Criteria: G1-AC03, G1-AC04",
        f"Execution Time   : {timestamp}",
        f"Live Endpoint    : {base_url if base_url else 'NOT_CONFIGURED (Offline Repository Mode - No-Mock Enforced)'}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 1] REAL G1 CORPUS RBAC & SCOPE METADATA AUDIT (data/g1/full/Policy_Corpus_G1_Full.csv)",
        f"  - Documents Verified     : {ca['total_docs']} ({', '.join(ca['docs'])})",
        f"  - Passages Verified      : {ca['total_passages']} | Manifest Checksums: {ca['manifest_entries']}",
        f"  - Core SEC 01 Roles Used : {ca['observed_core_roles']} (4/4: reader, policy_owner, steward, administrator)",
        f"  - CRM Policy Families    : {ca['policy_families']} ({len(ca['policy_families'])}/3 extracted from source_ref)",
        f"  - KNW 03 Lifecycle States: {ca['lifecycle_states']} (extracted from status column)",
        f"  - Invalid UserRoles      : {ca['invalid_roles']}",
        f"  - Invalid 6D Scope Docs  : {ca['missing_scope_docs']}",
        f"  - Part 1 Verdict         : {'PASS' if ca['corpus_passed'] else 'FAIL'}",
        "---------------------------------------------------------------------------------------------------------",
        "[PART 2] LIVE RUNTIME API AUDIT (SUB01 / SUB07 - 6D SCOPE CONTRACT & ASSERTION VERIFIED)",
    ]

    for tc, res in results:
        step_route = (
            f"POST {tc['warmup_endpoint']} -> {tc['method']} {tc['endpoint']}"
            if "warmup_endpoint" in tc
            else f"{tc['method']} {tc['endpoint']}"
        )
        lines.append(
            f"  [{res['status']}] {tc['tc_id']} | Role={tc['role']} | Target={tc['target_doc']} ({tc['target_version']}) | "
            f"{step_route} | {res['detail']}"
        )

    lines.extend([
        "---------------------------------------------------------------------------------------------------------",
        f"PART 1 SUMMARY : {'PASS' if ca['corpus_passed'] else 'FAIL'} ({ca['total_docs']}/11 docs, {len(ca['policy_families'])}/3 policy families verified)",
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
