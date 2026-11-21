# SONGNHAT CRM KNOWLEDGE & POLICY ASSISTANT (CKPA) — GATE G0
## HỒ SƠ THẨM ĐỊNH VÀ QUYẾT ĐỊNH TOÀN DIỆN CỔNG G0 (READY TO BUILD)
### (PHÊ DUYỆT BASE SCOPE, TÁCH BIỆT TÙY CHỌN O1 & LỆNH GIẢI NGÂN 10%)

**Mã Story (Jira):** `CKPA-40` (Mã gốc: `CRM-G0-ST10` | Parent Story Cổng G0 | Priority: `Highest`)  
**Mã Tiêu chí Cổng G0:** `G0-AC07`  
**Căn cứ pháp lý & RFP Traceability:** Mục 9 (G0), Mục 11 (Team), Mục 12 (10% Payment), Mục 13 (30/25/20/15/10%), Mục 14  
**Chủ trì phê duyệt / Product Owner:** `[P1] Mỹ Vân (Purchaser Sponsor / Đại diện Chủ đầu tư SongNhat)`  
**Người trình hồ sơ (Reporter / PM):** `[S1] Hoàng Tiến (Named Lead / Project Manager)`  
**Các Sub-tasks con:** `CKPA-41` (SUB28), `CKPA-42` (SUB29), `CKPA-43` (SUB30)  
**Thời gian ban hành:** 20/11/2026 (Múi giờ Việt Nam: Asia/Ho_Chi_Minh, UTC+7)

---

### PHẦN 1. BÁO CÁO THẨM ĐỊNH NHÀ THẦU / PHƯƠNG ÁN THEO RFP MỤC 13

> **Nguyên tắc thẩm định:** Toàn bộ các kiểm soát bắt buộc (*Mandatory controls*) phải đạt 100% trước khi chấm điểm; điểm đạt tối thiểu $\ge 70/100$, không trượt bất kỳ cổng trọng yếu nào (*no failed critical gate*).

| Tiêu chí đánh giá (RFP Mục 13) | Trọng số | Minh chứng & Cơ sở thẩm định độc lập | Điểm thành phần | Điểm quy đổi | Đánh giá |
|---|:---:|---|:---:|:---:|:---:|
| **1. Knowledge and policy fit** | 30% | Bao phủ đủ 3 họ chính sách, điều khoản áp dụng rõ ràng, logic ngày chi phối chuẩn UTC+7, trường trọng yếu có kiểu dữ liệu liên kết điều khoản (DAT 06), quy trình referral chuẩn. | **90 / 100** | **27.0%** | **ĐẠT** |
| **2. Governance and security** | 25% | Phân quyền RBAC 4 vai chuẩn Mục 2, cơ chế thu hồi khẩn cấp tức thời (authoritative withdrawal), xóa cache $\le 5$ phút, bảo vệ PII (SEC 02), rà soát pháp luật VN (SEC 03, Annex F). | **88 / 100** | **22.0%** | **ĐẠT** |
| **3. Vietnam and feasibility** | 20% | Năng lực ngôn ngữ tiếng Việt thương mại (VN 01: Unicode, thiếu dấu, viết tắt CRM, thuật ngữ kỹ thuật Anh - Việt, bảo toàn 14 từ phủ định), đội ngũ chuyên môn bản địa. | **87 / 100** | **17.4%** | **ĐẠT** |
| **4. Cost and value** | 15% | Bảng giá TCO 3 năm minh bạch bằng VND + VAT (DEL 05), bóc tách 13 hạng mục, phân tích độ nhạy và hoàn vốn Annex E (24.2m vs 33.3m), chọn Route 3 tối ưu chi phí. | **85 / 100** | **12.75%** | **ĐẠT** |
| **5. Operation and exit** | 10% | SLA 99.5% trong giờ làm việc (08:00–17:00 VN), RTO 4h / RPO 24h, sao lưu 35 ngày có replay xóa/rút/quyền, kịch bản bàn giao và thoát dữ liệu mở (OPS 08). | **93 / 100** | **9.3%** | **ĐẠT** |
| **TỔNG ĐIỂM CHẤM CHỌN** | **100%** | **Đạt toàn bộ 7 tình huống demo; Không trượt cổng trọng yếu.** | **88.45 / 100** | **88.45%** | **XUẤT SẮC** |

* **Đánh giá 7 Tình huống Demo bắt buộc (Mục 13):**
  1. *Current & historical answers:* Đạt — Phân biệt rõ ngày hiệu lực chi phối (`governing_date`).
  2. *Future policy:* Đạt — Chính sách tương lai không có hiệu lực trước ngày công bố (`KNW 03`).
  3. *Exact threshold boundary:* Đạt — Ngưỡng số và toán tử `$<=, >=, between$` không bị model thay đổi (`DAT 06`).
  4. *Missing exception:* Đạt — Thiếu ngoại lệ thì hiển thị Hold hoặc chuyển owner, không tự cấp quyền.
  5. *Conflicting contract:* Đạt — Hợp đồng xung đột chính sách kích hoạt `Conflict HOLD` (`DAT 05`).
  6. *Unauthorized user:* Đạt — Kiểm tra quyền Pre-retrieval, chặn truy cập tài liệu nhạy cảm (`SEC 01`).
  7. *Withdrawal during generation:* Đạt — Rút chính sách cập nhật authoritative state ngay, xóa cache $\le 5$ phút (`OPS 05`).

---

### PHẦN 2. KIỂM SOÁT 7 NHÓM BẰNG CHỨNG SẴN SÀNG CỔNG G0 (RFP MỤC 9 & MỤC 14)

| STT | Nhóm bằng chứng Cổng G0 | Căn cứ RFP | Hồ sơ / Deliverable đối soát | Kết quả thẩm định của P1 |
|:---:|---|---|---|:---:|
| **1** | **Xác nhận 3 Họ chính sách** | `DAT 03, VN 04` | POL-001 (Báo giá & Duyệt thương mại), POL-002 (Xử lý thông tin KH), POL-003 (Dịch vụ & Bảo hành). Đã ký Ma trận Thẩm quyền, chỉ định Policy Owners & Substitutes. | **ĐẠT (100%)** |
| **2** | **Mẫu duyệt 30 passages + 10 critical fields** | `DAT 01, DAT 06` | Bộ mẫu đại diện 30 passages + 10 critical rows (P2: 15+5, P3: 15+5) đã nghiệm thu tại CKPA-24/27; đối soát toàn vẹn SHA-256. | **ĐẠT (100%)** |
| **3** | **Năng lực Curation & Kinh phí trước G1** | `Mục 2, DEL 05` | Khoản mục 2 trong Báo giá DEL 05 đã duyệt 8.000.000 VND hỗ trợ chuẩn hóa nguồn; cam kết hoàn tất trần $\le 300$ đoạn / $\le 50$ fields trước G1. | **ĐẠT (100%)** |
| **4** | **Ma trận Thẩm quyền & Quy tắc Ngày** | `DAT 03, DAT 04` | Đã ký Ma trận thẩm quyền 5 lớp nguồn; quy tắc ngày chi phối giao dịch theo múi giờ Việt Nam (`Asia/Ho_Chi_Minh`, UTC+7). | **ĐẠT (100%)** |
| **5** | **Question Inventory & Baseline Effort** | `WP 01, VN 06` | Hồ sơ 4 tuần câu hỏi thực tế; đo baseline 7 phút thủ công vs 4 phút có trợ lý (tiết kiệm 3 phút/tác vụ, giải phóng 50h/tháng). | **ĐẠT (100%)** |
| **6** | **So sánh 3 Route có giá & TCO** | `WP 01, DEL 05` | Báo cáo so sánh 3 phương án (searchable library, configured product, custom có giới hạn); phân tích TCO 3 năm và chọn Route 3. | **ĐẠT (100%)** |
| **7** | **Quyết định riêng cho Tùy chọn O1** | `DAT 07, VN 03` | Ban hành Quyết định riêng số `03/2026/QĐ-P1-OPT1`: Tạm hoãn Tùy chọn O1 ở G0, chỉ triển khai thuần túy Base Scope (2 CSV). | **ĐẠT (100%)** |

---

### PHẦN 3. QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ / PURCHASER SPONSOR (P1)

#### 1. QUYẾT ĐỊNH BASE SCOPE (GO / STOP):
* **QUYẾT ĐỊNH: CHẤP THUẬN (GO BASE SCOPE).**
* Cho phép dự án chính thức đóng Giai đoạn Khảo sát (Discovery G0) và chuyển sang Giai đoạn Xây dựng Lõi có kiểm soát (**Gate G1 — Controlled Offline Implementation**).
* **Lộ trình thực hiện:** Phê duyệt lựa chọn **Phương án 3 (Bounded Custom Work)** kết hợp tái sử dụng các thành phần nguồn mở có sẵn (FastAPI, PostgreSQL pgvector + unaccent, Redis) để đảm bảo toàn quyền kiểm soát logic thẩm quyền và bảo mật dữ liệu.

#### 2. QUYẾT ĐỊNH TÁCH RIÊNG ĐỐI VỚI TÙY CHỌN O1 (SELECTED CRM CONTEXT):
* **QUYẾT ĐỊNH: TẠM HOÃN / CHƯA KÍCH HOẠT TÙY CHỌN O1 (Ban hành Quyết định số `03/2026/QĐ-P1-OPT1`).**
* **Căn cứ:** Theo Mục 1 và DAT 07 của RFP, Tùy chọn O1 phải được thẩm định và quyết định tách biệt. Ở giai đoạn G0/G1, hệ thống tập trung hoàn thiện tri thức quy trình trên 2 schema CSV cơ sở (`passages` và `critical_fields`). Việc không nạp hồ sơ khách hàng CRM thật giúp:
  - Triệt tiêu 100% rủi ro lộ lọt PII theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15.
  - Tiết kiệm chi phí đầu tư và vận hành connector CRM khi chưa đo lường được hiệu quả thực tế.
  - Tùy chọn O1 sẽ chỉ được xem xét kích hoạt lại tại Cổng G2/G3 nếu có nhu cầu phát sinh và được cấp thẩm quyền duyệt riêng.

#### 3. PHÊ DUYỆT LỆNH GIẢI NGÂN THANH TOÁN 10% CỔNG G0 (RFP MỤC 12):
* Căn cứ quy định tiến độ thanh toán tại Mục 12 RFP (10% tại G0, 25% tại G1, 25% tại G2, 25% tại G3, 15% tại G4):
* **LỆNH GIẢI NGÂN ĐỢT 1:** Phê duyệt thanh toán **10% Tổng giá trị Hợp đồng cơ sở** (tương đương **10.000.000 VND / 100.000.000 VND**) cho Nhà cung cấp sau khi toàn bộ sản phẩm bàn giao thiết kế DEL 01 được nghiệm thu đạt chuẩn.

#### 4. TỔNG KẾT SPRINT 2 REVIEW & DISCOVERY RETROSPECTIVE (CKPA-43):
* **Đánh giá Increment:** Hoàn thành 100% mục tiêu Sprint 2; đáp ứng đầy đủ Definition of Done (DoD).
* **Bài học kinh nghiệm & Cải tiến cho G1:**
  - Tiếp tục duy trì nghiêm ngặt phân định vai trò SoD (Separation of Duties).
  - Khẩn trương dựng kho cách ly `sealed-eval-repo` cho [S4] Quý Hải để bảo vệ tính độc lập của tập 100 câu hỏi Sealed.
  - Triển khai 2 bộ Validator CSV đúng hạn để sẵn sàng nạp Corpus Họ 1.

---

*(Ký ban hành ngày 20/11/2026)*  
**ĐẠI DIỆN CHỦ ĐẦU TƯ / PURCHASER SPONSOR (P1)**  
*(Đã ký)*  
**MỸ VÂN**
