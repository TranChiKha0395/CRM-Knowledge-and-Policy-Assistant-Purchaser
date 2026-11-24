# BIÊN BẢN KIỂM TOÁN ACL KHO SEALED (`sealed-eval-repo`) & CHỐT BẢO MẬT GATE G1

- **Mã công việc Jira:** `CKPA-79` (Parent: `CKPA-44` | Mở khóa: `CKPA-80` | Liên quan hồ sơ DEL 03: `CKPA-77`)
- **Mã truy vết RFP & Cổng G1:** Mục 8, Mục 11, `SEC 01`, `SEC 02`, `SEC 06`, `SEC 08` | Tiêu chí: `G1-AC04`, `G1-AC07`
- **Phân hệ kiểm thử:** `SUB03` (`sealed-eval-repo`) & Môi trường Test
- **Chủ trì thực hiện & Ký chứng nhận:** `[P5]` Anh Khoa (*Privacy and security owners*)
- **Phối hợp RACI:** `[S4]` Quý Hải, `[S5]` Ngọc Duy | **Reviewer:** `[P3]` Chí Kha | **Nghiệm thu:** `[P1]` Mỹ Vân
- **Chính sách kiểm toán:** **No-Mock** (Đối chiếu trực tiếp trên repository thật & file xuất log ACL thật từ `SUB03`; tuyệt đối không tạo dữ liệu giả lập)

---

## 1. Mục tiêu & Nguyên tắc tách biệt nhiệm vụ (SoD — RFP Mục 8, Mục 11 & `SEC 06`)
1. Bảo đảm kho đánh giá độc lập **`sealed-eval-repo`** (`SUB03`) lưu trữ bộ **100 Sealed Acceptance Cases** được cô lập hoàn toàn khỏi repository phát triển chung.
2. Xác nhận **0 lượt truy cập (Read / Clone / Download / Admin)** của nhóm kỹ sư phát triển **`[S2]` Quốc Hưng** và **`[S3]` Yến Nhi** vào `sealed-eval-repo`.
3. Xác nhận **0% dữ liệu cá nhân (PII)** trái phép trong toàn bộ repository chung và môi trường Test (`SEC 02`, `G1-AC04`).
4. Cung cấp bằng chứng kiểm toán ACL hợp lệ phục vụ tổng hợp Hồ sơ Bằng chứng `DEL 03` (`CKPA-77`) và mở khóa `CKPA-80`.

---

## 2. Kết quả kiểm toán Phần 1 — Cô lập Repository chung & Kiểm soát 0% PII (Thực thi tự động)
Thực thi trực tiếp qua script `security/scripts/g1_sealed_acl_audit_runner.py` và `scripts/ci_purchaser_guard.py`:

| Hạng mục kiểm toán | Phương pháp kiểm chứng | Kết quả thực tế | Trạng thái |
| :--- | :--- | :--- | :---: |
| **Cô lập tệp Sealed khỏi repo chung (`SEC 06`)** | Quét đệ quy toàn bộ cây thư mục repository & `Policy_Corpus_G1_Full.csv` | **0 tệp** & **0 bản ghi** Sealed lọt vào repo chung | **PASS** |
| **Kiểm soát 0% PII & tệp cấm (`SEC 02`, `G1-AC04`)** | Thực thi `scripts/ci_purchaser_guard.py` | **0 forbidden files, 0 PII hits**, CSV contracts & Sealed redaction OK | **PASS** |
| **Ranh giới phân quyền RBAC (`SEC 01`, `CKPA-70`)** | Đối chiếu `security/g0/rbac-matrix.md` & audit `CKPA-70` | `administrator` và nhóm kỹ sư phát triển bị chặn (`—`) trên `sealed_100` | **PASS** |

---

## 3. Kết quả kiểm toán Phần 2 — Cấu hình ACL & Access Logs kho ngoài `sealed-eval-repo` (`SUB03`)

| Đối tượng / Role | Vai trò dự án | Quyền yêu cầu theo RFP (`SEC 06`) | Trạng thái kiểm chứng hiện tại (No-Mock) |
| :--- | :--- | :--- | :--- |
| **`[S2]` Quốc Hưng** | Integration engineer | **No Access** (0 Read / 0 Clone) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ export GitHub Audit Log từ `[S4]`/`[S5]`)* |
| **`[S3]` Yến Nhi** | Retrieval & app engineer | **No Access** (0 Read / 0 Clone) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ export GitHub Audit Log từ `[S4]`/`[S5]`)* |
| **`[S4]` Quý Hải** | Quality lead | **Read / Write** (Chủ trì kiểm định độc lập) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ xác nhận danh sách Collaborators từ `[S4]`)* |
| **`[P5]` Anh Khoa** | Privacy & security owner | **Audit / Read** (Kiểm toán ACL độc lập) | **BLOCKED_EXTERNAL_REPO_ACCESS** *(Chờ cấp quyền audit hoặc bản xuất log ACL)* |

> **Cơ chế xác minh tự động khi nhận log từ `SUB03`:** Ngay khi `[S4]` Quý Hải hoặc `[S5]` Ngọc Duy xuất tệp GitHub Collaborators / Audit Log của kho `sealed-eval-repo`, `[P5]` sẽ chạy lại `python security/scripts/g1_sealed_acl_audit_runner.py --strict-external` với biến môi trường `CKPA_SEALED_ACL_LOG_PATH` để đối soát 0 lượt Read/Clone của `S2`/`S3` mà không sửa mã nguồn.

---

## 4. Xác nhận & Chốt Bảo mật Gate G1 (`[P5]` Ký)
- **Phần 1 — Cô lập dữ liệu repo chung & 0% PII (`G1-AC04`):** **ĐẠT (PASS)** — Đã xác minh tự động bằng script trên repository thật.
- **Phần 2 — Kiểm toán Access Logs kho ngoài `sealed-eval-repo` (`SUB03`):** **CHỜ BỔ SUNG EXPORT LOG TỪ `SUB03`** (`BLOCKED_EXTERNAL_REPO_ACCESS`) trước khi đóng hoàn toàn `CKPA-79` và mở khóa `CKPA-80`.
- **Chữ ký xác nhận kiểm toán Gate G1:** `[P5]` Anh Khoa — *Privacy and Security Owner*.