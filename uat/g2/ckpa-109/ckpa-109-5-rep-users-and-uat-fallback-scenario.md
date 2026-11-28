# HỒ SƠ CHUẨN BỊ 5 NGƯỜI DÙNG ĐẠI DIỆN, 20 NGƯỜI DÙNG ĐỊNH DANH & KỊCH BẢN UAT / FALLBACK
## [G2][Mục11] Chuẩn bị 5 NSD đại diện & Kịch bản UAT (Task CKPA-109)

> **Mã công việc (Jira):** `CKPA-109` | **Epic phụ trách (G2):** `CKPA-85` | **Tiêu chí nghiệm thu Cổng G2:** `G2-AC08`  
> **Nhánh Git làm việc:** `uat/CKPA-109-prep-5-rep-users-uat-fallback`  
> **Vị trí file chuẩn:** `uat/g2/ckpa-109/ckpa-109-5-rep-users-and-uat-fallback-scenario.md`  
> **Tệp dữ liệu kèm theo:**  
> - `uat/g2/ckpa-109/20_named_users_and_5_rep_users_matrix.csv` (Ma trận 20 Named Users & 5 Rep Users)  
> - `uat/g2/ckpa-109/usefulness_and_observed_effort_rubric.csv` (Thang chấm Usefulness & Biểu mẫu Effort 6 thành phần)  
> **Phía phụ trách:** Purchaser (Công ty Cổ phần Thiết bị Công nghiệp Song Nhật)  
> **Assignee / Lead điều phối:** `[P4] Ngô Thị Trà My (Staff users / Commercial & UAT Lead)`  
> **Collaborators / RACI:** `[P2] Trương Đình Hữu Tài (Policy Owner)`, `[P3] Trần Chí Kha (Data Steward)`, `[P5] Nguyễn Anh Khoa (Security & Privacy)`  
> **Ràng buộc SoD tối cao:** **ZERO S1–S5** (100% nhân sự thuộc Bên Mua SongNhat, tuyệt đối KHÔNG có `[S1]` Hoàng Tiến hay bất kỳ nhân sự nào thuộc nhà thầu phát triển S1–S5 tham gia làm Representative User — Tuân thủ nghiêm ngặt Mục 11 RFP & Discovery Charter CKPA-5).  
> **Ngày lập hồ sơ:** 2026-11-25 | **Trạng thái:** Bàn giao chờ thẩm định (PENDING REVIEW)  
> **Truy vết RFP & SRS:** Mục 8 (Observed effort prep, Usefulness >= 80%, Hold trong mẫu số, Critical Failure = 0%, unanswerable unsupported <= 5%), Mục 9 (G2), Mục 11 (5 Representative Staff Users outside Supplier - CKPA-5 sync), SEC 01 (20 Named Users RBAC - 4 vai trò chuẩn), Mục 9 / OPS 05 / OPS 06 / SEC 08 (Manual Fallback).

---

## 1. TỔNG QUAN VÀ MỤC TIÊU SUB-TASK CKPA-109

Căn cứ quy định tại Mục 8, Mục 9, Mục 11 RFP và tiêu chuẩn chuyển tiếp Cổng G2 (`G2-AC08`):
1. **Đồng bộ nhân sự độc lập Bên Mua theo Discovery Charter CKPA-5:** Chuẩn hóa và ban hành danh sách **5 Người dùng nghiệp vụ đại diện (5 Purchaser Representative Users)** gồm `[P4]` (Trà My) và đại diện `[P1, P2, P3, P5]`, bảo đảm tính khách quan tuyệt đối (0% nhân sự nhà cung cấp phát triển S1–S5).
2. **Thiết lập danh mục 20 Người dùng định danh (20 Named Users):** Phân bổ tài khoản theo đúng 4 vai trò hệ thống chuẩn tại RFP Mục 2 và `SEC 01` (`reader`, `policy_owner`, `steward`, `administrator`), phục vụ kiểm thử diện rộng giai đoạn Supervised Use.
3. **Ban hành thang đo Tính hữu dụng (Usefulness Rubric theo Mục 8 RFP):** Thiết lập chuẩn định lượng với Usefulness >= 80% (mẫu số bao gồm 100% ca Answerable kể cả ca bị Hold, đối soát raw vs staff-used), Critical Controls Failure = 0% (Zero Tolerance), và unanswerable received unsupported answers <= 5%.
4. **Chuẩn bị biểu mẫu đo Observed Effort 6 thành phần:** Xây dựng cơ chế đo lường thời gian thao tác thực tế (T1..T6 bao gồm failed attempts và fallback) đối chiếu với mốc **Cleaned Searchable Baseline = 15,53 phút** (Median = 14,30 phút) đã chốt tại CKPA-7 & CKPA-40/42, nhằm chuẩn bị cho mục tiêu cắt giảm >= 20% công sức tại Pilot G3.
5. **Xây dựng kịch bản diễn tập Dự phòng Thủ công (Manual Fallback Runbook):** Bảo đảm quy trình vận hành liên tục của doanh nghiệp theo Mục 9 / OPS 05 / OPS 06 / SEC 08 khi hệ thống AI gặp sự cố ngắt kết nối hoặc kích hoạt cơ chế an toàn Fail-Closed.

---

## 2. DANH SÁCH 5 PURCHASER REPRESENTATIVE USERS (NON-SUPPLIER)

Tuân thủ quy định Mục 11 RFP (trang 14) và Discovery Charter `P1_CKPA5_Discovery_Charter_Va_5_Representative_Users.md`:

| STT | Mã Người dùng | Họ và tên | Chức danh chuyên môn | Phòng ban công tác | Vai trò đại diện kiểm thử | Phạm vi Họ chính sách phụ trách |
|:---:|:---:|---|---|---|---|:---:|
| **1** | **SN-USR-01** | **Ngô Thị Trà My** | Chuyên viên Thương mại & Lead UAT | Phòng Kinh doanh & Thương mại | **Lead Representative User [P4]** | **All (POL-001 / POL-002 / POL-003)** |
| **2** | **SN-USR-02** | **Vắn Mỹ Vân** | Giám đốc Dự án / Purchaser Sponsor | Ban Giám đốc / Đại diện Chủ đầu tư | **Rep User [P1] (Purchaser Sponsor)** | **All (Thẩm định UX & Quyết định Gate)** |
| **3** | **SN-USR-03** | **Trương Đình Hữu Tài** | Trưởng phòng Chính sách / Policy Owner | Phòng Quản lý Chính sách Thương mại | **Rep User [P2] (Policy Owner)** | **POL-001 / POL-002 (Báo giá & Dữ liệu KH)** |
| **4** | **SN-USR-04** | **Trần Chí Kha** | Data Steward / Quản lý Kho tài liệu | Phòng Quản trị Tri thức & Dữ liệu | **Rep User [P3] (Data Steward)** | **All (Phả hệ tài liệu, metadata & CSV)** |
| **5** | **SN-USR-05** | **Nguyễn Anh Khoa** | Cán bộ An toàn Dữ liệu & Privacy Officer | Phòng Pháp chế & An toàn Thông tin | **Rep User [P5] (Security & Privacy)** | **All (RBAC, 0% PII & Luật 91/2025/QH15)** |

### Cam kết độc lập và Phân định trách nhiệm (Separation of Duties):
* Toàn bộ 5 nhân sự đại diện trên là nhân viên chính thức thuộc biên chế **Công ty Cổ phần Thiết bị Công nghiệp Song Nhật** (Bên Mua).
* **Tuyệt đối KHÔNG có sự tham gia của `[S1]` Hoàng Tiến** (Team Leader / Lead Developer) hay bất kỳ thành viên nào thuộc nhóm Supplier S1–S5 trong vai trò người dùng kiểm thử.
* 5 nhân sự đại diện không trực tiếp tham gia viết code, tinh chỉnh prompt, hoặc can thiệp vào thuật toán truy xuất của hệ thống.

---

## 3. MA TRẬN 20 NGƯỜI DÙNG ĐỊNH DANH (20 NAMED USERS) & PHÂN QUYỀN RBAC SEC 01

Nhằm phục vụ giai đoạn Supervised Use Cổng G2 và Pilot Cổng G3, danh mục 20 Người dùng định danh được phân bổ theo 4 vai trò RBAC hệ thống chuẩn (`reader`, `policy_owner`, `steward`, `administrator`):

| Nhóm chức năng | Số lượng | Mã User | Vai trò RBAC chuẩn (SEC 01) | Thẩm quyền chính trên hệ thống |
|---|:---:|---|---|---|
| **Ban Điều phối & Quản trị Cấp cao** | 5 | `SN-USR-01` .. `SN-USR-05` | `reader`, `policy_owner`, `steward`, `administrator` | 5 Representative Users theo CKPA-5: Phê duyệt chính sách, quản trị kho tri thức, kiểm toán an toàn và nghiệm thu dự án (`P4, P1, P2, P3, P5`). `SN-USR-05` ([P5]) giữ vai trò RBAC chuẩn `administrator`. |
| **Chuyên viên Vận hành Kinh doanh B2B** | 4 | `SN-USR-06`, `10`, `11`, `12` | `reader` | Tra cứu hạn mức chiết khấu, bảng tính Gross Margin, quy trình báo giá đại lý và kiểm tra thời hạn báo giá 15 ngày (`POL-001`). |
| **Chuyên viên Vận hành Hợp đồng & CRM** | 4 | `SN-USR-07`, `13`, `14`, `15` | `reader` | Tra cứu quy trình cập nhật thông tin pháp lý, đổi địa chỉ thuế, hóa đơn GTGT, kiểm tra thẩm quyền theo giá trị hợp đồng (`POL-002`). |
| **Chuyên viên CSKH & Kỹ thuật Bảo hành** | 5 | `SN-USR-08`, `09`, `16`, `17`, `18` | `reader` | Tra cứu điều kiện tiếp nhận 03 chứng từ, quy trình đổi mới 7 ngày, phân định Tuyến 1 / Tuyến 2 và điều khoản hãng OEM (`POL-003`). |
| **Kế toán & Quản trị Công nợ** | 1 | `SN-USR-19` | `reader` | Đối chiếu điều khoản thanh toán, bảo lưu chiết khấu và biên lợi nhuận hợp đồng phân phối B2B (`POL-001`). |
| **Quản trị viên IT Nội bộ SongNhat** | 1 | `SN-USR-20` | `administrator` | Giám sát vận hành kỹ thuật, kiểm tra kết nối API, cấu hình cờ khẩn cấp và kích hoạt Manual Fallback. |
| **Tổng cộng** | **20** | **SN-USR-01 .. SN-USR-20** | **20 Named Users** | **100% Nhân sự SongNhat đáp ứng chuẩn RBAC 4 vai trò của SEC 01** |

*(Chi tiết định danh từng người dùng được lưu trữ tại: `uat/g2/ckpa-109/20_named_users_and_5_rep_users_matrix.csv`).*

---

## 4. THANG ĐO TÍNH HỮU DỤNG CÂU TRẢ LỜI (USEFULNESS SCORING RUBRIC — MỤC 8 RFP)

Thang đo tính hữu dụng được 5 Rep Users áp dụng để chấm điểm trực tiếp sau mỗi phiên hỏi đáp giải quyết nghiệp vụ, tuân thủ nguyên tắc đo lường của Mục 8 RFP:

```
[Kết quả trả về của AI Workspace]
             |
             |-- Sửa <= 10% từ ngữ hoặc dùng ngay ---------> [USE-01: Direct Acceptance (Minor Edits)] -> MỤC TIÊU: >= 80%
             |                                              (Mẫu số: 100% ca Answerable kể cả bị Hold; đối soát raw vs staff-used)
             |
             |-- Cần viết lại > 10% nhưng đúng hướng -------> [USE-02: Major Rewrite]                  -> KIỂM SOÁT: <= 15%
             |
             |-- Sai điều khoản / Vi phạm chính sách --------> [USE-03: Critical Controls Failure]     -> ZERO TOLERANCE: 0% (Chặn release)
             |                                                          |
             |                                                          +--> Kích hoạt Nút Gắn Cờ (KNW 01) & Tạo Local Referral (KNW 05)
             |
             +-- Không trả lời được nhưng sinh bịa đặt ------> [USE-04: Unanswerable Unsupported]     -> NGƯỠNG TỐI ĐA: <= 5% (Mục 8 RFP)
```

1. **USE-01 — Chấp thuận trực tiếp (Direct Acceptance / Minor Edits <= 10%):**
   - *Tiêu chí:* Câu trả lời trích dẫn chính xác điều khoản, đầy đủ các trường thông tin trọng yếu (`Critical Fields`), chỉ dẫn nghiệp vụ rõ ràng; nhân viên có thể sử dụng nguyên văn hoặc chỉ cần bổ sung dưới 10% từ ngữ cụ thể cho khách hàng.
   - *Quy tắc mẫu số bắt buộc (Mục 8 RFP & đầu vào CKPA-111):*
     - Mẫu số tính toán bao gồm **100% các ca `Answerable`**, trong đó **toàn bộ các ca bị `Hold` (chờ làm rõ) vẫn được giữ nguyên trong mẫu số**.
     - Phân định rõ ràng 3 phân nhóm: `answerable` (có căn cứ trong corpus), `unanswerable` (vượt thẩm quyền hoặc ngoài phạm vi), và `missing_source` (thiếu nguồn trích dẫn).
     - Thực hiện đối soát song song giữa câu trả lời thô của hệ thống (`raw`) và câu trả lời thực tế nhân viên sử dụng (`staff-used`).
   - *Mục tiêu chỉ số:* Đạt tỷ lệ **>= 80%** tổng số phiên hỏi đáp nghiệp vụ.
2. **USE-02 — Chỉnh sửa lớn (Major Rewrite > 10%):**
   - *Tiêu chí:* Câu trả lời trích dẫn đúng tài liệu nhưng diễn giải còn dài dòng, chưa làm nổi bật hành động trọng tâm, nhân viên phải viết lại trên 10% nội dung trước khi phản hồi khách hàng.
   - *Mục tiêu kiểm soát:* Không vượt quá **<= 15%** tổng số lượt hỏi đáp.
3. **USE-03 — Vi phạm kiểm soát trọng yếu (Critical Controls Failure):**
   - *Tiêu chí:* Câu trả lời trích dẫn sai số điều khoản, áp dụng nhầm chính sách đã hết hiệu lực, hoặc phán quyết sai thẩm quyền phê duyệt.
   - *Ngưỡng nghiệm thu:* **0% (Zero Tolerance)** — Đây là chốt chặn an toàn bắt buộc (Critical Control), nếu xuất hiện vi phạm thì chặn release Cổng G2/G3.
   - *Hành động bắt buộc:* Nhân viên bấm nút **Gắn cờ (KNW 01)** để ghi nhận nhật ký lỗi, đồng thời bấm nút **Tạo Local Referral (KNW 05)** để chuyển tiếp xử lý.
4. **USE-04 — Tác vụ không trả lời được nhưng nhận câu trả lời không được hỗ trợ (Unanswerable Unsupported Answers):**
   - *Tiêu chí:* Các tác vụ không trả lời được (`unanswerable` hoặc `missing_source`) nhưng hệ thống lại sinh câu trả lời bịa đặt không có căn cứ điều khoản thay vì từ chối trả lời hợp lệ.
   - *Ngưỡng tối đa theo Mục 8 RFP:* **<= 5%**.

---

## 5. BIỂU MẪU ĐO LƯỜNG OBSERVED EFFORT 6 THÀNH PHẦN (RFP MỤC 8 & ANNEX E)

Thời gian xử lý một tác vụ nghiệp vụ được phân rã thành **6 thành phần định lượng độc lập**, ghi nhận đầy đủ cả các lượt thử thất bại (`failed attempts`), xử lý dự phòng (`fallback`) và câu trả lời không dùng:

```
T_Total = T1 + T2 + T3 + T4 + T5 + T6
```

| Thành phần Effort | Tên bước thao tác | Phương pháp đo lường | Thời gian kỳ vọng (Target) | Đối chứng Baseline thủ công G0 |
|:---:|---|---|:---:|:---:|
| **T1** | Tiếp nhận & Nhập câu hỏi | Bấm giờ từ khi tiếp nhận yêu cầu đến khi gửi câu hỏi lên Workspace | **10 - 25 giây** | Tra cứu sổ tay/tìm file: 180 - 300s |
| **T2** | Hệ thống tra cứu & Sinh phản hồi | Đo lường tự động bởi API Gateway / Hệ thống | **p95 <= 25s @ 5 concurrent users (OPS 02 SLA)** | Lật tìm từng trang tài liệu: 120 - 240s |
| **T3** | Đọc hiểu & Kiểm tra trích dẫn | Nhân viên đọc lướt giải thích và nhấp link mở `source_uri` kiểm tra | **45 - 90 giây** | Đọc đối chiếu văn bản giấy: 240 - 420s |
| **T4** | Đối soát trường trọng yếu | Nhìn bảng Critical Fields kiểm tra 40 trường trọng yếu (`CF-001..CF-040`) | **20 - 45 giây** | Tự tính toán Gross Margin: 180 - 300s |
| **T5** | Hiệu chỉnh văn bản & Lượt thử thất bại | Chỉnh sửa nội dung hoặc điều chỉnh truy vấn khi lượt thử đầu chưa khớp (`failed attempts`) | **30 - 60 giây (nếu có re-query)** | Tự soạn thảo toàn bộ email: 300 - 480s |
| **T6** | Tạo Local Referral & Xử lý Fallback | Bấm 1-click tạo phiếu chuyển tiếp hoặc xử lý theo quy trình dự phòng ngoại tuyến (`fallback`) | **15 - 45 giây (khi vượt quyền/fallback)** | Viết tờ trình giấy / ký tay: 240 - 480s |
| **Tổng cộng** | **Thời gian hoàn tất tác vụ** | **Tổng hợp tự động từ nhật ký phiên kiểm thử thực tế (tính cả failed attempts và fallback)** | **PENDING_20_DAY_PILOT_MEASUREMENT** | **Cleaned Searchable Baseline = 15,53 phút (Median = 14,30 phút)** |

### Nguyên tắc đối chứng và Tiêu chuẩn chất lượng (Quality Gate):
* **Mốc đối chứng cơ sở (G0 Baseline):** Dùng mốc **Cleaned Searchable Baseline = 15,53 phút** (`Median = 14,30 phút`, 95% CI: [14,82' ; 16,24']) đã được thẩm định độc lập tại `CKPA-7` và khóa cứng tại Quyết định Cổng G0 (`CKPA-40`/`42`), không dùng số kho thô 18.8 phút.
* **Chỉ tiêu cắt giảm >= 20%:** Đây là **Quality Gate của giai đoạn Pilot G3 (20 ngày làm việc thực tế)**, tương ứng yêu cầu đưa thời gian xử lý trung bình xuống `<= 12,42 phút/tác vụ` (tiết kiệm >= 3,11 phút/tác vụ mà vẫn giữ 0 lỗi trọng yếu).
* **Tuân thủ No-Mock tại G2:** Toàn bộ cột kết quả thực tế hiện được ghi nhận là **`PENDING_20_DAY_PILOT_MEASUREMENT`**, không đưa ra các con số kết luận giả lập trước khi có dữ liệu đo lường thực tế từ đợt Pilot 20 ngày.

---

## 6. KỊCH BẢN DIỄN TẬP VẬN HÀNH DỰ PHÒNG THỦ CÔNG (MANUAL FALLBACK DRILL RUNBOOK)
*(Căn cứ theo tiêu chuẩn RFP Mục 9, tiêu chuẩn vận hành OPS 05, OPS 06 và an ninh SEC 08)*

Kịch bản diễn tập được thiết lập nhằm bảo đảm tính liên tục của hoạt động kinh doanh (Business Continuity) khi hệ thống AI gặp sự cố kỹ thuật hoặc chuyển sang trạng thái tạm dừng an toàn (`Fail-Closed`):

```
[WORKSPACE AI GẶP SỰ CỐ / FAIL-CLOSED]
                 |
                 v (<= 5 phút)
[GIAI ĐOẠN 1: Phát hiện & Kích hoạt Cờ Khẩn cấp Emergency-Disable (SEC 08)]
                 |
                 v
[GIAI ĐOẠN 2: Kích hoạt Bảng Tra cứu Ngoại tuyến Offline Quick Reference Matrix (OPS 05)]
                 |
                 v
[GIAI ĐOẠN 3: Ghi nhận Nhật ký Xử lý Dự phòng Manual Fallback Log (OPS 06)]
                 |
                 v (Khi hệ thống AI phục hồi)
[GIAI ĐOẠN 4: Đối soát & Đồng bộ Dữ liệu Ngược (Reconciliation trong 2 giờ)]
```

### 6.1 Giai đoạn 1: Phát hiện & Kích hoạt Chế độ Dự phòng (T0 -> T0 + 5 phút)
* **Dấu hiệu kích hoạt:** Hệ thống AI mất kết nối quá 5 phút, hoặc xuất hiện cảnh báo xung đột chính sách diện rộng, hoặc quản trị viên kích hoạt cờ `POST /api/v1/admin/emergency-disable`.
* **Hành động:** 
  1. IT Administrator (`SN-USR-20`) phát thông báo khẩn cấp trên kênh nội bộ CRM.
  2. Giao diện Workspace tự động chuyển sang chế độ hiển thị Banner thông báo: *"Hệ thống AI đang bảo trì. Vui lòng sử dụng Quy trình Tra cứu Dự phòng Ngoại tuyến"*.

### 6.2 Giai đoạn 2: Vận hành Tra cứu Dự phòng Ngoại tuyến (Offline Mode)
* **Công cụ hỗ trợ:** Nhân viên sử dụng bộ tài liệu dự phòng ngoại tuyến gồm:
  - **Bảng ma trận thẩm quyền rút gọn 1 trang (One-page Quick Reference Card):** Đã in sẵn và đặt tại bàn làm việc của 100% nhân viên CRM.
  - **Bộ hồ sơ chính sách ngoại tuyến đã được ký số:** Bản lưu trữ PDF/Markdown của 11 tài liệu (`DOC-001 .. DOC-011`) trên ổ đĩa mạng nội bộ (Local NAS) độc lập với cloud.
* **Quy tắc xử lý:**
  - Với các yêu cầu thông thường (<= 5% chiết khấu, cập nhật email GTGT, tiếp nhận bảo hành cơ bản): Xử lý theo đúng quy định tại Bảng ma trận ngoại tuyến.
  - Với các tình huống đặc biệt (xin nợ chứng từ, chiết khấu > 5%, cháy nổ thiết bị): Lập phiếu đề xuất chuyển tiếp trực tiếp cho Trưởng phòng/Giám đốc qua email nội bộ có ký tên xác nhận.

### 6.3 Giai đoạn 3: Ghi nhận Nhật ký Xử lý Dự phòng (Manual Fallback Log)
* Mọi giao dịch và quyết định nghiệp vụ phát sinh trong thời gian dự phòng bắt buộc phải ghi nhận vào tệp **`Manual_Fallback_Operational_Log.xlsx`** nội bộ với các trường:
  - `Mã giao dịch CRM` | `Khách hàng` | `Loại yêu cầu` | `Căn cứ điều khoản áp dụng` | `Người thực hiện` | `Người phê duyệt ngoại lệ` | `Thời gian tiếp nhận & hoàn tất`.

### 6.4 Giai đoạn 4: Phục hồi và Hậu kiểm Đối soát (Reconciliation)
* Khi IT Administrator thông báo hệ thống phục hồi:
  1. `[P4] Ngô Thị Trà My` cùng các Rep Users đối chiếu 100% các ca xử lý trong nhật ký dự phòng với hệ thống CRM.
  2. Quản trị tri thức `[P3] Trần Chí Kha` kiểm tra tính toàn vẹn của dữ liệu và nhật ký kiểm toán.
  3. Hoàn tất báo cáo kết thúc diễn tập dự phòng trong vòng **2 giờ làm việc**.

---

## 7. BẢNG KÝ DUYỆT VÀ TIẾP NHẬN HỒ SƠ SUB-TASK CKPA-109

| Đại diện | Vai trò dự án | Họ và tên | Trách nhiệm đối soát | Trạng thái ký duyệt |
|:---|:---|:---|---|:---:|
| **Bên Mua ([P4])** | Lead UAT & Commercial | **Ngô Thị Trà My** | Chủ trì lập danh sách 5 Rep Users, 20 Named Users, biểu mẫu Effort & Kịch bản Fallback | **ĐÃ HOÀN TẤT BÀN GIAO** |
| **Bên Mua ([P2])** | Policy Owner | **Trương Đình Hữu Tài** | Thẩm định tính chính xác của Thang đo Usefulness & Ma trận thẩm quyền Fallback | **PENDING** |
| **Bên Mua ([P3])** | Data Steward | **Trần Chí Kha** | Thẩm định cấu trúc dữ liệu CSV và phương án lưu trữ ngoại tuyến DOC-001..011 | **PENDING** |
| **Bên Mua ([P5])** | Security & Privacy Officer | **Nguyễn Anh Khoa** | Thẩm định 20 Named Users đúng chuẩn RBAC Least Privilege & An toàn Fallback | **PENDING** |
| **Chủ đầu tư ([P1])** | Purchaser Sponsor / PO | **Vắn Mỹ Vân** | Phê duyệt chính thức danh sách nhân sự và kịch bản diễn tập Cổng G2 (G2-AC08) | **PENDING** |

---

*Hồ sơ hoàn tất ngày 25/11/2026. Sẵn sàng nghiệm thu Sub-task CKPA-109 trên hệ thống Jira và GitHub.*
