# BÁO CÁO NGHIỆM THU & ĐẶC TẢ HOÀN THÀNH STORY CKPA-65 (BẢN HIỆU CHỈNH)
## [G1][Mục8] Phân vùng 60/40/100 & 80 Challenges

> **Mã Story (Jira):** `CKPA-65` | **Mã gốc (Excel G1):** `CRM-G1-ST06`  
> **Tiêu chí nghiệm thu Cổng G1:** `G1-AC07`  
> **Nhánh Git làm việc:** `uat/CRM-G1-ST06-200-tasks-60-40-100-sealed`  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead điều phối Story:** `[P4] Ngô Thị Trà My (Staff users)`  
> **Collaborators / RACI:** `[S4] Quý Hải (Quality Lead)`, `[P2] Hữu Tài (Policy Owner)`, `[P3] Trần Chí Kha (Data Steward)`  
> **Reporter / Nghiệm thu (PO):** `[P1] Mỹ Vân (Purchaser sponsor)`  
> **Thời gian thực hiện:** 2026-11-16 $\rightarrow$ 2026-11-20 (Sprint 4 - G1 Impl W2)  
> **Truy vết RFP:** Mục 8 (60/40/100 + 80 challenges), Mục 11, DAT 08, SEC 02, SEC 06, Mục 9 (G1), VN 01, VN 02.

---

## 1. TỔNG QUAN USER STORY VÀ MỤC TIÊU CỔNG G1

### 1.1 Nội dung User Story
> **Là [P4] Người dùng nghiệp vụ đại diện (Staff users)**, tôi muốn hoàn tất đủ 200 câu hỏi thực tế sạch 0% PII (kèm kiểm tra mở xem `source_uri` văn bản gốc) để **[S4] Quý Hải** phân vùng 60/40/100 theo quy tắc gom nhóm chống rò rỉ (*"Keep related variants and records in one partition"*) và lưu trữ 80 Challenges vào kho riêng `sealed-eval-repo`, đồng thời chuyển giao cho 2 Policy Reviewers (**[P2] Hữu Tài**, **[P3] Chí Kha**) rà soát và đồng gán nhãn đáp án chuẩn, nhằm xác lập bộ dữ liệu nghiệm thu độc lập không thể bị thao túng cho Cổng G1 và G2.

### 1.2 Tiến độ 3 Sub-tasks trực thuộc Story CKPA-65 (DoD Tiêu chí a)
Toàn bộ 3/3 Sub-tasks thành phần được theo dõi minh bạch theo phân vai:

| Mã Sub-task | Người phụ trách chính | Nội dung công việc | Trạng thái thực tế |
|---|---|---|:---:|
| **CRM-G1-SUB16** | **`[P4]` Ngô Thị Trà My** | Thu thập, làm sạch đủ 200 câu hỏi thực tế (0% PII theo SEC 02/06) & thực hiện kiểm tra mở xem 100% liên kết tài liệu gốc `source_uri`. | **ĐÃ HOÀN THÀNH BÀN GIAO** |
| **CRM-G1-SUB17** | **`[S4]` Quý Hải** | Phân vùng 60 Dev / 40 Val / 100 Sealed theo quy tắc chống rò rỉ; thiết lập kho riêng `sealed-eval-repo` cách ly với S2/S3. | **ĐANG TIẾP NHẬN / PHÂN VÙNG** |
| **CRM-G1-SUB18** | **`[P2]` Hữu Tài & `[P3]` Chí Kha** | Rà soát nhãn độc lập (Two Policy Reviewers) và đồng ký duyệt nhãn vàng chuẩn cho 200 Real Tasks & 80 Challenges. | **CHỜ RÀ SOÁT NHÃN (PENDING)** |

---

## 2. KẾT QUẢ PHÂN VÙNG 200 REAL TASKS (60 DEV / 40 VAL / 100 SEALED)

### 2.1 Ma trận Phân bổ 200 Câu hỏi Thực tế (Đã chuẩn hóa thứ tự Họ chính sách)
Phân bổ chính xác theo 3 họ chính sách chuẩn của RFP Mục 1 & CKPA-58:

| Phân vùng (Partition) | Mục đích sử dụng | POL-001 (Báo giá & CK) | POL-002 (Xử lý thông tin KH) | POL-003 (Dịch vụ & Bảo hành) | Tổng số ca |
|---|---|:---:|:---:|:---:|:---:|
| **`DEV` (60 ca)** | Công khai cho đội Build (`S2` & `S3`) phát triển & tinh chỉnh hàng ngày | 24 ca | 18 ca | 18 ca | **60 ca** |
| **`VAL` (40 ca)** | Dành cho đánh giá độc lập (`S4`) tinh chỉnh ngưỡng truy xuất/chấm điểm trước G2 | 16 ca | 12 ca | 12 ca | **40 ca** |
| **`SEALED` (100 ca)** | **Niêm phong tuyệt đối trong `sealed-eval-repo`** phục vụ nghiệm thu độc lập G2 $\rightarrow$ G3 | 38 ca | 30 ca | 32 ca | **100 ca** |
| **Tổng cộng** | **Bộ dữ liệu thực tế 200 Real Tasks** | **78 ca** | **60 ca** | **62 ca** | **200 ca** |

### 2.2 Quy tắc Gom nhóm Chống Rò rỉ (*Keep related variants and records in one partition*)
- **Ràng buộc RFP Mục 8 (trang 10):** Tuyệt đối không để xảy ra hiện tượng rò rỉ dữ liệu (data leakage) giữa tập học/phát triển (`DEV`) và tập niêm phong nghiệm thu (`SEALED`).
- **Trạng thái bàn giao & Phân định trách nhiệm (`SoD`):**
  - Trên kho chung Purchaser, tệp `200_real_tasks_partitioned.csv` đặt trường `Partition = PENDING_S4_PARTITION_CKPA67` (cột `Provisional_Partition` chỉ phản ánh cơ cấu số lượng sơ bộ `60 DEV / 40 VAL / 100 SEALED` từ 2 đợt thu thập, kèm **18 nhóm biến thể `VG-01..VG-18`** [`6×13 + 10×12 + 2×1 = 200`] đã chuẩn hóa khóa ngoại điều khoản `PAS-xxx` và trường trọng yếu `CF-xxx`, đảm bảo cả 3 phân vùng đều có đủ 3 họ `POL-001`, `POL-002`, `POL-003` khi gom nguyên nhóm).
  - Thuật toán gom cụm toàn bộ các biến thể cùng `Variant_Group_ID` vào **duy nhất một phân vùng chính thức** (`60 DEV / 40 VAL / 100 SEALED`) thuộc thẩm quyền độc lập của **`[S4]` Phạm Quý Hải tại Sub-task `CKPA-67`** trên kho cách ly `sealed-eval-repo`.
  - 100 ca `SEALED` trên repo chung chỉ hiển thị mã băm xác thực `SHA-256` (`Record_SHA256`) và nhãn khóa `[LOCKED]`, tuyệt đối không lộ nội dung câu hỏi hay đáp án chi tiết.

### 2.3 Kiểm tra An toàn Bảo mật PII (SEC 02 & SEC 06)
- **Kết quả rà soát tự động & thủ công:** Toàn bộ 200 câu hỏi thực tế đạt **0% PII** (0 SĐT, 0 CCCD/CMND thật, 0 email cá nhân).
- **Trạng thái đồng thuận nhãn:** Đặt ở mức **`PENDING_P2_P3_REVIEW`** chờ 2 Policy Reviewers ([P2] Hữu Tài & [P3] Trần Chí Kha) chính thức ký duyệt.
- **Tệp dữ liệu lưu trữ (bản che hash 100 ca `SEALED` trên repo Purchaser):**
  - Định dạng CSV: [`200_real_tasks_partitioned.csv`](200_real_tasks_partitioned.csv)

---

## 3. DANH MỤC 80 CONSTRUCTED CHALLENGES (GỒM 40 CA VN 02)

- **40 ca chung toàn hệ thống (`CHAL-SYS-001 .. 040`):** Kiểm thử Future Policy (5 ca), Historical/Superseded (5 ca), Ranh giới ngưỡng `<, <=, =, >=, >` (6 ca), Thiếu phụ lục thiết yếu DAT 08 (5 ca), Xung đột hợp đồng vs chính sách DAT 05 (5 ca), RBAC least-privilege (5 ca), Ghi chú CRM cũ (4 ca), Prompt Injection ANS 08 (3 ca), và Thu hồi giữa lúc sinh câu trả lời - Worked Case 9 (2 ca).
- **40 ca định hướng Việt Nam VN 02 (`CHAL-VN-001 .. 040`):**
  - 10 ca Ngôn ngữ, không dấu, viết tắt CRM và bảo toàn từ phủ định.
  - 10 ca Ngày tháng & Múi giờ UTC+7 giờ Việt Nam, ranh giới 00:00:00, ngày nghỉ lễ Tết.
  - 10 ca Ngưỡng số tiền chiết khấu, tiền tệ USD/VND, ngoại lệ phê duyệt của Tổng Giám Đốc.
  - 10 ca Quyền truy cập direct link, RBAC snippet, cache purge 5 phút (OPS 05).
- **Tệp dữ liệu lưu trữ:** Cô lập tuyệt đối trong kho riêng **`sealed-eval-repo`** (`CKPA-48` / `CKPA-67`, không lưu plaintext `80_constructed_challenges` trên repo Purchaser theo nguyên tắc Chinese Wall).

---

## 4. BIÊN BẢN KIỂM TRA MỞ XEM TÀI LIỆU GỐC (`SOURCE_URI`)

- P4 cùng nhóm 4 người dùng đại diện đã kiểm tra mở xem 100% liên kết văn bản gốc (toàn bộ 11/11 tài liệu DOC-001..DOC-011 đã lên nhánh `develop` tại PR #32):
  - `DOC-001`: Quy trình Báo giá và Phê duyệt Thương mại SongNhat (POL-001).
  - `DOC-002`: Chính sách Xử lý và Quản trị Thông tin Khách hàng CRM SongNhat (POL-002).
  - `DOC-003`: Chính sách Tiếp nhận và Định tuyến Dịch vụ/Bảo hành Thiết bị Công nghiệp (POL-003 - tên tệp `DOC-003_POL-CRM-02_Warranty_and_Service_Routing.md`).
  - `DOC-004 .. DOC-011`: Đầy đủ các tài liệu SOP, Hợp đồng B2B, Phụ lục DPA, Điều khoản OEM và Ghi chú CRM.
- **Kết quả:** 100% liên kết mở đúng tài liệu, đúng số trang và điều khoản, **0 liên kết gãy**, trạng thái xác nhận **`VERIFIED_ACCESSIBLE`**.
- **Tệp lưu trữ:** [`source_uri_inspection_log.csv`](source_uri_inspection_log.csv).

---

## 5. HÀNG RÀO ĐỘC LẬP CHINESE WALL & BẢO VỆ 100 SEALED

- **CẢNH BÁO ĐỎ TUÂN THỦ:**
  - Kho câu hỏi và đáp án của **100 Sealed Acceptance Cases** tuyệt đối **KHÔNG ĐƯỢC GỬI CHO S2/S3/S5** và **KHÔNG COMMIT LÊN DEVELOP**.
  - P4 chỉ bàn giao trực tiếp file niêm phong cho **[S4] Quý Hải** để đưa vào `sealed-eval-repo` sau khi hoàn thành CKPA-48.
  - Bất kỳ hành vi làm lộ câu hỏi 100 Sealed cho đội phát triển đều vi phạm nghiêm trọng quy chế R10 (`rules.md`) và nguyên tắc SoD của RFP Mục 8 & 11.

---

## 6. BẢNG THEO DÕI KÝ NHẬN VÀ PHÊ DUYỆT STORY CKPA-65 (MINH BẠCH)

| Vai trò | Thành viên | Nhiệm vụ xác nhận | Trạng thái thực tế |
|---|---|---|:---:|
| **Lead điều phối Story (P4)** | **Ngô Thị Trà My** | Hoàn thành đủ 200 câu hỏi sạch PII & kiểm tra mở xem `source_uri` | **ĐÃ HOÀN THÀNH BÀN GIAO** |
| **Kiểm định Độc lập (S4)** | **Quý Hải** | Tiếp nhận phân vùng 60/40/100 & lưu 100 Sealed vào `sealed-eval-repo` | **CHỜ TIẾP NHẬN BÀN GIAO (PENDING)** |
| **Policy Reviewer 1 (P2)** | **Hữu Tài** | Thẩm định và ký duyệt nhãn đáp án chuẩn 3 họ chính sách | **CHỜ RÀ SOÁT NHÃN (PENDING)** |
| **Policy Reviewer 2 (P3)** | **Trần Chí Kha** | Thẩm định dữ liệu tham chiếu gốc và tính toàn vẹn băm SHA-256 | **CHỜ RÀ SOÁT NHÃN (PENDING)** |
| **Chủ đầu tư / PO (P1)** | **Mỹ Vân** | Phê duyệt đóng Story CKPA-65 / CRM-G1-ST06 (Tiêu chí G1-AC07) | **CHỜ NGHIỆM THU (PENDING)** |
