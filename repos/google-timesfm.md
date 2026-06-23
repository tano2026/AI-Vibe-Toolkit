# Google TimesFM — GitHub Repo

## TL;DR
Model dự báo chuỗi thời gian (time-series forecasting) do Google Research phát triển, 25k sao. Đọc dữ liệu quá khứ để dự đoán tương lai — không cần train lại từ đầu.

## Repo này dùng để làm gì
TimesFM là foundation model cho bài toán dự báo số liệu theo thời gian. Hiểu nôm na: thay vì phải train model riêng để dự báo doanh thu tháng tới, lượt truy cập website, hay tiêu thụ điện — mày chỉ cần quăng dữ liệu lịch sử vào, TimesFM tự suy ra pattern và dự báo tiếp.

Nó hoạt động như ChatGPT nhưng cho số liệu: được pretrain trên hàng tỷ điểm dữ liệu time-series từ nhiều ngành, rồi có thể zero-shot predict cho domain mới.

Use case thực tế:
- Dự báo traffic website theo giờ/ngày
- Dự đoán nhu cầu sản phẩm cho inventory
- Phát hiện anomaly (máy móc bất thường, spike traffic)
- Forecasting doanh thu / KPI marketing

## Setup từng bước
1. Cài qua pip:
```bash
pip install timesfm
```
2. Load model (tự download weights):
```python
import timesfm

tfm = timesfm.TimesFm(
    hparams=timesfm.TimesFmHparams(
        backend="gpu",  # hoặc "cpu"
        per_core_batch_size=32,
        horizon_len=128,
    ),
    checkpoint=timesfm.TimesFmCheckpoint(
        huggingface_repo_id="google/timesfm-1.0-200m-pytorch"
    ),
)
tfm.load_from_checkpoint(checkpoint=timesfm.TimesFmCheckpoint(
    huggingface_repo_id="google/timesfm-1.0-200m-pytorch"
))
```
3. Dự báo:
```python
import numpy as np

# Dữ liệu lịch sử: mảng số, ví dụ doanh thu 90 ngày qua
historical_data = np.array([...])  # shape: (batch, time_steps)

forecast_input = [historical_data]
freq = [0]  # 0=high freq (hourly/daily), 1=medium, 2=low

point_forecast, experimental_quantile_forecast = tfm.forecast(
    forecast_input,
    freq=freq,
)
print(point_forecast)  # Dự báo 128 bước tiếp theo
```

## Ví dụ thực tế
Dữ liệu: 90 ngày lượt truy cập website (dạng array số)
→ TimesFM dự báo 30 ngày tiếp theo
→ So sánh với actual: sai số MAPE ~8% — tốt hơn ARIMA truyền thống ~15%

Thời gian chạy: ~3 giây cho một chuỗi (CPU), ~0.3 giây (GPU).

## Lưu ý / Lỗi thường gặp
- Model 200M nặng ~800MB, lần đầu download mất thời gian
- Cần JAX hoặc PyTorch — chọn backend phù hợp khi install: `pip install timesfm[jax]` hoặc `pip install timesfm[torch]`
- Dữ liệu cần clean (không có NaN), nếu có gap cần interpolate trước
- Lỗi CUDA out of memory → giảm `per_core_batch_size`
- Zero-shot tốt nhưng fine-tune trên data domain cụ thể sẽ cho kết quả chính xác hơn

## Đánh giá cá nhân
- Điểm mạnh: Zero-shot cực mạnh, không cần data nhiều để bắt đầu dự báo. Google Research đứng sau nên research quality cao.
- Điểm yếu: Nặng (800MB model), không phải tool no-code — cần biết Python. Không có UI, phải tự build dashboard.
- Có nên dùng không: 8/10 — Nếu mày đang làm gì liên quan đến analytics, forecasting, hay build tool AI cho business — đây là foundation model tốt nhất hiện tại cho time-series. Dùng kết hợp với Streamlit hoặc Grafana để visualize.

## Link
- Repo: https://github.com/google-research/timesfm
- Model HuggingFace: https://huggingface.co/google/timesfm-1.0-200m-pytorch
- Paper: arxiv.org/abs/2310.10688
