---
name: statistical-analysis
description: >
  Phân tích số liệu thực tế bằng code (pandas, scipy, statsmodels). Xử lý dataset,
  tìm trend, kiểm định giả thuyết, tính correlation, detect outliers.
  Trigger khi user upload data file hoặc có dataset cần analyze thật.
  Trigger với: "phân tích data", "chạy thống kê", "có file excel này", "trend của số liệu",
  "correlation", "có ý nghĩa thống kê không", "analyze this data", "run stats".
---

# Statistical Analysis — Xử Lý Số Liệu Thật

---

## Quy trình chuẩn

### Bước 1 — Explore data trước (EDA)
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")  # hoặc read_excel, read_json

# Hiểu shape
print(df.shape)           # bao nhiêu rows x columns
print(df.dtypes)          # kiểu dữ liệu
print(df.isnull().sum())  # missing values ở đâu
print(df.describe())      # stats cơ bản: mean, std, min, max, quartiles

# Distribution check
df.hist(figsize=(12,8))
plt.tight_layout()
```

### Bước 2 — Clean data
```python
# Drop duplicates
df = df.drop_duplicates()

# Handle missing values (chọn 1 trong 2)
df = df.dropna(subset=['critical_column'])    # drop nếu cột quan trọng thiếu
df['other_col'] = df['other_col'].fillna(df['other_col'].median())  # fill với median

# Fix outliers (IQR method)
Q1 = df['value'].quantile(0.25)
Q3 = df['value'].quantile(0.75)
IQR = Q3 - Q1
df_clean = df[(df['value'] >= Q1 - 1.5*IQR) & (df['value'] <= Q3 + 1.5*IQR)]
```

### Bước 3 — Analyze theo mục tiêu

**Trend analysis:**
```python
from scipy import stats

# Linear trend
x = np.arange(len(df))
slope, intercept, r_value, p_value, std_err = stats.linregress(x, df['metric'])
print(f"Trend: {slope:+.2f}/period, R²={r_value**2:.2f}, p={p_value:.4f}")
# p < 0.05 → trend có ý nghĩa thống kê
```

**Correlation:**
```python
# Pearson (linear relationship, continuous data)
corr_matrix = df[['var1', 'var2', 'var3']].corr()
print(corr_matrix)
# |r| > 0.7: strong, 0.4-0.7: moderate, <0.4: weak
```

**Compare 2 groups (A/B test):**
```python
from scipy.stats import ttest_ind, mannwhitneyu

group_a = df[df['group']=='A']['metric']
group_b = df[df['group']=='B']['metric']

# Nếu data normal → t-test
t_stat, p_value = ttest_ind(group_a, group_b)
# Nếu data skewed → Mann-Whitney
u_stat, p_value = mannwhitneyu(group_a, group_b)

print(f"A: {group_a.mean():.2f} vs B: {group_b.mean():.2f}, p={p_value:.4f}")
print("Có ý nghĩa thống kê" if p_value < 0.05 else "Chưa có ý nghĩa thống kê")
```

**Time-series forecast (đơn giản):**
```python
from statsmodels.tsa.holtwinters import ExponentialSmoothing

model = ExponentialSmoothing(df['value'], trend='add', seasonal='add', seasonal_periods=12)
fitted = model.fit()
forecast = fitted.forecast(steps=6)  # dự báo 6 kỳ tới
print(forecast)
```

**Nếu có Google TimesFM (từ kho):**
```python
# Dùng cho time-series không cần fine-tune, zero-shot
import timesfm
tfm = timesfm.TimesFm(
    hparams=timesfm.TimesFmHparams(backend="cpu", per_core_batch_size=32, horizon_len=6),
    checkpoint=timesfm.TimesFmCheckpoint(huggingface_repo_id="google/timesfm-1.0-200m")
)
forecast_df = tfm.forecast_on_df(df, freq="M", value_name="value", num_jobs=-1)
```

---

## Interpret results — đừng chỉ đưa số

```
SAI: "p-value = 0.03"
ĐÚNG: "p-value = 0.03, thấp hơn threshold 0.05 → sự khác biệt này không phải ngẫu nhiên,
       group A thực sự perform tốt hơn group B với độ tin cậy 95%"

SAI: "Correlation = 0.72"
ĐÚNG: "Correlation = 0.72 — strong positive correlation giữa X và Y: khi X tăng thì Y
       có xu hướng tăng theo. Tuy nhiên, correlation ≠ causation — không thể kết luận
       X gây ra Y mà không có thêm evidence"

SAI: "Forecast: 1200, 1350, 1400..."
ĐÚNG: "Dự báo cho thấy growth tiếp tục nhưng đang decelerate (tốc độ tăng chậm dần).
       Confidence interval rộng → uncertainty cao sau tháng 4. Recommend review lại
       với data thực tế sau Q1"
```

---

## Khi nào cần Google TimesFM vs statsmodels

```
statsmodels ARIMA:    Dataset nhỏ (<1000 rows), cần explain được model
Google TimesFM:       Dataset lớn, không muốn tune hyperparameters, zero-shot is fine
scikit-learn:         Classification / clustering / regression với features
pandas alone:         Đủ cho aggregation, pivot, moving average cơ bản
```
