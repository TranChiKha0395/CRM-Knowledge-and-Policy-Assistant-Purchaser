"""Unit tests for Purchaser CI Guardrails & PR Metadata Gatekeeper."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import ci_pr_metadata_guard as pr_guard
from scripts import ci_purchaser_guard as repo_guard

VALID_PR_BODY = """
## Summary
Update security report.

## Related Jira Issue
- **Jira Key:** `CKPA-104`

## Evidence
- File: `security/g2/report.md`

## SoD & Compliance Checklist (Bắt buộc)
- [x] Không push thẳng main/develop
- [x] 0% PII thật
- [x] Không chứa plaintext 100 Sealed / 80 Challenges
- [x] Base Scope O1 = OFF
- [x] Không gán S4 review feat/
"""


class TestPrMetadataGuard(unittest.TestCase):
    def test_blocks_feature_branch_targeting_main(self):
        errs = pr_guard.validate_pr_metadata("main", "uat/CKPA-93-test", "[CKPA-93] test", VALID_PR_BODY)
        self.assertTrue(any("[WRONG_BASE_BRANCH]" in e for e in errs))

    def test_allows_develop_targeting_main(self):
        errs = pr_guard.validate_pr_metadata("main", "develop", "release: sync develop into main", "")
        self.assertEqual(errs, [])

    def test_blocks_missing_template_and_unchecked_sod(self):
        bad_body = "## Summary\nOnly summary\n## SoD & Compliance Checklist\n- [x] One\n- [ ] Two\n"
        errs = pr_guard.validate_pr_metadata("develop", "sec/CKPA-104-doc", "docs: update", bad_body)
        self.assertTrue(any("[PR_TEMPLATE]" in e for e in errs))
        self.assertTrue(any("[SOD_CHECKLIST]" in e for e in errs))

    def test_passes_valid_develop_pr(self):
        errs = pr_guard.validate_pr_metadata("develop", "sec/CKPA-104-doc", "[CKPA-104] docs", VALID_PR_BODY)
        self.assertEqual(errs, [])


class TestRepoGuard(unittest.TestCase):
    def test_detects_binary_bom_latex_localpath_and_broken_link(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "doc.docx").write_bytes(b"PK\x03\x04")
            (root / "bom.md").write_bytes(b"\xef\xbb\xbf# Title\n")
            (root / "bad.md").write_text(
                "Legacy CKPAOLD and $\\rightarrow$ and [x](file:///C:/Users/Admin/a.md) and [broken](./missing.md)\n",
                encoding="utf-8",
            )
            _, errs = repo_guard.run_all_checks(root)
            joined = "\n".join(errs)
            self.assertIn("[FORBIDDEN_FILE]", joined)
            self.assertIn("[UTF8_BOM]", joined)
            self.assertIn("[LEGACY_ID]", joined)
            self.assertIn("[INLINE_LATEX]", joined)
            self.assertIn("[LOCAL_PATH]", joined)
            self.assertIn("[BROKEN_LINK]", joined)

    def test_detects_wrong_policy_domain_and_synthetic_uat_csv(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            uat_dir = root / "uat" / "g2"
            uat_dir.mkdir(parents=True)
            rows = ["Eval_ID,Policy_Family,Policy_Family_Name,U1_Score,U2_Score,Consensus_Note"]
            for i in range(1, 31):
                rows.append(f"E-{i:02d},POL-001,Chính sách Đổi trả & Hoàn tiền,4,4,Copy paste note")
            (uat_dir / "eval.csv").write_text("\n".join(rows) + "\n", encoding="utf-8")
            _, errs = repo_guard.run_all_checks(root)
            joined = "\n".join(errs)
            self.assertIn("[WRONG_DOMAIN]", joined)
            self.assertIn("[NO_MOCK_VIOLATION]", joined)


if __name__ == "__main__":
    unittest.main()
