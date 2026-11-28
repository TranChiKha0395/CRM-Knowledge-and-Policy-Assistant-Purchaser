"""Automated GitHub Pull Request Governance & Template Gatekeeper.

Enforces SCRM Onboarding Guide & SoD PR rules automatically on GitHub Actions:
1. Base branch protection:
   - Feature/task PRs MUST target `develop`.
   - Only `develop` or `release/*` / `hotfix/*` branches may target `main`.
2. Branch prefix convention (for PRs targeting `develop`):
   - Must start with `gov/`, `policy/`, `data/`, `uat/`, `sec/`, `docs/`, `fix/`, `chore/`, or `ci/`.
3. PR Template & SoD Checklist (for PRs targeting `develop`):
   - PR description must include `## Related Jira Issue`, `## Evidence`, and `## SoD & Compliance Checklist`.
   - Inside `## SoD & Compliance Checklist`, all checkboxes must be checked (`[x]`, at least 5 items, 0 unchecked `[ ]`).
   - Blocks legacy `CKPAOLD` or `SQUAD` in PR title/body.
"""

from __future__ import annotations

import json
import os
import re
import sys

ALLOWED_DEV_PREFIXES = (
    "gov/",
    "policy/",
    "data/",
    "uat/",
    "sec/",
    "docs/",
    "fix/",
    "chore/",
    "ci/",
)

REQUIRED_PR_SECTIONS = (
    "## Related Jira Issue",
    "## Evidence",
    "## SoD & Compliance Checklist",
)

LEGACY_PATTERN = re.compile(r"\bCKPAOLD\b|\bSQUAD\b")
CHECKED_BOX_RE = re.compile(r"^\s*-\s*\[[xX]\]\s+\S+", re.MULTILINE)
UNCHECKED_BOX_RE = re.compile(r"^\s*-\s*\[\s\]\s+\S+", re.MULTILINE)


def validate_pr_metadata(base_ref: str, head_ref: str, title: str, body: str) -> list[str]:
    errors: list[str] = []
    base = (base_ref or "").strip()
    head = (head_ref or "").strip()
    pr_title = (title or "").strip()
    pr_body = body or ""

    if LEGACY_PATTERN.search(pr_title) or LEGACY_PATTERN.search(pr_body):
        errors.append(
            "[LEGACY_ID] Tiêu đề hoặc mô tả PR chứa mã cũ bị cấm (`CKPAOLD` / `SQUAD`). Chỉ sử dụng mã `CKPA`."
        )

    if base == "main":
        if head != "develop" and not head.startswith(("release/", "hotfix/")):
            errors.append(
                f"[WRONG_BASE_BRANCH] Nhánh `{head}` KHÔNG được mở PR thẳng vào `main`! "
                "Vui lòng đổi Base branch sang `develop` (chỉ `develop` hoặc `release/*` mới được merge vào `main`)."
            )
        return errors

    if base == "develop":
        if not head.startswith(ALLOWED_DEV_PREFIXES):
            errors.append(
                f"[BRANCH_PREFIX] Tên nhánh `{head}` chưa đúng chuẩn tiền tố vai trò "
                f"({', '.join(ALLOWED_DEV_PREFIXES)})."
            )

        for section in REQUIRED_PR_SECTIONS:
            if section.lower() not in pr_body.lower():
                errors.append(
                    f"[PR_TEMPLATE] Mô tả PR thiếu mục bắt buộc `{section}` theo `.github/PULL_REQUEST_TEMPLATE.md`."
                )

        m = re.search(
            r"##\s*SoD\s*&\s*Compliance\s*Checklist[^\n]*\n(.*?)(?=\n##\s+|\Z)",
            pr_body,
            flags=re.IGNORECASE | re.DOTALL,
        )
        if m:
            sod_block = m.group(1)
            checked = len(CHECKED_BOX_RE.findall(sod_block))
            unchecked = len(UNCHECKED_BOX_RE.findall(sod_block))
            if unchecked > 0:
                errors.append(
                    f"[SOD_CHECKLIST] Còn `{unchecked}` mục chưa tích `[x]` trong `## SoD & Compliance Checklist`."
                )
            if checked < 5:
                errors.append(
                    f"[SOD_CHECKLIST] Mục `## SoD & Compliance Checklist` cần tích đủ tối thiểu `5/5` mục `[x]` (hiện có `{checked}`)."
                )

    return errors


def _write_summary(base_ref: str, head_ref: str, errors: list[str]) -> None:
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if not summary_path:
        return
    lines = ["## PR Governance & SoD Checklist Gate\n"]
    lines.append(f"- **Route:** `{head_ref}` -> `{base_ref}`")
    if not errors:
        lines.append("- **Verdict:** **PASS**\n")
    else:
        lines.append(f"- **Verdict:** **FAIL ({len(errors)} lỗi quản trị PR)**\n")
        for err in errors:
            lines.append(f"- {err}")
    with open(summary_path, "a", encoding="utf-8") as fp:
        fp.write("\n".join(lines) + "\n")


def main() -> int:
    event_path = os.environ.get("GITHUB_EVENT_PATH")
    if not event_path or not os.path.exists(event_path):
        print("No GITHUB_EVENT_PATH detected; skipping PR metadata check outside pull_request event.")
        return 0

    with open(event_path, "r", encoding="utf-8") as fp:
        payload = json.load(fp)

    pr = payload.get("pull_request")
    if not pr:
        print("Event payload is not a pull_request; skipping PR metadata gate.")
        return 0

    base_ref = pr.get("base", {}).get("ref", "")
    head_ref = pr.get("head", {}).get("ref", "")
    title = pr.get("title", "")
    body = pr.get("body") or ""

    errors = validate_pr_metadata(base_ref, head_ref, title, body)
    _write_summary(base_ref, head_ref, errors)

    print(f"Checking PR metadata: {head_ref} -> {base_ref}")
    if errors:
        print(f"PR Governance Gate FAILED with {len(errors)} issue(s):")
        for err in errors:
            print(f"  - {err}")
        return 1

    print("PR Governance Gate PASSED (valid target branch, prefix, template sections & 5/5 SoD checklist).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
