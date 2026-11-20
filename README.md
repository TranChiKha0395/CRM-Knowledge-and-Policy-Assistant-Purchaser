# SongNhat SCRM — Purchaser Team Repository (`P1–P5`)

Repository quản trị tập trung tài liệu, dữ liệu nguồn đã làm sạch (`0% PII`), quy tắc chính sách, bộ đánh giá công khai (`60 DEV + 40 VAL`), hồ sơ pháp lý/bảo mật và kịch bản kiểm toán của phía **Purchaser (SongNhat — `P1–P5`)** cho dự án **CRM Knowledge and Policy Assistant (SCRM / `CKPA`)**.

Tuân thủ **RFP SongNhat (28 trang)** và **SCRM Team Onboarding & Workflow Guide v1.0**.

---

## 1. Kiến trúc 3 Repository của Dự án

| # | Repository | Phía quản lý | Nội dung lưu trữ | Ràng buộc SoD |
|---|---|---|---|---|
| **1** | **`CRM-Knowledge-and-Policy-Assistant-Purchaser`** *(Repo này)* | **Purchaser (`P1–P5`)** | Governance (`P1`), Policy approvals & Authority Matrix (`P2`), Corpus CSV + Manifest SHA-256 + Fixtures (`P3`), `60 DEV + 40 VAL` + Từ điển `VN 01` + `source_uri` log (`P4`), RBAC/Legal/PII audit scripts & logs (`P5`). | **0% PII thật**, **0% O1** (Base Scope), **CẤM lưu plaintext `100 Sealed` & `80 Challenges`**. |
| **2** | **`CRM-Knowledge-and-Policy-Assistant`** *(Repo Build/Code)* | **Supplier (`S1–S5`)** + đồng bộ dữ liệu sạch từ Purchaser | Source code backend/frontend/worker/infra (`S2, S3, S5`), docs kỹ thuật (`S1`), nhận đồng bộ CSV sạch (`P3`) & từ điển `VN 01` (`P4`) qua PR vào `develop`. | `S4` không code & không review PR `feat/`; không chứa `100 Sealed` / `80 Challenges`. |
| **3** | **`sealed-eval-repo`** *(Repo Niêm phong — `CKPA-48`)* | **`S4` Quý Hải** + Purchaser liên quan (`P1/P2/P3/P5`) | **100 Sealed Acceptance Cases**, **80 Constructed Challenges** (gồm 40 `VN 02`) và đáp án chuẩn đồng ký bởi `P2/P3` (`CKPA-67`, `CKPA-68`). | **Chinese Wall:** chặn tuyệt đối `Read/Clone` đối với `S2` & `S3`. |

---

## 2. Cấu trúc Thư mục & Phân quyền theo 5 vai Purchaser

```text
CRM-Knowledge-and-Policy-Assistant-Purchaser/
├── .github/
│   ├── PULL_REQUEST_TEMPLATE.md       # Mẫu PR chuẩn Onboarding Guide §17 + SoD
│   └── workflows/purchaser-ci.yml     # CI tự động: chặn Sealed/secrets, quét 0% PII, check CSV 21/23 cột
├── governance/                        # [P1] Mỹ Vân   — nhánh gov/
│   ├── g0/                            # Charter, Quyết định Route/Base Scope/O1 OFF, Sign-off G0
│   └── g1/                            # Biên bản nghiệm thu các sub-task & Gate G1 (CKPA-81, 84)
├── policy/                            # [P2] Hữu Tài  — nhánh policy/
│   ├── g0/                            # 3 Họ chính sách, Ma trận 5 lớp thẩm quyền, Ngày hiệu lực & Hold
│   └── g1/                            # Biên bản duyệt Corpus Họ 1 (CKPA-51), Họ 2-3 (CKPA-62), Reviewer #1 (CKPA-83)
├── data/                              # [P3] Chí Kha  — nhánh data/
│   ├── templates/                     # passages_template.csv (21 cột), critical_fields_template.csv (23 cột)
│   ├── g0/                            # Source Registry, 30 Passages + 10 Critical Fields mẫu G0
│   └── g1/                            # Family 1 (CKPA-50), Full 3 Họ (CKPA-58), sources/, fixtures/, reports/
├── uat/                               # [P4] Trà My   — nhánh uat/
│   ├── g0/                            # Question Inventory 4 tuần, Baseline Effort
│   └── g1/                            # CKPA-55 (60 DEV + 40 VAL, vn01_crm_dictionary.json), CKPA-66 (bản che hash 100 Sealed + source_uri log)
├── security/                          # [P5] Anh Khoa — nhánh sec/
│   ├── g0/                            # RBAC 20-User, Legal/Privacy Review (Annex F), Retention (Annex C)
│   ├── g1/                            # CKPA-47 (Chứng nhận 0% PII + .log chạy thật), CKPA-70, CKPA-79
│   └── scripts/                       # Script kiểm toán bảo mật (g1_security_audit_runner.py)
└── scripts/
    └── ci_purchaser_guard.py          # Script kiểm định tự động (SoD, 0% PII, CSV schema)
```

---

## 3. Quy ước Branch & GitHub Workflow (Onboarding Guide §11–19)

- **Nhánh bảo vệ:** `main` (chốt mốc Gate) và `develop` (nhánh tích hợp chính — mọi PR đều chọn `Base: develop`). **Cấm commit/push trực tiếp lên `main` hoặc `develop`.**
- **Quy ước đặt tên nhánh:** `<prefix>/<JIRA-ID>-<short-description>` (chữ thường, gạch nối, gắn mã `CKPA-xx`):
  - `P1` Mỹ Vân: `gov/CKPA-xx-...`
  - `P2` Hữu Tài: `policy/CKPA-xx-...`
  - `P3` Chí Kha: `data/CKPA-xx-...`
  - `P4` Trà My: `uat/CKPA-xx-...`
  - `P5` Anh Khoa: `sec/CKPA-xx-...`
- **Quy trình hằng ngày:**
  ```bash
  git checkout develop
  git pull origin develop
  git checkout -b <prefix>/CKPA-XX-short-description
  # Làm việc & tự chạy kiểm tra trước khi commit
  python scripts/ci_purchaser_guard.py
  git add <files>
  git commit -m "docs(scope): mô tả thay đổi [CKPA-XX]"
  git push -u origin <prefix>/CKPA-XX-short-description
  ```
- **Quy tắc đóng Jira:** Chỉ chuyển `Done` khi PR đạt CI, được reviewer phù hợp duyệt và đã đính kèm link PR/evidence lên Jira.
