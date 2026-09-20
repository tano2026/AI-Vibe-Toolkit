# fabric — GitHub Repo

## TL;DR
Kho prompt AI đã qua kiểm chứng, chạy thẳng từ terminal — mỗi tác vụ chỉ cần 1 lệnh. 43,6k sao, 4,2k fork.

## Repo này dùng để làm gì
Tổng hợp "Pattern" (mẫu prompt đã tối ưu sẵn) cho hàng loạt tác vụ: tóm tắt, viết lại, phân tích bài viết, trích insight, review code... Thay vì tự viết prompt từ đầu mỗi lần, gọi thẳng pattern có sẵn qua CLI.

## Setup từng bước
1. Cài (Go-based): `go install github.com/danielmiessler/fabric@latest`
2. Cấu hình API key model muốn dùng: `fabric --setup`
3. Dùng ngay:
```bash
echo "nội dung cần tóm tắt" | fabric --pattern summarize
cat bai-viet.txt | fabric --pattern extract_wisdom
```
4. Xem toàn bộ pattern có sẵn: `fabric --listpatterns`

## Ví dụ thực tế
Có 1 bài báo dài về xu hướng AI 2026 cần tóm tắt nhanh cho Research Pro dùng làm nguồn — thay vì tự viết prompt, chạy `cat baibao.txt | fabric --pattern extract_wisdom` ra ngay bullet point insight chính, tiết kiệm thời gian viết prompt lặp lại.

## Lưu ý / Lỗi thường gặp
- Cần tự cấu hình API key (không có key sẵn) — hỗ trợ nhiều provider (OpenAI, Claude, local model)
- Pattern là cộng đồng đóng góp — chất lượng không đồng đều, nên test trước khi dùng cho việc quan trọng
- Chạy qua CLI nên hợp pipe với lệnh khác (`cat file | fabric ...`), không hợp dùng trong code Python trực tiếp (cần gọi subprocess)

## Đánh giá cá nhân
- Điểm mạnh: tiết kiệm thời gian viết prompt lặp lại, pattern đa dạng, tích hợp tốt vào workflow terminal/script
- Điểm yếu: chất lượng pattern phụ thuộc cộng đồng, không có guarantee như skill tự viết riêng cho nghiệp vụ cụ thể
- Có nên dùng: 7/10 — hữu ích cho tác vụ chung (tóm tắt, viết lại), không thay được skill chuyên biệt đã xây riêng (vd source-evaluation)

## Link
- Repo: https://github.com/danielmiessler/fabric
