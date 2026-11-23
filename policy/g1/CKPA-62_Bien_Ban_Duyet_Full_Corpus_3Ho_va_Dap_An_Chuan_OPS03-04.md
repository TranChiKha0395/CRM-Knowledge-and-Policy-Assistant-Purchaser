# BIÊN BẢN THẨM ĐỊNH & PHÊ DUYỆT FULL CORPUS 3 HỌ CHÍNH SÁCH & ĐÁP ÁN CHUẨN OPS 03/04 (`CKPA-62`)

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`SCRM` / `CKPA`)
- **Mã nhiệm vụ Jira:** `CKPA-62` — `[G1][DAT04] Duyệt Họ 2-3, 6 chiều chuẩn & Hold`
- **Cổng nghiệm thu & Tiêu chí RFP:** `G1-AC01` | `DAT 03`, `DAT 04`, `DAT 05`, `DAT 06`, `DAT 08`, `KNW 03`, `OPS 03`, `OPS 04`, `SEC 01`, `SEC 02`, `Annex C`
- **Dữ liệu đầu vào đối chiếu:** Gói bàn giao `CKPA-58` (`CRM-G1-SUB10`) từ `[P3]` Trần Chí Kha (`2026-11-22 05:30 +07:00`)
- **Người thẩm định & Ký duyệt (Policy Owner):** `[P2]` Trương Đình Hữu Tài (`Huutai12`)
- **Người nghiệm thu (Purchaser Sponsor / PO):** `[P1]` Vắn Mỹ Vân (`vanvm26`)
- **Ngày thẩm định & Phê duyệt:** `2026-11-23` (`Asia/Ho_Chi_Minh`)
- **Kết luận phê duyệt:** **ĐẠT CHUẨN 100% (APPROVED — PASSED)**

---

## 1. TỔNG HỢP KẾT QUẢ THẨM ĐỊNH QUY MÔ FULL CORPUS 3 HỌ (`DAT 03` / `DAT 06` / `DAT 08`)

Đã đối chiếu 100% bản ghi trên 3 tệp dữ liệu chuẩn (`Policy_Corpus_G1_Full.csv`, `Critical_Fields_G1_Full.csv`, `Source_URI_And_Checksum_Manifest_G1_Full.csv`) với 11 tài liệu nguồn (`DOC-001..DOC-011`):

| Hạng mục kiểm định | Họ 1 (`POL-001`) | Họ 2 (`POL-002`) | Họ 3 (`POL-003`) | Tổng cộng Full 3 Họ | Trần / Tiêu chuẩn RFP | Kết quả |
|---|---:|---:|---:|---:|---|---|
| **Tài liệu nguồn (`DOC-001..011`)** | 4 (`DOC-001,004,006,007`) | 3 (`DOC-002,005,008`) | 4 (`DOC-003,009,010,011`) | **11 tài liệu** | `<= 30` tài liệu | **PASS** |
| **Passages (`Policy_Corpus_G1_Full.csv`)** | 40 (`39 Accepted + 1 Quarantined`) | 28 (`27 Accepted + 1 Quarantined`) | 28 (`27 Accepted + 1 Quarantined`) | **96 passages** (`93 Accepted + 3 Quarantined`) | `<= 300` passages (`21` cột UTF-8) | **PASS** |
| **Critical Fields (`Critical_Fields_G1_Full.csv`)** | 16 (`CF-001..004, 011..022`) | 13 (`CF-005..008, 023..031`) | 11 (`CF-009..010, 032..040`) | **40 critical fields** (`100% Accepted`) | `<= 50` fields (`23` cột UTF-8) | **PASS** |
| **SHA-256 & `source_uri` Manifest** | 56 | 41 | 39 | **136 / 136 bản ghi** | `= 96 + 40`, `exists=true`, `0` mismatch | **PASS** |
| **Bản ghi hạn chế quyền (`SEC 01`)** | 4 (`PAS-039,046,047`, `CF-015`) | 3 (`PAS-065,070`, `CF-027`) | 3 (`PAS-083,088`, `CF-035`) | **10 bản ghi** (không có `reader`) | `>= 1` (kiểm thử Pre-Retrieval RBAC) | **PASS** |
| **Quét PII thật & Base Scope** | 0 PII / `O1 = OFF` | 0 PII / `O1 = OFF` | 0 PII / `O1 = OFF` | **0 hits / 100% Base Scope** | `0` PII (`SEC 02` / `SEC 06`) | **PASS** |

---

## 2. ĐỐI CHIẾU 6 CHIỀU NGỮ CẢNH CHUẨN (`DAT 04`) TRÊN 100% BẢN GHI

Toàn bộ **96/96 passages** và **40/40 critical fields** (tổng **136/136 bản ghi**) đều được cấu trúc chuẩn theo định dạng `key:value` ngăn cách bởi dấu `;` với đầy đủ **6/6 chiều ngữ cảnh** bắt buộc của `DAT 04` (không có bản ghi nào thiếu chiều hoặc sai khóa):

| STT | Tên chiều (`DAT 04`) | Khóa cột `scope` | Giá trị chuẩn hóa trên `Policy_Corpus_G1_Full.csv` (96 dòng) | Giá trị chuẩn hóa trên `Critical_Fields_G1_Full.csv` (40 dòng) | Đánh giá |
|---:|---|---|---|---|---|
| 1 | **Công ty (Company)** | `company` | `SN` (96/96) | `SN` (40/40) | **Đạt 100%** |
| 2 | **Chi nhánh (Branch)** | `branch` | `all` (93), `HN,DN,HCM` (3) | `all` (40/40) | **Đạt 100%** |
| 3 | **Vai trò (Role)** | `role` | `sales` (39), `crm` (27), `cskh` (27), `sales_manager` (1), `crm_admin` (1), `service_manager` (1) | `sales` (15), `crm` (12), `cskh` (10), `sales_manager` (1), `crm_admin` (1), `service_manager` (1) | **Đạt 100%** |
| 4 | **Nhóm khách hàng (Customer Category)** | `customer_group` | `b2b` (88), `b2b_key_account` (5), `factory_project` (2), `distributor_tier1` (1) | `b2b` (40/40) | **Đạt 100%** |
| 5 | **Sản phẩm (Product)** | `product` | `industrial` (55), `all` (28), `mv_inverter` (6), `motor_3phase` (3), `explosion_proof_motor` (2), `gearbox` (1), `spare_parts` (1) | `industrial` (22), `all` (13), `explosion_proof_motor` (2), `mv_inverter` (2), `motor_3phase` (1) | **Đạt 100%** |
| 6 | **Phạm vi giao dịch (Transaction Scope)** | `transaction_scope` | 61 giá trị chuyên biệt theo nghiệp vụ (ví dụ: `standard_quotation`, `contract_conflict`, `tier1_internal_routing`, `oem_contract_conflict`, `missing_serial_or_card_hold`...) | 27 giá trị chuyên biệt khớp 1-1 với các điều kiện ngưỡng `CF-001..CF-040` | **Đạt 100%** |

---

## 3. KIỂM ĐỊNH 7 TRẠNG THÁI VÒNG ĐỜI (`KNW 03`) & QUY TẮC NGÀY HIỆU LỰC (`OPS 03` / `OPS 04`)

### 3.1. Phân bổ 7 trạng thái vòng đời (`KNW 03`)

| Trạng thái (`status`) | Passages (`96`) | Critical Fields (`40`) | Quy tắc hành vi bắt buộc của hệ thống (`OPS 03` / `ANS 02` / `SEC 05`) |
|---|---:|---:|---|
| **`effective`** | 78 (`75 Accepted + 3 Quarantined`) | 29 | **Được phép phục vụ hiện hành** nếu `effective_from <= now(Asia/Ho_Chi_Minh) <= effective_to` (hoặc `effective_to` rỗng) và `has_essential_attachments = true`. |
| **`superseded`** | 5 (`PAS-041..043, 067, 085`) | 5 (`CF-016..018, 028, 036`) | **Chặn mặc định** cho câu hỏi hiện hành. Chỉ dùng khi truy vấn có ngày sự kiện lịch sử thuộc `[effective_from, effective_to]` và **bắt buộc gắn nhãn `'Hướng dẫn lịch sử'`**. |
| **`scheduled`** | 4 (`PAS-044, 045, 068, 086`) | 4 (`CF-019, 020, 029, 037`) | **Cấm áp dụng trước `effective_from`** (`2027-01-01T00:00:00+07:00`). Chỉ hiển thị khi hỏi rõ quy định 2027 kèm nhãn `'Hướng dẫn tương lai — Chưa có hiệu lực'`. |
| **`withdrawn`** | 3 (`PAS-049, 069, 087`) | 2 (`CF-022, 030`) | **Chặn tuyệt đối (`Fail-Closed`)** và vô hiệu hóa cache cũ (`SEC 05` / `KNW 04`); cấm phục vụ cho cả truy vấn hiện hành lẫn lịch sử. |
| **`draft`** | 2 (`PAS-046, 070`) | 0 | **Chặn 100% ở lớp Pre-Retrieval**; không bao giờ dùng làm căn cứ trả lời. |
| **`owner_reviewed`** | 2 (`PAS-047, 088`) | 0 | **Chặn 100% ở lớp Pre-Retrieval** (mới rà soát, chưa ký duyệt phát hành). |
| **`approved`** | 2 (`PAS-048, 078`) | 0 | **Chặn 100% ở lớp Pre-Retrieval** (đã ký nhưng chưa đến lịch phát hành `effective`). |

### 3.2. Bộ đáp án chuẩn kiểm thử biên ngày & ngưỡng số học (`OPS 03` / `OPS 04`)

1. **Quy tắc múi giờ & Ngày chi phối (`OPS 03` — `Asia/Ho_Chi_Minh`, `UTC+7`):**
   - **Câu hỏi quy trình chung (không nêu ngày giao dịch):** Bắt buộc lấy phiên bản `effective` tại thời điểm hiện tại (`2026-11-23 +07:00` $\rightarrow$ dùng `VER-001` có hiệu lực từ `2026-11-06T09:00:00+07:00`).
   - **Mốc chuyển giao phiên bản `v0.9` $\rightarrow$ `VER-001` (`2026-11-06 09:00:00 +07:00`):**
     - Giao dịch phát sinh lúc `2026-11-06 08:59:59 +07:00` $\rightarrow$ Áp dụng `DOC00X-VER-000` (`superseded`: chiết khấu tiêu chuẩn `<= 3%`, hiệu lực báo giá `10 ngày`, ngưỡng pháp lý `< 300 triệu VND`, bảo hành Tuyến 1 `<= 22 kW`) + gắn nhãn **`Hướng dẫn lịch sử`**.
     - Giao dịch phát sinh từ `2026-11-06 09:00:00 +07:00` $\rightarrow$ Áp dụng `VER-001` (`effective`: chiết khấu tiêu chuẩn `<= 5%`, hiệu lực báo giá `15 ngày`, ngưỡng pháp lý `< 500 triệu VND`, bảo hành Tuyến 1 `<= 37 kW`).
   - **Mốc lên lịch tương lai `VER-002` (`2027-01-01 00:00:00 +07:00`):** Mọi truy vấn năm 2026 tuyệt đối không dùng `CF-019` (`1,5 tỷ VND`), `CF-020` (`20 ngày`), `CF-029` (`1 giờ`), `CF-037` (`<= 45 kW`).

2. **Quy tắc kiểm thử biên toán tử nghiêm ngặt (`OPS 04` — `<`, `<=`, `=`, `>=`, `>`, `between`):**
   - **Họ 1 — Chiết khấu & Đơn hàng (`CF-001..003`):**
     - `discount = 5.0%` (đơn `< 500 triệu`): Thuộc `<= 5%` (`CF-001`) $\rightarrow$ `Sales Staff` tự duyệt (2h).
     - `discount = 5.01%` hoặc `15.0%`: Thuộc `between 5;15` (`5% < discount <= 15%`, `CF-002`) $\rightarrow$ `Sales Manager` duyệt (4h).
     - `discount = 15.01%` hoặc `order_value = 1.000.000.000 VND`: Thuộc `>= 1.000.000.000 VND` / `> 15%` (`CF-003`) $\rightarrow$ `Sales Director` duyệt (48h).
   - **Họ 2 — Ngưỡng pháp lý KH trọng yếu (`CF-006`, `CF-007`):**
     - `cumulative_contract = 499.999.999 VND` (`< 500.000.000 VND`, `CF-006`) $\rightarrow$ `CRM Staff` xử lý (4h).
     - `cumulative_contract = 500.000.000 VND` (`>= 500.000.000 VND`, `CF-007`) $\rightarrow$ Bắt buộc trình `CRM Manager` phê duyệt (4h).
   - **Họ 3 — Công suất định tuyến bảo hành (`CF-009`, `CF-010`, `CF-032`):**
     - Động cơ thường `37.0 kW` (`<= 37 kW`, `CF-009`) $\rightarrow$ Tuyến 1 nội bộ (`Internal Tech Lead`).
     - Động cơ thường `37.1 kW` (`> 37 kW`, `CF-010`) $\rightarrow$ Tuyến 2 giám định Hãng (`Vendor Chief Engineer`).
     - Động cơ phòng nổ `Ex-d` công suất `15 kW` (`<= 37 kW` nhưng thuộc `CF-032`) $\rightarrow$ **Bắt buộc Tuyến 2 (`Vendor Chief Engineer`)** bất kể công suất.

---

## 4. CHỐT ĐÁP ÁN CHUẨN CHO TOÀN BỘ CÁC CA HOLD (`DAT 05` / `DAT 08` / `ANS 05` / `ANS 06`)

Policy Owner P2 phê duyệt bộ đáp án chuẩn bắt buộc cho **04 nhóm ca HOLD** trên toàn bộ 3 họ chính sách:

| Nhóm Ca HOLD | Mã căn cứ (`Passage` / `DOC`) | Điều kiện kích hoạt HOLD | Đáp án chuẩn bắt buộc của hệ thống (`Fail-Closed`) | Người / Vai trò nhận chuyển xử lý (`Escalation / Referral`) |
|---|---|---|---|---|
| **1. Quarantine / Hold do thiếu bảng biểu hoặc chú thích thiết yếu (`DAT 08`)** | • Họ 1: `PAS-040` (`DOC-001` Phụ lục B1)<br>• Họ 2: `PAS-066` (`DOC-002` Phụ lục B2)<br>• Họ 3: `PAS-082` (`DOC-003` Phụ lục B3)<br>• Tổng quát: `PAS-010` | `has_essential_attachments = false` (thiếu bảng chú thích loại trừ, bảng allowlist hoặc danh mục linh kiện hao mòn). | Cách ly bản ghi vào **Quarantine** ngay khi nạp; tạm giữ (**HOLD**) hướng dẫn đối với ngưỡng bị ảnh hưởng, **cấm suy đoán** nội dung bảng thiếu cho tới khi bổ sung đủ. | `Policy Steward` (`[P3]` Chí Kha) bổ sung phụ lục & `Policy Owner` (`[P2]` Hữu Tài) duyệt lại. |
| **2. Conflict Hold do mâu thuẫn giữa Hợp đồng / Hãng OEM và Chính sách công ty (`DAT 05`)** | • Họ 1: `PAS-008`, `PAS-055..057` (`DOC-006` HĐ khung B2B: CK 12%, hiệu lực 30 ngày, tạm ứng 15%)<br>• Họ 2: `PAS-018`, `PAS-075..076` (`DOC-008` Phụ lục DPA: xóa dữ liệu 15 ngày, email không dấu đỏ)<br>• Họ 3: `PAS-028`, `PAS-093` (`DOC-010` Hãng OEM `> 30 kW` vs `37 kW` `DOC-003`, `CF-040`) | Phát hiện xung đột điều khoản giữa `customer_contract` hoặc `manufacturer_terms` với `policy` (`DOC-001..003`). | **Cấm tự suy diễn thứ bậc ưu tiên** và **cấm mặc định văn bản mới nhất thắng**. Đặt trạng thái **HOLD**, trích dẫn song song các nguồn hợp lệ đang mâu thuẫn và chuyển phân xử. | • Họ 1: `Commercial Policy Owner` (+ `Legal` nếu điều khoản tạm ứng)<br>• Họ 2: `CRM Data Governance Owner` + `Legal Owner`<br>• Họ 3: `Warranty Policy Owner` |
| **3. Evidence / Document Hold do thiếu hoặc mờ chứng từ cốt lõi (`DAT 08` / `VN 04`)** | • Họ 2: `PAS-020` (`DOC-002` scan ĐKKD / Thông báo dấu đỏ bị mờ, mất góc, thiếu trang)<br>• Họ 3: `PAS-026`, `PAS-091` (`DOC-003` / `DOC-009` mờ/rách tem Serial Nameplate hoặc mất Phiếu bảo hành, `CF-039`) | Chứng từ xác minh khách hàng hoặc tem thiết bị bị mờ/rách/thiếu trang không đủ căn cứ đối chiếu. | Giữ hồ sơ ở trạng thái **HOLD**; không tự tiếp nhận hoặc suy đoán thông số; yêu cầu bổ sung bản rõ nét hoặc lập **Local Referral** trong SLA `<= 8 giờ làm việc` (`CF-039`). | • Họ 2: `CRM Data Governance Owner`<br>• Họ 3: `Warranty Policy Owner` (hoặc `Substitute Owner` — Phó GĐ Dịch vụ khi vắng mặt) + `Internal Tech Lead` |
| **4. Cấm suy luận tiền lệ từ Ghi chú CRM cũ / Khách VIP (`ANS 05` / `ANS 06`)** | • Họ 1: `PAS-058..060` (`DOC-007` `staff_note` tiền lệ CK 18%, miễn tạm ứng, giữ giá 45 ngày qua điện thoại)<br>• Họ 2: `PAS-018` (đề nghị miễn ĐKKD cho khách VIP)<br>• Họ 3: `PAS-095..096` (`DOC-011` `staff_note` tiền lệ miễn Phiếu BH 2025) | Truy vấn viện dẫn ghi chú CRM cũ (`staff_note`) hoặc trạng thái khách VIP để xin bỏ qua quy định hiện hành. | **Từ chối suy luận tiền lệ (`ANS 05` / `ANS 06`)**: khẳng định `staff_note` không có hiệu lực ghi đè `policy`; yêu cầu thực hiện đúng quy trình chuẩn hoặc đặt **HOLD** trình ngoại lệ chính thức. | Trình cấp thẩm quyền phê duyệt ngoại lệ tương ứng (`Sales Director` / `CRM Manager` / `Warranty Policy Owner`). |

---

## 5. XÁC NHẬN KÝ DUYỆT CỦA POLICY OWNER (`P2`)

Tôi xác nhận đã thẩm định độc lập toàn bộ **96 passages**, **40 critical fields**, **136 SHA-256 checksums** của Full Corpus 3 Họ chính sách (`POL-001`, `POL-002`, `POL-003`) từ gói bàn giao `CKPA-58`; xác nhận tuân thủ đầy đủ 6 chiều ngữ cảnh `DAT 04`, 7 trạng thái vòng đời `KNW 03`, quy tắc biên ngày/ngưỡng `OPS 03/04` và bộ đáp án chuẩn `HOLD` nêu trên.

- **Trạng thái phê duyệt:** **KÝ DUYỆT CHÍNH THỨC (SIGNED-OFF)**
- **Bàn giao tiếp theo:** Mở khóa cho `[S2]` Quốc Hưng (`CKPA-59`), `[S5]` Ngọc Duy (`CKPA-60`) nạp dữ liệu vào hệ thống đối soát & benchmark `OPS 01`, và trình `[P1]` Vắn Mỹ Vân nghiệm thu Cổng `G1-AC01`.

| Đại diện Thẩm định & Phê duyệt (`P2` — Policy Owner) | Đại diện Nghiệm thu (`P1` — Purchaser Sponsor) |
| :---: | :---: |
| *(Đã ký xác nhận)* | *(Chờ nghiệm thu trên Jira `CKPA-62`)* |
| **Trương Đình Hữu Tài** | **Vắn Mỹ Vân** |