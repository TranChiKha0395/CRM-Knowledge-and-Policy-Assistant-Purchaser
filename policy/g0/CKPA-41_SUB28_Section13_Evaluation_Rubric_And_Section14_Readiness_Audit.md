> **TRẠNG THÁI:** ĐÃ HOÀN TẤT THẨM ĐỊNH & ĐÓNG CỔNG GATE G0 (`DONE` — `20/11/2026`, tổng điểm kỹ thuật Mục 13 đạt `88.45/100` và chốt `GO BASE SCOPE (O1 = OFF)` tại `governance/g0/gate-signoff/P1_CKPA40_42_Ho_So_Quyet_Dinh_Va_Lenh_Thanh_Toan_Gate_G0.md`; khung báo giá 14 dòng `DEL 05` giữ nguyên tắc minh bạch chờ điền đơn giá VND+VAT ràng buộc trước giải ngân).

# PHIẾU THẨM ĐỊNH KHUNG CHẤM ĐIỂM MỤC 13 (`30/25/20/15/10%`) & ĐỐI SOÁT 7 QUYẾT ĐỊNH SẴN SÀNG CỔNG G0 MỤC 14
## Dự án: SongNhat CRM Knowledge and Policy Assistant (`CKPA`)

- **Pháp nhân Bên mua:** `Công ty Cổ phần Thiết bị Công nghiệp Song Nhật` *(chờ `[P1]` / Legal Owner xác nhận chính thức theo ĐKKD)*.
- **Mã công việc Jira:** `CKPA-41` (`CRM-G0-SUB28` — `[G0][Mục13] Thẩm định Thang 30/25/20/15/10 & Mục 14`)
- **Story cha:** `CKPA-40` (`CRM-G0-ST10` — `[G0][Mục9] Thẩm định G0, Quyết định O1 & Retro`) | **Epic:** `CKPA-3` (`CRM-G0-EP01`)
- **Tiêu chí nghiệm thu Cổng G0:** `G0-AC07`
- **Tham chiếu RFP:** Mục 9 (`Gate G0`), Mục 11 (`Separation of Duties`), Mục 12 (`DEL 01`, `DEL 05`, `DEL 06`), Mục 13 (`Bidder evaluation`: Mandatory controls gate, 7 demo scenarios, 5 criteria `30/25/20/15/10%`, `>= 70/100`), Mục 14 (`7 Decisions before issue and award`)
- **Chủ trì thực hiện (Assignee):** `[P2]` **Trương Đình Hữu Tài** (*Policy owners / Policy Reviewer #1 — Bên mua*)
- **Người báo cáo (Reporter):** `[P1]` **Vắn Mỹ Vân** (*Purchaser sponsor / Product Owner — Bên mua*)
- **Hội đồng phối hợp thẩm định độc lập (RACI — Đúng quy chế SoD):** `[P3]` Trần Chí Kha (*Knowledge & Data Steward / Policy Reviewer #2*), `[P5]` Nguyễn Anh Khoa (*Privacy & Security Owner*), `[S4]` Phạm Quý Hải (*Quality Lead — Independent QA Observer*). *(Thành viên triển khai/điều phối thương mại phía Nhà cung cấp `[S1]`, `[S2]`, `[S3]`, `[S5]` KHÔNG tham gia tự chấm điểm hồ sơ của mình.)*
- **Tệp dữ liệu kèm theo cùng Sub-task:**
  1. `CKPA-41_SUB28_Section13_Scorecard_30_25_20_15_10.csv` (Phiếu chấm điểm 5 tiêu chí tổng đúng `100%`, toàn bộ điểm số đang ở trạng thái `PENDING_DEMO_AND_QUOTE`)
  2. `CKPA-41_SUB28_Section14_7Decisions_G0_Readiness_Checklist.csv` (Bảng đối soát 7 Quyết định Bên mua Mục 14 ánh xạ `G0-AC01..07`)

---

## 1. NGUYÊN TẮC TÁCH BẠCH HAI TẦNG THẨM ĐỊNH: MỤC 13 VS MỤC 14 / MỤC 9

Theo thiết kế quản trị mua sắm của RFP Song Nhật, `[P2]` Trương Đình Hữu Tài thực hiện thẩm định trên **2 tầng hoàn toàn độc lập** để ngăn chặn việc gộp nhầm năng lực kỹ thuật với điều kiện phê duyệt đầu tư:
1. **Tầng 1 — Thẩm định hồ sơ nhà cung cấp & phương án (RFP Mục 13):**
   - Dùng để đánh giá công bằng 3 phương án (**Route 1: Thư viện tìm kiếm đã làm sạch**, **Route 2: Sản phẩm cấu hình sẵn**, **Route 3: Phát triển tùy chỉnh giới hạn**) trên cùng một bộ yêu cầu.
   - **Quy tắc cổng trước khi chấm điểm:** Bắt buộc vượt qua **Cổng Kiểm soát Bắt buộc (`Mandatory Controls Pass/Fail Gate`)** và **trình diễn trực tiếp 7 tình huống chính sách bắt buộc** trước khi tính điểm trọng số `30/25/20/15/10%` (ngưỡng đạt đề xuất `>= 70/100` và `0` cổng trọng yếu thất bại).
   - **Trung lập công nghệ:** Không ưu tiên nhà cung cấp, mô hình ngôn ngữ hay công cụ workflow nào; **tuyệt đối bác bỏ** các buổi demo chatbot đọc tài liệu chung chung thay cho kiểm soát tất định và nghiệm thu độc lập tại địa phương.
2. **Tầng 2 — Đối soát điều kiện sẵn sàng Cổng G0 của Bên mua (RFP Mục 14 & Mục 9):**
   - Dùng để kiểm tra **7 nhóm quyết định nội bộ của Song Nhật** (`Decision 1` Nhu cầu lặp lại → `Decision 7` Mở rộng) ánh xạ vào 7 tiêu chí `G0-AC01..07`.
   - Dù phương án kỹ thuật có đạt điểm cao ở Mục 13, Bên mua vẫn phải giữ trạng thái **`HOLD`** hoặc **`STOP`** nếu thiếu bằng chứng ở Mục 14 (như chưa có báo giá thực tế, chưa khóa vị trí Cloud Host hay chưa xác nhận nhân sự/nguồn dữ liệu).

> [!CAUTION]
> **KẾT LUẬN THẨM ĐỊNH HIỆN TẠI CỦA `[P2]`:**
> - **Điểm chấm Mục 13:** **`PENDING_DEMO_AND_QUOTE`** *(Chưa cấp bất kỳ điểm số định lượng nào do chưa có báo giá thương mại `DEL 05` có đơn giá VND+VAT thực tế từ nhà cung cấp và chưa tổ chức buổi trình diễn trực tiếp 7 tình huống chính sách bắt buộc).*
> - **Mức độ sẵn sàng Mục 14 / Cổng G0:** **`HOLD — CHƯA ĐỦ ĐIỀU KIỆN ĐÓNG CỔNG G0`**, do còn các điều kiện mở được liệt kê rõ tại Mục 3 và tệp `CKPA-41_SUB28_Section14_7Decisions_G0_Readiness_Checklist.csv`.

---

## 2. KHUNG THẨM ĐỊNH MỤC 13: CỔNG BẮT BUỘC, 7 TÌNH HUỐNG DEMO & THANG `30/25/20/15/10%`

### 2.1 Cổng Kiểm soát Bắt buộc (`Mandatory Controls Gate — PASS_REQUIRED_BEFORE_SCORING`)
Bất kỳ phương án hoặc nhà cung cấp nào không đạt một trong các chốt chặn sau sẽ bị loại hoặc giữ `HOLD` ngay trước khi chấm điểm trọng số:
1. Lọc quyền truy cập (`SEC 01`), trạng thái hiệu lực `effective` (`KNW 03`), ngày hiệu lực chi phối (`UTC+7`) và đủ 6 chiều `DAT 04` **nằm hoàn toàn ngoài prompt** (`ANS 01`).
2. Render tất định các trường trọng yếu định kiểu (`DAT 06`, `ANS 04`) gắn điều khoản nguồn, không để LLM suy đoán số học/tiền tệ.
3. Không dùng bộ nhớ mô hình, tìm kiếm web hay ghi chú nhân viên chưa duyệt (`staff_note`) để bịa quy tắc; kích hoạt `HOLD_DAT05` khi hợp đồng khách hàng xung đột chính sách (`DAT 05`).
4. Thu hồi tức thời commit DB trước khi xác nhận và thanh lọc cache `<= 300s` (`SEC 05`, `OPS 05`).
5. Base Scope tuyệt đối `0` hồ sơ khách hàng (`SEC 02`); Tùy chọn `O1` tách biệt hoàn toàn (`DAT 07`).
6. Minh bạch vị trí xử lý/lưu trữ dữ liệu, khóa không huấn luyện/ZDR (`SEC 04`), tách biệt 4 lớp Test/Prod (`SEC 06`) và hỗ trợ xuất dữ liệu mở (`OPS 08`).

### 2.2 Danh mục 7 Tình huống Trình diễn Trực tiếp Bắt buộc (RFP Mục 13 — `RFP-S13-02`)

| STT | Tình huống trình diễn bắt buộc | Yêu cầu kiểm chứng trực tiếp (Không chấp nhận slide/chatbot chung) | Đầu mối chứng kiến | Trạng thái hiện tại |
|:---:|---|---|---|---|
| **DEMO_01** | **Câu trả lời hiện tại & Câu trả lời lịch sử** (`Current & historical answers`) | Cùng 1 câu hỏi tra cứu theo ngày hiện tại (`UTC+7`) và ngày lịch sử trả đúng phiên bản tương ứng kèm trích dẫn nguyên văn và cảnh báo phiên bản cũ (`superseded`). | `[P2]`, `[P3]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_02** | **Chính sách tương lai** (`Future policy — scheduled`) | Chính sách trạng thái `scheduled` có `effective_from` ở tương lai tuyệt đối không được phục vụ làm hướng dẫn hiện hành; chỉ hiển thị dưới cờ xem trước có kiểm soát nếu được hỏi rõ. | `[P2]`, `[P3]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_03** | **Ranh giới ngưỡng chính xác** (`Exact threshold boundary`) | Kiểm tra các giá trị biên (`<= 5%`, `>= 500 triệu VND`, `<= 37 kW` vs `> 37 kW`, `<= 2h` vs `<= 4h`): `100%` khớp toán tử và đơn vị tiền tệ/kỹ thuật ngoài LLM (`OPS 04`). | `[P2]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_04** | **Thiếu điều kiện ngoại lệ / dữ kiện** (`Missing exception`) | Khi thiếu 1 trong 6 chiều `DAT 04` hoặc thiếu dữ kiện ảnh hưởng cấp duyệt, hệ thống trả `CLARIFICATION_REQUIRED` / `HOLD` kèm danh sách dữ kiện thiếu, không tự phỏng đoán phê duyệt (`ANS 05`). | `[P2]`, `[P3]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_05** | **Hợp đồng khách hàng mâu thuẫn chính sách** (`Conflicting contract`) | Khi tồn tại điều khoản riêng trong `customer_contract` (`DOC-006`) khác với `policy` (`DOC-001`), hệ thống bắt buộc chuyển `HOLD_DAT05` về Policy Owner, không tự chọn bên thắng (`DAT 05`). | `[P2]`, `[P5]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_06** | **Người dùng không có quyền** (`Unauthorized user`) | Tài khoản `reader` hoặc sai audience/chi nhánh bị chặn nhất quán trên truy xuất, câu trả lời, URL bằng chứng, cache và nhật ký; `administrator` bị chặn trên `sealed_100` (`SEC 01`). | `[P5]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |
| **DEMO_07** | **Thu hồi chính sách giữa lúc đang sinh câu trả lời** (`Withdrawal during generation`) | Thực thi lệnh thu hồi (`withdrawn`) khi câu trả lời đang sinh hoặc đang nằm trong cache -> chặn hiển thị tức thời trước khi render UI và xóa cache `<= 300s` (`SEC 05`, `OPS 05`). | `[P2]`, `[P5]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` |

### 2.3 Bảng Trọng số 5 Tiêu chí Chấm điểm Mục 13 (Tổng = `100%`, Ngưỡng đạt `>= 70/100`)
*(Chi tiết cấu trúc chấm điểm từng tiêu chí và đầu mối chấm xem tại `CKPA-41_SUB28_Section13_Scorecard_30_25_20_15_10.csv`.)*

| Mã | Tiêu chí đánh giá Mục 13 | Trọng số | Nội dung thẩm định cốt lõi | Chủ chấm (SoD) | Điểm thô (/100) | Điểm trọng số |
|---|---|---:|---|---|:---:|:---:|
| `SEC13_CRIT_01` | **Knowledge and policy fit** *(Phù hợp tri thức & chính sách)* | **`30%`** | Điều khoản áp dụng, ngày hiệu lực, 6 chiều `DAT 04`, `critical_fields`, ngoại lệ & chuyển xử lý trên tác vụ phổ biến | `[P2]`, `[P3]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` | `PENDING_DEMO_AND_QUOTE` |
| `SEC13_CRIT_02` | **Governance and security** *(Quản trị & bảo mật)* | **`25%`** | Thực thi RBAC/SoD, thẩm quyền 5 lớp, vòng đời phát hành, thu hồi tức thời, quyền riêng tư & tuyến nhà cung cấp thực tế | `[P5]`, Legal Owner, `[P2]` | `PENDING_DEMO_AND_QUOTE` | `PENDING_DEMO_AND_QUOTE` |
| `SEC13_CRIT_03` | **Vietnam and feasibility** *(Phù hợp VN & khả thi)* | **`20%`** | Ngôn ngữ tiếng Việt (`VN 01`/`VN 02`), tính khả thi khối lượng Curation & tải công việc Owner, tích hợp CSV & nhân sự định danh | `[P2]`, `[P3]`, `[P4]` | `PENDING_DEMO_AND_QUOTE` | `PENDING_DEMO_AND_QUOTE` |
| `SEC13_CRIT_04` | **Cost and value** *(Chi phí & giá trị)* | **`15%`** | TCO 3 năm đầy đủ VND+VAT (`DEL 05`), tính thực tế công sức/mức dùng, tái sử dụng & so sánh phương án chi phí thấp hơn | `[P1]`, `[P2]` | `PENDING_DEMO_AND_QUOTE` | `PENDING_DEMO_AND_QUOTE` |
| `SEC13_CRIT_05` | **Operation and exit** *(Vận hành & thoát)* | **`10%`** | Bảo trì, giám sát chi phí, khôi phục có Replay (`OPS 07`), hỗ trợ SLA (`DEL 06`), đào tạo & xuất mở không khóa công nghệ (`OPS 08`) | `[P5]`, `[P3]`, `[S4]` | `PENDING_DEMO_AND_QUOTE` | `PENDING_DEMO_AND_QUOTE` |
| **TỔNG** | **Ngưỡng đạt đề xuất: `>= 70/100` & `0` cổng trọng yếu thất bại** | **`100%`** | **Chỉ chấm sau khi vượt Cổng Kiểm soát Bắt buộc, hoàn tất Demo 7 tình huống và nhận báo giá `DEL 05` thật** | **Hội đồng Bên mua + QA `[S4]`** | **`PENDING_DEMO_AND_QUOTE`** | **`PENDING_DEMO_AND_QUOTE`** |

---

## 3. ĐỐI SOÁT 7 QUYẾT ĐỊNH SẴN SÀNG CỔNG G0 THEO MỤC 14 RFP

*(Chi tiết ánh xạ bằng chứng và điều kiện mở từng quyết định xem tại `CKPA-41_SUB28_Section14_7Decisions_G0_Readiness_Checklist.csv`.)*

1. **Decision 1 — Recurring need (`G0-AC01`):** Đã có danh mục 4 tuần lịch sử không rò rỉ (`520` lượt, `200` tác vụ) & bảng kiểm kê phần mềm (`CKPA-06`), hồ sơ ngôn ngữ `VN 01` (`CKPA-22`) và báo cáo Baseline sơ bộ (`15,53` phút, `CKPA-07`). **Trạng thái: `IN_REVIEW`** — còn mở: nộp raw stopwatch logs, định danh `4/5` Representative Staff Users (`RSU-02..05`) và kế hoạch `VER-000`.
2. **Decision 2 — Source readiness & O1 separate rights/value (`G0-AC02`, `G0-AC03`):** Đã có 3 họ chính sách, 5 lớp thẩm quyền, Sổ nguồn có cột quyền (`CKPA-15`/`25`), bộ mẫu 30+10 đủ 6 chiều `DAT 04` & kiểm tra SHA-256 (`CKPA-25`/`26`), và kế hoạch Curation (`CKPA-27`). **Trạng thái: `PENDING_OWNER_SIGNOFF`** — còn mở: `[P2]`/`[P1]` ký duyệt mẫu 30+10 & định danh Người thay thế (`VN 04`), bổ sung đơn giá VND dòng `L02` Curation vào kế hoạch ngân sách; giữ O1 tách biệt.
3. **Decision 3 — Policy controls ownership (`G0-AC02`, `G0-AC04`):** Đã hoàn tất 6 chiều `DAT 04` (`CKPA-10`), đặc tả `DAT 02` (`CKPA-14`), kiến trúc Selection ngoài prompt (`CKPA-21`) và 9 hợp đồng Annex B (`CKPA-29`). **Trạng thái: `IN_REVIEW`** — còn mở: ký phê duyệt chính thức của `[P2]`/`[P3]`/`[P1]` và đồng bộ cờ sửa lỗi mã nguồn G1.
4. **Decision 4 — Deployment governance (`G0-AC05`, `G0-AC07`):** Đã chuẩn hóa RBAC 20-User & khóa `sealed_100` (`CKPA-17`), hồ sơ pháp lý Annex F & lịch lưu giữ Annex C (`CKPA-19`/`34`), và điều khoản vận hành `DEL 06` (`CKPA-18`/`33`). **Trạng thái: `PENDING_OWNER_SIGNOFF`** — còn mở: chốt duy nhất 1 Cloud Host/DC (`PENDING_G0_SELECTION`), thẩm định pháp luật hiện hành của Legal/Records Owner và sửa `backend/src/shared/auth.py:65-72` tại G1.
5. **Decision 5 — Acceptance before build (`G0-AC04`, `G0-AC06`):** Đã hoàn tất kế hoạch độc lập 280 ca không rò rỉ 16-VG + quy chế `sealed-eval-repo` (`CKPA-30`), giao thức đo 20 ngày (`CKPA-31`) và rà soát tính khả kiểm (`CKPA-35`). **Trạng thái: `IN_REVIEW`** — còn mở: `[P2]`/`[P3]` hoàn tất gắn nhãn đối chiếu kép `PENDING_DUAL_REVIEW_P2_P3` trên `dev_60` và `[P1]`/`[P4]` ký giao thức 20 ngày.
6. **Decision 6 — Investment ceiling, route comparison & stop conditions (`G0-AC07`):** Đã có khung so sánh 3 phương án (`CKPA-37`), bóc tách khối lượng Base vs O1 (`CKPA-38`) và khung TCO 3 năm `DEL 05` + Annex E (`CKPA-39`). **Trạng thái: `BLOCKED_PENDING_QUOTE`** — **CHẶN CỔNG**: chưa có đơn giá VND+VAT thực tế trên 14 dòng `DEL 05`, chưa chấm Mục 13 sau Demo 7 tình huống, và chưa xác nhận trần đầu tư của `[P1]`.
7. **Decision 7 — Expansion (`O` — Post-G3 Separate):** Tùy chọn `O1` và mọi mở rộng kênh/tích hợp/ghi ngược CRM đều bị khóa ngoài Base Scope (`OFF`). **Trạng thái: `DEFERRED_SEPARATE_OPTION`** — tuân thủ hoàn toàn ranh giới RFP Mục 1 & Mục 14.

---

## 4. KHUNG XÁC NHẬN THẨM ĐỊNH ĐỘC LẬP (`CKPA-41`)

| Vai trò trong Hội đồng thẩm định (SoD) | Họ và tên | Nội dung xác nhận | Trạng thái ký duyệt |
|---|---|---|:---:|
| **`[P2]` Policy owners** *(Chủ trì thẩm định Mục 13/14)* | **Trương Đình Hữu Tài** | Xác nhận khung chấm điểm Mục 13, 7 tình huống Demo & bảng đối soát 7 Quyết định Mục 14 (kiến nghị `HOLD` tới khi đủ báo giá & Demo) | `[x] Đã ký xác nhận (20/11/2026)` |
| **`[P3]` Knowledge and data steward** *(Policy Reviewer #2)* | **Trần Chí Kha** | Xác nhận thẩm định tính sẵn sàng nguồn, 6 chiều `DAT 04` & khả thi Curation (Tiêu chí 1 & 3) | `[x] Đã ký xác nhận (20/11/2026)` |
| **`[P5]` Privacy and security owners** | **Nguyễn Anh Khoa** | Xác nhận thẩm định quản trị, bảo mật, pháp lý Annex F & vận hành thoát (Tiêu chí 2 & 5) | `[x] Đã ký xác nhận (20/11/2026)` |
| **`[S4]` Quality lead** *(Independent QA Observer)* | **Phạm Quý Hải** | Xác nhận tính khách quan của 7 kịch bản Demo, cổng kiểm soát bắt buộc & không có lỗi trọng yếu | `[x] Đã ký xác nhận (20/11/2026)` |
| **`[P1]` Purchaser sponsor / Product Owner** *(Reporter)* | **Vắn Mỹ Vân** | Tiếp nhận báo cáo thẩm định để chủ trì Hội đồng Quyết định Cổng G0 (`CKPA-42`) | `[x] Đã ký xác nhận (20/11/2026)` |
