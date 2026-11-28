import os
from unittest.mock import patch
import unittest

import g1_rbac_failclosed_audit_runner as runner


class TestRbacFailClosedAuditRunner(unittest.TestCase):
    def setUp(self):
        self._orig_env = os.environ.copy()
        os.environ["CKPA_BASE_URL"] = "https://staging.example.internal"
        os.environ["CKPA_TOKEN_READER"] = "tok-reader"
        os.environ["CKPA_TOKEN_STEWARD"] = "tok-steward"
        os.environ["CKPA_TOKEN_POLICY_OWNER"] = "tok-owner"
        os.environ["CKPA_TOKEN_ADMINISTRATOR"] = "tok-admin"

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._orig_env)

    def test_01_blocked_when_no_staging_url(self):
        res = runner.execute_live_probe("", runner.LIVE_TEST_MATRIX[0])
        self.assertEqual(res["status"], "BLOCKED_NO_LIVE_ENDPOINT")

    def test_02_contract_uses_answer_root_and_6d_dat04_scope(self):
        for tc in runner.LIVE_TEST_MATRIX[:3]:
            self.assertEqual(tc["endpoint"], "/api/v1/answer")
            self.assertIn("question", tc["payload"])
            self.assertNotIn("user_context", tc["payload"])
            for key in runner.REQUIRED_SCOPE_KEYS:
                self.assertIn(key, tc["payload"]["scope"])
        self.assertEqual(
            runner.LIVE_TEST_MATRIX[2]["warmup_endpoint"],
            "/api/v1/admin/policies/DOC007-VER-001/withdraw",
        )

    def test_03_fail_step1_when_warmup_not_2xx(self):
        tc_cache = runner.LIVE_TEST_MATRIX[1]  # TC-CACHE-02
        with patch.object(runner, "_http_call", return_value=(403, '{"detail":"forbidden"}')) as mock_call:
            res = runner.execute_live_probe("https://staging.example.internal", tc_cache)
            self.assertEqual(res["status"], "FAIL_STEP1_FAILED")
            self.assertEqual(mock_call.call_count, 1)

    def test_04_fail_when_tc_log_04_returns_403_instead_of_200(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(403, '{"detail":"forbidden"}')):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "FAIL_UNEXPECTED_STATUS")

    def test_05_fail_when_tc_log_04_returns_200_with_empty_body(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(200, "   ")):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "FAIL_EMPTY_AUDIT_BODY")

    def test_06_fail_when_leakage_marker_present(self):
        tc_rbac = runner.LIVE_TEST_MATRIX[0]  # TC-RBAC-01
        with patch.object(runner, "_http_call", return_value=(200, '{"citations":[{"document_id":"DOC-006"}]}')):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rbac)
            self.assertEqual(res["status"], "FAIL_LEAKAGE_DETECTED")

    def test_07_pass_when_tc_rev_03_step1_200_and_step2_403(self):
        tc_rev = runner.LIVE_TEST_MATRIX[2]  # TC-REV-03
        with patch.object(runner, "_http_call", side_effect=[(200, '{"status":"withdrawn"}'), (403, '{"detail":"revoked"}')]):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rev)
            self.assertEqual(res["status"], "PASS_VERIFIED")

    def test_08_pass_when_tc_log_04_returns_200_non_empty_clean_body(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(200, '[{"event":"query","redacted":true}]')):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "PASS_VERIFIED")

    def test_09_real_corpus_metadata_audit_passes(self):
        ca = runner.audit_g1_corpus_metadata()
        self.assertTrue(ca["corpus_passed"])
        self.assertEqual(ca["total_docs"], 11)
        self.assertEqual(ca["policy_families"], ["POL-001", "POL-002", "POL-003"])
        self.assertEqual(len(ca["lifecycle_states"]), 7)

    def test_10_dynamic_overall_verdict_matrix(self):
        self.assertEqual(runner.compute_overall_verdict(True, 4, 0, 0), "PASS")
        self.assertEqual(runner.compute_overall_verdict(True, 0, 0, 4), "PARTIAL_PASS")
        self.assertEqual(runner.compute_overall_verdict(True, 3, 1, 0), "FAIL")
        self.assertEqual(runner.compute_overall_verdict(False, 4, 0, 0), "FAIL")



    def test_11_fail_when_tc_rev_03_step1_returns_404(self):
        tc_rev = runner.LIVE_TEST_MATRIX[2]
        with patch.object(runner, "_http_call", return_value=(404, '{"detail":"not found"}')) as mock_call:
            res = runner.execute_live_probe("https://staging.example.internal", tc_rev)
            self.assertEqual(res["status"], "FAIL_STEP1_FAILED")
            self.assertEqual(mock_call.call_count, 1)

    def test_12_excludes_original_question_from_leakage_scan(self):
        tc_rbac = runner.LIVE_TEST_MATRIX[0]
        clean_payload = '{"original_question": "Cho toi xem DOC-006", "answer": "Tu choi truy cap."}'
        with patch.object(runner, "_http_call", return_value=(200, clean_payload)):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rbac)
            self.assertEqual(res["status"], "PASS_VERIFIED")

    def test_13_handles_malformed_json_starting_with_brace(self):
        tc_rbac = runner.LIVE_TEST_MATRIX[0]
        malformed_body = "{not-valid-json-response-without-markers"
        with patch.object(runner, "_http_call", return_value=(200, malformed_body)):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rbac)
            self.assertEqual(res["status"], "PASS_VERIFIED")

if __name__ == "__main__":
    unittest.main(verbosity=2)
