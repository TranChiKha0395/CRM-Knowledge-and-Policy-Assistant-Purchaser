# CÔNG TY CỔ PHẦN THIẾT BỊ CÔNG NGHIỆP SONG NHẬT
**DỰ ÁN: CRM KNOWLEDGE & POLICY ASSISTANT (CKPA / SCRM)**  
*Mã Story:* `CKPA-4` (CRM-G0-ST01) | *Mã Sub-task:* `CKPA-5` (CRM-G0-SUB01)  
*Mã Tiêu chí Cổng G0:* `G0-AC01`  
*Căn cứ RFP Traceability ID:* Mục 8 (Evaluation Framework), Mục 11 (Five representative staff users), Mục 14 (Decisions before award)  
*Phía RFP:* Purchaser  
*Priority:* Highest  
*Components (RFP):* WP01-Discovery, Governance-SoD  
*Lead / Assignee:* `[P1] Mỹ Vân (Purchaser sponsor)`  
*Reporter / Nghiệm thu (PO/SM):* `[S1] Hoàng Tiến (Named lead)`  
*Collaborators / RACI:* `[P4] Trà My`, `[P2] Hữu Tài`, `[P3] Chí Kha`, `[P5] Anh Khoa`  
*Lịch thực hiện:* 2026-11-09 → 2026-11-09 (Ngày đầu tiên Sprint 1 - Capped Discovery)  

---

# BIÊN BẢN KHỞI ĐỘNG VÀ HIẾN CHƯƠNG GIAI ĐOẠN KHẢO SÁT (DISCOVERY CHARTER)
### & QUYẾT ĐỊNH CHỈ ĐỊNH 5 REPRESENTATIVE STAFF USERS (100% PURCHASER)

---

### PHẦN 1. HIẾN CHƯƠNG GIAI ĐOẠN KHẢO SÁT (DISCOVERY CHARTER)

#### 1. Thời gian và Cơ chế triển khai
Căn cứ Hồ sơ Yêu cầu (RFP) dự án CRM Knowledge & Policy Assistant, Ban Giám đốc và Nhà tài trợ dự án (**[P1] Mỹ Vân**) chính thức phê duyệt khởi động giai đoạn Khảo sát có giới hạn thời gian (**Capped Discovery — 2 tuần**, từ ngày 09/11/2026 đến ngày 22/11/2026).
- **Sprint 1 (DUO W1):** 2026-11-09 đến 2026-11-13.
- **Sprint 2 (DUO W2):** 2026-11-16 đến 2026-11-20.
- **Cơ chế quản trị:** Áp dụng mô hình Scrum thích ứng (PO = `[P1] Mỹ Vân`, SM = `[S1] Hoàng Tiến`), tuân thủ nguyên tắc nhịp bền vững $\le 8$h/ngày và $\le 40$h/tuần/vai trò.

#### 2. Mục tiêu trọng tâm của Discovery (G0)
1. **Khảo sát dữ liệu thực tế (WP01):** Trích xuất danh mục câu hỏi lịch sử thực tế $\ge 4$ tuần (Question Inventory $\ge 4$w) đã làm sạch 0% PII; đo lường thời gian thao tác cơ sở (Baseline Effort: minh họa RFP ~7,0 phút/tác vụ thủ công) làm mốc đánh giá giảm $\ge 20\%$ công sức tại G3.
2. **Chuẩn hóa tri thức chính sách:** Đóng băng phạm vi 3 họ chính sách nghiệp vụ cốt lõi:
   - `POL-001`: Quy định Thẩm quyền Báo giá, Chiết khấu & Điều kiện Thương mại.
   - `POL-002`: Chính sách Thu thập, Quản trị & Bảo mật Dữ liệu Khách hàng (0% PII).
   - `POL-003`: Quy chuẩn Dịch vụ Kỹ thuật, Bảo hành, Đổi trả & RMA.
3. **Thiết kế kiến trúc và Kế hoạch kiểm định:** Thống nhất Bản thiết kế kiến trúc DEL 01, Điều khoản vận hành DEL 06, Kế hoạch kiểm định độc lập 280 ca (Annex B) và Bảng báo giá TCO 3 năm 13 hạng mục VND DEL 05.
4. **Sẵn sàng Cổng G0 (Ready to Build):** Thẩm định toàn diện 7 nhóm bằng chứng Cổng G0 theo Mục 9 và Mục 14 RFP để ra quyết định Base Scope và tách riêng Tùy chọn O1.

#### 3. Quy chế Phân định Trách nhiệm (Separation of Duties - SoD) theo Mục 8 & Mục 11
Nhằm bảo đảm tính khách quan, minh bạch và an toàn tuyệt đối, hai bên cam kết tuân thủ nghiêm ngặt nguyên tắc phân định quyền hạn:
* **Hàng rào độc lập (Chinese Wall):** 
  - Toàn bộ tập dữ liệu kiểm định độc lập gồm 100 câu hỏi Niêm phong (*100 Sealed Acceptance Cases*) và 80 kịch bản Thách thức (*80 Constructed Challenges*) do `[S4] Quý Hải` và nhóm Purchaser đồng quản lý trong kho lưu trữ riêng biệt (`sealed-eval-repo`).
  - Chặn tuyệt đối quyền truy cập (Read/Clone) đối với đội ngũ phát triển kỹ thuật (`[S2] Quốc Hưng` - Integration, `[S3] Yến Nhi` - Retrieval/App).
* **Nguyên tắc Assignee != Reporter trên Jira:** Chấm dứt triệt để tình trạng tự duyệt. Mọi nhiệm vụ và sản phẩm bàn giao Cổng G0 do Supplier hay Purchaser thực hiện đều phải có Reporter độc lập đối soát trước khi đóng thẻ.
* **Ma trận 10 Vai trò Dự án chuẩn RFP Mục 11:**
  - **Phía Bên mua (Purchaser P1–P5):**
    - `[P1] Mỹ Vân`: Purchaser sponsor / Product Owner (Chủ trì phê duyệt Cổng & ngân sách).
    - `[P2] Hữu Tài`: Policy owners (Chủ sở hữu chính sách / Policy Reviewer #1).
    - `[P3] Chí Kha`: Knowledge and data steward (Quản lý tri thức & Dữ liệu nguồn / Reviewer #2).
    - `[P4] Trà My`: Staff users (Đầu mối 5 Representative Staff Users).
    - `[P5] Anh Khoa`: Privacy and security owners (Chủ sở hữu Bảo mật & Pháp lý).
  - **Phía Nhà cung cấp (Supplier S1–S5):**
    - `[S1] Hoàng Tiến`: Named lead (Trưởng nhóm định danh / Scrum Master).
    - `[S2] Quốc Hưng`: Integration engineer (Kỹ sư Tích hợp & Dữ liệu - Đội Build).
    - `[S3] Yến Nhi`: Retrieval and application engineer (Kỹ sư Truy xuất & Ứng dụng - Đội Build).
    - `[S4] Quý Hải`: Quality lead (Trưởng nhóm Chất lượng & Kiểm định độc lập).
    - `[S5] Ngọc Duy`: Operations specialist (Chuyên viên Vận hành & Hạ tầng).

#### 4. Ranh giới Phạm vi Triển khai (Scope Boundary)
* Dự án tập trung triển khai **Base Scope** dựa trên 2 cấu trúc dữ liệu phẳng (`passages` và `critical_fields`).
* Tùy chọn **O1 (Selected CRM Context)** tạm hoãn, bắt buộc phải có văn bản phê duyệt riêng từ P1, không tự động tích hợp trong giai đoạn Discovery để loại trừ hoàn toàn nguy cơ rò rỉ dữ liệu khách hàng thật theo Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15.

---

### PHẦN 2. DANH SÁCH 5 REPRESENTATIVE STAFF USERS (100% PURCHASER)

Căn cứ quy định tại **Mục 8 & Mục 11 RFP** (*"Đầu mối nhóm 5 người dùng nghiệp vụ đại diện phía Bên mua: [P4] Trà My cùng [P1] Mỹ Vân, [P2] Hữu Tài, [P3] Chí Kha, [P5] Anh Khoa ngoài đội Build & Nhà cung cấp — nghiêm cấm nhân sự phía Supplier Team tham gia nhóm 5 Representative Staff Users"*):  
Nhà tài trợ dự án [P1] Mỹ Vân chính thức ký quyết định chốt danh sách 5 nhân sự đại diện người dùng nghiệp vụ thuộc phía Bên mua SongNhat:

| STT | Thành viên | Mã Role | Định danh RFP / Tên vai trò tiếng Việt | Phạm vi nghiệp vụ & Trách nhiệm tại G0 |
|:---:|---|:---:|---|---|
| **1** | **Trà My** | `[P4]` | **Staff users (Đầu mối 5 Representative Staff Users)** | Chủ trì trích xuất $\ge 4$ tuần lịch sử câu hỏi thực tế; xây dựng tập 60 DEV + 40 VAL; kiểm thử từ điển viết tắt CRM tiếng Việt VN 01. |
| **2** | **Mỹ Vân** | `[P1]` | **Purchaser sponsor (Nhà tài trợ / Chủ đầu tư dự án)** | Chủ trì thẩm định trải nghiệm người dùng, giám sát đo lường Baseline Effort, duyệt Discovery Charter & quyết định Cổng G0. |
| **3** | **Hữu Tài** | `[P2]` | **Policy owners (Chủ sở hữu chính sách)** | Cung cấp câu hỏi thực tế và thẩm định chuyên môn về thẩm quyền báo giá, biên độ chiết khấu, hạn mức công nợ theo `POL-001`. |
| **4** | **Chí Kha** | `[P3]` | **Knowledge and data steward (Quản lý tri thức & Dữ liệu nguồn)** | Cung cấp câu hỏi về quy trình tra cứu dữ liệu, trường trọng yếu, liên kết footnotes và các trường hợp ngoại lệ theo `POL-002` & `POL-003`. |
| **5** | **Anh Khoa** | `[P5]` | **Privacy and security owners (Chủ sở hữu Bảo mật & Pháp lý)** | Cung cấp câu hỏi và kiểm thử các tình huống tra cứu thông tin khách hàng, rà soát 0% PII và tuân thủ Luật Bảo vệ dữ liệu cá nhân. |

---

### PHẦN 3. CAM KẾT VÀ BẢO ĐẢM TÍNH ĐỘC LẬP THEO MỤC 8 & MỤC 11 RFP

1. **Tỷ lệ nhân sự Bên mua (Purchaser Ratio):**
   - Đại diện Bên mua [P1] Mỹ Vân khẳng định: **Toàn bộ 5 nhân sự nêu trên 100% thuộc phía Purchaser (SongNhat)**.
2. **Loại trừ tuyệt đối nhân sự Bên bán (0% Supplier):**
   - Xác nhận **TUYỆT ĐỐI 0% nhân sự thuộc Supplier Team** tham gia vào nhóm 5 Representative Users này.
   - Nghiêm cấm [S1] Hoàng Tiến (SM), [S2] Quốc Hưng, [S3] Yến Nhi (đội Build), [S4] Quý Hải (Independent QA) và [S5] Ngọc Duy (Ops) tham gia đóng vai người dùng đại diện để bảo đảm tính khách quan tuyệt đối cho tập câu hỏi khảo sát và số liệu đo Baseline Effort (~7,0 phút/tác vụ thủ công).

---

### PHẦN 4. KÝ DUYỆT VÀ HIỆU LỰC

Văn bản này có hiệu lực kể từ ngày ký (09/11/2026). Toàn bộ 10 thành viên hai bên cam kết tuân thủ đúng nội dung Hiến chương này.

| ĐẠI DIỆN CHỦ ĐẦU TƯ / PURCHASER SPONSOR [P1] | ĐẠI DIỆN NHÀ CUNG CẤP / PROJECT MANAGER [S1] |
|:---:|:---:|
| *(Đã ký duyệt)* | *(Đã ký cam kết tuân thủ)* |
| <br><br>**MỸ VÂN** | <br><br>**HOÀNG TIẾN** |
