# BIÊN BẢN KIỂM LẠI 100% `SOURCE_URI`, `DAT 08` & KÝ XÁC NHẬN `G1-AC01` (GATE G1)

- **Mã công việc Jira:** `CKPA-82` (Mã Excel: `CRM-G1-SUB28` | Gate: `Gate G1` | Tiêu chí: `G1-AC01`)
- **Truy vết RFP:** Mục 9 (*G1 re-verified original reference access*), `DAT 08`, `KNW 02`, `DAT 01–07`, `KNW 03`, `SEC 01–02`
- **Chủ trì thực hiện & Ký xác nhận:** `[P3]` Trần Chí Kha (*Knowledge and Data Steward*)
- **Nghiệm thu / Reviewer (`review-p2`):** `[P2]` Lý Hữu Tài (*Policy Owner*)
- **Phối hợp RACI:** `[P4]` Ngô Thị Trà My (*Staff Users*)
- **Ngày kiểm lại & ký chốt:** `2026-11-24` (Múi giờ `Asia/Ho_Chi_Minh`)
- **Phạm vi:** Base Scope thuần túy (`O1 = OFF`), 0% PII thật

---

## 1. Mục tiêu & Phạm vi Kiểm lại (Re-Verification)
Thực hiện kiểm tra chéo độc lập lần cuối (sau toàn bộ các bản chỉnh sửa Sprint 4, PR #32 `CKPA-58`, PR #40 `CKPA-62`, PR #42 `CKPA-66` và PR #51) trên toàn bộ bộ Corpus Gate G1 cuối cùng nhằm:
1. Xác nhận **100% liên kết tài liệu gốc (`source_uri`)** tồn tại thật, mở xem trực tiếp thành công, đúng phiên bản và khớp mã băm `SHA-256` (`Mục 9 G1 re-verified original reference access`).
2. Rà soát toàn vẹn cờ bảng biểu/chú thích thiết yếu **`DAT 08`** (`has_essential_attachments`) và đối soát cân bằng Quarantine (`Expected = Accepted + Quarantined`).
3. Xác nhận tuân thủ trần quy mô Base Scope G1 (`<= 30` tài liệu / `<= 300` đoạn / `<= 50` trường trọng yếu) và quy định lưu hành nội bộ **`KNW 02`**.

---

## 2. Kết quả Kiểm định Tự động trên Bản Corpus Cuối cùng
Thực thi trực tiếp `data/g1/scripts/validate_g1_repo.ps1` và đối chiếu tệp thực tế trên đĩa (xem nhật ký chạy thật tại `data/g1/reports/CKPA-82_source_uri_dat08_reverify.log`):

| Hạng mục kiểm định | Ngưỡng yêu cầu RFP / G1 | Kết quả đo thực tế | Trạng thái |
| :--- | :--- | :--- | :---: |
| **Số lượng tài liệu gốc (`DOC-001..011`)** | `<= 30` tài liệu (Base Scope) | **11 / 30** tài liệu (đủ 3 họ `POL-001`, `POL-002`, `POL-003` & 5 lớp thẩm quyền `DAT 03`) | **PASS** |
| **Số lượng đoạn văn (`Policy_Corpus_G1_Full.csv`)** | `<= 300` đoạn; `<= 6,000` ký tự Unicode/đoạn | **96 / 300** đoạn (`max = 591 / 6,000` ký tự Unicode, đúng 21 cột UTF-8) | **PASS** |
| **Số lượng trường trọng yếu (`Critical_Fields_G1_Full.csv`)** | `<= 50` trường; đúng 23 cột UTF-8 | **40 / 50** trường (đúng 23 cột UTF-8, `Accepted = 40`, `Quarantined = 0`) | **PASS** |
| **Kiểm lại 100% `source_uri` & `SHA-256` Manifest** | 100% tệp tồn tại, 0 link gãy, 0 lệch hash | **136 / 136** bản ghi Full Corpus & **56 / 56** bản ghi Family 1 khớp 100% (`0` missing, `0` hash mismatch) | **PASS** |
| **Kiểm soát `DAT 08` (`has_essential_attachments`)** | Cách ly Quarantine 100% đoạn thiếu bảng/chú thích | **96 = 93 Accepted (`true`) + 3 Quarantined (`false`)** (`PAS-040`, `PAS-066`, `PAS-082`) | **PASS** |
| **Phủ 7/7 trạng thái vòng đời `KNW 03`** | Đủ 7 trạng thái | `effective (78)`, `superseded (5)`, `scheduled (4)`, `withdrawn (3)`, `approved (2)`, `draft (2)`, `owner_reviewed (2)` | **PASS** |
| **Phân quyền `SEC 01` & Lưu hành nội bộ `KNW 02`** | 0% PII thật; chỉ dùng nội bộ CRM; không xuất ra KH | **7** đoạn hạn chế RBAC; **0 Real PII hits** trên 24 tệp `data/g1/`; 100% gắn ngữ cảnh nội bộ SongNhat | **PASS** |

---

## 3. Bảng Đối soát 11/11 Tệp Tài liệu Gốc (`source_uri` & `SHA-256`)

| STT | Mã tài liệu | Họ / Lớp `DAT 03` | Đường dẫn thực tế (`source_uri`) | Dung lượng (bytes) | `SHA-256` (16 ký tự đầu) | Mở xem & `DAT 08` |
| :---: | :---: | :--- | :--- | :---: | :---: | :---: |
| 1 | `DOC-001` | `POL-001` / Layer 1 (Policy) | `data/g1/sources/DOC-001_POL-CRM-01_Quotation_Commercial_Approval.md` | 31,258 | `246725539d0f01ce` | **VERIFIED** *(1 ca test Quarantine `PAS-040`)* |
| 2 | `DOC-002` | `POL-002` / Layer 1 (Policy) | `data/g1/sources/DOC-002_POL-CRM-03_Customer_Information_Handling.md` | 24,191 | `654dd44afa8ec5c8` | **VERIFIED** *(1 ca test Quarantine `PAS-066`)* |
| 3 | `DOC-003` | `POL-003` / Layer 1 (Policy) | `data/g1/sources/DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md` | 22,631 | `81cc609892000169` | **VERIFIED** *(1 ca test Quarantine `PAS-082`)* |
| 4 | `DOC-004` | `POL-001` / Layer 2 (SOP) | `data/g1/sources/DOC-004_SOP-CRM-QBG-01_Discount_GrossMargin.md` | 5,537 | `93336ddb79a56eda` | **VERIFIED** |
| 5 | `DOC-005` | `POL-002` / Layer 2 (SOP) | `data/g1/sources/DOC-005_SOP-CRM-KH-01_Customer_Verification_Update.md` | 4,602 | `e3296e762cfcf52a` | **VERIFIED** |
| 6 | `DOC-006` | `POL-001` / Layer 3 (Contract) | `data/g1/sources/DOC-006_HDNT-B2B-SYN-2026_Framework_Contract.md` | 3,820 | `a662b6fe30ac68ce` | **VERIFIED** |
| 7 | `DOC-007` | `POL-001` / Layer 4 (Staff Note) | `data/g1/sources/DOC-007_CRM-STAFF-NOTES-SYN_Quotation_History.md` | 3,699 | `8cd126e1764b6185` | **VERIFIED** |
| 8 | `DOC-008` | `POL-002` / Layer 3 (DPA) | `data/g1/sources/DOC-008_DPA-B2B-SYN-2026_Customer_Data_Addendum.md` | 2,758 | `9e3d25e1c7ea3323` | **VERIFIED** |
| 9 | `DOC-009` | `POL-003` / Layer 2 (SOP) | `data/g1/sources/DOC-009_SOP-CRM-BH-01_Warranty_Intake_Routing.md` | 4,554 | `e909cb8af362af9d` | **VERIFIED** |
| 10 | `DOC-010` | `POL-003` / Layer 5 (OEM Terms) | `data/g1/sources/DOC-010_OEM-TERMS-SYN-2026_Manufacturer_Warranty_Terms.md` | 2,867 | `43e9f0eed5f92b7e` | **VERIFIED** |
| 11 | `DOC-011` | `POL-003` / Layer 4 (Staff Note) | `data/g1/sources/DOC-011_CRM-STAFF-NOTES-BH_Warranty_History.md` | 2,666 | `5e225806bd3e8bd1` | **VERIFIED** |

---

## 4. Rà soát Cờ `DAT 08` & Đối chiếu chéo `CKPA-66` (`UAT`)
1. **3 ca kiểm thử cách ly `DAT 08` (`has_essential_attachments=false`) xác nhận đúng thiết kế:**
   - `PAS-040` (`DOC-001`): *Bảng chiết khấu bậc thang Đại lý Cấp 1 (Thiếu Chú thích Bảng `DAT 08`)* → Quarantined.
   - `PAS-066` (`DOC-002`): *Phụ lục Bảng phân quyền xuất dữ liệu đối tác (Thiếu Chú thích `DAT 08`)* → Quarantined.
   - `PAS-082` (`DOC-003`): *Phụ lục Danh mục Linh kiện Hao mòn Loại trừ (Thiếu Chú thích `DAT 08`)* → Quarantined.
2. **Đối chiếu chéo với `uat/g1/ckpa-66/source_uri_inspection_log.csv` (`CKPA-66`):** Khớp 100% trạng thái `VERIFIED_ACCESSIBLE` cho cả 11/11 tài liệu gốc.

---

## 5. Xác nhận & Ký duyệt Tiêu chí `G1-AC01`

| Vai trò | Thành viên | Nội dung xác nhận | Trạng thái |
| :--- | :--- | :--- | :---: |
| **Người thực hiện & Ký `G1-AC01` (`[P3]`)** | **Trần Chí Kha** (*Knowledge & Data Steward*) | Xác nhận 100% `source_uri` (11/11 tệp, 136/136 manifest SHA-256), `DAT 08` (93 Accepted + 3 Quarantined) và `KNW 02` đạt chuẩn **`G1-AC01`** | **ĐÃ KÝ (2026-11-24)** |
| **Nghiệm thu (`[P2]` — `review-p2`)** | **Lý Hữu Tài** (*Policy Owner*) | Đối chiếu & nghiệm thu `CKPA-82` để mở khóa `CKPA-83` | **CHỜ DUYỆT (`In Review`)** |
