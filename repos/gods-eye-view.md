# God's Eye View — GitHub Repo

## TL;DR
Web app 3D globe chạy trong browser, gộp toàn bộ dữ liệu công khai thời gian thực (máy bay, tàu biển, vệ tinh, động đất, cháy rừng, camera công cộng) vào 1 quả địa cầu photorealistic, điều khiển bằng giọng nói AI — của Bilawal Sidhu (series YouTube "WorldView" 5M+ view). #1 GitHub Trending, 39.7k star.

## Repo này dùng để làm gì
Bình thường muốn theo dõi máy bay/tàu/vệ tinh phải mở chục tab riêng (FlightRadar24, MarineTraffic, N2YO...). God's Eye View gộp hết vào 1 quả địa cầu 3D duy nhất: click vào máy bay xem transponder telemetry (OpenSky/adsb.lol), theo dõi tàu qua AIS beacon (AISStream), theo ~840 vệ tinh theo class màu (CelesTrak), lớp cháy rừng NASA FIRMS, giao thông đường phố (TomTom), và cả CCTV công cộng thật ở 1 số thành phố. Có voice agent (OpenAI Realtime API) để hỏi bằng tiếng thường, AI tự chú thích trực tiếp lên globe 3D. Toàn bộ chạy local-first, không có secret/dataset riêng — mọi thứ liên quan API key nhạy cảm được broker qua server riêng, không lộ ra client.

## Setup từng bước
1. **Cách dễ nhất — Pinokio** (không cần biết code): mở God's Eye View trong Pinokio → bấm Install → Start. Chạy được Windows/macOS/Linux.
2. **Chạy local từ terminal:**
   ```bash
   git clone https://github.com/bilawalsidhu/gods-eye-view.git
   cd gods-eye-view
   npm install
   npm run doctor   # kiểm tra môi trường trước khi chạy
   npm run dev
   ```
   Mở `http://localhost:4173`.
3. Yêu cầu Node.js 24.x (24.14.0+) hoặc 26.x — Node 25 đã end-of-life, `npm run doctor` sẽ tự cảnh báo nếu dính bản này.
4. **Không cần API key để bắt đầu** — app khởi động "keyless", tự dùng Esri World Imagery + OSM terrain miễn phí. Muốn có địa cầu photorealistic đầy đủ mới cần 1 API key duy nhất: **Google Maps (Map Tiles API)** — đây là key trả phí duy nhất bắt buộc, mọi key khác (OpenSky, AISStream, CelesTrak...) đều miễn phí hoặc không cần.
5. Không rành code — copy nguyên đoạn hướng dẫn này dán vào Claude Code/Codex/Cursor/Antigravity để agent tự clone + setup + dẫn dắt lấy Google Maps API key hộ:
   ```
   Clone https://github.com/bilawalsidhu/gods-eye-view và cài lên máy tao.
   Cài mọi thứ nó cần, dẫn tao lấy Google Maps API key cần thiết.
   ```
6. Sắp có **bản hosted chính thức** tại Halfpixel (không cần cài gì, mở thẳng trên browser) — repo hiện tại vẫn là bản open-source client, theo dõi README để biết khi ra mắt.

## Ví dụ thực tế
Dùng để theo dõi trực tiếp lộ trình chuyến bay quốc tế (vd bay ABTRIP đang xử lý), click vào 1 máy bay cụ thể trên globe xem route/tốc độ/độ cao thời gian thực, hoặc bật "Cockpit view" để camera bám theo góc nhìn từ trong máy bay đang bay — hợp làm demo trực quan cho nội dung về ngành hàng không trên kênh của Tan.

## Lưu ý / Lỗi thường gặp
- Đây là **client mã nguồn mở gốc**, không phải chỉ 1 trong nhiều bản sao — có nhiều fork/mirror trùng nội dung (vd `MikeeonTop/gods-eye-view`), bản chính chủ theo dõi cập nhật là **bilawalsidhu/gods-eye-view**.
- Repo tự đặt giới hạn đạo đức rõ ràng: **không** build tính năng tìm người theo tên, nhận diện khuôn mặt, hay theo dõi cá nhân cụ thể — PR nào phá giới hạn này sẽ bị từ chối merge. Đây là điểm quan trọng cần biết trước khi định mở rộng thêm layer riêng.
- CCTV camera pose và trajectory tên lửa là **ước lượng thô** (coarse estimate), traffic layer là dữ liệu mô phỏng dựa trên aggregate location data (TomTom) — không phải mọi thứ trên globe đều là dữ liệu chính xác 100% real-time, đọc kỹ phần "What's Live" trong README trước khi dùng làm nguồn tham khảo chính thức.
- `./scripts/dev-fresh.sh` từng có bug crash trên macOS chạy Bash 3.2 mặc định khi không set provider key — đã fix ở bản v0.1.1, nhớ pull bản mới nhất nếu gặp lỗi này.

## Đánh giá cá nhân
- **Điểm mạnh:** Trải nghiệm trực quan hiếm có — gộp nhiều nguồn OSINT công khai vào 1 giao diện đẹp, dễ demo, khởi động không cần API key nào (chỉ cần key khi muốn nâng cấp visual). Có giới hạn đạo đức rõ ràng ngay trong chính sách contribute, không phải chỉ nói suông.
- **Điểm yếu:** Một số layer (traffic, CCTV pose, trajectory) là dữ liệu mô phỏng/ước lượng chứ không phải real-time chính xác tuyệt đối — dễ gây hiểu lầm nếu dùng làm nguồn phân tích thật. Cần Node.js bản mới (24.x/26.x), máy cũ/môi trường cũ dễ vướng.
- **Có nên dùng không:** 8/10 cho mục đích trình diễn/giải trí/học hỏi về dữ liệu công khai (hàng không, hàng hải, vệ tinh) — không hợp làm nguồn dữ liệu chính thức cho quyết định nghiệp vụ thật vì độ chính xác từng layer khác nhau khá nhiều.

## Link
- Repo: https://github.com/bilawalsidhu/gods-eye-view
- Docs/Demo: xem README (Quick Start · First Five Minutes · Talk to It · What's Live) · kênh YouTube tác giả: https://youtube.com/@bilawalsidhu
