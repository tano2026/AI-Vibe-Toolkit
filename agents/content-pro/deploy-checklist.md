# Deploy Checklist — Content Pro

Checklist trước khi giao Content Pro vận hành thật cho 1 brand/kênh cụ thể.

## Trước khi bung

- [ ] Đã đọc `content-brand-playbooks.md` — brand này có sẵn playbook chưa? Nếu chưa, cần research insight khách hàng trước (không suy đoán)
- [ ] Đã xác nhận có insight khách hàng thật (từ `primary-research-design`/`social-listening-research`) hoặc dữ liệu bán hàng — không xây Pillar trên suy đoán thuần
- [ ] Xác nhận skill chiến thuật cần dùng đã sẵn sàng (viral-hooks, content-engine, brand-voice/personal-voice tương ứng brand)
- [ ] Xác nhận `fact-checker` sẵn sàng cho content có claim (giá, quy định, số liệu)

## Bung lần đầu

- [ ] Chạy `content-pillar-cluster-architecture` — ra khung Pillar/Cluster đầu tiên
- [ ] Chạy `content-strategy-review-gate` — 5 câu hỏi, PASS hết mới đi tiếp
- [ ] Xác định rõ ai đảm nhiệm vai trò nào trong `editorial-workflow-quality-gates` (Research/Brief/Draft/Review/Publish) — không để 1 người vừa viết vừa tự duyệt nếu tránh được
- [ ] Dựng tracker (Airtable/Sheet) theo dõi trạng thái content qua từng gate
- [ ] Thiết lập template checklist phân phối (`content-distribution-system`) cho brand này

## Test case đầu tiên (bắt buộc trước khi mở rộng)

- [ ] Chạy thử toàn bộ pipeline với 1 content thật (không phải giả lập)
- [ ] Đo: thời gian từ Research tới Publish, content có bị lệch brief không, gate nào hay vướng nhất
- [ ] Điều chỉnh quy trình theo thực tế phát sinh (vd rút gọn bước nếu quá chậm, không bỏ hẳn bước)

## Vận hành liên tục

- [ ] Lên lịch audit refresh content cũ (mặc định 6-8 tháng, brand Travel/Airport rút ngắn còn 3-4 tháng do thông tin dễ đổi)
- [ ] Review lại khung Pillar/Cluster mỗi 3-6 tháng qua `content-strategy-review-gate` — khung cũ có còn đúng không
- [ ] Cập nhật `content-brand-playbooks.md` khi có insight mới về brand đó

## Không làm (out of scope hiện tại)

- Content Pro KHÔNG tự động đăng bài — vẫn cần công cụ đăng thật (Postiz/thủ công)
- Content Pro KHÔNG thay thế pipeline sản xuất đã có (Trùm Sân Bay 9-agent, yt-cashcow) — chỉ bổ sung tầng chiến lược bao quanh
- Chưa có dual-review độc lập — content chiến lược cực lớn có thể cần thêm bước này trong tương lai (xem ARCHITECTURE.md, mục "Điểm mở rộng")
