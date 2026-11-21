# BÁO CÁO BÀN GIAO & MINH CHỨNG HOÀN THÀNH SUB-TASK CKPA-66
## [G1][Mục8] Hoàn tất 200 Câu hỏi thực & Check source

> **Mã công việc (Jira):** `CKPA-66` | **Mã gốc (Excel G1):** `CRM-G1-SUB16`  
> **Thuộc User Story:** `CKPA-65` / `CRM-G1-ST06` (*[G1][Mục8] Phân vùng 60/40/100 & 80 Challenges*)  
> **Tiêu chí nghiệm thu Cổng G1:** `G1-AC07`  
> **Nhánh Git làm việc:** `uat/CRM-G1-SUB16-complete-200-tasks-source-uri`  
> **Vị trí file chuẩn:** `docs/work-packages/ckpa-66-complete-200-tasks-source-uri-report.md`  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead:** `[P4] Ngô Thị Trà My (Staff users)`  
> **Collaborators / RACI:** `[P5] Nguyễn Anh Khoa`, `[P3] Trần Chí Kha`  
> **Reporter / Nghiệm thu (PO):** `[P1] Mỹ Vân (Purchaser sponsor)`  
> **Bên tiếp nhận bàn giao:** `[S4] Quý Hải (Quality Lead)`  
> **Lịch thực hiện:** 2026-11-16 $\rightarrow$ 2026-11-17 (Sprint 4 - G1 Impl W2)  
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
  - Họ 1: CF-001 ($\le 5\%$, CVKD), CF-002 (5-15\%$, TPKD), CF-003 ($> 15\%$, GĐKD), CF-004 (hiệu lực 15 ngày).
  - Họ 2: CF-005 (liên hệ/email GTGT), CF-006 (đổi đại diện PL $\le 500), CF-007 (đổi đại diện PL $> 500), CF-008 (quyền DLCN theo Luật 91/2025/QH15).
  - Họ 3: CF-009 (bảo hành tiêu chuẩn 24 tháng), CF-010 (đổi mới lỗi kỹ thuật 7 ngày).
- **Tập tin bàn giao:**
  - Định dạng CSV: [data/eval/200_clean_real_tasks.csv](../../data/eval/200_clean_real_tasks.csv)
  - Định dạng JSON: [data/eval/200_clean_real_tasks.json](../../data/eval/200_clean_real_tasks.json)

---

## 3. KẾT QUẢ BÀN GIAO 2: BIÊN BẢN KIỂM TRA MỞ XEM TÀI LIỆU GỐC (SOURCE_URI & DAT 08)

Tuân thủ quy định Mục 9 Cổng G1 (*re-verified original reference access*) và kiểm tra chú thích/bảng thiết yếu (DAT 08), nhóm người dùng đại diện (P4 Trà My cùng 4 nhân viên SongNhat) đã đối soát nguồn tham chiếu tài liệu:

| Mã Kiểm tra | Văn bản quy trình | Đường dẫn tài liệu thực tế (File_URI) | Mẫu điều khoản kiểm tra | Bảng biểu & Phụ lục thiết yếu | Kiểm tra Chú thích (DAT 08) | Kết quả thẩm tra thực tế |
|---|---|---|---|---|---|:---:|
| **CHK-DOC-01** | Quy trình Báo giá & Phê duyệt Thương mại (POL-001) | data/g1/sources/DOC-001_POL-CRM-01_Quotation_Commercial_Approval.md | Điều 1.1, 2.1-2.3, 3.1-3.3, 4.1 | Bảng 2.1 (CF-001 $\le 5\%$, CF-002 5-15\%$, CF-003 $> 15\%$), Phụ lục tính biên lợi nhuận | Đầy đủ chú thích thẩm quyền duyệt CVKD, TPKD, GĐKD và thời hạn báo giá 15 ngày | **PASS (100% Accessible & Verified, khớp Corpus CKPA-50)** |
| **CHK-DOC-02** | Quy chế Xử lý & Bảo vệ Dữ liệu Thông tin KH (POL-002) | data/g1/sources/DOC-002_POL-CRM-02_Customer_Data_Protection.md *(Dự thảo)* | Điều 1.2, 2.1-2.4, 3.1-3.3 *(Dự kiến)* | Biểu mẫu BM-04 (Đổi đại diện pháp luật), Quy định bảo vệ DLCN theo Luật 91/2025/QH15 | Chú thích ngưỡng 500 triệu lũy kế (CF-006, CF-007) và quyền dữ liệu cá nhân (CF-008) | **PENDING CURATION (Chờ [P3] Chí Kha hoàn tất biên tập Họ 2 tại CKPA-58)** |
| **CHK-DOC-03** | Quy định Tiếp nhận Dịch vụ & Bảo hành Kỹ thuật (POL-003) | data/g1/sources/DOC-003_POL-CRM-03_Warranty_and_Service_Routing.md *(Dự thảo)* | Điều 1.1, 2.2-2.5, 3.4, 4.2 *(Dự kiến)* | Bảng thời hạn bảo hành linh kiện 24 tháng (CF-009), Quy trình đổi mới 7 ngày (CF-010) | Chú thích điều kiện đổi mới 7 ngày và loại trừ lỗi do người dùng/thiên tai (DAT 08) | **PENDING CURATION (Chờ [P3] Chí Kha hoàn tất biên tập Họ 3 tại CKPA-58)** |

- **Tệp nhật ký chi tiết:** [data/eval/source_uri_inspection_log.csv](../../data/eval/source_uri_inspection_log.csv).
- **Kết luận:** 
  1. Nguồn tài liệu Họ 1 (POL-001) đã có sẵn trong repo và được đối soát 100% thành công với mã băm SHA-256 từ Corpus CKPA-50.
  2. Nguồn tài liệu Họ 2 và Họ 3 được ghi nhận trung thực là đang chờ hoàn thiện biên tập bởi [P3] Chí Kha tại CKPA-58 (cho cả Họ 2 và Họ 3); không khai khống đường dẫn tệp PDF ảo.

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
| **Lead bàn giao (P4)** | **Ngô Thị Trà My** | Hoàn thành đủ 200 câu hỏi sạch PII & Biên bản check source | **ĐÃ BÀN GIAO (CHỜ DUYỆT)** | Sẵn sàng mở PR nhánh `uat/CRM-G1-SUB16...` |
| **Chủ sở hữu Bảo mật (P5)** | **Nguyễn Anh Khoa** | Thẩm định độc lập tiêu chí 0% PII (SEC 02/06) trên 200 câu hỏi | **CHỜ RÀ SOÁT (PENDING)** | Kính mời P5 vào đối soát PII trên nhánh PR |
| **Quản lý Dữ liệu (P3)** | **Trần Chí Kha** | Thẩm định khớp nối tham chiếu gốc & mã băm SHA-256 | **CHỜ ĐỐI SOÁT (PENDING)** | Kính mời P3 kiểm tra liên kết source_uri |
| **Kiểm định Độc lập (S4)** | **Quý Hải** | Tiếp nhận 200 câu hỏi & nạp 100 Sealed vào sealed-eval-repo | **CHỜ TIẾP NHẬN (PENDING)** | S4 tiếp nhận dữ liệu phục vụ test offline G1 |
| **Chủ đầu tư / PO (P1)** | **Mỹ Vân** | Phê duyệt nghiệm thu Sub-task CKPA-66 (G1-AC07) | **CHỜ NGHIỆM THU (PENDING)** | Chờ xác nhận từ P5, P3 và S4 trước khi đóng ticket |

---

*Hồ sơ hoàn tất ngày 20/11/2026. Sẵn sàng đóng Sub-task CKPA-66 trên Jira.*
