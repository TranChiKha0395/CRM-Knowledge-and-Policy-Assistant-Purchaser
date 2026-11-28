# HỒ SƠ KÝ DUYỆT PRE-G2 - CKPA-104

- **Jira:** `CKPA-104` - `[G2][SEC03] Ký duyệt Pháp lý, SEC07/08 & QL& data`
- **Parent Jira:** `CKPA-85` - `[G2][IWP04-05] Hoàn thiện Workspace & Kiểm định Nghiệm thu G2`
- **Cổng & Tiêu chí:** Pre-G2 (`G2-AC04`, `G2-AC07` | RFP: `SEC 01..08`, `Annex C`, `Annex F`, `R02..R05`)
- **Branch:** `sec/CKPA-104-sign-pre-g2-legal-sec03-08`
- **Ngày lập:** `28/11/2026`
- **Lịch Jira:** `30/12/2026 -> 31/12/2026`
- **Estimate:** `12h`
- **Chủ trì:** `[P5]` Nguyễn Anh Khoa
- **Phối hợp:** `[S5]` Nguyễn Ngọc Duy, `[S4]` Phạm Quý Hải
- **Nghiệm thu:** `[P1]` Vắn Mỹ Vân
- **Reviewer:** `[P3]` Trần Chí Kha
- **Hỗ trợ pháp lý/vận hành:** `[P4]` Ngô Thị Trà My
- **Bằng chứng G1:** `CKPA-47`, `CKPA-70`, `CKPA-79`, `CKPA-103`

## 1. Mục tiêu và ranh giới

Hồ sơ này chuẩn bị danh mục pháp lý, dữ liệu và vận hành để [P1]/Legal Owner ký duyệt trước Gate G2. Tài liệu không thay thế ý kiến pháp lý chính thức và không xác nhận chữ ký còn thiếu.

Phạm vi bắt buộc:

- SEC 03 & Khung pháp lý (R02–R05): tuân thủ Luật BVDLCN 91/2025/QH15 & NĐ 356/2025/NĐ-CP (R02–R03), Luật An ninh mạng 116/2025/QH15 (R05), Thông báo minh bạch AI, quyền chủ thể và đánh giá chuyển dữ liệu.
- SEC 07: thông báo sự cố dữ liệu/sai lệch kiểm soát trọng yếu trong tối đa 4 giờ liên tục.
- SEC 08: thay đổi provider/model/prompt/selector/scope, đánh giá rủi ro, test, rollback và emergency-disable.
- QL& data: lịch lưu giữ, data owner, retention, backup, hold, deletion và withdrawal.
- Base Scope: O1 = OFF; không nạp dữ liệu CRM sản xuất vào giai đoạn G1/G2 và không chuyển hồ sơ khách hàng ra ngoài.

## 2. Ma trận bằng chứng Pre-G2

| Mã | Nội dung cần ký duyệt | Tài liệu/bằng chứng | Trạng thái |
|---|---|---|---|
| SEC 03 | Vai trò Controller/Processor/Subprocessor và xử lý dữ liệu | `security/g0/P1_HoSoPhapLy_CoNgay_v1_HoanChinh.md`; `security/g0/legal-privacy-review.md` | PENDING LEGAL SIGN-OFF |
| SEC 03 | Cơ sở pháp lý, thông báo và quyền chủ thể | `security/g0/P1_HoSoPhapLy_CoNgay_v1_HoanChinh.md` | PENDING LEGAL SIGN-OFF |
| SEC 03 | Đánh giá chuyển dữ liệu ra nước ngoài | `security/g0/legal-privacy-review.md` mục 2.1 | PENDING LEGAL SIGN-OFF |
| Annex F | Lập luận phân loại AI có ngày & hồ sơ filing/conformity (`G2-AC07`) | `security/g2/CKPA-103_Lap_Luan_Phan_Loai_AI_Va_Ho_So_Annex_F_G2.md` | PR #64 SUBMITTED; PENDING S1/P1 REVIEW |
| SEC 06/07 | 4-hour incident notification, evidence freeze, fail-closed | `security/g0/legal-privacy-review.md` mục 1.6 | PENDING RUNBOOK SIGN-OFF |
| SEC 05/07 | Withdrawal fail-closed | `security/g1/CKPA-70_Bao_Cao_Kiem_Toan_Lo_Lot_RBAC_Cache_FailClosed_G1.md` | TECHNICAL PASS; OWNER SIGN-OFF PENDING |
| SEC 08 | Change control, test and rollback | Runbook change-control trong mục 4 dưới đây | PENDING S5/P4 APPROVAL |
| DAT/QL | Retention đề xuất 12 tháng / 90 ngày / 35 ngày | `security/g0/P1_RaSoat_Retention_v1_HoanChinh.md` | P1 ĐÃ DUYỆT CÓ SỬA; OWNER PENDING THEO HẠNG MỤC |
| PII | Không PII trong kho chung/corpus/CI | `security/g1/CKPA-47_Chung_Nhan_Du_Lieu_Kiem_Thu_0_PII_G1.md` | G1 EVIDENCE PASS |
| O1 | O1 = OFF; không kết nối CRM thật | `security/g1/CKPA-47_Chung_Nhan_Du_Lieu_Kiem_Thu_0_PII_G1.md`; `policy/g0/CKPA-9_Bien_Ban_Xac_Nhan_Pham_Vi_G0_Va_3_Nhom_Chinh_Sach.md` | G1 BASE-SCOPE PASS |
| ACL | Kho Sealed và ranh giới collaborator | `security/g1/CKPA-79_Bien_Ban_Kiem_Toan_ACL_Sealed_Va_Chot_Bao_Mat_G1.md` | PART 1 PASS; EXTERNAL PART 2 PARTIAL_PASS/BLOCKED |

## 3. Quy trình sự cố SEC 07

1. T0: ghi nhận thời điểm phát hiện nghi ngờ sự cố dữ liệu sản xuất hoặc sai lệch chính sách trọng yếu.
2. S5 kích hoạt Fail-Closed, khoanh vùng dịch vụ, ngăn truy cập mở rộng và ngừng thay đổi có rủi ro.
3. S5 bảo toàn snapshot read-only: log truy cập, container, network, audit trail, config, cache và snapshot dữ liệu liên quan.
4. S5 thông báo Ban Quản trị/SongNhat tối đa 4 giờ liên tục kể từ T0.
5. P5/P1 đánh giá phạm vi dữ liệu cá nhân, pháp lý, chính sách và trách nhiệm thông báo theo Luật/Nghị định hiện hành.
6. Ghi nhật ký quyết định, recovery, owner, deadline và bằng chứng đóng cửa.
7. Sau recovery, P1/P5/S5 thực hiện hậu kiểm và xác nhận không tái diễn trước khi mở lại hoàn toàn.
8. Khi phục hồi, P4 cùng rep users đối chiếu nhật ký fallback; P3 kiểm tra tính toàn vẹn dữ liệu và audit log; báo cáo kết thúc diễn tập hoàn tất trong 2 giờ làm việc.

Điểm chưa ký: cơ quan/đối tác tiếp nhận thông báo cụ thể, mẫu thông báo pháp lý và SLA hậu kiểm phải được [P1]/Legal Owner xác nhận.

## 4. Quy trình thay đổi SEC 08

Mọi thay đổi provider, model, prompt, selector, embedding, scope hoặc data source phải có:

| Bước | Yêu cầu bắt buộc | Chủ trách nhiệm |
|---|---|---|
| 1 | Ticket thay đổi, lý do, phạm vi, owner và rollback | S5/P4 |
| 2 | Đánh giá bảo mật, PII, RBAC, source_ref, withdrawal, SLA | P5/P3/S5 |
| 3 | Chạy unit/integration/G1/G2 test có liên quan | P5/S1 |
| 4 | Duyệt risk acceptance và emergency-disable | P1/P5 |
| 5 | Triển khai có kiểm soát, quan sát và log | S5 |
| 6 | Xác nhận, đóng ticket hoặc rollback ngay | P1/P5/S5 |

Không kích hoạt thay đổi mới khi chưa có approval; không xóa/ghi đè bằng chứng; mọi thay đổi rollback phải giữ traceability đến tài liệu và chính sách cũ.

## 5. Lịch lưu giữ và owner

| Dữ liệu | Thời hạn đề xuất | Owner/vị trí | Điều kiện trước G2 |
|---|---:|---|---|
| Passage tri thức | Duy trì current/superseded/withdrawn khi cần lịch sử | P2/P3, kho nội bộ | P2/P3 xác nhận owner |
| Critical field | Đồng bộ vòng đời passage và vô hiệu hóa khi hết hiệu lực | P2/P3 | P2/P3 xác nhận giá trị và owner |
| CRM context/O1 | Base Scope: 0 ngày (`O1 = OFF`); Mở rộng có duyệt: tối đa 12 tháng, xóa sớm hơn khi hết mục đích cần thiết | S2/S5 | O1 OFF; chỉ kích hoạt sau phê duyệt mới |
| Answer/referral/audit | Tối đa 12 tháng cho mục đích kiểm toán/khiếu nại | S4/S5/P5 | P1 xác nhận mục đích đã duyệt |
| Raw export | Xóa bản sao tiện ích sau 90 ngày | P3/S2/P4 | Xác nhận chủ đối soát và danh mục quyền |
| Backup | Xoay vòng 35 ngày | S5 | Xác nhận replay withdrawal/deletion trước G4 |
| Cache | Withdrawal tối đa 5 phút; emergency-disable tối đa 5 phút | S5 | Đối chiếu bằng chứng live G1 và UAT fallback |

Chặn truy cập tức thời khác với xóa vật lý. Tài liệu/answer withdrawal phải ngăn truy cập hiện tại ngay lập tức trong khi chỉ giữ bằng chứng kiểm toán và hồ sơ theo thời hạn được phê duyệt.

Lưu ý trạng thái: P1 đã ký `Duyệt có sửa` hồ sơ retention ngày `17/11/2026`; [P5] Nguyễn Anh Khoa đề xuất chuyên môn. Các con số trên là đề xuất vận hành/Annex C, chưa phải thời hạn pháp lý bắt buộc cho đến khi Legal Owner/owner chịu trách nhiệm xác nhận.

## 6. Danh sách ký duyệt

| Hạng mục | Người ký/xác nhận | Trạng thái |
|---|---|---|
| Phân loại hệ thống AI và vai trò pháp lý | Legal Owner SongNhat | PENDING - G0 chỉ có đề xuất không thuộc rủi ro cao |
| Xử lý DLCN và chuyển dữ liệu ra nước ngoài | Legal Owner + P5 | PENDING |
| Incident SEC 07 và manual fallback | P1 + P5 + S5/P4 | PENDING |
| Change control SEC 08 | P1 + P5 + S5/P4 + P3/S1 khi có test | PENDING |
| Retention và data owner | P1 + P5 + P2/P3/S2/S4/S5 theo từng loại dữ liệu | P1 ĐÃ DUYỆT CÓ SỬA; chi tiết owner PENDING |
| Sealed/ACL external evidence | S4 + P5/S1 | PENDING external snapshot; PARTIAL_PASS hiện hữu |

## 7. Điều kiện đóng CKPA-104

CKPA-104 chỉ được chuyển `Done` khi tồn tại ít nhất:

- Biên bản hoặc văn bản ký duyệt Legal/Privacy/Security.
- Runbook SEC 07/08 đã được P1, P5, S5/P4 xác nhận.
- Ma trận owner và lịch lưu giữ đã hoàn tất.
- Danh mục remaining evidence và deadline được ghi rõ.
- Không còn khẳng định pháp lý chưa có cơ sở ký duyệt.