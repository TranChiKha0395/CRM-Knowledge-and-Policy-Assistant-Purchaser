Hồ sơ phân loại và pháp lý có ngày

Đồ án RFP SongNhat CRM Knowledge and Policy Assistant. Hoàn thành trước G2. Dữ liệu giả lập. Đây là hồ sơ học tập, không phải ý kiến pháp lý.

Ngày lập: 17/11/2026

Người lập: [P5] Nguyễn Anh Khoa (Privacy & Security Owner) & [P1] Văn Mỹ Vân (Purchaser Sponsor / PO)

Phiên bản: v1

Mục ghi 'Chờ S5' do S5 cung cấp. Mục để trống do P1 điền sau khi đọc văn bản gốc (xem P1_GhiChu_AnnexF). Điều chưa chắc ghi vào mục 8, không tự kết luận.

1. Tóm tắt hệ thống

Mục đích: cung cấp hướng dẫn nội bộ có trích dẫn cho nhân viên có thẩm quyền về các quy trình quan hệ khách hàng (CRM) đã được duyệt: quy trình báo giá và phê duyệt thương mại, xử lý thông tin khách hàng, tiếp nhận bảo hành. Trợ lý nhận diện chính sách và phiên bản áp dụng, giải thích thông tin cần có và tuyến phê duyệt, kèm trích dẫn chính xác (RFP, phần mở đầu).

Phạm vi cơ bản: không nhập hồ sơ khách hàng. Người dùng: 20 người có tên, 5 phiên đồng thời. Tri thức tối đa 30 tài liệu, 300 đoạn, 50 dòng critical field. Trợ lý giải thích quy trình; không phê duyệt giao dịch, không đưa ý kiến pháp lý hoặc thuế, không quyết định quyền hưởng, không cam kết với khách, không hướng dẫn sửa chữa thiết bị (ANS 07).

Option O1 (ngữ cảnh CRM): Không mua O1 ở mốc G0 (cắt hoàn toàn khỏi codebase & sprint hiện tại theo quyết định CKPA-40 / CKPA-42 (CRM-G0-ST10 / CRM-G0-SUB29) / Biên bản G0).

2. Phân loại hệ thống AI (CKPA-17)

| Mục | Nội dung |
| --- | --- |
| Mục đích sử dụng và đối tượng dùng | Hướng dẫn nội bộ cho nhân viên có thẩm quyền; không tự động ra quyết định. |
| Văn bản đối chiếu | Luật AI 134/2025/QH15 (hiệu lực 01/03/2026); Nghị định 142/2026/NĐ-CP (hiệu lực 01/05/2026); QĐ 33/2026/QĐ-TTg (danh mục rủi ro cao). Kiểm tra phiên bản hiện hành. |
| Đối chiếu danh mục rủi ro cao | Không thuộc danh mục AI rủi ro cao: Hệ thống chỉ tra cứu và giải thích quy trình nội bộ (báo giá, thông tin khách hàng, bảo hành); không tự động phê duyệt giao dịch, không quyết định quyền hưởng bảo hành, không cấp ngoại lệ thương mại và không tiết lộ dữ liệu khách hàng (cần đối chiếu lại toàn văn QĐ 33/2026/QĐ-TTg với Legal Owner trước Gate G2 - CKPA-34). |
| Kết luận phân loại tạm | Hệ thống AI rủi ro thấp / trung bình (Đề xuất phân loại tạm G0 — Chờ Legal Owner SongNhat chính thức ký duyệt phân loại tại Gate G2 - CKPA-34). |
| Lập luận | (1) Chỉ đóng vai trò công cụ hỗ trợ tra cứu nội bộ; (2) Toàn bộ 10 critical fields, ngưỡng số học và vai trò duyệt được xử lý cứng ở code backend (Deterministic), AI không tự suy diễn; (3) Bắt buộc giám sát con người (Human-in-the-loop): nhân viên phải đối chiếu trích dẫn gốc trước khi thao tác trên CRM. |
| Ngày đối chiếu và điều kiện thay đổi phân loại | Ngày đối chiếu: 17/11/2026. Điều kiện thay đổi phân loại: Nếu mở rộng sang tự động phê duyệt giao dịch, tự động quyết định quyền lợi khách hàng hoặc kích hoạt Option O1 (dữ liệu khách hàng thật), phải đánh giá lại phân loại rủi ro trước khi triển khai. |

RFP: dùng nội bộ hoặc có người xem xét lại không tự động tạo miễn trừ. Quyết định tự động về tư cách hưởng, tiết lộ dữ liệu hoặc giao dịch cần phạm vi và đánh giá mới.

3. Bảng vai trò theo ba luật (79, 80)

| Bên | Luật BVDLCN (91/2025/QH15; NĐ 356/2025/NĐ-CP) | Luật AI (134/2025/QH15; NĐ 142/2026/NĐ-CP) | Luật An ninh mạng (116/2025/QH15) |
| --- | --- | --- | --- |
| SongNhat (bên mua, đơn vị sử dụng) | Bên kiểm soát dữ liệu cá nhân (Data Controller) | Bên triển khai / người sử dụng hệ thống AI (AI Deployer) | Chủ quản hệ thống thông tin (nội bộ doanh nghiệp) |
| Supplier (nhóm S1–S5) | Bên xử lý dữ liệu cá nhân (Data Processor — Supplier Team S1–S5: Trưởng nhóm [S1] Hoàng Tiến, Vận hành [S5] Nguyễn Ngọc Duy) | Nhà cung cấp / Bên phát triển hệ thống AI (AI Provider) | Đơn vị cung cấp dịch vụ, vận hành kỹ thuật an toàn thông tin |
| Nhà cung cấp mô hình / hạ tầng (Chờ S5) | Bên xử lý phụ (Subprocessor — OpenAI / Azure OpenAI tại Đông Á/Đông Nam Á; phương án dự phòng Google Cloud Vertex AI Singapore — đồng bộ cấu hình .env / CKPA-34 / CKPA-17 (CRM-G0-SUB23 / CRM-G0-SUB10)) | Bên cung cấp mô hình AI nền tảng (LLM gpt-4o & Embedding text-embedding-3-small) | Nhà cung cấp dịch vụ API mô hình ngôn ngữ (Zero Data Retention) |
| Subprocessor khác (Chờ S5) | Không áp dụng bên thứ ba lưu trữ ngoài (Toàn bộ PostgreSQL/pgvector, Redis Cache, Audit Logs và Backup vận hành trên hạ tầng Local VM nội bộ tại Việt Nam — nguồn CKPA-34 / CKPA-17 (CRM-G0-SUB23 / CRM-G0-SUB10)) | Không áp dụng (Cơ sở dữ liệu nội bộ) | Hạ tầng máy chủ nội bộ SongNhat tại Việt Nam |

Điền tên vai trò đúng thuật ngữ trong văn bản gốc. Không đoán.

4. Xử lý dữ liệu (SEC 03)

| Hoạt động xử lý | Mục đích | Cơ sở pháp lý | Thông báo | Quyền chủ thể | Đánh giá cần có | Chuyển dữ liệu |
| --- | --- | --- | --- | --- | --- | --- |
| Câu hỏi của nhân viên (có thể lẫn dữ liệu cá nhân) | Tra cứu quy trình CRM nội bộ | Thực hiện hợp đồng lao động / nội quy nội bộ; bộ lọc pii_guard.py (mục tiêu G1–G2) chặn PII khách hàng | Thông báo quy chế dùng AI nội bộ & cấm nhập PII khách hàng trước G2 | Quyền được biết, truy cập, chỉnh sửa/xóa dữ liệu của nhân viên | Đánh giá tác động xử lý DLCN (DPIA) tại Gate G2 (CKPA-34) | Truyền prompt đã lọc PII qua HTTPS tới LLM API (Đông Á/Đông Nam Á) — thẩm định chuyển DLCN ra nước ngoài tại G2 |
| Văn bản chính sách và ví dụ | Làm kho tri thức chuẩn (Corpus) phục vụ tra cứu | Quyền quản trị nội bộ của SongNhat; dùng dữ liệu giả lập giai đoạn Pilot | Công bố nội bộ cho 20 người dùng định danh | Ẩn danh toàn bộ thông tin cá nhân thật trong ví dụ minh họa | Kiểm tra quyền sở hữu nguồn và tính hợp pháp (DAT 03) | Lưu trữ nội bộ tại Việt Nam (PostgreSQL/pgvector); gửi text tính vector qua Embedding API (in-memory) |
| Nhật ký, audit, phản hồi, referral | Giám sát an toàn, đối soát chất lượng, khiếu nại và referral | Nghĩa vụ bảo đảm an toàn hệ thống và quản trị nội bộ (đề xuất tối đa 12 tháng) | Thông báo cơ chế ghi log hoạt động cho 20 tài khoản nhân viên | Nhân viên có quyền tra soát và phản hồi chỉnh sửa nội dung liên quan | Đánh giá tuân thủ retention (Annex C) và bảo mật log (SEC 06) | Lưu trữ 100% nội bộ tại Việt Nam (bảng audit_logs) |
| Ngữ cảnh CRM (chỉ nếu mua O1) | Không áp dụng ở Base Scope (Đã cắt khỏi codebase tại CKPA-40 / CKPA-42 (CRM-G0-ST10 / CRM-G0-SUB29)) | Chỉ bật sau G3 nếu có đồng ý hoặc thực hiện hợp đồng với khách hàng | Thông báo chính sách quyền riêng tư cho khách hàng trước khi dùng | Đầy đủ quyền của chủ thể dữ liệu khách hàng | Bắt buộc lập DPIA và đánh giá chuyển dữ liệu ra nước ngoài trước khi bật O1 | Chưa phát sinh chuyển dữ liệu khách hàng ở Base Scope |

5. Nhà cung cấp, subprocessor, vị trí xử lý (Chờ S5 – SEC 04)

| Bên | Chức năng | Nơi xử lý / lưu / hỗ trợ (prompt, chỉ mục, log, backup) | Cấm huấn luyện trái phép? | Lưu giữ và xoá |
| --- | --- | --- | --- | --- |
| OpenAI / Microsoft Azure OpenAI (Dự phòng: Google Cloud Vertex AI) | LLM Inference API (gpt-4o) — sinh câu trả lời tiếng Việt trích dẫn | Khu vực Đông Á / Đông Nam Á (hoặc Singapore nếu dùng Vertex AI) | Có — Enterprise ZDR / Cấm huấn luyện lại mô hình | Tức thời (In-memory only), không lưu prompt/completion trên đĩa bên thứ ba |
| OpenAI / Microsoft Azure OpenAI | Embedding API (text-embedding-3-small, 1536 chiều) — vector hóa chính sách | Khu vực Đông Á / Đông Nam Á | Có — Enterprise ZDR / Cấm huấn luyện lại mô hình | Tức thời (In-memory only), giải phóng RAM ngay sau khi trả vector |
| Hạ tầng Local VM Nội bộ SongNhat (PostgreSQL/pgvector & Redis) | Lưu trữ documents, passages, passage_embeddings, audit_logs và Redis cache | Việt Nam (100% máy chủ nội bộ trong nước) | Có — Hạ tầng nội bộ SongNhat kiểm soát | Chặn tức thời (0s) khi rút chính sách; dọn sạch Redis cache trong <= 5 phút; audit_logs 12 tháng |
| Kho sao lưu mã hóa AES-256 nội bộ SongNhat | Backup cơ sở dữ liệu & cấu hình phục vụ DR (RTO 4h / RPO 24h) | Việt Nam (100% lưu trữ nội bộ trong nước) | Có — Hạ tầng nội bộ SongNhat kiểm soát | Xoay vòng tự động 35 ngày (Annex C); phát lại trạng thái xóa/rút trước khi khôi phục |

6. Lưu giữ (CKPA-19 (CRM-G0-SUB12), Annex C)

Xem file P1_RaSoat_Retention_v1. Tóm tắt ý kiến sơ bộ: chấp thuận passage và critical field; CRM context cơ bản không lưu; answer/referral, raw export và backup chấp thuận có điều kiện. Đề xuất là vận hành, không phải thời hạn luật định.

7. Sự cố và thay đổi provider (SEC 07, SEC 08)

S5 soạn quy trình; P1 duyệt. Yêu cầu RFP: thông báo cho bên mua trong 4 giờ trôi qua sau khi biết sự cố nghi ngờ về dữ liệu production hoặc kiểm soát chính sách trọng yếu; giữ bằng chứng hạn chế; tuân thủ nghĩa vụ luật định đã xác nhận. Review thay đổi provider, model, prompt, selector, phạm vi; đánh giá lại rủi ro, chạy lại test bị ảnh hưởng; giữ rollback, tắt khẩn cấp và chủ chịu trách nhiệm. Kết quả duyệt của P1: [chờ bản của S5].

8. Điểm chưa chắc chắn, cần hỏi chủ pháp lý hoặc giảng viên

| Vấn đề | Ai cần trả lời | Hạn |
| --- | --- | --- |
| 1. Câu hỏi của nhân viên (đã qua lọc pii_guard.py) truyền qua API của OpenAI/Azure OpenAI ở Đông Á/Đông Nam Á có cấu thành hoạt động chuyển dữ liệu cá nhân ra nước ngoài theo Luật 91/2025/QH15 & NĐ 356/2025/NĐ-CP không? | Legal Owner SongNhat (Thẩm định chính thức tại Gate G2 — CKPA-34) | Trước Gate G2 (CKPA-34) |
| 2. Thẩm định văn bản phân loại hệ thống AI (không thuộc danh mục AI rủi ro cao theo QĐ 33/2026/QĐ-TTg) và hồ sơ cấp độ an toàn thông tin (đề xuất Cấp độ 2 theo Luật ANM 116/2025/QH15). | Legal Owner & Privacy/Security Owner SongNhat | Trước Gate G2 (CKPA-34) |
| 3. Quy trình ứng phó sự cố trong <= 4 giờ liên tục (SEC 07) và quy trình quản lý thay đổi provider/model/prompt (SEC 08) do S5 (Nguyễn Ngọc Duy) & P4 (Ngô Thị Trà My) phối hợp hoàn thiện ở G1–G2. | S5 (Nguyễn Ngọc Duy) & P4 (Ngô Thị Trà My) | Trước Gate G2 (CKPA-34) |

9. Phụ lục: văn bản đã đọc

| Mã (Annex F) | Văn bản | Ngày đọc | Link |
| --- | --- | --- | --- |
| R02 | Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 | 17/11/2026 | https://congbao.chinhphu.vn/van-ban/luat-so-91-2025-qh15-45578.htm |
| R03 | Nghị định 356/2025/NĐ-CP | 17/11/2026 | https://vanban.chinhphu.vn/?docid=216387&pageid=27160 |
| R04 | Luật Trí tuệ nhân tạo 134/2025/QH15 | 17/11/2026 | https://vanban.chinhphu.vn/?docid=216334&pageid=27160 |
| R05 | Luật An ninh mạng 116/2025/QH15 | 17/11/2026 | https://vanban.bocongan.gov.vn/co-so-du-lieu-van-ban/luat-an-ninh-mang-1768902649?tab=related |
| R10 | Nghị định 142/2026/NĐ-CP | 17/11/2026 | https://vanban.chinhphu.vn/?docid=218029&orggroupid=2&pageid=27160 |
| R11 | QĐ 33/2026/QĐ-TTg (danh mục rủi ro cao) | 17/11/2026 | https://baochinhphu.vn/danh-muc-he-thong-tri-tue-nhan-tao-co-rui-ro-cao-102260702152849868.htm |
