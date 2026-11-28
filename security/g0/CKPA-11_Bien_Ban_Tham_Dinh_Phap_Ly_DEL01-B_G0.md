# BIÊN BẢN THẨM ĐỊNH PHÁP LÝ MA TRẬN THẨM QUYỀN 5 LỚP (DEL01-B — GATE G0)

- **Mã công việc Jira:** CKPA-11 (Epic: CKPA-3 | Mở khóa: CKPA-24, CKPA-28 | Liên quan: CKPA-8)
- **Tiêu đề hạng mục:** `[G0][DEL01-B] Thẩm định Pháp lý Ma trận Thẩm quyền`
- **Mã truy vết RFP & Cổng G0:** Mục 9 (G0), SEC 01, SEC 02, Annex F | Tiêu chí: `G0-AC02`
- **Chủ trì thẩm định (Lead):** `[P5]` Anh Khoa (Privacy & Security Owner — Purchaser Team)
- **Phối hợp soạn thảo (RACI):** `[P2]` Hữu Tài, `[P3]` Chí Kha
- **Người nghiệm thu (PO/SM):** `[P1]` Mỹ Vân (Purchaser Sponsor) | **Reporter:** `[S1]` Tiến Hoàng
- **Ngày hoàn tất thẩm định:** 2026-11-13 (Cập nhật đồng bộ hồ sơ Gate G0: 2026-11-22)

---

## 1. Mục tiêu & Cơ sở đối soát
Thực hiện thẩm định tính tuân thủ pháp lý, quyền riêng tư và phân tách dữ liệu cho tài liệu **Ma trận thẩm quyền 5 lớp (`DAT 03`)** và **Đặc tả phân quyền (`DAT 04`)** trước khi ban hành chính thức `DEL01-B` tại cổng Gate G0:
- Đối chiếu với Ma trận phạm vi cơ sở (`policy/g0/CKPA-9_02_Base_Scope_O1_And_Out_Of_Scope_Matrix.csv`) về ranh giới giữa hợp đồng thương mại khách hàng và chính sách vận hành nội bộ.
- Đối chiếu với các yêu cầu bảo mật cốt lõi: **SEC 01** (Kiểm soát truy cập theo vai trò RBAC), **SEC 02** (Bảo vệ dữ liệu cá nhân & 0% PII), và **Annex F** (Phụ lục tuân thủ pháp lý & quyền riêng tư).

---

## 2. Kết quả thẩm định 3 trụ cột tuân thủ (BDD Acceptance Criteria)

| STT | Hạng mục thẩm định | Tiêu chí đối soát | Kết quả thẩm định chi tiết | Đánh giá |
| :---: | :--- | :---: | :--- | :---: |
| **1** | **Tính hợp lệ của Ma trận thẩm quyền 5 lớp (`DAT 03`, `DAT 04`)** | Mục 9 (G0) | Xác nhận phân cấp thẩm quyền rõ ràng từ Nhân viên CS tuyến đầu (`Tier-1`) đến Giám đốc CRM / Policy Owner (`Tier-5`); không phát sinh chồng chéo quyền phê duyệt hoặc miễn trừ ngoại lệ trái quy định (*No Inferred Approval*). | **ĐẠT (PASS)** |
| **2** | **Ranh giới Hợp đồng khách hàng & Chính sách nội bộ** | `CKPA-9` Base Scope | Tách biệt rạch ròi điều khoản bảo mật thương mại riêng biệt của từng hợp đồng khách hàng với quy định vận hành nội bộ của Công ty Cổ phần Thiết bị Công nghiệp Song Nhật; chặn truy xuất chéo ngoài phạm vi được cấp phép. | **ĐẠT (PASS)** |
| **3** | **Điều kiện bảo mật & Tách biệt dữ liệu khách hàng** | `SEC 01`, `SEC 02`, `Annex F` | Áp dụng nguyên tắc tối thiểu hóa dữ liệu (*Data Minimization*) và cô lập dữ liệu định danh khách hàng (0% PII rò rỉ giữa các phân vùng). Xác nhận **không tồn tại xung đột pháp lý hoặc vi phạm quyền riêng tư** trên `DEL01-B`. | **ĐẠT (PASS)** |

---

## 3. Điều kiện áp dụng & Lưu ý vận hành sau thẩm định
1. **Bảo lưu nguyên tắc cô lập dữ liệu:** Mọi thay đổi về phân cấp thẩm quyền hoặc phạm vi hợp đồng khách hàng trong các giai đoạn sau (Gate G1/G2) phải được cập nhật đồng bộ vào `DEL01-B` và thông qua rà soát lại của `[P5]` Privacy & Security Owner.
2. **Tuân thủ Guardrail #1:** Không đính kèm nội dung nguyên văn hợp đồng nhạy cảm hoặc dữ liệu định danh khách hàng (PII) lên các thẻ Jira công khai có sự tham gia của nhóm Supplier (`S1–S5`).

---

## 4. Ký xác nhận ban hành (Sign-off)
- **Kết luận của `[P5]` Privacy & Security Owner:** Tài liệu `DEL01-B` đáp ứng đầy đủ tiêu chí **`G0-AC02`**, không phát sinh xung đột pháp lý hay rủi ro quyền riêng tư, đủ điều kiện ban hành chính thức và mở khóa (`unblock`) cho hạng mục kế tiếp **`CKPA-28`**.
- **Người thẩm định ký xác nhận:** `[P5] Nguyễn Anh Khoa` — Privacy & Security Owner.
- **Kính chuyển nghiệm thu:** `[P1] Mỹ Vân` — Purchaser Sponsor.