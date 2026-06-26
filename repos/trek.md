# TREK — GitHub Repo

## TL;DR
Self-hosted trip planner với real-time collaboration, interactive maps, budget tracker, packing lists, PWA support — alternative mã nguồn mở của WanderLog. 6.6K stars. Perfect cho travel brand như ABTRIP/Tano.

## Repo này dùng để làm gì
WanderLog, TripIt, Google Travel — các tool plan trip đều lock data trên server của họ. TREK cho phép:
- Self-host trên VPS riêng — data hoàn toàn của mày
- Real-time collaboration: nhiều người cùng edit trip plan
- Interactive maps tích hợp
- Budget tracker: track chi phí theo từng hạng mục
- Packing list: checklist theo chuyến đi
- PWA: cài như app trên điện thoại, dùng offline được
- SSO: đăng nhập qua Google/email

Cho travel brand: deploy riêng cho khách hàng dùng — white-label hoàn toàn.

## Setup từng bước
```bash
# Option 1: Docker (nhanh nhất)
git clone https://github.com/mauriceboe/TREK
cd TREK

# Config environment
cp .env.example .env
# Edit .env: DB connection, JWT secret, Google Maps API key

# Chạy với Docker Compose
docker-compose up -d

# Truy cập: http://localhost:3000
```

```bash
# Option 2: Manual setup
# Frontend (Next.js)
cd frontend
npm install
npm run build
npm start

# Backend (Node.js)
cd backend
npm install
npm run migrate  # setup database
npm start
```

**Cần có:**
- PostgreSQL (hoặc dùng Docker)
- Google Maps API key (cho interactive maps)
- SMTP config (cho email notifications)

## Ví dụ thực tế
**Use case cho ABTRIP/Tano:**
1. Deploy TREK trên VPS
2. White-label: đổi logo, màu brand
3. Khách đặt tour → tự lên kế hoạch chi tiết trên TREK platform của mày
4. Guide và khách cùng edit real-time: thêm điểm dừng, adjust budget, check packing list
5. Export itinerary thành PDF gửi cho khách

Thay vì dùng Google Docs hay WanderLog bên ngoài — mày có platform riêng, branded.

## Lưu ý / Lỗi thường gặp
- Google Maps API key cần bật: Maps JavaScript API, Places API, Directions API
- Production cần setup HTTPS (Let's Encrypt) — không dùng HTTP cho auth
- Database backup quan trọng — setup cronjob backup PostgreSQL hàng ngày
- PWA cache có thể stale — hướng dẫn user clear cache khi update version mới

## Đánh giá cá nhân
- Điểm mạnh: Self-hosted = data privacy; real-time collab; PWA offline; feature set đầy đủ cho travel; code clean, TypeScript
- Điểm yếu: Cần VPS + setup time; Google Maps API tốn tiền nếu traffic lớn; community còn nhỏ so với WanderLog
- Có nên dùng không: **8.5/10** — Rất phù hợp cho travel brand muốn có planning tool branded riêng. Setup một lần, dùng mãi. Không cần trả subscription WanderLog Pro.

## Link
- Repo: https://github.com/mauriceboe/TREK
- Demo: Xem screenshots trong README
- Topics: travel-planner, self-hosted, pwa, real-time, collaborative
