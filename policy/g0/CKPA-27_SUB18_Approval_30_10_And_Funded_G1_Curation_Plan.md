> **TRẠNG THÁI:** ĐÃ THẨM ĐỊNH & PHÊ DUYỆT TẠI CỔNG GATE G0 (`DONE` — `20/11/2026`, đồng bộ Quyết định Cổng G0 `CKPA-40`/`42`).

# BIÊN BẢN THẨM ĐỊNH, PHÊ DUYỆT BỘ MẪU `30` ĐOẠN TRI THỨC + `10` TRƯỜNG TRỌNG YẾU & KẾ HOẠCH CURATION G1 CÓ NGÂN SÁCH (`DEL01-C`)

- **Đơn vị chủ đầu tư:** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật *(chờ `[P1]` / Legal Owner xác nhận chính thức theo Giấy chứng nhận ĐKKD)*
- **Dự án:** CRM Knowledge & Policy Assistant (`CKPA`)
- **Mã công việc Jira:** Sub-task `CKPA-27` (`CRM-G0-SUB18` — tổng hợp nghiệm thu Story `CKPA-24` / `CRM-G0-ST06` gồm `CKPA-25`, `CKPA-26`, `CKPA-27`; thuộc Epic `CKPA-3` / `CRM-G0-EP01`)
- **Tiêu chí Cổng G0:** `G0-AC03` (`DEL01-C`)
- **Truy vết RFP:** Mục 2 (G0 readiness & hard caps), `DAT 01`, `DAT 06`, `DAT 08`, `KNW 03`, Mục 9 (Gate G0), Mục 11 (Ten roles & Policy Accountability), Mục 14 (Source readiness), `VN 03`, `VN 04`, `VN 06`
- **Chủ trì thẩm định (Assignee):** `[P2]` Hữu Tài (`Policy owners / Policy Reviewer #1`)
- **Người nghiệm thu (Reporter — đảm bảo `Assignee != Reporter`):** `[P1]` Vắn Mỹ Vân (`Purchaser sponsor / Product Owner`)
- **Phối hợp (RACI):** `[P3]` Trần Chí Kha (`Knowledge and data steward / Policy Reviewer #2`), `[S2]` Trần Quốc Hưng (`Integration engineer` — bằng chứng dry-run `CKPA-26`), `[S4]` Phạm Quý Hải (`Quality lead` — đối soát độc lập với bộ `60 dev_60`), `[P5]` Nguyễn Anh Khoa (thẩm định pháp lý nguồn `SRC-005`)
- **Giai đoạn / Múi giờ chuẩn:** Sprint 2 — G0 Discovery Tuần 2 (`18/11/2026`), múi giờ `Asia/Ho_Chi_Minh` (`UTC+7`)

---

## 1. Neo Truy vết Bằng chứng Kỹ thuật & Mã băm `SHA-256` Đã Xác minh (`CKPA-25` & `CKPA-26`)

Biên bản thẩm định này tham chiếu trực tiếp và khóa cứng tới đúng phiên bản byte của **03 tệp CSV** do `[P3]` Trần Chí Kha biên tập tại `CKPA-25` và đã vượt qua `100%` bài kiểm tra dry-run không ghi DB (`0` lỗi, `0` quarantined, `0` rejected) của `[S2]` Trần Quốc Hưng tại `CKPA-26`:

| Tệp nguồn được thẩm định (`CKPA-25`) | Mã lô kiểm tra (`CKPA-26`) | Số dòng / Số cột | Dung lượng (`bytes`) | Mã băm thực tế `SHA-256` (`64-hex`) | Trạng thái kỹ thuật |
|---|---|---|---:|---|---|
| `data/g0/passages.csv` | `DRYRUN-G0-20261117-001` | `30` đoạn / `21` cột | `35496` | `3362b3181a53ae6a7cd421ab59b7fc351e8e9b83631fc27dc75f1030e05d3593` | `APPROVED_AT_G0` (`max=591 <= 6.000` ký tự, đủ `6dim`) |
| `data/g0/critical_fields.csv` | `DRYRUN-G0-20261117-002` | `10` trường / `23` cột | `8244` | `33c3a0a6f5ce7f8b9ad0e1761693ea1803fcee2cb556f4474e2f14f3b3a56c2d` | `APPROVED_AT_G0` (`3/3 currency=VND`, đủ `6dim`) |
| `data/g0/CKPA-2_01_Source_Registry_And_Gap_Analysis.csv` | `DRYRUN-G0-20261117-003` | `7` nguồn / `20` cột | `5413` | `43adce3a8c33df678fa2912841bb8ec557de0048edf26d37600951f14a89cf81` | `APPROVED_AT_G0` (`G0=30/10`, `G1=300/50`) |

> **Nguyên tắc trách nhiệm nguồn chính sách (Mục 11 & Thương mại RFP):** Quyền công bố nguồn tri thức và trách nhiệm giải trình nội dung quy định thuộc hoàn toàn về các Chủ sở hữu chính sách được ủy quyền phía **Công ty Cổ phần Thiết bị Công nghiệp Song Nhật** (`[P2]` và `[P1]`). Bộ CSV mẫu sử dụng giá trị `status = effective` để kiểm chứng hợp đồng nạp dry-run `KNW 03`; việc kích hoạt phục vụ người dùng thực tế chỉ được phép sau khi có chữ ký phê duyệt chính thức tại Cổng G0 và nghiệm thu Cổng G1.

---

## 2. Kết quả Thẩm định Nội dung `30` Đoạn Tri thức (`PAS-001..030`) & `10` Trường Trọng yếu (`CF-001..010`)

### 2.1 Tổng hợp Đối soát Theo 03 Họ Chính sách Base Scope (`M`)
| Họ chính sách (`policy_id`) | Tài liệu / Phiên bản | Chủ sở hữu & Người thay thế (100% Purchaser) | Số đoạn mẫu G0 | Số trường trọng yếu G0 | Nguyên vẹn bảng & chú thích (`DAT 08`) | Đồng bộ 6 chiều `DAT 04` (`CKPA-10`) & `60 dev_60` (`CKPA-30`) |
|---|---|---|---:|---:|---|---|
| **`POL-001`** — Báo giá & Phê duyệt thương mại | `DOC-001` (`VER-001`) | `[P2]` Hữu Tài / Deputy Sales Director | `10` (`PAS-001..010`) | `4` (`CF-001..004`) | `10/10` `has_essential_attachments=true`; `0` quy tắc tự bịa | `100%` khớp regex `CKPA-10`; khớp khóa ngoại `VG-04`, `VG-06` (`24` ca `dev_60`) |
| **`POL-002`** — Xử lý thông tin khách hàng CRM | `DOC-002` (`VER-001`) | `[P2]`  Hữu Tài / Senior CRM Lead | `10` (`PAS-011..020`) | `4` (`CF-005..008`) | `10/10` `has_essential_attachments=true`; `0` hồ sơ khách hàng (`O1` OFF) | `100%` khớp regex `CKPA-10`; khớp khóa ngoại `VG-07` (`16` ca `dev_60`) |
| **`POL-003`** — Định tuyến dịch vụ / bảo hành | `DOC-003` (`VER-001`) | `[P2]`  Hữu Tài / Internal Tech Lead | `10` (`PAS-021..030`) | `2` (`CF-009..010`) | `10/10` `has_essential_attachments=true`; khóa biên `ANS 07` (`PAS-025`) | `100%` khớp regex `CKPA-10`; khớp khóa ngoại `VG-12`, `VG-16` (`20` ca `dev_60`) |
| **TỔNG MẪU CỔNG G0** | **03 Tài liệu cốt lõi** | **Đủ 03 cặp Chủ sở hữu + Thay thế** | **`30` đoạn** | **`10` trường** | **`30/30` nguyên vẹn (`0` lỗi `DAT 08`)** | **`40/40` dòng khớp 100% chuẩn `CKPA-10` & `CKPA-13`** |

### 2.2 Bảng Đối chiếu `10` Trường Trọng yếu Tất định (`DAT 06` & `OPS 04`)
| Mã trường | Họ chính sách | Điều khoản gốc (`source_clause`) | Kiểu dữ liệu | Toán tử & Giá trị | Đơn vị / Tiền tệ | Cấp phê duyệt (`approval_role`) | Hạn mức SLA (`time_limit`) | Chiều `transaction_scope` (`CKPA-10`) |
|---|---|---|---|---|---|---|---|---|
| `CF-001` | `POL-001` | Điều 2.1, tr.1 (`PAS-004`) | `number` | `<= 5` | `%` / — | `Sales Staff (reader)` | `2 giờ làm việc` | `quotation_standard` |
| `CF-002` | `POL-001` | Điều 2.2, tr.1 (`PAS-005`) | `number` | `between 5;15` | `%` / — | `Sales Manager` | `4 giờ làm việc` | `quotation_exception` |
| `CF-003` | `POL-001` | Điều 2.3–2.5, tr.2 (`PAS-006..008`) | `currency` | `>= 1000000000` | `VND` / **`VND`** | `Sales Director` | `48 giờ làm việc` | `quotation_exception` |
| `CF-004` | `POL-001` | Điều 1.2–1.3, tr.1 (`PAS-002..003`) | `duration` | `<= 15` | `ngày làm việc` / — | `Sales Staff (reader)` | `15 ngày làm việc` | `quotation_standard` |
| `CF-005` | `POL-002` | Điều 1.4–1.5, tr.1 (`PAS-012`) | `duration` | `<= 2` | `giờ làm việc` / — | `CRM Staff (reader)` | `2 giờ làm việc` | `crm_contact_update` |
| `CF-006` | `POL-002` | Điều 2.1–2.3, tr.1 (`PAS-014`) | `currency` | `< 500000000` | `VND` / **`VND`** | `CRM Staff (reader)` | `4 giờ làm việc` | `crm_legal_update` |
| `CF-007` | `POL-002` | Điều 2.4, 2.6–2.7, tr.2 (`PAS-016, 018`) | `currency` | `>= 500000000` | `VND` / **`VND`** | `CRM Manager` | `4 giờ làm việc` | `crm_legal_update` |
| `CF-008` | `POL-002` | Điều 2.5, tr.2 (`PAS-017`) | `duration` | `<= 1` | `giờ` / — | `CRM Director` | `1 giờ` *(ngoài giờ HC)* | `crm_urgent_afterhours` |
| `CF-009` | `POL-003` | Điều 1.2–2.1, 2.4 (`PAS-021, 023, 026`) | `number` | `<= 37` | `kW` / — | `Internal Tech Lead` | `4 giờ làm việc` | `warranty_tier1_internal` |
| `CF-010` | `POL-003` | Điều 2.2–2.3, tr.2 (`PAS-024..025`) | `number` | `> 37` | `kW` / — | `Vendor Chief Engineer` | `4 giờ làm việc` | `warranty_tier2_vendor` |

---

## 3. Kế hoạch Hoàn tất Biên tập Kho Tri thức G1 Có Ngân sách (`Funded G1 Curation Plan`)

Căn cứ Mục 2 RFP (*approve a representative first 30 passages and 10 critical rows, plus funded plan for remaining corpus*) và trần giả định Base Scope (`<= 30` tài liệu, `<= 300` đoạn, `<= 50` dòng trường trọng yếu), kế hoạch biên tập toàn kho tri thức chuẩn trước **Cổng G1** được phân bổ trong **03 đợt triển khai** với tổng ngân sách giờ công kế hoạch **`51` giờ công (`16h` G0 + `35h` G1)** theo đúng 10 vai trò RFP Mục 11:

| Đợt biên tập | Khung thời gian dự kiến (sau G0) | Phạm vi nội dung thực tế (không tự bịa quy tắc) | Quy mô mục tiêu lũy kế (Tôn trọng trần `300/50` của `Source Register`) | Phân công theo 10 vai trò RFP (Mục 11) | Giờ công kế hoạch |
|---|---|---|---|---|---:|
| **Mốc G0 (Hiện tại — `CKPA-25..27`)** | Tuần Discovery 1–2 (`09/11 – 20/11/2026`) | `03` chính sách cốt lõi `DOC-001..003` (`VER-001`), đủ nền tảng cho 9 tình huống Annex B & bộ `60 dev_60` | `03` docs / `30` passages / `10` fields | `[P3]` Trần Chí Kha (`8h`), `[P2]`  Hữu Tài (`4h`), `[S2]` Trần Quốc Hưng (`2h`), `[S4]` Phạm Quý Hải (`2h`) | **`16h`** |
| **Đợt 1 G1 — Tuần triển khai 1 (`POL-001` & Phiên bản Lịch sử/Tương lai)** | Tuần 1 sau G0 *(dự kiến 5 ngày làm việc)* | Mở rộng `DOC-001` (`POL-001`), phần SOP báo giá `DOC-004` (`<= 16 pas / <= 2 CF`), biên tập **`VER-000` (`superseded`, phủ giai đoạn lịch sử `2026-10-12..2026-11-05`)** và **`VER-002` (`scheduled`)** cho `DOC-001..003` để kiểm thử `Worked Case 3 & 4` | `10` docs / `110` passages / `22` fields | `[P3]` Trần Chí Kha (`8h` biên tập), `[P2]`  Hữu Tài (`3h` duyệt nguồn), `[S1]` Hoàng Tiến (`2h` điều phối tiến độ) | **`13h`** |
| **Đợt 2 G1 — Tuần triển khai 2 (`POL-002`, `DOC-006` & `DOC-007`)** | Tuần 2 sau G0 *(dự kiến 5 ngày làm việc)* | Mở rộng `DOC-002` (`POL-002`), hoàn thiện SOP CRM (`DOC-004`), chuẩn hóa mẫu Hợp đồng khung `DOC-006` (`customer_contract`, `<= 10 pas` — `Worked Case 5`) và Ghi chú lịch sử `DOC-007` (`staff_note`, `<= 10 pas`, `0% PII` — `Worked Case 6`) | `20` docs / `200` passages / `36` fields | `[P3]` Trần Chí Kha (`8h` biên tập), `[P2]` Hữu Tài (`2h` duyệt), `[P5]` Nguyễn Anh Khoa (`2h` rà soát `0% PII` & quyền dùng `SRC-005`) | **`12h`** |
| **Đợt 3 G1 — Tuần triển khai 3 (`POL-003`, `DOC-005` & Nghiệm thu G1)** | Tuần 3 sau G0 *(dự kiến 5 ngày làm việc)* | Mở rộng `DOC-003` (`POL-003`), chuyển đổi thủ công bảng lỗi `DOC-005` (`manufacturer_terms`, `<= 25 pas / <= 3 CF`, **chỉ thực hiện sau khi `[P5]` & Pháp chế xác nhận bản quyền**), chạy nạp đối soát 100% Manifest & kiểm định độc lập G1 | **`<= 30` docs / `<= 300` passages / `<= 50` fields** *(đúng phân bổ `70+85+70+30+25+10+10=300` và `16+16+12+3+3+0+0=50`)* | `[P3]` Trần Chí Kha (`5h` hoàn tất CSV), `[S4]` Phạm Quý Hải (`3h` đối soát độc lập nhãn & phạm vi), `[S2]` Trần Quốc Hưng (`2h` chạy validator & đối soát Manifest) | **`10h`** |
| **TỔNG KẾ HOẠCH CURATION G0 → G1** | **Hoàn tất trước Cổng G1** | **Đủ năng lực biên tập có kiểm soát, không tự bịa rule, không vượt trần Mục 2** | **`<= 30` Docs / `<= 300` Passages / `<= 50` Critical Fields** | **Phía Purchaser (`[P2], [P3], [P5]`): `40h` \| Phía Supplier (`[S1], [S2], [S4]`): `11h`** | **`51h`** *(`16h` G0 + `35h` G1)* |

### 3.1 Liên kết Ngân sách Tài chính Minh bạch (`DEL 05` & `VN 06`)
- **Chi phí hỗ trợ biên tập & chuẩn hóa dữ liệu phía Nhà cung cấp (`Supplier Curation Assistance`):** Được tách thành hạng mục báo giá riêng tại **Dòng 2 (`Line 2 — Curation & Data Structuring Assistance`) trong Bảng Báo giá 3 năm VND (`DEL 05` / `CKPA-39`)**, trạng thái hiện tại **`PENDING_SUPPLIER_QUOTE`** — tuyệt đối không sử dụng con số ước đoán nội bộ thay cho báo giá chính thức có VAT.
- **Công sức nhân sự Chủ đầu tư (`Purchaser Owner / Steward Effort — 40h` kế hoạch G0→G1):** Được ghi nhận tường minh là chi phí nội bộ của Công ty Cổ phần Thiết bị Công nghiệp Song Nhật để đưa vào mô hình đánh giá đầy đủ công sức vận hành và bảo trì theo yêu cầu **`VN 06`** (không bị ẩn khỏi phép tính hiệu quả tại Cổng G3).
- **Kế hoạch dự phòng tải công việc (`Capacity Guard`):** Toàn bộ phân bổ giờ công trên từng vai trò bảo đảm nhịp bền vững `<= 8h/ngày`, `<= 40h/tuần/vai trò`. Nếu nguồn chính sách thực tế phát sinh bảng phức tạp vượt dự kiến, `[P2]` và `[P1]` sẽ ưu tiên chốt đầy đủ điều khoản cốt lõi trước thay vì giảm tiêu chuẩn kiểm tra `DAT 08` hay ép vượt trần.

---

## 4. Các Điều kiện Mở Cần Theo dõi trước Cổng G1 (`Open Prerequisites`)

1. **`CUR-G1-01` (Quyền sử dụng nguồn hãng `SRC-005`):** `DOC-005` (`manufacturer_terms`) đang ở trạng thái `source_rights_confirmed = PENDING_LEGAL_CONFIRMATION`; nghiêm cấm nạp vào kho tri thức G1 nếu chưa có xác nhận bản quyền bằng văn bản từ `[P5]` Nguyễn Anh Khoa và bộ phận Pháp chế.
2. **`CUR-G1-02` (Khắc phục khoảng trống lịch sử `VER-000` & bản `VER-002`):** Bắt buộc hoàn tất biên tập phiên bản tiền nhiệm `VER-000` (`superseded`, hiệu lực đến `2026-11-06T08:59:59+07:00`) để phủ cửa sổ câu hỏi 4 tuần `2026-10-12..2026-11-05` (`CKPA-6`) và phiên bản `VER-002` (`scheduled`) trước khi nghiệm thu Cổng G1.
3. **`CUR-G1-03` (Phê duyệt thương mại `DEL 05` Dòng 2 & Quyết định G0):** Việc giải ngân hoặc khởi động Đợt 1–3 G1 chỉ được thực hiện sau khi `[P1]` Vắn Mỹ Vân phê duyệt báo giá `DEL 05` (`CKPA-39`) và ký quyết định Cổng G0 tại `CKPA-42`.

---

## 5. XÁC NHẬN THẨM ĐỊNH & PHÊ DUYỆT CỔNG GATE G0 (`SIGNED-OFF`)

| Vai trò ký duyệt | Họ và tên | Nội dung xác nhận | Trạng thái ký | Ngày ký (`UTC+7`) |
|---|---|---|---|---|
| **Chủ sở hữu Chính sách — Policy Reviewer #1 (`[P2]`)** |  Hữu Tài | Thẩm định nội dung `30` đoạn + `10` trường trọng yếu đúng văn bản gốc (khớp 3 mã băm `SHA-256` `CKPA-26`) và thống nhất kế hoạch Curation G1 `51h` | `[x] Đã ký xác nhận` | `20/11/2026` |
| **Quản trị Tri thức — Policy Reviewer #2 (`[P3]`)** | Trần Chí Kha | Xác nhận biên tập chuẩn hóa 6 chiều `DAT 04`, toàn vẹn bảng/chú thích `DAT 08` và cam kết tiến độ 3 đợt G1 | `[x] Đã ký xác nhận` | `20/11/2026` |
| **Đại diện Chủ đầu tư / PO (`[P1]`)** | Vắn Mỹ Vân | Phê duyệt bộ mẫu `30+10`, quyền sử dụng nguồn nội bộ `SRC-001..004, 006..007` và ngân sách kế hoạch Curation G1 (gắn `DEL 05` Dòng 2) | `[x] Đã ký xác nhận` | `20/11/2026` |
| **Kiểm định Độc lập QA (`[S4]`)** | Phạm Quý Hải | Xác nhận đối soát khóa ngoại khớp bộ `60 dev_60` không rò rỉ (`CKPA-30`) và kiểm soát ranh giới SoD | `[x] Đã ký xác nhận` | `20/11/2026` |
