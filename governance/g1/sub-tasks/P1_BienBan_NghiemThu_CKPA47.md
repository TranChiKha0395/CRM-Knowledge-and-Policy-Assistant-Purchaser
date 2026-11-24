# SONGNHAT CRM KNOWLEDGE & POLICY ASSISTANT (CKPA) — GATE G1
## BIÊN BẢN THẨM ĐỊNH VÀ NGHIỆM THU NHIỆM VỤ CKPA-47
**Tiêu đề:** Kiểm toán Dữ liệu Test 0% PII Trái phép & Ranh giới Allowlist O1  
**Mã nhiệm vụ (Jira):** `CKPA-47` (Parent: `CKPA-45` [G1][SEC06] Thiết lập Môi trường Test & Kho Sealed)  
**Mã gốc (Excel G1):** `CRM-G1-SUB02` | **Mã Tiêu chí Cổng G1:** `G1-AC07`  
**GitHub Branch:** `sec/CRM-G1-SUB02-audit-test-data-no-pii`  
**Căn cứ truy vết RFP:** SEC 02, SEC 06, DAT 07, Mục 9 (G1), Annex C  
**Người thực hiện (Assignee):** `[P5] Nguyễn Anh Khoa (Privacy and Security Owner)`  
**Người nghiệm thu (Reporter / PO):** `[P1] Mỹ Vân (Purchaser Sponsor)`  
**Các bên phối hợp (RACI):** `[S5] Ngọc Duy (DevOps/Sec), [P3] Trần Chí Kha (Data Steward)`  
**Ngày nghiệm thu:** 20/11/2026 (Múi giờ Việt Nam: Asia/Ho_Chi_Minh, UTC+7)

---

### 1. ĐỐI CHIẾU TIÊU CHÍ CHẤP NHẬN BDD (ACCEPTANCE CRITERIA)

| Thành phần BDD | Nội dung đặc tả | Kết quả thẩm định của P1 | Trạng thái |
|---|---|---|:---:|
| **Given** | Hạ tầng Test SUB01 (CKPA-46) tách Prod & tập dữ liệu mẫu/test. | Đã xác nhận hạ tầng DB/Redis Test độc lập, không dùng chung secrets. | **ĐẠT** |
| **When** | P5 thực hiện quét PII bằng Regex + audit script và đối chiếu Base vs O1. | Đã chạy script `security/scripts/g1_security_audit_runner.py`, quét toàn diện mọi tập dữ liệu. | **ĐẠT** |
| **Then** | 0% PII khách hàng thật trái phép; O1 allowlist tuân thủ SEC 02/DAT 07. | 0 SĐT, 0 Email, 0 CCCD; giữ nguyên Base Scope (2 CSV), không bật O1. | **ĐẠT** |

---

### 2. CHI TIẾT KẾT QUẢ KIỂM TOÁN CÁC TẬP DỮ LIỆU G1 (SEC 02 / SEC 06)

| Tập dữ liệu kiểm toán | Quy mô | Loại dữ liệu & Nguồn gốc | Kết quả quét PII (Regex + Audit) | Đánh giá của P1 |
|---|:---:|---|---|:---:|
| `passages_template.csv` & Corpus G1 | <= 300 đoạn | Văn bản chính sách nội bộ SongNhat đã chuẩn hóa | 0 SĐT, 0 Email cá nhân, 0 CCCD/MST KH thật | **PASS (0% PII)** |
| `critical_fields_template.csv` | <= 50 dòng | Tham số ngưỡng chiết khấu, SLA, thẩm quyền duyệt | Chỉ chứa giá trị định lượng & vai trò tổ chức | **PASS (0% PII)** |
| Tập công khai 60 Dev Tasks | 60 tác vụ | Dữ liệu giả lập B2B (Synthetic data) đã làm sạch | 0% thông tin định danh khách hàng thật | **PASS (0% PII)** |
| Tập 40 Validation & 80 Challenges (VN 02) | 120 tác vụ | Dữ liệu kiểm thử biên tổng hợp & mẫu câu hỏi sạch | 0% hồ sơ khách hàng thật; đạt chuẩn SEC 02 | **PASS (0% PII)** |
| Tập 100 Sealed Acceptance (Kho cách ly) | 100 tác vụ | Dữ liệu nghiệm thu ẩn danh được phê duyệt | Lưu riêng tại kho sealed-eval-repo; 0% PII | **PASS (0% PII)** |

---

### 3. ĐỐI CHIẾU RANH GIỚI TÙY CHỌN O1 (DAT 07) & AN TOÀN HẠ TẦNG (SEC 06)

1. **Xác nhận trạng thái Tùy chọn O1 (Selected CRM Context — DAT 07):**
   - Đối chiếu Biên bản chốt phạm vi Gate G0: Dự án triển khai thuần túy trong **Phạm vi Cơ sở (Base Scope — 2 tệp CSV passages và critical_fields)**.
   - **Không kích hoạt Tùy chọn O1**, không tồn tại endpoint/bảng nhập hồ sơ khách hàng CRM trong mã nguồn hoặc hạ tầng Test.
2. **Kiểm soát PII Input Guard (shared/pii_guard.py — SEC 02):**
   - Xác nhận bộ lọc đầu vào tự động phát hiện và che mờ SĐT, Email cá nhân, CCCD nếu người dùng vô tình nhập vào khung câu hỏi; không ghi PII vào audit log hay gửi LLM.
3. **Tách biệt môi trường Test & Production (SEC 06):**
   - Xác nhận môi trường Test (SUB01 / CKPA-46) sử dụng CSDL, khóa bí mật và biến môi trường độc lập hoàn toàn với Prod.

---

### 4. KẾT LUẬN & QUYẾT ĐỊNH CỦA PURCHASER SPONSOR (P1)

* **Kết quả thẩm định:** **ĐẠT CHUẨN 100% (PASSED)**.
* **Quyết định:**
  1. Chứng nhận toàn bộ dữ liệu kiểm thử Gate G1 hợp pháp, chứa đúng 0% PII khách hàng thật trái phép.
  2. Phê duyệt hoàn thành Sub-task `CRM-G1-SUB02` và **ĐÓNG TICKET CKPA-47 TRÊN JIRA**.
  3. **MỞ KHÓA ĐIỀU KIỆN THỰC THI CHO THẺ PHỤ THUỘC `CKPA-48`** (Lập kho sealed-eval-repo chặn Read S2/S3).

*(Ký duyệt ngày 20/11/2026 — Người mua / Purchaser Sponsor: Mỹ Vân)*
