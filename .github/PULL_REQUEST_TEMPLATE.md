## Summary
<!-- Mô tả ngắn gọn nội dung thay đổi của PR -->

## Related Jira Issue
- **Jira Key:** `CKPA-XX` (Mã Excel: `CRM-G1-SUBXX`)
- **Gate / AC:** `G1-AC0X`
- **Role thực hiện:** `[P1/P2/P3/P4/P5]`

## Changes
- 

## Testing & Verification
- [ ] Đã chạy `python scripts/ci_purchaser_guard.py` — **PASS (0 lỗi, 0 PII hits)**
- [ ] Đã đối chiếu đúng schema CSV UTF-8 (`21` cột Passages / `23` cột Critical Fields) nếu có file CSV

## Evidence
- Link Jira Issue / file log / biên bản đính kèm:

## SoD & Compliance Checklist (Bắt buộc)
- [ ] Không làm việc / không push trực tiếp lên `main` hoặc `develop`
- [ ] Không chứa secrets, API keys, mật khẩu hoặc PII khách hàng thật (`SEC 02 / SEC 06`)
- [ ] Không chứa nội dung plaintext `100 Sealed Acceptance Cases` hoặc `80 Constructed Challenges` (`sealed-eval-repo` riêng)
- [ ] Phạm vi Base Scope thuần túy (`O1 = OFF`)
- [ ] Không gán `[S4]` Quý Hải review PR nhánh `feat/` (nếu liên quan đồng bộ sang repo Supplier)

## Notes
<!-- Lưu ý, blocker hoặc điểm cần reviewer chú ý -->
