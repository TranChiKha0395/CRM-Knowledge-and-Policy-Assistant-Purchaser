# BIÊN BẢN THẨM ĐỊNH & PHÊ DUYỆT CORPUS VÀ CRITICAL FIELDS HỌ 1 (`CRM-G1-SUB05`)

* **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`CKPA`)
* **Họ chính sách thẩm định:** Họ 1 — Quy trình Báo giá và Phê duyệt Thương mại (`POL-001`)
* **Mã công việc & Tiêu chí Gate:** `CRM-G1-SUB05` | **Mã Tiêu chí Cổng G1:** `G1-AC01`
* **Chi nhánh GitHub:** `policy/CKPA-51-approve-family1-corpus`
* **Mã truy xuất nguồn gốc RFP:** `DAT 03`, `DAT 06`, `KNW 03`, `Mục 9 (Gate G1)`
* **Người thẩm định & Ký duyệt (Policy Owner):** `[P2] Hữu Tài`
* **Cộng tác viên chuẩn bị dữ liệu (Steward):** `[P3] Chí Kha` (từ đầu ra `CRM-G1-SUB04`)
* **Người nghiệm thu (Purchaser Sponsor):** `[P1] Mỹ Vân`
* **Ngày phê duyệt:** `2026-11-20` (Múi giờ Việt Nam: `Asia/Ho_Chi_Minh`, `UTC+7`)

---

## 1. Kết quả Kiểm tra Toàn vẹn Schema & Đồng bộ Dữ liệu (`DAT 01`, `DAT 02`, `DAT 08`)

Dữ liệu đầu vào từ nhiệm vụ `CRM-G1-SUB04` gồm hai tệp CSV chuẩn UTF-8 đã được đối soát toàn diện với Hợp đồng Dữ liệu Gate G0 (`CKPA-15`) và Từ điển trường dữ liệu:

1. **Tệp `Policy_Corpus_Family1.csv` (`40` bản ghi — `21` cột chuẩn UTF-8):**
   * Khớp 100% tên cột và thứ tự với `passages_template.csv` (`CKPA-15`).
   * Độ dài nội dung lớn nhất đạt `591` ký tự Unicode (đạt chuẩn `<= 6.000` ký tự, không cắt cụt âm thầm).
   * Không phát hiện trùng lặp `passage_id` (`0` bản ghi lỗi).
   * **Chuẩn hóa thời gian múi giờ Việt Nam (`Asia/Ho_Chi_Minh`):** 100% giá trị tại các trường `recorded_at`, `published_at`, `effective_from`, `effective_to` tuân thủ nghiêm ngặt định dạng ISO 8601 (`+07:00`).
   * **Kiểm tra đính kèm thiết yếu (`DAT 08`):** `39/40` bản ghi có `has_essential_attachments = True`; riêng `PAS-040` (*Phụ lục B1 - Bảng chiết khấu bậc thang Đại lý Cấp 1*) được chủ đích gắn `has_essential_attachments = False` để làm dữ liệu kiểm thử kích hoạt `HOLD_DAT08` tại G1.

2. **Tệp `Critical_Fields_Family1.csv` (`16` bản ghi — `23` cột chuẩn UTF-8):**
   * Khớp 100% tên cột và thứ tự với `critical_fields_template.csv` (`CKPA-15`).
   * **Liên kết khóa ngoại (`Referential Integrity`):** 100% (`16/16`) dòng `field_id` trỏ đúng `passage_id`, khớp `document_version_id` và đồng nhất trạng thái `status` với bảng `Policy_Corpus_Family1.csv`.

---

## 2. Thẩm định Phân bổ Nguồn theo Ma trận Thẩm quyền 5 Lớp (`DAT 03` / `CKPA-8`)

Toàn bộ 40 đoạn tri thức của Họ 1 được phân định rạch ròi theo Ma trận Thẩm quyền 5 lớp nguồn đã ký duyệt tại Gate G0:

| Mã Tài liệu | Lớp Thẩm quyền (`CKPA-8`) | Dải `passage_id` | Số lượng | Mục đích & Trạng thái Kiểm soát |
| :--- | :--- | :--- | :---: | :--- |
| **`DOC-001`** | `policy` (Chính sách công ty) | `PAS-001..010`, `PAS-031..049` | **29** | Quy định gốc v1.0 (`VER-001`), lịch sử v0.9 (`VER-000`), tương lai v2.0 (`VER-002`), và các bản nháp/thu hồi (`KNW 03`). |
| **`DOC-004`** | `SOP` (Quy trình thao tác chuẩn) | `PAS-050..054` | **05** | Hướng dẫn 5 bước lập phiếu đề xuất chiết khấu trên CRM, khớp ngưỡng `DOC-001` và quy định Substitute Owner (`VN 04`). |
| **`DOC-006`** | `customer_contract` (Hợp đồng khung) | `PAS-055..057` | **03** | Tình huống mâu thuẫn với `DOC-001` (chiết khấu 12%, hiệu lực 30 ngày, tạm ứng 15%) để kiểm thử kích hoạt **`HOLD_DAT05`**. |
| **`DOC-007`** | `staff_note` (Ghi chú CRM cũ) | `PAS-058..060` | **03** | Tiền lệ ngoại lệ cũ (chiết khấu VIP 18%, miễn tạm ứng, giữ giá qua điện thoại) để kiểm thử quy tắc cấm suy luận **`ANS 05`**. |
| **TỔNG CỘNG** | **04 nhóm nguồn đại diện** | — | **40** | **Đạt 100% chuẩn cấu trúc phân lớp thẩm quyền `DAT 03`** |

---

## 3. Thẩm định Vòng đời 7 Trạng thái Xuất bản (`KNW 03`)

Toàn bộ **07 trạng thái xuất bản** theo chuẩn `KNW 03` đều đã được kiểm tra và đối chiếu logic thời gian hiệu lực chặt chẽ:

| STT | Trạng thái (`status`) | Số đoạn (`Passages`) | Số trường (`Critical Fields`) | Dải ID & Phiên bản áp dụng | Kết quả thẩm định `KNW 03` |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | `effective` | **31** | **10** | `PAS-001..010`, `031..040`, `050..060` (`VER-001`, `DOC004/006/007-VER-001`) | **Đạt:** Có đủ `approver`, `published_at` và `effective_from = 2026-11-06T09:00:00+07:00`. |
| **2** | `superseded` | **03** | **03** | `PAS-041..043` / `CF-016..018` (`DOC001-VER-000`) | **Đạt:** Có `effective_to = 2026-11-06T08:59:59+07:00`, nối chuỗi thay thế bởi `VER-001` (`supersedes = DOC001-VER-000`). |
| **3** | `scheduled` | **02** | **02** | `PAS-044..045` / `CF-019..020` (`DOC001-VER-002`) | **Đạt:** Có `effective_from = 2027-01-01T00:00:00+07:00` (tương lai), chặn dùng cho giao dịch năm 2026. |
| **4** | `draft` | **01** | **00** | `PAS-046` (`DOC001-VER-003-DRAFT`) | **Đạt:** `approver` và `published_at` để trống đúng quy trình chưa duyệt; bị chặn bởi Pre-retrieval filter. |
| **5** | `owner_reviewed` | **01** | **00** | `PAS-047` (`DOC001-VER-001-REV`) | **Đạt:** Đã rà soát sơ bộ nhưng chưa ký duyệt/công bố (`approver = null`, `published_at = null`). |
| **6** | `approved` | **01** | **00** | `PAS-048` (`DOC001-VER-001-APP`) | **Đạt:** Đã có chữ ký duyệt (`Sponsor / Legal & Compliance Director`) nhưng chưa công bố (`published_at = null`), chưa có hiệu lực hiện hành. |
| **7** | `withdrawn` | **01** | **01** | `PAS-049` / `CF-022` (`DOC001-VER-001-WD`) | **Đạt:** Đã thu hồi khẩn từ `2026-10-15T14:00:00+07:00`; bắt buộc chặn tuyệt đối và không dùng lại từ cache (`SEC 05`). |

---

## 4. Thẩm định Bảng Trường Trọng Yếu Số học & Tiền tệ (`DAT 06`)

Đã đối soát **16/16 dòng** trong `Critical_Fields_Family1.csv` với văn bản điều khoản gốc trong `Policy_Corpus_Family1.csv`:

| Mã trường (`field_id`) | Tham chiếu gốc (`source_clause`) | Kiểu & Toán tử | Giá trị & Đơn vị/Tiền tệ | Vai trò phê duyệt (`approval_role`) | Trạng thái | Đối soát |
| :--- | :--- | :--- | :--- | :--- | :---: | :---: |
| **`CF-001`** | Điều 2.1 (`PAS-004`) | `number` (`<=`) | `5` `%` | `Sales Staff (reader)` | `effective` | Khớp 100% |
| **`CF-002`** | Điều 2.2 (`PAS-005`) | `number` (`between`) | `5;15` `%` | `Sales Manager` | `effective` | Khớp 100% |
| **`CF-003`** | Điều 2.3–2.5 (`PAS-006`) | `currency` (`>=`) | `1000000000` `VND` | `Sales Director` | `effective` | Khớp 100% |
| **`CF-004`** | Điều 1.2–1.3 (`PAS-002`) | `duration` (`<=`) | `15` `ngày làm việc` | `Sales Staff (reader)` | `effective` | Khớp 100% |
| **`CF-011`** | Phụ lục A1 (`PAS-031`) | `number` (`between`) | `5;10` `%` (Động cơ 3 pha `>= 20` bộ) | `Sales Manager` | `effective` | Khớp 100% |
| **`CF-012`** | Phụ lục A2 (`PAS-032`) | `number` (`<=`) | `3` `%` (Động cơ phòng nổ Ex-d) | `Sales Staff (reader)` | `effective` | Khớp 100% |
| **`CF-013`** | Phụ lục A3 (`PAS-033`) | `number` (`between`) | `5;12` `%` (Biến tần trung thế) | `Sales Manager` | `effective` | Khớp 100% |
| **`CF-014`** | Điều 4.1 (`PAS-035`) | `number` (`>=`) | `30` `%` (Tạm ứng đơn nhập khẩu) | `Sales Staff (reader)` | `effective` | Khớp 100% |
| **`CF-015`** | Điều 5.1 (`PAS-039`) | `number` (`>=`) | `18` `%` (Sàn Gross Margin — *Hạn chế quyền*) | `Sales Manager` | `effective` | Khớp 100% |
| **`CF-016`** | Điều 2.1 v0.9 (`PAS-041`) | `number` (`<=`) | `3` `%` | `Sales Staff (reader)` | `superseded` | Khớp 100% |
| **`CF-017`** | Điều 2.2 v0.9 (`PAS-041`) | `number` (`between`) | `3;10` `%` | `Sales Manager` | `superseded` | Khớp 100% |
| **`CF-018`** | Điều 1.2 v0.9 (`PAS-042`) | `duration` (`<=`) | `10` `ngày làm việc` | `Sales Staff (reader)` | `superseded` | Khớp 100% |
| **`CF-019`** | Điều 2.3 v2.0 (`PAS-044`) | `currency` (`>=`) | `1500000000` `VND` | `Sales Director` | `scheduled` | Khớp 100% |
| **`CF-020`** | Điều 1.2 v2.0 (`PAS-045`) | `duration` (`<=`) | `20` `ngày làm việc` | `Sales Staff (reader)` | `scheduled` | Khớp 100% |
| **`CF-021`** | Điều 4.2 (`PAS-036`) | `number` (`>`) | `3` `%` (Biến động tỷ giá gia hạn) | `Sales Manager` | `effective` | Khớp 100% |
| **`CF-022`** | Khuyến mãi cũ (`PAS-049`) | `number` (`<=`) | `8` `%` | `Sales Staff (reader)` | `withdrawn` | Khớp 100% |

*(Lưu ý kiểm soát bảo mật `SEC 01`: Bản ghi `PAS-039` và `CF-015` quy định sàn biên lợi nhuận gộp `18%` đã được giới hạn trường `audience = policy_owner,steward,administrator`, loại trừ `reader` đúng nguyên tắc phân quyền tối thiểu.)*

---

## 5. Xác nhận Phê duyệt Cổng G1 (`Policy Owner Sign-off — G1-AC01`)

Tôi, **`[P2] Hữu Tài`** — Chủ sở hữu Chính sách (*Policy Owner — Họ 1: Báo giá và Phê duyệt Thương mại*), xác nhận đã thẩm định toàn bộ **40 đoạn nội dung (`Policy_Corpus_Family1.csv`)** và **16 dòng trường trọng yếu (`Critical_Fields_Family1.csv`)** từ nhiệm vụ `CRM-G1-SUB04`:

* **Tình trạng dữ liệu:** `100%` bản ghi (`40/40` passages và `16/16` critical fields) đã được xác nhận đúng nội dung nghiệp vụ, đủ 7 trạng thái vòng đời (`KNW 03`), chính xác ngưỡng số học/tiền tệ (`DAT 06`) và có thông tin `owner = Commercial Policy Owner (Sales Director)`.
* **Quyết định:** **PHÊ DUYỆT (APPROVED)** cho phép `[P3] Chí Kha` và `[S2] Quốc Hưng` nạp bộ dữ liệu Họ 1 này vào môi trường kiểm thử Gate G1.

| CỘNG TÁC VIÊN DỮ LIỆU (`Knowledge & Data Steward`) | CHỦ SỞ HỮU CHÍNH SÁCH (`Policy Owner — Phê duyệt chính`) | NHÀ TÀI TRỢ DỰ ÁN (`Purchaser Sponsor — Nghiệm thu`) |
| :---: | :---: | :---: |
| **[Đã đối soát chuẩn CSV]** | **[ĐÃ KÝ PHÊ DUYỆT — APPROVED]** | **[Xác nhận tiếp nhận cổng `G1-AC01`]** |
| **`[P3] Chí Kha`** | **`[P2] Hữu Tài`** | **`[P1] Mỹ Vân`** |
| Ngày: `2026-11-20` | Ngày: `2026-11-20` | Ngày: `2026-11-20` |