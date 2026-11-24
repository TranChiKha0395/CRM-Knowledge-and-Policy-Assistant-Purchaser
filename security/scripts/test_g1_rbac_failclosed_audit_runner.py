import os
from unittest.mock import patch
import unittest

import g1_rbac_failclosed_audit_runner as runner


class TestRbacFailClosedAuditRunner(unittest.TestCase):
    def setUp(self):
        self._orig_env = os.environ.copy()
        os.environ["CKPA_STAGING_API_BASE_URL"] = "https://staging.example.internal"
        os.environ["CKPA_READER_BEARER_TOKEN"] = "tok-reader"
        os.environ["CKPA_STEWARD_BEARER_TOKEN"] = "tok-steward"
        os.environ["CKPA_POLICY_OWNER_BEARER_TOKEN"] = "tok-owner"
        os.environ["CKPA_ADMIN_BEARER_TOKEN"] = "tok-admin"

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._orig_env)

    def test_01_blocked_when_no_staging_url(self):
        os.environ.pop("CKPA_STAGING_API_BASE_URL", None)
        res = runner.execute_live_probe("", runner.LIVE_TEST_MATRIX[0])
        self.assertEqual(res["status"], "BLOCKED_NO_STAGING_ENDPOINT")

    def test_02_fail_step1_when_warmup_not_2xx(self):
        tc_cache = runner.LIVE_TEST_MATRIX[1]  # TC-CACHE-02
        with patch.object(runner, "_http_call", return_value=(403, '{"detail":"forbidden"}')) as mock_call:
            res = runner.execute_live_probe("https://staging.example.internal", tc_cache)
            self.assertEqual(res["status"], "FAIL_STEP1_FAILED")
            # Must abort immediately after Step 1 fails without calling Step 2
            self.assertEqual(mock_call.call_count, 1)

    def test_03_fail_when_tc_log_04_returns_403_instead_of_200(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(403, '{"detail":"forbidden"}')):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "FAIL_UNEXPECTED_STATUS")

    def test_04_fail_when_tc_log_04_returns_200_with_empty_body(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(200, "   ")):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "FAIL_EMPTY_AUDIT_BODY")

    def test_05_fail_when_leakage_marker_present(self):
        tc_rbac = runner.LIVE_TEST_MATRIX[0]  # TC-RBAC-01
        with patch.object(runner, "_http_call", return_value=(403, "error: POL-002_CONFIDENTIAL_BODY")):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rbac)
            self.assertEqual(res["status"], "FAIL_LEAKAGE_DETECTED")

    def test_06_pass_when_tc_rev_03_step1_200_and_step2_403(self):
        tc_rev = runner.LIVE_TEST_MATRIX[2]  # TC-REV-03
        with patch.object(runner, "_http_call", side_effect=[(200, '{"status":"withdrawn"}'), (403, '{"detail":"revoked"}')]):
            res = runner.execute_live_probe("https://staging.example.internal", tc_rev)
            self.assertEqual(res["status"], "PASS_VERIFIED")

    def test_07_pass_when_tc_log_04_returns_200_non_empty_clean_body(self):
        tc_log = runner.LIVE_TEST_MATRIX[3]  # TC-LOG-04
        with patch.object(runner, "_http_call", return_value=(200, '[{"event":"query","redacted":true}]')):
            res = runner.execute_live_probe("https://staging.example.internal", tc_log)
            self.assertEqual(res["status"], "PASS_VERIFIED")

    def test_08_dynamic_overall_verdict_matrix(self):
        self.assertEqual(runner.compute_overall_verdict(True, 4, 0, 0), "PASS")
        self.assertEqual(runner.compute_overall_verdict(True, 0, 0, 4), "PARTIAL_PASS")
        self.assertEqual(runner.compute_overall_verdict(True, 3, 1, 0), "FAIL")
        self.assertEqual(runner.compute_overall_verdict(False, 4, 0, 0), "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)