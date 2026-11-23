# SONGNHAT CRM KNOWLEDGE & POLICY ASSISTANT (CKPA) — GATE G1
## BIÊN BẢN THẨM ĐỊNH VÀ NGHIỆM THU NHIỆM VỤ CKPA-51
**Tiêu đề:** Ký duyệt Thẩm định Corpus & Critical Fields Họ 1  
**Mã nhiệm vụ (Jira):** `CKPA-51` (Parent: `CKPA-49` [G1][WP02] Biên tập Họ 1 & 2 Bộ Validator CSV)  
**Mã gốc (Excel G1):** `CRM-G1-SUB05` | **Mã Tiêu chí Cổng G1:** `G1-AC01`  
**GitHub Branch:** `policy/CRM-G1-SUB05-approve-family1-corpus`  
**Căn cứ truy vết RFP:** DAT 03 (Authority Matrix), DAT 06 (Critical Fields), KNW 03, Mục 9 (G1), WP 02  
**Người thực hiện (Assignee):** `[P2] Hữu Tài (Policy Owner — Họ 1 Báo giá và Phê duyệt Thương mại)`  
**Người nghiệm thu (Reporter / PO):** `[P1] Mỹ Vân (Purchaser Sponsor)`  
**Các bên phối hợp (RACI):** `[P3] Trần Chí Kha (Data Steward), [S2] Quốc Hưng (Integration Engineer)`  
**Ngày nghiệm thu:** 20/11/2026 (Múi giờ Việt Nam: Asia/Ho_Chi_Minh, UTC+7)

---

### 1. ĐỐI CHIẾU TIÊU CHÍ CHẤP NHẬN BDD (ACCEPTANCE CRITERIA)

| Thành phần BDD | Nội dung đặc tả | Kết quả thẩm định của P1 | Trạng thái |
|---|---|---|:---:|
| **Given** | Dữ liệu Họ 1 thô từ CRM-G1-SUB04 (P3 Chí Kha chuẩn bị). | 2 tệp CSV khớp 100% cấu trúc template G0, không lỗi cú pháp. | **ĐẠT** |
| **When** | Policy Owner P2 rà soát, đối chiếu quy định gốc và ký duyệt nội dung + 7 trạng thái. | Đã có chữ ký APPROVED chính thức của Policy Owner [P2] Hữu Tài. | **ĐẠT** |
| **Then** | 100% bản ghi Họ 1 có chữ ký duyệt của Policy Owner; đủ 7 trạng thái KNW 03. | 40 passages & 16 critical fields khớp 100% thẩm quyền & quy tắc. | **ĐẠT** |

---

### 2. KẾT QUẢ RÀ SOÁT CHI TIẾT CORPUS & BẢNG CRITICAL FIELDS HỌ 1

#### 2.1 Kiểm tra Schema & Toàn vẹn Dữ liệu (DAT 01, DAT 02, DAT 08)
- **`Policy_Corpus_Family1.csv` (40 bản ghi — 21 cột UTF-8):** Khớp 100% cấu trúc `passages_template.csv`. Độ dài lớn nhất 591 ký tự (đạt chuẩn <= 6.000 ký tự Unicode, không cắt âm thầm). 100% trường thời gian chuẩn ISO 8601 múi giờ `+07:00`.
- **Chủ đích kiểm thử DAT 08:** Bản ghi `PAS-040` (Phụ lục B1) được gắn `has_essential_attachments = False` để phục vụ kịch bản kiểm thử kích hoạt `HOLD_DAT08` tại Gate G1.
- **`Critical_Fields_Family1.csv` (16 bản ghi — 23 cột UTF-8):** Toàn bộ 16/16 trường liên kết khóa ngoại chính xác tới `passage_id` và khớp `document_version_id`.

#### 2.2 Thẩm định Phân bổ Nguồn theo Ma trận Thẩm quyền 5 Lớp (DAT 03 / CKPA-4)
- **`DOC-001` (policy — Chính sách công ty):** 29 đoạn (`PAS-001..010, 031..049`) — Quy định gốc v1.0, lịch sử v0.9, bản tương lai v2.0, nháp & thu hồi.
- **`DOC-004` (SOP — Quy trình thao tác chuẩn):** 05 đoạn (`PAS-050..054`) — 5 bước lập đề xuất chiết khấu trên CRM, tuân thủ Substitute Owner (VN 04).
- **`DOC-006` (customer_contract — Hợp đồng khung):** 03 đoạn (`PAS-055..057`) — Mâu thuẫn điều khoản chiết khấu/tạm ứng để kiểm thử Conflict HOLD (DAT 05).
- **`DOC-007` (staff_note — Ghi chú CRM cũ):** 03 đoạn (`PAS-058..060`) — Tiền lệ ngoại lệ cũ để kiểm thử quy tắc cấm suy luận (ANS 05).

#### 2.3 Thẩm định 7 Trạng thái Vòng đời Xuất bản (KNW 03)
- `effective`: 31 đoạn, 10 critical fields (Đủ approver, published_at, effective_from=2026-11-06T09:00:00+07:00).
- `superseded`: 03 đoạn, 03 critical fields (effective_to=2026-11-06T08:59:59+07:00, thay thế bởi v1.0).
- `scheduled`: 02 đoạn, 02 critical fields (effective_from=2027-01-01T00:00:00+07:00 tương lai, chặn trả lời năm 2026).
- `draft` / `owner_reviewed` / `approved`: 03 đoạn (approver/published_at để trống, bị chặn bởi Pre-retrieval).
- `withdrawn`: 01 đoạn, 01 critical field (Thu hồi khẩn từ 2026-10-15T14:00:00+07:00, cấm phục vụ & xóa cache <=5 phút theo SEC 05).

#### 2.4 Thẩm định Bảng Trường Trọng Yếu Số học & Tiền tệ (DAT 06)
- 16/16 dòng trường trọng yếu (`CF-001..CF-022`) khớp 100% ngưỡng chiết khấu (5%, 5-15%), đơn vị tiền tệ (1.000.000.000 VND), thời hạn (15 ngày) và vai trò phê duyệt (Sales Staff, Sales Manager, Sales Director).
- Bản ghi `PAS-039 / CF-015` quy định sàn Gross Margin (18%) được bảo vệ phân quyền `audience` loại trừ reader theo SEC 01.

---

### 3. KẾT LUẬN & QUYẾT ĐỊNH CỦA PURCHASER SPONSOR (P1)

* **Kết quả thẩm định:** **ĐẠT CHUẨN 100% (PASSED)**.
* **Quyết định:**
  1. Tiếp nhận và phê duyệt toàn bộ Corpus Họ 1 và Bảng Critical Fields đã có chữ ký của Policy Owner [P2] Hữu Tài.
  2. Xác nhận đạt Tiêu chí Cổng `G1-AC01`, đủ điều kiện bàn giao cho [P3] Chí Kha và [S2] Quốc Hưng nạp vào hệ thống qua Bộ Validator CSV (CKPA-52).
  3. **PHÊ DUYỆT ĐÓNG TICKET CKPA-51 TRÊN JIRA**.

*(Ký duyệt ngày 20/11/2026 — Người mua / Purchaser Sponsor: Mỹ Vân)*
