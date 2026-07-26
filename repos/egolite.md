# Egolite (ego lite) — GitHub Repo

## TL;DR
Trình duyệt Chromium của citrolabs, thiết kế để người và AI agent (Claude Code, Codex, Cursor...) dùng chung — mỗi agent chạy trong 1 "Space" riêng biệt, không giành tab với người dùng, kế thừa thẳng login/cookie/extension có sẵn. Nhanh hơn 2.5x so với agent-browser (Vercel) trên task phức tạp, ít tốn token hơn hẳn.

## Repo này dùng để làm gì
Khác các framework automation trình duyệt kiểu Browser-Use hay agent-browser (chỉ là thư viện, agent phải điều khiển 1 trình duyệt tách riêng, login không mang theo được), ego lite LÀ 1 trình duyệt thật, người dùng hàng ngày, agent chạy song song trong Space riêng của trình duyệt đó — tự động kế thừa cookie/session đăng nhập sẵn, không phải đăng nhập lại từ đầu. Cách agent điều khiển: viết code JavaScript gọi thẳng các hàm (`snapshot`, `fill`, `click`, `wait`, `navigate`, `capture`) qua `ego-browser`, thay vì kiểu CLI gọi từng lệnh rồi đọc kết quả — nên xử lý task nhiều bước nhanh hơn, ít lần gọi tool hơn.

## Setup từng bước
1. Tải app (hiện chỉ có bản macOS, Windows/Linux đang nằm trong roadmap):
```
Apple Silicon: https://cdn.ego.app/setup/macos/arm64/egolite.dmg
Intel: https://cdn.ego.app/setup/macos/x64/egolite.dmg
```
2. Cài xong, mở app — nó tự hỏi có muốn "migrate Chrome data" không. Chọn có để agent kế thừa luôn login/cookie/bookmark cũ.
3. App cài đặt sẽ tự động: cài trình duyệt + helper `ego-browser` + ghi skill vào mọi agent CLI có sẵn trên máy (Claude Code, Codex...).
4. Trong agent CLI (vd Claude Code), gọi trực tiếp:
```
/ego-browser follow @ego_agent on x.com for me
```
5. Agent tự nhận skill `ego-browser`, mở trang trong Space riêng, đọc Snapshot trang, thao tác, báo kết quả — tab của người dùng không bị đụng tới.

## Ví dụ thực tế
Đúng vào đúng chỗ trống trong `agents/shorts-affiliate-system` — bước "Affiliate Research" hiện dựa vào `/affiliate research-programs` (search text-based), nhưng nhiều chương trình affiliate yêu cầu **đăng nhập vào dashboard đối tác để lấy link tracking thật** (không có API công khai). Đây là việc trình duyệt agent làm tốt hơn search: mở dashboard affiliate program đã login sẵn (kế thừa session), tự lấy link tracking, dán vào storyboard — thay vì Nobitano tự làm tay từng chương trình.

## Lưu ý / Lỗi thường gặp
- **Chỉ chạy trên macOS** hiện tại — theo memory, Nobitano có máy Windows local (không phải Mac) và VPS Tencent Cloud Ubuntu — nghĩa là KHÔNG cài được ở 2 môi trường chính đang dùng, chỉ dùng được nếu có sẵn máy Mac riêng. Windows/Linux còn nằm ở "roadmap", chưa có ngày ra mắt cụ thể.
- "Experience accumulation" (agent tự nhanh hơn qua thời gian dùng) được ghi là "coming soon" — chưa có ở bản hiện tại, đừng kỳ vọng ngay.
- Repo chỉ 47 sao, còn khá non trẻ (release đầu tiên tháng 6/2026) — cộng đồng nhỏ, ít case study thực chiến để tham khảo khi gặp lỗi.
- Data trình duyệt lưu local trên máy, chỉ ghi nhận có opt-in Chrome migration hay không — không phải rủi ro privacy lớn, nhưng cũng đồng nghĩa không có bản cloud/headless để chạy trên VPS.

## Đánh giá cá nhân
- Điểm mạnh: giải đúng bài toán "agent cần login mà không muốn đăng nhập lại", tốc độ + tiết kiệm token đo được rõ ràng so với agent-browser (Vercel), MIT license.
- Điểm yếu: macOS-only là rào cản lớn nhất với hạ tầng hiện tại của Nobitano (Windows + VPS Linux, không phải Mac), dự án còn non.
- Có nên dùng: 5/10 cho hạ tầng hiện tại (không cài được) — sẽ lên 8/10 ngay khi Windows/Linux ra mắt, nên theo dõi roadmap thay vì bỏ qua hẳn.

## Link
- Repo: https://github.com/citrolabs/ego-lite
- Docs: https://lite.ego.app/document/
- Roadmap: https://lite.ego.app/roadmap

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# KHÔNG áp dụng trực tiếp — ego lite là app desktop macOS, không có API server để Hermes
# (chạy trong OpenClaw trên VPS Linux) gọi qua urllib.request. Nếu cần dùng, phải chạy
# trên 1 máy Mac riêng, không phải qua Hermes trên VPS.
```

### OpenClaw
```
Không route được từ OpenClaw (chạy trên VPS Linux) — ego lite yêu cầu app desktop macOS
cài trực tiếp trên máy, không phải service network gọi từ xa được.
```

### Antigravity
```
Không deploy được lên VPS Tencent Cloud (Ubuntu) — chờ bản Linux theo roadmap chính thức
trước khi cân nhắc đưa vào hạ tầng agent 24/7.
```
> ⚠️ Đây là công cụ dùng TAY trên máy Mac riêng (nếu có), không phải thứ gắn được vào hệ agent
> 24/7 hiện tại của Nobitano cho tới khi có bản Windows/Linux.
