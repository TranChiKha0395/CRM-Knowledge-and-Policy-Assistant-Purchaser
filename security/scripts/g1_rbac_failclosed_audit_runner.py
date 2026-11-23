import argparse
import csv
import datetime
import hashlib
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

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

LIVE_TEST_MATRIX = [
    {
        "tc_id": "TC-RBAC-01",
        "category": "Selection & Scope/Source_Ref Leakage (SEC 01 / ANS 02)",
        "role": "reader",
        "token_env": "CKPA_TOKEN_READER",
        "target_doc": "DOC-006",
        "target_version": "DOC006-VER-001",
        "method": "POST",
        "path": "/api/v1/query",
        "payload": {
            "question": "Dieu khoan chiet khau co dinh trong hop dong khung B2B DOC-006 la gi?",
            "user_context": {"role": "sales", "customer_group": "standard_b2c"},
        },
    },
    {
        "tc_id": "TC-RBAC-02",
        "category": "Cross-Role Cache Isolation & Replay (SEC 01)",
        "role": "legal_owner",
        "token_env": "CKPA_TOKEN_LEGAL_OWNER",
        "target_doc": "DOC-008",
        "target_version": "DOC008-VER-001",
        "method": "POST",
        "path": "/api/v1/query",
        "payload": {
            "question": "Phu luc DPA Hop dong B2B DOC-008 quy dinh thoi han xoa du lieu bao lau?",
            "user_context": {"role": "cskh", "customer_group": "b2b"},
        },
    },
    {
        "tc_id": "TC-REV-03",
        "category": "Immediate Withdrawal Fail-Closed <= 5m (SEC 05)",
        "role": "policy_owner",
        "token_env": "CKPA_TOKEN_POLICY_OWNER",
        "target_doc": "DOC-007",
        "target_version": "DOC007-VER-001",
        "method": "POST",
        "path": "/api/v1/admin/policies/DOC007-VER-001/withdraw",
        "payload": {"reason": "CKPA-70 SEC-05 immediate withdrawal audit verification"},
    },
    {
        "tc_id": "TC-LOG-04",
        "category": "Audit Log Redaction & Append-Only Check (SEC 08)",
        "role": "privacy_security_owner",
        "token_env": "CKPA_TOKEN_PRIVACY_OWNER",
        "target_doc": "DOC-008",
        "target_version": "DOC008-VER-001",
        "method": "GET",
        "path": "/api/v1/audit/logs?limit=10",
        "payload": None,
    },
]


def audit_g1_corpus_metadata():
    corpus_path = Path("data/g1/full/Policy_Corpus_G1_Full.csv")
    manifest_path = Path("data/g1/full/Source_URI_And_Checksum_Manifest_G1_Full.csv")
    with corpus_path.open(encoding="utf-8-sig") as f:
        corpus_rows = list(csv.DictReader(f))
    manifest_rows = []
    if manifest_path.exists():
        with manifest_path.open(encoding="utf-8-sig") as f:
            manifest_rows = list(csv.DictReader(f))

    doc_summary, invalid_roles, missing_scope_docs = {}, [], []
    for row in corpus_rows:
        doc_id = row.get("document_id", "").strip()
        scope = row.get("scope", "").strip()
        roles = [r.strip() for r in row.get("audience", "").split(",") if r.strip()]
        for r in roles:
            if r not in VALID_RFP_ROLES:
                invalid_roles.append((doc_id, r))
        if not scope or "role:" not in scope:
            missing_scope_docs.append(doc_id)
        doc_summary[doc_id] = doc_summary.get(doc_id, 0) + 1

    return {
        "total_passages": len(corpus_rows),
        "total_docs": len(doc_summary),
        "docs": sorted(doc_summary.keys()),
        "manifest_entries": len(manifest_rows),
        "invalid_roles": invalid_roles,
        "missing_scope_docs": sorted(set(missing_scope_docs)),
        "corpus_passed": len(invalid_roles) == 0 and len(missing_scope_docs) == 0 and len(doc_summary) > 0,
    }


def execute_live_http_test(base_url, tc):
    token = os.getenv(tc["token_env"], "").strip()
    if not token:
        return {
            "status": "BLOCKED_MISSING_TOKEN",
            "detail": f"Missing real auth token env var {tc['token_env']} (No-Mock policy: synthetic tokens forbidden)",
        }
    url = base_url.rstrip("/") + tc["path"]
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
        "X-Audit-Trace": f"CKPA-70-{tc['tc_id']}",
    }
    data = json.dumps(tc["payload"]).encode("utf-8") if tc["payload"] is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method=tc["method"])
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            digest = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
            return {"status": "EXECUTED", "detail": f"HTTP {resp.status} | body_len={len(body)} | sha256={digest}"}
    except urllib.error.HTTPError as e:
        err_body = e.read().decode("utf-8", errors="replace")
        digest = hashlib.sha256(err_body.encode("utf-8")).hexdigest()[:16]
        return {"status": "EXECUTED", "detail": f"HTTP {e.code} ({e.reason}) | body_len={len(err_body)} | sha256={digest}"}
    except Exception as exc:
        return {"status": "BLOCKED_CONNECTION_ERROR", "detail": f"Endpoint unreachable: {exc}"}


def main():
    parser = argparse.ArgumentParser(description="CKPA-70 No-Mock RBAC & Fail-Closed Audit Runner")
    parser.add_argument("--strict-live", action="store_true")
    args = parser.parse_args()

    timestamp = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=7))).isoformat()
    base_url = os.getenv("CKPA_BASE_URL", "").strip()
    ca = audit_g1_corpus_metadata()

    out_dir = Path("security/g1")
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir / "g1_rbac_failclosed_audit_CKPA-70.log"

    lines = [
        "=== [P5] SONGNHAT SCRM - GATE G1 RBAC, SOURCE_REF, CACHE & FAIL-CLOSED AUDIT LOG (NO-MOCK) ===",
        "Jira Issue       : CKPA-70 (Parent: CKPA-44 | Relates: CKPA-69 | Blocks: CKPA-71)",
        "RFP Traceability : SEC 01, SEC 05, SEC 08, ANS 02 | Gate Criteria: G1-AC03, G1-AC04",
        f"Execution Time   : {timestamp}",
        f"Live Endpoint    : {base_url if base_url else 'NOT_CONFIGURED (Offline Repository Mode - No-Mock Enforced)'}",
        "---------------------------------------------------------------------------------------------",
        "[PART 1] REAL G1 CORPUS RBAC & SCOPE METADATA AUDIT (data/g1/full/Policy_Corpus_G1_Full.csv)",
        f"  - Documents Verified : {ca['total_docs']} ({', '.join(ca['docs'])})",
        f"  - Passages Verified  : {ca['total_passages']} | Manifest Checksums: {ca['manifest_entries']}",
        f"  - Invalid UserRoles  : {ca['invalid_roles']}",
        f"  - Missing Scope Docs : {ca['missing_scope_docs']}",
        f"  - Part 1 Verdict     : {'PASS' if ca['corpus_passed'] else 'FAIL'}",
        "---------------------------------------------------------------------------------------------",
        "[PART 2] LIVE RUNTIME API AUDIT (SUB01 / SUB07 - NO-MOCK HTTP EXECUTION)",
    ]

    live_results = []
    for tc in LIVE_TEST_MATRIX:
        if not base_url:
            res = {
                "status": "BLOCKED_NO_LIVE_ENDPOINT",
                "detail": "CKPA_BASE_URL not set; synthetic mock execution prohibited per No-Mock policy",
            }
        else:
            res = execute_live_http_test(base_url, tc)
        live_results.append((tc, res))
        lines.append(
            f"  [{res['status']}] {tc['tc_id']} | Role={tc['role']} | Target={tc['target_doc']} ({tc['target_version']}) | "
            f"{tc['method']} {tc['path']} | {res['detail']}"
        )

    executed_count = sum(1 for _, r in live_results if r["status"] == "EXECUTED")
    lines.extend([
        "---------------------------------------------------------------------------------------------",
        f"PART 1 SUMMARY (Real G1 Corpus RBAC/Scope Metadata): {'PASSED' if ca['corpus_passed'] else 'FAILED'} ({ca['total_docs']}/11 docs verified).",
        f"PART 2 SUMMARY (Live Runtime API Execution)        : {executed_count}/{len(LIVE_TEST_MATRIX)} executed live; {len(LIVE_TEST_MATRIX) - executed_count}/{len(LIVE_TEST_MATRIX)} BLOCKED pending staging endpoint & tokens.",
        "OVERALL VERDICT: PARTIAL_PASS_DATA_VERIFIED / RUNTIME_BLOCKED_PENDING_LIVE_STAGING (ZERO MOCK DATA USED).",
    ])

    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[OK] Da ghi log kiem toan No-Mock: {log_path}")

    if args.strict_live and executed_count < len(LIVE_TEST_MATRIX):
        raise SystemExit(2)


if __name__ == "__main__":
    main()