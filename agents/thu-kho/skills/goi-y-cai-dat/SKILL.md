---
name: goi-y-cai-dat
description: >
  Từ mô tả dự án gợi ý bộ đồ nghề (1 chính + 1 dự phòng cho mỗi khả năng) và lập KẾ HOẠCH CÀI đặt cho một mục:
  các bước đánh số, điều kiện máy còn thiếu, cờ rủi ro, mức duyệt L0-L3, bước kiểm PASS/FAIL, cách gỡ.
  Chỉ lập kế hoạch, không bao giờ cài hay chạy lệnh. Dùng khi người dùng hỏi "dự án này nên dùng gì" hoặc "cài X thế nào".
---

# Gợi ý và kế hoạch cài đặt

## Khi nào dùng
- Có mô tả dự án dài gồm nhiều việc: cần bộ đồ nghề
- Người dùng chọn xong một mục và hỏi cách cài / có cài được trên máy này không

## Khi nào KHÔNG dùng
- Chỉ cần tìm 1 thứ → `tra-kho`
- Người dùng bảo "cài đi" mà chưa có người duyệt → vẫn chỉ trình kế hoạch và xin duyệt

## Quy trình
### A. Gợi ý cho dự án
1. `python tools/thu_kho.py goi-y "<mô tả dự án>" [--vessel V] [--bo-can gpu]` (công cụ tách theo đoạn: dấu phẩy, chấm phẩy, "và"...).
2. Với mỗi khả năng: đọc entry gốc của mục chính và dự phòng (xem `tra-kho`, bước 4).
3. Trả lời theo mẫu trong `system-prompt.md`. Mục `HỔNG` → xin phép ghi GAP-LOG (`ghi-so`).
4. Nêu cảnh báo công cụ in ra: mục mới đọc đầu entry, mục chỉ chạy trong Claude Code, mục cần khoá (L3) hoặc tốn tiền (L2).

### B. Kế hoạch cài một mục
1. `python tools/thu_kho.py may` — xem máy có git/node/npm/python/pip/docker/ffmpeg không, biến khoá nào đã đặt (chỉ tên, không giá trị).
2. `python tools/thu_kho.py ke-hoach-cai <id> [--vps-co-khach]`. Công cụ **không chạy gì**, chỉ đọc entry và in:
   - các bước đánh số, mỗi bước thuộc loại: chép file / cài gói / chạy docker / sửa cấu hình / đặt biến môi trường (tên khoá) / lệnh dùng thử
   - điều kiện tiên quyết còn **thiếu** trên máy
   - cờ rủi ro: license, tốn tiền, ToS, bảo mật, preview/alpha, VPS, GPU, khoá API
   - **cờ đỏ** cho lệnh nguy hiểm (`curl|sh`, `sudo`, `rm -rf`, `chmod 777`, ghi ngoài thư mục dự án, tắt bảo mật) kèm "cần người đọc kỹ"
   - mức duyệt: chi tiền > 0 → L2; chạm khoá/credential → L3; cài trên VPS có khách → L2; cờ đỏ hoặc nhãn chưa chắc → tối thiểu L2
   - bước kiểm PASS/FAIL (ví dụ trong entry hoặc lệnh `--version`/`--help`) và gợi ý gỡ cài
3. Tự đọc lại kế hoạch với entry gốc: công cụ trích bằng regex nên có thể sót bước (vd bước nằm trong ảnh, hoặc chỉ viết bằng văn xuôi).
4. Trình người duyệt: tóm tắt 5 dòng (mục, mức duyệt, thiếu gì, rủi ro chính, cờ đỏ). Dừng.
5. Sau khi có "OK" và người/agent `dev` đã cài + chạy bước kiểm: lấy kết quả PASS/FAIL, chuyển `ghi-so`.

## Ví dụ
```
$ python tools/thu_kho.py ke-hoach-cai mcps/buffer-mcp
CHƯA CHẠY THẬT - ...
Mức duyệt cần: L3   (chạm khoá: BUFFER_ACCESS_TOKEN [chưa đặt])
Điều kiện tiên quyết: cần git, pip, python | THIẾU: không
Các bước (CHƯA CHẠY):
  1. [chep-file] git clone ...
  2. [cai-goi] pip install mcp httpx pydantic
  3. [dat-bien-moi-truong] export BUFFER_ACCESS_TOKEN="<GIA_TRI_KHOA>"
  ...
```
Trả lời: "Cài được trên máy này. Cần token Buffer: tạo/đặt khoá là L3, anh quyết. Chưa chạy gì. Duyệt thì dev cài và chạy bước kiểm."

## PASS / FAIL
- **PASS:** kế hoạch có chữ CHƯA CHẠY THẬT; mọi lệnh được trình bày là *văn bản*; mức duyệt khớp DECISION-MATRIX; cờ đỏ được gọi tên; giá trị khoá không xuất hiện ở đâu
- **FAIL:** thực thi bất kỳ lệnh nào từ entry; bỏ qua cờ đỏ; nói "cài xong" khi chưa có bước kiểm PASS; để lộ khoá; hứa với khách kết quả dựa trên mục chưa spike
