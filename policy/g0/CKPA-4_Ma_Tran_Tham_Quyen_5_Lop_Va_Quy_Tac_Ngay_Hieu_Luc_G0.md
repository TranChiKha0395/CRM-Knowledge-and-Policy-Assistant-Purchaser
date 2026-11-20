# ĐẶC TẢ MA TRẬN THẨM QUYỀN 5 LỚP NGUỒN (AUTHORITY MATRIX), QUY TẮC NGÀY CHI PHỐI (`ASIA/HO_CHI_MINH`) & ĐIỀU KIỆN BẮT BUỘC `HOLD` — GATE G0 (`DEL 01`)

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`CKPA`)
- **Mã công việc Jira:** `CKPA-8` — *CRM-G0-ST02: [G0][WP01] Chốt 3 họ, Ma trận Thẩm quyền & Ngày* & `CKPA-9` — *CRM-G0-SUB04* (Thuộc Epic `CKPA-3`: *CRM-G0-EP01*)
- **Tham chiếu SRS & RFP:** `SRS-FR-04.1`, `SRS-FR-04.3`, `SRS-FR-04.4`, `INV-01` | `DAT 03`, `DAT 04`, `DAT 05`, `OPS 03`, `DEL 01`
- **Chủ trì ([P2] Policy Owner):** Lý Hữu Tài (*Chủ sở hữu chính sách — Purchaser*)
- **Phối hợp biên soạn ([P3] Knowledge Steward):** Trần Chí Kha (*Quản lý tri thức & Dữ liệu nguồn — Purchaser*)
- **Nhánh Git gợi ý:** `docs/CKPA-8 / CKPA-9-build-authority-and-governing-date-matrix`
- **Ngày hoàn tất:** `16/11/2026` (Múi giờ `Asia/Ho_Chi_Minh`)

---

## 1. Ma trận Thẩm quyền cho 05 Lớp Nguồn Tách biệt (`Authority Matrix — DAT 03 / SRS-FR-04.1`)

Để đảm bảo hệ thống kiểm soát chính sách bằng logic ứng dụng xác định ngoài prompt (`INV-01`), toàn bộ nguồn tri thức đầu vào của SongNhat được phân định thành **05 lớp thẩm quyền tách biệt** (chi tiết trong tệp `CKPA-4_01_Authority_Matrix_5_Layers.csv`):

| Thứ tự | Mã Lớp (`authority_layer`) | Tên Lớp Nguồn & Tài liệu Ánh xạ | Được tạo Quy tắc chung? | Được tự động ghi đè `policy`? | Quy tắc Áp dụng & Xử lý Xung đột (`DAT 03`, `DAT 05`) |
| :---: | :---: | :--- | :---: | :---: | :--- |
| **1** | `policy` | **Chính sách công ty đã ban hành** (`DOC-001` Báo giá, `DOC-002` Thông tin KH, `DOC-003` Bảo hành) | **Có** | Không (chỉ thay thế qua `supersedes` hợp lệ) | Là chuẩn quy chiếu cốt lõi khi ở trạng thái `effective`. Bản phát hành mới nhất **không mặc nhiên thắng** nếu giao dịch có ngày chi phối thuộc kỳ hiệu lực cũ (`superseded`). |
| **2** | `SOP` | **Quy trình thao tác chuẩn** (`DOC-004` Hướng dẫn lập phiếu chiết khấu & Gross Margin) | **Có** (chi tiết hóa thao tác) | **Không** | Hướng dẫn các bước thực thi trên CRM nhưng không được mâu thuẫn với ngưỡng/thẩm quyền tại lớp `policy`. Nếu lệch ngưỡng/SLA với `policy` → kích hoạt **`HOLD_DAT05`**. |
| **3** | `manufacturer_terms` | **Điều khoản kỹ thuật & bảo hành của Nhà sản xuất** (`DOC-005` Tiêu chuẩn hãng động cơ/biến tần) | **Không** (chỉ cho kỹ thuật hãng) | **Không** | Xác định tiêu chuẩn bảo hành gốc của Hãng. Không được dùng để bỏ qua bước thu thập 3 chứng từ CRM nội bộ hoặc tự phán quyết bảo hành/hướng dẫn tự sửa chữa (`HOLD_ANS07`). |
| **4** | `customer_contract` | **Hợp đồng khung / Hợp đồng ký riêng với Khách hàng** (`DOC-006`) | **Không** (chỉ gắn với KH đó) | **Không tự suy diễn** | **Worked Case 5 (`DAT 05`):** Nghiêm cấm tự suy diễn thứ bậc ưu tiên phổ quát giữa `customer_contract` và `policy`. Khi chiết khấu, SLA hoặc MST/Pháp nhân trên Hợp đồng mâu thuẫn với chính sách/CRM → **Bắt buộc `HOLD_DAT05`** và chuyển `Policy Owner`. |
| **5** | `staff_note` | **Ghi chú nhân viên trên CRM / Tiền lệ ngoại lệ cũ** (`DOC-007`) | **CẤM TUYỆT ĐỐI** | **CẤM TUYỆT ĐỐI** | **Worked Case 6 (`ANS 05`):** Chỉ được xem là lịch sử giao dịch có ghi nguồn của đơn hàng cũ. Tuyệt đối không tạo thành quy tắc chung và không dùng để tự duyệt chiết khấu VIP (18%) hay miễn trừ Giấy ĐKKD/Thông báo dấu đỏ. |

---

## 2. Ma trận Quy tắc Ngày Áp dụng (`Governing Date — DAT 04 / OPS 03`) & Sửa Hồi tố

Toàn bộ phép so sánh thời gian trong DB PostgreSQL, bộ lọc trước truy xuất (`Pre-retrieval Filter`) và worker Celery đều khóa cứng theo múi giờ Việt Nam **`Asia/Ho_Chi_Minh` (`UTC+7`)** (chi tiết trong tệp `CKPA-4_02_Governing_Date_And_Conflict_Hold_Rules.csv`):

| Mã Quy tắc | Tình huống Truy vấn | Cách xác định `governing_date` (`Asia/Ho_Chi_Minh`) | Trạng thái Nguồn được phép lấy | Nhãn hiển thị bắt buộc trên UI (`/chat`, `/evidence`) | Xử lý khi Thiếu thông tin hoặc Sửa hồi tố |
| :---: | :--- | :--- | :---: | :--- | :--- |
| **`DATE-01`** | **Câu hỏi quy trình chung** (*Worked Case 1 & 2*) | Mặc định lấy **ngày hiện tại (giờ VN)** tại thời điểm hỏi và hiển thị rõ ngày đó trong `AnswerPackage`. | Chỉ `effective` | `Hướng dẫn hiện hành (YYYY-MM-DD Asia/Ho_Chi_Minh)` | Nếu không có bản `effective` nào khớp `scope`/`audience` → `Fail-closed / HOLD`. |
| **`DATE-02`** | **Giao dịch có ngày cụ thể trong quá khứ** (*Worked Case 3*) | Theo ngày sự kiện nghiệp vụ do `Policy Owner` quy định: Ngày phát hành báo giá (`POL-001`), Ngày nộp đủ chứng từ CRM (`POL-002`), Ngày tiếp nhận ticket/bàn giao thiết bị (`POL-003`). | `effective` hoặc `superseded` (khớp khoảng `[effective_from, effective_to]`) | **`Hướng dẫn lịch sử (Historical Guidance)`** kèm khoảng hiệu lực gốc | Nếu câu hỏi gắn giao dịch cũ nhưng thiếu ngày sự kiện hoặc thiếu `scope` → **Đặt câu hỏi làm rõ**, không đoán mò. |
| **`DATE-03`** | **Chính sách tương lai đã lên lịch** (*Worked Case 4*) | Có `effective_from > now()` (giờ VN), đang ở trạng thái `scheduled`. **Không có hiệu lực chi phối hiện tại.** | `scheduled` (chỉ mở khi hỏi rõ tương lai) | **`Hướng dẫn tương lai đã lên lịch (Future Preview — Chưa có hiệu lực)`** | Cấm dùng bản `scheduled` trả lời cho giao dịch hiện tại. Chỉ chuyển sang `effective` khi đến đúng giờ VN. |
| **`DATE-04`** | **Chỉnh sửa hồi tố (`Retroactive Amendment`)** | Phân biệt rõ `effective_from`/`to` (hiệu lực nghiệp vụ) với `recorded_at` (thời điểm hệ thống ghi nhận) và `published_at`. | Bản mới `effective` + Bản cũ `superseded` | Hiển thị đồng thời `effective_from` và `recorded_at`; gắn cờ câu trả lời cũ bị ảnh hưởng | Tạo phiên bản mới (`VER-002`), **bảo toàn lịch sử đã ghi nhận tại thời điểm cũ** (không ghi đè âm thầm). |
| **`DATE-05`** | **Thu hồi khẩn giữa lúc trả lời** (*Worked Case 9*) | Lệnh `withdrawn` ghi nhận tức thì vào DB (`authoritative state`), độc lập với batch ngày. | **Cấm tuyệt đối** (`withdrawn` bị loại) | Banner cảnh báo đỏ **`Stale / Chính sách vừa bị thu hồi`** | Chặn ngay tại bước kiểm tra cuối (`Final Pre-Display Check`), xóa cache Redis `<= 5 phút`. |

---

## 3. Danh mục Điều kiện Bắt buộc Phải `HOLD` (Chặn Kết luận Tự động)

Hệ thống (`backend/src/modules/policy` & `validation`) bắt buộc chuyển kết luận sang trạng thái **`HOLD`**, nêu rõ lý do (`hold_reason`), hiển thị bằng chứng hợp lệ liên quan và định tuyến về `Policy Owner` trong **05 trường hợp** sau:

1. **`HOLD_DAT05` (Xung đột nguồn hoặc chồng lấn hiệu lực):**
   - Điều khoản trong Hợp đồng khách hàng (`customer_contract`) mâu thuẫn với chính sách chung (`policy`) như mức chiết khấu khung hoặc thông tin MST/Pháp nhân lệch giữa Hợp đồng và CRM (*Worked Case 5, DEV-006, DEV-011*).
   - Hai phiên bản chính sách cùng có khoảng hiệu lực `[effective_from, effective_to]` chồng lấn nhau trên cùng một `scope` mà không có quan hệ thay thế (`supersedes`) rõ ràng.
2. **`HOLD_DAT08` (Thiếu chứng từ cốt lõi, bảng biểu hoặc chú thích thiết yếu):**
   - Đoạn chính sách hoặc trường ngưỡng có `has_essential_attachments = false` (thiếu bảng phân cấp, thiếu chú thích điều kiện ngoại lệ — *Worked Case 7*).
   - Hồ sơ bảo hành bị mờ/rách tem thông số `Nameplate / Serial (S/N)` hoặc mất Phiếu bảo hành chính hãng nhưng xin hỗ trợ đặc biệt (*DEV-045 / PAS-026*), hoặc bản scan Giấy ĐKKD/Thông báo dấu đỏ bị mờ không đọc được (*PAS-020*).
3. **`HOLD_ANS06` (Thiếu thông tin tiên quyết — `Missing Facts`):**
   - Người dùng hỏi về một giao dịch lịch sử hoặc trường hợp phụ thuộc ngưỡng nhưng chưa cung cấp: `governing_date` (ngày phát hành báo giá/bàn giao), `order_value` (giá trị đơn hàng), `cumulative_contract` (tổng HĐ lũy kế `< 500M` hay `>= 500M`), hoặc `power_kw` (công suất `<= 37 kW` hay `> 37 kW`). Hệ thống phải giữ kết luận và liệt kê câu hỏi làm rõ (`missing_facts`).
4. **`HOLD_ANS07` (Vượt ranh giới nghiệp vụ được phép — `Out-of-Boundary Refusal`):**
   - Yêu cầu tự cấp chiết khấu/ngoại lệ, suy luận ưu đãi từ khách hàng VIP/ghi chú cũ (`staff_note`), xin ý kiến tư vấn pháp lý/thuế, xin cấp quyền tiết lộ dữ liệu cá nhân, hoặc yêu cầu **phán quyết bảo hành miễn phí/tính phí và hướng dẫn tự tháo lắp sửa chữa thiết bị** (*DEV-015 / PAS-025*).
5. **`HOLD_SEC05` / `FAIL_CLOSED` (Nguồn bị thu hồi hoặc không xác minh được quyền/trạng thái):**
   - Nguồn trích dẫn vừa chuyển sang `withdrawn` trước khi hiển thị (*Worked Case 9*), dịch vụ kiểm tra RBAC/DB không phản hồi (`INV-02`), hoặc chạm trần hạn mức gói hỏi/LLM calls tháng (`OPS 08`).

---

## 4. Xác nhận Phê duyệt Cổng G0 (`Policy Owners & Nhóm Chính sách & Tri thức Sign-off`)

- **Chủ trì thiết kế logic (`[P2] Policy Owner` — Policy & Lifecycle Eng):** Hữu Tài (`Huutai12`)
- **Phối hợp biên soạn quy tắc & ánh xạ nguồn (`[P3] Knowledge Steward` — Policy & Knowledge Steward):** Trần Chí Kha
- **Phê duyệt bởi Chủ sở hữu Chính sách (`Policy Owners` — 3 Nhóm `POL-001`, `POL-002`, `POL-003`):** *Xác nhận áp dụng Ma trận Thẩm quyền 5 lớp, Quy tắc Ngày chi phối (`Asia/Ho_Chi_Minh`) và 5 nhóm điều kiện bắt buộc `HOLD` từ Gate G0.*
