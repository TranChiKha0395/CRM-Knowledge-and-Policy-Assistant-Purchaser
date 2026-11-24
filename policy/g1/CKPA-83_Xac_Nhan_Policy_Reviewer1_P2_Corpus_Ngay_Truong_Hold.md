# BIÊN BẢN XÁC NHẬN CHUYÊN MÔN CHÍNH SÁCH CỦA POLICY REVIEWER #1 (`P2`) VỀ CORPUS, NGÀY, TRƯỜNG & HOLD (`CKPA-83`)

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`SCRM` / `CKPA`)
- **Mã nhiệm vụ Jira:** `CKPA-83` — `[G1][Mục8] Reviewer #1 xác nhận Ngày, Trường & Hold`
- **Cổng nghiệm thu & Tiêu chí RFP:** `G1-AC01`, `G1-AC05`, `G1-AC06` | `Mục 8`, `Mục 9 (G1)`, `OPS 03`, `OPS 04`, `DAT 03`, `DAT 04`, `DAT 05`, `DAT 06`, `DAT 08`, `KNW 02`, `KNW 03`, `SEC 01`, `SEC 02`
- **Hồ sơ đầu vào đối chiếu:**
  1. `CKPA-58` (`CRM-G1-SUB10`): Báo cáo biên tập & bộ dữ liệu Full Corpus 3 Họ (`data/g1/full/*`)[cite: 8]
  2. `CKPA-62`: Biên bản thẩm định & phê duyệt Full Corpus 3 Họ và Đáp án chuẩn `OPS 03/04` (`policy/g1/CKPA-62_...md`)[cite: 9]
  3. `CKPA-82` (`CRM-G1-SUB28`): Biên bản & nhật ký kiểm lại 100% `source_uri`, `SHA-256` & `DAT 08` tại commit `42f9ecc` (`data/g1/reports/CKPA-82_...md`, `.log`)[cite: 6, 7]
  4. `CKPA-70`: Báo cáo kiểm toán RBAC, `source_ref`, Cache & Fail-Closed (`security/g1/CKPA-70_...md`, `.log`)[cite: 10, 11]
- **Người thực hiện & Ký xác nhận (`Policy Reviewer #1` / `Policy Owner`):** `[P2]` Trương Đình Hữu Tài (`Huutai12`)[cite: 9]
- **Người nghiệm thu (`Purchaser Sponsor` / `PO`):** `[P1]` Vắn Mỹ Vân (`vanvm26`)[cite: 9]
- **Phối hợp RACI:** `[P3]` Trần Chí Kha (`Knowledge and Data Steward`), `[S4]` Quý Hải[cite: 7]
- **Ngày xác nhận:** `2026-11-24` (Múi giờ `Asia/Ho_Chi_Minh`)
- **Phạm vi:** Base Scope thuần túy (`O1 = OFF`), `0%` PII thật[cite: 7, 8]

---

## 1. Mục tiêu & Phạm vi Rà soát của Policy Reviewer #1 (`P2`)
Thực hiện rà soát độc lập và ký xác nhận chuyên môn chính sách trước khi Purchaser Sponsor (`[P1]` Vắn Mỹ Vân) chốt nghiệm thu Gate G1, bao gồm 4 trụ cột bắt buộc:
1. **Toàn vẹn Corpus, `source_uri` & `DAT 08` (`SUB27` / `SUB28` — `G1-AC01`):** Đối chiếu hồ sơ nguồn `DEL 03` (`DOC-001..DOC-011`) và kết quả kiểm lại 100% liên kết tài liệu gốc `CKPA-82`[cite: 7].
2. **Quy tắc Ngày hiệu lực chi phối & Vòng đời (`OPS 03` / `KNW 03` — `G1-AC05`):** Kiểm tra logic phân giải phiên bản theo thời điểm `Asia/Ho_Chi_Minh` (`UTC+7`) và hành vi chặn/gắn nhãn trên 7 trạng thái vòng đời[cite: 9].
3. **6 Chiều ngữ cảnh & Trường trọng yếu (`DAT 04` / `OPS 04` — `G1-AC01`, `G1-AC05`):** Đối chiếu tính đầy đủ của 6 khóa `scope` và bộ đáp án biên toán tử số học trên toàn bộ 40 trường trọng yếu (`CF-001..CF-040`)[cite: 9].
4. **Cơ chế Conflict Hold, Quarantine Hold & Fail-Closed (`DAT 05` / `DAT 08` / `ANS 05–06` — `G1-AC06`):** Xác nhận đáp án chuẩn bắt buộc khi gặp xung đột hợp đồng/OEM, thiếu bảng biểu thiết yếu, mờ chứng từ hoặc viện dẫn tiền lệ `staff_note`[cite: 9].

---

## 2. Kết quả Đối chiếu & Xác nhận 4 Trụ cột Chuyên môn

### 2.1. Trụ cột 1 — Xác nhận Corpus, `source_uri` (`SUB28`) & Hồ sơ nguồn `DEL 03` (`SUB27`) (`G1-AC01`)
Qua đối chiếu trực tiếp `data/g1/reports/CKPA-82_Bien_Ban_Kiem_Lai_100pct_Source_URI_DAT08_Va_Ky_G1_AC01.md`, nhật ký `CKPA-82_source_uri_dat08_reverify.log` (commit `42f9ecc`) và `CKPA-58`[cite: 6, 7, 8]:
- **Danh mục tài liệu nguồn (`DEL 03` — `DOC-001..DOC-011`):** Đủ **11 / 30** tài liệu Base Scope, phủ trọn vẹn **3 họ chính sách** (`POL-001`: 4 tài liệu; `POL-002`: 3 tài liệu; `POL-003`: 4 tài liệu) và **5 / 5 lớp thẩm quyền `DAT 03`** (`policy`, `SOP`, `customer_contract`, `staff_note`, `manufacturer_terms`)[cite: 7, 8, 9].
- **Kiểm lại 100% `source_uri` & `SHA-256` (`Mục 9 G1 re-verified original reference access`):** Toàn bộ **136 / 136 bản ghi** trong `Source_URI_And_Checksum_Manifest_G1_Full.csv` (96 passages + 40 critical fields) và **56 / 56 bản ghi** Family 1 đều trỏ tới tệp tồn tại thực tế (`exists = true`), mở đọc trực tiếp thành công và khớp `0` sai lệch mã băm `SHA-256`[cite: 7, 8].
- **Kiểm soát bảng biểu & chú thích thiết yếu (`DAT 08`):** Cân bằng chính xác `96 = 93 Accepted (true) + 3 Quarantined (false)` đối với 3 ca kiểm thử thiếu chú thích bảng (`PAS-040`, `PAS-066`, `PAS-082`); toàn bộ `40 / 40` trường trọng yếu đạt `Accepted = true`[cite: 7, 8].
- **Nghiệm thu `CKPA-82` (`review-p2`):** Policy Owner `[P2]` xác nhận **ĐẠT (APPROVED)** đối với biên bản kiểm lại `CKPA-82` của `[P3]` Trần Chí Kha[cite: 7].

### 2.2. Trụ cột 2 — Xác nhận Quy tắc Ngày hiệu lực (`OPS 03`) & 7 Trạng thái Vòng đời (`KNW 03`) (`G1-AC05`)
Đối chiếu bộ đáp án chuẩn tại `CKPA-62` với phân bố dữ liệu trên `Policy_Corpus_G1_Full.csv` và `Critical_Fields_G1_Full.csv`[cite: 9]:
- **Múi giờ chuẩn (`Asia/Ho_Chi_Minh`, `UTC+7`):** Mọi mốc thời gian đều chuẩn hóa ISO-8601 `+07:00`[cite: 9]. Truy vấn không nêu ngày sự kiện bắt buộc lấy phiên bản `effective` hiện hành (`VER-001`, hiệu lực từ `2026-11-06T09:00:00+07:00`)[cite: 9].
- **Phân giải ranh giới lịch sử (`superseded`) & tương lai (`scheduled`):**
  - Sự kiện trước `2026-11-06T09:00:00+07:00` áp dụng `DOC00X-VER-000` (`superseded`: chiết khấu tiêu chuẩn `<= 3%`, hiệu lực báo giá `10 ngày`, ngưỡng pháp lý `< 300 triệu VND`, bảo hành Tuyến 1 `<= 22 kW`) kèm nhãn bắt buộc **`Hướng dẫn lịch sử`**[cite: 9].
  - Tuyệt đối không áp dụng phiên bản tương lai `VER-002` (`scheduled`, hiệu lực `2027-01-01T00:00:00+07:00`: `CF-019`, `CF-020`, `CF-029`, `CF-037`) cho các truy vấn năm 2026[cite: 9].
- **Chặn tuyệt đối 4 trạng thái chưa/ngừng hiệu lực (`Pre-Retrieval & Fail-Closed`):** Toàn bộ `withdrawn` (`3` passages, `2` critical fields), `draft` (`2` passages), `owner_reviewed` (`2` passages) và `approved` (`2` passages) bị chặn 100% ở lớp Pre-Retrieval và vô hiệu hóa cache cũ (`SEC 05`)[cite: 7, 9].

### 2.3. Trụ cột 3 — Xác nhận 6 Chiều Ngữ cảnh (`DAT 04`) & Trường Trọng yếu (`OPS 04`) (`G1-AC01`, `G1-AC05`)
- **6 Chiều ngữ cảnh bắt buộc (`DAT 04`):** `100%` (`136 / 136` bản ghi) khai báo đầy đủ 6 khóa `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope` theo định dạng `key:value;` chuẩn hóa, không thiếu chiều hoặc lệch từ khóa[cite: 9].
- **40 Trường trọng yếu (`CF-001..CF-040`) & Biên toán tử số học (`OPS 04`):** Đã kiểm tra và xác nhận tính nhất quán của toàn bộ ngưỡng định lượng và SLA trên 3 họ[cite: 9]:
  - **Họ 1 (`POL-001` — 16 fields):** Chiết khấu tiêu chuẩn `<= 5.0%` (`CF-001`, Sales Staff, SLA 2h); `5.0% < discount <= 15.0%` (`CF-002`, Sales Manager, SLA 4h); `discount > 15.0%` hoặc `order_value >= 1.000.000.000 VND` (`CF-003`, Sales Director, SLA 48h)[cite: 9].
  - **Họ 2 (`POL-002` — 13 fields):** Hợp đồng lũy kế `< 500.000.000 VND` (`CF-006`, CRM Staff, SLA 4h); `>= 500.000.000 VND` (`CF-007`, CRM Manager, SLA 4h)[cite: 9].
  - **Họ 3 (`POL-003` — 11 fields):** Động cơ thường `<= 37.0 kW` (`CF-009`, Tuyến 1 nội bộ); `> 37.0 kW` (`CF-010`, Tuyến 2 Hãng); động cơ phòng nổ `Ex-d` bắt buộc Tuyến 2 bất kể công suất (`CF-032`)[cite: 9].

### 2.4. Trụ cột 4 — Xác nhận Cơ chế Hold & Fail-Closed (`DAT 05`, `DAT 08`, `ANS 05–06`) (`G1-AC06`)
Xác nhận 4 kịch bản kích hoạt trạng thái **HOLD / Từ chối suy diễn (`Fail-Closed`)** đã được mã hóa đầy đủ trong bộ đáp án chuẩn[cite: 9]:
1. **Quarantine Hold do thiếu phụ lục/chú thích thiết yếu (`DAT 08`):** `PAS-040`, `PAS-066`, `PAS-082` bị cách ly ngay khi nạp; cấm suy đoán nội dung bảng thiếu[cite: 9].
2. **Conflict Hold do xung đột Hợp đồng / Điều khoản Hãng OEM (`DAT 05`):** Khi phát hiện mâu thuẫn giữa `DOC-006` (HĐ khung B2B), `DOC-008` (Phụ lục DPA) hoặc `DOC-010` (Hãng OEM `> 30 kW` vs `37 kW`) với `policy`, hệ thống **cấm tự suy diễn thứ bậc ưu tiên**, đặt trạng thái **HOLD**, trích dẫn song song các nguồn hợp lệ và chuyển phân xử đúng Policy Owner / Legal Owner[cite: 9].
3. **Evidence Hold do chứng từ mờ/rách/thiếu (`DAT 08`):** Khi thiếu hoặc mờ ĐKKD dấu đỏ (`PAS-020`) hoặc mờ tem Serial Nameplate / mất phiếu bảo hành (`PAS-026`, `PAS-091`, `CF-039`), giữ **HOLD** và lập Local Referral trong SLA `<= 8 giờ làm việc`[cite: 9].
4. **Từ chối suy luận tiền lệ từ `staff_note` / Khách VIP (`ANS 05` / `ANS 06`):** Khẳng định `DOC-007` và `DOC-011` (`staff_note`) không có hiệu lực ghi đè `policy`[cite: 9].

---

## 3. Ghi nhận Phạm vi Kiểm thử Độc lập & Ràng buộc Runtime (`No-Mock`)
- **Mức độ dữ liệu & đặc tả chính sách (`G1-AC01`, `G1-AC05`, `G1-AC06`):** Toàn bộ bộ dữ liệu Corpus (96 passages, 40 critical fields, 136 checksums), metadata phân quyền (`CKPA-70` Phần 1: `11/11` tài liệu hợp lệ) và bộ đáp án chuẩn `OPS 03/04` & `HOLD` đã được đối chiếu độc lập và đạt **100%**[cite: 7, 9, 11].
- **Lưu ý đối với kiểm thử Runtime API (`SUB01` / `SUB07`):** Theo ghi nhận trung thực tại `CKPA-70` (Phần 2), các bài kiểm thử gọi HTTP trực tiếp tới endpoint Staging (`POST /api/v1/answer/`, `/withdraw`) đang ở trạng thái chờ cấp `CKPA_BASE_URL` và token thật từ đội triển khai (tuân thủ chính sách `No-Mock`, tuyệt đối không dùng dữ liệu giả lập)[cite: 10, 11]. Ngay khi môi trường Staging được mở, bộ đáp án chuẩn đã chốt tại `CKPA-62` và biên bản này là căn cứ đối chiếu nghiệm thu chính thức[cite: 9, 11].

---

## 4. Kết luận Ký xác nhận của Policy Reviewer #1 (`P2`)

Tôi — **Trương Đình Hữu Tài** (`[P2]` Policy Owner / Policy Reviewer #1) — xác nhận đã hoàn tất rà soát độc lập toàn bộ hồ sơ `DEL 03` (`SUB27` / `CKPA-58`), kết quả kiểm lại `source_uri` (`SUB28` / `CKPA-82`), đáp án chuẩn `CKPA-62` và kiểm toán metadata `CKPA-70`; **ký xác nhận đạt các tiêu chí `G1-AC01`, `G1-AC05`, `G1-AC06`** về Corpus, Ngày hiệu lực, 6 Chiều ngữ cảnh, Trường trọng yếu và Cơ chế Hold, kính trình Purchaser Sponsor (`[P1]` Vắn Mỹ Vân) xem xét chốt nghiệm thu Gate G1[cite: 7, 8, 9, 11].

| Policy Reviewer #1 (`[P2]` — Policy Owner) | Xác nhận đối soát (`[P3]` — Steward) | Nghiệm thu Gate G1 (`[P1]` — Sponsor / PO) |
| :---: | :---: | :---: |
| *(Đã ký xác nhận)* | *(Đã đối chiếu `CKPA-58` / `CKPA-82`)* | *(Trình nghiệm thu trên Jira `CKPA-83`)* |
| **Trương Đình Hữu Tài** | **Trần Chí Kha** | **Vắn Mỹ Vân** |