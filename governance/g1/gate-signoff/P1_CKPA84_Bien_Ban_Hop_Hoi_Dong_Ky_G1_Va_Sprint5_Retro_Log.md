# BIÊN BẢN HỌP HỘI ĐỒNG NGHIỆM THU CỔNG GATE G1 (CONTROLLED OFFLINE PILOT), LỆNH GIẢI NGÂN MỐC 2 (25%) & SPRINT 5 REVIEW / RETROSPECTIVE LOG

> **Dự án:** Trợ lý Tri thức và Chính sách CRM (SongNhat CRM Knowledge and Policy Assistant — SCRM / CKPA)  
> **Chủ đầu tư / Bên mua (Purchaser):** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật  
> **Nhà cung cấp / Bên phát triển (Supplier):** Đội ngũ Kỹ sư Dự án SCRM  
> **Mã công việc Jira:** `CKPA-84` (Mã gốc phân công: `CRM-G1-SUB30` — *[G1][Mục9] Họp Hội đồng Ký G1 (25%) & Biên bản S5 Retro*)  
> **Story Jira cha:** `CKPA-81` (`CRM-G1-ST10` — *[G1][Mục9] Nghiệm thu G1 (25%) & Sprint 5 Retro*) | **Parent Epic:** `CKPA-44` (`CRM-G1-EP01`)  
> **Cổng nghiệm thu:** Gate G1 — Controlled Offline Pilot & Benchmarks  
> **Truy vết RFP:** Mục 6, Mục 9 (G1 Sign-off & Proceed to G2), Mục 10 (W1–W3 & Kế hoạch W4), Mục 11 (Hours by role and week), Mục 12 (DEL 02 Working Core, DEL 03 Evidence Dossier, 25% Payment Milestone at G1), Scrum Events (Sprint 5 Review & Retrospective)  
> **Chủ trì Hội đồng / Phê duyệt (Assignee):** [P1] Vắn Mỹ Vân (Purchaser Sponsor / Product Owner — Bên mua)  
> **Đại diện đệ trình / Bàn giao (Reporter):** [S1] Hoàng Tiến (Named Lead / Scrum Master — Nhà cung cấp)  
> **Thành phần tham gia & Ký duyệt (RACI):** Toàn bộ 10 vai trò chuẩn RFP ([P1]–[P5] Bên mua & [S1]–[S5] Nhà cung cấp)  
> **Trạng thái Văn kiện:** **BẢN CHÍNH THỨC ĐÃ KÝ DUYỆT (FINAL v1.0 — SIGNED-OFF)**  
> **Trạng thái Cổng G1:** **CHẤP THUẬN NGHIỆM THU TOÀN DIỆN (APPROVED & PROCEED TO G2 — CHUYỂN JIRA `Done`)**  
> **Thời điểm tổ chức & Ký ban hành:** Ngày 27/11/2026 (09:00 – 11:30 — Giờ Việt Nam UTC+7)

---

## MỤC LỤC BIÊN BẢN HỌP HỘI ĐỒNG VÀ RETRO LOG

- **PHẦN 1: THÔNG TIN PHIÊN HỌP HỘI ĐỒNG VÀ ĐIỂM DANH 10 VAI TRÒ**
- **PHẦN 2: TIẾP NHẬN BÁO CÁO VÀ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐẦU VÀO**
- **PHẦN 3: BẢNG ĐỐI SOÁT CHI TIẾT 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)**
- **PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H / 276H — 100% DONE)**
- **PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG CHUYỂN GIAO)**
- **PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (`242H = 98H + 104H + 40H` / 30 TASKS — EPIC `CKPA-85`)**
- **PHẦN 7: NGHỊ QUYẾT HỘI ĐỒNG, CẤP PHÉP MỞ CỔNG G2 VÀ LỆNH GIẢI NGÂN MỐC 2 (25%)**
- **PHẦN 8: BẢNG KÝ DUYỆT CHÍNH THỨC CỦA 10 THÀNH VIÊN HỘI ĐỒNG DỰ ÁN**

---

# PHẦN 1: THÔNG TIN PHIÊN HỌP HỘI ĐỒNG VÀ ĐIỂM DANH 10 VAI TRÒ

Phiên họp Hội đồng Nghiệm thu Cổng G1 và Tổng kết Sprint 5 được triệu tập và chủ trì chính thức bởi Chủ đầu tư:

| Trường thông tin phiên họp | Giá trị ghi nhận thực tế | Ghi chú kiểm tra |
|---|---|---|
| **Thời gian họp** | 09:00 – 11:30, Ngày 27/11/2026 (Giờ Hà Nội — UTC+7) | Đúng lịch đăng ký tại Sprint Backlog |
| **Hình thức & Địa điểm** | Họp tập trung kết hợp trực tuyến tại Trụ sở Công ty Cổ phần Thiết bị Công nghiệp Song Nhật | Kênh bảo mật nội bộ, có ghi âm và lưu trữ nhật ký |
| **Chủ tọa phiên họp** | **[P1] Vắn Mỹ Vân** (Purchaser Sponsor / Product Owner) | Đại diện có thẩm quyền cao nhất của Bên mua |
| **Thư ký / Báo cáo kỹ thuật** | **[S1] Hoàng Tiến** (Named Lead / Scrum Master) | Đại diện quản lý Nhà cung cấp |
| **Mục đích phiên họp** | 1. Tiếp nhận kết quả bàn giao Hồ sơ Bằng chứng DEL 03 Part 1 & hợp nhất `develop @ 771b331`.<br>2. Xác nhận 7/7 tiêu chí Cổng G1-AC01..07 đạt 100% PASS (0 lỗi Critical Control).<br>3. Quyết toán giờ công W1–W3 (276h / 276h — 100% Done theo DEL 05).<br>4. Tổng kết Sprint 5 Review/Retro và thống nhất Kế hoạch Sprint 6 (G2).<br>5. Ký Biên bản Nghiệm thu G1, mở Cổng G2 và phê duyệt Lệnh giải ngân 25% kèm điều kiện bảo vệ tài chính. | Tuân thủ nghiêm ngặt Mục 9, 11, 12 RFP |

### Điểm danh 10 vai trò chuẩn RFP (10/10 Có mặt, tuân thủ nguyên tắc SoD):

1. **Phía Chủ đầu tư / Bên mua (Purchaser — 5 vai trò):**
   - **`[P1]` Vắn Mỹ Vân** — Purchaser Sponsor / Product Owner *(Chủ tọa Hội đồng — Có mặt)*.
   - **`[P2]` Trương Đình Hữu Tài** — Policy Owners / Policy Reviewer #1 *(Thành viên — Có mặt)*.
   - **`[P3]` Trần Chí Kha** — Knowledge & Data Steward *(Thành viên — Có mặt)*.
   - **`[P4]` Ngô Thị Trà My** — Staff Users Representative *(Thành viên điều phối 5 Rep Users — Có mặt)*.
   - **`[P5]` Nguyễn Anh Khoa** — Privacy & Security Owners *(Thành viên thẩm định An toàn/Bảo mật — Có mặt)*.
2. **Phía Nhà thầu / Nhà cung cấp (Supplier — 5 vai trò):**
   - **`[S1]` Hoàng Tiến** — Named Lead / Scrum Master *(Thành viên báo cáo — Có mặt)*.
   - **`[S2]` Trần Quốc Hưng** — Integration Engineer *(Thành viên kỹ thuật tích hợp — Có mặt)*.
   - **`[S3]` Phạm Lương Yến Nhi** — Retrieval & App Engineer *(Thành viên kỹ thuật RAG/Prompt — Có mặt)*.
   - **`[S4]` Phạm Quý Hải** — Quality Lead / Independent QA *(Thành viên kiểm định độc lập — Có mặt)*.
   - **`[S5]` Nguyễn Ngọc Duy** — Operations Specialist *(Thành viên vận hành hạ tầng — Có mặt)*.

---

# PHẦN 2: TIẾP NHẬN BÁO CÁO VÀ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐẦU VÀO

Hội đồng Nghiệm thu đã rà soát và tiếp nhận đầy đủ các văn kiện, biên bản chuyên môn cấu thành hồ sơ Cổng G1:

### 2.1. Tiếp nhận Hồ sơ Bằng chứng DEL 03 Part 1 (`CKPA-80`) & Bản vá Kỹ thuật (`CKPA-70`, `CKPA-75`, `CKPA-76` — Đã Done)
- Căn cứ Báo cáo tổng hợp `CKPA-80` (CRM-G1-SUB27), Nhà cung cấp đã hoàn thiện trọn bộ Hồ sơ Bằng chứng DEL 03 Part 1 qua 3 Sprint (W1, W2, W3).
- Toàn bộ các chốt chặn kỹ thuật cuối cùng (`CKPA-70`, `CKPA-75`, `CKPA-76`) đã hợp nhất lên nhánh chính **`develop @ 771b331`** kèm tag bất biến **`v0.2.1-g1-offline`** (PR #39 & PR #40 merged):
  - Xử lý triệt để `OPS 03` (`DAT04_NO_GOVERNING_DATE`), `DAT 08` (kiểm soát `unit`/`currency`), nối chuỗi Alembic migration nền (`base -> b01d4334f030 -> 20261121_01 -> 20261123_01`), và khắc phục 5 defects `DEF-CKPA75-01..05`.
  - Xử lý benchmark PostgreSQL (`create_all` & `TRUNCATE ... CASCADE`), guard `withdrawn` passage (`CKPA-70`), hash SHA-256 cho `_compose_document_version_id` (<= 64 ký tự), nâng ngưỡng micro-benchmark 150ms, và kiểm thử migration round-trip PostgreSQL 16 trên CI.
  - Kết quả kiểm thử trên `develop @ 771b331` (`v0.2.1-g1-offline`): Ruff & Mypy sạch **77 files**, chạy test đạt **257 passed, 1 skipped**, toàn bộ `CKPA-70`, `CKPA-75`, `CKPA-76` chuyển **`Done`**. *(Lưu ý truy vết `CKPA-70`: log `--strict-live` đang chờ `[P5]` chạy lại trên DB đã seed corpus thật ở **PR #65**).*

### 2.2. Tiếp nhận Kết quả Kiểm lại 100% source_uri từ `CKPA-82` (`[P3]` Trần Chí Kha — Đã Done)
- Căn cứ Biên bản và Nhật ký tái thẩm định `CKPA-82` (PR #52 & PR #55 đã merge vào nhánh `develop`), toàn bộ **136 / 136 bản ghi** dữ liệu Full Corpus (96 Passages + 40 Critical Fields) và **56 / 56 bản ghi** Family 1 đều tồn tại thực tế trên hệ thống lưu trữ, mở xem trực tiếp thành công, khớp 100% mã băm SHA-256.
- Đạt **0 liên kết hỏng (0 broken links)** và thực thi cơ chế cách ly kiểm soát bảng biểu **`DAT 08`**: 96 Passages = 93 Accepted + 3 Quarantined (cách ly đúng 3 ca thử nghiệm cố ý thiếu bảng biểu: `PAS-040`, `PAS-066`, `PAS-082`). Toàn bộ 40/40 trường trọng yếu đạt Accepted.

### 2.3. Tiếp nhận Thẩm định Chuyên môn Policy Reviewer #1 (`CKPA-83`) & Đồng ký Nhãn Vàng (`CKPA-67`, `CKPA-68` — Đã Done)
- Căn cứ Biên bản chuyên môn `CKPA-83` (PR #54, `Done`) và Biên bản đồng ký nhãn vàng `CKPA-68` (`Done`):
  1. Quy tắc Ngày hiệu lực chi phối (**`OPS 03`**) chuẩn hóa theo múi giờ Việt Nam (`UTC+7`), ranh giới ngày `2026-11-06 09:00:00 UTC+7` phân tách chính xác giữa bản lịch sử `VER-000` (`superseded`) và bản hiện hành `VER-001` (`effective`), khóa hoàn toàn bản tương lai `VER-002` (`scheduled`, 2027).
  2. Toàn bộ 136 bản ghi khai báo đủ **6 chiều ngữ cảnh bắt buộc** (`DAT 04`), chuẩn hóa 40 trường trọng yếu (`OPS 04`), 0% LLM số học (`llm_used=False`) và 4 kịch bản **HOLD / Fail-Closed**.
  3. Bộ **100 câu hỏi Sealed thay thế V2** (`VG-19..VG-43`, `52/24/24`, SHA-256 `372988c4...`) và **80 Constructed Challenges** (40 `VN 02`) đã được `[P2]` & `[P3]` đồng ký xác nhận kép và `[S4]` đóng băng ở trạng thái **`APPROVED_RELEASED_FROZEN` (`33180db`)** tại `CKPA-67` (`Done`).

### 2.4. Tiếp nhận Chứng nhận Kiểm toán An toàn & Bảo vệ Quyền riêng tư (`CKPA-79` — Đã Done)
- Đạt chuẩn **0% PII thật** trên 100% tài liệu và bộ câu hỏi (tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và `SEC 02`), xác nhận 0 tệp/bản ghi Sealed lọt vào kho chung.
- Kho ngoài `sealed-eval-repo @ 33180db` (`APPROVED_RELEASED_FROZEN`) khóa 100% quyền `Read/Write/Clone` đối với `S2/S3/S5`, cấp `Read-only` cho `P2/P3`, thu hồi quyền raw của `P5` sau kiểm toán. Thẻ `CKPA-79` đã được `[S1]` & `[P1]` phê duyệt **`Done`** (kèm lưu ý lưu trữ snapshot JSON/CSV Collaborators đồng bộ tại `CKPA-104` đầu Cổng G2).

---

# PHẦN 3: BẢNG ĐỐI SOÁT CHI TIẾT 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)

Hội đồng đã tiến hành rà soát từng tiêu chí chấp nhận kỹ thuật và quản trị theo quy định tại Mục 9 RFP:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát | Kết luận Hội đồng |
|:---:|---|---|---|:---:|
| **`G1-AC01`** | **Toàn vẹn Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..DOC-011) thuộc 3 họ POL-001/002/003 và 5 lớp thẩm quyền DAT 03; dưới 300 đoạn văn (thực tế 96); dưới 50 trường (thực tế 40); 100% source_uri khớp SHA-256; DAT 08 cân bằng 93 Acc + 3 Qua. | Biên bản `CKPA-82` của [P3], PR #52 & PR #55 merged; Xác nhận `CKPA-83` của [P2] (`Done`); Manifest 136 bản ghi checksum SHA-256 sạch. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Validators, Reconciliation & Benchmark Offline OPS 01** | 2 Base CSV Validators; Quarantine tự động; Full-Snapshot Reconciliation (Expected = Accepted + Quarantined); Benchmark OPS 01 trên 500 dòng <= 30 phút; LKG 100%; 100 Sealed + 80 Challenges. | `CKPA-52` (PR #26), `CKPA-59` (PR #28), `CKPA-60` (PR #29: 0.3738s, LKG 100%); Bộ `100 SEALED` V2 (`372988c4...`) + `80 Challenges` đạt **`APPROVED_RELEASED_FROZEN` (`33180db`)** tại `CKPA-67` & `CKPA-68` (`Done`); tối ưu batch prefetch `develop @ 771b331` (`v0.2.1-g1-offline`). | **ĐẠT (PASS)** |
| **`G1-AC03`** | **Immediate Withdrawal & Khóa O1 Mặc định (Base Scope)** | Rút hồi/thu hồi tài liệu có hiệu lực tức thì (commit trạng thái trước khi ack); Fail-closed đối với tài liệu đã thu hồi (`SEC 05`, `KNW 04`); Khóa cứng Option O1 trong Base Scope (`OPTION_O1_ENABLED = False`, `DAT 07`). | PR #28 logic commit trước ack; HTTP 403 khóa O1; PR #61 sửa route `POST /api/v1/answer`; kiểm soát `withdrawn` passage guard & sửa `CKPA-70` hợp nhất tại **`develop @ 771b331`** + tag **`v0.2.1-g1-offline`** (PR #39 & #40 merged, `Done`; log `--strict-live` `CKPA-70` chờ `[P5]` chạy lại trên DB seed thật ở **PR #65**). | **ĐẠT (PASS)** |
| **`G1-AC04`** | **Pre-retrieval RBAC 4 Vai trò & 7 Trạng thái Vòng đời** | Thực thi RBAC 4 vai trò (`reader`, `policy_owner`, `steward`, `administrator`) tại Pre-Retrieval (`SEC 01`); Quản lý đúng 7 trạng thái `KNW 03`; 0% rò rỉ khi từ chối; Kiểm toán kho Sealed (`SEC 06`). | RBAC phân vùng `SEALED_100` (`8f89d1d`, 231 tests PASS); `CKPA-70` hợp nhất tại `develop @ 771b331` + tag `v0.2.1-g1-offline` (`Done`; log `--strict-live` `CKPA-70` chờ `[P5]` chạy lại trên DB seed thật ở **PR #65**); `CKPA-79` đạt `Done` (`sealed_manifest.json @ 33180db`). | **ĐẠT (PASS)** |
| **`G1-AC05`** | **Governing Date UTC+7 (OPS 03) & Khớp 6 Chiều DAT 04** | Phân giải ngày sự kiện theo múi giờ Việt Nam UTC+7; Ranh giới lịch sử 2026-11-06T09:00:00+07:00; Khớp chính xác 6 chiều ngữ cảnh DAT 04; Tự động chuyển HOLD khi thiếu ngày chi phối. | `CKPA-62` (`Done`), `CKPA-63`, `CKPA-83` (`Done`); Toàn bộ `CKPA-75` & `CKPA-76` (`OPS 03`, `DAT 08`, Alembic migration round-trip PostgreSQL 16, `DEF-CKPA75-01..05`) hợp nhất tại **`develop @ 771b331`** + tag bất biến **`v0.2.1-g1-offline`** (Ruff/Mypy 77 files sạch, **257 passed, 1 skipped**), chuyển `Done`. | **ĐẠT (PASS)** |
| **`G1-AC06`** | **Deterministic Field Lookup (DAT 06) & Cơ chế HOLD** | Tra cứu trường trọng yếu định lượng qua Python Decimal thuần (0% số học qua LLM); Tự động kích hoạt HOLD khi thiếu bảng/chú thích (DAT 08) hoặc xung đột nguồn văn bản (DAT 05, OPS 04). | `CKPA-63` (PR #23: Decimal thuần, `llm_used=False`, auto HOLD 4 kịch bản); `CKPA-64` (30/30 tests PASS); Biên bản `CKPA-83` (`Done`); `CKPA-78` đã merge. | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Bộ 200 Real Tasks, 80 Challenges & Cô lập Môi trường** | Môi trường Test tách Prod (`SEC 06`); 0% PII thật (`SEC 02`); Kho ngoài `sealed-eval-repo` chặn `S2/S3`; Bộ 200 câu hỏi (60 Dev / 40 Val / 100 Sealed) + 80 Challenges (`VN 02`); 5 Rep Users độc lập. | `0% PII` pass (`CKPA-47`); Ma trận 5 NSD (`CKPA-5/31`); Bộ `100 Sealed` V2 + `80 Challenges` (`CKPA-65/67/68 Done`); `CKPA-79` đạt `Done` (`sealed-eval-repo @ 33180db` khóa 100% `S2/S3/S5`; lưu ý kèm snapshot Collaborators JSON/CSV tại `CKPA-104`). | **ĐẠT (PASS)** |

> **KẾT LUẬN ĐỐI SOÁT:** Toàn bộ **7 / 7 tiêu chí Cổng G1 đạt 100% (PASS)**, hệ thống ghi nhận **0 lỗi Critical Control**. Đủ điều kiện đóng Cổng G1 và mở khóa Cổng G2.

---

# PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H / 276H — 100% DONE)

Căn cứ quy định tại Mục 10, Mục 11 RFP và hồ sơ định mức DEL 05 đã chuẩn hóa tại `CKPA-80`, Hội đồng đối soát quyết toán giờ công lũy kế Cổng G1 (Tuần 1, Tuần 2, Tuần 3) theo đúng 10 vai trò:

### Bảng Tổng hợp Quyết toán Giờ công G1 Thực tế vs Kế hoạch (DEL 05):

| Mã Role | Họ và tên thành viên | Phía RFP | W1 (Sprint 3) | W2 (Sprint 4) | W3 (Sprint 5) | Tổng KH G1 | Thực tế Hoàn tất (`Done`) | Đạt tỷ lệ (%) | Nhịp bền vững (<= 40h/w) |
|---|---|---|---:|---:|---:|---:|---:|:---:|:---:|
| **`[P1]`** | Vắn Mỹ Vân | Purchaser | 0h | 0h | 4h | **4h** | **4h** | 100.0% | Đạt (Max 4h/w <= 40h) |
| **`[P2]`** | Trương Đình Hữu Tài | Purchaser | 8h | 12h | 4h | **24h** | **24h** | 100.0% | Đạt (Max 12h/w <= 40h) |
| **`[P3]`** | Trần Chí Kha | Purchaser | 16h | 8h | 12h | **36h** | **36h** | 100.0% | Đạt (Max 16h/w <= 40h) |
| **`[P4]`** | Ngô Thị Trà My | Purchaser | 16h | 16h | 0h | **32h** | **32h** | 100.0% | Đạt (Max 16h/w <= 40h) |
| **`[P5]`** | Nguyễn Anh Khoa | Purchaser | 8h | 8h | 12h | **28h** | **28h** | 100.0% | Đạt (Max 12h/w <= 40h) |
| **Cộng Bên Mua** | **5 vai trò Purchaser** | **Purchaser** | **48h** | **44h** | **32h** | **124h** | **124h** | **100.0%** | **Đạt chuẩn nhịp độ** |
| **`[S1]`** | Hoàng Tiến | Supplier | 0h | 8h | 8h | **16h** | **16h** | 100.0% | Đạt (Max 8h/w <= 40h) |
| **`[S2]`** | Trần Quốc Hưng | Supplier | 8h | 16h | 4h | **28h** | **28h** | 100.0% | Đạt (Max 16h/w <= 40h) |
| **`[S3]`** | Phạm Lương Yến Nhi | Supplier | 16h | 24h | 4h | **44h** | **44h** | 100.0% | Đạt (Max 24h/w <= 40h) |
| **`[S4]`** | Phạm Quý Hải | Supplier | 12h | 12h | 16h | **40h** | **40h** | 100.0% | Đạt (Max 16h/w <= 40h) |
| **`[S5]`** | Nguyễn Ngọc Duy | Supplier | 16h | 8h | 0h | **24h** | **24h** | 100.0% | Đạt (Max 16h/w <= 40h) |
| **Cộng Nhà Thầu** | **5 vai trò Supplier** | **Supplier** | **52h** | **68h** | **32h** | **152h** | **152h** | **100.0%** | **Đạt chuẩn nhịp độ** |
| **TOÀN DỰ ÁN** | **10 Vai trò chuẩn RFP** | **Toàn thể** | **100h** | **112h** | **64h** | **276h** | **276h** | **100.0%** | **100% tuân thủ nhịp độ** |

### Xác nhận đối soát quyết toán:
1. **Khớp 100% định mức:** Tổng thời lượng thực tế quyết toán của Cổng G1 là **276 giờ / 276 giờ (100% Done)** (Tuần 1: 100h, Tuần 2: 112h, Tuần 3: 64h), hoàn tất toàn bộ 30/30 Sub-tasks và 10/10 Stories, khớp chính xác với ma trận `PhanCongCongViec_G1.xlsx` (DEL 05) và Epic `CKPA-44`.
2. **Tuân thủ nhịp độ làm việc bền vững (Sustainable Pace):** Toàn bộ 10 thành viên có mức tải tối đa trong tuần không vượt quá **24 giờ/tuần** (thấp hơn ngưỡng trần 40 giờ/tuần) và không quá 8 giờ/ngày.

---

# PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG CHUYỂN GIAO)

### 5.1. Sprint 5 Review — Đánh giá Kết quả Đạt được (What Went Well)
1. **Hợp nhất kỹ thuật sạch & Swarming hiệu quả:** Xử lý dứt điểm `CKPA-75` & `CKPA-76`, hợp nhất lên nhánh `develop @ 771b331` kèm tag bất biến **`v0.2.1-g1-offline`** (PR #39 & PR #40 merged), Ruff/Mypy 77 files sạch, đạt **257 passed, 1 skipped**.
2. **Quy trình kiểm soát dữ liệu nguồn 2 lớp hiệu quả:** Sự kết hợp độc lập giữa `[P3]` Trần Chí Kha (`CKPA-82`) và `[P2]` Trương Đình Hữu Tài (`CKPA-83`) đã xác thực 136/136 SHA-256 và cách ly chuẩn xác 3 ca thiếu bảng biểu `DAT 08`.
3. **Kỷ luật No-Mock, Chinese Wall & SoD:** Thay thế thành công bộ 100 Sealed V2 (`33180db`), đồng ký nhãn vàng kép (`CKPA-68`), khóa hoàn toàn kho riêng cho `S2/S3/S5` (`CKPA-79`), và giữ vững nguyên tắc kiểm chứng thực tế trước khi ký duyệt.

### 5.2. Sprint 5 Retrospective — Các Điểm Cần Tối Ưu khi bước vào Sprint 6
1. **Chuẩn hóa hồ sơ log kho ngoài ngay đầu G2:** Lưu kèm bản snapshot JSON/CSV Collaborators xuất từ `ckpa-dev-val-eval/sealed-eval-repo` vào kho bằng chứng nội bộ tại nhiệm vụ `CKPA-104`.
2. **Hoàn thiện báo giá thương mại DEL 05:** Đôn đốc hoàn tất điền đơn giá thực tế 14 dòng VND+VAT tại `CKPA-39` làm cơ sở giải ngân và chấm điểm thương mại.

### 5.3. Bảng Hành động Chuyển giao sang Sprint 6 / Cổng G2 (Action Items)

| Mã Action | Nội dung Hành động Cụ thể | Người chịu trách nhiệm | Trạng thái / Hạn hoàn thành | Tiêu chí nghiệm thu |
|---|---|---|---|---|
| **`RETRO-S5-01`** | Duy trì cờ `OPTION_O1_ENABLED = False`, khóa toàn bộ tính năng thử nghiệm ngoài Base Scope. | `[S2]` Quốc Hưng & `[S5]` Ngọc Duy | Đã xác nhận (Duy trì liên tục G2) | File cấu hình `backend/src/config.py` được `[P5]` xác nhận |
| **`RETRO-S5-02`** | Đóng băng cấu hình kiểm thử bảo mật và API `POST /api/v1/answer` sau khi `CKPA-70` hợp nhất `develop @ 771b331` (`v0.2.1-g1-offline`). | `[S1]` Hoàng Tiến & `[P5]` Anh Khoa | **ĐÃ HOÀN TẤT (`Done` 27/11)** *(Chờ `[P5]` chạy lại `--strict-live` trên DB seed thật tại PR #65)* | `CKPA-70` chuyển `Done` |
| **`RETRO-S5-03`** | Đính kèm snapshot JSON/CSV Collaborators của `sealed-eval-repo` vào hồ sơ kiểm toán đầu Cổng G2 (`CKPA-104`). | `[S4]` Quý Hải & `[P5]` Anh Khoa | Ngày 1 Sprint 6 (`CKPA-104`) | Snapshot Collaborators lưu kèm trong kho bằng chứng G2 |
| **`RETRO-S5-04`** | Nộp 14 dòng đơn giá VND + thuế VAT thực tế tại `CKPA-39` để kích hoạt chuyển khoản giải ngân Mốc 2 (25%). | `[S1]` Hoàng Tiến & `[P1]` Mỹ Vân | Trước khi Kế toán chuyển khoản | Bảng giá `DEL 05` xóa trạng thái `PENDING_SUPPLIER_QUOTE` |

---

# PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (242H / 3 GIAI ĐOẠN / 30 TASKS)

Căn cứ Kế hoạch triển khai chuẩn hóa tại (`DEL 05`) đồng bộ từ `CKPA-80` và Epic `CKPA-85`, Hội đồng thống nhất kích hoạt Sprint 6 (Cổng G2 — Supervised Use) với tổng định mức **242 giờ** (Purchaser: **126h** + Supplier: **116h**, tuân thủ nhịp độ bền vững 14h–32h/tuần <= 40h/tuần) phân bổ cho 10 vai trò qua 3 giai đoạn (30 Tasks `CKPA-91` → `CKPA-120`):

1. **Giai đoạn 1 (Ngày 1–2 Sprint 6 — Build Workspace, Lifecycle, Ops & Legal Prep — 98h):**
   - **WP 04 Answer Package, Referral & Anti-Injection (`[S3]` Yến Nhi, 16h):** `CKPA-91` (8h), `CKPA-92` (4h), `CKPA-97` (4h) — Answer Package chuẩn 100–250 từ (`ANS 03-04`), Local Referral 3 trạng thái & 9 ca Annex B (`KNW 05`), chống Prompt Injection & khóa Streaming (`ANS 08`).
   - **WP 05 Vòng đời 7 Trạng thái & Change Impact (`[S2]` Quốc Hưng, 8h):** `CKPA-94` (8h) — 7 trạng thái `KNW 03`, chặn Stale Answer (`KNW 04`) & 5 nhãn phản hồi (`KNW 07`).
   - **Vận hành, Cache Purge & Đóng băng RC (`[S5]` Ngọc Duy 16h, `[S4]` Quý Hải 12h, `[S1]` Hoàng Tiến 8h — 36h):** `CKPA-98` (16h: Purge cache <= 5 phút `OPS 05`, Cap 1k/2k `OPS 08` & `OPS 06`), `CKPA-100` (12h: chuẩn bị 80 Challenges gồm 40 `VN 02`), `CKPA-101` (8h: đóng băng tag `v0.3.0-g2-rc`).
   - **Pháp lý, Chính sách, Dữ liệu & Chuẩn bị UAT Bên Mua (38h):** `[P5]` Anh Khoa 14h (`CKPA-103`: lập luận phân loại AI có ngày Annex F); `[P2]` Hữu Tài 6h (`CKPA-95`); **`[P3]` Trần Chí Kha 6h** (`CKPA-96`: diễn tập Change Impact & 5 nhãn `KNW 07`); `[P4]` Trà My 12h (`CKPA-93`: 6h đánh giá UX 40 ca Val & `CKPA-109`: 6h chuẩn bị 5 NSD đại diện).

2. **Giai đoạn 2 (Ngày 3–4 Sprint 6 — Kiểm định Độc lập 100 Sealed / 80 Challenges & Swarming — 104h):**
   - **Benchmark Hiệu năng, Swarming & QA Độc lập (`[S5]` 10h, `[S2]` 8h, `[S3]` 8h, `[S4]` 16h — 42h):** `CKPA-99` (10h: benchmark p95 <= 25s @ 5 concurrent users `OPS 02`), `CKPA-102` (8h) & `CKPA-105` (8h: swarming sửa lỗi non-Sealed), `CKPA-106` (16h: chạy độc lập 100 Sealed & 80 Challenges).
   - **Thẩm định Độc lập, Pháp lý & Tiền thẩm định Bên Mua (62h):** `[P5]` Anh Khoa 12h (`CKPA-104`: ký duyệt pháp lý `SEC 03/07/08`, 0 lộ dữ liệu & đính kèm snapshot ACL kho Sealed); `[P2]` Hữu Tài 14h (`CKPA-107`: Reviewer #1 chấm 100 Sealed & 80 Challenges); **`[P3]` Trần Chí Kha 14h** (`CKPA-108`: Reviewer #2 chấm Applicability & Recall@5); `[P4]` Trà My 14h (`CKPA-110`: 5 NSD chấm Hữu ích >= 80% & diễn tập Fallback); `[P1]` Mỹ Vân 8h (`CKPA-118`: tiền thẩm định `DEL 02/03` & hồ sơ pháp lý).

3. **Giai đoạn 3 (Ngày 5 Sprint 6 — Đào tạo, Chốt Hồ sơ DEL 02/03 & Hội đồng Nghiệm thu G2 — 40h):**
   - **Kiểm toán Mẫu số & Chốt Hồ sơ Steward (`[P3]` Trần Chí Kha, 8h):** Khớp chính xác `CKPA-111` (4h: ký bảng mẫu số có Hold) và `CKPA-117` (4h: chốt nhật ký Steward & hồ sơ G2) — Tổng Sprint 6 của `[P3]` = **28h**.
   - **Hoàn tất Đào tạo, Ký Hồ sơ Độc lập & Kiểm tra Mở Pilot (20h):** `[P2]` Hữu Tài 4h (`CKPA-112`), `[P4]` Trà My 4h (`CKPA-113`), `[S5]` Ngọc Duy 4h (`CKPA-114`: xác nhận Cap 1k/2k & Probe 99.5%), `[S4]` Quý Hải 4h (`CKPA-115`: ký báo cáo điểm độc lập `DEL 03`), `[P5]` Anh Khoa 4h (`CKPA-116`: đồng ký hồ sơ pháp lý & sự cố G2).
   - **Hội đồng Nghiệm thu Cổng G2 & Sprint 6 Retro (`[P1]` Mỹ Vân 6h, `[S1]` Hoàng Tiến 6h — 12h):** `CKPA-119` (6h: ký nghiệm thu G2 mốc 25% & mở 20 ngày Pilot G3) và `CKPA-120` (6h: báo cáo giờ công Tuần 4 & Sprint 6 Review/Retro).

---

# PHẦN 7: NGHỊ QUYẾT HỘI ĐỒNG, CẤP PHÉP MỞ CỔNG G2 VÀ LỆNH GIẢI NGÂN MỐC 2 (25%)

Căn cứ kết quả đối soát toàn diện đạt 7/7 tiêu chí Cổng G1, 0 lỗi Critical Control và sự nhất trí 100% của 10 vai trò tham dự, Chủ tịch Hội đồng **`[P1]` Vắn Mỹ Vân** chính thức quyết nghị:

### 7.1. Phê duyệt Nghiệm thu Chính thức Cổng Gate G1 (Sign-off Gate G1)
- Nghiệm thu toàn diện Giai đoạn Thử nghiệm Nội bộ Ngoại tuyến có Kiểm soát (Controlled Offline Pilot & Benchmarks).
- Công nhận các kết quả bàn giao: Bộ Corpus 3 họ chuẩn hóa, Pipeline RAG offline đạt chuẩn (`develop @ 771b331`, tag bất biến `v0.2.1-g1-offline`, 257 passed), bộ 200 Tasks & 80 Challenges niêm phong độc lập (`33180db`), Hồ sơ Bằng chứng DEL 03 Part 1 và Báo cáo quyết toán 276 / 276 giờ công (100% Done). *(Log `--strict-live` của `CKPA-70` theo dõi đồng bộ trên DB seed thật tại PR #65).*
- Chính thức chuyển User Story cha **`CKPA-81`** và Sub-task **`CKPA-84`** sang trạng thái **`Done`** trên hệ thống Jira.

### 7.2. Quyết định Cấp phép Chuyển tiếp Mở Cổng Gate G2 (Proceed to G2)
- Cấp phép cho dự án chuyển tiếp sang Giai đoạn Thử nghiệm Nội bộ Giới hạn (Sprint 6 — Gate G2 Live Pilot).
- **Ràng buộc kiểm soát bắt buộc trong Sprint 6:**
  1. Duy trì nghiêm ngặt phạm vi Base Scope thuần túy: Khóa cứng `OPTION_O1_ENABLED = False`, không nạp dữ liệu CRM sống khi chưa có phê duyệt riêng từ Legal Owner.
  2. Đính kèm snapshot Collaborators JSON/CSV kho ngoài tại `CKPA-104` và triển khai Giao thức đo 20 ngày năng suất cho 5 Rep Users (`CKPA-109`).

### 7.3. Lệnh Giải ngân Thanh toán Mốc 2 (25% Giá trị Hợp đồng Base Scope)
- Căn cứ Điều 12 Hợp đồng Dịch vụ Phần mềm số 01/2026/HDDV-CKPA và nguyên tắc bảo vệ tài chính tại `CKPA-42`:
  1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
  2. **Tỷ lệ giải ngân:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT).
  3. **Công thức xác định giá trị thanh toán thực tế:**
     `Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)`
  4. **Điều kiện Bảo vệ Tài chính Bắt buộc trước khi Chuyển khoản (`PENDING_SUPPLIER_QUOTE`):**
     - Về mặt kỹ thuật, điều kiện nghiệm thu Cổng G1 đã hoàn tất 100%.
     - Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật **CHỈ THỰC HIỆN GIẢI NGÂN CHUYỂN KHOẢN** khi Nhà cung cấp hoàn tất nộp đầy đủ **Bảng giá Thương mại `DEL 05` chính thức gồm 14 dòng đơn giá VND + thuế VAT thực tế tại task `CKPA-39`** (xóa bỏ hoàn toàn trạng thái `PENDING_SUPPLIER_QUOTE`, tuyệt đối không sử dụng bảng số liệu minh họa của Phụ lục E) kèm theo **Hóa đơn Giá trị gia tăng (VAT) hợp lệ**.

---

# PHẦN 8: BẢNG KÝ DUYỆT CHÍNH THỨC CỦA 10 THÀNH VIÊN HỘI ĐỒNG DỰ ÁN

Các thành viên Hội đồng đại diện cho 10 vai trò RFP đã đọc kỹ, thống nhất toàn bộ nội dung và cùng ký tên xác nhận chính thức ngày **27/11/2026**:

| Vai trò chuẩn RFP | Họ và tên thành viên | Chức vụ / Đơn vị đại diện | Trách nhiệm xác nhận | Chữ ký xác nhận (27/11/2026) |
|---|---|---|---|:---:|
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ đầu tư — Song Nhật | Chủ tịch Hội đồng — Phê duyệt Cổng G1, Mở G2 & Ký Lệnh Giải ngân 25% | *(Đã ký duyệt chính thức — 27/11/2026)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | Xác nhận `CKPA-83`, đồng ký `CKPA-68` & Tiêu chuẩn Chính sách | *(Đã ký duyệt chuyên môn — 27/11/2026)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | Xác nhận `CKPA-82` (100% SHA-256), đồng ký `CKPA-68` & Toàn vẹn G1 | *(Đã ký duyệt dữ liệu — 27/11/2026)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ | Xác nhận 100 Sealed V2 (`CKPA-65/66`) & Kế hoạch Đo 20 ngày Effort | *(Đã ký duyệt nghiệp vụ — 27/11/2026)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin | Xác nhận 0% PII, RBAC (`CKPA-70`) & ACL kho Sealed (`CKPA-79`) | *(Đã ký duyệt an ninh — 27/11/2026)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | Bàn giao DEL 03 Part 1 (`CKPA-80`), Quyết toán 276h & Kế hoạch Sprint 6 | *(Đã ký xác nhận bàn giao — 27/11/2026)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | Xác nhận Swarming `CKPA-76`, migration round-trip & hợp nhất `develop @ 771b331` | *(Đã ký xác nhận kỹ thuật — 27/11/2026)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | Xác nhận Lookup Decimal thuần, 0% LLM số học & Khóa cứng Base Scope | *(Đã ký xác nhận kỹ thuật — 27/11/2026)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Kiểm định Độc lập | Xác nhận đóng băng `CKPA-67 @ 33180db` & Kiểm định 7/7 Tiêu chí G1 | *(Đã ký kiểm định độc lập — 27/11/2026)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hạ tầng | Xác nhận Hạ tầng CI/Test PostgreSQL 16 & Môi trường vận hành G1 | *(Đã ký xác nhận vận hành — 27/11/2026)* |

---
*Biên bản bản chính thức Final v1.0 này được lập thành 04 (bốn) bản gốc bằng tiếng Việt có giá trị pháp lý như nhau ngày 27/11/2026. Bên Mua lưu giữ 02 bản, Bên Cung cấp lưu giữ 02 bản để làm căn cứ đóng Cổng G1, chuyển tiếp Sprint 6 (Cổng G2) và giải ngân Mốc 2 (25%) khi hoàn tất báo giá 14 dòng DEL 05 tại `CKPA-39` kèm hóa đơn VAT hợp lệ.*
