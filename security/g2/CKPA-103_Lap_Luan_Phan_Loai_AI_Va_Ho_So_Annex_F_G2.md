# VĂN BẢN LẬP LUẬN PHÂN LOẠI AI CÓ NGÀY, MA TRẬN TRÁCH NHIỆM & HỒ SƠ FILING / CONFORMITY (ANNEX F)

- **Mã công việc Jira:** `CKPA-103` (Parent Epic Gate G2: `CKPA-85` | Kế thừa từ G0: `CKPA-17`, `CKPA-34`)
- **Mã truy vết RFP & Tiêu chí G2:** `SEC 03`, `Annex F` (`R04`, `R10`, `R11`, *applicable filing or conformity evidence*), `VN 05` | Tiêu chí nghiệm thu: **`G2-AC07`**
- **Nhánh Git thực hiện:** `sec/CKPA-103-dated-ai-classification-annexf`
- **Vị trí tệp chuẩn:** `security/g2/CKPA-103_Lap_Luan_Phan_Loai_AI_Va_Ho_So_Annex_F_G2.md`
- **Đơn vị chủ quản (Bên mua / AI Deployer):** Công ty Cổ phần Thiết bị Công nghiệp Song Nhật (`SongNhat SCRM`)
- **Chủ trì thực hiện:** `[P5]` Nguyễn Anh Khoa (Privacy & Security Owner)
- **Phối hợp & Thẩm định RACI:** `[S1]` Hoàng Tiến (Supplier Lead), `[P1]` Vắn Mỹ Vân (Purchaser Sponsor / PO), `[P2]` Trương Đình Hữu Tài (Policy Owner)
- **Ngày lập & đối chiếu pháp lý:** `2026-11-27` (Phiên bản `v2.0 — Gate G2`)
- **Lưu ý phạm vi đồ án:** Hồ sơ phục vụ thẩm định tuân thủ Gate G2 của dự án *SongNhat CRM Knowledge and Policy Assistant* trên dữ liệu giả lập; không thay thế ý kiến tư vấn pháp lý độc lập ngoài phạm vi đồ án.

---

## 1. Bối cảnh Hệ thống & Phạm vi Thẩm định tại Gate G2

Căn cứ hồ sơ kiến trúc đã chốt từ Gate G0–G1 (`security/g0/P1_HoSoPhapLy_CoNgay_v1_HoanChinh.md`, `CKPA-40`, `CKPA-42`) và cấu hình triển khai thực tế tại Gate G2:

1. **Mục đích vận hành:** Hệ thống **CRM Knowledge and Policy Assistant** là công cụ hỗ trợ tra cứu nội bộ có trích dẫn dành cho tối đa **20 nhân viên có tên** (tối đa **5 phiên đồng thời**) của Song Nhật về 3 nhóm quy trình đã được phê duyệt: *(i) Báo giá & phê duyệt thương mại*, *(ii) Xử lý thông tin khách hàng*, và *(iii) Tiếp nhận & xử lý bảo hành*.
2. **Giới hạn chức năng (Non-Autonomous Guardrails):**
   - Chỉ giải thích quy trình, nhận diện phiên bản chính sách hiệu lực (`effective`) và trả về trích dẫn nguyên văn kèm nguồn (`passage` / `document_lineage`).
   - **Không tự động ra quyết định đối với khách hàng:** Không tự phê duyệt giao dịch thương mại, không tự quyết định quyền hưởng bảo hành hoặc chiết khấu, không cấp ngoại lệ, không đưa ý kiến tư vấn pháp lý/thuế và không hướng dẫn sửa chữa kỹ thuật thiết bị (`ANS 07`).
   - **Kiểm soát tất định (Deterministic Policy Core):** Toàn bộ 40 trường trọng yếu (*critical fields*), ngưỡng phê duyệt số học và phân quyền RBAC (`reader`, `policy_owner`, `steward`, `administrator`) được xử lý cứng tại tầng mã nguồn backend, không giao cho mô hình ngôn ngữ lớn (LLM) tự suy diễn.
   - **Loại trừ dữ liệu khách hàng thật (Base Scope):** Option O1 (kết nối ngữ cảnh hồ sơ CRM khách hàng thật) đã bị cắt hoàn toàn khỏi codebase theo quyết định `CKPA-40` / `CKPA-42`; lớp lọc `pii_guard.py` và quy chế nội bộ ngăn chặn nhập số CCCD, tài khoản ngân hàng hoặc hồ sơ định danh cá nhân vào luồng hỏi đáp.

---

## 2. Lập luận Phân loại Hệ thống AI Có Ngày (*Dated AI Classification Rationale* — `R04`, `R10`, `R11`)

### 2.1. Thông tin định danh bản phân loại
- **Ngày thực hiện phân loại & ký xác nhận G2:** `2026-11-27`
- **Căn cứ văn bản pháp quy đối chiếu (hiệu lực hiện hành tại thời điểm đánh giá):**
  - **`R04` — Luật Trí tuệ nhân tạo số `134/2025/QH15`** (Quốc hội ban hành, có hiệu lực từ ngày `01/03/2026`).
  - **`R10` — Nghị định số `142/2026/NĐ-CP`** (Chính phủ quy định chi tiết thi hành một số điều của Luật Trí tuệ nhân tạo, có hiệu lực từ ngày `01/05/2026`).
  - **`R11` — Quyết định số `33/2026/QĐ-TTg`** (Thủ tướng Chính phủ ban hành Danh mục hệ thống trí tuệ nhân tạo có rủi ro cao).
  - **`VN 05` & `Annex F`** (Yêu cầu tuân thủ pháp luật Việt Nam về AI, bảo vệ dữ liệu cá nhân và nghĩa vụ hồ sơ/đánh giá hợp chuẩn của RFP).

### 2.2. Kết quả đối chiếu tiêu chí phân loại mức độ rủi ro

| Tiêu chí thẩm định (`R04`, `R10`, `R11`) | Đặc tính kỹ thuật & vận hành của SongNhat CKPA | Kết quả đối chiếu |
| :--- | :--- | :--- |
| **1. Đối chiếu Danh mục Hệ thống AI có rủi ro cao (`R11` — QĐ `33/2026/QĐ-TTg`)** | Hệ thống chỉ phục vụ tra cứu quy trình nội bộ cho nhân viên; **không** thuộc các lĩnh vực hạ tầng thiết yếu quốc gia, y tế, giáo dục, tuyển dụng/đánh giá tín dụng tự động, chấm điểm công dân hay ra quyết định hành chính/pháp lý ảnh hưởng trực tiếp đến quyền và lợi ích hợp pháp của cá nhân. | **Không thuộc danh mục AI rủi ro cao (`Not High-Risk`)** |
| **2. Mức độ tự chủ & Tác động pháp lý (`R04` — Luật AI `134/2025/QH15`)** | Đầu ra chỉ mang tính tham chiếu nội bộ kèm trích dẫn; mọi hành động nghiệp vụ (lập báo giá, duyệt chiết khấu, tiếp nhận bảo hành) đều do nhân viên có thẩm quyền thực hiện thủ công trên hệ thống CRM sau khi đối chiếu văn bản gốc (*Human-in-the-loop* bắt buộc). | **Rủi ro thấp / trung bình (`Low / Limited Risk` — Trợ lý hỗ trợ tra cứu nội bộ)** |
| **3. Tính chất mô hình AI sử dụng (`R04`, `R10`)** | Hệ thống sử dụng mô hình ngôn ngữ nền tảng thương mại sẵn có (`gpt-4o` cho sinh văn bản trích dẫn và `text-embedding-3-small` cho lập chỉ mục vector) qua API với cấu hình *Zero Data Retention (ZDR)*; **không** huấn luyện mới, **không** tinh chỉnh (*fine-tune*) mô hình nền tảng trên dữ liệu cá nhân. | **Hệ thống AI ứng dụng chuyên biệt tích hợp mô hình nền tảng qua API** |
| **4. Nghĩa vụ minh bạch tương tác (`R04`, `R10`, `VN 05`)** | Giao diện và tài liệu hướng dẫn người dùng nội bộ thông báo rõ ràng đây là trợ lý AI tra cứu chính sách, hiển thị trích dẫn nguồn và cảnh báo kiểm tra lại điều khoản gốc trước khi áp dụng cho khách hàng. | **Áp dụng nghĩa vụ minh bạch & giám sát con người (`Applicable`)** |

### 2.3. Kết luận phân loại chính thức tại Gate G2 & Điều kiện tái phân loại
- **Kết luận phân loại có ngày (`2026-11-27`):** Hệ thống *SongNhat CRM Knowledge and Policy Assistant* (trong giới hạn Base Scope của Gate G2) được phân loại là **Hệ thống AI không thuộc danh mục rủi ro cao (Nhóm rủi ro thấp / trung bình — công cụ hỗ trợ tra cứu tri thức nội bộ có giám sát của con người)** theo Luật AI `134/2025/QH15` (`R04`), Nghị định `142/2026/NĐ-CP` (`R10`) và Quyết định `33/2026/QĐ-TTg` (`R11`).
- **Điều kiện kích hoạt đánh giá phân loại lại (*Re-classification Triggers*):** Phân loại này chỉ có hiệu lực đối với phạm vi hiện tại. Bất kỳ thay đổi nào sau đây đều **bắt buộc dừng triển khai và lập hồ sơ tái phân loại rủi ro** trước khi đưa vào vận hành:
  1. Kích hoạt **Option O1** (nạp hồ sơ khách hàng thật từ CRM vào ngữ cảnh truy vấn) hoặc mở rộng đối tượng sử dụng trực tiếp ra khách hàng bên ngoài.
  2. Chuyển đổi chức năng từ *gợi ý tra cứu* sang *tự động phê duyệt* báo giá, chiết khấu, điều kiện bảo hành hoặc từ chối quyền lợi khách hàng mà không có bước phê duyệt độc lập của con người.
  3. Thay đổi nhà cung cấp mô hình AI nền tảng (`SEC 08`) hoặc tự huấn luyện/fine-tune mô hình riêng trên dữ liệu vận hành thực tế.

---

## 3. Ma trận Phân định Trách nhiệm 3 Bên (*Responsibility Matrix* — `R04`, `R10`, `R11`, `VN 05`)

Căn cứ cấu trúc vai trò tại Gate G0 (`CKPA-17`, `CKPA-34`) và trách nhiệm vận hành thực tế tại Gate G2, nghĩa vụ tuân thủ theo Luật AI `134/2025/QH15` (`R04`), Nghị định `142/2026/NĐ-CP` (`R10`) và Quyết định `33/2026/QĐ-TTg` (`R11`) được phân định rõ ràng giữa 3 chủ thể như sau:

| Hạng mục nghĩa vụ tuân thủ (`R04`, `R10`, `R11`, `VN 05`) | Bên mua / Bên triển khai AI<br>**Song Nhật** (`[P1]–[P5]`) | Nhà cung cấp / Bên phát triển hệ thống<br>**Supplier Team** (`[S1]–[S5]`) | Nhà cung cấp mô hình AI nền tảng<br>**OpenAI / Azure OpenAI** *(Dự phòng: GCP Vertex AI)* |
| :--- | :--- | :--- | :--- |
| **1. Vai trò pháp lý theo Luật AI `134/2025/QH15` (`R04`)** | **Bên triển khai / Người sử dụng hệ thống AI** (*AI Deployer*) | **Nhà cung cấp / Bên phát triển hệ thống AI ứng dụng** (*AI System Provider / Integrator*) | **Nhà cung cấp mô hình AI nền tảng** (*Foundation Model Provider* — cung cấp API `gpt-4o`, `text-embedding-3-small`) |
| **2. Xác định phạm vi sử dụng & Phân loại rủi ro có ngày (`R04`, `R11`)** | **Chịu trách nhiệm chính (Accountable / Responsible):** Xác nhận mục đích sử dụng nội bộ, ký duyệt văn bản phân loại AI có ngày và kiểm soát không vượt phạm vi Base Scope. | **Phối hợp cung cấp thông số kỹ thuật (Consulted):** Cung cấp kiến trúc RAG, luồng dữ liệu và giới hạn hành vi của hệ thống để đối chiếu danh mục `R11`. | **Không áp dụng trực tiếp cho ứng dụng:** Công bố tài liệu kỹ thuật (*Model Card / System Card*) và giới hạn an toàn của mô hình nền tảng. |
| **3. Kiểm soát chất lượng tri thức & Tính xác thực nguồn trích dẫn (`R04`, `R10`)** | **Chịu trách nhiệm chính (`[P2]`, `[P3]`):** Phê duyệt văn bản chính sách chuẩn (`Corpus`), quản lý trạng thái hiệu lực (`effective` / `withdrawn`) và rà soát 40 critical fields. | **Thực thi kỹ thuật (`[S2]`, `[S3]`):** Đảm bảo cơ chế truy xuất đúng phiên bản hiệu lực, chặn tài liệu `DRAFT`/`SCHEDULED`/`WITHDRAWN` (`CKPA-70`) và ép buộc trả lời kèm trích dẫn. | **Hỗ trợ năng lực suy luận:** Tuân thủ chỉ dẫn hệ thống (*system prompt*) dựa trên ngữ cảnh được cấp, không tự bịa nguồn ngoài ngữ cảnh. |
| **4. Giám sát con người (*Human-in-the-loop*) & Đào tạo người dùng (`R04`, `R10`)** | **Chịu trách nhiệm chính (`[P1]`, `[P4]`):** Ban hành quy chế nội bộ bắt buộc 20 nhân viên định danh kiểm tra trích dẫn gốc trước khi thao tác CRM; thực hiện UAT (`CKPA-109`). | **Thiết kế giao diện hỗ trợ (`[S1]`, `[S3]`):** Hiển thị rõ thông báo miễn trừ trách nhiệm AI, mã tài liệu, đoạn trích dẫn và luồng chuyển tiếp xử lý ngoại lệ (*referral*). | **Không áp dụng:** Không trực tiếp quản lý quy trình nghiệp vụ của người dùng cuối tại doanh nghiệp. |
| **5. Minh bạch AI & Cấm huấn luyện trái phép trên dữ liệu (`R04`, `R10`, `VN 05`)** | **Giám sát tuân thủ (`[P5]`):** Yêu cầu điều khoản hợp đồng *Zero Data Retention (ZDR)*, cấm sử dụng prompt/dữ liệu Song Nhật để huấn luyện mô hình; thông báo minh bạch cho nhân viên. | **Cấu hình kỹ thuật (`[S5]`):** Thiết lập endpoint Enterprise API tắt lưu trữ/huấn luyện dữ liệu; triển khai bộ lọc `pii_guard.py` trước khi gửi request ra API ngoài. | **Cam kết dịch vụ Enterprise:** Xử lý inference/embedding tức thời trong bộ nhớ (*in-memory*), không lưu giữ prompt/completion trên đĩa và không dùng dữ liệu khách hàng để huấn luyện lại mô hình. |
| **6. Ghi nhật ký vận hành, Quản lý thay đổi & Ứng phó sự cố (`SEC 06`–`SEC 08`, `R10`)** | **Giám sát & Nghiệm thu (`[P1]`, `[P5]`):** Lưu trữ `audit_logs` nội bộ tại Việt Nam (12 tháng), thẩm định lại rủi ro khi đổi model/prompt (`SEC 08`) và tiếp nhận báo cáo sự cố trong `<= 4 giờ` (`SEC 07`). | **Vận hành & Xử lý kỹ thuật (`[S5]`):** Duy trì cơ chế ghi log đầy đủ, cơ chế tắt khẩn cấp (*kill-switch* / *rollback*), thông báo sự cố trong `<= 4 giờ` và không tự ý đổi provider/model khi chưa được duyệt. | **Cam kết SLA hạ tầng API:** Đảm bảo tính sẵn sàng, mã hóa đường truyền HTTPS/TLS và thông báo sự cố bảo mật nền tảng theo cam kết dịch vụ. |

---

## 4. Hồ sơ Bằng chứng Nộp hồ sơ / Đánh giá Hợp chuẩn (*Applicable Filing or Conformity Evidence — Annex F*)

Theo quy định của **Luật AI `134/2025/QH15` (`R04`)**, **Nghị định `142/2026/NĐ-CP` (`R10`)**, **Quyết định `33/2026/QĐ-TTg` (`R11`)** và **Phụ lục F (`Annex F`)** của RFP, nghĩa vụ nộp hồ sơ đăng ký hoặc đánh giá sự phù hợp (*filing / conformity assessment*) được phân loại thành hai nhóm: **Nghĩa vụ đặc thù cho AI rủi ro cao (Miễn áp dụng)** và **Nghĩa vụ tuân thủ chung đối với hệ thống AI triển khai nội bộ (Áp dụng bắt buộc)**.

### 4.1. Bảng tổng hợp trạng thái áp dụng & bằng chứng kiểm chứng (`Annex F`)

| Mã nghĩa vụ (`Annex F`) | Nội dung yêu cầu pháp lý (`R04`, `R10`, `R11`) | Trạng thái áp dụng tại Gate G2 | Lập luận & Bằng chứng đối chiếu trong Repo Purchaser |
| :--- | :--- | :--- | :--- |
| **`AF-01`** | **Nộp hồ sơ đăng ký / công bố đánh giá sự phù hợp bắt buộc dành cho Hệ thống AI có rủi ro cao** trước khi đưa vào lưu thông hoặc sử dụng. | **Không áp dụng (`Not Applicable — Exempt`)** | Theo Mục 2 văn bản này, hệ thống chỉ hỗ trợ tra cứu quy trình nội bộ có giám sát con người và **không thuộc Danh mục hệ thống AI có rủi ro cao** ban hành kèm Quyết định `33/2026/QĐ-TTg` (`R11`). Do đó, không phát sinh nghĩa vụ nộp hồ sơ thẩm định tiền kiểm hoặc chứng nhận hợp chuẩn dành riêng cho AI rủi ro cao. Bằng chứng lưu trữ chính là **Văn bản phân loại AI có ngày (`CKPA-103`)** này để xuất trình khi hậu kiểm. |
| **`AF-02`** | **Hồ sơ xác định phân loại rủi ro AI có ngày & cơ chế kiểm soát giới hạn phạm vi** (*Dated AI Classification & Scope Guardrails*). | **Áp dụng bắt buộc (`Applicable — Verified`)** | - `security/g0/P1_HoSoPhapLy_CoNgay_v1_HoanChinh.md` (Bản phân loại nền tảng G0 ngày `17/11/2026`).<br>- `security/g2/CKPA-103_Lap_Luan_Phan_Loai_AI_Va_Ho_So_Annex_F_G2.md` (Bản thẩm định chính thức Gate G2 ngày `2026-11-27`).<br>- Quyết định cắt bỏ Option O1 (`CKPA-40` / `CKPA-42`) đảm bảo không xử lý dữ liệu khách hàng thật. |
| **`AF-03`** | **Bằng chứng minh bạch hệ thống AI & Giám sát của con người** (*Transparency Notice & Human-in-the-loop Governance*). | **Áp dụng bắt buộc (`Applicable — Verified`)** | - `data/g0/passages.csv` (`PAS-019` — Quy định tối thiểu hóa dữ liệu và nguyên tắc tra cứu nội bộ).<br>- `uat/g2/ckpa-109/ckpa-109-5-rep-users-and-uat-fallback-scenario.md` & `20_named_users_and_5_rep_users_matrix.csv` (Danh sách 20 người dùng định danh và kịch bản UAT kiểm tra tính hữu ích & trích dẫn nguồn dưới sự giám sát của con người). |
| **`AF-04`** | **Bằng chứng kiểm soát dữ liệu đầu vào, ẩn danh PII & tách biệt quyền truy cập** (*Data Governance, 0% PII & RBAC Fail-Closed*). | **Áp dụng bắt buộc (`Applicable — Verified`)** | - `security/g1/CKPA-47_Chung_Nhan_Du_Lieu_Kiem_Thu_0_PII_G1.md` & `g1_pii_audit_CKPA-47.log` (Xác nhận 0% PII trong kho dữ liệu kiểm thử).<br>- `security/g1/CKPA-70_Bao_Cao_Kiem_Toan_Lo_Lot_RBAC_Cache_FailClosed_G1.md` & `g1_rbac_failclosed_audit_CKPA-70.log` (Xác nhận khóa chặt tài liệu `DRAFT`/`SCHEDULED`/`WITHDRAWN` trên corpus và logic backend). |
| **`AF-05`** | **Bằng chứng cam kết nhà cung cấp mô hình nền tảng & Lưu vết vận hành** (*Subprocessor ZDR, Audit Logs & Change Control*). | **Áp dụng bắt buộc (`Applicable — Verified with G2 Operational Controls`)** | - Điều khoản cấu hình Enterprise API *Zero Data Retention (ZDR)*, không huấn luyện lại mô hình của OpenAI / Azure OpenAI (dự phòng Vertex AI Singapore) và lưu trữ `audit_logs` 100% nội bộ tại Việt Nam (`security/g0/P1_HoSoPhapLy_CoNgay_v1_HoanChinh.md`, Mục 5).<br>- Cơ chế quản lý thay đổi provider/model/prompt (`SEC 08`) và ứng phó sự cố `<= 4 giờ` (`SEC 07`). |

### 4.2. Xác nhận nghiệm thu tiêu chí `G2-AC07`
- **Trạng thái hoàn thành:** **ĐẠT (`PASS` — Sẵn sàng nghiệm thu Gate G2 cho thẻ `CKPA-103`)**.
- **Hành động duy trì tuân thủ:** Tệp này được lưu trữ cố định tại nhánh `develop` của repository Purchaser (`security/g2/CKPA-103_Lap_Luan_Phan_Loai_AI_Va_Ho_So_Annex_F_G2.md`) làm bằng chứng đối soát cho Hội đồng nghiệm thu Gate G2 (`CKPA-85`) và mọi đợt rà soát thay đổi mô hình/phạm vi (`SEC 08`) về sau.
