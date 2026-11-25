# BIÊN BẢN HỌP HỘI ĐỒNG RÀ SOÁT CỔNG GATE G1 (CONTROLLED OFFLINE PILOT), XÁC LẬP TRẠNG THÁI HOLD, DỰ THẢO LỆNH GIẢI NGÂN MỐC 2 (25%) & SPRINT 5 REVIEW / RETROSPECTIVE LOG

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
> **Thời điểm tổ chức phiên họp:** Ngày 25/11/2026 (09:00 – 11:30 Giờ Việt Nam — UTC+7)  
> **Trạng thái Văn kiện:** **BIÊN BẢN HỌP HỘI ĐỒNG RÀ SOÁT CỔNG G1 & SPRINT 5 RETROSPECTIVE**  
> **Nghị quyết Cổng G1:** **TẠM DỪNG CHỜ GIẢI TỎA (HOLD / PENDING_G1_BLOCKERS) — TIẾP TỤC GIỮ THẺ JIRA `CKPA-81` VÀ `CKPA-84` Ở TRẠNG THÁI `IN PROGRESS`**

---

## MỤC LỤC BIÊN BẢN HỌP HỘI ĐỒNG RÀ SOÁT

- **PHẦN 1: THÔNG TIN PHIÊN HỌP HỘI ĐỒNG VÀ ĐIỂM DANH 10 VAI TRÒ NGÀY 25/11/2026**
- **PHẦN 2: TIẾP NHẬN BÁO CÁO VÀ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐẦU VÀO**
- **PHẦN 3: BẢNG ĐỐI SOÁT TRUNG THỰC 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)**
- **PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H THEO DEL 05 & HIỆN TRẠNG 216H DONE / 60H IN PROGRESS)**
- **PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG KHẮC PHỤC)**
- **PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (360H / 3 GIAI ĐOẠN / 30 TASKS — [P3] CHUẨN 28H)**
- **PHẦN 7: NGHỊ QUYẾT HỘI ĐỒNG: XÁC LẬP TRẠNG THÁI HOLD, GIỮ JIRA IN PROGRESS VÀ TREO LỆNH GIẢI NGÂN 25%**
- **PHẦN 8: BẢNG KÝ DUYỆT XÁC NHẬN CỦA 10 THÀNH VIÊN HỘI ĐỒNG DỰ ÁN**

---

# PHẦN 1: THÔNG TIN PHIÊN HỌP HỘI ĐỒNG VÀ ĐIỂM DANH 10 VAI TRÒ NGÀY 25/11/2026

Phiên họp Hội đồng Rà soát Cổng G1 và Đánh giá Tổng kết Sprint 5 được triệu tập và chủ trì chính thức bởi Chủ đầu tư:

| Trường thông tin phiên họp | Giá trị ghi nhận thực tế | Ghi chú kiểm tra |
|---|---|---|
| **Thời gian họp** | 09:00 – 11:30, Ngày 25/11/2026 (Giờ Hà Nội — UTC+7) | Phiên họp rà soát cuối Sprint 5 |
| **Hình thức & Địa điểm** | Họp tập trung kết hợp trực tuyến tại Trụ sở Công ty Cổ phần Thiết bị Công nghiệp Song Nhật | Kênh bảo mật nội bộ, có ghi âm và lưu trữ nhật ký |
| **Chủ tọa phiên họp** | **[P1] Vắn Mỹ Vân** (Purchaser Sponsor / Product Owner) | Đại diện có thẩm quyền cao nhất của Bên mua |
| **Thư ký / Báo cáo kỹ thuật** | **[S1] Hoàng Tiến** (Named Lead / Scrum Master) | Đại diện quản lý Nhà cung cấp |
| **Mục đích phiên họp** | 1. Tiếp nhận và đối soát thực tế Hồ sơ Bằng chứng DEL 03 Part 1.<br>2. Kiểm tra độc lập 7 tiêu chí Cổng G1-AC01..07 dựa trên log thực tế.<br>3. Đối soát giờ công W1–W3 (276h theo DEL 05) và ghi nhận tiến độ 216h Done / 60h In Progress.<br>4. Đánh giá Sprint 5 Review/Retro và xác lập 4 Blockers kỹ thuật.<br>5. Nghị quyết xác lập trạng thái HOLD, thống nhất giữ CKPA-81 và CKPA-84 ở `In Progress`, treo Lệnh giải ngân 25%. | Tuân thủ nghiêm ngặt Mục 9, 11, 12 RFP & nguyên tắc No-Mock |

### Điểm danh 10 vai trò chuẩn RFP (Đảm bảo 100% có mặt tham gia phiên họp rà soát):

1. **Phía Chủ đầu tư / Bên mua (Purchaser — 5 vai trò):**
   - **`[P1]` Vắn Mỹ Vân** — Purchaser Sponsor / Product Owner *(Chủ tọa Hội đồng — Có mặt)*.
   - **`[P2]` Trương Đình Hữu Tài** — Policy Owners / Policy Reviewer #1 *(Thành viên — Có mặt)*.
   - **`[P3]` Trần Chí Kha** — Knowledge & Data Steward *(Thành viên kiểm soát dữ liệu — Có mặt)*.
   - **`[P4]` Ngô Thị Trà My** — Staff Users Representative *(Thành viên điều phối 5 Rep Users — Có mặt)*.
   - **`[P5]` Nguyễn Anh Khoa** — Privacy & Security Owners *(Thành viên thẩm định An toàn/Bảo mật — Có mặt)*.
2. **Phía Nhà thầu / Nhà cung cấp (Supplier — 5 vai trò):**
   - **`[S1]` Hoàng Tiến** — Named Lead / Scrum Master *(Thành viên báo cáo quản lý — Có mặt)*.
   - **`[S2]` Trần Quốc Hưng** — Integration Engineer *(Thành viên kỹ thuật tích hợp — Có mặt)*.
   - **`[S3]` Phạm Lương Yến Nhi** — Retrieval & App Engineer *(Thành viên kỹ thuật RAG/Prompt — Có mặt)*.
   - **`[S4]` Phạm Quý Hải** — Quality Lead / Independent QA *(Thành viên kiểm định độc lập — Có mặt)*.
   - **`[S5]` Nguyễn Ngọc Duy** — Operations Specialist *(Thành viên vận hành hạ tầng — Có mặt)*.

---

# PHẦN 2: TIẾP NHẬN BÁO CÁO VÀ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐẦU VÀO

Hội đồng Nghiệm thu tổng hợp và tiếp nhận trung thực các văn kiện, biên bản chuyên môn cấu thành hồ sơ Cổng G1 tính đến ngày 25/11/2026:

### 2.1. Tiếp nhận Hồ sơ Bằng chứng DEL 03 Part 1 từ `CKPA-80` (`[S1]` Hoàng Tiến — Đã Done)
- Căn cứ Báo cáo tổng hợp `CKPA-80` (CRM-G1-SUB27), Nhà cung cấp đã nộp Hồ sơ Bằng chứng DEL 03 Part 1 phản ánh kết quả phát triển qua 3 Sprint (W1, W2, W3).
- Mã nguồn hệ thống hiện đang đóng băng tại tag **`v0.2.0-g1-offline`**.
- **Ghi nhận thực tế kỹ thuật:** PR #33 bên repo Supplier hiện đang mở (OPEN) ở trạng thái **`NEEDS_SIGNOFF`** do phát hiện lỗi thiếu bảng passages trong fresh-DB Alembic migration. Nhà cung cấp đang chuyển giao 5 khiếm khuyết `DEF-CKPA75-01..05` sang nhóm Swarming tại `CKPA-76` để khắc phục. Tag `v0.2.1-g1-offline` chưa được phát hành chính thức.

### 2.2. Tiếp nhận Kết quả Kiểm lại 100% source_uri từ `CKPA-82` (`[P3]` Trần Chí Kha — Đã Done)
- Căn cứ Biên bản và Nhật ký tái thẩm định `CKPA-82` (PR #52 & PR #55 đã merge vào nhánh `develop`), toàn bộ **136 / 136 bản ghi** dữ liệu Full Corpus (96 Passages + 40 Critical Fields) và **56 / 56 bản ghi** Family 1 đều tồn tại thực tế trên hệ thống lưu trữ, mở xem trực tiếp thành công, khớp 100% mã băm SHA-256.
- Đạt **0 liên kết hỏng (0 broken links)** và thực thi cơ chế cách ly kiểm soát bảng biểu **`DAT 08`**: 96 Passages = 93 Accepted + 3 Quarantined (cách ly đúng 3 ca thử nghiệm cố ý thiếu bảng biểu: `PAS-040`, `PAS-066`, `PAS-082`). Toàn bộ 40/40 trường trọng yếu đạt Accepted.

### 2.3. Tiếp nhận Thẩm định Chuyên môn Policy Reviewer #1 từ `CKPA-83` (`[P2]` Trương Đình Hữu Tài — Đã nộp PR #54)
- Căn cứ Biên bản chuyên môn `CKPA-83` (PR #54 trên `develop`), Policy Reviewer #1 xác nhận:
  1. Quy tắc Ngày hiệu lực chi phối (**`OPS 03`**) chuẩn hóa theo múi giờ Việt Nam (`UTC+7`), ranh giới ngày `2026-11-06 09:00:00 UTC+7` phân tách chính xác giữa phiên bản lịch sử `VER-000` (`superseded` kèm nhãn *"Hướng dẫn lịch sử"*) và bản hiện hành `VER-001` (`effective`). Khóa hoàn toàn bản tương lai `VER-002` (`scheduled`, 2027) đối với các sự kiện năm 2026.
  2. Toàn bộ 136 bản ghi khai báo đủ **6 chiều ngữ cảnh bắt buộc** (`DAT 04`): `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`.
  3. Chuẩn hóa chính xác 40 trường trọng yếu (`OPS 04`), không thực hiện tính toán số học qua LLM (`llm_used=False`).
  4. Mã hóa chuẩn 4 kịch bản **HOLD / Fail-Closed**: Quarantine Hold, Conflict Hold (xung đột hợp đồng/OEM trích dẫn song song, cấm tự suy diễn thứ bậc ưu tiên), Evidence Hold (mờ tem/mất phiếu lập Local Referral trong 8h làm việc), và Từ chối suy luận từ `staff_note` (`ANS 05/06`).
  *Lưu ý: Thẩm định đã hoàn tất ở cấp Policy Reviewer #1, đang chờ đối soát đồng bộ cùng kết quả kiểm tra tại CKPA-68.*

### 2.4. Tiếp nhận Báo cáo Kiểm toán An toàn & Quyền riêng tư từ `CKPA-79` (`[P5]` Nguyễn Anh Khoa — In Progress)
- Phần 1 (Kiểm toán Kho nội bộ): Đạt chuẩn **0% PII thật** trên 100% tài liệu và bộ câu hỏi (tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và `SEC 02`), xác nhận 0 tệp/bản ghi Sealed lọt vào kho chung.
- Phần 2 (Kiểm toán Kho ngoài `sealed-eval-repo`): Nhật ký `g1_sealed_acl_audit_CKPA-79.log` đang ghi nhận trạng thái **`BLOCKED_EXTERNAL_REPO_ACCESS`** do đang chờ `[S4]/[S5]` xuất tệp danh sách Collaborators và GitHub Audit Log thực tế từ kho ngoài `sealed-eval-repo` (SUB03) để chạy đối chiếu `--strict-external`.

---

# PHẦN 3: BẢNG ĐỐI SOÁT TRUNG THỰC 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)

Hội đồng đối soát trung thực từng tiêu chí chấp nhận kỹ thuật Cổng G1 dựa trên bằng chứng log và hiện trạng thực tế ngày 25/11/2026:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát | Kết luận Đối soát Hội đồng |
|:---:|---|---|---|:---:|
| **`G1-AC01`** | **Toàn vẹn Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..DOC-011) thuộc 3 họ POL-001/002/003 và 5 lớp thẩm quyền DAT 03; dưới 300 đoạn văn (thực tế 96); dưới 50 trường (thực tế 40); 100% source_uri khớp SHA-256; DAT 08 cân bằng 93 Acc + 3 Qua. | Biên bản CKPA-82 của [P3], PR #52 & PR #55 merged trên develop; Xác nhận CKPA-83 của [P2]; Manifest 136 bản ghi checksum SHA-256 sạch. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Validators, Reconciliation & Benchmark Offline OPS 01** | 2 Base CSV Validators; Quarantine tự động; Full-Snapshot Reconciliation (Expected = Accepted + Quarantined); Benchmark OPS 01 trên 500 dòng đạt thời gian xử lý <= 30 phút; LKG đạt 100%. | CKPA-52 (PR #26), CKPA-59 (PR #28), CKPA-60 (PR #29: 0.3738s, LKG 100%); Tuy nhiên bộ 100 SEALED hiện tại bị cảnh báo lộ nguồn lúc 12:07 25/11 (CKPA-67) cần thay thế; CKPA-68 đang In Progress; tag v0.2.1-g1-offline chưa ban hành. | **CHỜ GIẢI TỎA<br>(HOLD / PENDING_SEALED)** |
| **`G1-AC03`** | **Immediate Withdrawal & Khóa O1 Mặc định (Base Scope)** | Rút hồi/thu hồi tài liệu có hiệu lực tức thì (commit trạng thái trước khi ack); Fail-closed đối với tài liệu đã thu hồi (SEC 01, SEC 02, SEC 05, KNW 04); Khóa cứng Option O1 trong Base Scope (OPTION_O1_ENABLED = False, DAT 07). | Đã lập trình mã nguồn tại CKPA-59 (PR #28); Tuy nhiên nhật ký kiểm toán CKPA-70 `g1_rbac_failclosed_audit_CKPA-70.log` ghi nhận `BLOCKED_NO_LIVE_ENDPOINT` (lệch dấu / ở /api/v1/answer/), cần live endpoint nội bộ để xác nhận runtime. | **CHỜ GIẢI TỎA<br>(HOLD / BLOCKED_ENDPOINT)** |
| **`G1-AC04`** | **Pre-retrieval RBAC 4 Vai trò & 7 Trạng thái Vòng đời** | Thực thi RBAC 4 vai trò (reader, policy_owner, steward, administrator) tại tầng Pre-Retrieval (SEC 01); Quản lý đúng 7 trạng thái KNW 03; 0% rò rỉ link/citation/cache/log khi bị từ chối truy cập. | Đã tích hợp mã nguồn tại CKPA-46, CKPA-54; Tuy nhiên nhật ký `g1_rbac_failclosed_audit_CKPA-70.log` thực tế đạt `OVERALL VERDICT: PARTIAL_PASS` (0/4 PASS_VERIFIED, 4/4 BLOCKED do thiếu live endpoint runtime). | **CHỜ GIẢI TỎA<br>(HOLD / PARTIAL_PASS)** |
| **`G1-AC05`** | **Governing Date UTC+7 (OPS 03) & Khớp 6 Chiều DAT 04** | Phân giải ngày sự kiện theo múi giờ Việt Nam UTC+7; Ranh giới lịch sử 2026-11-06T09:00:00+07:00; Khớp chính xác 6 chiều ngữ cảnh DAT 04; Tự động chuyển HOLD khi thiếu ngày chi phối. | CKPA-62 (Done), CKPA-63 (PR #23: unit test PASS); Thẩm định chuyên môn CKPA-83 của [P2]; Tuy nhiên PR #33 (CKPA-75) bên Supplier OPEN ở `NEEDS_SIGNOFF`, đang swarming xử lý DEF-CKPA75-01..05 tại CKPA-76. | **CHỜ GIẢI TỎA<br>(HOLD / NEEDS_SIGNOFF)** |
| **`G1-AC06`** | **Deterministic Field Lookup (DAT 06) & Cơ chế HOLD** | Tra cứu trường trọng yếu định lượng qua Python Decimal thuần (0% số học qua LLM); Tự động kích hoạt HOLD khi thiếu bảng/chú thích (DAT 08) hoặc xung đột nguồn văn bản (DAT 05, OPS 04). | CKPA-63 (PR #23: Decimal thuần, llm_used=False, auto HOLD 4 kịch bản); Biên bản thẩm định CKPA-83 của [P2]; CKPA-78 của [S3] đã merge. | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Bộ 200 Real Tasks, 80 Challenges & Cô lập Môi trường** | Môi trường Test tách Prod (SEC 06); 0% PII thật (SEC 02); Kho ngoài sealed-eval-repo chặn S2/S3; Bộ 200 câu hỏi thực tế (60 Dev / 40 Val / 100 Sealed) + 80 Challenges (40 VN 02); 5 Rep Users độc lập. | 0% PII pass (CKPA-47); Tuy nhiên log `g1_sealed_acl_audit_CKPA-79.log` Part 2 đang `BLOCKED_EXTERNAL_REPO_ACCESS` (chưa có log kho ngoài) và sự cố cảnh báo lộ nguồn 100 câu hỏi Sealed tại CKPA-67 (12:07 25/11). | **CHỜ GIẢI TỎA<br>(HOLD / BLOCKED_AUDIT)** |

> **KẾT LUẬN ĐỐI SOÁT HỘI ĐỒNG:** Hiện tại đạt **2 / 7 tiêu chí (G1-AC01, G1-AC06 PASS)**; 5 tiêu chí còn lại (**G1-AC02, G1-AC03, G1-AC04, G1-AC05, G1-AC07**) đang ở trạng thái **TẠM DỪNG CHỜ GIẢI TỎA (HOLD / PENDING_G1_BLOCKERS)** do vướng 4 Blockers kỹ thuật chưa thể nghiệm thu ngay.

---

# PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H THEO DEL 05 & 10 VAI TRÒ)

Căn cứ quy định tại Mục 10, Mục 11 RFP và hồ sơ định mức DEL 05 đã chuẩn hóa tại `CKPA-80`, Hội đồng đối soát giờ công lũy kế Cổng G1 tính đến thời điểm họp ngày 25/11/2026:

### Bảng Tổng hợp Giờ công G1 Kế hoạch (DEL 05) vs Hiện trạng Thực tế:

| Mã Role | Họ và tên thành viên | Phía RFP | W1 (Sprint 3) | W2 (Sprint 4) | W3 (Sprint 5) | Tổng KH G1 | Thực tế Đã Done | Đang xử lý (In Progress) | Nhịp bền vững (<= 40h/w) |
|---|---|---|---:|---:|---:|---:|---:|---:|:---:|
| **`[P1]`** | Vắn Mỹ Vân | Purchaser | 0h | 0h | 4h | **4h** | **0h** | 4h | Đạt (Max 4h/w <= 40h) |
| **`[P2]`** | Trương Đình Hữu Tài | Purchaser | 8h | 12h | 4h | **24h** | **20h** | 4h | Đạt (Max 12h/w <= 40h) |
| **`[P3]`** | Trần Chí Kha | Purchaser | 16h | 8h | 12h | **36h** | **36h** | 0h | Đạt (Max 16h/w <= 40h) |
| **`[P4]`** | Ngô Thị Trà My | Purchaser | 16h | 16h | 0h | **32h** | **32h** | 0h | Đạt (Max 16h/w <= 40h) |
| **`[P5]`** | Nguyễn Anh Khoa | Purchaser | 8h | 8h | 12h | **28h** | **16h** | 12h | Đạt (Max 12h/w <= 40h) |
| **Cộng Bên Mua** | **5 vai trò Purchaser** | **Purchaser** | **48h** | **44h** | **32h** | **124h** | **104h** | **20h** | **Đạt chuẩn nhịp độ** |
| **`[S1]`** | Hoàng Tiến | Supplier | 0h | 8h | 8h | **16h** | **8h** | 8h | Đạt (Max 8h/w <= 40h) |
| **`[S2]`** | Trần Quốc Hưng | Supplier | 8h | 16h | 4h | **28h** | **24h** | 4h | Đạt (Max 16h/w <= 40h) |
| **`[S3]`** | Phạm Lương Yến Nhi | Supplier | 16h | 24h | 4h | **44h** | **44h** | 0h | Đạt (Max 24h/w <= 40h) |
| **`[S4]`** | Phạm Quý Hải | Supplier | 12h | 12h | 16h | **40h** | **24h** | 16h | Đạt (Max 16h/w <= 40h) |
| **`[S5]`** | Nguyễn Ngọc Duy | Supplier | 16h | 8h | 0h | **24h** | **12h** | 12h | Đạt (Max 16h/w <= 40h) |
| **Cộng Nhà Thầu** | **5 vai trò Supplier** | **Supplier** | **52h** | **68h** | **32h** | **152h** | **112h** | **40h** | **Đạt chuẩn nhịp độ** |
| **TOÀN DỰ ÁN** | **10 Vai trò chuẩn RFP** | **Toàn thể** | **100h** | **112h** | **64h** | **276h** | **216h (78.3%)** | **60h (21.7%)** | **100% tuân thủ nhịp độ** |

### Xác nhận đối soát tiến độ và quyết toán:
1. **Khung định mức chuẩn:** Tổng thời lượng định mức Cổng G1 là **276 giờ** (Tuần 1: 100h, Tuần 2: 112h, Tuần 3: 64h), khớp chính xác với ma trận phân bổ công việc `PhanCongCongViec_G1.xlsx` (DEL 05) và Epic `CKPA-44`. Con số nháp 372h ghi nhận tại mô tả cũ đã chính thức được bãi bỏ.
2. **Tiến độ ghi nhận thực tế trên Jira ngày 25/11/2026:**
   - Đã hoàn tất và đóng thẻ (Done): **216 giờ / 276 giờ** (đạt **78.3%**).
   - Đang trong quá trình xử lý (In Progress): **60 giờ / 276 giờ** (chiếm **21.7%**), tương ứng với các sub-tasks kỹ thuật đang giải tỏa lỗi (CKPA-65, CKPA-67, CKPA-68, CKPA-69, CKPA-70, CKPA-73, CKPA-75, CKPA-76, CKPA-77, CKPA-79, CKPA-83, CKPA-84).
   - Tổng quyết toán 100% (276h) sẽ được Hội đồng phê duyệt chính thức sau khi toàn bộ 11+ sub-tasks hoàn tất và các Blockers kỹ thuật được giải tỏa.
3. **Tuân thủ nhịp độ làm việc bền vững (Sustainable Pace):** Toàn bộ 10 thành viên có mức tải tối đa trong tuần không vượt quá **24 giờ/tuần** (thấp hơn nhiều so với ngưỡng trần 40 giờ/tuần theo quy định Scrum/RFP) và không quá 8 giờ/ngày.

---

# PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG KHẮC PHỤC)

### 5.1. Sprint 5 Review — Đánh giá Kết quả Đạt được (What Went Well)
1. **Đóng gói kỹ thuật chính xác & kỷ luật kiểm soát:** Đã đóng băng tag phát hành `v0.2.0-g1-offline`; nhóm phát triển đang thực hiện swarming sửa lỗi độc lập tại `CKPA-76` để xử lý dứt điểm các lỗi migration trước khi phát hành tag cập nhật.
2. **Quy trình kiểm soát dữ liệu nguồn 2 lớp hiệu quả:** Sự kết hợp độc lập giữa `[P3]` Trần Chí Kha (kiểm tra liên kết vật lý & SHA-256 tại CKPA-82) và `[P2]` Trương Đình Hữu Tài (thẩm định chính sách, ngày hiệu lực & cơ chế HOLD tại CKPA-83) đã phát hiện và cách ly chuẩn xác 3 ca thiếu bảng biểu `DAT 08`.
3. **Thực thi triệt để nguyên tắc tách vai (Chinese Wall & SoD):** Bảo vệ an toàn kho riêng `sealed-eval-repo`, QA Lead `[S4]` độc lập tuyệt đối với code của `S2/S3`, 5 Người dùng đại diện thuộc 100% Bên mua ngoài nhóm kỹ sư, và 100% Story/Sub-tasks tuân thủ nguyên tắc `Assignee != Reporter`.
4. **Vệ sinh quản trị và kiểm thử tự động:** Toàn bộ tài liệu được dọn sạch rác citation AI, 100% UTF-8 không lỗi font, CI Guard vận hành ổn định chạy tự động toàn bộ 96 tệp đạt PASS.

### 5.2. Sprint 5 Retrospective — Các Điểm Cần Tối Ưu (What Could Be Improved)
1. **Khắc phục sự cố lộ nguồn câu hỏi kiểm định:** Việc nguồn 100 câu hỏi Sealed bị công khai cần được xử lý triệt để bằng cách cấp bộ câu hỏi thay thế độc lập mới từ `[P4]`, đảm bảo tính toàn vẹn của cổng đánh giá.
2. **Tốc độ đồng bộ môi trường Runtime:** Đội kiểm toán bảo mật `[P5]` cần được cấp phát endpoint API thực tế nội bộ sớm để giải tỏa tình trạng `BLOCKED_NO_LIVE_ENDPOINT` tại CKPA-70.
3. **Hỗ trợ trích xuất nhật ký kho ngoài:** `[S4]` và `[S5]` cần sớm xuất tệp Collaborators / GitHub Audit Log thực tế từ `sealed-eval-repo` để `[P5]` giải tỏa `BLOCKED_EXTERNAL_REPO_ACCESS` tại CKPA-79.

### 5.3. Bảng Hành động Khắc phục (Action Items)

| Mã Action | Nội dung Hành động Cụ thể | Người chịu trách nhiệm | Hạn hoàn thành | Tiêu chí nghiệm thu |
|---|---|---|---|---|
| **`RETRO-S5-01`** | Duy trì cờ `OPTION_O1_ENABLED = False`, khóa toàn bộ tính năng thử nghiệm ngoài Base Scope. | `[S2]` Quốc Hưng & `[S5]` Ngọc Duy | Ngay | File cấu hình `backend/src/config.py` được `[P5]` xác nhận |
| **`RETRO-S5-02`** | Cung cấp endpoint Runtime nội bộ và sửa lỗi định tuyến `/api/v1/answer/` để `[P5]` hoàn tất audit CKPA-70. | `[S1]` Hoàng Tiến & `[S5]` Ngọc Duy | 26/11/2026 | Log `g1_rbac_failclosed_audit_CKPA-70.log` chuyển từ BLOCKED sang PASS |
| **`RETRO-S5-03`** | Xuất tệp Collaborators & GitHub Audit Log từ kho riêng `sealed-eval-repo` phục vụ kiểm toán đối chiếu `--strict-external`. | `[S4]` Quý Hải & `[S5]` Ngọc Duy | 26/11/2026 | Log `g1_sealed_acl_audit_CKPA-79.log` Part 2 chuyển sang PASS |
| **`RETRO-S5-04`** | Cung cấp bộ câu hỏi thay thế độc lập cho 100 câu Sealed và hoàn tất thẩm định 2 Policy Reviewers tại CKPA-68. | `[P4]` Trà My, `[P2]` Tài & `[P3]` Kha | 26/11/2026 | Biên bản đồng thuận CKPA-68 chuyển Done |

---

# PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (360H / 3 GIAI ĐOẠN / 30 TASKS)

Căn cứ Kế hoạch triển khai đã đồng bộ từ `PhanCongCongViec_G2_ChuanJira_RFP.xlsx` (DEL 05) tại `CKPA-80`, kế hoạch dự kiến Sprint 6 (Cổng G2 Live Pilot) có tổng dự toán **360 giờ** phân bổ cho 10 vai trò qua 3 giai đoạn:

1. **Giai đoạn 1 (Ngày 1–2 Sprint 6 — Build Workspace, Lifecycle, Ops & Legal Prep — 144h):**
   - **WP 04 Answer Package & Guardrails (`[S3]` Yến Nhi, 40h):** Answer Package chuẩn 100–250 từ, các trường cấu trúc cứng ANS 03-04; Local Referral và 9 kịch bản Annex B (KNW 05); chống Prompt Injection & khóa Streaming ANS 08.
   - **WP 04 Lifecycle & Feedback (`[S2]` Quốc Hưng, 38h):** Vòng đời 7 trạng thái và hiệu lực lịch KNW 03; ngăn chặn Stale Answer khi thu hồi (KNW 04); phân loại phản hồi và trích xuất ứng viên tri thức (KNW 06-07).
   - **Vận hành & Dự phòng (`[S5]` Ngọc Duy, 24h):** Xóa cache vật lý tự động <= 5 phút và cơ chế Fail-Closed (OPS 05); quy trình Emergency Disable và tìm kiếm dự phòng Mục 9.
   - **Pháp lý, Bảo mật, Dữ liệu & Đóng gói (42h):**
     - `[P5]` Anh Khoa (24h): Lập luận rủi ro AI Annex F; quy trình báo cáo sự cố trong 4h và Change Control (SEC 03-08).
     - `[P2]` Hữu Tài (10h): Rà soát chính sách triển khai G2.
     - **`[P3]` Trần Chí Kha (6h):** Rà soát dữ liệu và kiểm soát thay đổi (khớp chính xác task Jira **`CKPA-96`**: 6h).
     - `[P4]` Trà My (10h): Diễn tập thu hồi và đào tạo 5 Rep Users.
     - `[S1]` Hoàng Tiến (12h): Đóng gói Working Core DEL 02.

2. **Giai đoạn 2 (Ngày 3–4 Sprint 6 — Kiểm định Độc lập 180 Ca & Đào tạo — 142h):**
   - **Kiểm định Hiệu năng & QA Độc lập (`[S5]` 12h, `[S4]` Quý Hải 40h):** Benchmark 5 người dùng đồng thời, p95 <= 25s trên 100 truy vấn (OPS 02); kiểm thử 80 Challenges; chấm điểm 100 câu Sealed; lập Báo cáo Điểm số Độc lập DEL 03.
   - **Thẩm định Độc lập phía Bên Mua (80h):**
     - `[P2]` Hữu Tài (26h): Chấm độc lập điều khoản, ngoại lệ, ngày chi phối.
     - **`[P3]` Trần Chí Kha (18h):** Thẩm định độc lập nguồn dữ liệu và tri thức (khớp chính xác 2 task Jira: **`CKPA-108`**: 14h và **`CKPA-111`**: 4h).
     - `[P4]` Trà My (24h): Đánh giá tính hữu ích và mức độ chỉnh sửa nhỏ >= 80%.
     - `[P5]` Anh Khoa (10h): Xác nhận 0 lỗi rò rỉ dữ liệu trên 180 ca.
   - **Đệ trình Hồ sơ G2 (`[S1]` 10h):** Tổng hợp Hồ sơ Điểm số Độc lập và Căn cứ Pháp lý G2.

3. **Giai đoạn 3 (Ngày 5 Sprint 6 — Hội đồng Nghiệm thu G2 & Kích hoạt Pilot G3 — 74h):**
   - **Báo cáo Quyết toán (`[S1]` 10h):** Lập báo cáo giờ công Tuần 4 và kế hoạch 20 ngày quan sát G3.
   - **Rà soát Hồ sơ Cổng (`[P3]` 4h):** Khớp chính xác task Jira **`CKPA-117`**: 4h.
   - **Hội đồng Thẩm định & Nghiệm thu G2 (`[P1]` Mỹ Vân 30h):** Chủ trì Hội đồng đánh giá 8 tiêu chí Cổng G2; ký lệnh kích hoạt 20 ngày sử dụng có giám sát; ký Biên bản G2 và lệnh giải ngân Mốc 3 (25%).
   - **Kiểm định Đóng Cổng (`[S4]` 15h, `[S5]` 15h):** Kiểm tra kỹ thuật chốt cổng G2.

> **XÁC NHẬN KHỚP GIỜ [P3] TRẦN CHÍ KHA TRONG SPRINT 6:**  
> Tổng giờ Sprint 6 của `[P3]` là **28 giờ**, khớp chính xác 100% với 4 tasks trên hệ thống Jira G2:  
> - `CKPA-96`: 6 giờ  
> - `CKPA-108`: 14 giờ  
> - `CKPA-111`: 4 giờ  
> - `CKPA-117`: 4 giờ  
> *(Tổng cộng: 6h + 14h + 4h + 4h = 28h)*.

---

# PHẦN 7: NGHỊ QUYẾT HỘI ĐỒNG: XÁC LẬP TRẠNG THÁI HOLD, GIỮ JIRA IN PROGRESS VÀ TREO LỆNH GIẢI NGÂN 25%

Căn cứ kết quả đối soát thực tế tại phiên họp ngày 25/11/2026 (mới đạt 2/7 tiêu chí, 5 tiêu chí còn lại đang chờ xử lý lỗi kỹ thuật và bổ sung bằng chứng log), Hội đồng Nghiệm thu Cổng G1 do **`[P1]` Vắn Mỹ Vân** chủ trì thống nhất quyết nghị:

### 7.1. Xác lập Trạng thái Nghiệm thu Cổng Gate G1
- Hội đồng thống nhất **CHƯA ĐÓNG CỔNG G1**, chính thức xác lập trạng thái Cổng G1 là **TẠM DỪNG CHỜ GIẢI TỎA (HOLD / PENDING_G1_BLOCKERS)**.
- Thống nhất theo đề nghị của `[P3]` Trần Chí Kha: **Tiếp tục giữ User Story cha `CKPA-81` và Sub-task `CKPA-84` ở trạng thái `In Progress` trên Jira**, tuyệt đối không đóng thẻ khống khi chưa giải tỏa dứt điểm 4 Blockers kỹ thuật.
- Phiên họp tái thẩm định và ký chốt Cổng G1 sẽ được triệu tập ngay sau khi các Blockers được đóng.

### 7.2. Bốn (04) Blockers Kỹ thuật Bắt buộc phải Giải tỏa trước khi Chuyển tiếp G2:
1. `[P4]` Ngô Thị Trà My hoàn tất cấp phát bộ câu hỏi thay thế độc lập cho 100 câu Sealed và hoàn thành thẩm định chuyên môn đồng thuận tại `CKPA-68`.
2. `[S1]` Hoàng Tiến và `[S5]` Nguyễn Ngọc Duy hoàn tất cấp phát endpoint Staging nội bộ, sửa lỗi định tuyến `/api/v1/answer/` để `[P5]` chạy kiểm toán lại và chuyển `CKPA-70` sang PASS hoàn toàn.
3. `[S2]` Trần Quốc Hưng hoàn tất swarming tại `CKPA-76`, khắc phục triệt để các lỗi migration fresh-DB và đạt xác nhận retest độc lập từ `[S4]` trên tag bản vá mới.
4. `[S4]` Phạm Quý Hải và `[S5]` Nguyễn Ngọc Duy xuất đầy đủ tệp Collaborators & GitHub Audit Log thực tế từ kho ngoài `sealed-eval-repo` để `[P5]` hoàn tất kiểm toán `--strict-external` tại `CKPA-79`.

### 7.3. Dự thảo Lệnh Giải ngân Thanh toán Mốc 2 (25% Giá trị Hợp đồng Base Scope)
- Căn cứ quy định tại Mục 12 RFP và Hợp đồng Dịch vụ Phần mềm:
  1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
  2. **Tỷ lệ giải ngân quy định:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT).
  3. **Công thức xác định giá trị thanh toán thực tế:**
     `Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)`
  4. **Điều kiện Tiên quyết Giải ngân (ĐIỀU KIỆN TREO — PENDING_SUPPLIER_QUOTE):**
     - Dự thảo Lệnh giải ngân 25% này **TẠM TREO HIỆU LỰC THI HÀNH**.
     - Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật **TUYỆT ĐỐI CHƯA GIẢI NGÂN** cho đến khi hội đủ cả 2 điều kiện bắt buộc:
       - **Điều kiện 1:** Toàn bộ 4 Blockers kỹ thuật nêu tại Mục 7.2 được giải tỏa hoàn toàn và Hội đồng ký Biên bản Nghiệm thu Cổng G1 chính thức.
       - **Điều kiện 2:** Nhà cung cấp hoàn tất nộp Bảng giá Thương mại DEL 05 chính thức với đầy đủ **14 dòng đơn giá VND + thuế VAT thực tế** tại task `CKPA-39` (xóa bỏ hoàn toàn trạng thái `PENDING_SUPPLIER_QUOTE`, tuyệt đối không sử dụng bảng số liệu minh họa của Phụ lục E, nhất quán với nguyên tắc tại `CKPA-42`).

---

# PHẦN 8: BẢNG KÝ DUYỆT XÁC NHẬN CỦA 10 THÀNH VIÊN HỘI ĐỒNG DỰ ÁN

*(Biên bản ghi nhận sự đồng thuận 10/10 thành viên tại phiên họp rà soát ngày 25/11/2026: Xác nhận đối soát trung thực hiện trạng, đồng thuận trạng thái HOLD, thống nhất giữ CKPA-81 và CKPA-84 ở `In Progress` và cam kết thực hiện Action Items giải tỏa Blockers)*:

| Vai trò chuẩn RFP | Họ và tên thành viên | Chức vụ / Đơn vị đại diện | Trách nhiệm xác nhận phiên họp | Chữ ký xác nhận ngày 25/11/2026 |
|---|---|---|---|:---:|
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ đầu tư — Song Nhật | Chủ tịch Hội đồng — Ban hành Biên bản Rà soát & Quyết nghị HOLD | *(Đã ký ban hành Biên bản Rà soát & HOLD)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | Xác nhận Tiêu chuẩn Chính sách & Cam kết đồng duyệt CKPA-68 | *(Đã ký xác nhận rà soát)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | Xác nhận 100% source_uri SHA-256 & Giám sát giải tỏa Blockers | *(Đã ký xác nhận rà soát)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ | Tiếp nhận xử lý cấp bộ 100 câu Sealed thay thế | *(Đã ký xác nhận rà soát)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin | Xác nhận 0% PII, chờ live endpoint CKPA-70 & log CKPA-79 | *(Đã ký xác nhận rà soát)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | Bàn giao DEL 03 Part 1, cam kết cấp live endpoint & hoàn thiện DEL 05 | *(Đã ký xác nhận rà soát)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | Cam kết hoàn tất Swarming sửa lỗi migration tại CKPA-76 | *(Đã ký xác nhận rà soát)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | Cam kết khắc phục định tuyến API & khóa cứng Base Scope | *(Đã ký xác nhận rà soát)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Kiểm định Độc lập | Độc lập kiểm định, cam kết retest bản vá mới & xuất log kho ngoài | *(Đã ký xác nhận rà soát)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hạ tầng | Cam kết cấp môi trường Staging nội bộ & hỗ trợ xuất log kho ngoài | *(Đã ký xác nhận rà soát)* |

---
*Biên bản này được lập thành 04 (bốn) bản gốc bằng tiếng Việt có giá trị pháp lý như nhau tại phiên họp rà soát ngày 25/11/2026. Lệnh giải ngân 25% và Quyết định chuyển tiếp mở Cổng G2 chỉ có hiệu lực thi hành sau khi toàn bộ 4 Blockers kỹ thuật được giải tỏa và Hội đồng ký ban hành Biên bản nghiệm thu chính thức.*
