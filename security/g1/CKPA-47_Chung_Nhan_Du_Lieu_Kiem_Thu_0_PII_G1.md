# CHỨNG NHẬN DỮ LIỆU KIỂM THỬ HỢP PHÁP GATE G1 (`0% PII` & RANH GIỚI `O1 = OFF`) — `CKPA-47`

- **Dự án:** SongNhat CRM Knowledge and Policy Assistant (`SCRM` / `CKPA`)
- **Mã công việc & Truy vết RFP:** `CKPA-47` (`CRM-G1-SUB02`) | Tiêu chí Cổng: `G1-AC07` | `SEC 02`, `SEC 06`, `DAT 07`, `Mục 9 (G1)`, `Annex C`
- **Người lập & Kiểm toán (`Assignee`):** `[P5]` Nguyễn Anh Khoa — Privacy and Security Owner (Phía Purchaser)
- **Phối hợp & Nghiệm thu (`RACI`):** Nghiệm thu: `[P1]` Vắn Mỹ Vân | Phối hợp: `[S5]` Nguyễn Ngọc Duy, `[P3]` Trần Chí Kha
- **Phiên bản hồ sơ:** `v2.2` (Đồng bộ quét toàn bộ kho `CRM-Knowledge-and-Policy-Assistant-Purchaser` ngày `2026-11-24`, bổ sung đầy đủ gói `CKPA-58` & `CKPA-66`)
- **Công cụ & Bằng chứng đính kèm:** `security/scripts/g1_security_audit_runner.py` & `security/g1/g1_pii_audit_CKPA-47.log`

---

## I. PHÂN TÁCH PHẠM VI KIỂM TOÁN DỮ LIỆU & HẠ TẦNG GATE G1 (`PASS` VS. `EXTERNAL ISOLATED`)

Tuân thủ nguyên tắc trung thực tuyệt đối (`No-Mock`), Chủ sở hữu Quyền riêng tư & Bảo mật (`[P5]`) tách bạch rõ các tập dữ liệu trên kho chung Purchaser đã được quét trực tiếp (`PASS`) với kho niêm phong bên ngoài (`sealed-eval-repo`):

| STT | Hạng mục dữ liệu / Hạ tầng | Nguồn / Jira | Trạng thái | Chi tiết kiểm toán & Bằng chứng đối chiếu |
| :---: | :--- | :--- | :---: | :--- |
| **1** | Toàn bộ kho dữ liệu, biên bản & tài liệu hiện hữu trên `CRM-Knowledge-and-Policy-Assistant-Purchaser` | Nhánh tích hợp `develop` | **PASS (`0% PII`)** | Đã quét trực tiếp toàn bộ tệp `.csv`, `.json`, `.md`, `.log`, `.txt`, `.yml` bằng `security/scripts/g1_security_audit_runner.py` & `scripts/ci_purchaser_guard.py`. Kết quả: **`0` PII hits**; 100% dữ liệu giả lập (synthetic) đạt chuẩn `SEC 02`. |
| **2** | Hạ tầng Test tách Prod & Phân quyền IAM 4 vai trò cốt lõi | `CKPA-46` — `[S5]` Nguyễn Ngọc Duy | **PASS (`SEC 06`)** | Xác nhận tách biệt biến môi trường/CSDL Test khỏi Prod và cấu hình đủ 4 vai trò cốt lõi (`reader`, `steward`, `policy_owner`, `administrator`). |
| **3** | Gói dữ liệu chính sách Họ 1 (`Family 1` Corpus, Critical Fields & Fixtures) | `CKPA-50` (`Done`) — `[P3]` Trần Chí Kha | **PASS (`0% PII`)** | Đã quét trực tiếp `data/g1/family1/`, `data/g1/fixtures/`, `data/g1/sources/`: 40 passages + 16 critical fields chỉ chứa quy định nội bộ SongNhat, `0%` PII khách hàng thật. |
| **4** | Gói dữ liệu Full Corpus 3 Họ (`POL-001..003`, 11 tài liệu `DOC-001..011`) | `CKPA-58` (`Done`) — `[P3]` Trần Chí Kha | **PASS (`0% PII`)** | Đã quét trực tiếp `data/g1/full/` (96 passages, 40 critical fields, 136 SHA-256 manifest) và 11/11 tệp nguồn `data/g1/sources/`: **`0` PII hits**. |
| **5** | Bộ 100 câu hỏi mở (`60 DEV + 40 VAL`), Từ điển `VN 01` & Bản che hash 200 Real Tasks | `CKPA-55`, `CKPA-66` (`Done`) — `[P4]` Ngô Thị Trà My | **PASS (`0% PII`)** | Đã quét trực tiếp `uat/g1/ckpa-55/` và `uat/g1/ckpa-66/`: 100 câu mở hoàn toàn ẩn danh, 100 dòng `SEALED` đã khóa bằng mã băm `[SEALED_TASK_HIDDEN_PER_GUARDRAIL_1]`, **`0` SĐT / Email cá nhân / CCCD / MST thật**. |
| **6** | Kho cách ly `sealed-eval-repo` (`100 Sealed` plaintext & `80 Constructed Challenges`) | `CKPA-48` / `CKPA-67` / `CKPA-79` — `[S4]` Phạm Quý Hải | **ISOLATED (`CKPA-79`)** | Tuyệt đối không lưu plaintext trên kho chung Purchaser (được chặn cứng bởi CI Guard). Kiểm toán ACL & Audit Log kho ngoài thực hiện theo quy trình No-Mock tại `security/g1/CKPA-79_Bien_Ban_Kiem_Toan_ACL_Sealed_Va_Chot_Bao_Mat_G1.md`. |

---

## II. ĐỐI CHIẾU QUYẾT ĐỊNH PHẠM VI GATE G0 & RANH GIỚI TÙY CHỌN `O1` (`DAT 07`)

| Hạng mục kiểm soát | Kết quả đối chiếu thực tế |
| :--- | :--- |
| **Quyết định kiến trúc từ Gate G0 (`CKPA-40`/`42`)** | Triển khai 100% trong **Phạm vi Cơ sở (`Base Scope`)** với 02 tệp CSV chuẩn (`passages` 21 cột và `critical_fields` 23 cột). **Tắt hoàn toàn Tùy chọn `O1` (`Selected CRM Context = OFF`)**. |
| **Kiểm tra trường dữ liệu `O1` (`DAT 07`)** | Không tồn tại kết nối API đọc hồ sơ khách hàng trực tiếp từ CRM sản xuất; không phát sinh trường định danh khách hàng ngoài danh mục tối thiểu. |
| **Kết luận tuân thủ `SEC 02` & `DAT 07`** | **ĐẠT CHUẨN** — Ranh giới dữ liệu kiểm thử Gate G1 hoàn toàn cô lập khỏi dữ liệu khách hàng thật của SongNhat. |

---

## III. KẾT QUẢ THỰC THI CÔNG CỤ KIỂM TOÁN TỰ ĐỘNG & LOG ĐÍNH KÈM

Công cụ `security/scripts/g1_security_audit_runner.py` quét tự động SĐT Việt Nam (kể cả phân tách bằng dấu chấm/gạch ngang/khoảng trắng), email ngoài tên miền `@songnhat.vn` / `@example.com`, số CCCD 12 chữ số và MST 10 chữ số trên toàn bộ kho `CRM-Knowledge-and-Policy-Assistant-Purchaser`. Nhật ký chi tiết được xuất tự động tại `security/g1/g1_pii_audit_CKPA-47.log` với kết quả **`0` PII hits**.

---

## IV. XÁC NHẬN & PHÊ DUYỆT KIỂM TOÁN (`GATE G1 — G1-AC07`)

| ĐẠI DIỆN KIỂM TOÁN BẢO MẬT (`[P5]`) | PHÊ DUYỆT NGHIỆM THU CỔNG G1 (`[P1]`) |
| :---: | :---: |
| **Nguyễn Anh Khoa**<br>`[P5]` Privacy and Security Owner<br>Đã kiểm toán & xác nhận `0% PII` trên kho Purchaser (cập nhật đồng bộ `CKPA-58` & `CKPA-66` ngày `24/11/2026`) | **Vắn Mỹ Vân**<br>`[P1]` Purchaser Sponsor / Product Owner<br>Đã phê duyệt nghiệm thu (`governance/g1/sub-tasks/P1_BienBan_NghiemThu_CKPA47.md`, ký lần đầu `20/11/2026`) |
