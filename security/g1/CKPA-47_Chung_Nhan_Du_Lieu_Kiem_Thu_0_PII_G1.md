| DỰ ÁN SONGNHAT CRM KNOWLEDGE AND POLICY ASSISTANT (SCRM) — GATE G1 CHỨNG NHẬN DỮ LIỆU KIỂM THỬ HỢP PHÁP G1 (0% PII & RANH GIỚI O1) Mã Jira: CKPA-47 (CRM-G1-SUB02) \| Tiêu chí Cổng: G1-AC07 \| Phiên bản: 2.1 (Đồng bộ SHA a5a6a14) |
| --- |

| Mã công việc & Truy vết RFP | CKPA-47 \| CRM-G1-SUB02 \| G1-AC07 \| SEC 02, SEC 06, DAT 07, Mục 9 (G1), Annex C |
| --- | --- |
| Người lập & Kiểm toán (Assignee) | [P5] Nguyễn Anh Khoa — Privacy and Security Owner (Phía Purchaser) |
| Phối hợp & Nghiệm thu (RACI) | Reporter/Nghiệm thu: [P1] Mỹ Vân \| Phối hợp: [S5] Ngọc Duy, [P3] Chí Kha |
| Thời điểm & Commit kiểm toán | 2026-11-20 18:10:14 UTC+7 \| Nhánh: develop \| Commit SHA: a5a6a14 |
| Công cụ & Bằng chứng đính kèm | `security/scripts/g1_security_audit_runner.py` & `security/g1/g1_pii_audit_CKPA-47.log` |

I. PHÂN TÁCH PHẠM VI KIỂM TOÁN DỮ LIỆU & HẠ TẦNG GATE G1 (PASS VS. PENDING)

Để bảo đảm tính trung thực tuyệt đối của hồ sơ nghiệm thu Gate G1, Chủ sở hữu quyền riêng tư & bảo mật ([P5]) tách bạch rõ ràng giữa các tập dữ liệu/hạ tầng đã thực sự tồn tại trên repository và đã được quét kiểm toán trực tiếp (trạng thái PASS) với các gói dữ liệu chưa bàn giao hoặc đang ở trạng thái To Do (trạng thái PENDING):

| Hạng mục dữ liệu / Hạ tầng | Nguồn / PR / Jira | Trạng thái | Chi tiết kiểm toán & Bằng chứng đối chiếu |
| --- | --- | --- | --- |
| 1. Toàn bộ kho mã nguồn, cấu hình & dữ liệu hiện hữu trên develop | Nhánh develop(SHA: a5a6a14 — 20/11/2026 18:10:14 UTC+7) | PASS(0% PII) | Đã quét thực tế 48 tệp dữ liệu, tài liệu và cấu hình (.csv, .json, .md, .txt, .yml) bằng g1_security_audit_runner.py. Kết quả: 0 PII hits; 100% là dữ liệu giả lập (synthetic) hợp chuẩn SEC 02. |
| 2. Hạ tầng Test tách Prod & Phân quyền IAM 4 vai trò | CKPA-46 (PR #21)[S5] Ngọc Duy | PASS(SEC 06) | [P5] đã review trực tiếp PR #21 (ops/CRM-G1-SUB01-isolated-test-prod-iam): xác nhận tách biệt biến môi trường/hạ tầng Test khỏi Prod và cấu hình đủ 4 vai trò (reader, steward, policy_owner, admin). |
| 3. Gói dữ liệu chính sách Họ 1 (Base CSV Corpus & Fixtures) | CKPA-50 (PR #18 — đã merge vào develop)[P3] Chí Kha | PASS(0% PII) | Đã quét trực tiếp trong 48 tệp trên develop (data/g1/family1/, data/g1/fixtures/, data/g1/sources/): chỉ chứa chính sách nội bộ SongNhat và siêu dữ liệu hiệu lực, 0% PII khách hàng thật. |
| 4. Bộ 100 câu hỏi nghiệp vụ thực tế của người dùng đại diện | CKPA-55 (PR #20)[P4] Trà My | PASS(0% PII) | Đã kiểm chứng trực tiếp trên PR #20 (mở ngày 20/11): các tình huống hỏi đáp nghiệp vụ CRM đều dùng ngữ cảnh ẩn danh/giả lập, không lộ số điện thoại, email cá nhân hay CCCD khách hàng thật. |
| 5. Gói dữ liệu chính sách Họ 2–3 | CKPA-58[P3] Chí Kha (To Do) | PENDING(Chưa bàn giao) | Thẻ CKPA-58 đang ở trạng thái To Do, chưa mở PR trên repository. [P5] sẽ chạy quét kiểm toán bổ sung ngay khi [P3] bàn giao dữ liệu Họ 2–3. |
| 6. Bộ câu hỏi đánh giá 40 Val & 80 Challenges | CKPA-67[P4] Trà My / [S4] (To Do) | PENDING(Chưa bàn giao) | Dữ liệu chưa phát sinh trên repository. Sẽ được chạy quét 0% PII bổ sung trước khi ký biên bản nghiệm thu cổng Gate G1. |
| 7. Kho kín sealed-eval-repo & 100 Sealed Acceptance Cases | CKPA-48 / CKPA-79[S4] Quý Hải (To Do) | PENDING(Chưa tạo kho) | Kho sealed-eval-repo chưa khởi tạo. Không chốt PASS trước; việc kiểm toán phân quyền độc lập (Chinese Wall ACL chặn S2, S3) sẽ thực hiện tại CKPA-48 và CKPA-79 (Sprint 5). |

II. ĐỐI CHIẾU QUYẾT ĐỊNH PHẠM VI GATE G0 & RANH GIỚI TÙY CHỌN O1 (DAT 07)

| Quyết định kiến trúc từ Gate G0 | Triển khai 100% trong Phạm vi Cơ sở (Base Scope) với 02 tệp CSV chuẩn (passages và critical_fields). Không mua và không kích hoạt Tùy chọn O1 (Selected CRM Context). |
| --- | --- |
| Kiểm tra trường dữ liệu O1 (DAT 07) | Xác nhận không tồn tại kết nối API đọc hồ sơ khách hàng trực tiếp từ hệ thống CRM sản xuất; không phát sinh trường định danh khách hàng ngoài danh mục tối thiểu. |
| Kết luận tuân thủ SEC 02 & DAT 07 | ĐẠT CHUẨN — Ranh giới dữ liệu kiểm thử Gate G1 hoàn toàn cô lập khỏi dữ liệu khách hàng thật của SongNhat. |

III. KẾT QUẢ THỰC THI CÔNG CỤ KIỂM TOÁN TỰ ĐỘNG & LOG ĐÍNH KÈM

Công cụ kiểm toán tự động `security/scripts/g1_security_audit_runner.py` đã được đồng bộ quy tắc nhận diện PII với `backend/src/shared/pii_guard.py` (quét SĐT Việt Nam kể cả có dấu chấm/gạch ngang/khoảng trắng, email cá nhân ngoài domain `@songnhat.vn`, số CCCD 12 chữ số và MST 10 chữ số; tự động loại trừ `.git/`, `venv/`, `node_modules/`). Bản ghi thực thi chi tiết trên nhánh `develop` tại Commit SHA `a5a6a14` (lúc 2026-11-20 18:10:14 UTC+7, quét 48 tệp, 0 PII hits) được lưu tại tệp `security/g1/g1_pii_audit_CKPA-47.log` đính kèm cùng thẻ Jira `CKPA-47`.

IV. XÁC NHẬN & PHÊ DUYỆT KIỂM TOÁN (GATE G1 — G1-AC07)

| ĐẠI DIỆN KIỂM TOÁN BẢO MẬT ([P5]) | PHÊ DUYỆT NGHIỆM THU CỔNG G1 ([P1]) |
| --- | --- |
| Họ và tên: Nguyễn Anh Khoa — Vai trò: `[P5]` Privacy and Security Owner — Trạng thái: Đã kiểm toán & xác nhận 0% PII trên các gói dữ liệu hiện hữu (`develop` SHA `a5a6a14`, PR #18, PR #20 & PR #21). Ngày ký: 20/11/2026 | Họ và tên: Mỹ Vân — Vai trò: `[P1]` Purchaser Sponsor / Product Owner — Trạng thái: Đã phê duyệt nghiệm thu (`governance/g1/sub-tasks/P1_BienBan_NghiemThu_CKPA47.md`). Ngày phê duyệt: 20/11/2026 |
