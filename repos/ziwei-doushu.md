# ziwei-doushu (Renhuai123) — GitHub Repo

## TL;DR
Web app Next.js đầy đủ + dataset 518,400 lá số mẫu cho Tử Vi Đẩu Số, build trên chính iztro — clone về là có ngay 1 sản phẩm tử vi hoàn chỉnh thay vì code từ đầu. 2,490⭐, MIT (code) + tự do thương mại (data, chỉ cần ghi nguồn).

## Repo này dùng để làm gì
Đây không chỉ là lib tính toán như iztro mà là cả 1 web app Next.js 14 hoàn chỉnh: trang lập lá số, trang hợp lá số (so 2 người), trình đọc cổ thư tử vi (Cốt Tủy Phú, Tử Vi Đẩu Số Toàn Tập/Toàn Thư), trang tra cứu 14 chính tinh + 12 cung, dark/light mode, responsive mobile. Engine tính toán bên trong dùng chính `iztro` + `lunar-javascript`. Đi kèm 1 bộ 518,400 lá số mẫu (mọi tổ hợp năm×tháng×ngày×giờ×giới tính), mỗi mẫu có sẵn văn bản luận giải theo 13 chủ đề (tổng quan, tài vận, sự nghiệp, tình cảm, sức khỏe...) — dataset này dùng thương mại tự do, không cần xin phép, chỉ cần ghi nguồn.

## Setup từng bước
1. `git clone https://github.com/Renhuai123/ziwei-doushu.git && cd ziwei-doushu`
2. `npm install`
3. `cp .env.example .env.local` rồi điền API key LLM của mày vào (bản open source KHÔNG kèm sẵn route API luận giải AI, route `/api/interpret` phải tự viết)
4. `npm run dev` → mở `localhost:3000`
5. Muốn lấy bộ dataset mẫu: vào tab Releases của repo, tải 3 phần zip (~5.5GB tổng), gộp lại bằng `cat part1 part2 part3 > combined.zip` rồi unzip

## Ví dụ thực tế
Dùng dataset mẫu làm RAG cho chatbot tử vi: lấy lá số người dùng nhập vào, tìm sample gần khớp nhất trong 518k mẫu (theo năm/tháng/ngày/giờ/giới tính), feed văn bản luận giải mẫu đó vào prompt cho Claude viết lại theo giọng văn riêng của kênh — nhanh hơn và rẻ hơn bắt LLM tự luận giải from scratch mỗi lần.

## Lưu ý / Lỗi thường gặp
- Bản open source CHỈ gồm: thuật toán lập lá số + kho kiến thức/cổ thư + frontend. Phần giữ lại (không mở): prompt luận giải AI, route API backend, hệ thống user/thanh toán, cấu hình deploy. Tức là chạy được phần "xem lá số" ngay, nhưng phần "AI luận giải" phải tự code thêm.
- Bộ dataset 5.5GB tải về khá nặng, chia 3 phần — nhớ gộp đúng thứ tự trước khi unzip, có kèm SHA256SUMS để verify file không lỗi.
- Tác giả vẫn đang vận hành song song bản SaaS riêng (wdyziweidoushu666.com) — repo open source là phiên bản "lõi", không phải bản đầy đủ tính năng của sản phẩm thật của họ.

## Đánh giá cá nhân
- Điểm mạnh: tiết kiệm cực nhiều thời gian build UI/UX từ đầu, dataset 518k mẫu thương mại tự do là tài sản hiếm — ít kho nào cho free và cho dùng thương mại luôn như vậy.
- Điểm yếu: thiếu lớp AI luận giải + backend, nghĩa là vẫn phải tự code phần "não" của sản phẩm; UI theo gu/màu sắc riêng của tác giả, có thể cần restyle nếu muốn ra brand riêng.
- Có nên dùng: 8/10 — đáng để clone làm điểm khởi đầu build SaaS tử vi, đặc biệt nếu kết hợp dataset với Claude để tạo lớp luận giải riêng.

## Link
- Repo: https://github.com/Renhuai123/ziwei-doushu
- Dataset Releases: https://github.com/Renhuai123/ziwei-doushu/releases/tag/v3.0-samples
- Demo/sản phẩm gốc tác giả: https://wdyziweidoushu666.com
