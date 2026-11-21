# CÔNG TY CỔ PHẦN THIẾT BỊ CÔNG NGHIỆP SONG NHẬT (PURCHASER)
**DỰ ÁN: CRM KNOWLEDGE & POLICY ASSISTANT (CKPA / SCRM) — CỔNG G0**  
*Mã Story cha:* `CKPA-40` (CRM-G0-ST10) | *Mã Sub-task:* `CKPA-42` (CRM-G0-SUB29)  
*Mã Tiêu chí Cổng G0:* `G0-AC07`  
*GitHub Branch:* `—` (Tác vụ thẩm định / ban hành văn bản phi mã nguồn)  
*Phía RFP:* Purchaser  
*Priority:* Highest  
*Components (RFP):* Gate-G0  
*RFP Traceability ID:* Mục 9 (G0), Mục 12 (10% payment), Mục 14 (Decisions before award)  
*Deliverable / Evidence:* Biên bản Nghiệm thu G0, Quyết định Base/O1 & Lệnh Thanh toán 10%  
*Assignee / Lead:* `[P1] Mỹ Vân (Purchaser sponsor / Product Owner)`  
*Reporter / Nghiệm thu (PO/SM):* `[S1] Hoàng Tiến (Named lead / Scrum Master)`  
*Collaborators / RACI:* Toàn bộ P1..P5 & S1..S5  
*Lịch thực hiện:* 2026-11-20 → 2026-11-20 (Story Points: — | Original Estimate: 4h)  

---

# BIÊN BẢN NGHIỆM THU CỔNG G0 (READY TO BUILD)
### QUYẾT ĐỊNH BASE SCOPE, QUYẾT ĐỊNH RIÊNG TÙY CHỌN O1 & LỆNH GIẢI NGÂN THANH TOÁN 10% HỢP ĐỒNG (MỤC 12)

---

### ĐỐI SOÁT TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA BDD: GIVEN - WHEN - THEN)

* **GIVEN (Điều kiện tiền đề):** Đã tiếp nhận Phiếu thẩm định SUB28 (`CKPA-41`) do `[S1] Hoàng Tiến` đệ trình và `[P2] Hữu Tài` chủ trì chuyên môn, xác nhận hồ sơ đề xuất đạt **88.45 / 100 điểm** theo RFP Mục 13 và vượt qua toàn bộ 7 tình huống demo bắt buộc.
* **WHEN (Hành động thực thi):** `[P1] Mỹ Vân` (Purchaser sponsor / PO) chủ trì Hội đồng thẩm định Cổng G0 cùng toàn thể 10 thành viên hai bên (P1..P5 & S1..S5) vào ngày **20/11/2026** để ra quyết định Go/Stop và Tùy chọn O1.
* **THEN (Kết quả đầu ra):** Ban hành đầy đủ 3 văn kiện pháp lý bắt buộc:
  1. **Biên bản G0 Sign-off** phê duyệt Base Scope (Go Route 3 — Bounded Custom Work);
  2. **Quyết định riêng bằng văn bản số `03/2026/QĐ-P1-OPT1`** về việc Tạm hoãn Tùy chọn O1 nhằm bảo vệ 100% dữ liệu PII;
  3. **Lệnh giải ngân thanh toán mốc 10% G0** (tương đương 10.000.000 VND) theo đúng Mục 12 RFP.

---

### I. ĐỐI SOÁT 7 NHÓM BẰNG CHỨNG SẴN SÀNG CỔNG G0 (RFP MỤC 9 & MỤC 14)

| STT | Nhóm bằng chứng Cổng G0 | Căn cứ RFP | Hồ sơ / Deliverable đối soát | Kết quả thẩm định của P1 |
|:---:|---|---|---|:---:|
| **1** | **Xác nhận 3 Họ chính sách** | `DAT 03, VN 04` | POL-001 (Báo giá & Duyệt thương mại), POL-002 (Xử lý thông tin KH), POL-003 (Dịch vụ & Bảo hành). Đã ký Ma trận Thẩm quyền, loại trừ 5 mảng ngoài scope. | **ĐẠT (100%)** |
| **2** | **Mẫu duyệt 30 passages + 10 critical fields** | `DAT 01, DAT 06` | Bộ mẫu đại diện 30 passages + 10 critical rows đã nghiệm thu tại CKPA-24/27; đối soát toàn vẹn SHA-256 (DEL01-C). | **ĐẠT (100%)** |
| **3** | **Năng lực Curation & Kinh phí trước G1** | `Mục 2, DEL 05` | Khoản mục 2 trong Báo giá DEL 05 đã duyệt kinh phí 8.000.000 VND hỗ trợ chuẩn hóa nguồn; cam kết hoàn tất trước G1. | **ĐẠT (100%)** |
| **4** | **Ma trận Thẩm quyền & Quy tắc Ngày** | `DAT 03, DAT 04` | Đã ký Ma trận thẩm quyền 5 lớp nguồn; quy tắc ngày chi phối giao dịch theo múi giờ Việt Nam (`Asia/Ho_Chi_Minh`, UTC+7). | **ĐẠT (100%)** |
| **5** | **Question Inventory & Baseline Effort** | `WP 01, VN 06` | Hồ sơ 4 tuần câu hỏi thực tế (DEL01-A); đo baseline 7,0 phút thủ công vs 4,0 phút có trợ lý (tiết kiệm 3 phút/tác vụ), 5 NSD chuẩn Mục 11. | **ĐẠT (100%)** |
| **6** | **So sánh 3 Route có giá & TCO** | `WP 01, DEL 05` | Báo cáo so sánh 3 phương án (searchable library, configured product, custom có giới hạn); phân tích TCO 3 năm (DEL01-I & DEL 05); chọn Route 3. | **ĐẠT (100%)** |
| **7** | **Quyết định riêng cho Tùy chọn O1** | `DAT 07, VN 03` | Ban hành Quyết định riêng số `03/2026/QĐ-P1-OPT1`: Tạm hoãn Tùy chọn O1 ở G0, chỉ triển khai thuần túy Base Scope (2 CSV). | **ĐẠT (100%)** |

---

### II. BỘ QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1] MỸ VÂN

#### 1. QUYẾT ĐỊNH BASE SCOPE (GO / STOP):
* **QUYẾT ĐỊNH: CHẤP THUẬN (GO BASE SCOPE).**
* Cho phép dự án chính thức đóng Giai đoạn Khảo sát (Discovery G0) và chuyển sang Giai đoạn Xây dựng Lõi có kiểm soát (**Gate G1 — Controlled Offline Implementation**).
* **Lộ trình thực hiện:** Phê duyệt lựa chọn **Phương án 3 (Bounded Custom Work)** kết hợp tái sử dụng các thành phần nguồn mở có sẵn (FastAPI, PostgreSQL pgvector + unaccent, Redis) để đảm bảo toàn quyền kiểm soát logic thẩm quyền và bảo mật dữ liệu.

#### 2. QUYẾT ĐỊNH TÁCH RIÊNG ĐỐI VỚI TÙY CHỌN O1 (VĂN BẢN SỐ: `03/2026/QĐ-P1-OPT1`):
* **Căn cứ pháp lý:** Theo Mục 1 và DAT 07 của RFP, Tùy chọn O1 (Selected CRM Context) phải được thẩm định và quyết định độc lập bằng văn bản riêng.
* **QUYẾT ĐỊNH: TẠM HOÃN / CHƯA KÍCH HOẠT TÙY CHỌN O1 TRONG GIAI ĐOẠN G0/G1.**
* **Lý do:** Ở giai đoạn G0/G1, hệ thống tập trung hoàn thiện tri thức quy trình trên 2 schema CSV cơ sở (`passages` và `critical_fields`). Việc không nạp hồ sơ khách hàng CRM thật giúp:
  - Triệt tiêu 100% rủi ro lộ lọt PII theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15.
  - Tiết kiệm chi phí đầu tư và vận hành connector CRM khi chưa đo lường được hiệu quả thực tế.
  - Tùy chọn O1 sẽ chỉ được xem xét kích hoạt lại tại Cổng G2/G3 nếu có nhu cầu phát sinh và được cấp thẩm quyền duyệt riêng.

#### 3. PHÊ DUYỆT LỆNH GIẢI NGÂN THANH TOÁN 10% CỔNG G0 (RFP MỤC 12):
* Căn cứ quy định tiến độ thanh toán tại Mục 12 RFP (10% tại G0, 25% tại G1, 25% tại G2, 25% tại G3, 15% tại G4):
* **LỆNH GIẢI NGÂN ĐỢT 1:** Phê duyệt thanh toán **10% Tổng giá trị Hợp đồng cơ sở** (tương đương **10.000.000 VND / 100.000.000 VND**) cho Nhà cung cấp sau khi toàn bộ sản phẩm bàn giao thiết kế DEL 01 và 7 bằng chứng Cổng G0 được nghiệm thu đạt chuẩn.

---

### III. KÝ DUYỆT VÀ BAN HÀNH

*(Ký ban hành ngày 20/11/2026)*

| ĐẠI DIỆN CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1] | ĐẠI DIỆN NHÀ CUNG CẤP / PROJECT MANAGER [S1] |
|:---:|:---:|
| *(Chủ trì ký duyệt ngày 20/11/2026)* | *(Đệ trình hồ sơ ngày 20/11/2026)* |
| <br><br>**MỸ VÂN** | <br><br>**HOÀNG TIẾN** |
