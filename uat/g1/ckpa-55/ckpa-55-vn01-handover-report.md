# BÁO CÁO BÀN GIAO & MINH CHỨNG HOÀN THÀNH SUB-TASK CKPA-55 (BẢN HIỆU CHỈNH CHÍNH THỨC)
## [G1][VN01] Chuẩn bị 100 Câu hỏi thực & Từ điển VN

> **Mã công việc (Jira):** `CKPA-55` | **Mã gốc (Excel G1):** `CRM-G1-SUB08`  
> **Tiêu chí nghiệm thu Cổng G1:** `G1-AC07`  
> **Nhánh Git làm việc:** `uat/CRM-G1-SUB08-100-real-tasks-vn01-terms` (đồng bộ trên PR #20)  
> **Vị trí file chuẩn:** `uat/g1/ckpa-55/ckpa-55-vn01-handover-report.md`  
> **Phía phụ trách:** Purchaser (SongNhat)  
> **Assignee / Lead:** `[P4] Ngô Thị Trà My (Staff users)`  
> **Collaborators / RACI:** `[P5] Nguyễn Anh Khoa`, `[S3] Yến Nhi`  
> **Reporter / Nghiệm thu (PO):** `[P1] Mỹ Vân (Purchaser sponsor)`  
> **Người tiếp nhận bàn giao:** `[S4] Quý Hải (Quality Lead)` & `[S3] Yến Nhi (Retrieval Engineer)`  
> **Truy vết RFP:** Mục 8 (Evaluation), Mục 11 (Team Ownership), ANS 02, SEC 02, SEC 06, VN 01.

---

## 1. TỔNG QUAN VÀ MỤC TIÊU CÔNG VIỆC

Theo yêu cầu Cổng G1 (Mục 8 & Mục 11 RFP) và quy chuẩn phân định trách nhiệm **SCRM Onboarding Guide (§6.4 & §9)**, vai trò **P4 (Người dùng nghiệp vụ đại diện)** cùng 4 nhân sự nghiệp vụ SongNhat thực hiện nhiệm vụ:
1. **Làm sạch và bàn giao 100 câu hỏi thực tế đầu tiên** (gồm 60 ca `DEV` và 40 ca `VAL`), bảo đảm **0% PII** (thông tin định danh cá nhân) theo quy định bảo mật `SEC 02` và `SEC 06`.
2. **Tổng hợp Bảng Từ điển Viết tắt CRM & Thuật ngữ Tiếng Việt (`VN 01 Profile`)**, bao gồm tiếng Việt không dấu, chữ viết tắt CRM và thuật ngữ song ngữ Anh – Việt phục vụ trực tiếp cho module Chuẩn hóa truy vấn (`ANS 02`).
3. **Tuân thủ phân định vai trò SoD (Separation of Duties):** P4 chỉ bàn giao dữ liệu nghiệp vụ (JSON/CSV) và báo cáo minh chứng; việc tích hợp mã nguồn backend (`models.py`) do kỹ sư truy xuất `S3` (Yến Nhi) độc lập thực hiện trên nhánh phát triển của Supplier.

---

## 2. KẾT QUẢ BÀN GIAO 1: 100 CÂU HỎI THỰC TẾ ĐỢT 1 (100% SẠCH PII)

### 2.1 Chuẩn hóa Phân bổ 3 Họ Chính sách (Đã hiệu chỉnh đúng thứ tự RFP Mục 1 & CKPA-58)
Thứ tự 3 họ chính sách đã được hiệu chỉnh chính xác, tránh hoàn toàn lỗi đảo ngược giữa Họ 2 và Họ 3:

| Mã Họ chính sách | Tên quy trình nghiệp vụ chuẩn RFP | Số lượng ca `DEV` | Số lượng ca `VAL` | Tổng số câu hỏi | Ghi chú điều chỉnh |
|---|---|:---:|:---:|:---:|---|
| **`POL-001`** *(Họ 1)* | Quy trình Báo giá & Phê duyệt Thương mại | 24 ca | 16 ca | **40 câu** (40%) | Giữ nguyên chuẩn |
| **`POL-002`** *(Họ 2)* | Quy trình Xử lý Thông tin & Dữ liệu Khách hàng | 18 ca | 12 ca | **30 câu** (30%) | **Đã sửa:** Chuyển về đúng Họ 2 (trước bị nhầm là Họ 3) |
| **`POL-003`** *(Họ 3)* | Quy trình Tiếp nhận Dịch vụ & Bảo hành Kỹ thuật | 18 ca | 12 ca | **30 câu** (30%) | **Đã sửa:** Chuyển về đúng Họ 3 (trước bị nhầm là Họ 2) |
| **Tổng cộng** | **3 họ chính sách cốt lõi SongNhat** | **60 ca** | **40 ca** | **100 ca thực tế** | Khớp 100% thứ tự với CKPA-50 & CKPA-58 |

### 2.2 Bảng Ánh xạ Mã Trường Trọng yếu (Mapping Table: Legacy ID $\rightarrow$ Canonical ID)
Nhằm tránh gãy khóa ngoại khi Trưởng nhóm Kiểm định độc lập (`S4` Quý Hải) chạy script chấm tự động, toàn bộ các mã trường trọng yếu đã được đồng bộ chuẩn xác với bộ mã `CF-xxx` của bộ Corpus (CKPA-50 & G0):

| Mã trường ban đầu (Legacy ID) | Mã chuẩn hóa Corpus (`CF-xxx`) | Tên trường trọng yếu | Thuộc Họ | Ngưỡng / Quy tắc áp dụng chuẩn CKPA-50 |
|---|---|---|:---:|---|
| `CRIT-QBG-01` | **`CF-001`** | Hạn mức chiết khấu tiêu chuẩn | Họ 1 | $\le 5\%$, Chuyên viên Kinh doanh (CVKD) duyệt |
| `CRIT-QBG-02` | **`CF-002`** | Hạn mức chiết khấu cấp trung | Họ 1 | $> 5\%$ đến $\le 15\%$, Trưởng phòng Kinh doanh (TPKD) duyệt |
| `CRIT-QBG-03` | **`CF-003`** | Hạn mức chiết khấu đặc biệt | Họ 1 | $> 15\%$, Giám đốc Kinh doanh / GĐ Thương mại duyệt |
| `CRIT-QBG-04` | **`CF-004`** | Thời hạn hiệu lực báo giá | Họ 1 | Báo giá có hiệu lực tối đa 15 ngày kể từ ngày ban hành |
| `CRIT-CRM-01` | **`CF-005`** | Thời hạn cập nhật thông tin liên hệ / email GTGT | Họ 2 | SLA xử lý $\le 2$ giờ làm việc (`CRM Staff` — `reader`) |
| `CRIT-CRM-02` | **`CF-006`** | Cập nhật pháp lý DN dưới ngưỡng ($< 500$M) | Họ 2 | Hợp đồng lũy kế $< 500$ triệu VND, `CRM Staff` xử lý trong 4 giờ làm việc |
| `CRIT-CRM-03` | **`CF-007`** | Phê duyệt pháp lý KH trọng yếu ($\ge 500$M) | Họ 2 | Hợp đồng lũy kế $\ge 500$ triệu VND, `CRM Manager` phê duyệt trong 4 giờ làm việc |
| `CRIT-CRM-04` | **`CF-008`** | Cập nhật pháp lý khẩn cấp ngoài giờ hành chính | Họ 2 | SLA xử lý $\le 1$ giờ khi có phê duyệt của `CRM Director` |
| `CRIT-BH-01` | **`CF-009`** | Ngưỡng công suất định tuyến bảo hành Tuyến 1 | Họ 3 | Công suất $\le 37$ kW (kiểm tra đủ 03 chứng từ), định tuyến `Internal Tech Lead` |
| `CRIT-BH-02` | **`CF-010`** | Ngưỡng công suất định tuyến giám định Hãng Tuyến 2 | Họ 3 | Công suất $> 37$ kW (hoặc lỗi bo mạch chính), định tuyến `Vendor Chief Engineer` |

*(Ghi chú cấu trúc mã CF: Nhóm mã mở rộng `CF-011` đến `CF-022` thuộc Họ 1; Họ 2 sử dụng dải chuẩn `CF-005`..`CF-008`; Họ 3 sử dụng dải chuẩn `CF-009`..`CF-010` theo đúng cấu trúc dữ liệu G0 & CKPA-50).*

### 2.3 Phân định Rõ ràng về Phân nhóm Biến thể (Variant Groups) & Chống Rò rỉ Dữ liệu (RFP Mục 8)
- **Hiện trạng bộ 100 câu đợt 1:** Dữ liệu gắn nhãn ban đầu chứa 16 nhóm biến thể (`VG-01` đến `VG-16`). Việc gán nhãn `DEV` (60 ca) và `VAL` (40 ca) trong đợt 1 là phân bổ định lượng sơ bộ để kiểm định tỷ lệ câu hỏi theo 3 Họ chính sách (40 POL-001 / 30 POL-002 / 30 POL-003).
- **Nguyên tắc chống rò rỉ dữ liệu (RFP Mục 8):** RFP quy định rõ: *"Keep related variants and records in one partition"* (phải gom toàn bộ các biến thể thuộc cùng một nhóm vào duy nhất một phân vùng, tuyệt đối không tách sang cả DEV và VAL để tránh việc mô hình học thuộc đáp án trong tập DEV rồi trả lời tập VAL).
- **Phân định trách nhiệm (SoD Boundary):** Trách nhiệm thực hiện thuật toán phân vùng chính thức 60 DEV / 40 VAL / 100 SEALED và gom cụm toàn bộ `Variant_Group_ID` chống rò rỉ thuộc thẩm quyền độc lập của **[S4] Quý Hải tại Sub-task CKPA-67** (trên không gian độc lập `sealed-eval-repo`). P4 thực hiện bàn giao toàn bộ các nhóm biến thể sạch PII để S4 xử lý triệt để bài toán phân vùng tại CKPA-67.

### 2.4 Kết quả Kiểm tra An toàn Bảo mật PII (SEC 02 & SEC 06)
- **Kết quả quét tự động & rà soát nghiệp vụ:**
  - Không chứa số điện thoại cá nhân (0 SĐT).
  - Không chứa số Căn cước công dân / CMND thật (0 CCCD).
  - Không chứa email cá nhân hoặc tài khoản ngân hàng thực của khách hàng (0 email).
- **Trạng thái đồng thuận nhãn:** Đã cập nhật đúng thực tế là **`PENDING_P2_P3_REVIEW`** (Chờ rà soát và xác nhận chính thức từ Policy Reviewers `[P2]` Hữu Tài và `[P3]` Trần Chí Kha, không tự ý ghi khống `AGREED_BY_P2_AND_P3`).
- **Tệp dữ liệu lưu trữ đã cập nhật:**
  - Định dạng CSV: [`100_real_questions_clean_pii.csv`](100_real_questions_clean_pii.csv)

---

## 3. KẾT QUẢ BÀN GIAO 2: TỪ ĐIỂN VIẾT TẮT CRM & CHUẨN HÓA TRUY VẤN VN 01

- **Tệp bàn giao:** [`vn01_crm_dictionary.json`](vn01_crm_dictionary.json)
- **Nội dung:** Gồm **42 nhóm từ viết tắt CRM** (`kh`, `ck`, `hđ`, `cskh`, `cvkd`, `tpkd`, `gđcn`, `tgđ`, `bo`, `stock`...), **31 cụm từ tiếng Việt không dấu**, **16 thuật ngữ kỹ thuật song ngữ Anh - Việt** và **14 từ phủ định tiếng Việt bắt buộc bảo toàn** (`không`, `chưa`, `chẳng`, `miễn`, `ngoại trừ`, `cấm`, `từ chối`...).
- **Quy trình tích hợp:** P4 bàn giao tệp JSON định dạng mở cho `S3` (Yến Nhi) để S3 chủ động cập nhật vào module backend (`backend/src/modules/retrieval/models.py`) trên nhánh phát triển kỹ thuật của Supplier, bảo đảm P4 không can thiệp vào mã nguồn phần mềm.

---

## 4. BẢNG THEO DÕI TRẠNG THÁI KÝ NHẬN VÀ BÀN GIAO (ĐÃ NGHIỆM THU `DONE`)

| Vai trò | Thành viên | Nhiệm vụ đối soát | Trạng thái thực tế | Ghi chú theo dõi |
|---|---|---|:---:|---|
| **Lead bàn giao (P4)** | **Ngô Thị Trà My** | Hoàn tất dữ liệu 100 câu hỏi sạch PII & Từ điển VN 01 | **ĐÃ HOÀN TẤT BÀN GIAO** | Đồng bộ chuẩn `PAS-001..030` & `CF-001..010` |
| **Chủ sở hữu Bảo mật (P5)** | **Nguyễn Anh Khoa** | Thẩm định độc lập tiêu chí 0% PII (SEC 02/06) | **ĐÃ THẨM ĐỊNH (`0% PII`)** | CI Guard & PII Audit PASS 0 vi phạm |
| **Kiểm định Độc lập (S4)** | **Phạm Quý Hải** | Tiếp nhận 100 câu hỏi phục vụ đánh giá offline G1 | **ĐÃ TIẾP NHẬN** | Chuyển tiếp phân vùng tại `CKPA-67` |
| **Kỹ sư Truy xuất (S3)** | **Phạm Lương Yến Nhi** | Tiếp nhận Từ điển VN 01 tích hợp vào module retrieval | **ĐÃ TIẾP NHẬN TỪ ĐIỂN** | Tích hợp vào module chuẩn hóa truy vấn |
| **Chủ đầu tư / PO (P1)** | **Vắn Mỹ Vân** | Phê duyệt nghiệm thu Sub-task Cổng G1 (G1-AC07) | **ĐÃ NGHIỆM THU (`Done` 19/11/2026)** | Xem `governance/g1/sub-tasks/P1_CKPA55_BienBan_NghiemThu_100CauHoi_Va_TuDien_VN01.md` |

---

## 5. CAM KẾT HÀNG RÀO ĐỘC LẬP CHINESE WALL CHO CKPA-65 / CKPA-66

Thực hiện nghiêm túc cảnh báo về an toàn dữ liệu nghiệm thu:
1. **Đối với Đợt 1 (CKPA-55):** Bao gồm 60 ca DEV và 40 ca VAL là tập dữ liệu mở, phục vụ phát triển và tinh chỉnh mô hình.
2. **Đối với Đợt 2 (CKPA-65 / CKPA-66):** Bao gồm kho **100 Sealed Acceptance Cases**:
   - **CAM KẾT TUYỆT ĐỐI:** Không gửi cho các kỹ sư phát triển `S2`, `S3`, `S5` và **không bao giờ push nội dung câu hỏi/đáp án của 100 Sealed lên nhánh `develop` hoặc repo chung**.
   - Nội dung 100 Sealed chỉ được bàn giao trực tiếp, riêng biệt cho **[S4] Quý Hải** để nạp vào kho cách ly `sealed-eval-repo` theo đúng quy định RFP Mục 8 & Điều R10 của `rules.md`.
