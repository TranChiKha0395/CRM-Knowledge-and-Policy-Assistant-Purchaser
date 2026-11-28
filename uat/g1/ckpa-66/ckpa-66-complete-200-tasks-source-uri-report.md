# BÁO CÁO BÀN GIAO & MINH CHỨNG HOÀN THÀNH SUB-TASK CKPA-66
## [G1][Mục8] Hoàn tất 200 Câu hỏi thực & Check source

> **Mã công việc (Jira):** `CKPA-66` | **Mã gốc (Excel G1):** `CRM-G1-SUB16`  
> **Thuộc User Story:** `CKPA-65` / `CRM-G1-ST06` (*[G1][Mục8] Phân vùng 60/40/100 & 80 Challenges*)  
> **Tiêu chí nghiệm thu Cổng G1:** `G1-AC07`  
> **Nhánh Git làm việc:** `uat/ckpa-66-sync-source-uri-lowercase-folder`  
> **Vị trí file chuẩn:** `uat/g1/ckpa-66/ckpa-66-complete-200-tasks-source-uri-report.md`  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead:** `[P4] Ngô Thị Trà My (Staff users)`  
> **Collaborators / RACI:** `[P5] Nguyễn Anh Khoa`, `[P3] Trần Chí Kha`  
> **Reporter / Nghiệm thu (PO):** `[P1] Mỹ Vân (Purchaser sponsor)`  
> **Bên tiếp nhận bàn giao:** `[S4] Quý Hải (Quality Lead)`  
> **Lịch thực hiện:** 2026-11-16 -> 2026-11-26 (Sprint 4–5 - Đồng bộ gói 100 Sealed V2 `CKPA-67`/`CKPA-68`)  
> **Truy vết RFP:** Mục 8 (200 permitted real tasks), SEC 02, SEC 06, Mục 9 (G1), DAT 08.

---

## 1. TỔNG QUAN VÀ MỤC TIÊU SUB-TASK

Theo quy chuẩn phân công công việc Cổng G1 và SCRM Onboarding Guide (§6.4):
- Vai trò **[P4] Ngô Thị Trà My** cùng 4 nhân sự người dùng nghiệp vụ SongNhat (ngoài nhóm Supplier S1–S5) có nhiệm vụ hoàn tất 100 câu hỏi thực tế đợt 2, kết hợp cùng 100 câu đợt 1 (CKPA-55) thành trọn vẹn **200 câu hỏi thực tế được phép (200 permitted real tasks)** đạt chuẩn 0% PII (SEC 02 / SEC 06).
- Đồng thời thực hiện kiểm tra mở xem thực tế tài liệu gốc qua **`source_uri`**, đối soát tính đầy đủ của bảng biểu, sơ đồ và chú thích thiết yếu (DAT 08) theo yêu cầu tái kiểm chứng quyền truy cập tài liệu tham chiếu gốc tại Mục 9 G1 (*re-verified original reference access*).

---

## 2. KẾT QUẢ BÀN GIAO 1: 200 CÂU HỎI THỰC TẾ ĐÃ LÀM SẠCH (0% PII)

### 2.1 Cấu trúc Phân bổ theo 3 Họ Chính sách Chuẩn (Khớp RFP Mục 1 & CKPA-58)
200 câu hỏi thực tế được làm sạch toàn diện và phân bổ cân bằng cho 3 quy trình CRM cốt lõi của SongNhat:

| Mã Họ chính sách | Tên quy trình nghiệp vụ chuẩn RFP | Đợt 1 Mở (`CKPA-55`) | Đợt 2 Sealed V2 (`CKPA-67`) | Tổng số câu hỏi thực tế | Tỷ lệ cơ cấu |
|---|---|:---:|:---:|:---:|:---:|
| **POL-001** *(Họ 1)* | Quy trình Báo giá & Phê duyệt Thương mại | 40 ca | 52 ca | **92 câu** | 46.0% |
| **POL-002** *(Họ 2)* | Quy trình Xử lý Thông tin & Dữ liệu Khách hàng | 30 ca | 24 ca | **54 câu** | 27.0% |
| **POL-003** *(Họ 3)* | Quy trình Tiếp nhận Dịch vụ & Bảo hành Kỹ thuật | 30 ca | 24 ca | **54 câu** | 27.0% |
| **Tổng cộng** | **3 họ chính sách cốt lõi SongNhat** | **100 ca (`VG-01..18`)** | **100 ca (`VG-19..43`)** | **200 ca thực tế** | **100%** |

*(Ghi chú SoD & Phân vùng dữ liệu: Theo đúng phân định trách nhiệm Cổng G1, vai trò `[P4]` Trà My bàn giao 100 câu mở `TASK-001..100` (`VG-01..VG-18`) trên repo Purchaser và bàn giao cách ly gói 100 câu `SEALED` thay thế V2 (`TASK-101..200` / `VG-19..VG-43`) cho `[S4]` Quý Hải đóng băng tại `ckpa-dev-val-eval/sealed-eval-repo @ 33180db` (`CKPA-67`), đã được `[P2]` & `[P3]` đồng ký duyệt nhãn vàng tại `CKPA-68`).*

### 2.2 Rà soát An toàn Bảo mật PII (SEC 02 & SEC 06)
- **Phương pháp rà soát:** Kết hợp công cụ Regex Scan tự động và rà soát thủ công 100% trường Question_VN:
  - Số điện thoại cá nhân thật: **0 phát hiện** (0 SĐT).
  - Số Căn cước công dân / CMND thật: **0 phát hiện** (0 CCCD).
  - Email cá nhân thật: **0 phát hiện** (0 Email).
  - Toàn bộ tên định danh khách hàng đều được ẩn danh hóa hoặc dùng mã mẫu (Đại lý A, Khách hàng B2B X).
- **Trạng thái đồng thuận nhãn vàng:** 100 ca `SEALED` đạt **`P2_P3_CO_SIGNED_APPROVED`** tại `CKPA-68`; 100 ca mở đặt **`PENDING_P2_P3_REVIEW`** (đã rà soát khớp 100% `PAS-xxx` và `CF-xxx`).
- **Đồng bộ mã trường trọng yếu:** Toàn bộ trường `Gold_Critical_Field_IDs` được đồng bộ sang mã chuẩn **`CF-001..CF-040`** của Full Corpus `CKPA-58`:
  - Họ 1: `CF-001` (`<= 5%`, Sales Staff), `CF-002` (`5% < CK <= 15%`, Sales Manager), `CF-003` (`> 15%` hoặc `>= 1 tỷ VND`, Sales Director), `CF-004` (hiệu lực `15 ngày làm việc`), cùng dải mở rộng `CF-011..CF-022`.
  - Họ 2: `CF-005` (liên hệ/email GTGT `<= 2 giờ`, CRM Staff), `CF-006` (pháp lý DN `< 500M`, CRM Staff), `CF-007` (pháp lý KH trọng yếu `>= 500M`, CRM Manager), `CF-008` (pháp lý khẩn ngoài giờ `<= 1 giờ`, CRM Director), cùng dải `CF-023..CF-031`.
  - Họ 3: `CF-009` (Tuyến 1 nội bộ `<= 37 kW`, Internal Tech Lead), `CF-010` (Tuyến 2 Hãng `> 37 kW`, Vendor Chief Engineer), `CF-032` (động cơ phòng nổ `Ex-d` bắt buộc Tuyến 2), cùng dải `CF-033..CF-040`.
- **Tập tin bàn giao:**
  - Định dạng CSV: [200_clean_real_tasks.csv](200_clean_real_tasks.csv)

---

## 3. KẾT QUẢ BÀN GIAO 2: BIÊN BẢN KIỂM TRA MỞ XEM TÀI LIỆU GỐC (SOURCE_URI & DAT 08)

Tuân thủ quy định Mục 9 Cổng G1 (*re-verified original reference access*) và kiểm tra chú thích/bảng thiết yếu (DAT 08), nhóm người dùng đại diện (P4 Trà My cùng 4 nhân viên SongNhat) đã đối soát 100% nguồn tham chiếu tài liệu. 

Sau khi PR #32 (`[CKPA-58]` Curate Full 3-Family G1 Corpus) được merge chính thức vào nhánh `develop`, toàn bộ 11/11 tài liệu gốc (`DOC-001 .. DOC-011`) thuộc 3 họ chính sách và 5 lớp thẩm quyền (DAT 03) đã hiện diện đầy đủ, mở xem trực tiếp thành công và đạt **100% VERIFIED_ACCESSIBLE**:

| Mã Kiểm tra | Tài liệu ID | Văn bản quy trình | Đường dẫn tài liệu thực tế (`File_URI`) | Mẫu điều khoản kiểm tra | Bảng biểu & Phụ lục thiết yếu | Kiểm tra Chú thích (DAT 08) | Kết quả thẩm tra thực tế |
|---|:---:|---|---|---|---|---|:---:|
| **CHK-DOC-01** | DOC-001 | Quy trình Báo giá và Phê duyệt Thương mại SongNhat | `data/g1/sources/DOC-001_POL-CRM-01_Quotation_Commercial_Approval.md` | Điều 1.1-1.4, 2.1-2.5, 3.1-3.2, 4.1-4.3, 5.1 | Bảng 2.1 (`CF-001 <= 5%`, `CF-002 5-15%`, `CF-003 > 15%`), Phụ lục A1-A3, Phụ lục B1 (`PAS-040`) | Thẩm quyền duyệt CVKD, TPKD, GĐKD và thời hạn `15 ngày làm việc` (`CF-004`) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-02** | DOC-002 | Chính sách Xử lý và Quản trị Thông tin Khách hàng CRM SongNhat | `data/g1/sources/DOC-002_POL-CRM-03_Customer_Information_Handling.md` | Điều 1.1-1.5, 2.1-2.7, 3.1-3.2, 4.1-4.5, 5.1 | Quy định bảo vệ DLCN theo Luật 91/2025/QH15, Phụ lục B2 (`PAS-066`) | Ngưỡng 500M (`CF-006 < 500M` CRM Staff, `CF-007 >= 500M` CRM Manager), SLA khẩn ngoài giờ `<= 1h` (`CF-008`) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-03** | DOC-003 | Chính sách Tiếp nhận và Định tuyến Dịch vụ/Bảo hành Thiết bị Công nghiệp | `data/g1/sources/DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md` | Điều 1.1-1.3, 2.1-2.5, 3.1-3.4, 4.1-4.3, 5.1 | Bảng phân tuyến công suất (`CF-009 <= 37 kW`, `CF-010 > 37 kW`, Ex-d `CF-032`), bảo hành tiêu chuẩn 12 tháng (`CF-034`), Phụ lục B3 (`PAS-082`) | 03 chứng từ bắt buộc, bổ sung ảnh Fault Code biến tần (`CF-033`), loại trừ lỗi người dùng | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-04** | DOC-004 | SOP Lập phiếu đề xuất chiết khấu và Gross Margin CRM | `data/g1/sources/DOC-004_SOP-CRM-QBG-01_Discount_GrossMargin.md` | Bước 1 (`PAS-050`), Bước 2-5 (`PAS-051..054`) | Quy chuẩn phiếu đề xuất chiết khấu, bảng tính Gross Margin `BM-KD-02` | Thẩm quyền SOP xếp sau Policy (DAT 03 layer 2), Substitute Owner (`VN 04`) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-05** | DOC-005 | SOP Xác minh Chứng từ & Cập nhật Hồ sơ Khách hàng CRM | `data/g1/sources/DOC-005_SOP-CRM-KH-01_Customer_Verification_Update.md` | Bước 1 (`PAS-071`), Bước 2-4 (`PAS-072..074`) | Quy trình kiểm tra GPKD/CCCD đại diện pháp luật | Thời hạn xử lý hồ sơ thông tin và phân quyền cập nhật CRM | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-06** | DOC-006 | Mẫu Hợp đồng khung phân phối B2B | `data/g1/sources/DOC-006_HDNT-B2B-SYN-2026_Framework_Contract.md` | Điều 4.2-4.4 Hợp đồng B2B (`PAS-055..057`) | Điều khoản chiết khấu khung 12% Biến tần trung thế, hiệu lực báo giá 30 ngày làm việc, tạm ứng 15% | Kiểm thử xung đột DAT 05: Cấm tự suy diễn thứ bậc ưu tiên giữa Hợp đồng khách hàng và Chính sách nội bộ, bắt buộc kích hoạt Conflict Hold | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-07** | DOC-007 | Tập mẫu Ghi chú lịch sử giao dịch & tiền lệ chiết khấu VIP | `data/g1/sources/DOC-007_CRM-STAFF-NOTES-SYN_Quotation_History.md` | Ghi chú NOTE-SYN-001 (`PAS-058`) | Tiền lệ duyệt chiết khấu 18% khách VIP năm 2025 | Kiểm thử DAT 03 / ANS 05: Ghi chú cá nhân không phủ quyết chính sách | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-08** | DOC-008 | Phụ lục Bảo vệ Dữ liệu Khách hàng B2B DPA-B2B-SYN-2026 | `data/g1/sources/DOC-008_DPA-B2B-SYN-2026_Customer_Data_Addendum.md` | Điều 3.2 Phụ lục DPA (`PAS-075`) | Cam kết xóa dữ liệu cá nhân khách hàng B2B trong 15 ngày | Xung đột thời hạn lưu trữ Annex C (15 ngày vs 90 ngày) kích hoạt Conflict Hold | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-09** | DOC-009 | SOP Tiếp nhận Chứng từ & Định tuyến Bảo hành Tuyến 1/Tuyến 2 | `data/g1/sources/DOC-009_SOP-CRM-BH-01_Warranty_Intake_Routing.md` | Bước 1 (`PAS-089`), Bước 2-4 (`PAS-090..092`) | Biểu mẫu phiếu tiếp nhận bảo hành, checklist tem niêm phong | Định tuyến Tuyến 1 (thay linh kiện) và Tuyến 2 (gửi hãng sản xuất OEM) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-10** | DOC-010 | Điều khoản Bảo hành Tiêu chuẩn của Hãng Sản xuất OEM-TERMS | `data/g1/sources/DOC-010_OEM-TERMS-SYN-2026_Manufacturer_Warranty_Terms.md` | Điều 2.1 Điều khoản Hãng (`PAS-093`) | Yêu cầu gửi báo cáo giám định Hãng cho thiết bị công suất `> 30 kW` | Xung đột ngưỡng công suất Hãng `> 30 kW` vs chính sách nội bộ `37 kW` của `DOC-003` (`CF-040`, DAT 03 layer 5, Conflict Hold) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-11** | DOC-011 | Tập Ghi chú Lịch sử CRM Bảo hành | `data/g1/sources/DOC-011_CRM-STAFF-NOTES-BH_Warranty_History.md` | Ghi chú NOTE-BH-001 (`PAS-095`) | Tiền lệ giải quyết bảo hành ngoại lệ không cần Phiếu bảo hành năm 2025 | Ghi chú cũ không được ghi đè quy định 03 chứng từ bắt buộc của Policy v1.0 | **PASS (100% VERIFIED_ACCESSIBLE)** |

- **Tệp nhật ký chi tiết:** [source_uri_inspection_log.csv](source_uri_inspection_log.csv).
- **Kết luận:** 
  1. Toàn bộ 11/11 tài liệu gốc đã được merge đầy đủ trên nhánh `develop` tại PR #32.
  2. Tên tệp Họ 3 được lưu chuẩn xác là `DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md` và Họ 2 là `DOC-002_POL-CRM-03_Customer_Information_Handling.md`.
  3. Tất cả liên kết kiểm tra mở xem thực tế đều đạt chuẩn 100% `VERIFIED_ACCESSIBLE`, không có liên kết nào bị thiếu hoặc gãy.

---

## 4. CAM KẾT BẢO VỆ HÀNG RÀO ĐỘC LẬP CHINESE WALL (SCRM ONBOARDING GUIDE §4, §23)

Nhằm bảo đảm tính khách quan tuyệt đối cho giai đoạn kiểm định độc lập Cổng G2 -> G3:
1. **Trên nhánh Git công khai (`uat/...` / PR):** 100 ca Sealed chỉ hiển thị mã băm SHA-256 xác thực toàn vẹn (`SEALED_TASK_HIDDEN_PER_GUARDRAIL_1`) và metadata phân vùng.
2. **Bàn giao cách ly:** Nội dung chi tiết câu hỏi và đáp án của 100 ca Sealed V2 được `[P4]` đóng gói và bàn giao **trực tiếp, riêng biệt cho `[S4]` Quý Hải** đóng băng tại kho riêng `ckpa-dev-val-eval/sealed-eval-repo @ 33180db` (`CKPA-67` & `CKPA-68`).
3. **Tuyệt đối cấm:** Không gửi nội dung 100 Sealed cho các kỹ sư phát triển `S2`, `S3`, `S5` và không commit lên nhánh `develop` chung.

---

## 5. BẢNG THEO DÕI KÝ NHẬN VÀ BÀN GIAO SUB-TASK CKPA-66 (MINH BẠCH)

| Vai trò | Thành viên | Trách nhiệm đối soát | Trạng thái thực tế | Ghi chú theo dõi |
|---|---|---|:---:|---|
| **Lead bàn giao (P4)** | **Ngô Thị Trà My** | Hoàn thành đủ 200 câu hỏi sạch PII & Biên bản check source 11/11 doc | **ĐÃ HOÀN TẤT & ĐỒNG BỘ** | Gồm gói 100 Sealed V2 (`VG-19..43`) |
| **Chủ sở hữu Bảo mật (P5)** | **Nguyễn Anh Khoa** | Thẩm định độc lập tiêu chí 0% PII (SEC 02/06) trên 200 câu hỏi | **ĐÃ THẨM ĐỊNH (0% PII)** | CI Guard PASS 0 vi phạm PII |
| **Quản lý Dữ liệu (P3)** | **Trần Chí Kha** | Thẩm định khớp nối tham chiếu gốc, mã băm SHA-256 & đồng ký nhãn `CKPA-68` | **ĐÃ MERGE & ĐỒNG KÝ** | 11/11 `source_uri` VERIFIED_ACCESSIBLE |
| **Kiểm định Độc lập (S4)** | **Quý Hải** | Tiếp nhận 200 câu hỏi & đóng băng 100 Sealed V2 vào `sealed-eval-repo` | **ĐÃ ĐÓNG BĂNG (`33180db`)** | Hoàn tất `CKPA-67` (`Done` 26/11) |
| **Chủ đầu tư / PO (P1)** | **Mỹ Vân** | Phê duyệt nghiệm thu Sub-task CKPA-66 (G1-AC07) | **ĐÃ NGHIỆM THU (`Done`)** | Đủ 3 file UAT chuẩn mực & đồng bộ 200/200 `source_uri` |

---

*Hồ sơ cập nhật đồng bộ ngày 26/11/2026 (v1.4): (1) Đồng bộ metadata ẩn danh của 100 ca `SEALED-001..100` (`VG-19..VG-43`, cơ cấu `52/24/24`, SHA-256 `372988c4...`, `P2_P3_CO_SIGNED_APPROVED`) khớp với kho đóng băng `ckpa-dev-val-eval/sealed-eval-repo @ 33180db` (`CKPA-67` & `CKPA-68`); (2) Chuẩn hóa nghiệp vụ 100 câu mở (`VG-01..VG-18`: hiệu chỉnh `TASK-040` về động cơ 3 pha `37 kW` Tuyến 1, `TASK-072` về hộp giảm tốc `15 kW` Tuyến 1, ngưỡng `<= 37 kW` / `> 37 kW`, `CF-004` cho `VG-04`, `CF-006` cho `VG-13`, `PAS-018` cho `VG-16` và đồng nhất 100% `Record_SHA256` giữa 3 tệp CSV UAT); (3) Chuẩn hóa bảng nhật ký `source_uri_inspection_log.csv` khớp nguyên văn `DOC-001..DOC-011`.*
