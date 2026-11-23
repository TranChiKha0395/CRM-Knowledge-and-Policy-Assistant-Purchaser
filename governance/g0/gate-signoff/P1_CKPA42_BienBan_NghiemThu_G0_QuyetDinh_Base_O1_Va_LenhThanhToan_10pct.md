# CÔNG TY CỔ PHẦN THIẾT BỊ CÔNG NGHIỆP SONG NHẬT (PURCHASER)
**DỰ ÁN: CRM KNOWLEDGE & POLICY ASSISTANT (CKPA / SCRM) — CỔNG G0**  
*Mã Story cha:* `CKPA-40` (CRM-G0-ST10) | *Mã Sub-task:* `CKPA-42` (CRM-G0-SUB29)  
*Mã Tiêu chí Cổng G0:* `G0-AC07`  
*GitHub Branch:* `gov/CKPA-42-g0-10pct-payment-signoff-md`  
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
### QUYẾT ĐỊNH BASE SCOPE, QUYẾT ĐỊNH RIÊNG TÙY CHỌN O1 & XÁC LẬP NGUYÊN TẮC GIẢI NGÂN MỐC 10% G0 THEO BÁO GIÁ DEL 05 (MỤC 12 RFP)

---

### THÔNG TIN NHIỆM VỤ

| Thuộc tính | Chi tiết |
|---|---|
| **Mã nhiệm vụ Jira:** | CKPA-42 (Mã gốc: CRM-G0-SUB29 \| Thuộc Story cha: CKPA-40 / CRM-G0-ST10) |
| **Mã Tiêu chí Cổng G0:** | G0-AC07 \| Phía RFP: Purchaser \| Priority: Highest \| Branch: `gov/CKPA-42-g0-10pct-payment-signoff-md` |
| **Hợp phần (Components):** | Gate-G0 |
| **Căn cứ RFP Traceability ID:** | Mục 9 (G0), Mục 12 (10% payment), Mục 14 (Decisions before award) |
| **Deliverable / Evidence:** | Biên bản Nghiệm thu G0, Quyết định Base/O1 & Lệnh Thanh toán 10% |
| **Assignee / Lead (Doer):** | [P1] Mỹ Vân (Purchaser sponsor / Product Owner) |
| **Reporter / Nghiệm thu (PO/SM):** | [S1] Hoàng Tiến (Named lead / Scrum Master) |
| **Collaborators / RACI & Lịch:** | Toàn bộ P1..P5 & S1..S5 \| Lịch: 2026-11-20 → 2026-11-20 (4h) |

---

### I. ĐỐI SOÁT 7 NHÓM BẰNG CHỨNG SẴN SÀNG CỔNG G0 (RFP MỤC 9 & MỤC 14)

| STT | Nhóm bằng chứng Cổng G0 | Hồ sơ / Bằng chứng nghiệm thu | Kết luận thẩm định |
|:---:|---|---|:---:|
| **1** | Xác nhận 3 Họ chính sách (POL-001..003) | DEL01-B: Ma trận thẩm quyền 5 lớp, loại trừ 5 mảng ngoài scope | **ĐẠT (100%)** |
| **2** | Mẫu duyệt 30 passages + 10 critical fields | DEL01-C: Đã ký duyệt, đối soát nguyên vẹn SHA-256 | **ĐẠT (100%)** |
| **3** | Năng lực Curation & Ngân sách trước G1 | DEL 05 (CKPA-39): Khoản mục 2 (Curation assistance) đã chuẩn hóa phạm vi $\le 300$ đoạn / $\le 50$ fields; cam kết hoàn tất trước G1 | **ĐẠT (100%)** |
| **4** | Ma trận Thẩm quyền & Ngày chi phối UTC+7 | DEL01-B: Ngày UTC+7 & đúng 6 chiều phạm vi DAT 04 | **ĐẠT (100%)** |
| **5** | Question Inventory $\ge$ 4w & Baseline Effort | DEL01-A: Hồ sơ Question Log 4 tuần thực tế (520 câu hỏi tại CKPA-06); Baseline Effort đo thực tế 5 NSD độc lập Bên mua | **ĐẠT (100%)** |
| **6** | So sánh 3 Route có giá & TCO 3 năm | DEL01-I & DEL 05 (CKPA-39): Chuẩn hóa 14 dòng chi tiết ↔ 13 nhóm DEL 05; mô hình Annex E minh họa; chọn Route 3 Bounded Custom | **ĐẠT (100%)** |
| **7** | Quyết định riêng cho Tùy chọn O1 | Quyết định số 03/2026/QĐ-P1-OPT1: Tạm hoãn Tùy chọn O1 | **ĐẠT (100%)** |

---

### II. QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1] MỸ VÂN

#### 1. QUYẾT ĐỊNH BASE SCOPE (GO / STOP):
* Căn cứ kết quả thẩm định toàn diện 7 nhóm bằng chứng Cổng G0 và điểm đánh giá kỹ thuật 88.45/100 tại SUB28.
* **QUYẾT ĐỊNH: CHẤP THUẬN (GO BASE SCOPE).** Cho phép dự án chính thức đóng Giai đoạn Khảo sát (Discovery G0) và chuyển sang Giai đoạn Xây dựng Lõi có kiểm soát (**Gate G1 — Controlled Offline Implementation**).
* **Phương án kiến trúc:** Phê duyệt lựa chọn **Phương án 3 (Bounded Custom Work)** trên nền tảng nguồn mở kiểm soát dữ liệu nội bộ (FastAPI, PostgreSQL pgvector + unaccent, Redis).

#### 2. QUYẾT ĐỊNH RIÊNG CHO TÙY CHỌN O1 (VĂN BẢN SỐ: `03/2026/QĐ-P1-OPT1`):
* Căn cứ Mục 1 và DAT 07 RFP: Tùy chọn O1 (Selected CRM Context) phải được thẩm định và quyết định tách biệt bằng văn bản riêng.
* **QUYẾT ĐỊNH: TẠM HOÃN / CHƯA KÍCH HOẠT TÙY CHỌN O1 TRONG GIAI ĐOẠN G0/G1.**
* **Lý do:** Hệ thống tập trung tối ưu hóa tri thức trên 2 cấu trúc phẳng cơ sở (Policy Corpus và Critical Fields). Việc không kết nối và không nạp dữ liệu khách hàng CRM thật giúp triệt tiêu 100% nguy cơ lộ lọt PII theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và tiết kiệm chi phí tích hợp connector.
* Tùy chọn O1 sẽ chỉ được xem xét kích hoạt lại tại Cổng G2 hoặc G3 khi có nhu cầu thực tế và được phê duyệt riêng.

#### 3. NGUYÊN TẮC GIẢI NGÂN THANH TOÁN MỐC 10% CỔNG G0 (RFP MỤC 12 & HỒ SƠ THƯƠNG MẠI DEL 05):
* Căn cứ quy định tiến độ thanh toán tại Mục 12 RFP (RFP-S12-08): Tiến độ giải ngân đề xuất gồm 5 đợt: 10% tại G0, 25% tại G1, 25% tại G2, 25% tại G3, và 15% tại G4, phụ thuộc vào bằng chứng được chấp nhận và hợp đồng ký kết.
* Căn cứ Hồ sơ thương mại DEL 05 chuẩn hóa Sprint 2 (CKPA-39 do [S1] Hoàng Tiến đệ trình): Toàn bộ 14 dòng chi phí chi tiết (ánh xạ thành 13 nhóm hợp đồng DEL 05) hiện đang ở trạng thái minh bạch `PENDING_SUPPLIER_QUOTE`. Nhà cung cấp và Bên mua thống nhất **tuyệt đối không sử dụng các con số kịch bản minh họa của Phụ lục E (như 100 triệu VND, trần công thức 64,8 triệu VND, 2 triệu/tháng hay 10 triệu VND) làm báo giá thật hay căn cứ phát hành lệnh giải ngân**.
* **QUYẾT ĐỊNH CỦA [P1] PRODUCT OWNER:**
  1. **Nghiệm thu mặt kỹ thuật và cấu trúc của Hồ sơ thương mại DEL 05:** Đạt yêu cầu về cấu trúc 14 dòng bóc tách chi tiết, phân tách rõ Base Scope vs Tùy chọn O1, gắn kèm mô hình kiểm thử sức chịu đựng Annex E minh họa.
  2. **Xác lập nguyên tắc giải ngân Đợt 1 (Mốc G0):** Giá trị thanh toán 10% mốc G0 sẽ được tính toán và chi trả chính thức bằng đúng **10% Tổng giá trị Hợp đồng cơ sở (Base Scope)** ngay sau khi Nhà cung cấp hoàn tất điền đơn giá VND ràng buộc và thuế VAT thực tế cho 14 dòng DEL 05 theo đúng cam kết tại CKPA-39.
  3. **Quyền dữ liệu và quyền xuất bản nguồn:** Luôn do Bên mua kiểm soát theo vai trò, độc lập hoàn toàn với tiến độ giải ngân (Mục 12 RFP).
* **Chứng từ kèm theo:** Bộ hồ sơ thiết kế DEL 01 (DEL01-A..I), Biểu mẫu báo giá 14 dòng DEL 05 (CKPA-39), Báo cáo so sánh 3 phương án và Biên bản nghiệm thu Cổng G0.

---

### III. KÝ DUYỆT VÀ BAN HÀNH

*(Ký ban hành ngày 20/11/2026)*

| ĐẠI DIỆN CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1]<br>*(Chủ trì ký duyệt ngày 20/11/2026)* | ĐẠI DIỆN NHÀ CUNG CẤP / PROJECT MANAGER [S1]<br>*(Đệ trình hồ sơ ngày 20/11/2026)* |
|:---:|:---:|
| <br><br>**MỸ VÂN** | <br><br>**HOÀNG TIẾN** |
