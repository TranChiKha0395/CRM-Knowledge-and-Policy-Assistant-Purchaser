# BIÊN BẢN KIỂM TOÁN ACL KHO SEALED & CHỐT BẢO MẬT GATE G1

- **Mã công việc Jira:** `CKPA-79` (Parent: `CKPA-44` | Chặn / Mở khóa: `CKPA-80` | Liên quan: `CKPA-77`)
- **Mã truy vết RFP & Tiêu chí G1:** `Mục 8`, `Mục 11`, `SEC 01`, `SEC 02`, `SEC 06` *(Ghi chú: mã `SEC 08` trên thẻ Jira cũ là mã import từ bảng Jira; theo RFP chuẩn của dự án, `SEC 08` thuộc kiểm soát thay đổi provider/model/prompt/selector và rollback nên không áp dụng cho task ACL kho Sealed này)* | Tiêu chí: `G1-AC04`, `G1-AC07`
- **Phân hệ thực hiện:** `SUB03` (Evaluation — kho riêng `sealed-eval-repo`) & Repository chung Purchaser
- **Chủ trì thực hiện:** `[P5]` Anh Khoa (Privacy & Security Owner)
- **Phối hợp RACI:** `[S4]` Quý Hải, `[S5]` Ngọc Duy (xuất JSON/CSV Collaborators, Team Permissions & GitHub Audit Log của `sealed-eval-repo`), `[P4]` Independent Evaluator | **Review:** `[P3]` Chí Kha
- **Chính sách kiểm thử:** **No-Mock** (100% quét dữ liệu thật trong repository chung và yêu cầu trích xuất JSON/CSV thật từ GitHub Collaborators/Team Permissions & Audit Log của kho riêng `sealed-eval-repo`, đối soát theo GitHub username thật qua `CKPA_FORBIDDEN_USERS`, `CKPA_S4_USERS`, `CKPA_P5_USERS`; tuyệt đối không giả lập log truy cập)

---

## 1. Mục tiêu & Nguyên tắc tách biệt Chinese Wall (`Mục 8`, `Mục 11`, `SEC 01`, `SEC 06`)
Theo kiến trúc tách biệt đánh giá độc lập (`Chinese Wall` / `SoD`) của dự án **SongNhat SCRM**:
1. Toàn bộ **`100 Sealed Acceptance Cases`** và **`80 Constructed Challenges`** phải được lưu trữ cô lập tuyệt đối tại repository riêng **`sealed-eval-repo`** (`SUB03`), hoàn toàn tách khỏi repository phát triển chung.
2. **Nhóm kỹ sư phát triển** (`[S2]` Quốc Hưng — Backend/RAG, `[S3]` Yến Nhi — Retrieval/App) có **0% quyền truy cập** (`Read / Write / Clone / Org-Team Inherited`) đối với kho riêng `sealed-eval-repo`. Ở tầng API ứng dụng (`security/g0/rbac-matrix.md`), endpoint `GET /api/v1/evaluation/runs` với partition `sealed_100` chặn `administrator` (`—`) và chỉ cấp quyền xem cho `independent_evaluator` (`✓`), còn `POST /api/v1/evaluation/runs` chỉ cấp cho `independent_evaluator` và `administrator` (ma trận API không cấp quyền truy cập `sealed_100` cho nhóm kỹ sư phát triển).
3. Chỉ **Chủ sở hữu dữ liệu đánh giá / Vận hành kho riêng** (`[S4]` Quý Hải — `write`/`maintain`/`admin`), **Kiểm toán Bảo mật** (`[P5]` Anh Khoa — `read`/`audit`) và **Đánh giá độc lập** (`[P4]`) được cấp quyền hợp lệ trên `sealed-eval-repo`.

---

## 2. Kết quả kiểm toán Phần 1 — Cô lập Repository chung & 0% PII (Status: `PASS`)
Kiểm toán tự động trực tiếp trên toàn bộ cây thư mục repository chung (`CRM-Knowledge-and-Policy-Assistant-Purchaser`) thông qua `security/scripts/g1_sealed_acl_audit_runner.py` và `scripts/ci_purchaser_guard.py`:
- **Xác minh tồn tại G1 Corpus chuẩn (`data/g1/full/Policy_Corpus_G1_Full.csv`):** **Có (`True`)**.
- **Tệp cấm theo `FORBIDDEN_NAME_PATTERNS` (`100_sealed`, `sealed_plaintext`, `80_constructed_challenges`, `.env`, keys):** **0 tệp vi phạm**.
- **Symlink trỏ ra ngoài repository:** **0 vi phạm**.
- **Quét toàn bộ tệp `.csv`/`.json`/`.txt`/`.tsv` tìm bản ghi `sealed_100` / `80_constructed_challenges` chưa ẩn:** **0 dòng rò rỉ**.
- **Kết quả chạy `scripts/ci_purchaser_guard.py`:** **PASS** (`0 forbidden files, 0 PII hits, CSV contracts & Sealed redaction OK`).

---

## 3. Kết quả kiểm toán Phần 2 — Kiểm tra ACL & GitHub Audit Log kho `sealed-eval-repo` (`SUB03`) (Status: `BLOCKED`)

| Hạng mục kiểm toán ACL (`sealed-eval-repo`) | Vai trò / Đối tượng & Biến môi trường | Quyền chuẩn RFP (`Mục 8`, `SEC 01`) | Trạng thái xác minh hiện tại (No-Mock) |
| :--- | :--- | :--- | :--- |
| **Chặn quyền trực tiếp & kế thừa Team nhóm phát triển** | `[S2]` Quốc Hưng, `[S3]` Yến Nhi (`CKPA_FORBIDDEN_USERS`) | **Cấm 100%** (0 Collaborator / 0 Org-Team / 0 truy cập thành công) | **BLOCKED** (`BLOCKED_EXTERNAL_REPO_ACCESS` — chờ `[S4]`/`[S5]` xuất JSON/CSV thật từ `sealed-eval-repo`) |
| **Xác nhận quyền quản trị kho Sealed** | `[S4]` Quý Hải (`CKPA_S4_USERS`) | **Read / Write** (`write` / `maintain` / `admin`) | **BLOCKED** (Chờ log JSON/CSV thật từ `SUB03`) |
| **Xác nhận quyền kiểm toán bảo mật** | `[P5]` Anh Khoa (`CKPA_P5_USERS`) | **Audit / Read** (`read` / `triage` / `audit`) | **BLOCKED** (Chờ log JSON/CSV thật từ `SUB03`) |
| **Chặn tài khoản lạ ngoài danh sách phê duyệt** | Mọi tài khoản ngoài `CKPA_S4_USERS` $\cup$ `CKPA_P5_USERS` $\cup$ `CKPA_EXTRA_APPROVED_USERS` (`[P4]`) | **Cấm 100%** | **BLOCKED** (Chờ log JSON/CSV thật từ `SUB03`) |

- **Schema xuất dữ liệu bắt buộc từ `sealed-eval-repo`:** Tệp `.json` hoặc `.csv` không rỗng, có đủ 5 trường bắt buộc (`record_type`, `repository`, `actor`, `permission_or_action`, `outcome`), không trùng lặp bản ghi, phân biệt rõ `collaborator`/`team_permission` với `audit_event` (`allowed` vs `denied`), và đối chiếu SHA-256 nguồn xuất.
- **Bộ kiểm thử tự động (Unit & Negative Tests):** Đã bổ sung `security/scripts/test_g1_sealed_acl_audit_runner.py` (10/10 test cases kiểm chứng đầy đủ các kịch bản `PASS`, `BLOCKED`, `FAIL`, `PARTIAL_PASS`).

---

## 4. Kết luận tổng thể (`OVERALL VERDICT: PARTIAL_PASS`) & Điều kiện đóng Jira `CKPA-79`
- **Trạng thái hiện tại:** **`PARTIAL_PASS`** (`Part 1 = PASS`, `Part 2 = BLOCKED` do chưa được cấp tệp JSON/CSV export từ kho ngoài `sealed-eval-repo`, `0%` dữ liệu giả lập).
- **Trạng thái thẻ Jira `CKPA-79`:** Giữ nguyên **`In Progress`**; sẽ chạy `--strict-external` để đạt `OVERALL VERDICT: PASS`, chuyển `Done` và mở khóa `CKPA-80` ngay sau khi nhận được JSON/CSV Collaborators & Audit Log thật của `sealed-eval-repo` từ `[S4]` Quý Hải / `[S5]` Ngọc Duy.