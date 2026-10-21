# NHIỆM VỤ cho Antigravity: sửa và hoàn thiện trang tra cứu kho trên VPS

Bối cảnh: trang chạy ở `https://kho.43.156.72.127.sslip.io` (nginx, Basic Auth, HTTPS đều ổn). Trang trống vì lỗi dữ liệu, đã sửa trong `tools/build_kho_web.py` (các trường capability, vessel_fit, needs là chuỗi "a,b", trang cần danh sách; lỗi trình duyệt: `r._cap.map is not a function`).

## Mô hình
- **Trang web** = `/var/www/kho/index.html`, một file tĩnh, tự chứa dữ liệu. Ô tìm là JavaScript trong `tools/kho-web/template.html`, KHÔNG phải Thủ Kho và không có AI.
- **Thủ Kho (tra và gợi ý)** = `tools/thu_kho.py` (CLI Python, chạy offline) + `agents/thu-kho/` (system-prompt.md, README.md, EXAMPLES.md). Nó là công cụ và lời nhắc, chưa phải dịch vụ chạy sẵn. Chưa có bot nào nối nó với người dùng.
- Dữ liệu chung: `catalog/catalog.json` (919 mục, đã gắn nhãn hết).

## Việc 1 (làm ngay): đưa bản sửa lên VPS
1. `cd ~/ai-vibe-toolkit && git pull` (cần bản main có commit "sửa kiểu dữ liệu trang tra cứu").
2. `python3 tools/build_kho_web.py --out /var/www/kho`
3. Kiểm bằng trình duyệt tải lại mạnh (Ctrl+F5), đăng nhập `tano`: thấy "919 mục"; gõ `zalo` ra 3 mục đầu gồm "Zalo OA — Playbook..." và "Zalo Channel Connection Guide"; F12 không có lỗi đỏ. Dán kết quả.

## Việc 2: ô tìm quá chặt
Hiện ô tìm đòi khớp MỌI từ: "bot Zalo chăm sóc khách" ra 0 mục, trong khi "chăm sóc khách" ra 15 và "zalo chăm sóc" ra 3. Sửa trong `tools/kho-web/template.html` (hàm lọc theo từ khoá): bỏ từ phụ (bot, cần, muốn, làm, cho, giúp, và), xếp hạng theo số từ khớp, nếu không có mục khớp hết thì hiện mục khớp nhiều từ nhất. Giữ tìm không dấu. Kiểm: 5 câu thử trong tools/thu_kho.py `tim` và trên trang cho cùng mục đầu ở ít nhất 4/5 câu. Thêm test vào tools/tests/test_thu_kho.py nếu làm được, chạy `python -m pytest tools/tests -q`.

## Việc 3 (báo cáo trước khi làm): Thủ Kho trên VPS
1. Chạy thử trên VPS: `python3 tools/thu_kho.py tim "bot Zalo chăm sóc khách"` phải ra guide Zalo OA ở top 3. Dán kết quả.
2. Báo tao: Hermes và OpenClaw đang chạy ở máy nào, nạp `agents/thu-kho/system-prompt.md` thế nào. KHÔNG tự nối bot hay mở dịch vụ mới khi chưa được duyệt.

## Luật
- Không push thẳng vào main. Sửa xong tạo nhánh và báo, tao duyệt rồi mới gộp.
- Không đổi mật khẩu, không tắt auth_basic hay HTTPS, không đụng dịch vụ khác trên VPS.
- Lệnh lỗi thì dán nguyên văn, không đoán.
