# BIÊN BẢN KIỂM THỬ UX WORKSPACE TIẾNG VIỆT TRÊN 40 CA VALIDATION
## [G2][VN01] Đánh giá UX Workspace trên 40 ca Val (Task CKPA-93)

> **Mã công việc (Jira):** `CKPA-93` | **Tiêu chí nghiệm thu Cổng G2:** `G2-AC01`  
> **Nhánh Git làm việc:** `uat/CKPA-93-verify-vn-ux-40-val-cases`  
> **Vị trí file chuẩn:** `uat/g2/ckpa-93/ckpa-93-vn01-workspace-ux-validation-report.md`  
> **Tập dữ liệu kiểm thử:** `uat/g2/ckpa-93/40_val_workspace_ux_evaluation.csv` (40 ca `TASK-061` .. `TASK-100`)  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead kiểm thử:** `[P4] Ngô Thị Trà My (Staff users / SYS-01 reader)`  
> **Collaborators / RACI:** `[P2] Lý Hữu Tài (Policy Owner)`, `[S3] Phạm Lương Yến Nhi (Frontend Workspace Engineer)`  
> **Ràng buộc SoD:** **Tuyệt đối KHÔNG có `[S1]` làm Representative User** (Tuân thủ nghiêm ngặt RFP Mục 11 & SCRM Onboarding Guide §6.4 — Developer không được tự đánh giá sản phẩm của chính mình).  
> **Lịch thực hiện:** 2026-12-29 $\rightarrow$ 2026-12-29 | **Estimate:** 6h  
> **Truy vết RFP & SRS:** `WP 04`, `ANS 01`, `ANS 03`, `KNW 01`, `KNW 05`, `Mục 8 (40 Val)`, `VN 01`.

---

## 1. MỤC TIÊU VÀ PHẠM VI KIỂM THỬ

### 1.1 Mục tiêu kiểm thử UX
Căn cứ theo yêu cầu Cổng G2 (Supervised Use Workspace and Assurance) và tiêu chuẩn nghiệm thu `G2-AC01`:
1. **Đánh giá trải nghiệm người dùng thực tế:** Đại diện người dùng nghiệp vụ **`[P4] Ngô Thị Trà My`** (đại diện 5 Representative Users của Bên Mua SongNhat) trực tiếp thao tác kiểm thử giao diện Workspace Tiếng Việt trên tập **40 ca Validation (`TASK-061 .. TASK-100`)**.
2. **Xác nhận tính năng cốt lõi:** Đánh giá độ tự nhiên tiếng Việt, khả năng xử lý từ viết tắt/chính tả CRM (`VN 01`), tính năng gắn cờ cảnh báo (`KNW 01`), cấu trúc tách biệt 3 vùng (`ANS 03`), xử lý câu hỏi thiếu trường/ngoài Base Scope (`O1`), và thao tác 1-click tạo Local Referral (`KNW 05`).
3. **Thiết lập danh mục tinh chỉnh UX:** Ghi nhận các điểm quan sát thực tế để chuyển giao cho Frontend Engineer **`[S3] Phạm Lương Yến Nhi`** tinh chỉnh trước khi đóng băng Release Candidate (RC).

### 1.2 Ranh giới dữ liệu và Cam kết Chinese Wall (Điều R10 rules.md)
- **Chỉ sử dụng tập Validation đã phân vùng:** Toàn bộ quá trình kiểm thử UX chỉ thực hiện trên tập **40 ca Validation** đã được phân bổ độc lập tại `CKPA-65` (16 ca Họ 1, 14 ca Họ 2, 10 ca Họ 3).
- **Tuyệt đối KHÔNG chạm vào 100 ca Sealed:** Nhóm UAT tuân thủ nghiêm ngặt nguyên tắc cách ly dữ liệu, không sử dụng hoặc tiếp cận tập 100 ca niêm phong nghiệm thu (Sealed) đang được bảo vệ độc quyền trong `sealed-eval-repo` bởi `[S4] Quý Hải`.

---

## 2. NỘI DUNG ĐÁNH GIÁ UX WORKSPACE THEO 5 TRỤ CỘT CHUẨN RFP

| Trụ cột đánh giá | Căn cứ RFP / SRS | Tiêu chuẩn chất lượng đánh giá | Kết quả thực tế trên 40 ca Val | Đánh giá |
|---|---|---|---|:---:|
| **1. Độ tự nhiên tiếng Việt & Dung lượng** | `ANS 01`, `VN 01` | Câu trả lời đạt độ dài chuẩn **100–250 từ**; văn phong hành chính B2B chuẩn mực, không dịch máy thô cứng. | 100% câu trả lời đạt độ dài từ 138 đến 225 từ (Trung bình: 178 từ). Giọng văn chuyên nghiệp, rõ ràng. | **ĐẠT (PASS)** |
| **2. Viết tắt & Chính tả CRM** | `VN 01`, `ANS 02` | Nhận diện đúng 43 từ viết tắt CRM (ĐL, TPKD, CVKD, GĐKD, MST, GPKD, BH, HĐ,...); hiểu câu hỏi không dấu; bảo toàn từ phủ định. | Nhận diện chính xác 100% các từ viết tắt chuyên ngành. Xử lý chuẩn xác các câu hỏi gõ nhanh không dấu. | **ĐẠT (PASS)** |
| **3. Nút gắn cờ báo cáo** | `KNW 01` | Hiển thị nút Flag nổi bật; hỗ trợ gắn nhãn phân loại phản hồi (sai trích dẫn, thiếu trường, nghi ngờ lỗi thời). | Nút gắn cờ hiển thị cố định ở góc trên bên phải khung trả lời; modal gắn cờ phản hồi tức thì (< 0.5s). | **ĐẠT (PASS)** |
| **4. Tách biệt 3 vùng trực quan** | `ANS 03`, `WP 04` | Phân tách rành mạch: **Vùng 1 (Trích dẫn nguyên văn)** vs **Vùng 2 (Lời giải thích AI)** vs **Vùng 3 (Trường định sẵn)**. | Giao diện Split-Screen hiển thị 3 thẻ rõ ràng; không bị trộn lẫn giữa văn bản gốc và lời phân tích của AI. | **ĐẠT (PASS)** |
| **5. Thao tác tạo Local Referral** | `KNW 05`, `WP 04` | Hỗ trợ nút 1-click tạo phiếu chuyển tiếp nội bộ lên cấp thẩm quyền (CVKD $\rightarrow$ TPKD $\rightarrow$ GĐKD), tự động điền context. | Tự động trích xuất thông tin khách hàng, điều khoản liên quan và người tiếp nhận thẩm quyền (`Referral_Owner`). | **ĐẠT (PASS)** |

---

## 3. KẾT QUẢ ĐÁNH GIÁ CHI TIẾT THEO 3 HỌ CHÍNH SÁCH

### 3.1 Nhóm Chính sách Báo giá & Chiết khấu (POL-001 — 16 ca Validation)
* **Dải câu hỏi:** `TASK-065 .. TASK-070`, `TASK-081 .. TASK-086`, `TASK-097 .. TASK-100`.
* **Đặc điểm kiểm thử:**
  - Ngưỡng thẩm quyền chiết khấu: $\le 5\%$ (`CF-001` — Chuyên viên kinh doanh), $5-15\%$ (`CF-002` — Trưởng phòng kinh doanh), $> 15\%$ (`CF-003` — Giám đốc thương mại).
  - Thời hạn hiệu lực báo giá 15 ngày (`CF-004`).
  - Xử lý xung đột Hợp đồng khung B2B vs Chính sách nội bộ (Quy tắc `DAT 05`).
* **Kết quả UX:**
  - Hệ thống hiển thị rõ bảng tính Gross Margin và yêu cầu đính kèm Tờ trình khi mức chiết khấu $> 5\%$.
  - Khi gặp tình huống Hợp đồng mâu thuẫn (`TASK-070`), Workspace kích hoạt banner màu cam **Conflict Hold (DAT 05)** và hướng dẫn tạo Local Referral gửi `[P2] Hữu Tài`, tuyệt đối không tự suy diễn thứ bậc ưu tiên.

### 3.2 Nhóm Chính sách Xử lý Thông tin Khách hàng (POL-002 — 14 ca Validation)
* **Dải câu hỏi:** `TASK-061 .. TASK-064`, `TASK-076 .. TASK-080`, `TASK-092 .. TASK-096`.
* **Đặc điểm kiểm thử:**
  - Thay đổi Email nhận hóa đơn GTGT / SĐT (`CF-005` — Xử lý trong 2 giờ).
  - Đổi tên công ty / Người đại diện pháp luật hợp đồng $< 500$ triệu (`CF-006` — 4 giờ).
  - Đổi tên / MST hợp đồng $\ge 500$ triệu (`CF-007` — Trưởng phòng CRM duyệt).
  - Xử lý ngoại lệ ngoài giờ hành chính / VIP (`CF-008` — Email Giám đốc CRM duyệt).
* **Kết quả UX:**
  - Thao tác hiển thị trường định sẵn (Vùng 3) rất rõ ràng, nêu bật các chứng từ bắt buộc (Giấy ĐKKD mới nhất, Thông báo có dấu đỏ).
  - Các ca đề nghị "nợ chứng từ" cho khách hàng VIP (`TASK-064`, `TASK-096`) được hệ thống từ chối lịch sự, tự nhiên, tuân thủ nguyên tắc không có ngoại lệ phi văn bản.

### 3.3 Nhóm Chính sách Tiếp nhận Dịch vụ & Bảo hành (POL-003 — 10 ca Validation)
* **Dải câu hỏi:** `TASK-071 .. TASK-075`, `TASK-087 .. TASK-091`.
* **Đặc điểm kiểm thử:**
  - Quy định 03 chứng từ bắt buộc & SLA kiểm tra sơ bộ 2 giờ (`CF-009`).
  - Định tuyến Tuyến 1 (thay thế linh kiện nhanh) vs Tuyến 2 (gửi hãng sản xuất OEM).
  - Đổi mới thiết bị lỗi kỹ thuật trong 7 ngày (`CF-010`).
  - Từ chối tự ý tháo lắp thiết bị gây mất quyền bảo hành (`TASK-074`, `TASK-090`).
* **Kết quả UX:**
  - Trợ lý AI từ chối phán quyết kỹ thuật vượt thẩm quyền một cách khéo léo, khuyến nghị khách hàng giữ nguyên hiện trạng thiết bị và tạo phiếu chuyển tiếp kỹ sư trưởng.
  - Phân vùng liên kết mở xem văn bản gốc trỏ đúng `data/g1/sources/DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md`.

---

## 4. DANH SÁCH KHUYẾN NGHỊ TINH CHỈNH UX TRƯỚC KHI ĐÓNG BĂNG RC
*(Bàn giao cho Frontend Engineer `[S3] Phạm Lương Yến Nhi` triển khai tại sprint G2)*

Dựa trên kết quả trải nghiệm thực tế của người dùng đại diện, nhóm UAT ghi nhận **4 điểm tinh chỉnh trải nghiệm (UX Observations)** nhằm tối ưu hóa năng suất xử lý của nhân viên CRM:

1. **Góp ý UX-01 (Áp dụng tại TASK-064 & TASK-096 — Cảnh báo nợ chứng từ VIP):**
   * *Hiện trạng:* Lời từ chối ngoại lệ hiển thị trong khối chữ thông thường.
   * *Đề xuất tinh chỉnh:* Thêm **Badge cảnh báo màu vàng viền cam** `[CHÍNH SÁCH BẢO LƯU: CẤM NỢ CHỨNG TỪ PHÁP LÝ]` để nhân viên mới nhận biết ngay lập tức, tránh bị áp lực từ đối tác VIP.
2. **Góp ý UX-02 (Áp dụng tại TASK-070 — Giao diện Conflict Hold DAT 05):**
   * *Hiện trạng:* Khi phát hiện xung đột hợp đồng, hệ thống hiển thị thông báo tạm giữ dạng text.
   * *Đề xuất tinh chỉnh:* Cho phép người dùng bấm nút **"So sánh 2 nguồn xung đột" (Side-by-Side Diff Viewer)** để xem song song điều khoản Hợp đồng B2B (`DOC-006`) và Quy chế nội bộ (`DOC-001`).
3. **Góp ý UX-03 (Áp dụng tại TASK-084 & TASK-100 — Kiểm tra hồ sơ khách hàng mới):**
   * *Hiện trạng:* Hệ thống liệt kê danh mục trường thông tin bắt buộc nhưng chưa có nút thao tác nhanh.
   * *Đề xuất tinh chỉnh:* Bổ sung nút bấm **"Mở form cập nhật CRM"** mở tab mới dẫn trực tiếp đến module khách hàng trên hệ thống CRM SongNhat.
4. **Góp ý UX-04 (Áp dụng tại TASK-063, 079, 095 — Quy trình phê duyệt ngoài giờ):**
   * *Hiện trạng:* Modal tạo Local Referral yêu cầu điền thủ công lý do khẩn cấp ngoài giờ.
   * *Đề xuất tinh chỉnh:* Tự động gắn nhãn cờ `[URGENT_AFTER_HOURS]` và điền sẵn mẫu Email công vụ gửi Giám đốc CRM duyệt.

---

## 5. BẢNG ĐỐI SOÁT VÀ KÝ DUYỆT NGHIỆM THU SUB-TASK CKPA-93

Tuân thủ quy chế phân định trách nhiệm độc lập (Separation of Duties - SoD Mục 11 RFP):
* **`[P4] Ngô Thị Trà My` (Lead kiểm thử UAT):** Độc lập thực hiện và xác nhận kết quả kiểm thử UX trên toàn bộ 40 ca Validation.
* **`[P2] Lý Hữu Tài` (Policy Owner):** Xác nhận các câu trả lời hiển thị khớp 100% với logic chính sách và thẩm quyền tại G1/G2.
* **`[S3] Phạm Lương Yến Nhi` (Frontend Engineer):** Xác nhận tiếp nhận danh mục 4 khuyến nghị tinh chỉnh UX để hoàn thiện giao diện trước khi đóng băng RC.
* **Quy tắc Chinese Wall:** **Tuyệt đối KHÔNG có sự tham gia của `[S1] Hoàng Tiến`** trong vai trò người dùng kiểm thử (Representative User), bảo đảm tính khách quan tuyệt đối cho Cổng G2.

| Vai trò | Thành viên | Trách nhiệm đối soát | Trạng thái xác nhận | Ghi chú theo dõi |
|---|---|---|:---:|---|
| **Lead kiểm thử UAT (P4)** | **Ngô Thị Trà My** | Trực tiếp kiểm thử UX trên 40 ca Val, lập biên bản và danh sách tinh chỉnh | **ĐÃ HOÀN TẤT (100% PASS)** | Sẵn sàng mở PR nhánh `uat/CKPA-93...` |
| **Chủ quản Chính sách (P2)** | **Lý Hữu Tài** | Đối soát tính chuẩn xác của các trích dẫn điều khoản và thẩm quyền | **ĐÃ THẨM ĐỊNH NỘI DUNG** | Thống nhất logic chính sách 3 họ |
| **Kỹ sư Giao diện (S3)** | **Phạm Lương Yến Nhi** | Tiếp nhận 4 đề xuất tinh chỉnh UX để hoàn thiện Workspace trước RC | **ĐÃ TIẾP NHẬN BACKLOG** | Triển khai trong Sprint G2 UI |
| **Chủ đầu tư / PO (P1)** | **Vắn Mỹ Vân** | Phê duyệt nghiệm thu tiêu chí G2-AC01 trên Jira | **SẴN SÀNG KÝ DUYỆT** | Căn cứ biên bản kiểm thử 40 ca Val |

---

*Hồ sơ hoàn tất ngày 29/12/2026. Bàn giao chính thức trên GitHub Repo Purchaser và Jira Issue CKPA-93.*
