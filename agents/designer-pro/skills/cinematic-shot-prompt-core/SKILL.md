---
name: cinematic-shot-prompt-core
description: >
  Công thức viết prompt ảnh/video AI theo ngôn ngữ điện ảnh (cỡ cảnh, góc máy,
  chuyển động máy, ánh sáng, màu) — THUẦN, không gắn brand nào, không phụ thuộc
  công cụ nào. Dùng khi cần clip/ảnh trông "có đạo diễn" thay vì prompt chung chung.
  Chạy được bằng text thuần trên mọi generator (Higgsfield, Veo, Kling, Seedance...).
---

# Cinematic Shot Prompt (Core — không gắn brand)

> Trạng thái: công thức tổng hợp từ 3 nguồn đã đọc (xem `stacks/cinematic-techniques-ai-video.md`). **Chưa test trên generator thật** — chạy thử 3 clip rồi chấm trước khi coi là chuẩn.

## TL;DR
Mỗi prompt video = 1 shot, mô tả theo 6 phần cố định: **S**ubject → **C**ontext → **L**ens/khung hình → **C**amera motion → **A**tmosphere (ánh sáng) → **M**ood/màu. Một shot chỉ MỘT chuyển động máy chính. Muốn nhiều cảnh = nhiều shot, ghép sau.

## Khi nào dùng
- Làm clip mở đầu/chuyển cảnh/b-roll bằng AI cho video của ABTRIP, Tano, Wonder Mart
- Prompt cũ cho ra clip "phẳng", máy cứ lắc linh tinh, ánh sáng nhạt
- KHÔNG dùng cho ảnh poster/infographic có chữ (dùng `image-prompt-formula-core`)

## 6 phần (điền đủ, mỗi phần 1 câu ngắn)
| Phần | Hỏi gì | Ví dụ |
|---|---|---|
| Subject | Ai/cái gì, đang làm gì | "nữ nhân viên mặc đồng phục đẩy vali qua cổng ưu tiên" |
| Context | Ở đâu, lúc nào | "sảnh đi sân bay Nội Bài T1, sáng sớm" |
| Lens/khung | Cỡ cảnh + góc + ống kính | "medium shot, ngang tầm mắt, 35mm, nền mờ nhẹ" |
| Camera motion | MỘT chuyển động | "dolly in chậm" |
| Atmosphere | Nguồn sáng, hướng, độ cứng | "nắng ban mai xiên qua cửa kính, mềm" |
| Mood/màu | Cảm xúc + bảng màu | "ấm, tin cậy, tông vàng nhạt và xanh navy" |

## Từ vựng (rút gọn)
- **Cỡ cảnh:** extreme wide / wide / medium / close-up / extreme close-up
- **Góc máy:** ngang tầm mắt, low angle (nhân vật mạnh/to), high angle (nhỏ/yếu), overhead, POV, dutch angle (bất an)
- **Chuyển động máy:** dolly in/out, pan, tilt, crane up/down, orbit/arc, crash zoom, handheld, FPV drone, whip pan, hyperlapse/timelapse
- **Ánh sáng:** golden hour, soft window light, hard top light, backlight/rim light, neon
- **Chọn theo cảm xúc:** tin cậy/ấm → dolly in chậm + ánh sáng mềm; căng thẳng → handheld + sáng cứng; hoành tráng → crane/drone + wide; thân mật → close-up + nông sâu trường

## Quy tắc
1. MỘT chuyển động máy chính mỗi shot. Hai chuyển động đối nghịch (zoom in + dolly out) thường cho clip méo
2. Mô tả bằng từ cụ thể ("dolly in chậm"), không dùng "cinematic, epic, stunning" suông
3. Đặt tên thật cho nguồn sáng thay vì "lighting đẹp"
4. Với Higgsfield: dùng đúng TÊN PRESET camera của họ nếu có (tra trong tài liệu công cụ), vì công cụ nhận diện preset
5. Không nhờ AI vẽ chữ/logo trong clip — thêm bằng dựng hậu kỳ
6. Người thật cụ thể (nhân viên, khách): chỉ dùng ảnh mình có quyền sử dụng

## Ví dụ hoàn chỉnh (ABTRIP Fast Track)
> Nữ nhân viên mặc đồng phục xanh navy dẫn vị khách doanh nhân qua cổng ưu tiên. Sảnh đi sân bay Nội Bài T1, sáng sớm. Medium shot ngang tầm mắt, ống 35mm, nền mờ nhẹ. Dolly in chậm. Nắng ban mai xiên qua cửa kính, ánh sáng mềm. Tông ấm, tin cậy, vàng nhạt và xanh navy.

## Bảng lỗi hay gặp
| Lỗi | Nguyên nhân thường gặp | Sửa |
|---|---|---|
| Máy lắc/méo | 2+ chuyển động trong 1 prompt | Chỉ giữ 1 |
| Nhân vật biến dạng giữa clip | Shot quá dài/quá nhiều hành động | Chia thành 2 shot ngắn |
| Màu xỉn | Không nêu nguồn sáng/bảng màu | Điền Atmosphere + Mood |
| Chữ méo | Yêu cầu AI vẽ chữ | Bỏ chữ, thêm ở hậu kỳ |

## Cách kiểm chứng (PASS/FAIL)
Viết 3 prompt theo công thức + 3 prompt cũ chung chung, cùng subject, tạo trên cùng 1 generator, so cạnh nhau. PASS = ít nhất 2/3 cặp bản công thức tốt hơn rõ rệt (mày tự chấm). FAIL = ghi lại generator nào, lỗi gì rồi sửa công thức.
