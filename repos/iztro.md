# iztro — GitHub Repo

## TL;DR
Thư viện JS/TS nhẹ tính lá số Tử Vi Đẩu Số (Zi Wei Dou Shu), output sẵn tiếng Việt — build app/web tử vi cho người Việt không cần tự dịch thuật ngữ. 3,830⭐, MIT.

## Repo này dùng để làm gì
Nhập ngày sinh (dương hoặc âm lịch) + giờ sinh + giới tính → trả về toàn bộ dữ liệu lá số: 12 cung, chính tinh/phụ tinh, tứ hóa, đại hạn/tiểu hạn/lưu niên/lưu nguyệt/lưu nhật, can chi tứ trụ, con giáp, cung hoàng đạo... Điểm mạnh nhất so với các lib cùng loại: hỗ trợ sẵn 6 ngôn ngữ output gồm Trung giản thể, Trung phồn thể, Anh, Nhật, Hàn, và **tiếng Việt** — chỉ cần đổi 1 tham số locale, không cần tự dịch tên cung/sao.

## Setup từng bước
1. `npm install iztro -S` (hoặc yarn/pnpm)
2. Import và gọi hàm tạo lá số:
```ts
import { astro } from 'iztro';

// Theo dương lịch — locale 'vi-VN' trả tiếng Việt
const astrolabe = astro.bySolar('2000-8-16', 2, 'male', true, 'vi-VN');

// Theo âm lịch
const astrolabeLunar = astro.byLunar('2000-7-17', 2, 'male', false, true, 'vi-VN');
```
3. Đọc dữ liệu lá số: `astrolabe.palaces` (12 cung), `astrolabe.star('紫微')...` để truy vấn theo sao cụ thể
4. Muốn xem thử không cần code: vào https://ziwei.pub (bản online dùng chính lib này)
5. Có sẵn bản port cho ai không dùng JS: `iztro-py` (Python thuần, PyPI) hoặc `dart_iztro` (Flutter, build app mobile)

## Ví dụ thực tế
Kiểm tra cung Tài Bạch có Hóa Kỵ không (dùng cho web/app tử vi tự động luận giải):
```ts
import { astro } from 'iztro';

const astrolabe = astro.bySolar('1995-3-10', 4, 'female', true, 'vi-VN');
const taiBach = astrolabe.palace('财帛'); // truy theo tên cung gốc Trung, output vẫn ra tiếng Việt
console.log(taiBach.majorStars); // danh sách chính tinh tại cung này, tên đã dịch tiếng Việt
```

Áp vào AI Vibe Toolkit: ghép `iztro` (tính lá số) + Claude/Hermes (luận giải nội dung) → tool tự tạo lá số + viết bài tử vi cá nhân hoá cho content TikTok/YouTube kiểu "tử vi tuần này của 12 con giáp".

## Lưu ý / Lỗi thường gặp
- Bản dịch tiếng Anh tác giả tự ghi rõ là dịch ý chứ chưa chuẩn hoá thuật ngữ — tiếng Việt cũng nên tự test kỹ tên cung/sao trước khi đưa vào sản phẩm thật, vì cộng đồng dịch theo kiểu PR tự nguyện, không phải bản dịch chuyên gia tử vi kiểm duyệt.
- Tử Vi Đẩu Số có nhiều phái khác nhau (cách tính tứ hóa, độ sáng sao khác nhau giữa phái) — từ bản v2.3.0 có thêm config + plugin để chỉnh theo phái mình muốn, không mặc định đúng 100% với mọi trường phái.
- Lib chỉ tính toán lá số (structured data), KHÔNG có sẵn phần luận giải bằng văn — muốn ra bài viết/luận giải phải tự ghép thêm LLM (Claude) đọc dữ liệu lá số rồi viết.
- Đây là chủ đề văn hoá/giải trí, không phải khoa học chính xác — nếu làm content/app nên có disclaimer rõ ràng, tránh để người dùng hiểu nhầm là dự đoán chắc chắn.

## Đánh giá cá nhân
- Điểm mạnh: nhẹ, doc đầy đủ (docs.iztro.com), API rõ ràng kiểu chain-call, đã có sẵn port Python/Flutter cho ai không dùng JS, và quan trọng nhất — output tiếng Việt built-in, tiết kiệm cả công đoạn dịch thuật ngữ Hán-Việt phức tạp.
- Điểm yếu: chỉ là lib tính toán, tự thân không tạo ra nội dung luận giải; cần kết hợp thêm LLM mới ra sản phẩm hoàn chỉnh.
- Có nên dùng: 8/10 — base tốt nhất hiện tại để build bất kỳ sản phẩm tử vi nào cho thị trường Việt Nam.

## Link
- Repo: https://github.com/SylarLong/iztro
- Docs: https://docs.iztro.com
- Demo online: https://ziwei.pub
- Bản Python: https://pypi.org/project/iztro-py/
- Bản Flutter: https://github.com/EdwinXiang/dart_iztro
