# Ví dụ dựng bằng chính CLI của Agent Factory

> Hai ví dụ dưới đây do `tools/agent_factory.py` sinh ra với `tools/thu_kho.py` thật. Không sửa tay sau khi sinh (trừ README này, `KET-QUA-KIEM.md`, `KET-QUA-HANH-VI.md` và `KET-QUA-HANH-VI-LAI.md`).
> Trạng thái chung: **chưa duyệt, chưa spike, chưa chạy với credential thật.** Xem `KET-QUA-KIEM.md` để biết kết quả `kiem` thật và những chỗ sinh ra còn lệch.

| Thư mục | Loại | Ghi chú |
|---|---|---|
| `facebook-channel-agent/` | Agent riêng lẻ | Đăng bài và trả lời bình luận Facebook, tự chủ L1, vessel Hermes, chế độ `draft_only` hai tuần đầu |
| `trum-san-bay-opc/` | OPC | **DEMO dựng từ thiết kế NHÁP chưa duyệt** (`agents/trum-san-bay/OPC-DESIGN-NOTES.md`, dừng sau Phần 2 trên 5 phần). Không phải kế hoạch triển khai |

## Hồ sơ kiểm

| File | Nội dung |
|---|---|
| `KET-QUA-KIEM.md` | Đầu ra thật của `kiem` và `ban-giao` trên hai ví dụ (đã sinh lại 2026-10-19 sau khi vá khuôn) |
| `KET-QUA-HANH-VI.md` | Lượt kiểm hành vi bằng mô phỏng lần đầu (45 tình huống) và các lỗ hổng thiết kế tìm được |
| `KET-QUA-HANH-VI-LAI.md` | Chạy lại 9 tình huống của facebook-channel-agent trên tài liệu đã vá (vẫn là mô phỏng trên giấy) |

Hai ví dụ này đã được SINH LẠI bằng CLI ngày 2026-10-19 sau khi vá khuôn (dữ liệu nhạy cảm của khách, câu xác nhận tạm, fail-closed, cổng cho tin gửi đối tác, trả lời công khai nhất quán, kiểm chú thích affiliate). Ngày trong hồ sơ vì thế là 2026-10-19.

## Lệnh đã dùng

```
python tools/agent_factory.py moi-agent --slug facebook-channel-agent \
  --job "đăng bài và trả lời bình luận trên một Facebook Page → bản nháp bài đăng và bản nháp trả lời bình luận, chỉ đăng sau khi duyệt → chủ Page (CEO) duyệt" \
  --kha-nang social-media,content-writing,customer-support --tu-chu L1 --vessel hermes --kenh facebook \
  --khong-lam "...;..." --kpi "...=|cách đo|nguồn số" --banner "DEMO ..." --dau-ra agents/agent-factory/examples

python tools/agent_factory.py moi-opc --slug trum-san-bay-opc --thuong-hieu "Trùm Sân Bay" \
  --doanh-thu affiliate,dich-vu --kenh facebook,zalo,instagram --goi-mo-rong tai-chinh,doi-tac \
  --kha-nang-them ticketing-aviation --mo-ta "..." --banner "DEMO ..." --dau-ra agents/agent-factory/examples
```

Dựng lại thì dùng `--ghi-de` (chỉ ghi đè được thư mục do công cụ tạo). Dựng lại ở ngày khác sẽ đổi ngày trong hồ sơ và có thể đổi mục kho nếu thủ kho hoặc catalog đã đổi.

## Chưa làm

Không file nào ở đây đã được người điền. Tất cả ô `CHƯA CÓ — hỏi CEO` (chủ sở hữu, bộ nhận diện, bảng giá, danh sách đối tác, pháp nhân, cổng thanh toán, ngưỡng tự khoá) còn nguyên.
