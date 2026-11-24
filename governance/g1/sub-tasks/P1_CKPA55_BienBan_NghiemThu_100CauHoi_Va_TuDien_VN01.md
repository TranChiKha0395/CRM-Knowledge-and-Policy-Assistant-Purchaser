# CÔNG TY CỔ PHẦN THIẾT BỊ CÔNG NGHIỆP SONG NHẬT (PURCHASER)
**DỰ ÁN: CRM KNOWLEDGE & POLICY ASSISTANT (CKPA / SCRM) — CỔNG G1**  
*Mã Story cha:* `CKPA-53` (CRM-G1-ST03) | *Mã Sub-task:* `CKPA-55` (CRM-G1-SUB08)  
*Mã Tiêu chí Cổng G1:* `G1-AC07`  
*GitHub Branch:* `uat/CRM-G1-SUB08-100-real-tasks-vn01-terms`  
*Phía RFP:* Purchaser  
*Priority:* Medium  
*Components (RFP):* Evaluation-Dataset, WP03-Selection  
*RFP Traceability ID:* Mục 8 (Evaluation), Mục 11 (Staff users), ANS 02, SEC 02, SEC 06, VN 01  
*Deliverable / Evidence:* 100 Câu hỏi Thực tế Đợt 1 (Sạch PII) & Từ điển Viết tắt CRM Tiếng Việt  
*Assignee / Lead:* `[P4] Trà My (Staff users)`  
*Reporter / Nghiệm thu (PO/SM):* `[P1] Mỹ Vân (Purchaser sponsor / Product Owner)`  
*Collaborators / RACI:* `[P5] Anh Khoa, [S3] Yến Nhi` (Tiếp nhận: `[S4] Quý Hải, [S3] Yến Nhi`)  
*Lịch thực hiện:* 2026-11-09 → 2026-11-10 (Original Estimate: 16h)  

---

# BIÊN BẢN NGHIỆM THU ĐẦU RA SUB-TASK CKPA-55
### 100 CÂU HỎI THỰC TẾ ĐỢT 1 (60 DEV + 40 VAL SẠCH 100% PII) & TỪ ĐIỂN VIẾT TẮT CRM TIẾNG VIỆT (VN 01 PROFILE)

---

### ĐỐI SOÁT TIÊU CHÍ NGHIỆM THU (ACCEPTANCE CRITERIA BDD: GIVEN - WHEN - THEN)

* **GIVEN (Điều kiện tiền đề):** Đã có Question Inventory $\ge 4$ tuần từ Giai đoạn Discovery G0 và Hồ sơ Phân tích ngôn ngữ VN 01 Profile.
* **WHEN (Hành động thực thi):** `[P4] Trà My` cùng 4 nhân viên nghiệp vụ Bên mua SongNhat (ngoài S1–S5) trích xuất, làm sạch 100 câu hỏi thực tế đầu tiên (0% PII theo SEC 02/06) và tổng hợp bảng Từ điển Viết tắt CRM tiếng Việt VN 01.
* **THEN (Kết quả đầu ra):** Đã bàn giao đầy đủ tập 100 câu hỏi sạch PII (60 DEV + 40 VAL) cho `[S4] Quý Hải` phục vụ kiểm thử độc lập, và bàn giao Từ điển VN 01 cho `[S3] Yến Nhi` tích hợp vào module truy xuất ANS 02 (`backend/src/modules/retrieval/models.py`). `[P1] Mỹ Vân` xác nhận nghiệm thu đạt 100% yêu cầu.

---

### I. KẾT QUẢ THẨM ĐỊNH TẬP 100 CÂU HỎI THỰC TẾ ĐỢT 1 (60 DEV + 40 VAL)

| Mã quy trình | Tên quy trình nghiệp vụ SongNhat | Phân vùng DEV | Phân vùng VAL | Tổng số câu hỏi |
|---|---|:---:|:---:|:---:|
| **POL-001** | Quy trình Báo giá & Phê duyệt Thương mại | 24 ca | 16 ca | **40 ca (40%)** |
| **POL-002** | Quy trình Xử lý Thông tin & Dữ liệu Khách hàng | 18 ca | 12 ca | **30 ca (30%)** |
| **POL-003** | Quy trình Tiếp nhận Dịch vụ & Bảo hành Kỹ thuật | 18 ca | 12 ca | **30 ca (30%)** |
| **TỔNG CỘNG** | **ĐỦ 3 HỌ CHÍNH SÁCH CỐT LÕI (BASE SCOPE)** | **60 ca** | **40 ca** | **100 ca thực tế** |

#### Kết quả kiểm toán an toàn bảo mật PII (RFP SEC 02 & SEC 06):
* **Rà soát số điện thoại cá nhân:** 0 phát hiện (Không có số điện thoại thật).
* **Rà soát số CCCD / CMND:** 0 phát hiện (Không có số định danh 9 hoặc 12 chữ số).
* **Rà soát Email cá nhân:** 0 phát hiện (Chỉ dùng domain tổ chức hoặc email mẫu).
* **Tên đối tác & khách hàng:** 100% được ẩn danh hóa sang mã B2B hoặc tên pháp nhân giả định.
* **Kiểm soát phân định vai trò SoD:** Đã cập nhật trạng thái `PENDING_P2_P3_REVIEW` cho 100 ca, dành quyền thẩm định và ký duyệt nhãn vàng chính thức cho `[P2] Hữu Tài` và `[P3] Chí Kha` tại Sprint 4 (CKPA-68 / SUB18).

---

### II. KẾT QUẢ THẨM ĐỊNH TỪ ĐIỂN VIẾT TẮT CRM & CHUẨN HÓA TRUY VẤN VN 01

Bộ từ điển `vn01_crm_dictionary.json` do `[P4] Trà My` xây dựng gồm 4 cấu phần đáp ứng toàn diện ANS 02 & VN 01:
1. **42 Nhóm từ viết tắt CRM (abbreviations):** Bao phủ toàn bộ thuật ngữ thương mại, chiết khấu, chức danh phê duyệt (`cvkd`, `tpkd`, `gdkd`, `gdcn`, `tgd`), dịch vụ bảo hành (`cskh`, `bh`, `bd`, `cvdv`, `ktv`) và kho vận pháp lý (`po`, `bo`, `stock`, `mst`, `cccd`, `pii`, `sla`, `sop`).
2. **31 Cụm từ tiếng Việt không dấu (unaccent_mappings):** Tự động khôi phục dấu tiếng Việt chuẩn xác cho các truy vấn gõ nhanh (`chiet khau` $\rightarrow$ chiết khấu, `bao gia` $\rightarrow$ báo giá, `bien tan` $\rightarrow$ biến tần, `dong co` $\rightarrow$ động cơ...).
3. **16 Thuật ngữ kỹ thuật & sản phẩm song ngữ (technical_and_product_terms):** Chuẩn hóa các dòng sản phẩm chủ lực (`motor 3 pha`, `inverter`, `gearbox`, `explosion proof motor`) và thuật ngữ vận hành (`tombstone`, `quarantine`, `hold`, `referral`).
4. **Bảo toàn 14 từ phủ định tiếng Việt bắt buộc (vietnamese_negations_preserved):** Giữ nguyên các từ: `không`, `chưa`, `chẳng`, `miễn`, `ngoại trừ`, `ngoài`, `không được`, `cấm`, `loại trừ`, `không áp dụng`, `vắng mặt`, `thiếu`, `từ chối`, `hủy` để tránh làm đảo ngược hoàn toàn ngữ nghĩa truy vấn.

---

### III. KẾT LUẬN NGHIỆM THU CỦA PRODUCT OWNER / PURCHASER SPONSOR [P1] MỸ VÂN

1. **Xác nhận bàn giao:** Tập 100 câu hỏi thực tế (60 DEV + 40 VAL) và Bộ Từ điển VN 01 đã được bàn giao đầy đủ cho `[S4] Quý Hải` và `[S3] Yến Nhi`.
2. **Quyết định:** **CHẤP THUẬN NGHIỆM THU ĐẠT CHUẨN SUB-TASK CKPA-55 (CRM-G1-SUB08).**
3. **Đóng thẻ trên Jira:** Chuyển trạng thái ticket CKPA-55 sang **DONE**.

*(Ký duyệt ngày 19/11/2026)*

| NGƯỜI LẬP & BÀN GIAO / ASSIGNEE [P4] | NGƯỜI NGHIỆM THU / PRODUCT OWNER [P1] |
|:---:|:---:|
| *(Đã ký bàn giao)* | *(Đã thẩm định & Chấp thuận nghiệm thu)* |
| <br><br>**TRÀ MY** | <br><br>**MỸ VÂN** |
