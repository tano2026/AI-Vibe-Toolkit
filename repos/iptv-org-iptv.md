# iptv-org/iptv — GitHub Repo

## TL;DR
Kho 127k sao tổng hợp hàng chục nghìn kênh IPTV công khai từ khắp thế giới — dạng file M3U, cộng đồng cùng cập nhật, mở hoàn toàn.

## Repo này dùng để làm gì
Đây là danh bạ truyền hình mở lớn nhất internet. Repo chứa các file playlist M3U với link stream của kênh TV từ hàng trăm quốc gia — từ tin tức, thể thao, giải trí đến phim.

Không phải tool AI, nhưng cực kỳ hữu ích cho:
- Build ứng dụng xem TV online
- Tạo smart TV channel list
- Nghiên cứu về IPTV streaming infrastructure
- Vibe coder build media player app

File M3U có thể load vào VLC, Kodi, hoặc bất kỳ player nào hỗ trợ IPTV.

## Setup từng bước
**Cách 1: Xem ngay với VLC**
1. Mở VLC → Media → Open Network Stream
2. Dán URL:
```
https://iptv-org.github.io/iptv/index.m3u
```
3. Chờ load playlist → Chọn kênh muốn xem

**Cách 2: Dùng trong app/code**
```python
import requests

# Lấy toàn bộ playlist
playlist = requests.get("https://iptv-org.github.io/iptv/index.m3u").text

# Lọc kênh Việt Nam
vn_playlist = requests.get("https://iptv-org.github.io/iptv/countries/vn.m3u").text
print(vn_playlist[:500])
```

**Cách 3: Tích hợp vào Kodi**
1. Kodi → Add-ons → PVR IPTV Simple Client
2. Nhập URL: `https://iptv-org.github.io/iptv/countries/vn.m3u`

## Ví dụ thực tế
Build một trang web xem TV đơn giản:
```html
<video id="player" controls></video>
<script src="https://cdn.jsdelivr.net/npm/hls.js"></script>
<script>
  const stream = "https://link-từ-playlist-m3u";
  const video = document.getElementById('player');
  if (Hls.isSupported()) {
    const hls = new Hls();
    hls.loadSource(stream);
    hls.attachMedia(video);
  }
</script>
```

## Lưu ý / Lỗi thường gặp
- Nhiều stream có thể chết (link hỏng) — đây là vấn đề cố hữu của IPTV public
- Repo có CI tự động kiểm tra link hàng ngày, nhưng vẫn không tránh khỏi link die
- Một số kênh geo-restricted (chỉ xem được ở quốc gia gốc)
- Không nên dùng cho mục đích thương mại — nhiều kênh có bản quyền
- CORS có thể block nếu embed trực tiếp trên web — cần proxy

## Đánh giá cá nhân
- Điểm mạnh: Khổng lồ — hàng chục nghìn kênh, cập nhật liên tục bởi cộng đồng. Dễ dùng ngay với VLC.
- Điểm yếu: Tỷ lệ link chết cao, đặc biệt kênh nhỏ/địa phương. Không có guarantee về uptime hay chất lượng stream.
- Có nên dùng không: 7/10 — Nếu mày build app media player hay cần prototype IPTV feature, đây là nguồn dữ liệu tốt nhất hiện có. Cho cá nhân xem TV thì ok. Không build sản phẩm thương mại trên này.

## Link
- Repo: https://github.com/iptv-org/iptv
- Playlist index: https://iptv-org.github.io/iptv/index.m3u
- Theo quốc gia: https://iptv-org.github.io/iptv/countries/vn.m3u (Việt Nam)
