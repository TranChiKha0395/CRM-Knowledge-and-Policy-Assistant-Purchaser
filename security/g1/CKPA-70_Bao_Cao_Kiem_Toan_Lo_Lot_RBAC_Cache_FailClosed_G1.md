# BÁO CÁO KIỂM TOÁN LỘ LỌT RBAC, SOURCE_REF, CACHE & FAIL-CLOSED (GATE G1)

- **Mã công việc Jira:** `CKPA-70` (Parent: `CKPA-44` | Liên quan: `CKPA-69` | Mở khóa: `CKPA-71`)
- **Mã truy vết RFP & Cổng G1:** `SEC 01`, `SEC 02`, `SEC 05`, `KNW 03`, `KNW 04`, `OPS 05`, `ANS 02` | Tiêu chí: `G1-AC03`, `G1-AC04`
- **Phân hệ kiểm thử:** `SUB01` (Test), `SUB07` (Pre-retrieval)
- **Chủ trì thực hiện:** `[P5]` Anh Khoa | **Phối hợp:** `[S5]` Ngọc Duy | **Nghiệm thu:** `[P1]` Mỹ Vân | **Review:** `[P3]` Chí Kha, `[S1]` Hoàng Tiến
- **Chính sách kiểm thử:** **No-Mock** (100% đối chiếu dữ liệu thật G1 & thực thi HTTP trực tiếp đúng hợp đồng schema `AnswerQueryRequest` khi có endpoint Staging; tuyệt đối không dùng dữ liệu giả lập)

---

## 1. Phạm vi & Mục tiêu kiểm toán
Đánh giá khả năng ngăn chặn rò rỉ thông tin phân quyền trước và trong quá trình truy xuất RAG của phân hệ **Purchaser** trên **3 họ chính sách CRM thật (`POL-001`, `POL-002`, `POL-003`)** và **trạng thái vòng đời `KNW 03`**, tập trung vào 4 rủi ro trọng yếu:
1. Lộ lọt `source_ref`, trích dẫn (`citation`) hoặc tiêu đề tài liệu khi ngoài phạm vi `scope` 6 chiều `DAT 04` / `audience` (`SEC 01`, `SEC 02`, `ANS 02`).
2. Nhiễm chéo & tái sử dụng bộ nhớ đệm (`Cross-Role Cache Isolation & Reuse`) giữa các `UserRole` (`steward` -> `reader`) (`SEC 01`, `KNW 03`, `OPS 05`).
3. Độ trễ thu hồi quyền truy cập đối với tài liệu đã bị rút/hủy hiệu lực (`Immediate Withdrawal Fail-Closed <= 5 phút`: `policy_owner` rút tài liệu -> `reader` truy vấn lại bị chặn) (`SEC 05`, `KNW 03`, `KNW 04`).
4. Rò rỉ dữ liệu nhạy cảm/tiêu đề tài liệu trong nhật ký kiểm toán & ranh giới quyền `administrator` (`Audit Log Redaction` — `SEC 01`, `SEC 02`, `OPS 05`).

---

## 2. Kết quả kiểm toán Phần 1 — Xác thực Metadata Phân quyền Corpus G1 Thật
Kiểm toán tự động trực tiếp trên `data/g1/full/Policy_Corpus_G1_Full.csv` (21 cột UTF-8) và `data/g1/full/Source_URI_And_Checksum_Manifest_G1_Full.csv`:
- **Tổng số tài liệu kiểm toán:** **11 tài liệu thật** (`DOC-001` đến `DOC-011`, `96` passages, `136` manifest checksums).
- **3 họ chính sách CRM thật trích xuất từ cột `source_ref`:** `['POL-001', 'POL-002', 'POL-003']` (**3/3 họ đạt chuẩn**).
- **Tính hợp lệ của 4 vai trò cốt lõi `SEC 01` (`audience`):** **100% đạt chuẩn RFP** (`reader`, `policy_owner`, `steward`, `administrator`), **0** vai trò ngoài danh mục.
- **Tính đầy đủ của ràng buộc `scope` 6 chiều (`DAT 04`):** **11/11** tài liệu có đầy đủ 6 chiều (`company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`).
- **Trạng thái Phần 1:** **PASS (Dữ liệu thật đã xác minh)**.

---

## 3. Ma trận kiểm thử Phần 2 — Thực thi Runtime Live API (`SUB01` / `SUB07` — Contract `scope: str` & Assertion)

| Mã TC | Hạng mục kiểm thử & Luồng thực thi | 4 `UserRole` cốt lõi (`SEC 01`) | Tài liệu & Phiên bản thật | Endpoint & Payload Contract (`AnswerQueryRequest`) | Trạng thái hiện tại (No-Mock) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC-RBAC-01** | Selection, 6D Scope & Source_Ref Leakage (`SEC 01`, `SEC 02`, `ANS 02`) | `reader` | `DOC-006` (`DOC006-VER-001`) | `POST /api/v1/answer` (`question`, `scope` 6 chiều; assert 0 rò rỉ `DOC-006`/`source_ref`) | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_READER`)* |
| **TC-CACHE-02** | Cross-Role Cache Isolation 2 bước (`steward` -> `reader`) (`SEC 01`, `KNW 03`, `OPS 05`) | `steward` -> `reader` | `DOC-008` (`DOC008-VER-001`) | `POST /api/v1/answer` (Bước 1 `steward` query -> Bước 2 `reader` query; assert 0 rò rỉ `DOC-008`) | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_STEWARD`/`READER`)* |
| **TC-REV-03** | Immediate Withdrawal Fail-Closed 2 bước (`withdraw` -> `answer`) (`SEC 05`, `KNW 03`, `KNW 04`) | `policy_owner` -> `reader` | `DOC-007` (`DOC007-VER-001`) | `POST /api/v1/admin/policies/DOC007-VER-001/withdraw` -> `POST /api/v1/answer` (assert 0 rò rỉ `DOC-007`) | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_POLICY_OWNER`/`READER`)* |
| **TC-LOG-04** | Audit Log Redaction & Boundary (`SEC 01`, `SEC 02`, `OPS 05`) | `administrator` | `DOC-008` (`DOC008-VER-001`) | `GET /api/v1/audit/logs?limit=10` (assert 0 lộ tiêu đề mật / PII) | **BLOCKED_NO_LIVE_ENDPOINT** *(Chờ `CKPA_BASE_URL` & `CKPA_TOKEN_ADMINISTRATOR`)* |

---

## 4. Bằng chứng kỹ thuật & Trạng thái Gate G1 (`G1-AC03` & `G1-AC04`)
- **Nhánh & PR cập nhật:** `sec/CKPA-70-s1-review-sync` (PR #49) & `sec/CKPA-70-fix-answer-trailing-slash` (PR #61 — đồng bộ chuẩn route `POST /api/v1/answer` không có dấu `/` cuối).
- **Script kiểm toán No-Mock:** `security/scripts/g1_rbac_failclosed_audit_runner.py` (khớp schema `AnswerQueryRequest` với `scope: str` 6 chiều `DAT 04`, assertion pass/fail thật và cờ `--strict-live`; 10/10 unit tests PASS).
- **Nhật ký thực thi thật:** `security/g1/g1_rbac_failclosed_audit_CKPA-70.log`.
- **Kiểm định CI Guard:** Đã chạy `scripts/ci_purchaser_guard.py` (**0 PII**, **0 tệp cấm**).
- **Kết luận trung thực:**
  - **Phần dữ liệu Corpus G1 (`DOC-001`..`DOC-011`):** **PASSED** (100% khớp 4 vai trò cốt lõi `SEC 01`, 3/3 họ chính sách `POL-001..003` & `scope` 6 chiều `DAT 04`).
  - **Phần kiểm thử Runtime End-to-End (`SUB01`/`SUB07`):** **BLOCKED** do: (1) phía Supplier đang xử lý lỗi lộ metadata `SCHEDULED`/`DRAFT`/`WITHDRAWN` ở `KnowledgeService.get_document_lineage()` và kiểm tra `effective_from` ở `get_passage()` (ghi nhận trên Jira `CKPA-70`), và (2) repository Purchaser chưa được cấp endpoint Staging & token thật (`CKPA_BASE_URL`). Giữ Jira `CKPA-70` (và Story cha `CKPA-69`) ở trạng thái **`In Progress`** cho tới khi chạy `--strict-live` đạt 4/4 `PASS_VERIFIED`.