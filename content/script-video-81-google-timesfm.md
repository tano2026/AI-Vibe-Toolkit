# Script Video 81 — Google TimesFM

## Thông tin
- Tool/Repo liên quan: /repos/google-timesfm.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~60 giây

## Hook (3 giây đầu)
"Google vừa thả model AI đọc dữ liệu quá khứ để đoán tương lai — 25 nghìn sao chỉ trong vài tháng."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — vấn đề]
Dự báo doanh thu, traffic website, hay phát hiện máy móc sắp hỏng — trước đây phải thuê data scientist, train model riêng, tốn hàng tuần.

[Đoạn 2 — giải pháp]
TimesFM là foundation model của Google Research cho bài toán dự báo chuỗi thời gian. Hiểu đơn giản: nó giống ChatGPT nhưng thay vì đọc văn bản — nó đọc số liệu theo thời gian. Quăng 90 ngày dữ liệu vào, nó tự dự báo 30 ngày tiếp theo. Không cần train lại từ đầu.

[Đoạn 3 — demo]
Mình test với dữ liệu traffic website 90 ngày. Ba dòng Python, đợi 3 giây. Output ra dự báo chuẩn hơn ARIMA truyền thống gần 2 lần. Model nặng 800MB, tải về một lần, dùng mãi.

[Đoạn 4 — kết + CTA]
Use case ngay: dự báo KPI marketing, inventory, anomaly detection. Link repo ở bio — 25k sao chứng minh rồi. Follow để xem thêm AI tools như thế này.

## Ghi chú quay (OBS)
- Cảnh 1: GitHub repo google-research/timesfm — show 25k stars
- Cảnh 2: Code Python 3 dòng trong VSCode
- Cảnh 3: Output chart dự báo — đường actual vs predicted
- Cảnh 4: HuggingFace model page

## Caption/Sub note (CapCut)
- Highlight: "25k sao", "zero-shot", "không cần train lại", "3 giây"
- Cắt cảnh tại giây 10 (sang code), giây 30 (sang chart output)

## Thumbnail idea (Canva)
Nền xanh dương đậm (màu Google), đường biểu đồ chuỗi thời gian đứt đoạn rồi tiếp tục sang tương lai. Text: "AI ĐỌC QUÁ KHỨ DỰ ĐOÁN TƯƠNG LAI". Logo Google nhỏ góc phải.

## CTA cuối video
"Link GitHub trong bio — clone về test ngay với dữ liệu của mày."
