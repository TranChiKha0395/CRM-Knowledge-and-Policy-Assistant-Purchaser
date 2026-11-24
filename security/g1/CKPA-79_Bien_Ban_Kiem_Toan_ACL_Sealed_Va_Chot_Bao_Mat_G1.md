# BIÊN BẢN KIỂM TOÁN ACL KHO SEALED & CHỐT BẢO MẬT GATE G1

- **Mã công việc Jira:** `CKPA-79` (Parent: `CKPA-44` | Chặn / Mở khóa: `CKPA-80` | Liên quan: `CKPA-77`)
- **Mã truy vết RFP & Tiêu chí G1:** `Mục 8`, `Mục 11`, `SEC 01`, `SEC 02`, `SEC 06` *(Ghi chú: mã `SEC 08` trên thẻ Jira cũ là mã import từ bảng Jira; theo RFP chuẩn của dự án, `SEC 08` thuộc kiểm soát thay đổi provider/model/prompt/selector và rollback nên không áp dụng cho task ACL kho Sealed này)* | Tiêu chí: `G1-AC04`, `G1-AC07`
- **Phân hệ thực hiện:** `SUB03` (Evaluation — kho riêng `sealed-eval-repo`) & Repository chung Purchaser
- **Chủ trì thực hiện:** `[P5]` Anh Khoa (Privacy & Security Owner)
- **Phối hợp RACI:** `[S4]` Quý Hải, `[S5]` Ngọc Duy (xuất danh sách Collaborators & GitHub Audit Log của `sealed-eval-repo`) | **Review:** `[P3]` Chí Kha
- **Chính sách kiểm thử:** **No-Mock** (100% quét dữ liệu thật trong repository chung và yêu cầu trích xuất JSON/CSV thật từ GitHub Audit Log của kho riêng `sealed-eval-repo`, đối soát theo GitHub username thật qua `CKPA_FORBIDDEN_USERS` và `CKPA_ALLOWED_USERS`; tuyệt đối không giả lập log truy cập)

---

## 1. Mục tiêu & Nguyên tắc tách biệt Chinese Wall (`Mục 8`, `Mục 11`, `SEC 01`, `SEC 06`)
Theo kiến trúc tách biệt đánh giá độc lập (`Chinese Wall` / `SoD`) của dự án **SongNhat SCRM**:
1. Toàn bộ **`100 Sealed Acceptance Cases`** và **`80 Constructed Challenges`** phải được lưu trữ cô lập tuyệt đối tại repository riêng **`sealed-eval-repo`** (`SUB03`), hoàn toàn tách khỏi repository phát triển chung.
2. **Nhóm kỹ sư phát triển** (`[S2]` Quốc Hưng — Backend/RAG, `[S3]` Yến Nhi — Retrieval/App) có **0% quyền truy cập** (`Read / Clone / Download / Admin`) đối với kho riêng `sealed-eval-repo`. Trong khi đó, ở tầng API ứng dụng (`security/g0/rbac-matrix.md`), endpoint `GET /api/v1/evaluation/runs` với partition `sealed_100` chặn `administrator` (`—`) và chỉ cấp quyền xem cho `independent_evaluator` (`✓`), còn `POST /api/v1/evaluation/runs` chỉ cấp cho `independent_evaluator` và `administrator` (ma trận API không cấp quyền truy cập `sealed_100` cho nhóm kỹ sư phát triển).
3. Chỉ **Chủ sở hữu dữ liệu đánh giá / Vận hành kho riêng** (`[S4]` Quý Hải — Read/Write), **Kiểm toán Bảo mật** (`[P5]` Anh Khoa — Audit/Read) và **Đánh giá độc lập** (`[P4]`) được cấp quyền hợp lệ trên `sealed-eval-repo`.

---

## 2. Kết quả kiểm toán Phần 1 — Cô lập Repository chung & 0% PII (Đã hoàn thành)
Kiểm toán tự động trực tiếp trên toàn bộ cây thư mục repository chung (`CRM-Knowledge-and-Policy-Assistant-Purchaser`) thông qua `security/scripts/g1_sealed_acl_audit_runner.py` (đồng bộ `FORBIDDEN_NAME_PATTERNS` từ `scripts/ci_purchaser_guard.py`) và `scripts/ci_purchaser_guard.py`:
- **Tệp cấm theo `FORBIDDEN_NAME_PATTERNS` (`100_sealed`, `sealed_plaintext`, `80_constructed_challenges`, `.env`, keys):** **0 tệp vi phạm**.
- **Rò rỉ bản ghi `sealed_100` / `80_constructed_challenges` trong `Policy_Corpus_G1_Full.csv`:** **0 dòng**.
- **Kết quả chạy `scripts/ci_purchaser_guard.py`:** **PASS** (`0 forbidden files, 0 PII hits, CSV contracts & Sealed redaction OK`).
- **Kết luận Phần 1:** **PASSED**.

---

## 3. Kết quả kiểm toán Phần 2 — Kiểm tra ACL & GitHub Audit Log kho `sealed-eval-repo` (`SUB03`)

| Hạng mục kiểm toán ACL (`sealed-eval-repo`) | Vai trò / Đối tượng | Quyền chuẩn RFP (`Mục 8`, `SEC 01`) | Trạng thái xác minh hiện tại (No-Mock) |
| :--- | :--- | :--- | :--- |
| **Chặn truy cập nhóm phát triển** | `[S2]` Quốc Hưng, `[S3]` Yến Nhi (`CKPA_FORBIDDEN_USERS`) | **Cấm 100%** (0 Read / 0 Clone / 0 Collaborator) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ `[S4]`/`[S5]` xuất JSON/CSV Collaborators & Audit Log từ `sealed-eval-repo`)* |
| **Xác nhận quyền quản trị kho Sealed** | `[S4]` Quý Hải (`CKPA_ALLOWED_USERS`) | **Read / Write** (Quản lý kho đánh giá) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ log JSON/CSV thật từ `SUB03`)* |
| **Xác nhận quyền kiểm toán bảo mật** | `[P5]` Anh Khoa (`CKPA_ALLOWED_USERS`) | **Audit / Read** (Giám sát độc lập) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ log JSON/CSV thật từ `SUB03`)* |

- **Cơ chế chống False Negative:** Script `g1_sealed_acl_audit_runner.py` bắt buộc tệp `CKPA_SEALED_ACL_LOG_PATH` phải là tệp `.json` hoặc `.csv` không rỗng, có trường `actor`/`username`/`login` hợp lệ, đồng thời đối chiếu đầy đủ GitHub username thật qua `CKPA_FORBIDDEN_USERS` và `CKPA_ALLOWED_USERS` trước khi kết luận `PASS_VERIFIED_EXTERNAL_ACL`.

---

## 4. Bằng chứng kỹ thuật & Điều kiện đóng thẻ Jira `CKPA-79`
- **Script kiểm toán No-Mock:** `security/scripts/g1_sealed_acl_audit_runner.py` (hỗ trợ cờ `--strict-external` khi có tệp log JSON/CSV thật của `sealed-eval-repo`).
- **Nhật ký thực thi thật:** `security/g1/g1_sealed_acl_audit_CKPA-79.log`.
- **Trạng thái thẻ Jira `CKPA-79`:** Giữ nguyên **`In Progress`** theo đúng chính sách No-Mock; sẽ cập nhật kết quả `--strict-external`, chuyển `Done` và mở khóa `CKPA-80` (`Tổng hợp DEL03, Giờ W1-3 & Kế hoạch G2`) ngay sau khi `[S4]` Quý Hải / `[S5]` Ngọc Duy xuất log ACL thật từ kho riêng `sealed-eval-repo`.