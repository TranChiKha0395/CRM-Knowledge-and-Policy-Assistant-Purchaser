# BÁO CÁO NGHIỆM THU & ĐẶC TẢ HOÀN THÀNH STORY CKPA-65 (BẢN HIỆU CHỈNH)
## [G1][Mục8] Phân vùng 60/40/100 & 80 Challenges

> **Mã Story (Jira):** `CKPA-65` | **Mã gốc (Excel G1):** `CRM-G1-ST06`  
> **Tiêu chí nghiệm thu Cổng G1:** `G1-AC07`  
> **Nhánh Git làm việc:** `uat/CRM-G1-ST06-200-tasks-60-40-100-sealed`  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead điều phối Story:** `[P4] Ngô Thị Trà My (Staff users)`  
> **Collaborators / RACI:** `[S4] Quý Hải (Quality Lead)`, `[P2] Hữu Tài (Policy Owner)`, `[P3] Trần Chí Kha (Data Steward)`  
> **Reporter / Nghiệm thu (PO):** `[P1] Mỹ Vân (Purchaser sponsor)`  
> **Thời gian thực hiện:** 2026-11-16 -> 2026-11-26 (Sprint 4–5 - Đồng bộ chốt `CKPA-65`, `CKPA-67`, `CKPA-68`)  
> **Truy vết RFP:** Mục 8 (60/40/100 + 80 challenges), Mục 11, DAT 08, SEC 02, SEC 06, Mục 9 (G1), VN 01, VN 02.

---

## 1. TỔNG QUAN USER STORY VÀ MỤC TIÊU CỔNG G1

### 1.1 Nội dung User Story
> **Là [P4] Người dùng nghiệp vụ đại diện (Staff users)**, tôi muốn hoàn tất đủ 200 câu hỏi thực tế sạch 0% PII (kèm kiểm tra mở xem `source_uri` văn bản gốc) để **[S4] Quý Hải** phân vùng 60/40/100 theo quy tắc gom nhóm chống rò rỉ (*"Keep related variants and records in one partition"*) và lưu trữ 80 Challenges vào kho riêng `sealed-eval-repo`, đồng thời chuyển giao cho 2 Policy Reviewers (**[P2] Hữu Tài**, **[P3] Chí Kha**) rà soát và đồng gán nhãn đáp án chuẩn, nhằm xác lập bộ dữ liệu nghiệm thu độc lập không thể bị thao túng cho Cổng G1 và G2.

### 1.2 Tiến độ 3 Sub-tasks trực thuộc Story CKPA-65 (DoD Tiêu chí a)
Toàn bộ 3/3 Sub-tasks thành phần đã hoàn tất và đóng `Done` trên Jira:

| Mã Sub-task | Người phụ trách chính | Nội dung công việc | Trạng thái thực tế |
|---|---|---|:---:|
| **`CKPA-66` (`CRM-G1-SUB16`)** | **`[P4]` Ngô Thị Trà My** | Thu thập, làm sạch đủ 200 câu hỏi thực tế (0% PII theo SEC 02/06) & thực hiện kiểm tra mở xem 100% liên kết tài liệu gốc `source_uri`. | **ĐÃ HOÀN THÀNH (`Done`)** |
| **`CKPA-67` (`CRM-G1-SUB17`)** | **`[S4]` Quý Hải** | Niêm phong bộ `100 SEALED` thay thế V2 (`VG-19..VG-43`, `52/24/24`, SHA-256 `372988c4...`) + `80 Challenges` tại `ckpa-dev-val-eval/sealed-eval-repo` (`33180db`), cách ly tuyệt đối khỏi `S2/S3`. | **ĐÃ ĐÓNG BĂNG (`Done`)** |
| **`CKPA-68` (`CRM-G1-SUB18`)** | **`[P2]` Hữu Tài & `[P3]` Chí Kha** | Rà soát nhãn độc lập (Two Policy Reviewers) và đồng ký duyệt nhãn vàng chuẩn cho `100 Sealed` & `80 Challenges` (`CKPA-68_Bien_Ban_Dong_Gan_Nhan_Va_Ky_Xac_Nhan_Kep_P2_P3.md`). | **ĐÃ ĐỒNG KÝ DUYỆT (`Done`)** |

---

## 2. KẾT QUẢ PHÂN VÙNG 200 REAL TASKS (60 DEV / 40 VAL / 100 SEALED)

### 2.1 Ma trận Phân bổ 200 Câu hỏi Thực tế (Đồng bộ Gói Thay thế V2 `sealed-eval-repo @ 33180db`)
Phân bổ chính xác theo 3 họ chính sách chuẩn của RFP Mục 1, `CKPA-58` và `CKPA-67` / `CKPA-68`:

| Phân vùng (Partition) | Mục đích sử dụng | POL-001 (Báo giá & CK) | POL-002 (Xử lý thông tin KH) | POL-003 (Dịch vụ & Bảo hành) | Tổng số ca |
|---|---|:---:|:---:|:---:|:---:|
| **`DEV` (60 ca sơ bộ / Open)** | Phục vụ đội Build (`S2` & `S3`) phát triển & tinh chỉnh hàng ngày (`VG-01..VG-18`) | 24 ca | 18 ca | 18 ca | **60 ca** |
| **`VAL` (40 ca sơ bộ / Open)** | Phục vụ đánh giá độc lập (`S4`) tinh chỉnh ngưỡng trước G2 (`VG-01..VG-18`) | 16 ca | 12 ca | 12 ca | **40 ca** |
| **`SEALED` (100 ca V2)** | **Niêm phong đóng băng trong `sealed-eval-repo @ 33180db`** (`VG-19..VG-43`, phục vụ nghiệm thu G2 -> G3) | 52 ca | 24 ca | 24 ca | **100 ca** |
| **Tổng cộng** | **Bộ dữ liệu thực tế 200 Real Tasks (`VG-01..VG-43`)** | **92 ca** | **54 ca** | **54 ca** | **200 ca** |

### 2.2 Quy tắc Gom nhóm Chống Rò rỉ (*Keep related variants and records in one partition*)
- **Ràng buộc RFP Mục 8 (trang 10):** Tuyệt đối không để xảy ra hiện tượng rò rỉ dữ liệu (data leakage) giữa tập mở (`DEV`/`VAL`) và tập niêm phong nghiệm thu (`SEALED`).
- **Trạng thái bàn giao & Phân định trách nhiệm (`SoD`):**
  - Tập 100 câu mở (`TASK-001..TASK-100`) thuộc **18 nhóm biến thể `VG-01..VG-18`**; tập 100 câu niêm phong thay thế V2 (`TASK-101..TASK-200` / `SEALED-001..100`) thuộc **25 nhóm biến thể độc lập `VG-19..VG-43`** (`25 x 4 = 100` ca), bảo đảm **0% trùng lặp hoặc giao cắt `Variant_Group_ID`** giữa Open 100 và Sealed 100.
  - Trên kho chung Purchaser, 100 ca mở giữ `Partition = PENDING_S4_PARTITION_CKPA67` để `[S4]` gom nguyên nhóm `VG` khi chia `60 DEV / 40 VAL`, còn 100 ca `SEALED` ghi nhận `Partition = SEALED`, mã băm `Record_SHA256` đồng bộ từ `sealed_100.csv` (`33180db`), `P2_P3_Consensus_Status = P2_P3_CO_SIGNED_APPROVED` và khóa toàn bộ câu hỏi/đáp án dưới nhãn `[SEALED_TASK_HIDDEN_PER_GUARDRAIL_1]` / `[LOCKED]`.

### 2.3 Kiểm tra An toàn Bảo mật PII (SEC 02 & SEC 06)
- **Kết quả rà soát tự động & thủ công:** Toàn bộ 200 câu hỏi thực tế đạt **0% PII** (0 SĐT, 0 CCCD/CMND thật, 0 email cá nhân).
- **Trạng thái đồng thuận nhãn:** 100 ca `SEALED` và 80 `Challenges` đã đạt **`P2_P3_CO_SIGNED_APPROVED`** tại `CKPA-68`; 100 ca mở trên repo Purchaser đã được `[P3]` rà soát đồng bộ điều khoản `PAS-xxx` và trường trọng yếu `CF-xxx` khớp 100% với `DOC-001..DOC-011`.
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
  - Bất kỳ hành vi làm lộ câu hỏi 100 Sealed cho đội phát triển đều vi phạm nghiêm trọng quy chế tách vai tại **SCRM Team Onboarding & Workflow Guide v1.0 (§4, §23)** và nguyên tắc SoD của RFP Mục 8 & 11.

---

## 6. BẢNG THEO DÕI KÝ NHẬN VÀ PHÊ DUYỆT STORY CKPA-65 (ĐÃ ĐÓNG `DONE` 26/11/2026)

| Vai trò | Thành viên | Nhiệm vụ xác nhận | Trạng thái thực tế |
|---|---|---|:---:|
| **Lead điều phối Story (P4)** | **Ngô Thị Trà My** | Hoàn thành đủ 200 câu hỏi sạch PII (gồm gói 100 Sealed V2) & kiểm tra mở xem `source_uri` | **ĐÃ HOÀN THÀNH (`Done`)** |
| **Kiểm định Độc lập (S4)** | **Quý Hải** | Niêm phong đóng băng `100 Sealed` (`VG-19..VG-43`) & `80 Challenges` trên `sealed-eval-repo @ 33180db` | **ĐÃ ĐÓNG BĂNG (`Done` — `CKPA-67`)** |
| **Policy Reviewer 1 (P2)** | **Hữu Tài** | Thẩm định và đồng ký duyệt nhãn đáp án chuẩn 3 họ chính sách (`CKPA-68`) | **ĐÃ KÝ DUYỆT (`Done` — `CKPA-68`)** |
| **Policy Reviewer 2 (P3)** | **Trần Chí Kha** | Thẩm định tham chiếu gốc, toàn vẹn SHA-256 & đồng ký duyệt nhãn vàng (`CKPA-68`) | **ĐÃ KÝ DUYỆT (`Done` — `CKPA-68`)** |
| **Chủ đầu tư / PO (P1)** | **Mỹ Vân** | Phê duyệt đóng Story `CKPA-65` / `CRM-G1-ST06` (Tiêu chí `G1-AC07`) | **ĐÃ NGHIỆM THU (`Done` 26/11/2026)** |
