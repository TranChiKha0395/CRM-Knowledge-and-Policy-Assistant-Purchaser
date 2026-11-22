Rà soát lịch lưu giữ (Annex C) – ý kiến duyệt sơ bộ

Task CKPA-19 (CRM-G0-SUB12: [G0][AnnexC] Đề xuất Lịch lưu giữ 90d/12m/35d & Hold) / Parent: CKPA-16 (CRM-G0-ST04). Dữ liệu giả lập (đồ án học tập).

| Bản ghi | Đề xuất của RFP (Annex C) | Ý kiến sơ bộ | Lý do | Cần xác nhận với |
| --- | --- | --- | --- | --- |
| Passage tri thức | Mã, tiêu đề, tham chiếu gốc, nội dung, chủ sở hữu và người duyệt, phạm vi, đối tượng, hiệu lực, thời điểm ghi nhận, trạng thái, liên kết thay thế. Giữ tri thức hiện hành đã duyệt và lịch sử cần thiết được phép. | Chấp thuận | Khớp DAT 01; lịch sử cần thiết phục vụ trả lời theo ngày | S2, P4 |
| Critical field | Rule ID, phiên bản clause, giá trị có kiểu, toán tử, tiền tệ/đơn vị, tài liệu, vai trò, điều kiện ngoại lệ, phạm vi, khoảng hiệu lực. Chủ chính sách duyệt giá trị chính xác; không tự trích xuất. | Chấp thuận | Khớp DAT 06 | P2, P3 |
| CRM context (chỉ O1) | Khoá tài khoản và bản ghi, trường cần thiết, mốc nguồn, xác minh, đối tượng, phiên bản. Tối đa 12 tháng nếu có lý do; xoá sớm hơn khi không cần. Cơ bản không lưu snapshot CRM. | Chấp thuận: cơ bản 0 ngày (không lưu snapshot CRM); Option O1 đã cắt khỏi Base Scope tại CKPA-5 | Phụ thuộc quyết định CKPA-75 (mã lưu trữ CKPAOLD trước 19/11) | S2, S5 |
| Answer và referral | Mã task và lần thử, câu hỏi, ngữ cảnh được phép, nguồn và phiên bản, ngày, câu trả lời, hold, phản hồi, trạng thái referral, chi phí. Tối thiểu để chứng minh claim, tối đa 12 tháng theo mục đích đã duyệt. | Chấp thuận có điều kiện: lưu tối đa 12 tháng trên PostgreSQL nội bộ cho mục đích đối soát khiếu nại, kiểm toán nguồn trích dẫn và đánh giá Pilot G3 | Cần ghi rõ 'mục đích đã duyệt' cho thời hạn 12 tháng | S4, S5 |
| Raw export | Hạn chế cho chủ đối soát. Xoá bản sao tiện lợi sau 90 ngày trừ khi có lý do được duyệt. | Chấp thuận có điều kiện: chỉ định P3 (Trần Chí Kha) và S2 (Trần Quốc Hưng) là chủ đối soát; xóa bản sao tạm sau 90 ngày | Cần chỉ định ai là chủ đối soát | S2, P4 |
| Backup | Xoay vòng 35 ngày. Phát lại trạng thái xoá và rút trước khi dữ liệu khôi phục được truy cập. Legal hold và nghĩa vụ hồ sơ cần chủ rà soát. | Chấp thuận có điều kiện: S5 (Nguyễn Ngọc Duy) xác nhận xoay vòng 35 ngày trên kho mã hóa AES-256 nội bộ (CKPA-19 / CKPA-34), cần bổ sung quy trình test replay xóa/rút trước G4 | S5 xác nhận cơ chế phát lại xoá/rút (OPS 07) | S5 |

Nguyên tắc cần giữ (Annex C)

Rút chính sách (withdrawal) khác với xoá (deletion): giữ bằng chứng kiểm toán hạn chế hợp pháp nhưng ngăn việc dùng hiện tại.

Sửa lỗi tạo phiên bản ghi nhận mới và thay đổi phụ thuộc; không âm thầm viết lại câu trả lời lịch sử.

Xử lý quyền chủ thể phải bao gồm kho đang hoạt động, chỉ mục, cache, nhật ký, nhà cung cấp và backup; phân biệt chặn tức thì với hết hạn vật lý.

Quyết định của P1: ☐ Duyệt như trên   ☑ Duyệt có sửa   ☐ Chưa duyệt

Ngày: 17/11/2026 — Người duyệt: [P1] Văn Mỹ Vân (Purchaser Sponsor / PO) | Đề xuất chuyên môn: [P5] Nguyễn Anh Khoa (Privacy & Security Owner) (Khung cơ sở G0; trình ký chính thức tại Gate G2)
