# RuView — GitHub Repo

## TL;DR
Biến WiFi thường thành hệ thống "nhìn xuyên tường": detect người, đo nhịp thở/tim, track chuyển động — không cần camera, không cần wearable. Chỉ cần WiFi + ESP32. 74K+ sao.

## Repo này dùng để làm gì
RuView khai thác tín hiệu WiFi (CSI - Channel State Information) để cảm nhận không gian vật lý. Khi người đi qua, thở, hay cử động — tín hiệu WiFi bị phản chiếu và thay đổi. RuView phân tích những thay đổi này để:

- **Presence detection**: có người trong phòng hay không (không cần camera)
- **Vital signs**: đo nhịp thở và nhịp tim passively, không cần đeo gì
- **Motion tracking**: track chuyển động qua tường
- **Pose estimation**: DensePose từ WiFi signal

Tích hợp native với: Home Assistant, Apple Home/HomePod, Google Home, Amazon Alexa, Matter.

## Setup từng bước

### Hardware cần
- ESP32 board (~$5-10) — flash firmware của RuView
- Router WiFi thường (không cần đặc biệt)

### Software setup
```bash
git clone https://github.com/ruvnet/RuView.git
cd RuView

# Install dependencies
npm install

# Flash ESP32 firmware
npm run flash-esp32

# Start server
npm start
```

### Kết nối Home Assistant
```bash
# Chạy với MQTT flag
./ruview --mqtt mqtt://homeassistant.local:1883

# RuView tự announce qua MQTT Discovery
# Hiện lên trong HA như sensor thông thường
```

## Ví dụ thực tế
**Smart home**: Phát hiện có người về nhà → bật đèn, điều hòa — không cần motion sensor hay camera. Phát hiện người già ngã trong phòng → alert ngay.

**Sleep tracking**: Đặt ESP32 cạnh giường → đo nhịp thở suốt đêm → xem dashboard sáng hôm sau. Không đeo gì cả.

**Security**: Phát hiện có người trong nhà khi đang đi vắng — ngay cả khi họ đứng im (vì vẫn thở).

## Lưu ý / Lỗi thường gặp
- ESP32 phải đặt đúng vị trí để coverage tốt (thường góc phòng)
- Accuracy của vital signs phụ thuộc vào khoảng cách và vật cản
- Nhiều thiết bị WiFi trong nhà có thể gây nhiễu
- Vẫn là research-grade cho một số tính năng (pose estimation qua tường còn hạn chế)
- Cần có kiến thức cơ bản về embedded/IoT để setup

## Đánh giá cá nhân
- Điểm mạnh: Concept cực kỳ ấn tượng, privacy-friendly (không camera), tích hợp tốt với smart home, hardware rẻ
- Điểm yếu: Setup phức tạp, accuracy chưa bằng dedicated sensors, vẫn cần calibration, doc còn sparse ở một số phần
- Có nên dùng không: **7/10** — Nếu mày thích IoT và muốn thứ gì đó thật sự cool để build, đây là project đáng deep dive. Không phải cho người mới.

## Link
- Repo: https://github.com/ruvnet/RuView
- Homepage: https://cognitum.one/seed
- Home Assistant docs: https://github.com/ruvnet/RuView/blob/main/docs/integrations/home-assistant.md
