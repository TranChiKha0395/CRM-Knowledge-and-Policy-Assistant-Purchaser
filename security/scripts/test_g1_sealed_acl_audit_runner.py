import json
import os
from pathlib import Path
import tempfile
import unittest

import g1_sealed_acl_audit_runner as runner


class TestSealedAclAuditRunner(unittest.TestCase):
    def setUp(self):
        self._orig_env = os.environ.copy()
        os.environ["CKPA_FORBIDDEN_USERS"] = "quochung-dev,yennhi-ai"
        os.environ["CKPA_S4_USERS"] = "quyhai-lead"
        os.environ["CKPA_P5_USERS"] = "anhkhoa-cloud"
        os.environ["CKPA_EXTRA_APPROVED_USERS"] = "p4-evaluator"
        os.environ["CKPA_EXPECTED_SEALED_REPO"] = "sealed-eval-repo"

    def tearDown(self):
        os.environ.clear()
        os.environ.update(self._orig_env)

    def _write_json_log(self, records):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
        json.dump(records, tmp)
        tmp.close()
        os.environ["CKPA_SEALED_ACL_LOG_PATH"] = tmp.name
        self.addCleanup(lambda: Path(tmp.name).unlink(missing_ok=True))

    def test_01_blocked_when_no_env_path(self):
        os.environ.pop("CKPA_SEALED_ACL_LOG_PATH", None)
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "BLOCKED")
        self.assertEqual(res["code"], "BLOCKED_EXTERNAL_REPO_ACCESS")

    def test_02_fail_on_empty_file(self):
        tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False, encoding="utf-8")
        tmp.write("   ")
        tmp.close()
        os.environ["CKPA_SEALED_ACL_LOG_PATH"] = tmp.name
        self.addCleanup(lambda: Path(tmp.name).unlink(missing_ok=True))
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_INVALID_LOG_FORMAT")

    def test_03_fail_on_missing_required_headers(self):
        self._write_json_log([{"actor": "quyhai-lead"}])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_MISSING_REQUIRED_FIELDS")

    def test_04_fail_on_duplicate_records(self):
        rec = {
            "record_type": "collaborator",
            "repository": "sealed-eval-repo",
            "actor": "quyhai-lead",
            "permission_or_action": "write",
            "outcome": "allowed",
            "timestamp": "2026-11-24T10:00:00+07:00",
        }
        self._write_json_log([rec, rec])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_DUPLICATE_RECORDS")

    def test_05_fail_when_s2_has_inherited_team_permission(self):
        self._write_json_log([
            {
                "record_type": "team_permission",
                "repository": "sealed-eval-repo",
                "actor": "quochung-dev",
                "permission_or_action": "read",
                "outcome": "allowed",
                "grant_source": "org_team:backend-devs",
            }
        ])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_ACL_POLICY_VIOLATION")

    def test_06_fail_when_unapproved_account_present(self):
        self._write_json_log([
            {
                "record_type": "collaborator",
                "repository": "sealed-eval-repo",
                "actor": "unknown-contractor",
                "permission_or_action": "read",
                "outcome": "allowed",
            }
        ])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_ACL_POLICY_VIOLATION")

    def test_07_fail_when_wrong_repository_exported(self):
        self._write_json_log([
            {
                "record_type": "collaborator",
                "repository": "wrong-public-repo",
                "actor": "quyhai-lead",
                "permission_or_action": "write",
                "outcome": "allowed",
            }
        ])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_ACL_POLICY_VIOLATION")

    def test_08_fail_when_s4_only_has_read_not_write(self):
        self._write_json_log([
            {
                "record_type": "collaborator",
                "repository": "sealed-eval-repo",
                "actor": "quyhai-lead",
                "permission_or_action": "read",
                "outcome": "allowed",
            },
            {
                "record_type": "collaborator",
                "repository": "sealed-eval-repo",
                "actor": "anhkhoa-cloud",
                "permission_or_action": "read",
                "outcome": "allowed",
            },
        ])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "FAIL")
        self.assertEqual(res["code"], "FAIL_INSUFFICIENT_S4_PERMISSION")

    def test_09_pass_when_s2_denied_and_s4_p5_authorized(self):
        self._write_json_log([
            {
                "record_type": "collaborator",
                "repository": "sealed-eval-repo",
                "actor": "quyhai-lead",
                "permission_or_action": "write",
                "outcome": "allowed",
            },
            {
                "record_type": "collaborator",
                "repository": "sealed-eval-repo",
                "actor": "anhkhoa-cloud",
                "permission_or_action": "read",
                "outcome": "allowed",
            },
            {
                "record_type": "audit_event",
                "repository": "sealed-eval-repo",
                "actor": "yennhi-ai",
                "permission_or_action": "git.clone",
                "outcome": "denied",
            },
        ])
        res = runner.audit_external_sealed_repo_acl()
        self.assertEqual(res["status"], "PASS")
        self.assertEqual(res["code"], "PASS_VERIFIED_EXTERNAL_ACL")

    def test_10_overall_verdict_matrix(self):
        self.assertEqual(runner.compute_overall_verdict(True, "PASS"), "PASS")
        self.assertEqual(runner.compute_overall_verdict(True, "BLOCKED"), "PARTIAL_PASS")
        self.assertEqual(runner.compute_overall_verdict(False, "PASS"), "FAIL")
        self.assertEqual(runner.compute_overall_verdict(True, "FAIL"), "FAIL")


if __name__ == "__main__":
    unittest.main(verbosity=2)