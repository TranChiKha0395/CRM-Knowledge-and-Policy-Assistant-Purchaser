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
> **Thời điểm tổ chức & Ký ban hành:** Ngày 27/11/2026 (Hoàn tất đệ trình & đối soát ngày 24/11/2026 — Giờ Việt Nam UTC+7)  
> **Trạng thái Cổng G1:** **NGHIỆM THU CHÍNH THỨC — CHẤP THUẬN TOÀN DIỆN (APPROVED & PROCEED TO G2)**

---

## MỤC LỤC BIÊN BẢN HỌP HỘI ĐỒNG VÀ RETRO LOG

- **PHẦN 1: THÔNG TIN PHIÊN HỌP HỘI ĐỒNG VÀ ĐIỂM DANH 10 VAI TRÒ**
- **PHẦN 2: TIẾP NHẬN BÁO CÁO VÀ THẨM ĐỊNH TỪ CÁC SUB-TASKS ĐẦU VÀO**
- **PHẦN 3: BẢNG ĐỐI SOÁT CHI TIẾT 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)**
- **PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H THEO DEL 05 & 10 VAI TRÒ)**
- **PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG KHẮC PHỤC)**
- **PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (360H / 3 GIAI ĐOẠN / 30 TASKS)**
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
| **Mục đích phiên họp** | 1. Đánh giá kết quả bàn giao Hồ sơ Bằng chứng DEL 03 Part 1.<br>2. Kiểm tra độc lập 7 tiêu chí Cổng G1-AC01..07 (0 lỗi Critical Control).<br>3. Đối soát quyết toán định mức giờ công W1–W3 (276h).<br>4. Đánh giá Sprint 5 Review/Retro và thống nhất Kế hoạch Sprint 6 (G2).<br>5. Ký Biên bản Nghiệm thu G1, phê duyệt mở G2 và lệnh giải ngân 25%. | Tuân thủ nghiêm ngặt Mục 9, 11, 12 RFP |

### Điểm danh 10 vai trò chuẩn RFP (Đảm bảo 100% có mặt, tuân thủ nguyên tắc SoD):

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

### 2.1. Tiếp nhận Hồ sơ Bằng chứng DEL 03 Part 1 từ `CKPA-80` (`[S1]` Hoàng Tiến — Đã Done)
- Căn cứ Báo cáo tổng hợp `CKPA-80` (CRM-G1-SUB27), Nhà cung cấp đã hoàn thiện trọn bộ Hồ sơ Bằng chứng DEL 03 Part 1 phản ánh trung thực toàn bộ kết quả phát triển qua 3 Sprint (W1, W2, W3).
- Mã nguồn hệ thống đã được đóng băng tại tag **`v0.2.0-g1-offline`** và hoàn tất kiểm thử bản vá swarming **`v0.2.1-g1-offline`** tại `CKPA-76`, đảm bảo 100% khép kín môi trường nội bộ, không phụ thuộc kết nối Internet bên ngoài.

### 2.2. Tiếp nhận Kết quả Kiểm lại 100% source_uri từ `CKPA-82` (`[P3]` Trần Chí Kha — Đã Done)
- Căn cứ Biên bản và Nhật ký tái thẩm định `CKPA-82` (PR #52 & PR #55 merged trên `develop`), toàn bộ **136 / 136 bản ghi** dữ liệu Full Corpus (96 Passages + 40 Critical Fields) và **56 / 56 bản ghi** Family 1 đều tồn tại thực tế trên hệ thống lưu trữ, mở xem trực tiếp thành công, khớp 100% mã băm SHA-256.
- Đạt **0 liên kết hỏng (0 broken links)** và thực thi cơ chế cách ly kiểm soát bảng biểu **`DAT 08`**: 96 Passages = 93 Accepted + 3 Quarantined (cách ly đúng 3 ca thử nghiệm cố ý thiếu bảng biểu: `PAS-040`, `PAS-066`, `PAS-082`). Toàn bộ 40/40 trường trọng yếu đạt Accepted.

### 2.3. Tiếp nhận Thẩm định Chuyên môn Policy Reviewer #1 từ `CKPA-83` (`[P2]` Trương Đình Hữu Tài — Đã Done)
- Căn cứ Biên bản chuyên môn `CKPA-83` (PR #54 merged trên `develop`), Policy Reviewer #1 xác nhận:
  1. Quy tắc Ngày hiệu lực chi phối (**`OPS 03`**) chuẩn hóa theo múi giờ Việt Nam (`UTC+7`), ranh giới ngày `2026-11-06 09:00:00 UTC+7` phân tách chính xác giữa phiên bản lịch sử `VER-000` (`superseded` kèm nhãn *"Hướng dẫn lịch sử"*) và bản hiện hành `VER-001` (`effective`). Khóa hoàn toàn bản tương lai `VER-002` (`scheduled`, 2027) đối với các sự kiện năm 2026.
  2. Toàn bộ 136 bản ghi khai báo đủ **6 chiều ngữ cảnh bắt buộc** (`DAT 04`): `company`, `branch`, `role`, `customer_group`, `product`, `transaction_scope`.
  3. Chuẩn hóa chính xác 40 trường trọng yếu (`OPS 04`), không thực hiện tính toán số học qua LLM (`llm_used=False`).
  4. Mã hóa chuẩn 4 kịch bản **HOLD / Fail-Closed**: Quarantine Hold, Conflict Hold (xung đột hợp đồng/OEM trích dẫn song song, cấm tự suy diễn thứ bậc ưu tiên), Evidence Hold (mờ tem/mất phiếu lập Local Referral trong 8h làm việc), và Từ chối suy luận từ `staff_note` (`ANS 05/06`).

### 2.4. Tiếp nhận Chứng nhận Kiểm toán ACL & Bảo vệ Quyền riêng tư từ `CKPA-79` (`[P5]` Nguyễn Anh Khoa)
- Đạt chuẩn **0% PII thật** trên 100% tài liệu và bộ câu hỏi (tuân thủ Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15 và `SEC 02`).
- Kiểm toán an toàn truy cập (ACL) xác nhận phân vùng kiểm định độc lập trong kho ngoài `sealed-eval-repo` được niêm phong tuyệt đối, ngăn chặn 100% quyền truy cập của các kỹ sư phát triển `S2/S3` (`SEC 06`).
- Quyền Pre-retrieval RBAC 4 vai trò (`reader`, `policy_owner`, `steward`, `administrator`) và 7 trạng thái vòng đời (`KNW 03`) được thực thi nghiêm ngặt, không rò rỉ liên kết, đoạn trích hay nội dung cache khi bị từ chối truy cập.

---

# PHẦN 3: BẢNG ĐỐI SOÁT CHI TIẾT 7/7 TIÊU CHÍ NGHIỆM THU CỔNG G1 (G1-AC01 .. G1-AC07)

Hội đồng đã tiến hành rà soát từng tiêu chí chấp nhận kỹ thuật và quản trị theo quy định tại Mục 9 RFP:

| Mã Tiêu chí | Tên Tiêu chí Cổng G1 | Yêu cầu Kỹ thuật Kiểm soát RFP | Bằng chứng Thực tế Đối soát | Kết luận Hội đồng |
|:---:|---|---|---|:---:|
| **`G1-AC01`** | **Toàn vẹn Curation Full Corpus 3 Họ Chính sách** | Đủ 11 tài liệu nguồn (DOC-001..DOC-011) thuộc 3 họ POL-001/002/003 và 5 lớp thẩm quyền DAT 03; dưới 300 đoạn văn (thực tế 96); dưới 50 trường (thực tế 40); 100% source_uri khớp SHA-256; DAT 08 cân bằng 93 Acc + 3 Qua. | Biên bản CKPA-82 của [P3], PR #52 & PR #55; Xác nhận CKPA-83 của [P2]; Manifest 136 bản ghi checksum sạch. | **ĐẠT (PASS)** |
| **`G1-AC02`** | **Validators, Reconciliation & Benchmark Offline OPS 01** | 2 Base CSV Validators; Quarantine tự động; Full-Snapshot Reconciliation (Expected = Accepted + Quarantined); Benchmark OPS 01 trên 500 dòng đạt thời gian xử lý <= 30 phút; LKG đạt 100%. | CKPA-52 (PR #26), CKPA-59 (PR #28), CKPA-60 (PR #29: thời gian đo 0.3738s <= 30p, LKG 100%); Tag v0.2.0 & v0.2.1. | **ĐẠT (PASS)** |
| **`G1-AC03`** | **Immediate Withdrawal & Khóa O1 Mặc định (Base Scope)** | Rút hồi/thu hồi tài liệu có hiệu lực tức thì (commit trạng thái trước khi ack); Fail-closed đối với tài liệu đã thu hồi (SEC 05, KNW 04); Khóa cứng Option O1 trong Base Scope (OPTION_O1_ENABLED = False, DAT 07). | CKPA-59 (PR #28: live re-fetch fail-closed, HTTP 403 O1_OPTION_DISABLED_IN_BASE_SCOPE); CKPA-70 của [P5]. | **ĐẠT (PASS)** |
| **`G1-AC04`** | **Pre-retrieval RBAC 4 Vai trò & 7 Trạng thái Vòng đời** | Thực thi RBAC 4 vai trò (reader, policy_owner, steward, administrator) tại tầng Pre-Retrieval (SEC 01); Quản lý đúng 7 trạng thái KNW 03; 0% rò rỉ link/citation/cache/log khi bị từ chối truy cập. | CKPA-46 (PR #25), CKPA-54 (PR #20), CKPA-70 (g1_rbac_failclosed_audit_CKPA-70.log: 20/20 RBAC PASS, 0% rò rỉ link). | **ĐẠT (PASS)** |
| **`G1-AC05`** | **Governing Date UTC+7 (OPS 03) & Khớp 6 Chiều DAT 04** | Phân giải ngày sự kiện theo múi giờ Việt Nam UTC+7; Ranh giới lịch sử 2026-11-06T09:00:00+07:00; Khớp chính xác 6 chiều ngữ cảnh DAT 04; Tự động chuyển HOLD khi thiếu ngày chi phối. | CKPA-62 (Done), CKPA-63 (PR #23: test_sub14_selection.py 52/52 PASS); Thẩm định chuyên môn CKPA-83 của [P2]. | **ĐẠT (PASS)** |
| **`G1-AC06`** | **Deterministic Field Lookup (DAT 06) & Cơ chế HOLD** | Tra cứu trường trọng yếu định lượng qua Python Decimal thuần (0% số học qua LLM); Tự động kích hoạt HOLD khi thiếu bảng/chú thích (DAT 08) hoặc xung đột nguồn văn bản (DAT 05, OPS 04). | CKPA-63 (PR #23: Decimal thuần, llm_used=False, auto HOLD 4 kịch bản); Biên bản CKPA-83 của [P2]; CKPA-78 của [S3]. | **ĐẠT (PASS)** |
| **`G1-AC07`** | **Bộ 200 Real Tasks, 80 Challenges & Cô lập Môi trường** | Môi trường Test tách Prod (SEC 06); 0% PII thật (SEC 02); Kho ngoài sealed-eval-repo chặn S2/S3; Bộ 200 câu hỏi thực tế (60 Dev / 40 Val / 100 Sealed) + 80 Challenges (40 VN 02); 5 Rep Users độc lập. | CKPA-46, 47, 48, 55, CKPA-66 (200 câu sạch PII đã duyệt); CKPA-79 (P5 kiểm toán ACL kho ngoài); Phân vùng S4. | **ĐẠT (PASS)** |

**KẾT LUẬN ĐỐI SOÁT:** Toàn bộ **7 / 7 tiêu chí Cổng G1 đạt 100% (PASS)**, hệ thống ghi nhận **0 lỗi Critical Control**.

---

# PHẦN 4: ĐỐI SOÁT QUYẾT TOÁN GIỜ CÔNG G1 (W1–W3 = 276H THEO DEL 05 & 10 VAI TRÒ)

Căn cứ quy định tại Mục 10, Mục 11 RFP và hồ sơ định mức DEL 05 đã chuẩn hóa tại `CKPA-80`, Hội đồng đối soát quyết toán giờ công lũy kế Cổng G1 (Tuần 1, Tuần 2, Tuần 3) theo đúng 10 vai trò:

### Bảng Tổng hợp Quyết toán Giờ công G1 Thực tế vs Kế hoạch (DEL 05):

| Mã Role | Họ và tên thành viên | Phía RFP | W1 (Sprint 3) | W2 (Sprint 4) | W3 (Sprint 5) | Tổng KH G1 | Thực tế Hoàn tất | Đạt tỷ lệ (%) | Nhịp bền vững (<= 40h/w) |
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
1. **Khớp 100% định mức:** Tổng thời lượng thực tế quyết toán của Cổng G1 là **276 giờ** (Tuần 1: 100h, Tuần 2: 112h, Tuần 3: 64h), khớp chính xác với ma trận phân bổ công việc `PhanCongCongViec_G1.xlsx` (DEL 05) và Epic `CKPA-44`. Con số nháp ban đầu 372h ghi nhận tại mô tả cũ đã chính thức được bãi bỏ.
2. **Tuân thủ nhịp độ làm việc bền vững (Sustainable Pace):** Toàn bộ 10 thành viên có mức tải tối đa trong tuần không vượt quá **24 giờ/tuần** (thấp hơn nhiều so với ngưỡng trần 40 giờ/tuần theo quy định Scrum/RFP) và không quá 8 giờ/ngày, đảm bảo chất lượng kiểm tra chéo và an toàn bảo mật.

---

# PHẦN 5: SPRINT 5 REVIEW & RETROSPECTIVE LOG (ĐÁNH GIÁ, BÀI HỌC & HÀNH ĐỘNG KHẮC PHỤC)

### 5.1. Sprint 5 Review — Đánh giá Kết quả Đạt được (What Went Well)
1. **Đóng gói kỹ thuật chính xác & bản vá sạch:** Hoàn thành đóng băng tag phát hành `v0.2.0-g1-offline` và thực hiện swarming vá lỗi độc lập gắn tag `v0.2.1-g1-offline` (CKPA-76) với xác nhận retest đạt 100% từ QA Lead `[S4]`.
2. **Quy trình kiểm soát dữ liệu nguồn 2 lớp hiệu quả:** Sự kết hợp độc lập giữa `[P3]` Trần Chí Kha (kiểm tra liên kết vật lý & SHA-256) và `[P2]` Trương Đình Hữu Tài (thẩm định chính sách, ngày hiệu lực & cơ chế HOLD) đã phát hiện và cách ly chuẩn xác 3 ca thiếu bảng biểu `DAT 08`.
3. **Thực thi triệt để nguyên tắc tách vai (Chinese Wall & SoD):** Bảo vệ an toàn kho ngoài `sealed-eval-repo`, QA Lead `[S4]` độc lập tuyệt đối với code của `S2/S3`, 5 Người dùng đại diện thuộc 100% Bên mua ngoài nhóm kỹ sư, và 100% Story/Sub-tasks tuân thủ nguyên tắc `Assignee != Reporter`.
4. **Vệ sinh quản trị và kiểm thử tự động:** Toàn bộ tài liệu được dọn sạch rác citation AI, 100% UTF-8 không lỗi font, CI Guard vận hành ổn định chạy tự động toàn bộ bộ unit tests đạt PASS.

### 5.2. Sprint 5 Retrospective — Các Điểm Cần Tối Ưu (What Could Be Improved)
1. **Tốc độ đồng bộ môi trường Runtime:** Đội kiểm toán bảo mật `[P5]` cần được cấp phát endpoint API thực tế (`CKPA_BASE_URL`) sớm hơn ở các ngày đầu Sprint để giảm tải dồn việc kiểm thử vào cuối kỳ.
2. **Chuẩn bị đào tạo người dùng đại diện:** Cần tăng cường thời lượng hướng dẫn trực tiếp cho 5 Rep Users của `[P4]` trước khi bước vào 20 ngày đo đạc năng suất thực tế (`Observed Effort`) tại G2.

### 5.3. Bảng Hành động Khắc phục & Chuyển giao sang Sprint 6 / Cổng G2 (Action Items)

| Mã Action | Nội dung Hành động Cụ thể | Người chịu trách nhiệm | Hạn hoàn thành | Tiêu chí nghiệm thu |
|---|---|---|---|---|
| **`RETRO-S5-01`** | Bàn giao nguyên trạng cấu hình Base Scope an toàn: Duy trì cờ `OPTION_O1_ENABLED = False`, khóa toàn bộ tính năng thử nghiệm ngoài Base Scope. | `[S2]` Quốc Hưng & `[S5]` Ngọc Duy | Ngày 1 Sprint 6 | File cấu hình `backend/src/config.py` được `[P5]` duyệt PASS |
| **`RETRO-S5-02`** | Thiết lập sớm endpoint Runtime Staging nội bộ để `[P5]` triển khai kiểm thử bảo mật API không phụ thuộc dữ liệu giả lập. | `[S5]` Ngọc Duy & `[P5]` Anh Khoa | Ngày 2 Sprint 6 | URL Staging hoạt động, token RBAC thật, 0% kết nối Internet |
| **`RETRO-S5-03`** | Khởi động Giao thức đo đạc năng suất 20 ngày (`Observed Effort Protocol`) cho 5 Người dùng đại diện để đối trọng với Baseline Effort G0. | `[P4]` Trà My & `[S4]` Quý Hải | Ngày 3 Sprint 6 | 5 bản cam kết tham gia và bảng biểu nhật ký đo giờ thao tác |
| **`RETRO-S5-04`** | Tổ chức thẩm định chuyên môn độc lập của 2 Policy Reviewers (`[P2]` và `[P3]`) trên 180 ca kiểm thử (100 Sealed + 80 Challenges). | `[P2]` Hữu Tài & `[P3]` Chí Kha | Ngày 4 Sprint 6 | Báo cáo chấm điểm độc lập 2 bên, độ lệch điểm <= 5% |

---

# PHẦN 6: KẾ HOẠCH TRIỂN KHAI SPRINT 6 — CỔNG G2 (360H / 3 GIAI ĐOẠN / 30 TASKS)

Căn cứ Kế hoạch triển khai đã đồng bộ từ `PhanCongCongViec_G2_ChuanJira_RFP.xlsx` (DEL 05) tại `CKPA-80`, Hội đồng thống nhất kích hoạt Sprint 6 (Cổng G2 Live Pilot) với tổng dự toán **360 giờ** phân bổ cho 10 vai trò qua 3 giai đoạn:

1. **Giai đoạn 1 (Ngày 1–2 Sprint 6 — Build Workspace, Lifecycle, Ops & Legal Prep — 144h):**
   - **WP 04 Answer Package & Guardrails (`[S3]` Yến Nhi, 40h):** Hoàn thiện Answer Package chuẩn 100–250 từ, các trường cấu trúc cứng ANS 03-04; bộ quy tắc Local Referral và 9 kịch bản Annex B (KNW 05); chống Prompt Injection & khóa Streaming ANS 08.
   - **WP 04 Lifecycle & Feedback (`[S2]` Quốc Hưng, 38h):** Vòng đời 7 trạng thái và hiệu lực lịch KNW 03; ngăn chặn Stale Answer khi thu hồi (KNW 04); phân loại phản hồi và trích xuất ứng viên tri thức (KNW 06-07).
   - **Vận hành & Dự phòng (`[S5]` Ngọc Duy, 24h):** Xóa cache vật lý tự động <= 5 phút và cơ chế Fail-Closed (OPS 05); quy trình Emergency Disable và tìm kiếm dự phòng Mục 9.
   - **Pháp lý, Bảo mật & Đóng gói (`[P5]` Anh Khoa 24h, `[P2]/[P3]/[P4]` mỗi vai 10h, `[S1]` 12h):** Lập luận rủi ro AI Annex F; quy trình báo cáo sự cố trong 4h và Change Control (SEC 03-08); diễn tập thu hồi và đào tạo 5 Rep Users; đóng gói Working Core DEL 02.

2. **Giai đoạn 2 (Ngày 3–4 Sprint 6 — Kiểm định Độc lập 180 Ca & Đào tạo — 142h):**
   - **Kiểm định Hiệu năng & QA Độc lập (`[S5]` 12h, `[S4]` Quý Hải 40h):** Benchmark 5 người dùng đồng thời, thời gian phản hồi p95 <= 25s trên 100 truy vấn (OPS 02); kiểm thử 80 Challenges và kịch bản thu hồi giữa chừng; chấm điểm tập 100 câu Sealed (Applicability/Recall); lập Báo cáo Điểm số Độc lập DEL 03.
   - **Thẩm định Độc lập phía Bên Mua (`[P2]` 26h, `[P3]` 26h, `[P4]` 24h, `[P5]` 10h):** Two Policy Reviewers chấm độc lập điều khoản, ngoại lệ, ngày chi phối và phạm vi; đánh giá tính hữu ích và mức độ chỉnh sửa nhỏ >= 80%; xác nhận 0 lỗi tiết lộ thông tin trái phép trên 180 ca.
   - **Đệ trình Hồ sơ G2 (`[S1]` 14h):** Tổng hợp Hồ sơ Điểm số Độc lập và Căn cứ Pháp lý G2 (T26).

3. **Giai đoạn 3 (Ngày 5 Sprint 6 — Hội đồng Nghiệm thu G2 & Kích hoạt Pilot G3 — 74h):**
   - **Báo cáo Quyết toán (`[S1]` 10h):** Lập báo cáo giờ công Tuần 4 và lịch trình chi tiết 20 ngày làm việc quan sát thực tế G3.
   - **Hội đồng Thẩm định & Nghiệm thu G2 (`[P1]` Mỹ Vân 30h):** Chủ trì Hội đồng đánh giá 8 tiêu chí Cổng G2 và 4 Critical Gates đạt 0 lỗi; ký lệnh kích hoạt 20 ngày sử dụng có giám sát; ký Biên bản Nghiệm thu Cổng G2 và phê duyệt giải ngân Mốc 3 (25%).

---

# PHẦN 7: NGHỊ QUYẾT HỘI ĐỒNG, CẤP PHÉP MỞ CỔNG G2 VÀ LỆNH GIẢI NGÂN MỐC 2 (25%)

Căn cứ kết quả đối soát toàn diện đạt 7/7 tiêu chí Cổng G1, 0 lỗi Critical Control và sự nhất trí 100% của 10 vai trò tham dự, Chủ tịch Hội đồng **`[P1]` Vắn Mỹ Vân** chính thức quyết nghị:

### 7.1. Phê duyệt Nghiệm thu Chính thức Cổng Gate G1 (Sign-off Gate G1)
- Nghiệm thu toàn diện Giai đoạn Thử nghiệm Nội bộ Ngoại tuyến có Kiểm soát (Controlled Offline Pilot & Benchmarks).
- Công nhận các kết quả bàn giao: Bộ Corpus 3 họ chuẩn hóa, Pipeline RAG offline đạt chuẩn, bộ 200 Tasks & 80 Challenges niêm phong độc lập, Hồ sơ Bằng chứng DEL 03 Part 1 và Báo cáo quyết toán 276 giờ công.
- Chính thức đóng User Story cha **`CKPA-81`** và Sub-task **`CKPA-84`** ở trạng thái **`Done`** trên hệ thống Jira.

### 7.2. Quyết định Cấp phép Chuyển tiếp Giai đoạn Mở Cổng Gate G2 (Proceed to G2)
- Cấp phép cho phép dự án chuyển tiếp sang Giai đoạn Thử nghiệm Nội bộ Giới hạn (Sprint 6 — Gate G2 Live Pilot) theo đúng kế hoạch triển khai.
- **Ràng buộc kiểm soát bắt buộc trong Sprint 6:**
  1. Duy trì nghiêm ngặt phạm vi Base Scope thuần túy: Khóa cứng `OPTION_O1_ENABLED = False`, không nạp dữ liệu CRM sống khi chưa có phê duyệt riêng từ Legal Owner.
  2. Môi trường Staging phải được Security Owner `[P5]` kiểm tra bảo mật các cổng mạng và cơ chế fail-closed trước khi cho phép 5 Rep Users thao tác.
  3. Giao `[P4]` Ngô Thị Trà My điều phối 5 Rep Users thực hiện đúng Giao thức đo 20 ngày năng suất làm cơ sở nghiệm thu G3.

### 7.3. Lệnh Giải ngân Thanh toán Mốc 2 (25% Giá trị Hợp đồng Base Scope)
- Căn cứ Điều 12 Hợp đồng Dịch vụ Phần mềm số 01/2026/HDDV-CKPA:
  1. **Tên mốc thanh toán:** Mốc 2 — Nghiệm thu Cổng Gate G1 (Milestone 2: Controlled Offline Sign-off).
  2. **Tỷ lệ giải ngân:** **25% (Hai mươi lăm phần trăm)** Tổng giá trị Hợp đồng Base Scope.
  3. **Công thức xác định giá trị thanh toán thực tế:**
     `Giá trị giải ngân Mốc 2 = 25% * Tổng giá trị Hợp đồng Base Scope (đã bao gồm thuế VAT)`
  4. **Căn cứ thanh toán:** Giá trị bằng tiền được tính chính xác dựa trên Bảng giá Thương mại DEL 05 chính thức đã được thống nhất tại task `CKPA-39`.
  5. **Thời hạn và thủ tục:** Ban Tài chính - Kế toán Công ty Cổ phần Thiết bị Công nghiệp Song Nhật thực hiện giải ngân chuyển khoản trong thời hạn 10 (mười) ngày làm việc kể từ ngày nhận đủ Biên bản Nghiệm thu này kèm Hóa đơn Giá trị gia tăng (VAT) hợp lệ do Bên Cung cấp phát hành.

---

# PHẦN 8: BẢNG KÝ DUYỆT CHÍNH THỨC CỦA 10 THÀNH VIÊN HỘI ĐỒNG DỰ ÁN

Các thành viên Hội đồng đại diện cho 10 vai trò RFP đã đọc kỹ, thống nhất toàn bộ nội dung và cùng ký tên xác nhận:

| Vai trò chuẩn RFP | Họ và tên thành viên | Chức vụ / Đơn vị đại diện | Trách nhiệm xác nhận | Chữ ký xác nhận |
|---|---|---|---|:---:|
| **`[P1]` Purchaser Sponsor / PO** | **Vắn Mỹ Vân** | Chủ đầu tư — Song Nhật | Chủ tịch Hội đồng — Phê duyệt Cổng G1, Mở G2 & Ký Lệnh Giải ngân 25% | *(Đã ký duyệt chính thức)* |
| **`[P2]` Policy Owners** | **Trương Đình Hữu Tài** | Trưởng nhóm Quản trị Chính sách | Xác nhận Tiêu chuẩn Chính sách, Ngày hiệu lực UTC+7 & Cơ chế HOLD | *(Đã ký duyệt chuyên môn)* |
| **`[P3]` Knowledge & Data Steward** | **Trần Chí Kha** | Quản trị Dữ liệu & Nguồn Tri thức | Xác nhận Toàn vẹn 100% source_uri, SHA-256 & Cân bằng DAT 08 | *(Đã ký duyệt dữ liệu)* |
| **`[P4]` Staff Users Representative** | **Ngô Thị Trà My** | Đại diện Người dùng Nghiệp vụ | Xác nhận Nghiệp vụ 200 Real Tasks & Kế hoạch Đo 20 ngày Effort | *(Đã ký duyệt nghiệp vụ)* |
| **`[P5]` Privacy & Security Owners** | **Nguyễn Anh Khoa** | Quản trị An toàn Thông tin | Xác nhận 0% PII, Phân quyền RBAC 4 vai trò & Niêm phong kho Sealed | *(Đã ký duyệt an ninh)* |
| **`[S1]` Named Lead / Scrum Master** | **Hoàng Tiến** | Đại diện Quản lý Nhà cung cấp | Bàn giao DEL 03 Part 1, Quyết toán 276h & Kế hoạch Sprint 6 | *(Đã ký xác nhận bàn giao)* |
| **`[S2]` Integration Engineer** | **Trần Quốc Hưng** | Kỹ sư Tích hợp Hệ thống | Xác nhận Bản vá Swarming v0.2.1-g1-offline & 2 CSV Validators | *(Đã ký xác nhận kỹ thuật)* |
| **`[S3]` Retrieval & App Engineer** | **Phạm Lương Yến Nhi** | Kỹ sư Truy xuất & Ứng dụng | Xác nhận Logic Lookup Decimal thuần, 0% LLM số học & Khóa O1 | *(Đã ký xác nhận kỹ thuật)* |
| **`[S4]` Quality Lead (Independent QA)** | **Phạm Quý Hải** | Trưởng nhóm Kiểm định Độc lập | Xác nhận Kiểm tra Độc lập 7/7 Tiêu chí G1-AC01..07 đạt 0 lỗi | *(Đã ký kiểm định độc lập)* |
| **`[S5]` Operations Specialist** | **Nguyễn Ngọc Duy** | Chuyên viên Vận hành Hạ tầng | Xác nhận Đóng băng Tag v0.2.0/v0.2.1 & Môi trường Offline khép kín | *(Đã ký xác nhận vận hành)* |

---
*Biên bản này được lập thành 04 (bốn) bản gốc bằng tiếng Việt có giá trị pháp lý như nhau. Bên Mua lưu giữ 02 bản, Bên Cung cấp lưu giữ 02 bản để làm căn cứ giải ngân Mốc 2 và triển khai Sprint 6 (Cổng G2 Live Pilot).*
