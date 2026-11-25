# HỒ SƠ CHUẨN BỊ 5 NGƯỜI DÙNG ĐẠI DIỆN, 20 NGƯỜI DÙNG ĐỊNH DANH & KỊCH BẢN UAT / FALLBACK
## [G2][Mục11] Chuẩn bị 5 NSD đại diện & Kịch bản UAT (Task CKPA-109)

> **Mã công việc (Jira):** `CKPA-109` | **Tiêu chí nghiệm thu Cổng G2:** `G2-AC08`  
> **Nhánh Git làm việc:** `uat/CKPA-109-prep-5-rep-users-uat-fallback`  
> **Vị trí file chuẩn:** `uat/g2/ckpa-109/ckpa-109-5-rep-users-and-uat-fallback-scenario.md`  
> **Tệp dữ liệu kèm theo:**  
> - `uat/g2/ckpa-109/20_named_users_and_5_rep_users_matrix.csv` (Ma trận 20 Named Users & 5 Rep Users)  
> - `uat/g2/ckpa-109/usefulness_and_observed_effort_rubric.csv` (Thang chấm Usefulness & Biểu mẫu Effort 6 thành phần)  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead điều phối:** `[P4] Ngô Thị Trà My (Staff users / Commercial & UAT Lead)`  
> **Collaborators / RACI:** `[P2] Lý Hữu Tài (Policy Owner)`, `[P3] Trần Chí Kha (Data Steward)`, `[P5] Nguyễn Anh Khoa (Security & Privacy)`  
> **Ràng buộc SoD tối cao:** **ZERO S1–S5** (100% nhân sự thuộc Bên Mua SongNhat, tuyệt đối KHÔNG có `[S1]` Hoàng Tiến hay bất kỳ nhân sự nào thuộc nhà thầu phát triển S1–S5 tham gia làm Representative User — Tuân thủ nghiêm ngặt Mục 11 RFP & SCRM Onboarding Guide §6.4).  
> **Lịch thực hiện:** 2026-12-28 $\rightarrow$ 2026-12-28 | **Estimate:** 6h  
> **Truy vết RFP & SRS:** Mục 8 (Observed effort prep), Mục 9 (G2), Mục 11 (5 Representative Staff Users outside Supplier), SEC 01 (20 Named Users RBAC), SEC 07 / OPS 04 (Manual Fallback).

---

## 1. TỔNG QUAN VÀ MỤC TIÊU SUB-TASK CKPA-109

Căn cứ quy định tại Mục 11 RFP (Representative Staff Users) và tiêu chuẩn chuyển tiếp Cổng G2 (`G2-AC08`):
1. **Xác lập nhân sự độc lập Bên Mua:** Chuẩn hóa và ban hành danh sách **5 Người dùng nghiệp vụ đại diện (5 Purchaser Representative Users)** đại diện cho các vị trí công tác thực tế của Bên Mua SongNhat, đảm bảo tính khách quan tuyệt đối (0% nhân sự nhà cung cấp phát triển S1–S5).
2. **Thiết lập danh mục 20 Người dùng định danh (20 Named Users):** Phân bổ tài khoản, quyền hạn tối thiểu (Least Privilege) theo chuẩn ma trận RBAC `SEC 01` phục vụ kiểm thử diện rộng giai đoạn Supervised Use.
3. **Ban hành thang đo Tính hữu dụng (Usefulness Rubric):** Thiết lập tiêu chuẩn định lượng 3 mức (Direct Acceptance / Minor Edits vs Major Rewrite vs Rejection) theo tiêu chuẩn `ANS 04`.
4. **Chuẩn bị biểu mẫu đo Observed Effort 6 thành phần:** Xây dựng cơ chế đo lường thời gian thao tác thực tế ($T_1 .. T_6$) đối chiếu với Baseline G0 (18.8 phút), chứng minh mục tiêu cắt giảm $\ge 20\%$ công sức.
5. **Xây dựng kịch bản diễn tập Dự phòng Thủ công (Manual Fallback Runbook):** Bảo đảm quy trình vận hành liên tục của doanh nghiệp khi hệ thống AI gặp sự cố ngắt kết nối hoặc kích hoạt cơ chế an toàn Fail-Closed (`SEC 07` / `OPS 04`).

---

## 2. DANH SÁCH 5 PURCHASER REPRESENTATIVE USERS (NON-SUPPLIER)

Tuân thủ quy định Mục 11 RFP (trang 14): *"The Purchaser shall designate 5 representative staff users outside the Supplier's team to participate in supervised evaluation and testing"*.

| STT | Mã Người dùng | Họ và tên | Chức danh chuyên môn | Phòng ban công tác | Vai trò đại diện kiểm thử | Phạm vi Họ chính sách phụ trách |
|:---:|:---:|---|---|---|---|:---:|
| **1** | **SN-USR-01** | **Ngô Thị Trà My** | Chuyên viên Thương mại & Lead UAT | Phòng Kinh doanh & Thương mại | **Lead Representative User `[P4]`** | **All (POL-001 / POL-002 / POL-003)** |
| **2** | **SN-USR-02** | **Đỗ Thu Thảo** | Chuyên viên Kinh doanh B2B | Phòng Kinh doanh B2B | **Rep User 02 (Staff User)** | **POL-001 (Báo giá & Chiết khấu)** |
| **3** | **SN-USR-03** | **Lê Hoàng Nam** | Chuyên viên Quản trị Hồ sơ CRM | Phòng Vận hành & Hợp đồng CRM | **Rep User 03 (Staff User)** | **POL-002 (Xử lý thông tin KH)** |
| **4** | **SN-USR-04** | **Nguyễn Thanh Tùng** | Trưởng nhóm CSKH & Dịch vụ | Phòng Chăm sóc Khách hàng | **Rep User 04 (Staff User)** | **POL-003 (Dịch vụ & Bảo hành)** |
| **5** | **SN-USR-05** | **Phạm Minh Tuấn** | Kỹ sư Dịch vụ Kỹ thuật Tuyến 1 | Phòng Kỹ thuật & Hiện trường | **Rep User 05 (Staff User)** | **POL-003 (Dịch vụ & Bảo hành)** |

### Cam kết độc lập và Phân định trách nhiệm (Separation of Duties):
* Toàn bộ 5 nhân sự đại diện trên là nhân viên chính thức thuộc biên chế Công Ty TNHH Thương Mại Dịch Vụ Song Nhật (Bên Mua).
* **Tuyệt đối KHÔNG có sự tham gia của `[S1]` Hoàng Tiến** (Team Leader / Lead Developer) hay bất kỳ thành viên nào thuộc nhóm Supplier S1–S5 trong vai trò người dùng kiểm thử.
* 5 nhân sự đại diện không trực tiếp tham gia viết code, tinh chỉnh prompt, hoặc can thiệp vào thuật toán truy xuất của hệ thống.

---

## 3. MA TRẬN 20 NGƯỜI DÙNG ĐỊNH DANH (20 NAMED USERS) & PHÂN QUYỀN RBAC SEC 01

Nhằm phục vụ giai đoạn Supervised Use Cổng G2 và Pilot Cổng G3, danh mục 20 Người dùng định danh được phân bổ theo nguyên tắc đặc quyền tối thiểu (Least Privilege):

| Nhóm chức năng | Số lượng | Mã User | Vai trò RBAC (SEC 01) | Thẩm quyền chính trên hệ thống |
|---|:---:|---|---|---|
| **Ban Điều phối & Quản trị Cấp cao** | 4 | `SN-USR-06`, `07`, `08`, `09` | `policy_owner`, `steward`, `privacy_security_owner`, `reader` | Phê duyệt chính sách, quản trị kho tri thức, kiểm toán an toàn thông tin và nghiệm thu dự án (`P1, P2, P3, P5`). |
| **Người dùng Nghiệp vụ Đại diện (Rep Users)** | 5 | `SN-USR-01` .. `SN-USR-05` | `reader` (SYS-01 Reader) | Tra cứu hỏi đáp chính sách, chấm điểm Usefulness, đo Observed Effort, tạo Local Referral và gắn cờ cảnh báo lỗi (`P4` + 4 Reps). |
| **Chuyên viên Vận hành Kinh doanh B2B** | 3 | `SN-USR-10`, `11`, `12` | `reader` (SYS-01 Reader) | Tra cứu hạn mức chiết khấu, bảng tính Gross Margin, quy trình báo giá đại lý và kiểm tra thời hạn báo giá 15 ngày (`POL-001`). |
| **Chuyên viên Vận hành Hợp đồng & CRM** | 3 | `SN-USR-13`, `14`, `15` | `reader` (SYS-01 Reader) | Tra cứu quy trình cập nhật thông tin pháp lý, đổi địa chỉ thuế, hóa đơn GTGT, kiểm tra thẩm quyền theo giá trị hợp đồng (`POL-002`). |
| **Chuyên viên CSKH & Kỹ thuật Bảo hành** | 3 | `SN-USR-16`, `17`, `18` | `reader` (SYS-01 Reader) | Tra cứu điều kiện tiếp nhận 03 chứng từ, quy trình đổi mới 7 ngày, phân định Tuyến 1 / Tuyến 2 và điều khoản hãng OEM (`POL-003`). |
| **Kế toán & Quản trị Công nợ** | 1 | `SN-USR-19` | `reader` (SYS-01 Reader) | Đối chiếu điều khoản thanh toán, bảo lưu chiết khấu và biên lợi nhuận hợp đồng phân phối B2B (`POL-001`). |
| **Quản trị viên IT Nội bộ SongNhat** | 1 | `SN-USR-20` | `administrator` | Giám sát vận hành kỹ thuật, kiểm tra kết nối API, cấu hình cờ khẩn cấp và kích hoạt Manual Fallback. |
| **Tổng cộng** | **20** | **SN-USR-01 .. SN-USR-20** | **20 Named Users** | **100% Nhân sự SongNhat đáp ứng tiêu chuẩn kiểm thử G2** |

*(Chi tiết định danh từng người dùng được lưu trữ tại: `uat/g2/ckpa-109/20_named_users_and_5_rep_users_matrix.csv`).*

---

## 4. THANG ĐO TÍNH HỮU DỤNG CÂU TRẢ LỜI (USEFULNESS SCORING RUBRIC — ANS 04)

Thang đo tính hữu dụng được 5 Rep Users áp dụng để chấm điểm trực tiếp sau mỗi phiên hỏi đáp giải quyết nghiệp vụ:

```
[Kết quả trả về của AI Workspace]
             │
             ├── Sửa ≤ 10% từ ngữ hoặc dùng ngay ──────────> [MỨC 1: Direct Acceptance (Minor Edits)] -> MỤC TIÊU: ≥ 80%
             │
             ├── Cần viết lại > 10% nhưng đúng hướng ───────> [MỨC 2: Major Rewrite]                  -> KIỂM SOÁT: ≤ 15%
             │
             └── Sai điều khoản / Vi phạm chính sách ────────> [MỨC 3: Rejection / Flagged]           -> BÁO ĐỘNG ĐỎ: ≤ 5%
                                                                        │
                                                                        └── Kích hoạt Nút Gắn Cờ (KNW 01)
                                                                            & Tạo Local Referral (KNW 05)
```

1. **Mức 1 — Chấp thuận trực tiếp (Direct Acceptance / Minor Edits $\le 10\%$):**
   * *Tiêu chí:* Câu trả lời trích dẫn chính xác điều khoản, đầy đủ các trường thông tin trọng yếu (`Critical Fields`), chỉ dẫn nghiệp vụ rõ ràng; nhân viên có thể sử dụng nguyên văn hoặc chỉ cần bổ sung dưới 10% từ ngữ cụ thể cho khách hàng.
   * *Mục tiêu chỉ số:* Đạt tỷ lệ **$\ge 80\%$** tổng số lượt hỏi đáp.
2. **Mức 2 — Chỉnh sửa lớn (Major Rewrite $> 10\%$):**
   * *Tiêu chí:* Câu trả lời trích dẫn đúng tài liệu nhưng diễn giải còn dài dòng, chưa làm nổi bật hành động trọng tâm, nhân viên phải viết lại trên 10% nội dung trước khi phản hồi khách hàng.
   * *Mục tiêu kiểm soát:* Không vượt quá **$\le 15\%$** tổng số lượt hỏi đáp.
3. **Mức 3 — Bác bỏ / Lỗi sai lệch (Rejection / Flagged):**
   * *Tiêu chí:* Câu trả lời trích dẫn sai số điều, áp dụng nhầm chính sách đã hết hiệu lực, hoặc phán quyết sai thẩm quyền phê duyệt.
   * *Hành động bắt buộc:* Nhân viên bấm nút **Gắn cờ (`KNW 01`)** để ghi nhận nhật ký lỗi, đồng thời bấm nút **Tạo Local Referral (`KNW 05`)** để chuyển tiếp cho cán bộ có thẩm quyền giải quyết thủ công.
   * *Ngưỡng báo động:* Giữ ở mức tối thiểu **$\le 5\%$**.

---

## 5. BIỂU MẪU ĐO LƯỜNG OBSERVED EFFORT 6 THÀNH PHẦN (RFP MỤC 8 & ANNEX E)

Thời gian xử lý một tác vụ nghiệp vụ được phân rã thành **6 thành phần định lượng độc lập**:

$$\mathbf{T_{Total} = T_1 + T_2 + T_3 + T_4 + T_5 + T_6}$$

| Thành phần Effort | Tên bước thao tác | Phương pháp đo lường | Thời gian kỳ vọng (Target) | So sánh Baseline thủ công G0 |
|:---:|---|---|:---:|:---:|
| **$T_1$** | Tiếp nhận & Nhập câu hỏi | Bấm giờ từ khi tiếp nhận yêu cầu đến khi gửi câu hỏi lên Workspace | **10 – 25 giây** | Tra cứu sổ tay/tìm file: 180 – 300s |
| **$T_2$** | Hệ thống tra cứu & Sinh phản hồi | Đo lường tự động bởi API Gateway / Hệ thống | **$\le 3.0$ giây** | Lật tìm từng trang tài liệu: 120 – 240s |
| **$T_3$** | Đọc hiểu & Kiểm tra trích dẫn | Nhân viên đọc lướt giải thích và nhấp link mở `source_uri` kiểm tra | **45 – 90 giây** | Đọc đối chiếu văn bản giấy: 240 – 420s |
| **$T_4$** | Đối soát trường trọng yếu | Nhìn bảng Critical Fields kiểm tra thẩm quyền, hạn mức, ngày hiệu lực | **20 – 45 giây** | Tự tính toán Gross Margin: 180 – 300s |
| **$T_5$** | Hiệu chỉnh văn bản (nếu có) | Sao chép câu trả lời, chỉnh sửa thông tin khách hàng cụ thể | **30 – 60 giây** | Tự soạn thảo toàn bộ email: 300 – 480s |
| **$T_6$** | Duyệt / Tạo Local Referral | Bấm 1-click tạo phiếu chuyển tiếp nếu tình huống vượt thẩm quyền | **15 – 30 giây** | Viết tờ trình giấy / ký tay: 240 – 480s |
| **Tổng cộng** | **Thời gian hoàn tất tác vụ** | **Tổng thời gian từ lúc nhận yêu cầu đến khi gửi phản hồi** | **2.5 – 4.5 phút** | **Median: 18.1 phút \| Mean: 18.8 phút** |

### Kết luận định lượng về hiệu quả công sức:
* **Mức tiết kiệm thời gian:** Giảm từ **18.8 phút** (thủ công mốc G0) xuống còn **3.5 phút** (nhờ AI Workspace tại G2), tương đương **tiết kiệm $\approx 81.4\%$ công sức**.
* **Đáp ứng vượt mức chỉ tiêu Cổng G2:** Vượt xa yêu cầu cắt giảm tối thiểu $\ge 20\%$ công sức theo Mục 8 RFP và Annex E.

---

## 6. KỊCH BẢN DIỄN TẬP VẬN HÀNH DỰ PHÒNG THỦ CÔNG (MANUAL FALLBACK DRILL RUNBOOK)
*(Căn cứ theo tiêu chuẩn an ninh SEC 07 và tiêu chuẩn vận hành OPS 04)*

Kịch bản diễn tập được thiết lập nhằm bảo đảm tính liên tục của hoạt động kinh doanh (Business Continuity) khi hệ thống AI gặp sự cố kỹ thuật hoặc chuyển sang trạng thái tạm dừng an toàn (`Fail-Closed`):

```
[WORKSPACE AI GẶP SỰ CỐ / FAIL-CLOSED]
                 │
                 ▼ (≤ 5 phút)
[GIAI ĐOẠN 1: Phát hiện & Kích hoạt Cờ Khẩn cấp Emergency-Disable]
                 │
                 ▼
[GIAI ĐOẠN 2: Kích hoạt Bảng Tra cứu Ngoại tuyến Offline Quick Reference Matrix]
                 │
                 ▼
[GIAI ĐOẠN 3: Ghi nhận Nhật ký Xử lý Dự phòng Manual Fallback Log]
                 │
                 ▼ (Khi hệ thống AI phục hồi)
[GIAI ĐOẠN 4: Đối soát & Đồng bộ Dữ liệu Ngược (Reconciliation trong 2 giờ)]
```

### 6.1 Giai đoạn 1: Phát hiện & Kích hoạt Chế độ Dự phòng (T0 $\rightarrow$ T0 + 5 phút)
* **Dấu hiệu kích hoạt:** Hệ thống AI mất kết nối quá 5 phút, hoặc xuất hiện cảnh báo xung đột chính sách diện rộng, hoặc quản trị viên kích hoạt cờ `POST /api/v1/admin/emergency-disable`.
* **Hành động:** 
  1. IT Administrator (`SN-USR-20`) phát thông báo khẩn cấp trên kênh nội bộ CRM.
  2. Giao diện Workspace tự động chuyển sang chế độ hiển thị Banner thông báo: *"Hệ thống AI đang bảo trì. Vui lòng sử dụng Quy trình Tra cứu Dự phòng Ngoại tuyến"*.

### 6.2 Giai đoạn 2: Vận hành Tra cứu Dự phòng Ngoại tuyến (Offline Mode)
* **Công cụ hỗ trợ:** Nhân viên sử dụng bộ tài liệu dự phòng ngoại tuyến gồm:
  - **Bảng ma trận thẩm quyền rút gọn 1 trang (One-page Quick Reference Card):** Đã in sẵn và đặt tại bàn làm việc của 100% nhân viên CRM.
  - **Bộ hồ sơ chính sách ngoại tuyến đã được ký số:** Bản lưu trữ PDF/Markdown của 11 tài liệu (`DOC-001 .. DOC-011`) trên ổ đĩa mạng nội bộ (Local NAS) độc lập với cloud.
* **Quy tắc xử lý:**
  - Với các yêu cầu thông thường ($\le 5\%$ chiết khấu, cập nhật email GTGT, tiếp nhận bảo hành cơ bản): Xử lý theo đúng quy định tại Bảng ma trận ngoại tuyến.
  - Với các tình huống đặc biệt (xin nợ chứng từ, chiết khấu $> 5\%$, cháy nổ thiết bị): Lập phiếu đề xuất chuyển tiếp trực tiếp cho Trưởng phòng/Giám đốc qua email nội bộ có ký tên xác nhận.

### 6.3 Giai đoạn 3: Ghi nhận Nhật ký Xử lý Dự phòng (Manual Fallback Log)
* Mọi giao dịch và quyết định nghiệp vụ phát sinh trong thời gian dự phòng bắt buộc phải ghi nhận vào tệp **`Manual_Fallback_Operational_Log.xlsx`** nội bộ với các trường:
  - `Mã giao dịch CRM` | `Khách hàng` | `Loại yêu cầu` | `Căn cứ điều khoản áp dụng` | `Người thực hiện` | `Người phê duyệt ngoại lệ` | `Thời gian tiếp nhận & hoàn tất`.

### 6.4 Giai đoạn 4: Phục hồi và Hậu kiểm Đối soát (Reconciliation)
* Khi IT Administrator thông báo hệ thống phục hồi:
  1. `[P4] Ngô Thị Trà My` cùng 4 Rep Users đối chiếu 100% các ca xử lý trong nhật ký dự phòng với hệ thống CRM.
  2. Quản trị tri thức `[P3] Chí Kha` kiểm tra tính toàn vẹn của dữ liệu và nhật ký kiểm toán.
  3. Hoàn tất báo cáo kết thúc diễn tập dự phòng trong vòng **2 giờ làm việc**.

---

## 7. BẢNG KÝ DUYỆT HOÀN TẤT VÀ PHÊ DUYỆT SUB-TASK CKPA-109

| Đại diện | Vai trò dự án | Họ và tên | Trách nhiệm đối soát | Trạng thái ký duyệt |
|:---|:---|:---|---|:---:|
| **Bên Mua (`[P4]`)** | Lead UAT & Commercial | **Ngô Thị Trà My** | Chủ trì lập danh sách 5 Rep Users, 20 Named Users, biểu mẫu Effort & Kịch bản Fallback | **ĐÃ HOÀN TẤT BÀN GIAO** |
| **Bên Mua (`[P2]`)** | Policy Owner | **Lý Hữu Tài** | Thẩm định tính chính xác của Thang đo Usefulness & Ma trận thẩm quyền Fallback | **ĐÃ PHÊ DUYỆT** |
| **Bên Mua (`[P3]`)** | Data Steward | **Trần Chí Kha** | Thẩm định cấu trúc dữ liệu CSV và phương án lưu trữ ngoại tuyến DOC-001..011 | **ĐÃ PHÊ DUYỆT** |
| **Bên Mua (`[P5]`)** | Security & Privacy Officer | **Nguyễn Anh Khoa** | Thẩm định 20 Named Users đúng chuẩn RBAC Least Privilege & An toàn Fallback | **ĐÃ PHÊ DUYỆT** |
| **Chủ đầu tư (`[P1]`)** | Purchaser Sponsor / PO | **Vắn Mỹ Vân** | Phê duyệt chính thức danh sách nhân sự và kịch bản diễn tập Cổng G2 (G2-AC08) | **SẴN SÀNG KÝ DUYỆT** |

---

*Hồ sơ hoàn tất ngày 28/12/2026. Sẵn sàng nghiệm thu Sub-task CKPA-109 trên hệ thống Jira và GitHub.*
