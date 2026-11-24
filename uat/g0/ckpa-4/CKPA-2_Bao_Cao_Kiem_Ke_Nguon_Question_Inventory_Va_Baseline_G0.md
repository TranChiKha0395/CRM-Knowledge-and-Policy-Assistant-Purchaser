# BÁO CÁO KIỂM KÊ NGUỒN TRI THỨC, DANH MỤC CÂU HỎI ĐẠI DIỆN 4 TUẦN (QUESTION INVENTORY) & ĐO LƯỜNG ĐƯỜNG CƠ SỞ (BASELINE EFFORT) — GATE G0 (`DEL 01`)

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`CKPA`)
- **Mã công việc Jira:** `CKPA-4` — *CRM-G0-ST01: [G0][WP01] Hoàn tất Charter, 4w Log & Baseline* kèm Sub-tasks `CKPA-6` (CRM-G0-SUB02) & `CKPA-7` (CRM-G0-SUB03) (Thuộc Epic `CKPA-3`: *CRM-G0-EP01*)
- **Tham chiếu SRS & RFP:** `SRS-FR-01.1`, `SRS-FR-01.2`, `SRS Mục 1.2 & 2.1` | `WP 01`, `DEL 01`
- **Chủ trì thực hiện (`[P3] Knowledge Steward`):** Trần Chí Kha (*BA & Policy/Knowledge Steward *)
- **Phối hợp (`[S1] Named Lead`):** Hoàng Tiến (*PM / BA Lead *)
- **Nhánh Git gợi ý:** `uat/CKPA-4-inventory-sources-and-4-week-baseline`
- **Ngày hoàn tất:** `16/11/2026` (Múi giờ `Asia/Ho_Chi_Minh`)

---

## 1. Kiểm kê Quy trình, Tài liệu Nguồn Được Phép & Phân tích Khoảng trống (`Source Registry & Gap Analysis`)

Thực hiện yêu cầu của `WP 01` và `SRS-FR-01.1`, `[P3] Trần Chí Kha` (Knowledge Steward) chủ trì cùng `[S1] Hoàng Tiến` (Named Lead) đã kiểm kê toàn bộ nguồn tài liệu nghiệp vụ liên quan đến `03` nhóm chính sách khởi đầu của SongNhat, xác nhận chủ sở hữu chính sách (`Policy Owner`) cùng người thay thế (`Backup Owner`), phân lớp theo `5` tầng thẩm quyền (`DAT 03`) và chỉ rõ khoảng trống cần xử lý trước `Gate G1` (chi tiết trong tệp đính kèm `data/g0/CKPA-2_01_Source_Registry_And_Gap_Analysis.csv`):

| Mã Nguồn (`source_id`) | Mã Tài liệu & Phiên bản | Nhóm Chính sách (`Policy_ID`) | Lớp Thẩm quyền (`DAT 03`) | Chủ sở hữu Chính (`Policy Owner`) | Người Thay thế (`Backup Owner`) | Quy mô Đã duyệt ở `G0` | Quy mô Mục tiêu ở `G1` | Khoảng trống Hiện hữu (`Gaps`) & Biện pháp Xử lý |
| :---: | :---: | :--- | :---: | :--- | :--- | :---: | :---: | :--- |
| `SRC-001` | `DOC-001` (`VER-001`) | **1. Báo giá & Phê duyệt thương mại** (`POL-001`) | `policy` | Commercial Policy Owner (`Sales Director`) | Deputy Sales Director | `10` đoạn / `04` trường (`CF-001..004`) | `100` đoạn / `18` trường | Bảng chiết khấu nằm rải rác trong Word; cần tạo thêm bản `VER-000` (`superseded`) & `VER-002` (`scheduled`) để kiểm thử Worked Case 3 & 4 ở G1. |
| `SRC-002` | `DOC-002` (`VER-001`) | **2. Xử lý thông tin khách hàng CRM** (`POL-002`) | `policy` | CRM Data Governance Owner (`CRM Manager`) | Senior CRM Lead | `10` đoạn / `04` trường (`CF-005..008`) | `100` đoạn / `16` trường | Nhân viên hay nhầm giữa đổi Email/SĐT (`2h`) và sửa pháp lý DN (`4h`, ngưỡng `500M VND`); đã tách rõ 4 dòng `CF-005..008`. |
| `SRC-003` | `DOC-003` (`VER-001`) | **3. Định tuyến dịch vụ / bảo hành** (`POL-003`) | `policy` | Warranty Policy Owner (`Service Director`) | Internal Tech Lead | `10` đoạn / `02` trường (`CF-009..010`) | `100` đoạn / `16` trường | Ngưỡng công suất `<= 37 kW` (Tuyến 1) và `> 37 kW` (Tuyến 2) đã được chuẩn hóa sang CSV kèm ranh giới cấm phán quyết bảo hành (`ANS 07`). |
| `SRC-004` | `DOC-004` (`VER-001`) | Phụ trợ Nhóm 1 (`POL-001`) | `SOP` | Commercial Policy Owner | Deputy Sales Director | `0` (Mở rộng ở G1) | Nằm trong trần `300` đoạn | Đang ở trạng thái `owner_reviewed`; sẽ nạp vào Đợt 1 `Gate G1` (`CKPA-16`) trước `26/11/2026`. |
| `SRC-005` | `DOC-005` (`VER-001`) | Phụ trợ Nhóm 3 (`POL-003`) | `manufacturer_terms` | Warranty Policy Owner | Vendor Chief Engineer | `0` (Mở rộng ở G1) | Nằm trong trần `300` đoạn | Chứa thuật ngữ kỹ thuật tiếng Anh (`Inverter`, `Gearbox`, `Nameplate`); sẽ đồng bộ từ điển `VN 01` ở G1. |
| `SRC-006` | `DOC-006` (`VER-001`) | Kiểm thử xung đột (`POL-001..003`) | `customer_contract` | Commercial Policy Owner | Legal Owner | `0` (Mở rộng ở G1) | Nằm trong trần `300` đoạn | Dùng để kiểm thử `Conflict Hold (DAT 05 - Worked Case 5)`: cấm tự suy diễn ưu tiên hợp đồng vs chính sách. |
| `SRC-007` | `DOC-007` (`VER-001`) | Kiểm thử tiền lệ (`POL-001..002`) | `staff_note` | CRM Data Governance Owner | Commercial Policy Owner | `0` (Mở rộng ở G1) | Nằm trong trần `300` đoạn | Ghi chú CRM cũ/tiền lệ VIP chỉ là lịch sử có ghi nguồn, cấm tạo quy tắc chung (`Worked Case 6`). |

> **Kết luận kiểm kê nguồn tại G0:** Cả `03` nhóm chính sách khởi đầu đều đã có đầy đủ **Policy Owner chính thức + Người thay thế** và nguồn văn bản hợp lệ (`VN 04`); không có nhóm nào bị loại khỏi Base Scope.

---

## 2. Danh mục Câu hỏi Thực tế Đại diện 4 Tuần Lịch sử (`Question Inventory — SRS-FR-01.1`)

### 2.1 Nguyên tắc thu thập & Tính đại diện 4 tuần lịch sử
- **Tuân thủ nguyên tắc trung thực của RFP (`Mục 8 & Mục 10`):** RFP quy định rõ *"2 tuần Discovery không tự động tạo ra 4 tuần lịch sử câu hỏi"*. Do đó, để lập bộ `Question Inventory` phản ánh đúng **tối thiểu 4 tuần lịch sử đại diện**, nhóm đã thực hiện kết hợp `02` nguồn:
  1. **Trích xuất nhật ký câu hỏi lịch sử 4 tuần (`12/10/2026 – 08/11/2026`, tương đương `20` ngày làm việc):** Tổng hợp từ phiếu hỏi nội bộ, lịch sử ticket hỗ trợ quy trình của Sales, CRM và CSKH tại SongNhat với tổng lưu lượng ghi nhận **`N = 520` lượt hỏi quy trình lặp lại** (đã khử 100% PII khách hàng theo `SEC 02`).
  2. **Kế hoạch quan sát bổ sung (`>= 20` ngày làm việc tại `Gate G3`):** Để đối chứng công bằng với đường cơ sở, giai đoạn Pilot có giám sát tại `Gate G3` (`CKPA-38`) được khóa cứng tối thiểu **`20` ngày làm việc thực tế** (`25/12/2026 – 22/01/2027`, hoặc kích hoạt sớm từ `24/12/2026` để có `21` ngày làm việc dự phòng) với `>= 5` nhân sự phi-lập-trình. Nếu lưu lượng câu hỏi trong tuần lễ thấp, thời gian quan sát sẽ được kéo dài tương ứng cho đến khi đủ mẫu đại diện.

### 2.2 Phân bổ 16 Nhóm Câu hỏi (`VG-01..VG-16`) & Tuyển chọn 200 Real Tasks (`60 Dev / 40 Val / 100 Sealed`)
Từ `N = 520` lượt hỏi trong 4 tuần lịch sử, `[P3] Knowledge Steward` và `[P5] Privacy/Security Owner` đã chuẩn hóa thành **`16` nhóm biến thể câu hỏi lặp lại (`VG-01` → `VG-16`)** và rút mẫu phân tầng thành **`n = 200` tác vụ câu hỏi thực tế được phép** (khớp 100% với phân vùng `60 Dev` công khai tại `CKPA-30 (CRM-G0-SUB20)`):

| Nhóm Chính sách (`Policy_ID`) | Các Nhóm Biến thể (`Variant Groups`) | Lượt hỏi trong 4 tuần (`N = 520`) | Tỷ trọng (`%`) | Số Tác vụ Thực tế Tuyển chọn (`n = 200`) | Phân bổ `60 Dev / 40 Val / 100 Sealed` |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **1. Báo giá & Phê duyệt thương mại (`POL-001`)** | `VG-01` → `VG-06` (Chiết khấu `<=5%`, `5–15%`, `>15%/1 tỷ`, trường bắt buộc/15 ngày, VIP note cũ, xung đột HĐ khung) | **240** lượt | `46,2%` | **82** tasks | `24 Dev` / `17 Val` / `41 Sealed` |
| **2. Xử lý thông tin khách hàng CRM (`POL-002`)** | `VG-07` → `VG-11` (Đổi Email/SĐT `2h`, sửa pháp lý `<500M`, duyệt `>=500M`, khẩn ngoài giờ `1h`, VIP thiếu ĐKKD/lệch HĐ) | **160** lượt | `30,8%` | **66** tasks | `20 Dev` / `13 Val` / `33 Sealed` |
| **3. Định tuyến dịch vụ / bảo hành (`POL-003`)** | `VG-12` → `VG-16` (3 chứng từ & kiểm tra `2h`, Tuyến 1 `<=37 kW`, Tuyến 2 `>37 kW/bo mạch`, từ chối phán quyết `ANS 07`, mờ/rách Serial `HOLD`) | **120** lượt | `23,1%` | **52** tasks | `16 Dev` / `10 Val` / `26 Sealed` |
| **TỔNG TOÀN DỰ ÁN (`BASE SCOPE`)** | **Đủ 16 Variant Groups & 9 Worked Cases** | **520 lượt / 4 tuần** | **100,0%** | **200 Real Tasks** | **`60 Dev` / `40 Val` / `100 Sealed`** |

---

## 3. Báo cáo Đo lường Đường cơ sở Công sức Nhân viên (`Baseline Effort — SRS-FR-01.2`)

### 3.1 Phương pháp đo & 05 Thành phần Công sức
Đường cơ sở (`Manual Baseline`) được đo trên mẫu số **`n = 200` tác vụ thực tế** khi nhân viên (`Sales`, `CRM`, `CSKH`) tra cứu thủ công trên thư viện văn bản hiện tại (chưa có Trợ lý CKPA). Mỗi tác vụ được ghi nhận đầy đủ `05` thành phần thời gian (đơn vị: **phút / tác vụ**):
1. **Chuẩn bị (`prep_min`):** Xác định nhóm chính sách, ngày giao dịch chi phối và phạm vi áp dụng.
2. **Tra cứu (`search_min`):** Mở file quy trình/phụ lục và tìm điều khoản, bảng ngưỡng liên quan.
3. **Kiểm tra (`verify_min`):** Đối chiếu phiên bản hiện hành, thẩm quyền duyệt, chứng từ bắt buộc và ngoại lệ.
4. **Làm lại (`rework_min`):** Thời gian sửa lại khi mở nhầm phiên bản cũ, áp dụng sai ngưỡng hoặc bị trả phiếu do thiếu chứng từ.
5. **Dự phòng (`fallback_min`):** Thời gian nhắn tin/gọi hỏi lại Policy Owner hoặc Trưởng bộ phận khi gặp điều khoản mâu thuẫn/không chắc chắn.

### 3.2 Kết quả Thống kê Baseline (Mẫu số, Trung vị, Khoảng Tứ phân vị IQR & Độ bất định 95% CI)
*(Chi tiết phân bố 16 nhóm câu hỏi lưu tại `uat/g0/ckpa-6/CKPA-2_02_Question_Inventory_4Week_Representative.csv`. Bảng dưới ghi nhận thời gian tra cứu trên kho văn bản thô chưa chuẩn hóa; sau khi làm sạch thư viện tìm kiếm theo kiểm chứng độc lập `CKPA-7` & Quyết định Cổng G0 `P1_CKPA40_42`, mốc **Cleaned Searchable Baseline** chính thức khóa cứng tại **`Mean = 15,53 phút`, `Median = 14,30 phút`, `95% CI: [14,82' ; 16,24']`**)*

| Phân khúc Chính sách | Mẫu số (`n` / `N` 4 tuần) | Chuẩn bị (TV) | Tra cứu (TV) | Kiểm tra (TV) | Làm lại (TV) | Dự phòng (TV) | **Tổng Công sức Trung vị (`Median`)** | **Khoảng Tứ phân vị (`IQR`)** | **Trung bình (`Mean`) & Độ bất định (`95% CI`)** | Tỷ lệ phải làm lại / hỏi lại (`Rework Rate`) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **1. Báo giá & Thương mại (`POL-001`)** | `n = 82` (`N = 240`) | `2,5'` | `5,0'` | `4,5'` | `3,5'` | `3,0'` | **`18,5 phút`** | `6,2 phút` (`15,4' – 21,6'`) | `19,2 phút` (`95% CI: [17,8' ; 20,6']`) | `26,8%` |
| **2. Thông tin Khách hàng (`POL-002`)** | `n = 66` (`N = 160`) | `2,0'` | `4,5'` | `5,0'` | `3,5'` | `3,0'` | **`18,0 phút`** | `5,8 phút` (`15,1' – 20,9'`) | `18,7 phút` (`95% CI: [17,2' ; 20,2']`) | `24,2%` |
| **3. Dịch vụ & Bảo hành (`POL-003`)** | `n = 52` (`N = 120`) | `2,5'` | `4,5'` | `4,0'` | `3,0'` | `3,5'` | **`17,5 phút`** | `6,5 phút` (`14,5' – 21,0'`) | `18,3 phút` (`95% CI: [16,6' ; 20,0']`) | `25,0%` |
| **TỔNG HỢP TOÀN DỰ ÁN (`G0 BASELINE`)** | **`n = 200` (`N = 520`)** | **`2,3'`** | **`4,8'`** | **`4,5'`** | **`3,4'`** | **`3,1'`** | **`18,1 phút`** | **`6,1 phút` (`15,0' – 21,1'`)** | **`18,8 phút` (`95% CI: [17,9' ; 19,7']`)** | **`25,5%`** |

### 3.3 Ghi nhận Độ phủ, Độ bất định & Tuyên bố Không Khẳng định ROI Sớm (`RFP Mục 1.2`)
1. **Độ phủ & Độ bất định (`Coverage & Uncertainty`):**
   - Mẫu cơ sở `n = 200` tác vụ đại diện cho `38,5%` tổng lưu lượng `N = 520` câu hỏi trong 4 tuần lịch sử của `20` nhân sự mục tiêu (`Sales`, `CRM`, `CSKH`).
   - Độ phân tán (`IQR = 6,1 phút`) tập trung chủ yếu ở các ca biên: đơn hàng `>= 1 tỷ VND`, xung đột Hợp đồng khung (`Worked Case 5`), yêu cầu ngoài giờ hành chính (`CF-008`) và thiết bị mất tem Serial (`Worked Case 7`), nơi thời gian chờ phản hồi dự phòng (`fallback_min`) dao động từ `0` đến `12` phút.
   - Tại `Gate G3`, hệ thống có hỗ trợ AI (`Assisted Use`) sẽ được đo đối chứng trực tiếp với **Thư viện hiện tại đã làm sạch có thể tìm kiếm (`Cleaned Searchable Baseline`)** trên cùng bộ tiêu chí, mục tiêu giảm **`>= 20%` tổng công sức trung bình** so với mốc Cleaned Searchable Baseline đã kiểm chứng tại `CKPA-7` & chốt cứng tại Quyết định Cổng G0 `CKPA-40`/`42` (tức đưa mức trung bình từ **`15,53 phút`** — `Median 14,30 phút` — xuống **`<= 12,42 phút/tác vụ`**, tiết kiệm `>= 3,11 phút/tác vụ` mà vẫn giữ `0` lỗi trọng yếu; đối với kho văn bản thô ban đầu `18,8 phút` tương ứng mức giảm `<= 15,0 phút`).
2. **Tuyên bố Tuân thủ Ranh giới Thương mại (`No Unproven ROI Claim`):**
   - Tuân thủ nghiêm ngặt `RFP Mục 1.2` và `SRS Mục 1.2`, báo cáo đường cơ sở này **CHỈ ghi nhận thời gian thao tác tra cứu, kiểm tra và chuyển tuyến quy trình nội bộ**.
   - **TUYỆT ĐỐI KHÔNG tuyên bố** việc giảm sự cố tuân thủ pháp lý, giảm tỷ lệ khách hàng rời bỏ (`churn`), tăng tỷ lệ chốt đơn hay lợi tức đầu tư (`ROI`) là kết quả đã được chứng minh tại cổng `Gate G0`. Mọi đánh giá hiệu quả kinh tế và hoàn vốn (`Payback <= 24 tháng`) sẽ chỉ được tính toán dựa trên số liệu quan sát thực tế tối thiểu `20` ngày làm việc tại `Gate G3` (`DEL 03` & `DEL 05`).
