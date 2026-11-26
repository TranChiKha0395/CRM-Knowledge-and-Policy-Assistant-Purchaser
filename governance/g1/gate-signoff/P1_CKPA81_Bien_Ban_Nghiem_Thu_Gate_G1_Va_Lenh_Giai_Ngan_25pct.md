# HỒ SƠ BÁO CÁO NGHIỆM THU CỔNG GATE G1 (CONTROLLED OFFLINE PILOT & BENCHMARKS), ĐỐI SOÁT 7/7 TIÊU CHÍ G1-AC01..07, QUYẾT ĐỊNH MỞ CỔNG G2 VÀ LỆNH GIẢI NGÂN MỐC 2 (25%)

> **Dự án:** Trợ lý Tri thức và Chính sách CRM (SongNhat CRM Knowledge and Policy Assistant — SCRM / CKPA)  
> **Chủ đầu tư / Bên mua (Purchaser):** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật  
> **Cấp thẩm quyền phê duyệt:** [P1] Vắn Mỹ Vân – Purchaser Sponsor / Product Owner  
> **Mã Story Jira cha:** `CKPA-81` (Mã gốc Excel: `CRM-G1-ST10` — *[G1][Mục9] Nghiệm thu G1 (25%) & Sprint 5 Retro*) | **Epic:** `CKPA-44`  
> **Các Sub-tasks trực thuộc tích hợp đối soát:**  
> - `CKPA-82` (`CRM-G1-SUB28`): Rà soát lại 100% source_uri & bảng/chú thích DAT 08 (`[P3]` Trần Chí Kha hoàn thành, PR #52 & PR #55 đã merge — **Done**)  
> - `CKPA-83` (`CRM-G1-SUB29`): Xác nhận chuyên môn Policy Reviewer #1 về Ngày/Trường/Hold (`[P2]` Trương Đình Hữu Tài hoàn thành, PR #54 đã merge — **Done**)  
> - `CKPA-84` (`CRM-G1-SUB30`): Họp Hội đồng Ký G1 (25%) & Biên bản Sprint 5 Retro (`[P1]` Vắn Mỹ Vân chủ trì — **Done**)  
> **Trạng thái Văn kiện:** **BẢN CHÍNH THỨC ĐÃ KÝ DUYỆT (FINAL v1.0 — SIGNED-OFF)**  
> **Quyết định Cổng G1:** **CHẤP THUẬN NGHIỆM THU TOÀN DIỆN (APPROVED & PROCEED TO G2 — CHUYỂN JIRA `Done`)**  
> **Thời điểm ban hành chính thức:** Ngày 27/11/2026 (Giờ Việt Nam — UTC+7)

---

## MỤC LỤC VĂN KIỆN NGHIỆM THU CHÍNH THỨC

- **PHẦN I:** TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐÃ HOÀN TẤT (CKPA-82, CKPA-83 & CKPA-84)
- **PHẦN II:** BẢNG ĐỐI SOÁT 7/7 TIÊU CHÍ CỔNG G1 (G1-AC01 .. G1-AC07) ĐẠT 100% PASS
- **PHẦN III:** QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: ĐÓNG CỔNG G1 VÀ CẤP PHÉP CHUYỂN TIẾP SANG CỔNG G2
- **PHẦN IV:** LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25%) VÀ ĐIỀU KIỆN BẢO VỆ TÀI CHÍNH (`PENDING_SUPPLIER_QUOTE`)
- **PHẦN V:** BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT CHÍNH THỨC 10 VAI TRÒ HỘI ĐỒNG

---

# PHẦN I: TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐÃ HOÀN TẤT

Hội đồng Nghiệm thu Cổng G1 do **`[P1]` Vắn Mỹ Vân** chủ trì ghi nhận và tiếp nhận toàn diện kết quả thực hiện độc lập từ toàn bộ các Sub-tasks kỹ thuật và chuyên môn đã hoàn tất:

### 1.1 Tiếp nhận Kết quả Rà soát Nguồn Tri thức từ `CKPA-82` (`[P3]` Trần Chí Kha — ĐÃ HOÀN THÀNH `Done`)
Căn cứ Biên bản kiểm lại `data/g1/reports/CKPA-82_Bien_Ban_Kiem_Lai_100pct_Source_URI_DAT08_Va_Ky_G1_AC01.md` và nhật ký `CKPA-82_source_uri_dat08_reverify.log` (đối soát thực tế qua PR #52 và PR #55 trên nhánh `develop`):
- **Trần quy mô dữ liệu Base Scope G1:**
  - Tài liệu nguồn gốc: Đạt **11 / 30** tài liệu (phủ đủ 3 họ chính sách `POL-001`, `POL-002`, `POL-003` và 5 lớp thẩm quyền `DAT 03`: Policy, SOP, Customer Contract, Staff Note, Manufacturer Terms).
  - Đoạn văn trích xuất (`Passages`): Đạt **96 / 300** đoạn (độ dài tối đa 591 / 6.000 ký tự Unicode, đúng chuẩn 21 cột UTF-8).
  - Trường trọng yếu (`Critical Fields`): Đạt **40 / 50** trường (đúng chuẩn 23 cột UTF-8).
- **Kiểm lại 100% `source_uri` & mã băm mật mã SHA-256 (Mục 9 RFP):**
  - Toàn bộ **136 / 136** bản ghi Full Corpus Manifest (96 đoạn + 40 trường) và **56 / 56** bản ghi Family 1 đều trỏ tới tệp tồn tại thực tế trên đĩa, mở xem trực tiếp thành công, khớp 100% mã băm SHA-256, xác nhận **0 liên kết hỏng (0 broken links)** và **0 lệch mã băm**.
- **Kiểm soát cờ bảng biểu & chú thích thiết yếu (`DAT 08`):**
  - Cân bằng dữ liệu chính xác tuyệt đối: **96 Passages = 93 Accepted + 3 Quarantined**.
  - Cách ly đúng 3 trường hợp cố ý thiếu bảng biểu/chú thích để kiểm thử: `PAS-040` (Phụ lục B1 Bảng chiết khấu Đại lý Cấp 1), `PAS-066` (Phụ lục B2 Bảng phân quyền xuất dữ liệu đối tác), `PAS-082` (Phụ lục B3 Danh mục linh kiện hao mòn loại trừ). Toàn bộ 40/40 trường trọng yếu đạt trạng thái Accepted.
- **Tuân thủ phân quyền và bảo vệ quyền riêng tư:**
  - 100% tệp dữ liệu đạt chuẩn **0% PII thật** (tái kiểm tra qua `security/g1/g1_pii_audit_CKPA-47.log`).

### 1.2 Tiếp nhận Thẩm định Chuyên môn Chính sách từ `CKPA-83` (`[P2]` Trương Đình Hữu Tài — ĐÃ HOÀN THÀNH `Done`)
Căn cứ Biên bản chuyên môn `policy/g1/CKPA-83_Xac_Nhan_Policy_Reviewer1_P2_Corpus_Ngay_Truong_Hold.md` (PR #54 merged):
- **Trụ cột Ngày hiệu lực chi phối (`OPS 03`) & Vòng đời tri thức (`KNW 03`):**
  - Chuẩn hóa múi giờ Việt Nam (`Asia/Ho_Chi_Minh`, `UTC+7`), ranh giới `2026-11-06 09:00:00 UTC+7` phân tách giữa bản lịch sử `VER-000` (`superseded` kèm nhãn *"Hướng dẫn lịch sử"*) và bản hiện hành `VER-001` (`effective`); khóa hoàn toàn bản tương lai `VER-002` (`scheduled`, `2027-01-01`).
  - Chặn 100% ở tầng Pre-Retrieval đối với 4 trạng thái chưa hoặc ngừng hiệu lực (`withdrawn`, `draft`, `owner_reviewed`, `approved`).
- **Trụ cột 6 Chiều ngữ cảnh (`DAT 04`) & 40 Trường trọng yếu (`OPS 04`):**
  - 100% (136/136 bản ghi) khai báo đầy đủ 6 chiều: `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`.
  - Chuẩn hóa các ngưỡng số học qua Decimal thuần (`llm_used=False`, 0% LLM số học).
- **Trụ cột Cơ chế HOLD & Ranh giới Fail-Closed (`DAT 05`, `DAT 08`, `ANS 05/06`):**
  - Mã hóa chuẩn 4 kịch bản HOLD: Quarantine Hold, Conflict Hold, Evidence Hold (lập phiếu chuyển tiếp 8h làm việc) và Từ chối suy luận từ `staff_note`.

### 1.3 Tiếp nhận Dữ liệu Niêm phong, Kiểm toán An ninh & Bản vá Kỹ thuật (`CKPA-67`, `CKPA-68`, `CKPA-79`, `CKPA-70`, `CKPA-75`, `CKPA-76`)
- **`CKPA-67` & `CKPA-68` (`Done`):** Gói **100 câu hỏi Sealed V2** (`VG-19..VG-43`, `52/24/24`, SHA-256 `372988c4...`) và **80 Constructed Challenges** (40 `VN 02`) đã được `[P2]` & `[P3]` đồng ký nhãn vàng và `[S4]` đóng băng ở trạng thái **`APPROVED_RELEASED_FROZEN` (`33180db`)** trên kho `ckpa-dev-val-eval/sealed-eval-repo`.
- **`CKPA-79` (`Done`):** Kho `sealed-eval-repo @ 33180db` khóa 100% quyền `Read/Write/Clone` đối với `S2/S3/S5`; `P2/P3` chỉ Read-only; `P5` thu hồi quyền raw sau kiểm toán. Đã đạt phê duyệt chính thức từ `[S1]` & `[P1]`.
- **`CKPA-70`, `CKPA-75`, `CKPA-76` (`Done`):** Toàn bộ chốt chặn kỹ thuật cuối (`OPS 03`, `DAT 08`, Alembic migration `base -> b01d4334f030 -> 20261121_01 -> 20261123_01`, `DEF-CKPA75-01..05`, `withdrawn` passage guard, hash SHA-256 cho `_compose_document_version_id`) đã hợp nhất lên **`develop @ 771b331`** (PR #39 & PR #40 merged), Ruff/Mypy sạch **77 files**, chạy test đạt **257 passed, 1 skipped**.

---

# PHẦN II: BẢNG ĐỐI SOÁT 7/7 TIÊU CHÍ CỔNG G1 (G1-AC01 .. G1-AC07) ĐẠT 100% PASS

Hội đồng Nghiệm thu đối soát chi tiết từng tiêu chí chấp nhận dựa trên bằng chứng kỹ thuật và nhật ký thực tế trên `develop`:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát (No-Mock) | Kết luận Đánh giá |
| :---: | :--- | :--- | :--- | :---: |
| **`G1-AC01`** | **Toàn vẹn Dữ liệu Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..011); dưới 300 đoạn văn; dưới 50 trường trọng yếu; 100% bản ghi đủ 6 chiều DAT 04; 0 link gãy source_uri; 136 SHA-256 khớp 100%. | Biên bản `CKPA-82` của [P3] (PR #52 & PR #55); Xác nhận `CKPA-83` của [P2] (`Done`); `Policy_Corpus_G1_Full.csv` đạt 93 Acc + 3 Qua. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Bộ Dữ liệu Kiểm thử Độc lập 200 Tasks & 80 Challenges** | Phân vùng chuẩn 60 Dev / 40 Val / 100 Sealed chống rò rỉ; Niêm phong 100 Sealed + 80 Challenges trong `sealed-eval-repo`; 2 Policy Reviewers đồng duyệt. | Gói `100 SEALED` V2 (`VG-19..VG-43`, SHA-256 `372988c4...`) + `80 Challenges` đã đạt **`APPROVED_RELEASED_FROZEN` (`33180db`)** tại `CKPA-67` (`Done`); `[P2]` & `[P3]` đồng ký tại `CKPA-68` (`Done`); `CKPA-65` (`Done`). | **ĐẠT (PASS)** |
| **`G1-AC03`** | **Immediate Withdrawal & Khóa O1 Mặc định (Base Scope)** | Rút hồi tức thì commit trước ack, fail-closed (`SEC 05`, `KNW 04`); Khóa Option O1 mặc định trong Base Scope (`OPTION_O1_ENABLED=False`, `DAT 07`); An ninh log truy cập (`SEC 01`, `SEC 02`). | PR #28 logic commit trước ack; HTTP 403 khóa O1; PR #61 sửa route `POST /api/v1/answer`; kiểm soát `withdrawn` passage guard & sửa `CKPA-70` đã hợp nhất lên **`develop @ 771b331`** (PR #39 & #40 merged, `Done`). | **ĐẠT (PASS)** |
| **`G1-AC04`** | **Pre-retrieval RBAC 4 Vai trò & 7 Trạng thái Vòng đời** | Thực thi RBAC 4 vai trò (`reader`, `policy_owner`, `steward`, `administrator`) tại Pre-Retrieval (`SEC 01`); Quản lý đúng 7 trạng thái `KNW 03`; 0% rò rỉ khi từ chối; Kiểm toán kho Sealed (`SEC 06`). | RBAC phân vùng `SEALED_100` (`8f89d1d`, 231 tests PASS); sửa lỗi `CKPA-70` hợp nhất tại `develop @ 771b331` (`Done`); `CKPA-79` đạt `Done` (`sealed_manifest.json @ 33180db`). | **ĐẠT (PASS)** |
| **`G1-AC05`** | **Hiệu năng Pipeline Benchmark Offline & Bàn giao DEL 02/03** | Đóng băng mã nguồn, Pipeline RAG đạt chỉ số kiểm chuẩn; Bàn giao trọn bộ Kiến trúc `DEL 02` và Báo cáo kiểm định `DEL 03`. | Toàn bộ `CKPA-75` & `CKPA-76` (`OPS 03`, `DAT 08`, Alembic migration round-trip PostgreSQL 16, `DEF-CKPA75-01..05`) đã hợp nhất lên **`develop @ 771b331`** (PR #39 & #40 merged, Ruff/Mypy 77 files sạch, **257 passed, 1 skipped**), chuyển `Done`. | **ĐẠT (PASS)** |
| **`G1-AC06`** | **Deterministic Field Lookup (`DAT 06`) & Cơ chế HOLD** | Tra cứu trường trọng yếu định lượng qua Python Decimal thuần (0% số học qua LLM); Tự động kích hoạt HOLD khi thiếu ngày chi phối (`OPS 03`), thiếu bảng (`DAT 08`) hoặc xung đột nguồn (`DAT 05`, `OPS 04`). | `CKPA-63` (PR #23: 52/52 tests PASS); `CKPA-64` [S4] retest đạt 30/30 tests PASS; Thẩm định chuyên môn `CKPA-83` của [P2] (`Done`). | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Môi trường Test tách Prod, 0% PII & Tách vai SoD** | Môi trường Test tách Prod (`SEC 06`); 0% PII thật (`SEC 02`); QA Lead `[S4]` độc lập code `S2/S3`; 5 NSD đại diện thuộc 100% Bên Mua; kho `sealed-eval-repo` cô lập `S2/S3`. | Môi trường Test tách Prod; 0% PII (`CKPA-47` PASS); Ma trận 5 NSD (`CKPA-5/31`); `CKPA-79` đạt `Done` (`sealed-eval-repo @ 33180db` khóa 100% `S2/S3/S5`; lưu ý kèm snapshot Collaborators JSON/CSV khi khởi động `CKPA-104` tại G2). | **ĐẠT (PASS)** |

**KẾT LUẬN ĐỐI SOÁT:** Toàn bộ **7 / 7 tiêu chí Cổng G1 đạt 100% (PASS)**, hệ thống ghi nhận **0 lỗi Critical Control**. Đủ điều kiện nghiệm thu Cổng G1 và chuyển tiếp sang Cổng G2.

---

# PHẦN III: QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: ĐÓNG CỔNG G1 VÀ CẤP PHÉP CHUYỂN TIẾP SANG CỔNG G2

Căn cứ kết quả đối soát đạt 7/7 tiêu chí và biên bản họp Hội đồng `CKPA-84` ngày 27/11/2026:

1. **Quyết định Phê duyệt Nghiệm thu Chính thức Cổng Gate G1:**
   - Chủ đầu tư **CHÍNH THỨC PHÊ DUYỆT NGHIỆM THU CỔNG GATE G1** (Controlled Offline Pilot & Benchmarks).
   - Chuyển trạng thái User Story cha **`CKPA-81`** và toàn bộ 3/3 Sub-tasks trực thuộc (**`CKPA-82`**, **`CKPA-83`**, **`CKPA-84`**) sang **`Done`** trên hệ thống Jira.
   - Quyết toán hoàn tất **276 / 276 giờ công (100% Done)** theo định mức `DEL 05` (W1: 100h, W2: 112h, W3: 64h).

2. **Quyết định Cấp phép Chuyển tiếp Mở Cổng Gate G2 (Proceed to G2):**
   - Cấp phép cho dự án chuyển tiếp chính thức sang **Sprint 6 — Cổng Gate G2 (Live Pilot)** theo kế hoạch `360h / 30 tasks` đã thống nhất.
   - Duy trì nghiêm ngặt ràng buộc Base Scope: Khóa cứng `OPTION_O1_ENABLED = False`, không nạp dữ liệu CRM sống khi chưa có phê duyệt riêng, và bổ sung snapshot Collaborators JSON/CSV kho ngoài tại nhiệm vụ đầu Cổng G2 (`CKPA-104`).

---

# PHẦN IV: LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25%) VÀ ĐIỀU KIỆN BẢO VỆ TÀI CHÍNH (`PENDING_SUPPLIER_QUOTE`)

Căn cứ Điều 12 Hợp đồng Dịch vụ Phần mềm số 01/2026/HDDV-CKPA và nguyên tắc bảo vệ quyền lợi Bên Mua tại Cổng G0 (`CKPA-42`):

1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
2. **Tỷ lệ giải ngân quy định:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT).
3. **Công thức xác định giá trị thanh toán thực tế:**
   `Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)`
4. **Điều kiện Bảo vệ Tài chính Bắt buộc trước khi Chuyển khoản (`PENDING_SUPPLIER_QUOTE`):**
   - Về mặt kỹ thuật, điều kiện nghiệm thu Cổng G1 đã hoàn tất 100%.
   - Tuy nhiên, Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật **CHỈ THỰC HIỆN GIẢI NGÂN CHUYỂN KHOẢN** khi Nhà cung cấp hoàn tất nộp đầy đủ **Bảng giá Thương mại `DEL 05` chính thức gồm 14 dòng đơn giá VND + thuế VAT thực tế tại task `CKPA-39`** (xóa bỏ hoàn toàn trạng thái `PENDING_SUPPLIER_QUOTE`, tuyệt đối không sử dụng bảng số liệu minh họa của Phụ lục E) kèm theo **Hóa đơn Giá trị gia tăng (VAT) hợp lệ**.

---

# PHẦN V: BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT CHÍNH THỨC 10 VAI TRÒ HỘI ĐỒNG

### 5.1 Tổng kết Sprint 5 Retrospective
- **Những điểm thực hiện xuất sắc:**
  - Quy trình kiểm soát dữ liệu nguồn 2 lớp (`CKPA-82`, `CKPA-83`) đạt độ chính xác 100%, cách ly chuẩn 3 ca `DAT 08`.
  - Xử lý triệt để sự cố rò rỉ đề bài bằng bộ 100 Sealed V2 (`33180db`), đồng ký nhãn vàng kép (`CKPA-68`) và giữ vững kỷ luật No-Mock xuyên suốt cổng G1.
  - Phối hợp Swarming hiệu quả (`CKPA-76`), khắc phục dứt điểm migration và đạt **257 passed** trên nhánh `develop @ 771b331`.
- **Kế hoạch chuyển giao sang Sprint 6 (Cổng G2):**
  - Đính kèm snapshot Collaborators JSON/CSV của `sealed-eval-repo` vào hồ sơ kiểm toán đầu G2 (`CKPA-104`).
  - Triển khai Giao thức đo 20 ngày năng suất (`Observed Effort`) với 5 Người dùng đại diện (`CKPA-109`).

### 5.2 BẢNG KÝ DUYỆT NGHIỆM THU CHÍNH THỨC CỦA 10 THÀNH VIÊN HỘI ĐỒNG (NGÀY 27/11/2026)

| Vai trò RFP | Họ và tên | Chức danh / Đại diện | Trạng thái Ký duyệt Chính thức |
| :--- | :--- | :--- | :---: |
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ tịch Hội đồng Thẩm định & Nghiệm thu | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ SongNhat | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin & Quyền riêng tư | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Đảm bảo Chất lượng Độc lập | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hệ thống | *(Đã ký duyệt chính thức — 27/11/2026)* |

---
*Văn kiện bản chính thức Final v1.0 này là căn cứ pháp lý và kỹ thuật xác nhận đóng Cổng Gate G1, cấp phép triển khai Sprint 6 (Cổng G2) và phê duyệt giải ngân Mốc 2 (25%) khi Nhà cung cấp hoàn tất nộp báo giá thực tế 14 dòng DEL 05 tại `CKPA-39` và hóa đơn VAT hợp lệ.*
