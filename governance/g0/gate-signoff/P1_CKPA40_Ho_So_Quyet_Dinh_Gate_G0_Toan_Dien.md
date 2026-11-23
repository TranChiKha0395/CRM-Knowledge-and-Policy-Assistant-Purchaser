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
