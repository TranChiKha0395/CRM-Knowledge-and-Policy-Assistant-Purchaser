# BỘ HỒ SƠ CHÍNH THỨC NGHIỆM THU CỔNG GATE G1 (CONTROLLED OFFLINE PILOT & BENCHMARKS), QUYẾT ĐỊNH CẤP PHÉP MỞ CỔNG G2 VÀ LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25%)

> **Dự án:** Trợ lý Tri thức và Chính sách CRM (CRM Knowledge & Policy Assistant — SCRM / CKPA)  
> **Chủ đầu tư / Bên mua (Purchaser):** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật  
> **Cấp thẩm quyền phê duyệt:** [P1] Vắn Mỹ Vân – Purchaser Sponsor / Product Owner  
> **Mã Story Jira cha:** `CKPA-81` (Mã gốc Excel: `CRM-G1-ST10` — *[G1][Mục9] Nghiệm thu G1 (25%) & Sprint 5 Retro*) | **Epic:** `CKPA-44`  
> **Các Sub-tasks trực thuộc đã tích hợp và hoàn tất:**  
> - `CKPA-82` (`CRM-G1-SUB28`): Rà soát lại 100% source_uri & bảng/chú thích DAT 08 (`[P3]` Trần Chí Kha hoàn thành, PR #52 & PR #55 đã merge)  
> - `CKPA-83` (`CRM-G1-SUB29`): Xác nhận chuyên môn Policy Reviewer #1 về Ngày/Trường/Hold (`[P2]` Trương Đình Hữu Tài hoàn thành, PR #54 đã merge)  
> - `CKPA-84` (`CRM-G1-SUB30`): Họp Hội đồng Ký G1 (25%) & Biên bản Sprint 5 Retro (`[P1]` Vắn Mỹ Vân chủ trì)  
> **Trạng thái Cổng G1:** **NGHIỆM THU CHÍNH THỨC (APPROVED & SIGNED-OFF)**  
> **Thời điểm ban hành:** Ngày 24/11/2026 (Giờ Việt Nam — UTC+7)

---

## MỤC LỤC VĂN KIỆN NGHIỆM THU

- **PHẦN I:** TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS (CKPA-82 & CKPA-83)
- **PHẦN II:** BẢNG ĐỐI SOÁT TOÀN DIỆN 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)
- **PHẦN III:** QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: PHÊ DUYỆT CỔNG G1 VÀ CẤP PHÉP MỞ CỔNG G2 (LIVE PILOT)
- **PHẦN IV:** LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25% GIÁ TRỊ HỢP ĐỒNG BASE SCOPE)
- **PHẦN V:** BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT 10 VAI TRÒ HỘI ĐỒNG

---

# PHẦN I: TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS

Hội đồng Nghiệm thu Cổng G1 do **`[P1]` Vắn Mỹ Vân** chủ trì ghi nhận và tiếp nhận toàn diện kết quả thực hiện độc lập từ các Sub-tasks kỹ thuật và chuyên môn:

### 1.1 Tiếp nhận Kết quả Rà soát Nguồn Tri thức từ `CKPA-82` (`[P3]` Trần Chí Kha)
Căn cứ Biên bản kiểm lại `data/g1/reports/CKPA-82_Bien_Ban_Kiem_Lai_100pct_Source_URI_DAT08_Va_Ky_G1_AC01.md` và nhật ký `CKPA-82_source_uri_dat08_reverify.log` (đã đối soát thực tế qua PR #52 và PR #55 trên nhánh `develop`):
- **Trần quy mô dữ liệu Base Scope G1:**
  - Tài liệu nguồn gốc: Đạt **11 / 30** tài liệu (phủ đủ 3 họ chính sách `POL-001`, `POL-002`, `POL-003` và 5 lớp thẩm quyền `DAT 03`: Policy, SOP, Customer Contract, Staff Note, Manufacturer Terms).
  - Đoạn văn trích xuất (`Passages`): Đạt **96 / 300** đoạn (độ dài tối đa 591 / 6.000 ký tự Unicode, đúng chuẩn 21 cột UTF-8).
  - Trường trọng yếu (`Critical Fields`): Đạt **40 / 50** trường (đúng chuẩn 23 cột UTF-8).
- **Kiểm lại 100% `source_uri` & mã băm mật mã SHA-256 (Mục 9 RFP):**
  - Toàn bộ **136 / 136** bản ghi Full Corpus Manifest (96 đoạn + 40 trường) và **56 / 56** bản ghi Family 1 đều trỏ tới tệp tồn tại thực tế trên đĩa, mở xem trực tiếp thành công, khớp 100% mã băm SHA-256, xác nhận **0 liên kết hỏng (0 broken links)** và **0 lệch mã băm**.
- **Kiểm soát cờ bảng biểu & chú thích thiết yếu (`DAT 08`):**
  - Cân bằng dữ liệu chính xác tuyệt đối: **96 Passages = 93 Accepted + 3 Quarantined**.
  - Cách ly đúng 3 trường hợp cố ý thiếu bảng biểu/chú thích để kiểm thử: `PAS-040` (Phụ lục B1 Bảng chiết khấu Đại lý Cấp 1), `PAS-066` (Phụ lục B2 Bảng phân quyền xuất dữ liệu đối tác), `PAS-082` (Phụ lục B3 Danh mục linh kiện hao mòn loại trừ). Toàn bộ 40/40 trường trọng yếu đạt trạng thái Accepted.
- **Tuân thủ phân quyền và bảo vệ quyền riêng tư:**
  - 100% tệp dữ liệu đạt chuẩn **0% PII thật** (được tái kiểm tra và xác nhận qua nhật ký `security/g1/g1_pii_audit_CKPA-47.log`).

### 1.2 Tiếp nhận Thẩm định Chuyên môn Chính sách từ `CKPA-83` (`[P2]` Trương Đình Hữu Tài)
Căn cứ Biên bản chuyên môn `policy/g1/CKPA-83_Xac_Nhan_Policy_Reviewer1_P2_Corpus_Ngay_Truong_Hold.md` (PR #54):
- **Trụ cột Ngày hiệu lực chi phối (`OPS 03`) & Vòng đời tri thức (`KNW 03`):**
  - Toàn bộ các mốc thời gian được chuẩn hóa theo múi giờ Việt Nam (`Asia/Ho_Chi_Minh`, `UTC+7`).
  - Mốc chuyển giao ranh giới phiên bản: `2026-11-06 09:00:00 UTC+7`. Trước thời điểm này áp dụng phiên bản lịch sử v0.9 (`superseded` kèm nhãn bắt buộc *"Hướng dẫn lịch sử"*). Từ thời điểm này trở đi áp dụng phiên bản hiện hành `VER-001` (`effective`).
  - Cấm tuyệt đối áp dụng phiên bản tương lai `VER-002` (`scheduled`, hiệu lực từ `2027-01-01`) cho các giao dịch năm 2026.
  - Chặn 100% ở tầng Pre-Retrieval đối với 4 trạng thái chưa hoặc ngừng hiệu lực (`withdrawn`, `draft`, `owner_reviewed`, `approved`).
- **Trụ cột 6 Chiều ngữ cảnh (`DAT 04`) & 40 Trường trọng yếu (`OPS 04`):**
  - 100% (136/136 bản ghi) khai báo đầy đủ 6 chiều: `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`.
  - Chuẩn hóa các ngưỡng số học: Chiết khấu từ 5% trở xuống (CVKD duyệt trong 2h), trên 5% đến 15% (TPKD duyệt trong 4h), trên 15% hoặc đơn từ 1 tỷ VND (GĐKD duyệt trong 48h); Hợp đồng lũy kế dưới 500 triệu VND (CRM Staff, 4h) vs từ 500 triệu VND trở lên (CRM Manager, 4h); Công suất động cơ thường từ 37.0 kW trở xuống (Tuyến 1 Kỹ thuật nội bộ) vs trên 37.0 kW (Tuyến 2 Hãng), riêng động cơ phòng nổ Ex-d bắt buộc Tuyến 2.
- **Trụ cột Cơ chế HOLD & Ranh giới Fail-Closed (`DAT 05`, `DAT 08`, `ANS 05/06`):**
  - Mã hóa chuẩn 4 kịch bản HOLD: Quarantine Hold (thiếu bảng biểu), Conflict Hold (xung đột Hợp đồng khung/OEM cấm tự suy diễn thứ bậc ưu tiên, bắt buộc trích dẫn song song), Evidence Hold (mờ chứng từ, tạo phiếu chuyển tiếp xử lý trong 8 giờ làm việc), và Từ chối tiền lệ ghi chú CRM (`staff_note` không ghi đè chính sách).

---

# PHẦN II: BẢNG ĐỐI SOÁT TOÀN DIỆN 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)

Hội đồng Nghiệm thu Cổng G1 đã tiến hành kiểm tra độc lập và đối soát chi tiết từng tiêu chí chấp nhận:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát | Kết luận |
| :---: | :--- | :--- | :--- | :---: |
| **`G1-AC01`** | **Toàn vẹn Dữ liệu Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..011); dưới 300 đoạn văn; dưới 50 trường trọng yếu; 100% bản ghi đủ 6 chiều DAT 04; 0 link gãy source_uri; 136 SHA-256 khớp 100%. | Biên bản CKPA-82 của [P3], PR #52 & PR #55; Xác nhận của [P2] tại CKPA-83; File Policy_Corpus_G1_Full.csv. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Bộ Dữ liệu Kiểm thử Độc lập 200 Tasks & 80 Challenges** | Phân vùng chuẩn 60 Dev / 40 Val / 100 Sealed chống rò rỉ; Niêm phong 100 Sealed + 80 Challenges trong sealed-eval-repo; 2 Policy Reviewers đồng duyệt. | Báo cáo CKPA-65, CKPA-66; Biên bản CKPA-83 của [P2]; Kho niêm phong độc lập của [S4] Quý Hải. | **ĐẠT (PASS)** |
| **`G1-AC03`** | **Bảo vệ Quyền Riêng tư & Tuân thủ An toàn Bảo mật** | Đạt 0% PII thật (SEC 02/06); Kiểm thử Pre-Retrieval RBAC chặn 100% quyền trái phép (SEC 01); Không rò rỉ snippet/link khi bị từ chối; Ẩn danh nhật ký SEC 08. | Báo cáo Kiểm toán Bảo mật CKPA-70 của [P5]; Log g1_rbac_failclosed_audit_CKPA-70.log; Chứng nhận CKPA-47. | **ĐẠT (PASS)** |
| **`G1-AC04`** | **Kiểm soát Vòng đời, Ngày chi phối & Cơ chế Fail-Closed** | Xử lý chuẩn 7 trạng thái KNW 03; Phân định ranh giới ngày 2026-11-06 09:00:00 UTC+7 (OPS 03); Ngưỡng số học chuẩn (OPS 04); Thu hồi khẩn cấp tức thì Fail-Closed dưới 5 phút (SEC 05). | Biên bản CKPA-83; Test runner g1_rbac_failclosed_audit_runner.py (TC-REV-03 PASS); Biên bản CKPA-62. | **ĐẠT (PASS)** |
| **`G1-AC05`** | **Hiệu năng Pipeline Benchmark Offline & Bàn giao DEL 02/03** | Đóng băng mã nguồn tag v0.2.0-g1-offline; Pipeline RAG đạt các chỉ số kiểm chuẩn trên tập Dev/Val; Bàn giao trọn bộ Kiến trúc DEL 02 và Báo cáo kiểm định DEL 03. | Git tag v0.2.0-g1-offline; Gói hồ sơ kỹ thuật DEL 02 / DEL 03 từ nhóm kỹ sư S2/S3/S5; Xác nhận của [P2]. | **ĐẠT (PASS)** |
| **`G1-AC06`** | **Tuân thủ Tuyệt đối Ranh giới Tách vai (SoD & Chinese Wall)** | QA Lead [S4] độc lập 100% với code/prompt S2/S3; 100 Sealed không lộ cho dev; 5 NSD đại diện thuộc 100% Bên Mua ngoài S1-S5; Nguyên tắc Assignee khác Reporter. | Rà soát phân quyền kho sealed-eval-repo; Ma trận 5 NSD thực tế tại CKPA-5 / CKPA-31; 100% task Jira tuân thủ SoD. | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Quản trị Scrum, Giờ công W1-3 & Chữ ký Đồng thuận** | Toàn bộ các Sub-tasks con của Sprint 3, 4, 5 hoàn tất; Nhịp làm việc bền vững dưới 40 giờ/tuần/vai trò; Đủ chữ ký của 10 vai trò trên biên bản tổng kết. | Báo cáo đối soát giờ công W1-3 của Scrum Master [S1]; Biên bản Sprint 5 Retrospective (Mục V). | **ĐẠT (PASS)** |

---

# PHẦN III: QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: PHÊ DUYỆT CỔNG G1 VÀ CẤP PHÉP MỞ CỔNG G2 (LIVE PILOT)

Căn cứ kết quả kiểm tra **ĐẠT TOÀN DIỆN 7/7 Tiêu chí Nghiệm thu Cổng G1** và hệ thống đạt **0 lỗi Critical Control**:

1. **Phê duyệt Nghiệm thu Cổng Gate G1 (Controlled Offline Pilot & Benchmarks):**
   - Chủ đầu tư công nhận Nhà cung cấp đã hoàn thành đầy đủ, trung thực và đúng hạn các kết quả bàn giao của Cổng G1 theo đúng cam kết trong Hợp đồng và Hồ sơ Yêu cầu (RFP).
   - Chính thức đóng User Story cha **`CKPA-81`** ở trạng thái **`Done`** trên hệ thống Jira.

2. **Quyết định Cấp phép Mở Cổng Gate G2 (Live Pilot Authorization):**
   - Cấp phép cho phép dự án chuyển tiếp sang Giai đoạn Thử nghiệm Nội bộ Giới hạn (Sprint 6 — Gate G2 Live Pilot) theo đúng kế hoạch triển khai 10 tuần.
   - **Ràng buộc kiểm soát bắt buộc tại Cổng G2:**
     - Duy trì cờ cấu hình an toàn: **`OPTION_O1_ENABLED = False` (Base Scope thuần túy)**. Tuyệt đối không kết nối dữ liệu khách hàng CRM sống khi chưa có Tờ trình pháp lý được Legal Owner phê duyệt riêng.
     - Hạ tầng Staging và môi trường kiểm thử thực tế phải được Security Owner `[P5]` thẩm định độc lập các cổng mạng và chứng chỉ bảo mật trước khi kích hoạt.
     - Giao `[P4]` Ngô Thị Trà My điều phối 5 Người dùng đại diện thực hiện nghiêm ngặt Giao thức đo đạc năng suất 20 ngày (`Observed Effort Protocol`) làm đối trọng kiểm chứng với Baseline Effort đã chốt tại G0.

---

# PHẦN IV: LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25% GIÁ TRỊ HỢP ĐỒNG BASE SCOPE)

Căn cứ Điều 12 Hợp đồng Dịch vụ Phần mềm số 01/2026/HDDV-CKPA và Biên bản Nghiệm thu Đạt Cổng G1:

1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
2. **Tỷ lệ giải ngân:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope.
3. **Giá trị thanh toán thực tế:**
   - Được xác định chính xác theo công thức: Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)
   - Số tiền cụ thể căn cứ trên Bảng giá Thương mại DEL 05 chính thức đã được thống nhất tại task `CKPA-39`.
4. **Điều kiện và Thời hạn thanh toán:**
   - Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật thực hiện chuyển khoản vào tài khoản ngân hàng của Bên Cung cấp trong thời hạn 10 (mười) ngày làm việc kể từ ngày nhận đủ:
     - 01 bản gốc Biên bản Nghiệm thu Cổng G1 này có đầy đủ chữ ký xác nhận của đại diện hai bên.
     - 01 bản Hóa đơn Giá trị gia tăng (VAT) hợp lệ tương ứng với giá trị giải ngân Mốc 2 do Bên Cung cấp phát hành.

---

# PHẦN V: BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT 10 VAI TRÒ HỘI ĐỒNG

### 5.1 Đánh giá và Rút kinh nghiệm Sprint 5 Retrospective
- **Những điểm thực hiện xuất sắc (What went well):**
  - Sự phối hợp nhịp nhàng giữa `[P3]` Trần Chí Kha và `[P2]` Trương Đình Hữu Tài giúp quy trình kiểm tra chéo dữ liệu nguồn và thẩm định chính sách diễn ra chặt chẽ, phát hiện sớm và cách ly đúng 3 tài liệu thiếu bảng biểu vào Quarantine theo chuẩn `DAT 08`.
  - Hàng rào độc lập Chinese Wall được duy trì tuyệt đối: Kho niêm phong 100 câu hỏi Sealed trong `sealed-eval-repo` được cô lập hoàn toàn khỏi đội ngũ kỹ sư phát triển `S2/S3/S5`.
  - Toàn bộ kho lưu trữ Purchaser đã được dọn sạch các tag citation AI thừa, chuẩn hóa 100% UTF-8 và nâng cấp CI Guard chạy tự động 21/21 unit tests PASS.
- **Những điểm cần tối ưu cho Cổng G2 (What to improve):**
  - Tăng cường tốc độ đồng bộ và cấp phát endpoint thật (`CKPA_BASE_URL`) để đội kiểm toán bảo mật `[P5]` triển khai kiểm thử Runtime API trực tiếp mà không cần chờ đợi.
  - Phổ biến sâu hơn cho 5 người dùng đại diện về quy trình ghi nhận nhật ký thao tác trong 20 ngày thử nghiệm Pilot.

---

### 5.2 BẢNG KÝ DUYỆT ĐỒNG THUẬN CỦA 10 THÀNH VIÊN HỘI ĐỒNG NGHIỆM THU

| Vai trò RFP | Họ và tên | Chức danh / Đại diện | Chữ ký xác nhận |
| :--- | :--- | :--- | :---: |
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ tịch Hội đồng Thẩm định & Nghiệm thu | *(Đã ký duyệt chính thức)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | *(Đã ký duyệt chuyên môn)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | *(Đã ký duyệt dữ liệu)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ SongNhat | *(Đã ký duyệt nghiệp vụ)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin & Quyền riêng tư | *(Đã ký duyệt bảo mật)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | *(Đã ký xác nhận bàn giao)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | *(Đã ký xác nhận kỹ thuật)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | *(Đã ký xác nhận kỹ thuật)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Đảm bảo Chất lượng Độc lập | *(Đã ký kiểm định độc lập)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hệ thống | *(Đã ký xác nhận vận hành)* |

---
*Biên bản này được lập thành 04 (bốn) bản gốc bằng tiếng Việt có giá trị pháp lý như nhau. Bên Mua giữ 02 bản, Bên Cung cấp giữ 02 bản để làm căn cứ giải ngân Mốc 2 và triển khai Cổng Gate G2.*
