# HỒ SƠ BÁO CÁO RÀ SOÁT CỔNG GATE G1 (CONTROLLED OFFLINE PILOT & BENCHMARKS), ĐỐI SOÁT 7 TIÊU CHÍ G1-AC01..07, QUYẾT ĐỊNH TREO ĐIỀU KIỆN MỞ G2 VÀ LỆNH GIẢI NGÂN MỐC 2 (25%)

> **Dự án:** Trợ lý Tri thức và Chính sách CRM (SongNhat CRM Knowledge & Policy Assistant — SCRM / CKPA)  
> **Chủ đầu tư / Bên mua (Purchaser):** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật  
> **Cấp thẩm quyền rà soát:** [P1] Vắn Mỹ Vân – Purchaser Sponsor / Product Owner  
> **Mã Story Jira cha:** `CKPA-81` (Mã gốc Excel: `CRM-G1-ST10` — *[G1][Mục9] Nghiệm thu G1 (25%) & Sprint 5 Retro*) | **Epic:** `CKPA-44`  
> **Các Sub-tasks trực thuộc tích hợp đối soát:**  
> - `CKPA-82` (`CRM-G1-SUB28`): Rà soát lại 100% source_uri & bảng/chú thích DAT 08 (`[P3]` Trần Chí Kha hoàn thành, PR #52 & PR #55 đã merge — ĐẠT)  
> - `CKPA-83` (`CRM-G1-SUB29`): Xác nhận chuyên môn Policy Reviewer #1 về Ngày/Trường/Hold (`[P2]` Trương Đình Hữu Tài hoàn thành, PR #54 đã merge — ĐẠT)  
> - `CKPA-84` (`CRM-G1-SUB30`): Họp Hội đồng Ký G1 (25%) & Biên bản Sprint 5 Retro (`[P1]` Vắn Mỹ Vân chủ trì — Đang rà soát)  
> **Trạng thái Văn kiện:** **BẢN DỰ THẢO RÀ SOÁT CHỜ GIẢI TỎA BLOCKERS (DRAFT v0.9 — PENDING_G1_BLOCKERS)**  
> **Khuyến nghị Quyết định Cổng G1:** **TẠM DỪNG CHỜ GIẢI TỎA (HOLD / PENDING_G1_BLOCKERS)**  
> **Thời điểm ban hành rà soát:** Ngày 25/11/2026 (Giờ Việt Nam — UTC+7)

---

## MỤC LỤC VĂN KIỆN RÀ SOÁT

- **PHẦN I:** TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐÃ HOÀN TẤT (CKPA-82 & CKPA-83)
- **PHẦN II:** BẢNG ĐỐI SOÁT TRUNG THỰC 7/7 TIÊU CHÍ CỔNG G1 (G1-AC01 .. G1-AC07) THEO LOG THỰC TẾ
- **PHẦN III:** QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: XÁC LẬP TRẠNG THÁI HOLD VÀ 4 BLOCKERS BẮT BUỘC TRƯỚC KHI MỞ G2
- **PHẦN IV:** LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25%) VÀ ĐIỀU KIỆN TREO PENDING_SUPPLIER_QUOTE
- **PHẦN V:** BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT 10 VAI TRÒ HỘI ĐỒNG

---

# PHẦN I: TỔNG HỢP CĂN CỨ VÀ KẾT QUẢ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐÃ HOÀN TẤT

Hội đồng Nghiệm thu Cổng G1 do **`[P1]` Vắn Mỹ Vân** chủ trì ghi nhận và tiếp nhận toàn diện kết quả thực hiện độc lập từ các Sub-tasks kỹ thuật và chuyên môn đã hoàn tất:

### 1.1 Tiếp nhận Kết quả Rà soát Nguồn Tri thức từ `CKPA-82` (`[P3]` Trần Chí Kha — ĐÃ HOÀN THÀNH)
Căn cứ Biên bản kiểm lại `data/g1/reports/CKPA-82_Bien_Ban_Kiem_Lai_100pct_Source_URI_DAT08_Va_Ky_G1_AC01.md` và nhật ký `CKPA-82_source_uri_dat08_reverify.log` (đã đối soát thực tế qua PR #52 và PR #55 trên nhánh `develop`):
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
  - 100% tệp dữ liệu đạt chuẩn **0% PII thật** (được tái kiểm tra và xác nhận qua nhật ký `security/g1/g1_pii_audit_CKPA-47.log`).

### 1.2 Tiếp nhận Thẩm định Chuyên môn Chính sách từ `CKPA-83` (`[P2]` Trương Đình Hữu Tài — ĐÃ HOÀN THÀNH)
Căn cứ Biên bản chuyên môn `policy/g1/CKPA-83_Xac_Nhan_Policy_Reviewer1_P2_Corpus_Ngay_Truong_Hold.md` (PR #54):
- **Trụ cột Ngày hiệu lực chi phối (`OPS 03`) & Vòng đời tri thức (`KNW 03`):**
  - Toàn bộ các mốc thời gian được chuẩn hóa theo múi giờ Việt Nam (`Asia/Ho_Chi_Minh`, `UTC+7`).
  - Mốc chuyển giao ranh giới phiên bản: `2026-11-06 09:00:00 UTC+7`. Trước thời điểm này áp dụng phiên bản lịch sử v0.9 (`superseded` kèm nhãn bắt buộc *"Hướng dẫn lịch sử"*). Từ thời điểm này trở đi áp dụng phiên bản hiện hành `VER-001` (`effective`).
  - Cấm tuyệt đối áp dụng phiên bản tương lai `VER-002` (`scheduled`, hiệu lực từ `2027-01-01`) cho các giao dịch năm 2026.
  - Chặn 100% ở tầng Pre-Retrieval đối với 4 trạng thái chưa hoặc ngừng hiệu lực (`withdrawn`, `draft`, `owner_reviewed`, `approved`).
- **Trụ cột 6 Chiều ngữ cảnh (`DAT 04`) & 40 Trường trọng yếu (`OPS 04`):**
  - 100% (136/136 bản ghi) khai báo đầy đủ 6 chiều: `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`.
  - Chuẩn hóa các ngưỡng số học qua Decimal thuần (0% LLM số học): Chiết khấu từ 5% trở xuống (CVKD duyệt trong 2h), trên 5% đến 15% (TPKD duyệt trong 4h), trên 15% hoặc đơn từ 1 tỷ VND (GĐKD duyệt trong 48h); Hợp đồng lũy kế dưới 500 triệu VND (CRM Staff, 4h) vs từ 500 triệu VND trở lên (CRM Manager, 4h); Công suất động cơ thường từ 37.0 kW trở xuống (Tuyến 1 Kỹ thuật nội bộ) vs trên 37.0 kW (Tuyến 2 Hãng), riêng động cơ phòng nổ Ex-d bắt buộc Tuyến 2.
- **Trụ cột Cơ chế HOLD & Ranh giới Fail-Closed (`DAT 05`, `DAT 08`, `ANS 05/06`):**
  - Mã hóa chuẩn 4 kịch bản HOLD: Quarantine Hold (thiếu bảng biểu), Conflict Hold (xung đột Hợp đồng khung/OEM cấm tự suy diễn thứ bậc ưu tiên, bắt buộc trích dẫn song song), Evidence Hold (mờ chứng từ, tạo phiếu chuyển tiếp xử lý trong 8 giờ làm việc), và Từ chối tiền lệ ghi chú CRM (`staff_note` không ghi đè chính sách).

---

# PHẦN II: BẢNG ĐỐI SOÁT TRUNG THỰC 7/7 TIÊU CHÍ CỔNG G1 (G1-AC01 .. G1-AC07) THEO LOG THỰC TẾ

Hội đồng Nghiệm thu đối soát chi tiết từng tiêu chí chấp nhận dựa trên bằng chứng kỹ thuật và nhật ký kiểm toán thực tế (No-Mock) trên nhánh `develop`:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát (No-Mock) | Kết luận Đánh giá |
| :---: | :--- | :--- | :--- | :---: |
| **`G1-AC01`** | **Toàn vẹn Dữ liệu Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..011); dưới 300 đoạn văn; dưới 50 trường trọng yếu; 100% bản ghi đủ 6 chiều DAT 04; 0 link gãy source_uri; 136 SHA-256 khớp 100%. | Biên bản CKPA-82 của [P3], PR #52 & PR #55; Xác nhận của [P2] tại CKPA-83; File Policy_Corpus_G1_Full.csv. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Bộ Dữ liệu Kiểm thử Độc lập 200 Tasks & 80 Challenges** | Phân vùng chuẩn 60 Dev / 40 Val / 100 Sealed chống rò rỉ; Niêm phong 100 Sealed + 80 Challenges trong sealed-eval-repo; 2 Policy Reviewers đồng duyệt. | [S4] cảnh báo nguồn câu hỏi bị công khai lúc 12:07 ngày 25/11 -> 100 SEALED hiện tại không dùng làm holdout độc lập được, đang yêu cầu [P4] cấp bộ thay thế; CKPA-68 (2 Policy Reviewers đồng duyệt) vẫn In Progress chưa có kết quả. | **CHƯA ĐẠT<br>(PENDING_SEALED_REPLACEMENT & CKPA-68)** |
| **`G1-AC03`** | **Immediate Withdrawal & Khóa O1 Mặc định (Base Scope)** | Rút hồi tức thì commit trước ack, fail-closed (SEC 05, KNW 04); Khóa Option O1 mặc định trong Base Scope (OPTION_O1_ENABLED=False, DAT 07); An ninh log truy cập (SEC 01, SEC 02). | PR #28 đã merge logic commit trước ack; cờ O1 khóa mặc định 403; tuy nhiên nhật ký g1_rbac_failclosed_audit_CKPA-70.log đang ở mức PARTIAL_PASS (4/4 BLOCKED_NO_LIVE_ENDPOINT do chờ Staging URL thật và xử lý lệch dấu / tại /api/v1/answer/). | **CHƯA ĐẠT TOÀN DIỆN<br>(PARTIAL_PASS — BLOCKED_NO_LIVE_ENDPOINT)** |
| **`G1-AC04`** | **Pre-retrieval RBAC 4 Vai trò & 7 Trạng thái Vòng đời** | Thực thi RBAC 4 vai trò (reader, policy_owner, steward, administrator) tại Pre-Retrieval (SEC 01); Quản lý đúng 7 trạng thái KNW 03; 0% rò rỉ link/citation/cache/log khi từ chối; Kiểm toán kho Sealed (SEC 06). | Unit tests PR #20 & PR #49 pass; nhưng log chạy runtime thật g1_rbac_failclosed_audit_CKPA-70.log đang 0/4 PASS_VERIFIED, 4/4 BLOCKED_NO_LIVE_ENDPOINT; g1_sealed_acl_audit_CKPA-79.log Part 2 đang BLOCKED_EXTERNAL_REPO_ACCESS (chờ log thật kho ngoài). | **CHƯA ĐẠT TOÀN DIỆN<br>(PARTIAL_PASS — BLOCKED_EXTERNAL_ACCESS)** |
| **`G1-AC05`** | **Hiệu năng Pipeline Benchmark Offline & Bàn giao DEL 02/03** | Đóng băng mã nguồn tag v0.2.0-g1-offline; Pipeline RAG đạt chỉ số kiểm chuẩn; Bàn giao trọn bộ Kiến trúc DEL 02 và Báo cáo kiểm định DEL 03. | Đã gắn tag v0.2.0-g1-offline; tuy nhiên báo cáo kiểm định CKPA-75 của [S4] và PR #33 bên repo Supplier vẫn OPEN với kết luận NEEDS_SIGNOFF (lỗi fresh-DB Alembic migration thiếu passages, đang bàn giao DEF-CKPA75-01..05 sang Swarming CKPA-76 để cắt patch tag v0.2.1-g1-offline). | **CHƯA ĐẠT<br>(NEEDS_SIGNOFF — Chờ Swarming CKPA-76)** |
| **`G1-AC06`** | **Deterministic Field Lookup (DAT 06) & Cơ chế HOLD** | Tra cứu trường trọng yếu định lượng qua Python Decimal thuần (0% số học qua LLM); Tự động kích hoạt HOLD khi thiếu ngày chi phối (OPS 03), thiếu bảng (DAT 08) hoặc xung đột nguồn (DAT 05, OPS 04). | CKPA-63 (PR #23: 52/52 tests PASS); CKPA-64 S4 retest đạt 30/30 tests PASS; Thẩm định chuyên môn CKPA-83 của [P2] đã xác nhận. | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Môi trường Test tách Prod, 0% PII & Tách vai SoD** | Môi trường Test tách Prod (SEC 06); 0% PII thật (SEC 02); QA Lead [S4] độc lập code S2/S3; 5 NSD đại diện thuộc 100% Bên Mua; kho sealed-eval-repo cô lập S2/S3. | Môi trường Test đã dựng (PR #25); Quét nội bộ 0% PII (PR #50 Part 1 PASS); Ma trận 5 NSD tại CKPA-5/31; tuy nhiên xác nhận kiểm toán ACL kho ngoài tại CKPA-79 Part 2 vẫn đang BLOCKED chờ log thật từ S4/S5. | **CHƯA ĐẠT TOÀN DIỆN<br>(PARTIAL_PASS — Chờ log ACL kho ngoài)** |

**KẾT LUẬN ĐỐI SOÁT:** Hiện tại mới đạt **2 / 7 tiêu chí (G1-AC01, G1-AC06)**; còn **5 / 7 tiêu chí (G1-AC02, G1-AC03, G1-AC04, G1-AC05, G1-AC07)** đang ở trạng thái `PARTIAL_PASS`, `BLOCKED` hoặc `NEEDS_SIGNOFF`. Hệ thống **chưa đủ điều kiện tuyên bố 0 lỗi Critical Control**.

---

# PHẦN III: QUYẾT ĐỊNH CỦA CHỦ ĐẦU TƯ: XÁC LẬP TRẠNG THÁI HOLD VÀ 4 BLOCKERS BẮT BUỘC TRƯỚC KHI MỞ G2

Căn cứ nguyên tắc kiểm định trung thực (No-Mock) và bảo vệ an toàn dự án:

1. **Quyết định Xác lập Trạng thái Cổng G1:**
   - Chủ đầu tư **CHƯA KÝ NGHIỆM THU ĐÓNG CỔNG G1**, tạm thời xác lập trạng thái **`HOLD / PENDING_G1_BLOCKERS`**.
   - Tiếp tục giữ User Story cha **`CKPA-81`** ở trạng thái **`In Progress`** trên hệ thống Jira cho đến khi giải tỏa toàn bộ các điểm nghẽn kỹ thuật.

2. **Danh mục 4 Điểm nghẽn Bắt buộc (Blockers) phải giải tỏa trước khi cấp phép mở Cổng G2:**
   - **`BLOCKER-01` (G1-AC02 / CKPA-67, CKPA-68):** [P4] Ngô Thị Trà My cung cấp bộ 100 câu hỏi Sealed thay thế bảo mật do bộ cũ bị công khai trên repo; [P2] Hữu Tài và [P3] Chí Kha hoàn thành đồng duyệt nhãn vàng độc lập tại `CKPA-68`.
   - **`BLOCKER-02` (G1-AC03, G1-AC04 / CKPA-70):** [S1] Hoàng Tiến và [S5] Ngọc Duy sửa triệt để lỗi route `/api/v1/answer/`, cấp Staging live endpoint để [P5] Anh Khoa thực thi kiểm thử `--strict-live` đạt 4/4 PASS thật, xóa bỏ hoàn toàn trạng thái `BLOCKED_NO_LIVE_ENDPOINT`.
   - **`BLOCKER-03` (G1-AC04, G1-AC07 / CKPA-79):** [S4] Quý Hải và [S5] Ngọc Duy xuất tệp JSON/CSV Collaborators & GitHub Audit Log thật từ kho riêng `sealed-eval-repo` để [P5] Anh Khoa chạy `--strict-external` đạt PASS thật, xóa bỏ trạng thái `BLOCKED_EXTERNAL_REPO_ACCESS`.
   - **`BLOCKER-04` (G1-AC05 / CKPA-75, CKPA-76):** Đội Build [S2] hoàn tất xử lý 5 defects (DEF-CKPA75-01..05) trong đợt Swarming `CKPA-76`, cắt patch tag **`v0.2.1-g1-offline`** và QA Lead [S4] delta retest đạt 100% PASS (đóng PR #33 bên repo Supplier).

---

# PHẦN IV: LỆNH GIẢI NGÂN THANH TOÁN MỐC 2 (25%) VÀ ĐIỀU KIỆN TREO PENDING_SUPPLIER_QUOTE

Căn cứ Điều 12 Hợp đồng Dịch vụ Phần mềm số 01/2026/HDDV-CKPA và nguyên tắc bảo vệ quyền lợi Bên Mua tại Cổng G0 (`CKPA-42`):

1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
2. **Tỷ lệ giải ngân quy định:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT).
3. **Công thức xác định giá trị thanh toán thực tế:**
   `Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)`
4. **Điều kiện Tiên quyết Giải ngân (ĐIỀU KIỆN TREO — PENDING_SUPPLIER_QUOTE):**
   - Lệnh giải ngân 25% này **chỉ có giá trị dự thảo và TẠM TREO HIỆU LỰC THI HÀNH**.
   - Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật **TUYỆT ĐỐI CHƯA GIẢI NGÂN** cho đến khi hội đủ cả 2 điều kiện bắt buộc:
     1. Toàn bộ **4 Blockers kỹ thuật** nêu tại Phần III được giải tỏa và Hội đồng ký Biên bản Nghiệm thu Cổng G1 chính thức.
     2. Nhà cung cấp hoàn tất nộp Bảng giá Thương mại DEL 05 chính thức với đầy đủ **14 dòng đơn giá VND + thuế VAT thực tế** tại task `CKPA-39` (xóa bỏ trạng thái `PENDING_SUPPLIER_QUOTE`, tuyệt đối không sử dụng bảng số liệu minh họa của Phụ lục E).

---

# PHẦN V: BIÊN BẢN SPRINT 5 RETROSPECTIVE & BẢNG KÝ DUYỆT 10 VAI TRÒ HỘI ĐỒNG

### 5.1 Đánh giá và Rút kinh nghiệm Sprint 5 Retrospective
- **Những điểm thực hiện tốt:**
  - Quy trình kiểm soát dữ liệu nguồn 2 lớp của `[P3]` Trần Chí Kha (`CKPA-82`) và `[P2]` Trương Đình Hữu Tài (`CKPA-83`) đạt độ chính xác 100%, cách ly chuẩn 3 ca thiếu bảng biểu `DAT 08`.
  - Giữ vững kỷ luật No-Mock: Không chấp nhận các báo cáo giả lập, kiên quyết yêu cầu bằng chứng thật trên live endpoint và log thật từ kho ngoài.
- **Những điểm cần tập trung giải quyết ngay:**
  - Khẩn trương khắc phục lỗi rò rỉ đề bài 100 Sealed để bảo toàn tính độc lập của kỳ đánh giá Cổng G1.
  - Sớm cấp endpoint Staging và export log kho ngoài để đội Bảo mật [P5] hoàn tất các bài kiểm thử bị nghẽn.

---

### 5.2 BẢNG GHI NHẬN TRẠNG THÁI KÝ DUYỆT CỦA 10 THÀNH VIÊN HỘI ĐỒNG

*(Bảng phản ánh trung thực tiến độ thực tế: Các vai trò chưa hoàn tất sub-task hoặc đang vướng blocker được để trạng thái **PENDING**, không ký khống khi chưa giải tỏa lỗi kỹ thuật)*:

| Vai trò RFP | Họ và tên | Chức danh / Đại diện | Trạng thái Ký duyệt Hiện tại |
| :--- | :--- | :--- | :---: |
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ tịch Hội đồng Thẩm định & Nghiệm thu | *(Ký ban hành Bản dự thảo Rà soát & Quyết định HOLD)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | *(Đã ký duyệt Corpus & CKPA-83 / PENDING đồng duyệt CKPA-68)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | *(Đã ký duyệt dữ liệu CKPA-82 / PENDING chờ giải tỏa Blockers)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ SongNhat | **PENDING** *(Đang phối hợp cấp bộ 100 Sealed thay thế)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin & Quyền riêng tư | **PENDING** *(Chờ live endpoint tại CKPA-70 & log kho ngoài CKPA-79)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | **PENDING** *(Đang điều phối cấp live endpoint & hoàn thiện DEL 05)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | **PENDING** *(Đang thực hiện Swarming fix tại CKPA-76)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | **PENDING** *(Đang hỗ trợ fix route /api/v1/answer/)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Đảm bảo Chất lượng Độc lập | **PENDING** *(Báo cáo NEEDS_SIGNOFF tại CKPA-75, chờ retest tag v0.2.1)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hệ thống | **PENDING** *(Đang triển khai môi trường Staging & hỗ trợ S4)* |

---
*Văn kiện này là Bản dự thảo rà soát Cổng G1 phục vụ công tác đối soát kỹ thuật và giám sát dự án của Bên Mua. Lệnh giải ngân 25% và Quyết định mở Cổng G2 chỉ được ký ban hành chính thức sau khi toàn bộ 4 Blockers kỹ thuật được giải tỏa và Nhà cung cấp nộp đủ báo giá DEL 05 thực tế.*
