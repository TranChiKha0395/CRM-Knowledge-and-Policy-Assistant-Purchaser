# BÁO CÁO KIỂM TOÁN LỘ LỌT RBAC, SOURCE_REF, CACHE & FAIL-CLOSED (GATE G1)

- **Mã công việc Jira:** `CKPA-70` (Parent: `CKPA-44` | Liên quan: `CKPA-69` | Mở khóa: `CKPA-71`)
- **Mã truy vết RFP & Cổng G1:** `SEC 01`, `SEC 05`, `SEC 08`, `ANS 02` | Tiêu chí: `G1-AC03`, `G1-AC04`
- **Phân hệ kiểm thử:** `SUB01` (Test), `SUB07` (Pre-retrieval)
- **Chủ trì thực hiện:** `[P5]` Anh Khoa | **Phối hợp:** `[S5]` Ngọc Duy | **Nghiệm thu:** `[P1]` Mỹ Vân
- **Chính sách kiểm thử:** **No-Mock** (100% đối chiếu dữ liệu thật G1 & thực thi HTTP trực tiếp khi có endpoint Staging; tuyệt đối không dùng dữ liệu giả lập)

---

## 1. Phạm vi & Mục tiêu kiểm toán
Đánh giá khả năng ngăn chặn rò rỉ thông tin phân quyền trước và trong quá trình truy xuất RAG của phân hệ **Purchaser**, tập trung vào 4 rủi ro trọng yếu:
1. Lộ lọt `source_ref`, trích dẫn (`citation`) hoặc tiêu đề tài liệu khi ngoài phạm vi `scope` / `audience` (`SEC 01`, `ANS 02`).
2. Nhiễm chéo bộ nhớ đệm (`Cross-Role Cache Isolation / Replay`) giữa các `UserRole` khác nhau (`SEC 01`).
3. Độ trễ thu hồi quyền truy cập đối với tài liệu đã bị rút/hủy hiệu lực (`Immediate Withdrawal Fail-Closed <= 5 phút` — `SEC 05`).
4. Rò rỉ dữ liệu nhạy cảm hoặc tiêu đề tài liệu trong nhật ký kiểm toán (`Audit Log Redaction` — `SEC 08`).

---

## 2. Kết quả kiểm toán Phần 1 — Xác thực Metadata Phân quyền Corpus G1 Thật
Kiểm toán tự động trực tiếp trên `data/g1/full/Policy_Corpus_G1_Full.csv` và `data/g1/full/Source_URI_And_Checksum_Manifest_G1_Full.csv`:
- **Tổng số tài liệu kiểm toán:** **11 tài liệu thật** (`DOC-001` đến `DOC-011`).
- **Tính hợp lệ của `UserRole` (`audience`):** **100% đạt chuẩn RFP** (`reader`, `policy_owner`, `steward`, `administrator`), **0** vai trò ngoài danh mục.
- **Tính đầy đủ của ràng buộc `scope`:** **11/11** tài liệu có đầy đủ thuộc tính phân vùng (`role:sales`, `role:crm`, `role:cskh`, `customer_group`, `transaction_scope`).
- **Trạng thái Phần 1:** **PASS (Dữ liệu thật đã xác minh)**.

---

## 3. Ma trận kiểm thử Phần 2 — Thực thi Runtime Live API (`SUB01` / `SUB07` — No-Mock)

| Mã TC | Hạng mục kiểm thử | `UserRole` (Chuẩn RFP) | Tài liệu & Phiên bản thật | Endpoint thực thi | Trạng thái hiện tại (No-Mock) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-RBAC-01** | Selection & Scope/Source_Ref (`SEC 01`, `ANS 02`) | `reader` | `DOC-006` (`DOC006-VER-001`) | `POST /api/v1/query` | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_READER`)* |
| **TC-RBAC-02** | Cross-Role Cache Isolation (`SEC 01`) | `legal_owner` | `DOC-008` (`DOC008-VER-001`) | `POST /api/v1/query` | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_LEGAL_OWNER`)* |
| **TC-REV-03** | Immediate Withdrawal Fail-Closed (`SEC 05`) | `policy_owner` | `DOC-007` (`DOC007-VER-001`) | `POST /api/v1/admin/policies/DOC007-VER-001/withdraw` | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_POLICY_OWNER`)* |
| **TC-LOG-04** | Audit Log Redaction Check (`SEC 08`) | `privacy_security_owner` | `DOC-008` (`DOC008-VER-001`) | `GET /api/v1/audit/logs?limit=10` | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_PRIVACY_OWNER`)* |

---

## 4. Bằng chứng kỹ thuật & Trạng thái Gate G1 (`G1-AC03` & `G1-AC04`)
- **Script kiểm toán No-Mock:** `security/scripts/g1_rbac_failclosed_audit_runner.py` (hỗ trợ `--strict-live` và biến môi trường `CKPA_BASE_URL`, `CKPA_TOKEN_*`).
- **Nhật ký thực thi thật:** `security/g1/g1_rbac_failclosed_audit_CKPA-70.log`.
- **Kiểm định CI Guard:** Đã chạy `scripts/ci_purchaser_guard.py` (**0 PII**, **0 tệp cấm**).
- **Kết luận trung thực:**
  - **Phần dữ liệu Corpus G1 (`DOC-001`..`DOC-011`):** **PASSED** (100% đúng `UserRole` chuẩn RFP và có đầy đủ `scope`).
  - **Phần kiểm thử Runtime End-to-End (`SUB01`/`SUB07`):** **BLOCKED** do repository hiện tại chỉ lưu trữ dữ liệu và tài liệu, chưa có endpoint Staging & token thật được cấp bởi nhóm triển khai (`S1`/`S3`/`S5`). Ngay khi có `CKPA_BASE_URL`, chỉ cần chạy lại `python security/scripts/g1_rbac_failclosed_audit_runner.py --strict-live` để cập nhật bằng chứng HTTP thật và mở khóa `CKPA-71`.