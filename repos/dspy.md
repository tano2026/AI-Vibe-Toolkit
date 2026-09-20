# dspy — GitHub Repo

## TL;DR
Lập trình hoá prompt thay vì tự tay tinh chỉnh — để tính năng AI không còn dễ vỡ khi đổi model. 37,7k sao, từ Stanford NLP.

## Repo này dùng để làm gì
Framework tối ưu prompt và pipeline LLM tự động — thay vì viết tay từng câu prompt rồi thử-sai, DSPy để hệ thống tự tối ưu prompt dựa trên ví dụ + metric đánh giá. Đổi model (GPT sang Claude) không phải viết lại prompt từ đầu.

## Setup từng bước
1. Cài: `pip install dspy-ai`
2. Định nghĩa "signature" (input/output mong muốn, không phải prompt thô):
```python
import dspy

class ClassifyDeal(dspy.Signature):
    """Chấm điểm deal theo fit và intent"""
    deal_info = dspy.InputField()
    score = dspy.OutputField(desc="điểm 0-10")

classifier = dspy.Predict(ClassifyDeal)
```
3. DSPy tự tối ưu prompt thật sự gửi cho model dựa trên ví dụ train đưa vào (`dspy.teleprompt`)

## Ví dụ thực tế
Skill `deal-scoring-forecast-discipline` đang viết tay ngưỡng fit×intent — nếu muốn tự động tối ưu cách chấm điểm dựa trên deal thật đã thắng/thua trước đó (thay vì đoán ngưỡng), DSPy cho phép train pipeline chấm điểm tự cải thiện theo data thật, không cần tự tay chỉnh prompt mỗi lần sai.

## Lưu ý / Lỗi thường gặp
- Cần dữ liệu ví dụ (train set) để tối ưu — không có data thật thì DSPy không phát huy được lợi thế so với viết tay
- Đường cong học khá dốc — khái niệm "signature/module/optimizer" khác hẳn cách viết prompt thông thường, cần thời gian làm quen
- Không hợp cho task 1 lần — giá trị thật khi có pipeline chạy lặp lại nhiều, cần ổn định qua thời gian

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng vấn đề "prompt dễ vỡ khi đổi model" — từ Stanford, có nghiên cứu nền tảng vững
- Điểm yếu: cần đầu tư thời gian học + cần data để train, không phải giải pháp nhanh
- Có nên dùng: 7/10 — đáng thử cho pipeline chạy lặp lại nhiều (deal scoring, content classification), không cần cho task chạy 1 lần

## Link
- Repo: https://github.com/stanfordnlp/dspy
