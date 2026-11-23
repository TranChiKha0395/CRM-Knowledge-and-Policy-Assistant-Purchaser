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
> **Lịch thực hiện:** 2026-11-16 $\rightarrow$ 2026-11-23 (Sprint 4 - G1 Impl W2)  
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

| Mã Họ chính sách | Tên quy trình nghiệp vụ chuẩn RFP | Đợt 1 (CKPA-55) | Đợt 2 (Bổ sung) | Tổng số câu hỏi thực tế | Tỷ lệ cơ cấu |
|---|---|:---:|:---:|:---:|:---:|
| **POL-001** *(Họ 1)* | Quy trình Báo giá & Phê duyệt Thương mại | 40 ca | 38 ca | **78 câu** | 39.0% |
| **POL-002** *(Họ 2)* | Quy trình Xử lý Thông tin & Dữ liệu Khách hàng | 30 ca | 30 ca | **60 câu** | 30.0% |
| **POL-003** *(Họ 3)* | Quy trình Tiếp nhận Dịch vụ & Bảo hành Kỹ thuật | 30 ca | 32 ca | **62 câu** | 31.0% |
| **Tổng cộng** | **3 họ chính sách cốt lõi SongNhat** | **100 ca** | **100 ca** | **200 ca thực tế** | **100%** |

*(Ghi chú SoD & Phân vùng dữ liệu: Theo đúng phân định trách nhiệm Cổng G1, vai trò [P4] Trà My bàn giao tập dữ liệu sạch PII toàn diện 200 câu dưới dạng mã trung lập TASK-001..TASK-200. Thuật toán gom cụm biến thể theo Variant_Group_ID và phân vùng chính thức 60 DEV / 40 VAL / 100 SEALED chống rò rỉ dữ liệu thuộc thẩm quyền độc lập của [S4] Quý Hải tại Sub-task CKPA-67).*

### 2.2 Rà soát An toàn Bảo mật PII (SEC 02 & SEC 06)
- **Phương pháp rà soát:** Kết hợp công cụ Regex Scan tự động và rà soát thủ công 100% trường Question_VN:
  - Số điện thoại cá nhân thật: **0 phát hiện** (0 SĐT).
  - Số Căn cước công dân / CMND thật: **0 phát hiện** (0 CCCD).
  - Email cá nhân thật: **0 phát hiện** (0 Email).
  - Toàn bộ tên định danh khách hàng đều được ẩn danh hóa hoặc dùng mã mẫu (Đại lý A, Khách hàng B2B X).
- **Trạng thái đồng thuận nhãn vàng:** Đặt ở mức minh bạch là **PENDING_P2_P3_REVIEW** chờ 2 Policy Reviewers ([P2] Hữu Tài và [P3] Trần Chí Kha) rà soát và xác nhận chính thức trên Jira.
- **Đồng bộ mã trường trọng yếu:** Toàn bộ trường Gold_Critical_Field_IDs được đồng bộ sang mã chuẩn **CF-001 .. CF-010** của Corpus CKPA-50:
  - Họ 1: CF-001 ($\le 5\%$, CVKD), CF-002 (5-15\%, TPKD), CF-003 ($> 15\%$, GĐKD), CF-004 (hiệu lực 15 ngày).
  - Họ 2: CF-005 (liên hệ/email GTGT), CF-006 (đổi đại diện PL $\le 500$M), CF-007 (đổi đại diện PL $> 500$M), CF-008 (quyền DLCN theo Luật 91/2025/QH15).
  - Họ 3: CF-009 (bảo hành tiêu chuẩn 24 tháng), CF-010 (đổi mới lỗi kỹ thuật 7 ngày).
- **Tập tin bàn giao:**
  - Định dạng CSV: [200_clean_real_tasks.csv](200_clean_real_tasks.csv)

---

## 3. KẾT QUẢ BÀN GIAO 2: BIÊN BẢN KIỂM TRA MỞ XEM TÀI LIỆU GỐC (SOURCE_URI & DAT 08)

Tuân thủ quy định Mục 9 Cổng G1 (*re-verified original reference access*) và kiểm tra chú thích/bảng thiết yếu (DAT 08), nhóm người dùng đại diện (P4 Trà My cùng 4 nhân viên SongNhat) đã đối soát 100% nguồn tham chiếu tài liệu. 

Sau khi PR #32 (`[CKPA-58]` Curate Full 3-Family G1 Corpus) được merge chính thức vào nhánh `develop`, toàn bộ 11/11 tài liệu gốc (`DOC-001 .. DOC-011`) thuộc 3 họ chính sách và 5 lớp thẩm quyền (DAT 03) đã hiện diện đầy đủ, mở xem trực tiếp thành công và đạt **100% VERIFIED_ACCESSIBLE**:

| Mã Kiểm tra | Tài liệu ID | Văn bản quy trình | Đường dẫn tài liệu thực tế (`File_URI`) | Mẫu điều khoản kiểm tra | Bảng biểu & Phụ lục thiết yếu | Kiểm tra Chú thích (DAT 08) | Kết quả thẩm tra thực tế |
|---|:---:|---|---|---|---|---|:---:|
| **CHK-DOC-01** | DOC-001 | Quy trình Báo giá và Phê duyệt Thương mại SongNhat | `data/g1/sources/DOC-001_POL-CRM-01_Quotation_Commercial_Approval.md` | Điều 1.1, 2.1-2.3, 3.1-3.3, 4.1 | Bảng 2.1 (CF-001 $\le 5\%$, CF-002 5-15\%, CF-003 $> 15\%$), Phụ lục tính Gross Margin | Thẩm quyền duyệt CVKD, TPKD, GĐKD và thời hạn 15 ngày | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-02** | DOC-002 | Chính sách Xử lý và Quản trị Thông tin Khách hàng CRM SongNhat | `data/g1/sources/DOC-002_POL-CRM-03_Customer_Information_Handling.md` | Điều 1.1-1.3, 2.1-2.4, 3.1-3.3, 4.1-4.4, 5.1 | Biểu mẫu BM-04, Quy định bảo vệ DLCN theo Luật 91/2025/QH15 | Ngưỡng 500M (CF-006, CF-007), quyền RBAC reader (CF-008, CF-024) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-03** | DOC-003 | Chính sách Tiếp nhận và Định tuyến Dịch vụ/Bảo hành Thiết bị Công nghiệp | `data/g1/sources/DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md` | Điều 1.1-1.3, 2.1-2.5, 3.1-3.4, 4.1-4.3, 5.1 | Bảng thời hạn bảo hành 24 tháng (CF-009, CF-032), Đổi mới 7 ngày (CF-010, CF-033) | 03 chứng từ bắt buộc, điều kiện đổi mới 7 ngày, loại trừ lỗi người dùng | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-04** | DOC-004 | SOP Lập phiếu đề xuất chiết khấu và Gross Margin CRM | `data/g1/sources/DOC-004_SOP-CRM-QBG-01_Discount_GrossMargin.md` | Bước 1 (PAS-050), Bước 2-3 (PAS-051..054) | Quy chuẩn phiếu đề xuất chiết khấu, công thức Gross Margin | Thẩm quyền SOP xếp sau Policy (DAT 03 layer 2) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-05** | DOC-005 | SOP Xác minh Chứng từ & Cập nhật Hồ sơ Khách hàng CRM | `data/g1/sources/DOC-005_SOP-CRM-KH-01_Customer_Verification_Update.md` | Bước 1 (PAS-070), Bước 2-4 (PAS-071..073) | Quy trình kiểm tra GPKD/CCCD đại diện pháp luật | Thời hạn xử lý hồ sơ thông tin và phân quyền cập nhật CRM | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-06** | DOC-006 | Mẫu Hợp đồng khung phân phối B2B | `data/g1/sources/DOC-006_HDNT-B2B-SYN-2026_Framework_Contract.md` | Điều 4.2 Hợp đồng B2B (PAS-055) | Điều khoản bảo lưu chiết khấu cam kết 18% cố định Đại lý cấp 1 | Kiểm thử xung đột DAT 05: Hợp đồng KH ưu tiên cao hơn Chính sách nội bộ | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-07** | DOC-007 | Tập mẫu Ghi chú lịch sử giao dịch & tiền lệ chiết khấu VIP | `data/g1/sources/DOC-007_CRM-STAFF-NOTES-SYN_Quotation_History.md` | Ghi chú NOTE-SYN-001 (PAS-056) | Tiền lệ duyệt chiết khấu 16% của GĐKD năm 2025 | Kiểm thử DAT 03 / ANS 05: Ghi chú cá nhân không phủ quyết chính sách | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-08** | DOC-008 | Phụ lục Bảo vệ Dữ liệu Khách hàng B2B DPA-B2B-SYN-2026 | `data/g1/sources/DOC-008_DPA-B2B-SYN-2026_Customer_Data_Addendum.md` | Điều 3.2 Phụ lục DPA (PAS-075) | Cam kết xóa dữ liệu cá nhân khách hàng B2B trong 15 ngày | Xung đột thời hạn lưu trữ Annex C (15 ngày vs 90 ngày) kích hoạt Conflict Hold | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-09** | DOC-009 | SOP Tiếp nhận Chứng từ & Định tuyến Bảo hành Tuyến 1/Tuyến 2 | `data/g1/sources/DOC-009_SOP-CRM-BH-01_Warranty_Intake_Routing.md` | Bước 1 (PAS-089), Bước 2-4 (PAS-090..092) | Biểu mẫu phiếu tiếp nhận bảo hành, checklist tem niêm phong | Định tuyến Tuyến 1 (thay linh kiện) và Tuyến 2 (gửi hãng sản xuất OEM) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-10** | DOC-010 | Điều khoản Bảo hành Tiêu chuẩn của Hãng Sản xuất OEM-TERMS | `data/g1/sources/DOC-010_OEM-TERMS-SYN-2026_Manufacturer_Warranty_Terms.md` | Điều 2.1 Điều khoản Hãng (PAS-093) | Bảo hành động cơ/biến tần công nghiệp 18 tháng từ ngày xuất xưởng | Xung đột thời hạn SongNhat 24 tháng vs Hãng 18 tháng (CF-040, DAT 03 layer 5) | **PASS (100% VERIFIED_ACCESSIBLE)** |
| **CHK-DOC-11** | DOC-011 | Tập Ghi chú Lịch sử CRM Bảo hành | `data/g1/sources/DOC-011_CRM-STAFF-NOTES-BH_Warranty_History.md` | Ghi chú NOTE-BH-001 (PAS-095) | Tiền lệ giải quyết bảo hành ngoại lệ không cần Phiếu bảo hành năm 2025 | Ghi chú cũ không được ghi đè quy định 03 chứng từ bắt buộc của Policy v1.0 | **PASS (100% VERIFIED_ACCESSIBLE)** |

- **Tệp nhật ký chi tiết:** [source_uri_inspection_log.csv](source_uri_inspection_log.csv).
- **Kết luận:** 
  1. Toàn bộ 11/11 tài liệu gốc đã được merge đầy đủ trên nhánh `develop` tại PR #32.
  2. Tên tệp Họ 3 được lưu chuẩn xác là `DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md` và Họ 2 là `DOC-002_POL-CRM-03_Customer_Information_Handling.md`.
  3. Tất cả liên kết kiểm tra mở xem thực tế đều đạt chuẩn 100% `VERIFIED_ACCESSIBLE`, không có liên kết nào bị thiếu hoặc gãy.

---

## 4. CAM KẾT BẢO VỆ HÀNG RÀO ĐỘC LẬP CHINESE WALL (ĐIỀU R10 RULES.MD)

Nhằm bảo đảm tính khách quan tuyệt đối cho giai đoạn kiểm định độc lập Cổng G2 $\rightarrow$ G3:
1. **Trên nhánh Git công khai (`uat/...` / PR):** 100 ca Sealed chỉ hiển thị mã băm SHA-256 xác thực toàn vẹn (`SEALED_TASK_HIDDEN_PER_GUARDRAIL_1`) và metadata phân vùng.
2. **Bàn giao cách ly:** Nội dung chi tiết câu hỏi và đáp án của 100 ca Sealed được P4 đóng gói và bàn giao **trực tiếp, riêng biệt cho [S4] Quý Hải** để đưa vào kho riêng `sealed-eval-repo` sau khi CKPA-48 hoàn thành.
3. **Tuyệt đối cấm:** Không gửi nội dung 100 Sealed cho các kỹ sư phát triển `S2`, `S3`, `S5` và không commit lên nhánh `develop` chung.

---

## 5. BẢNG THEO DÕI KÝ NHẬN VÀ BÀN GIAO SUB-TASK CKPA-66 (MINH BẠCH)

| Vai trò | Thành viên | Trách nhiệm đối soát | Trạng thái thực tế | Ghi chú theo dõi |
|---|---|---|:---:|---|
| **Lead bàn giao (P4)** | **Ngô Thị Trà My** | Hoàn thành đủ 200 câu hỏi sạch PII & Biên bản check source 11/11 doc | **ĐÃ HOÀN TẤT & ĐỒNG BỘ** | Nhánh `uat/ckpa-66-sync-source-uri-lowercase-folder` |
| **Chủ sở hữu Bảo mật (P5)** | **Nguyễn Anh Khoa** | Thẩm định độc lập tiêu chí 0% PII (SEC 02/06) trên 200 câu hỏi | **ĐÃ THẨM ĐỊNH (0% PII)** | CI Guard PASS 0 vi phạm PII |
| **Quản lý Dữ liệu (P3)** | **Trần Chí Kha** | Thẩm định khớp nối tham chiếu gốc & mã băm SHA-256 | **ĐÃ MERGE DEVELOP (PR #32)** | 11/11 source_uri VERIFIED_ACCESSIBLE |
| **Kiểm định Độc lập (S4)** | **Quý Hải** | Tiếp nhận 200 câu hỏi & nạp 100 Sealed vào sealed-eval-repo | **ĐÃ TIẾP NHẬN PHÂN VÙNG** | Độc lập tại CKPA-67 |
| **Chủ đầu tư / PO (P1)** | **Mỹ Vân** | Phê duyệt nghiệm thu Sub-task CKPA-66 (G1-AC07) | **CHỜ KÝ DUYỆT ĐÓNG VÉ** | Đủ 3 file UAT chuẩn mực |

---

*Hồ sơ cập nhật ngày 23/11/2026. Sẵn sàng nghiệm thu Sub-task CKPA-66 trên Jira và GitHub.*
