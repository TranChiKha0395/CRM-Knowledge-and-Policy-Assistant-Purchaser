# BỘ HỒ SƠ QUYẾT ĐỊNH CỔNG GATE G0, PHÊ DUYỆT BASE SCOPE (O1 = OFF) VÀ LỆNH GIẢI NGÂN THANH TOÁN 10%

> **Dự án:** Trợ lý Tri thức và Chính sách CRM (CRM Knowledge & Policy Assistant)  
> **Chủ đầu tư / Bên mua (Purchaser):** Công ty TNHH Thương mại Dịch vụ Kỹ thuật Song Nhật  
> **Cấp thẩm quyền phê duyệt:** [P1] Văn Mỹ Vân – Purchaser Sponsor / Product Owner  
> **Các Jira Ticket tích hợp:** CKPA-40 (Hồ sơ Quyết định Cổng Gate G0 Toàn diện) & CKPA-42 (Biên bản Nghiệm thu G0, Quyết định Base/O1 & Lệnh Thanh toán 10%)  
> **Trạng thái Gate G0:** **GO BASE SCOPE (APPROVED)** | **Tùy chọn O1:** **DEFERRED (TẠM HOÃN)**  
> **Ngày ban hành:** 21/11/2026 (Giờ Việt Nam — UTC+7)

---

## PHẦN 1: HỒ SƠ QUYẾT ĐỊNH CỔNG GATE G0 TOÀN DIỆN (CKPA-40)

# CÔNG TY CỔ PHẦN THIẾT BỊ CÔNG NGHIỆP SONG NHẬT (PURCHASER)
**DỰ ÁN: CRM KNOWLEDGE & POLICY ASSISTANT (CKPA / SCRM) — GATE G0**  
*Mã Story Jira cha:* `CKPA-40` (CRM-G0-ST10)  
*Mã Tiêu chí Cổng G0:* `G0-AC07`  
*GitHub Branch:* `gov/CKPA-40-g0-gate-decision-md`  
*Phía RFP:* Purchaser  
*Priority:* Highest  
*Components (RFP):* Gate-G0, WP01-Discovery  
*RFP Traceability ID:* Mục 9 (G0), Mục 11, Mục 12 (10% payment), Mục 13 (30/25/20/15/10%), Mục 14, Annex E, VN 06  
*Deliverable / Evidence:* Hồ sơ Thẩm định và Quyết định Toàn diện Cổng G0  
*Chủ trì phê duyệt / PO:* `[P1] Mỹ Vân (Purchaser sponsor / Product Owner)`  
*Người trình hồ sơ / Reporter:* `[S1] Hoàng Tiến (Named lead / Scrum Master)`  
*Collaborators / RACI:* Toàn bộ 10 vai: P1–P5 (SongNhat Purchaser) & S1–S5 (Supplier Team)  
*Lịch thực hiện & Story Points:* 2026-11-19 → 2026-11-20 | Story Points: 2 SP | Tổng giờ công G0: 252h  

---

# HỒ SƠ THẨM ĐỊNH VÀ QUYẾT ĐỊNH TOÀN DIỆN CỔNG G0
### (READY TO BUILD — DISCOVERY GATE)
### PHÊ DUYỆT BASE SCOPE (ROUTE 3), TÁCH BIỆT TÙY CHỌN O1 & XÁC LẬP NGUYÊN TẮC GIẢI NGÂN 10% (DEL 05)

---

### THÔNG TIN STORY JIRA

| Thuộc tính | Chi tiết |
|---|---|
| **Mã Story Jira cha:** | CKPA-40 (Mã gốc: CRM-G0-ST10 \| Priority: Highest \| Sprint 2 - G0 Disc W2) |
| **Mã Tiêu chí Cổng G0:** | G0-AC07 \| Hợp phần: Gate-G0, WP01-Discovery \| GitHub Branch: `gov/CKPA-40-g0-gate-decision-md` |
| **Căn cứ RFP Traceability ID:** | Mục 9 (G0), Mục 11, Mục 12 (10% payment), Mục 13 (30/25/20/15/10%), Mục 14 |
| **Deliverable / Evidence:** | Biên bản Nghiệm thu Cổng G0, Quyết định Phương án/Base Scope, Quyết định Riêng O1 & Lệnh Thanh toán 10% |
| **Chủ trì phê duyệt / PO:** | [P1] Mỹ Vân (Purchaser sponsor / Product Owner) |
| **Người trình hồ sơ / Reporter:** | [S1] Hoàng Tiến (Named lead / Scrum Master) |
| **Collaborators / RACI:** | Toàn bộ 10 vai: P1–P5 (SongNhat Purchaser) & S1–S5 (Supplier Team) |
| **Lịch thực hiện & Story Points:** | 2026-11-19 → 2026-11-20 \| Story Points: 2 SP \| Tổng giờ công G0: 252h |

---

### PHẦN 1. BÁO CÁO SO SÁNH CÓ GIÁ 3 PHƯƠNG ÁN TRIỂN KHAI & THẨM ĐỊNH MỤC 13

Căn cứ Báo cáo So sánh 3 phương án (CKPA-5 / `g0-3-route-comparison-and-decision.md`) do [P4] Trà My & [S1] Hoàng Tiến lập, số liệu Baseline CKPA-2 do [P3] Chí Kha đo lường (Median = 18.1 phút, Mean = 18.8 phút/tác vụ), và thẩm định chuyên môn Mục 13 do [P2] Hữu Tài chủ trì (CKPA-41):

| Tiêu chuẩn đối chiếu | Phương án 1: Thư viện tìm kiếm sạch | Phương án 2: Sản phẩm cấu hình sẵn | Phương án 3: Custom có giới hạn (ĐƯỢC CHỌN) |
|---|---|---|---|
| **Năng lực Tiếng Việt & Viết tắt CRM (VN 01)** | Chỉ tìm đúng từ khóa; không tổng hợp câu trả lời, không chuẩn hóa thiếu dấu. | Hỗ trợ hỏi đáp cơ bản; khó tinh chỉnh thuật ngữ SongNhat; chưa demo tenant thật. | Tùy chỉnh pipeline pgvector + FTS, hỗ trợ từ viết tắt CRM & 30 unaccent mapping (100% đạt). |
| **Kiểm soát Ngày chi phối & Phạm vi (DAT 04)** | Không đáp ứng — nhân viên phải tự đọc và đối chiếu ngày bằng mắt. | Không hỗ trợ Ma trận 5 lớp (DAT 03) và không chặn mâu thuẫn hợp đồng (DAT 05). | Đáp ứng 100% — lọc cứng ngoài prompt theo giờ UTC+7 và tự động kích hoạt Conflict Hold. |
| **Tra cứu Trường Trọng yếu (DAT 06)** | Phụ thuộc người dùng tự mở file đọc bảng biểu, dễ sai sót số học. | Không đọc được bảng biểu/hình ảnh trong bài viết tri thức (hạn chế Copilot R07). | Đáp ứng 100% — render cứng 10 critical fields qua Python, cấm LLM tự tính toán/bịa số. |
| **Rút chính sách khẩn cấp (SEC 05 / OPS 05)** | Xóa thủ công trên SharePoint, không đảm bảo dọn cache tức thì. | Phụ thuộc chu kỳ re-index của hãng, không đáp ứng dọn cache $\le$ 5 phút. | Kiểm soát ở Backend, chặn hiển thị tức thời (0s) và dọn sạch Redis cache $\le$ 5 phút. |
| **Chi phí TCO 3 năm (VNĐ gồm VAT)** | Khởi tạo ~15.000.000 VNĐ (100h nội bộ); vận hành 0 VNĐ. TCO: ~15.000.000 VNĐ. | Khởi tạo 80–120M + bản quyền ~15,3M/tháng (20 users). TCO 3 năm > 650.000.000 VNĐ. | Khởi tạo $\le$ 64.8M (hoặc 100M); vận hành 2.5M/tháng. TCO 3 năm ~154,8–190.000.000 VNĐ. |
| **Hiệu quả cắt giảm Effort & Hoàn vốn** | Không đạt — Baseline 18.8' không giảm được $\ge$ 20% công sức. | Chưa kiểm chứng — bị loại do vượt trần ngân sách và hạn chế đọc bảng biểu. | Tiết kiệm 3.76–3.8 phút/tác vụ (> ngưỡng 3.68' Annex E); hoàn vốn $\le$ 24 tháng. |

* **Kết quả chấm điểm Nhà thầu / Phương án 3 theo RFP Mục 13 (CKPA-41 / SUB28):**
  - Knowledge & policy fit (30%): 90 / 100 $\rightarrow$ Quy đổi: 27.00%
  - Governance & security (25%): 88 / 100 $\rightarrow$ Quy đổi: 22.00%
  - Vietnam & feasibility (20%): 87 / 100 $\rightarrow$ Quy đổi: 17.40%
  - Cost & value (15%): 85 / 100 $\rightarrow$ Quy đổi: 12.75%
  - Operation & exit (10%): 93 / 100 $\rightarrow$ Quy đổi: 9.30%
  - **$\rightarrow$ TỔNG ĐIỂM: 88.45 / 100** *(ĐẠT XUẤT SẮC, vượt xa ngưỡng tối thiểu $\ge$ 70/100, đạt 7/7 tình huống demo bắt buộc)*.

---

### PHẦN 2. ĐỐI SOÁT 7 NHÓM BẰNG CHỨNG SẴN SÀNG CỔNG G0 (RFP MỤC 9 & MỤC 14)

| STT | Nhóm bằng chứng Cổng G0 (RFP Mục 9/14) | Sản phẩm nghiệm thu đối soát | Kết quả thẩm định của P1 |
|:---:|---|---|:---:|
| **1** | Xác nhận 3 Họ chính sách (POL-001..003) | DEL01-B: Ma trận thẩm quyền 5 lớp, loại trừ 5 mảng ngoài scope | **ĐẠT (100%)** |
| **2** | Mẫu duyệt 30 passages + 10 critical fields | DEL01-C: Đã ký duyệt, đối soát nguyên vẹn SHA-256 | **ĐẠT (100%)** |
| **3** | Năng lực Curation & Chuẩn hóa Nguồn | Cam kết trần curation $\le 300$ passages / $\le 50$ fields theo CKPA-39; nhân sự nội bộ P3/P2 thực hiện, không phát sinh chi phí mua ngoài | **ĐẠT (100%)** |
| **4** | Ma trận Thẩm quyền & Ngày chi phối giờ VN | DEL01-B: Ngày UTC+7 & đúng 6 chiều phạm vi DAT 04 | **ĐẠT (100%)** |
| **5** | Question Inventory $\ge$ 4w & Baseline Effort | DEL01-A: Tiết kiệm 3,76' > 3,68', 5 NSD 100% Bên mua | **ĐẠT (100%)** |
| **6** | So sánh 3 Route có giá & TCO 3 năm | DEL01-I & DEL 05 (CKPA-39): Chuẩn hóa 14 dòng chi tiết ↔ 13 nhóm DEL 05; mô hình Annex E minh họa; chọn Route 3 Bounded Custom | **ĐẠT (100%)** |
| **7** | Quyết định riêng cho Tùy chọn O1 | Quyết định số 03/2026/QĐ-P1-OPT1: Tạm hoãn Tùy chọn O1 | **ĐẠT (100%)** |

---

### PHẦN 3. BỘ QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1] VĂN MỸ VÂN

#### 1. QUYẾT ĐỊNH LỰA CHỌN PHƯƠNG ÁN & BASE SCOPE (GO BASE SCOPE):
* Căn cứ Báo cáo So sánh 3 Phương án, bảng điểm Mục 13 (88.45/100) và 7 bằng chứng sẵn sàng Cổng G0.
* **QUYẾT ĐỊNH: CHẤP THUẬN (GO BASE SCOPE).** Phê duyệt lựa chọn **Phương án 3 (Custom có giới hạn / Bounded Custom Work)**. Cho phép dự án chính thức đóng Giai đoạn Khảo sát (Discovery G0) và chuyển sang Giai đoạn Xây dựng Lõi có kiểm soát (**Gate G1 — Controlled Offline Implementation**).
* **Điều kiện xem lại route:** Áp dụng kỷ luật chi phí G0 (chốt trần theo Báo giá chính thức DEL 05; chứng minh tiết kiệm $\ge$ 3,68 phút/tác vụ tại G3 theo CKPA-06/07). Tại mốc G3 sau 20 ngày Pilot UAT, nếu không đạt mức giảm $\ge$ 20% công sức hoặc thời gian hoàn vốn > 24 tháng, SongNhat sẽ dừng mở rộng và kích hoạt thoái lui sạch (DEL 04, OPS 08).

#### 2. QUYẾT ĐỊNH RIÊNG BIỆT TÙY CHỌN O1 (SELECTED CRM CONTEXT — SỐ: `03/2026/QĐ-P1-OPT1`):
* Căn cứ Mục 1 và DAT 07 của RFP: Tùy chọn O1 phải được thẩm định và quyết định tách biệt bằng văn bản riêng.
* **QUYẾT ĐỊNH: TẠM HOÃN / CẮT HOÀN TOÀN TÙY CHỌN O1 KHỎI BASE SCOPE Ở GIAI ĐOẠN G0/G1.**
* **Lý do:** Hệ thống tập trung tối ưu hóa tri thức trên 2 bảng phẳng cơ sở (Policy Corpus và Critical Fields). Việc không nạp hồ sơ khách hàng CRM thật giúp triệt tiêu 100% nguy cơ lộ lọt PII theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 và tiết kiệm chi phí đầu tư/vận hành connector.
* Tùy chọn O1 chỉ được xem xét kích hoạt lại tại Cổng G2/G3 nếu phát sinh nhu cầu thực tế và được phê duyệt riêng.

#### 3. NGUYÊN TẮC GIẢI NGÂN THANH TOÁN MỐC 10% CỔNG G0 (RFP MỤC 12 & HỒ SƠ THƯƠNG MẠI DEL 05):
* Căn cứ quy định tiến độ thanh toán tại Mục 12 RFP (Mốc 1: 10% tại G0 khi nghiệm thu hoàn thành DEL 01).
* Căn cứ Hồ sơ thương mại DEL 05 chuẩn hóa Sprint 2 (CKPA-39): Toàn bộ 14 dòng chi phí chi tiết hiện ở trạng thái `PENDING_SUPPLIER_QUOTE`. Thống nhất **tuyệt đối không sử dụng các con số kịch bản minh họa của Phụ lục E (100 triệu, trần công thức 64,8 triệu, 2 triệu/tháng hay 10 triệu) làm báo giá thật**.
* **QUYẾT ĐỊNH CỦA [P1] PRODUCT OWNER:**
  1. Nghiệm thu mặt cấu trúc và phương pháp luận của Hồ sơ thương mại DEL 05 (chuẩn hóa 14 dòng bóc tách chi tiết ↔ 13 nhóm hợp đồng, tách biệt Base Scope vs O1).
  2. Lệnh giải ngân 10% Cổng G0 sẽ được tính toán và chi trả chính thức bằng đúng **10% Giá trị Hợp đồng cơ sở (Base Scope)** ký kết ngay sau khi Nhà cung cấp điền đủ đơn giá VND ràng buộc và thuế VAT cho 14 dòng DEL 05 theo đúng cam kết tại CKPA-39.
  3. Quyền dữ liệu và xuất bản nguồn luôn do Bên mua kiểm soát độc lập với thanh toán theo Mục 12 RFP.
* **Chứng từ thanh toán:** Trọn bộ thiết kế DEL 01 (DEL01-A..I), Biểu mẫu báo giá 14 dòng DEL 05 (CKPA-39) và Biên bản nghiệm thu Cổng G0.

---

### PHẦN 4. TỔNG KẾT SPRINT 2 REVIEW & DISCOVERY RETROSPECTIVE (CKPA-43 / SUB30)

1. **Sprint 2 Review:** Toàn bộ 4 Story Sprint 2 (CKPA-28, CKPA-32, CKPA-36, CKPA-40) hoàn tất 100% DoD. Nghiệm thu quyết toán giờ công G0 theo đúng định mức 10 vai trò: **252 giờ** (Tuần 1: 136h; Tuần 2: 116h).
2. **Discovery Retrospective (Rút kinh nghiệm cho G1):**
   * *Điểm duy trì:* Tiếp tục thực hiện nghiêm ngặt phân định vai trò SoD giữa Bên mua và Nhà cung cấp; đảm bảo nguyên tắc Assignee != Reporter trên mọi ticket.
   * *Hành động cải tiến bắt buộc cho G1:* [S4] Quý Hải khẩn trương dựng kho riêng biệt `sealed-eval-repo` khóa hoàn toàn quyền Read/Clone đối với [S2] Quốc Hưng và [S3] Yến Nhi trước khi nạp 100 câu hỏi Sealed; [S2] hoàn tất 2 bộ CSV Validators đúng hạn để nạp Corpus Họ 1.

---

### KÝ DUYỆT VÀ BAN HÀNH

*(Ký ban hành ngày 20/11/2026)*

| ĐẠI DIỆN CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1]<br>*(Chủ trì ký duyệt ngày 20/11/2026)* | ĐẠI DIỆN NHÀ CUNG CẤP / PROJECT MANAGER [S1]<br>*(Đệ trình hồ sơ ngày 20/11/2026)* |
|:---:|:---:|
| <br><br>**VĂN MỸ VÂN** | <br><br>**HOÀNG TIẾN** |


---

## PHẦN 2: BIÊN BẢN NGHIỆM THU GATE G0, QUYẾT ĐỊNH BASE/O1 VÀ LỆNH GIẢI NGÂN 10% (CKPA-42)

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

