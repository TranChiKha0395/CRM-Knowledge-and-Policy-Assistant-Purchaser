# BIÊN BẢN ĐỐI SOÁT, PHÊ DUYỆT MẪU DỮ LIỆU G0 (30 PASSAGES + 10 CRITICAL FIELDS) & KẾ HOẠCH HOÀN TẤT CORPUS TRƯỚC GATE G1

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`CKPA`)
- **Mã công việc Jira:** `CKPA-24` — *CRM-G0-ST06: [G0][DAT01] Duyệt mẫu 30+10 & Kế hoạch Curation* kèm `CKPA-25` (SUB16), `CKPA-26` (SUB17), `CKPA-27` (SUB18) (Thuộc Epic `CKPA-3`: *CRM-G0-EP01*)
- **Tham chiếu SRS & RFP:** `SRS-FR-01.4`, `SRS Mục 7.3` | `WP 01`, `DAT 01`, `DAT 06`, `DAT 08`, `VN 03`, `VN 04`, `DEL 01`
- **Chủ trì biên soạn (`[P3] Knowledge Steward`):** Trần Chí Kha (*BA & Policy/Knowledge Steward *)
- **Rà soát độc lập ([S4] Quality Lead):** Phạm Quý Hải (*Trưởng nhóm Chất lượng & Kiểm định độc lập*)
- **Nhánh Git gợi ý:** `chore/CKPA-3-approve-g0-30-passages-and-10-fields`
- **Ngày hoàn tất:** `16/11/2026` (Múi giờ `Asia/Ho_Chi_Minh`)

---

## 1. Tuyên bố Tuân thủ Ranh giới RFP & Đồng bộ Toàn Dự án

1. **Không tự bịa quy tắc chính sách (`RFP Mục 2 & VN 04`):** Toàn bộ `30` đoạn nội dung đại diện đầu tiên (`passages.csv`) và `10` dòng trường chính sách trọng yếu đầu tiên (`critical_fields.csv`) được trích xuất, làm sạch và chuẩn hóa trực tiếp từ `03` văn bản quy trình đã duyệt của SongNhat. Tuyệt đối không tự đặt thêm quy tắc ngoài nguồn để chạy theo hạn ngạch số lượng.
2. **Khớp 100% Hợp đồng Dữ liệu 2 CSV UTF-8 (`CKPA-12` / `erd_and_csv_contracts_revised.md`):**
   - `passages.csv`: Đúng **21 cột chuẩn UTF-8** (`passage_id, document_id, document_version_id, title, content, source_ref, page_number, clause_ref, language, owner, approver, recorded_at, published_at, effective_from, effective_to, scope, audience, status, supersedes, has_essential_attachments, record_action`). Mỗi đoạn `<= 6.000` ký tự Unicode, không cắt cụt âm thầm.
   - `critical_fields.csv`: Đúng **23 cột chuẩn UTF-8** (`field_id, policy_id, policy_version_id, document_version_id, field_name, field_type, operator, value, unit, currency, approval_role, time_limit, exception_condition, required_documents, effective_from, effective_to, scope, audience, source_clause, owner, approver, status, record_action`).
3. **Đồng bộ 100% với Bộ 60 Dev Tasks Công khai (`CKPA-30 / CRM-G0-SUB20` — `[S4] Quality Lead`):**
   - Mọi khóa ngoại `document_id` (`DOC-001..003`), `document_version_id` (`VER-001`), `policy_id` (`POL-001..003`), `passage_id` (`PAS-001..030`) và `field_id` (`CF-001..010`) khớp tuyệt đối với bảng phân vùng `CKPA-10_G0_60_Dev_Tasks_Public_Partition-v2.csv`.

---

## 2. Bảng Đối soát 30 Đoạn Nội dung (`passages.csv`) & 10 Trường Trọng yếu (`critical_fields.csv`)

| Nhóm chính sách (`Policy_ID`) | Mã Tài liệu & Phiên bản | Chủ sở hữu (`Policy Owner`) | Người phê duyệt (`Approver`) | Số đoạn G0 (`passages.csv`) | Dải mã `passage_id` | Số dòng trường (`critical_fields.csv`) | Dải mã `field_id` | Kiểm tra `DAT 08` (Bảng/Chú thích) |
| :--- | :---: | :--- | :--- | :---: | :---: | :---: | :---: | :---: |
| **1. Báo giá và phê duyệt thương mại** (`POL-001`) | `DOC-001` (`VER-001`) | Commercial Policy Owner (`Sales Director`) | Sponsor / Legal & Compliance Director | **10** | `PAS-001` → `PAS-010` | **04** | `CF-001` → `CF-004` | `has_essential_attachments = true` (100%) |
| **2. Xử lý thông tin khách hàng CRM** (`POL-002`) | `DOC-002` (`VER-001`) | CRM Data Governance Owner (`CRM Manager`) | Sponsor / Legal & Compliance Director | **10** | `PAS-011` → `PAS-020` | **04** | `CF-005` → `CF-008` | `has_essential_attachments = true` (100%) |
| **3. Định tuyến dịch vụ / bảo hành** (`POL-003`) | `DOC-003` (`VER-001`) | Warranty Policy Owner (`Service Director`) | Sponsor / Legal & Compliance Director | **10** | `PAS-021` → `PAS-030` | **02** | `CF-009` → `CF-010` | `has_essential_attachments = true` (100%) |
| **TỔNG CỘNG MỐC GATE G0** | **03 Tài liệu** | **Đủ 03 Policy Owners + Backup** | **Đã ký duyệt G0** | **30 / 30** | `PAS-001` → `PAS-030` | **10 / 10** | `CF-001` → `CF-010` | **0 dòng lỗi / 0 dòng thiếu chú thích** |

### Chi tiết 10 Dòng `Critical Fields` đã khóa cứng (`DAT 06`)
| `field_id` | `policy_id` | `source_clause` | `field_type` | `operator` | `value` | `unit` / `currency` | `approval_role` | `time_limit` (SLA) |
| :---: | :---: | :--- | :---: | :---: | :---: | :---: | :--- | :---: |
| `CF-001` | `POL-001` | Điều 2.1, trang 1 (`PAS-004`) | `number` | `<=` | `5` | `%` | `Sales Staff (reader)` | `2 giờ làm việc` |
| `CF-002` | `POL-001` | Điều 2.2, trang 1 (`PAS-005`) | `number` | `between` | `5;15` | `%` | `Sales Manager` | `4 giờ làm việc` |
| `CF-003` | `POL-001` | Điều 2.3–2.5, trang 2 (`PAS-006..008`) | `currency` | `>=` | `1000000000` | `VND` / `VND` | `Sales Director` | `48 giờ làm việc` |
| `CF-004` | `POL-001` | Điều 1.2–1.3, trang 1 (`PAS-002..003`) | `duration` | `<=` | `15` | `ngày làm việc` | `Sales Staff (reader)` | `15 ngày làm việc` |
| `CF-005` | `POL-002` | Điều 1.4–1.5, trang 1 (`PAS-012`) | `duration` | `<=` | `2` | `giờ làm việc` | `CRM Staff (reader)` | `2 giờ làm việc` |
| `CF-006` | `POL-002` | Điều 2.1–2.3, trang 1 (`PAS-014`) | `currency` | `<` | `500000000` | `VND` / `VND` | `CRM Staff (reader)` | `4 giờ làm việc` |
| `CF-007` | `POL-002` | Điều 2.4 & 2.6–2.7, trang 2 (`PAS-016, 018`) | `currency` | `>=` | `500000000` | `VND` / `VND` | `CRM Manager` | `4 giờ làm việc` |
| `CF-008` | `POL-002` | Điều 2.5, trang 2 (`PAS-017`) | `duration` | `<=` | `1` | `giờ` | `CRM Director` | `1 giờ` |
| `CF-009` | `POL-003` | Điều 1.2–2.1 & 2.4 (`PAS-021, 023, 026`) | `number` | `<=` | `37` | `kW` | `Internal Tech Lead` | `4 giờ làm việc` |
| `CF-010` | `POL-003` | Điều 2.2–2.3, trang 2 (`PAS-024..025`) | `number` | `>` | `37` | `kW` | `Vendor Chief Engineer` | `4 giờ làm việc` |

---

## 3. Kiểm tra Đầy đủ Bảng, Sơ đồ & Chú thích Thiết yếu (`DAT 08` & `VN 03`)

- **Rà soát thủ công trước nhập liệu (`VN 03`):** Trong Base Scope, hệ thống không dùng OCR hay parser bảng PDF tự động. `[P3] Knowledge Steward` đã chuyển đổi thủ công toàn bộ bảng phân cấp chiết khấu, bảng chứng từ xác minh pháp lý và bảng phân tuyến công suất động cơ (`<= 37 kW` vs `> 37 kW`) thành văn bản có cấu trúc UTF-8 kèm dòng `critical_fields` tương ứng.
- **Trạng thái cờ `has_essential_attachments`:** Cả `30/30` đoạn mẫu G0 đều đã đính kèm đầy đủ nội dung chú thích ngoại lệ vào trường `content` và `exception_condition` (`has_essential_attachments = true`).
- **Quy tắc kiểm thử Quarantine (`OPS 01 / DAT 08`):** Khi sang `Gate G1` (`CKPA-13` & `CKPA-16`), bộ test fixture sẽ bổ sung riêng các dòng kiểm thử có `has_essential_attachments = false`, thiếu `currency` khi `field_type = currency`, hoặc độ dài `> 6.000` ký tự Unicode để chứng minh hệ thống tự động đẩy vào bảng `QUARANTINE_ROWS` và kích hoạt `HOLD_DAT08`.

---

## 4. Kế hoạch Có Ngân sách Hoàn tất Kho Tri thức Chuẩn trước Cổng `Gate G1` (`CKPA-16`)

Theo yêu cầu `SRS-FR-01.4` và `RFP Mục 2.2`, phần dữ liệu còn lại của 3 nhóm chính sách (tối đa `<= 30` tài liệu, `<= 300` đoạn `passages`, `<= 50` dòng `critical_fields`) được lập kế hoạch nhân sự, thời gian và ngân sách giờ công cụ thể để hoàn tất trước ngày chốt `Gate G1 (10/12/2026)`:

| Đợt Curation (Tuần dự án) | Thời gian thực hiện | Hạng mục mở rộng (Thực tế từ nguồn được phép, không bịa rule) | Khối lượng mục tiêu lũy kế | Nhân sự thực hiện & Duyệt | Ngân sách giờ công (`Original Estimate`) |
| :--- | :---: | :--- | :---: | :--- | :---: |
| **Mốc G0 (Hiện tại — `CKPA-24`)** | `10/11 – 17/11/2026` | 03 văn bản chính sách cốt lõi (`DOC-001..003`), đủ 9 Worked Cases cơ sở | **03** docs / **30** passages / **10** critical fields | `[P3]` (Soạn) + `[S4]` (Rà độc lập) + `[P2]` / `Policy Owners` (Duyệt) | **16h** (Đã hoàn tất 100%) |
| **Đợt 1 G1 (Tuần 3 — `CKPA-16`)** | `20/11 – 26/11/2026` | Mở rộng nhóm **Báo giá & Thương mại (`POL-001`)**: SOP báo giá dự án nhà máy, phụ lục chiết khấu theo dòng biến tần/hộp giảm tốc, phiên bản lịch sử `superseded` (`VER-000`) và phiên bản tương lai `scheduled` (`VER-002`) | **10** docs / **110** passages / **22** critical fields | `[P3]` (10h) + `[P2]` (3h điều phối Owner) | **13h** |
| **Đợt 2 G1 (Tuần 4 — `CKPA-16`)** | `27/11 – 01/12/2026` | Mở rộng nhóm **Xử lý thông tin KH (`POL-002`)**: SOP xác minh đại lý cấp 1/2, mẫu hợp đồng khung B2B có điều khoản xung đột (`customer_contract`), ghi chú lịch sử (`staff_note`) | **20** docs / **200** passages / **36** critical fields | `[P3]` (10h) + `[P2]` (2h điều phối Owner) | **12h** |
| **Đợt 3 G1 (Tuần 4–5 — `CKPA-16`)** | `02/12 – 04/12/2026` | Mở rộng nhóm **Dịch vụ & Bảo hành (`POL-003`)**: Điều khoản bảo hành hãng sản xuất (`manufacturer_terms`), ma trận lỗi bo mạch/cơ khí, đối soát Manifest 100% qua 2 CSV Validators (`CKPA-13`) | **<= 30** docs / **<= 300** passages / **<= 50** critical fields | `[P3]` (5h) + `[S4]` (3h đối soát nhãn đôi) + `[S2]` (2h import) | **10h** |
| **TỔNG NGÂN SÁCH CURATION G0 → G1** | **Hoàn tất 04/12/2026** | **Đạt 100% điều kiện Cổng `Gate G1 - Controlled Offline`** | **<= 30 Docs / <= 300 Passages / <= 50 Fields** | **`[P3]`, `[P2]`, `[S4]`, `[S2]` & `Policy Owners`** | **51 giờ công** (`16h` G0 + `35h` G1) |

---

## 5. Xác nhận Phê duyệt Cổng G0 (`Sign-off Record`)

- **Người biên soạn & Chuẩn hóa (`[P3] Knowledge Steward` — Policy & Knowledge Steward):** Trần Chí Kha — *Đã kiểm tra UTF-8, khớp 21/23 cột và truy vết 100% về điều khoản gốc.*
- **Người rà soát độc lập ([S4] Quality Lead — Trưởng nhóm Kiểm định Độc lập):** Phạm Quý Hải — *Đã đối soát khớp 100% với bộ 60 Dev Tasks (`CKPA-30 (CRM-G0-SUB20)`), đạt đồng thuận nhãn đôi (`Cohen's Kappa >= 0.80`).*
- **Chủ sở hữu Chính sách (`Policy Owners` — 3 Nhóm chính sách):** *Đồng ý phê duyệt 30 đoạn + 10 dòng trường trọng yếu đầu tiên và ngân sách hoàn tất corpus trước G1.*
