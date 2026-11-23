# BIÊN BẢN XÁC NHẬN PHẠM VI GATE G0, CHỐT 03 NHÓM CHÍNH SÁCH KHỞI ĐẦU, POLICY OWNERS & RANH GIỚI `IN-SCOPE (M)` / `O1 (OFF)` / `OUT-OF-SCOPE (O)`

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`CKPA`)
- **Mã công việc Jira:** `CKPA-8` — *CRM-G0-ST02: [G0][WP01] Chốt 3 họ, Ma trận Thẩm quyền & Ngày* & `CKPA-9` — *CRM-G0-SUB04* (Thuộc Epic `CKPA-3`: *CRM-G0-EP01 [G0][WP01] Khảo sát Discovery & Hồ sơ Cổng G0*)
- **Tham chiếu SRS & RFP:** `SRS Mục 2.1–2.3`, `SRS-FR-01.1` | `RFP Mục 2`, `WP 01`, `VN 04`, `DEL 01`
- **Chủ trì thực hiện ([P2] Policy Owner):**Hữu Tài (*Chủ sở hữu chính sách — Purchaser*)
- **Đại diện Bên Mua / Product Owner ([P1] Purchaser Sponsor):** Văn Mỹ Vân (*Chủ đầu tư dự án*)
- **Điều phối Scrum / Đại diện Supplier ([S1] Named Lead):** Hoàng Tiến (*Trưởng nhóm Nhà cung cấp*)
- **Phối hợp 10 thành viên chuẩn RFP Mục 11:**
  - Phía Bên Mua (Purchaser): [P1] Văn Mỹ Vân, [P2] Hữu Tài, [P3] Trần Chí Kha, [P4] Ngô Thị Trà My, [P5] Nguyễn Anh Khoa
  - Phía Nhà Cung Cấp (Supplier): [S1] Hoàng Tiến, [S2] Trần Quốc Hưng, [S3] Phạm Lương Yến Nhi, [S4] Phạm Quý Hải, [S5] Nguyễn Ngọc Duy
- **Nhánh Git gợi ý:** `docs/CKPA-1-define-g0-scope-and-policy-families`
- **Ngày hoàn tất & Ký duyệt:** `16/11/2026` (Múi giờ `Asia/Ho_Chi_Minh`)

---

## 1. Xác nhận 03 Nhóm Chính sách Khởi đầu & Sàng lọc Nhóm Thiếu Chủ sở hữu (`SRS Mục 2.1` & `VN 04`)

Thực hiện yêu cầu của `WP 01`, `VN 04` và `SRS Mục 2.1`, `[S1] Named Lead` (Hoàng Tiến) đã chủ trì rà soát cùng các Chủ sở hữu Chính sách (`Policy Owners`) của SongNhat và thống nhất **chốt cứng `03` nhóm chính sách khởi đầu đưa vào Phạm vi Cơ sở (`In-Scope Base — M`)**, đồng thời **đánh dấu loại trừ (`EXCLUDED_AT_G0`) `02` nhóm đề xuất phụ chưa có Policy Owner / nằm ngoài ranh giới `ANS 07`** (chi tiết tại tệp đính kèm `CKPA-1_01_Policy_Families_And_Owners_Signoff.csv`):

| Mã Nhóm (`Policy_ID`) | Tên Nhóm Chính sách & Tài liệu Gốc | Quyết định tại `G0` | Phạm vi Hỗ trợ Được Phép (`M`) | Giới hạn Cứng Tuyệt đối Không Được Vượt (`ANS 07`) | Chủ sở hữu Chính (`Policy Owner`) | Người Thay thế (`Backup Owner`) | Quy mô Mẫu `G0` & Trần `G1` |
| :---: | :--- | :---: | :--- | :--- | :--- | :--- | :---: |
| **`POL-001`** | **1. Báo giá và phê duyệt thương mại**<br>(`DOC-001`, `VER-001`) | **`IN_SCOPE_BASE (M)`** | Giải thích thông tin CRM bắt buộc, ngưỡng chiết khấu/đơn hàng (`CF-001..004`) và tuyến xử lý ngoại lệ thương mại đã duyệt | Không tự cấp ngoại lệ/chiết khấu; không suy luận phê duyệt từ khách VIP/ghi chú cũ; không tự tạo điều khoản | **Commercial Policy Owner**<br>(`Sales Director` — *Phụ trách chính sách: `[P2]` Hữu Tài*) | **Deputy Sales Director**<br>(`Backup Owner 1`) | **G0:** `10` đoạn / `04` trường<br>**G1:** `<= 100` đoạn / `<= 18` trường |
| **`POL-002`** | **2. Xử lý thông tin khách hàng CRM**<br>(`DOC-002`, `VER-001`) | **`IN_SCOPE_BASE (M)`** | Giải thích quy trình ghi nhận, chỉnh sửa hoặc xác minh thông tin liên hệ/pháp lý khách hàng đã phê duyệt (`CF-005..008`) | Không tự tiết lộ dữ liệu khách hàng; không tự sửa bản ghi CRM; không tự xác lập cơ sở pháp lý hoặc miễn trừ chứng từ | **CRM Data Governance Owner**<br>(`CRM Manager`) | **Senior CRM Lead**<br>(`Backup Owner 2`) | **G0:** `10` đoạn / `04` trường<br>**G1:** `<= 100` đoạn / `<= 16` trường |
| **`POL-003`** | **3. Định tuyến yêu cầu dịch vụ / bảo hành**<br>(`DOC-003`, `VER-001`) | **`IN_SCOPE_BASE (M)`** | Xác định 3 chứng từ bắt buộc, tuyến chuyển tiếp theo công suất (`<= 37 kW` vs `> 37 kW`, `CF-009..010`) và chủ sở hữu bảo hành được ủy quyền | Không tự quyết định quyền được bảo hành miễn phí/tính phí; không hướng dẫn tháo lắp hoặc sửa chữa thiết bị công nghiệp | **Warranty Policy Owner**<br>(`Service Director`) | **Internal Tech Lead**<br>(`Backup Owner 3`) | **G0:** `10` đoạn / `02` trường<br>**G1:** `<= 100` đoạn / `<= 16` trường |
| `EX-POL-004` | *Chính sách Công nợ, Thuế & Kế toán Hợp đồng* | **`EXCLUDED_AT_G0 (O)`** | *Loại khỏi Base Scope* | Tư vấn thuế/pháp lý thuộc danh mục từ chối bắt buộc (`ANS 07`) | *Chưa chỉ định tại G0* | *Không có* | `0` *(Loại bỏ theo `VN 04`)* |
| `EX-POL-005` | *Quy trình Logistics, Kho vận & Giao nhận Quốc tế* | **`EXCLUDED_AT_G0 (O)`** | *Loại khỏi Base Scope* | Nằm ngoài 3 họ quy trình CRM khởi đầu của RFP Mục 2 | *Chưa chỉ định tại G0* | *Không có* | `0` *(Loại bỏ theo `VN 04`)* |

> **Xác nhận tính sẵn sàng của Chủ sở hữu (`VN 04`):** Cả `03` nhóm chính sách trong Base Scope (`POL-001`, `POL-002`, `POL-003`) đều đã có quyết định phân công **Chủ sở hữu chính thức (`Policy Owner`) kèm Người thay thế (`Backup Owner`)** và văn bản nguồn chuẩn hóa (`DOC-001..007`). Tuyệt đối không để nhà cung cấp/nhóm kỹ thuật tự bịa quy tắc thay cho Policy Owner.

---

## 2. Phân định Ranh giới Tuyệt đối: `In-Scope Base (M)` vs `Optional O1 (OFF)` vs `Out-of-Scope (O)` (`SRS Mục 2.2 & 2.3`)

Toàn bộ kiến trúc, mã nguồn (`backend/`, `frontend/`, `worker/`), cơ sở dữ liệu và kế hoạch kiểm thử của đội `10` thành viên tuân thủ nghiêm ngặt ma trận phân định ranh giới dưới đây (chi tiết tại tệp đính kèm `CKPA-1_02_Base_Scope_O1_And_Out_Of_Scope_Matrix.csv`):

### 2.1 Danh mục Phạm vi Cơ sở Bắt buộc (`In-Scope Base — M` / Common Bid Basis)

| Mã Hạng mục | Nhóm Tham số Cơ sở | Giới hạn Hợp đồng Bắt buộc (`M`) | Cơ chế Kiểm soát & Thực thi trong Hệ thống |
| :---: | :--- | :--- | :--- |
| **`SCP-M01`** | **Tổ chức & Người dùng** | `1` công ty (`SongNhat`); tối đa **`20` named users**; tối đa **`5` phiên đồng thời** | Phân quyền tối thiểu (`reader`, `steward`, `policy_owner`, `administrator`, `privacy_security_owner`, `legal_owner`, `independent_evaluator`); lọc `audience` 3 lớp (`pre-retrieval`, `pre-generation`, `pre-display`). |
| **`SCP-M02`** | **Kho tri thức & Đầu vào CSV** | Tối đa **`30` tài liệu**, **`300` đoạn (`passages`)**, **`50` dòng `critical_fields`** qua đúng **`2` tệp CSV UTF-8** | G0 duyệt trước `30` đoạn + `10` trường (`CKPA-3`). **Cấm nhập hồ sơ khách hàng, lịch sử hộp thư hoặc hồ sơ CRM đầy đủ.** Dòng thiếu chú thích thiết yếu (`has_essential_attachments=false`) bị đẩy vào `Quarantine` (`DAT 08`). |
| **`SCP-M03`** | **Làm mới & Rút chính sách** | `1` batch hằng ngày/schema (**`<= 500` dòng thay đổi/`30` phút**); rút chính sách (`withdrawn`) tức thời | Hiển thị **tuổi snapshot (`Snapshot Age`, cảnh báo `> 25h`)**; thu hồi chính sách chặn ngay ở bước kiểm tra cuối và dọn sạch cache Redis trong **`<= 5 phút (`300s`)** (`OPS 05`). |
| **`SCP-M04`** | **Hạn mức Yêu cầu & AI** | Trần **`1.000` `AnswerPackage`/tháng** (tính cả `hold`/`error`); tối đa **`2` LLM calls/package** (`<= 6.000` input / `<= 900` output tokens); trần **`2.000` calls/tháng** | Gói ngữ cảnh tối đa `8` đoạn (`<= 6.000` ký tự Unicode/đoạn); câu trả lời `100–250` từ tiếng Việt; **không cắt cụt âm thầm**; chạm trần hạn mức phải chuyển `HOLD` rõ ràng (`OPS 08`). |
| **`SCP-M05`** | **Kiểm soát Xác định Ngoài Prompt** | `5` lớp thẩm quyền (`DAT 03`), `7` trạng thái vòng đời (`KNW 03`), `governing_date` theo **`Asia/Ho_Chi_Minh`**, `Conflict Hold` (`DAT 05`) | Mọi phép toán biên (`<, <=, ==, >=, >, between`) của `critical_fields` chạy bằng Python/SQL xác định (`INV-01`, `INV-04`); **cấm streaming trước khi kiểm chứng xong** (`INV-03`). |
| **`SCP-M06`** | **Lộ trình 5 Cổng (`G0–G4`)** | `2` tuần Discovery (`G0`) + `10` tuần triển khai cơ sở (gồm tối thiểu **`20` ngày làm việc** quan sát Pilot tại `G3`) | Không gộp `G3` và `G4`; quyết định mở rộng tách riêng với nghiệm thu Pilot; duy trì hàng rào độc lập **Chinese Wall** đối với bộ `100 Sealed`. |

---

### 2.2 Quyết định Tách biệt Tùy chọn `O1 — Selected CRM Context` (`OFF` tại Base Scope)

- **Mã hạng mục:** `SCP-O1` (`Optional O1 — Selected CRM Context`, tham chiếu `RFP Mục 2`, `DAT 07`, `SEC 08`, `SRS Mục 1.4 & 2.3`).
- **Quyết định chính thức tại Cổng G0:** **TÁCH RIÊNG VÀ TẮT HOÀN TOÀN (`OFF`) TRONG BASE SCOPE.**
  1. **Không trộn vào Codebase & DB Cơ sở:** Trong phạm vi cơ sở (`M`), hệ thống chỉ tiếp nhận đúng `02` tệp CSV UTF-8 (`passages.csv` 21 cột và `critical_fields.csv` 23 cột). Không mở đường dẫn `/api/v1/ingestion/o1-context`, không tạo bảng lưu trữ bản ghi khách hàng `O1` và không bật cờ `FEATURE_O1_CRM_CONTEXT_ENABLED` (được kiểm tra tự động bằng unit test tại `backend/tests/test_srs_scaffold_contracts.py`).
  2. **Điều kiện kích hoạt trong tương lai (nếu có):** Tùy chọn `O1` (schema CSV thứ 3 cho tối đa `2.000` dòng đầu / `5.000` dòng lưu giữ, chọn tối đa `1` bản ghi được kiểm soát quyền `DAT 07`) chỉ được triển khai khi có **Báo giá riêng, Phụ lục hợp đồng / Change Request (`SEC 08`) và Phê duyệt Pháp lý (`SEC 03`) tách biệt**, tuyệt đối không giả định `O1` nằm sẵn trong tiến độ 10 tuần cơ sở.

---

### 2.3 Danh sách 10 Hạng mục Ngoài Phạm vi Mặc định (`Out-of-Scope — O`, CẤM đưa vào Base Pilot)

| Mã Loại trừ | Hạng mục Ngoài Phạm vi (`Out-of-Scope — O`) | Quy tắc Cưỡng chế Kỹ thuật & Vận hành (`SRS Mục 2.3`) |
| :---: | :--- | :--- |
| **`SCP-O01`** | **1. Kết nối trực tiếp tới CRM hoặc kho dữ liệu sống (`Live Connectors`)** | Cấm kết nối trực tiếp vào DB/API CRM sản xuất; chỉ nạp qua `2` tệp CSV UTF-8 đã kiểm duyệt. |
| **`SCP-O02`** | **2. OCR, xử lý giọng nói/âm thanh, tích hợp kênh Zalo hoặc lịch sử hộp thư (`Mailbox`)** | Cấm tích hợp Zalo, voice hoặc đồng bộ hòm thư; chỉ giao tiếp văn bản qua Workspace nội bộ. |
| **`SCP-O03`** | **3. Tự động đọc/trích xuất bảng biểu, sơ đồ hoặc PDF gốc chưa chuẩn hóa** | Bảng biểu/chú thích phải được Steward & Policy Owner chuẩn hóa thủ công sang CSV UTF-8 (`VN 03`); thiếu chú thích (`has_essential_attachments=false`) bị đẩy vào `Quarantine` (`DAT 08`). |
| **`SCP-O04`** | **4. Ngôn ngữ hoặc nhóm chính sách ngoài `03` nhóm đã chốt (sinh câu trả lời tiếng Anh)** | Chỉ trả lời tiếng Việt cho đúng 3 nhóm POL-001, POL-002, POL-003; cấm âm thầm dịch điều khoản ràng buộc. |
| **`SCP-O05`** | **5. Soạn thảo phản hồi sẵn sàng gửi trực tiếp ra khách hàng bên ngoài (`KNW 02`)** | Mọi `AnswerPackage` đều gắn cảnh báo bắt buộc `INTERNAL_USE_WARNING_VI` (*"Hướng dẫn làm việc nội bộ..."*). |
| **`SCP-O06`** | **6. Ghi ngược vào CRM (`Writeback`), tự tạo task CRM (`KNW 05`) hoặc tự động phê duyệt (`Auto-approval`)** | Phiếu `Local Referral` chỉ lưu nội bộ (`referred` → `owner_responded` → `closed`), không gửi tin nhắn hay ghi dữ liệu sang CRM. |
| **`SCP-O07`** | **7. Tư vấn pháp lý/thuế, cấp quyền tiết lộ dữ liệu, phán quyết bảo hành hoặc hướng dẫn sửa chữa thiết bị (`ANS 07`)** | Bắt buộc từ chối (`REFUSED_OUT_OF_SCOPE` / `HOLD_ANS07`) và chỉ dẫn tuyến chuyển chuyên trách. |
| **`SCP-O08`** | **8. Tự động huấn luyện (`Auto-training`) hoặc tự động sửa quy tắc từ phản hồi người dùng (`KNW 06`)** | Mọi góp ý chỉ vào hàng đợi `feedback_candidate` chờ Steward & Policy Owner duyệt và phát hành bản mới. |
| **`SCP-O09`** | **9. Truyền phát (`Streaming`) nội dung trước khi hoàn tất kiểm tra nguồn và quyền cuối cùng** | Khóa cứng `ENABLE_ANSWER_STREAMING = False` (`INV-03`); chỉ trả gói hoàn chỉnh sau bước `Final Pre-Display Check`. |
| **`SCP-O10`** | **10. Hỗ trợ liên tục 24/7 ngoài giờ làm việc thỏa thuận** | Khung giờ dịch vụ tiêu chuẩn: `08:00–17:00` giờ Việt Nam (`Asia/Ho_Chi_Minh`) các ngày làm việc (`OPS 06`). |

---

## 3. Xác nhận Nghiệm thu & Mở khóa Dây chuyền Gate G0 (`Sign-off`)

- **Chủ trì xác lập phạm vi (`[S1] Named Lead` — PM / BA Lead):** Hoàng Tiến (`Tiến Hoàng`) — *Đã hoàn tất 100% Acceptance Criteria của `CKPA-8` / `CKPA-9` (CRM-G0-ST02 / CRM-G0-SUB04), đồng bộ tuyệt đối với `SRS Mục 2`, `CKPA-2`, `CKPA-3`, `CKPA-4`, `CKPA-6` và `CKPA-30 (CRM-G0-SUB20)`.*
- **Đại diện Quản trị Tri thức (`[P3] Knowledge Steward` — BA & Policy/Knowledge Steward):** Trần Chí Kha — *Xác nhận đồng bộ danh mục nguồn, 30 passages + 10 critical fields mẫu G0.*
- **Đại diện Chủ sở hữu Chính sách (`Policy Owners` — `POL-001`, `POL-002`, `POL-003`) & Sponsor:** *Xác nhận phê duyệt phạm vi cơ sở Gate G0 (`DEL 01`).*
