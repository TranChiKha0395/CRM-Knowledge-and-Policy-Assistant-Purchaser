# BẢNG PHÂN CÔNG VÀ HƯỚNG DẪN NỘP LẠI BÀI TẬP LÊN JIRA CLOUD (GATE G0)
## Dự án: CRM Knowledge and Policy Assistant (`CKPA`)
### Căn cứ: RFP Mục 11 (10 Chuẩn vai & Tách vai SoD) & Phân công công việc Cổng G0 (`PhanCongCongViec_G0.xlsx`)

> **Thư mục lưu trữ bài nộp mới đã chỉnh sửa:** `CKPA_Submissions_G0_Final`
> - Toàn bộ 32 tệp bài nộp đã được cập nhật chuẩn xác: định danh 10 vai trò RFP (P1–P5 Bên Mua | S1–S5 Nhà cung cấp), chuẩn hóa mã Jira Cloud (`CKPA-4` .. `CKPA-43`), tách vai kiểm định độc lập (S4 Quý Hải) và Two Policy Reviewers (P2 Hữu Tài, P3 Chí Kha).
> - Mỗi thành viên kiểm tra dòng tên mình trong bảng dưới đây, vào thư mục tương ứng trong `by_jira_task/` lấy tệp và đính kèm vào đúng mã Issue trên Jira.

---

## 1. BẢNG TRA CỨU: TASK JIRA + TÊN FILE + NGƯỜI PHỤ TRÁCH NỘP LẠI

| STT | Mã Jira Task | Loại Task | Mã Backlog G0 | Tóm tắt Task (Summary trên Jira) | Tên File Bài Nộp (Đã chỉnh sửa) | Người Phụ Trách (Assignee) | Mã Role RFP | Jira Account / Email | Thư mục Chứa File |
|:---:|:---:|:---:|:---:|---|---|---|:---:|---|---|
| 1 | `CKPA-6` | Sub-task | `CRM-G0-SUB02` | [G0][Mục2] Trích xuất >=4w Log & Kiểm kê Phần mềm | `CKPA-2_02_Question_Inventory_4Week_Representative.csv` | **Ngô Thị Trà My** | `P4` | `tra.my@songnhat.com.vn` | `CKPA-04_ST01_[P4]_TraMy_Charter-Log-Baseline` |
| 2 | `CKPA-7` | Sub-task | `CRM-G0-SUB03` | [G0][VN06] Kiểm chứng Baseline Effort & 5 NSD độc lập | `CKPA-2_03_Baseline_Effort_Measurement_Log.csv` | **Phạm Quý Hải** | `S4` | `quy.hai@supplier.example.vn` | `CKPA-04_ST01_[P4]_TraMy_Charter-Log-Baseline` |
| 3 | `CKPA-4` | Story | `CRM-G0-ST01` | [G0][WP01] Hoàn tất Charter, 4w Log & Baseline | `CKPA-2_Bao_Cao_Kiem_Ke_Nguon_Question_Inventory_Va_Baseline_G0.md` | **Ngô Thị Trà My** | `P4` | `tra.my@songnhat.com.vn` | `CKPA-04_ST01_[P4]_TraMy_Charter-Log-Baseline` |
| 4 | `CKPA-9` | Sub-task | `CRM-G0-SUB04` | [G0][DAT03] Chốt 3 họ, Ma trận 5 lớp & Quy tắc Hold | `CKPA-1_01_Policy_Families_And_Owners_Signoff.csv` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 5 | `CKPA-10` | Sub-task | `CRM-G0-SUB05` | [G0][DAT04] Ánh xạ 6 chiều Phạm vi & 9 ca Annex B | `CKPA-1_02_Base_Scope_O1_And_Out_Of_Scope_Matrix.csv` | **Trần Chí Kha** | `P3` | `chi.kha@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 6 | `CKPA-8` | Story | `CRM-G0-ST02` | [G0][WP01] Chốt 3 họ, Ma trận Thẩm quyền & Ngày | `CKPA-1_Bien_Ban_Xac_Nhan_Pham_Vi_G0_Va_3_Nhom_Chinh_Sach.md` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 7 | `CKPA-9` | Sub-task | `CRM-G0-SUB04` | [G0][DAT03] Chốt 3 họ, Ma trận 5 lớp & Quy tắc Hold | `CKPA-4_01_Authority_Matrix_5_Layers.csv` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 8 | `CKPA-9` | Sub-task | `CRM-G0-SUB04` | [G0][DAT03] Chốt 3 họ, Ma trận 5 lớp & Quy tắc Hold | `CKPA-4_02_Governing_Date_And_Conflict_Hold_Rules.csv` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 9 | `CKPA-9` | Sub-task | `CRM-G0-SUB04` | [G0][DAT03] Chốt 3 họ, Ma trận 5 lớp & Quy tắc Hold | `CKPA-4_Authority_and_Governing_Date_Matrix-v4.docx` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 10 | `CKPA-9` | Sub-task | `CRM-G0-SUB04` | [G0][DAT03] Chốt 3 họ, Ma trận 5 lớp & Quy tắc Hold | `CKPA-4_Ma_Tran_Tham_Quyen_5_Lop_Va_Quy_Tac_Ngay_Hieu_Luc_G0.md` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-08_ST02_[P2]_HuuTai_Policy-Authority-Matrix` |
| 11 | `CKPA-13` | Sub-task | `CRM-G0-SUB07` | [G0][DAT01] Thiết kế Field Dict & 2 Base+O1 Schemas | `critical_fields_template.csv` | **Trần Quốc Hưng** | `S2` | `quoc.hung@supplier.example.vn` | `CKPA-12_ST03_[S2]_QuocHung_Data-Design-ERD-CSV` |
| 12 | `CKPA-13` | Sub-task | `CRM-G0-SUB07` | [G0][DAT01] Thiết kế Field Dict & 2 Base+O1 Schemas | `passages_template.csv` | **Trần Quốc Hưng** | `S2` | `quoc.hung@supplier.example.vn` | `CKPA-12_ST03_[S2]_QuocHung_Data-Design-ERD-CSV` |
| 13 | `CKPA-12` | Story | `CRM-G0-ST03` | [G0][DEL01] Thiết kế Field Dict & Base/O1 CSV | `erd_and_csv_contracts_revised.md` | **Trần Quốc Hưng** | `S2` | `quoc.hung@supplier.example.vn` | `CKPA-12_ST03_[S2]_QuocHung_Data-Design-ERD-CSV` |
| 14 | `CKPA-17` | Sub-task | `CRM-G0-SUB10` | [G0][SEC01] Thiết kế RBAC 20-User & Pháp lý Annex F | `rbac-matrix.md` | **Nguyễn Anh Khoa** | `P5` | `anh.khoa@songnhat.com.vn` | `CKPA-16_ST04_[P5]_AnhKhoa_Security-RBAC-AnnexC` |
| 15 | `CKPA-19` | Sub-task | `CRM-G0-SUB12` | [G0][AnnexC] Đề xuất Lịch lưu giữ 90d/12m/35d & Hold | `P1_RaSoat_Retention_v1_HoanChinh.docx` | **Nguyễn Anh Khoa** | `P5` | `anh.khoa@songnhat.com.vn` | `CKPA-16_ST04_[P5]_AnhKhoa_Security-RBAC-AnnexC` |
| 16 | `CKPA-18` | Sub-task | `CRM-G0-SUB11` | [G0][SEC04] Kê khai Hạ tầng, Subprocessor & OPS01-08 | `231b21cc-8b0b-45ee-ba6f-401fd214fca6.png` | **Nguyễn Ngọc Duy** | `S5` | `ngoc.duy@supplier.example.vn` | `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` |
| 17 | `CKPA-18` | Sub-task | `CRM-G0-SUB11` | [G0][SEC04] Kê khai Hạ tầng, Subprocessor & OPS01-08 | `3e2484e8-2d2d-470b-874d-e11a830d1535.png` | **Nguyễn Ngọc Duy** | `S5` | `ngoc.duy@supplier.example.vn` | `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` |
| 18 | `CKPA-18` | Sub-task | `CRM-G0-SUB11` | [G0][SEC04] Kê khai Hạ tầng, Subprocessor & OPS01-08 | `8c1b2f34-5c3a-45f6-89bf-f291eb895714.png` | **Nguyễn Ngọc Duy** | `S5` | `ngoc.duy@supplier.example.vn` | `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` |
| 19 | `CKPA-18` | Sub-task | `CRM-G0-SUB11` | [G0][SEC04] Kê khai Hạ tầng, Subprocessor & OPS01-08 | `Screenshot 2026-11-18 023015.png` | **Nguyễn Ngọc Duy** | `S5` | `ngoc.duy@supplier.example.vn` | `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` |
| 20 | `CKPA-18` | Sub-task | `CRM-G0-SUB11` | [G0][SEC04] Kê khai Hạ tầng, Subprocessor & OPS01-08 | `Screenshot 2026-11-18 023030.png` | **Nguyễn Ngọc Duy** | `S5` | `ngoc.duy@supplier.example.vn` | `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` |
| 21 | `CKPA-25` | Sub-task | `CRM-G0-SUB16` | [G0][DEL01-C] Lập Source Register & Mẫu 30+10 DAT08 | `CKPA-2_01_Source_Registry_And_Gap_Analysis.csv` | **Trần Chí Kha** | `P3` | `chi.kha@songnhat.com.vn` | `CKPA-24_ST06_[P3]_ChiKha_Curation-30Passages-10Fields` |
| 22 | `CKPA-25` | Sub-task | `CRM-G0-SUB16` | [G0][DEL01-C] Lập Source Register & Mẫu 30+10 DAT08 | `critical_fields.csv` | **Trần Chí Kha** | `P3` | `chi.kha@songnhat.com.vn` | `CKPA-24_ST06_[P3]_ChiKha_Curation-30Passages-10Fields` |
| 23 | `CKPA-25` | Sub-task | `CRM-G0-SUB16` | [G0][DEL01-C] Lập Source Register & Mẫu 30+10 DAT08 | `passages.csv` | **Trần Chí Kha** | `P3` | `chi.kha@songnhat.com.vn` | `CKPA-24_ST06_[P3]_ChiKha_Curation-30Passages-10Fields` |
| 24 | `CKPA-27` | Sub-task | `CRM-G0-SUB18` | [G0][Mục2] Duyệt Mẫu 30+10 & Ngân sách Curation G1 | `CKPA-3_Bien_Ban_Phe_Duyet_30_Passages_10_Critical_Fields_Va_Ke_Hoach_G1.md` | **Lý Hữu Tài** | `P2` | `huu.tai@songnhat.com.vn` | `CKPA-24_ST06_[P3]_ChiKha_Curation-30Passages-10Fields` |
| 25 | `CKPA-30` | Sub-task | `CRM-G0-SUB20` | [G0][DEL01-G] Chốt Kế hoạch 60/40/100 + 80 & Kho riêng | `testing-tiers.md` | **Phạm Quý Hải** | `S4` | `quy.hai@supplier.example.vn` | `CKPA-28_ST07_[S4]_QuyHai_EvalPlan-280Cases-TestingTiers` |
| 26 | `CKPA-30` | Sub-task | `CRM-G0-SUB20` | [G0][DEL01-G] Chốt Kế hoạch 60/40/100 + 80 & Kho riêng | `CKPA-10_01_Quy_Chuan_Kiem_Thu_Doc_Lap_Va_Mau_So_Bao_Cao.docx` | **Phạm Quý Hải** | `S4` | `quy.hai@supplier.example.vn` | `CKPA-28_ST07_[S4]_QuyHai_EvalPlan-280Cases-TestingTiers` |
| 27 | `CKPA-30` | Sub-task | `CRM-G0-SUB20` | [G0][DEL01-G] Chốt Kế hoạch 60/40/100 + 80 & Kho riêng | `CKPA-10_02_Bo_60_Dev_Tasks_Cong_Khai_Clean_PII.docx` | **Phạm Quý Hải** | `S4` | `quy.hai@supplier.example.vn` | `CKPA-28_ST07_[S4]_QuyHai_EvalPlan-280Cases-TestingTiers` |
| 28 | `CKPA-30` | Sub-task | `CRM-G0-SUB20` | [G0][DEL01-G] Chốt Kế hoạch 60/40/100 + 80 & Kho riêng | `CKPA-10_G0_60_Dev_Tasks_Public_Partition-v2.csv` | **Phạm Quý Hải** | `S4` | `quy.hai@supplier.example.vn` | `CKPA-28_ST07_[S4]_QuyHai_EvalPlan-280Cases-TestingTiers` |
| 29 | `CKPA-34` | Sub-task | `CRM-G0-SUB23` | [G0][DEL01-F] Chốt Hồ sơ Pháp lý, O1 & Lịch Annex C | `legal-privacy-review.md` | **Nguyễn Anh Khoa** | `P5` | `anh.khoa@songnhat.com.vn` | `CKPA-32_ST08_[P5]_AnhKhoa_[S5]_NgocDuy_Operating-Terms-Legal` |
| 30 | `CKPA-34` | Sub-task | `CRM-G0-SUB23` | [G0][DEL01-F] Chốt Hồ sơ Pháp lý, O1 & Lịch Annex C | `P1_HoSoPhapLy_CoNgay_v1_HoanChinh.docx` | **Nguyễn Anh Khoa** | `P5` | `anh.khoa@songnhat.com.vn` | `CKPA-32_ST08_[P5]_AnhKhoa_[S5]_NgocDuy_Operating-Terms-Legal` |
| 31 | `CKPA-37` | Sub-task | `CRM-G0-SUB25` | [G0][DEL01-I] So sánh 3 Phương án & Lịch 10 tuần | `g0-3-route-comparison-and-decision.md` | **Hoàng Tiến** | `S1` | `hoang.tien@supplier.example.vn` | `CKPA-36_ST09_[S1]_HoangTien_3Route-Comparison-TCO` |
| 32 | `CKPA-42` | Sub-task | `CRM-G0-SUB29` | [G0][Mục9] Chủ trì G0, Duyệt Base/O1 & 10% Payment | `P1_QuyetDinhRoute_v1_HoanChinh.docx` | **Văn Mỹ Vân** | `P1` | `my.van@songnhat.com.vn` | `CKPA-40_ST10_[P1]_MyVan_GateG0-Decision-Signoff` |

---

## 2. HƯỚNG DẪN CHI TIẾT HÀNH ĐỘNG NỘP LẠI CHO TỪNG THÀNH VIÊN

### Nhóm Bên Mua (Purchaser Team — P1 đến P5):
1. **[P1] Văn Mỹ Vân (Purchaser Sponsor / Product Owner):**
   - **Task Jira:** `CKPA-42` (Sub-task `CRM-G0-SUB29` thuộc Story `CKPA-40`)
   - **Tệp nộp:** `P1_QuyetDinhRoute_v1_HoanChinh.docx` (Tại thư mục `CKPA-40_ST10_[P1]_MyVan_GateG0-Decision-Signoff`)
   - **Hành động:** Đăng nhập tài khoản `van.my`, mở task `CKPA-42`, bấm **Attach** và tải lên văn bản quyết định phê duyệt phương án Base Scope / O1 và ký duyệt giải ngân 10% Gate G0.

2. **[P2] Lý Hữu Tài (Policy Owner — Policy Reviewer #1):**
   - **Task Jira:** 
     - `CKPA-8` (Story `CRM-G0-ST02`): Nộp `CKPA-1_Bien_Ban_Xac_Nhan_Pham_Vi_G0_Va_3_Nhom_Chinh_Sach.md`
     - `CKPA-9` (Sub-task `CRM-G0-SUB04`): Nộp 5 tệp: `CKPA-1_01_Policy_Families_And_Owners_Signoff.csv`, `CKPA-4_01_Authority_Matrix_5_Layers.csv`, `CKPA-4_02_Governing_Date_And_Conflict_Hold_Rules.csv`, `CKPA-4_Authority_and_Governing_Date_Matrix-v4.docx`, `CKPA-4_Ma_Tran_Tham_Quyen_5_Lop_Va_Quy_Tac_Ngay_Hieu_Luc_G0.md`
     - `CKPA-27` (Sub-task `CRM-G0-SUB18` thuộc Story `CKPA-24`): Nộp `CKPA-3_Bien_Ban_Phe_Duyet_30_Passages_10_Critical_Fields_Va_Ke_Hoach_G1.md`
   - **Hành động:** Vào các thư mục `CKPA-08_...` và `CKPA-24_...`, đính kèm các tệp trên vào đúng các task `CKPA-8`, `CKPA-9` và `CKPA-27`.

3. **[P3] Trần Chí Kha (Knowledge and Data Steward — Policy Reviewer #2):**
   - **Task Jira:**
     - `CKPA-10` (Sub-task `CRM-G0-SUB05` thuộc Story `CKPA-8`): Nộp `CKPA-1_02_Base_Scope_O1_And_Out_Of_Scope_Matrix.csv`
     - `CKPA-25` (Sub-task `CRM-G0-SUB16` thuộc Story `CKPA-24`): Nộp 3 tệp: `CKPA-2_01_Source_Registry_And_Gap_Analysis.csv`, `critical_fields.csv`, `passages.csv`
   - **Hành động:** Đính kèm các tệp biểu mẫu tri thức, nguồn dữ liệu và 30 passages + 10 critical fields vào `CKPA-10` và `CKPA-25`.

4. **[P4] Ngô Thị Trà My (Staff Users Lead — Đại diện 5 Người dùng nghiệp vụ):**
   - **Task Jira:**
     - `CKPA-4` (Story `CRM-G0-ST01`): Nộp `CKPA-2_Bao_Cao_Kiem_Ke_Nguon_Question_Inventory_Va_Baseline_G0.md`
     - `CKPA-6` (Sub-task `CRM-G0-SUB02`): Nộp `CKPA-2_02_Question_Inventory_4Week_Representative.csv`
   - **Hành động:** Lấy tệp từ `CKPA-04_ST01_[P4]_TraMy_Charter-Log-Baseline` và đính kèm lên Jira `CKPA-4` và `CKPA-6`.

5. **[P5] Nguyễn Anh Khoa (Privacy and Security Owner):**
   - **Task Jira:**
     - `CKPA-17` (Sub-task `CRM-G0-SUB10` thuộc Story `CKPA-16`): Nộp `rbac-matrix.md`
     - `CKPA-19` (Sub-task `CRM-G0-SUB12` thuộc Story `CKPA-16`): Nộp `P1_RaSoat_Retention_v1_HoanChinh.docx`
     - `CKPA-34` (Sub-task `CRM-G0-SUB23` thuộc Story `CKPA-32`): Nộp 2 tệp: `legal-privacy-review.md` và `P1_HoSoPhapLy_CoNgay_v1_HoanChinh.docx`
   - **Hành động:** Đính kèm hồ sơ bảo mật, RBAC 20 người dùng, rà soát pháp lý và lịch lưu giữ Annex C lên `CKPA-17`, `CKPA-19` và `CKPA-34`.

---

### Nhóm Nhà Cung Cấp (Supplier Team — S1 đến S5):
6. **[S1] Hoàng Tiến (Named Lead / Scrum Master):**
   - **Task Jira:** `CKPA-37` (Sub-task `CRM-G0-SUB25` thuộc Story `CKPA-36`; phối hợp theo dõi `CKPA-39` không có tệp đính kèm riêng)
   - **Tệp nộp:** `g0-3-route-comparison-and-decision.md` (Từ thư mục `CKPA-36_ST09_[S1]_HoangTien_3Route-Comparison-TCO`)
   - **Hành động:** Đính kèm báo cáo so sánh 3 phương án, tiến độ 10 tuần và bảng báo giá 13 hạng mục VND+VAT DEL 05.

7. **[S2] Trần Quốc Hưng (Integration Engineer):**
   - **Task Jira:**
     - `CKPA-12` (Story `CRM-G0-ST03`): Nộp `erd_and_csv_contracts_revised.md`
     - `CKPA-13` (Sub-task `CRM-G0-SUB07`): Nộp 2 tệp: `critical_fields_template.csv` và `passages_template.csv`
   - **Hành động:** Lấy tệp từ `CKPA-12_ST03_[S2]_QuocHung_Data-Design-ERD-CSV` đính kèm vào Story `CKPA-12` và Sub-task `CKPA-13`.

8. **[S3] Phạm Lương Yến Nhi (Retrieval and Application Engineer):**
   - **Task Jira:** Phối hợp cùng [P5] Khoa trên Story `CKPA-16` / `CKPA-17` (và theo dõi thiết kế API/AnswerPackage tại `CKPA-20` / `CKPA-21` — không có tệp nộp riêng trong bảng 32 tệp): Đồng tác giả phần router 12 endpoint API và cấu trúc AnswerPackage 7 thành phần trong `rbac-matrix.md`.

9. **[S4] Phạm Quý Hải (Quality Lead — Trưởng nhóm Kiểm định độc lập):**
   - **Task Jira:**
     - `CKPA-7` (Sub-task `CRM-G0-SUB03` thuộc Story `CKPA-4`): Nộp `CKPA-2_03_Baseline_Effort_Measurement_Log.csv`
     - `CKPA-30` (Sub-task `CRM-G0-SUB20` thuộc Story `CKPA-28`): Nộp 4 tệp: `testing-tiers.md`, `CKPA-10_01_Quy_Chuan_Kiem_Thu_Doc_Lap_Va_Mau_So_Bao_Cao.docx`, `CKPA-10_02_Bo_60_Dev_Tasks_Cong_Khai_Clean_PII.docx`, `CKPA-10_G0_60_Dev_Tasks_Public_Partition-v2.csv`
   - **Ràng buộc SoD:** [S4] Quý Hải hoàn toàn độc lập với code/prompt của S2/S3. Lưu trữ tập niêm phong trong repo riêng `sealed-eval-repo`.

10. **[S5] Nguyễn Ngọc Duy (Operations Specialist — Chuyên viên Vận hành):**
    - **Task Jira:** `CKPA-18` (Sub-task `CRM-G0-SUB11` thuộc Story `CKPA-16`; phối hợp hạ tầng trên `CKPA-33` thuộc `CKPA-32` — không có tệp nộp riêng)
    - **Tệp nộp:** 5 ảnh chụp màn hình kiểm chứng hạ tầng Docker / CI Pipeline:
      - `231b21cc-8b0b-45ee-ba6f-401fd214fca6.png`
      - `3e2484e8-2d2d-470b-874d-e11a830d1535.png`
      - `8c1b2f34-5c3a-45f6-89bf-f291eb895714.png`
      - `Screenshot 2026-11-18 023015.png`
      - `Screenshot 2026-11-18 023030.png`
    - **Hành động:** Lấy ảnh từ thư mục `CKPA-18_SUB11_[S5]_NgocDuy_SecOps-Infra-Screenshots` và đính kèm lên task `CKPA-18`.

---
*Tài liệu được sinh tự động theo chuẩn Jira Cloud và RFP SongNhat CRM Knowledge and Policy Assistant.*
