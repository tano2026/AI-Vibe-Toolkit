# WanGP Kaggle — Video AI Miễn Phí Dùng T4 GPU Của Kaggle

**GitHub:** https://github.com/kayas881/WanGP-Kaggle
**Stars:** 10⭐ | **GPU:** Tesla T4 15GB (FREE từ Kaggle)
**Models:** Wan2.1 T2V, I2V, FLF2V, SkyReels, VACE

---

## Concept

Kaggle cho **30 giờ GPU T4 miễn phí mỗi tuần** — đủ để generate 20-40 video chất lượng cao.

```
Kaggle Free Account
→ 30h/tuần T4 GPU (15GB VRAM)
→ WanGP interface
→ Video 1080P, 5-10 giây
→ $0 hoàn toàn
```

---

## Setup (1 lần, 10 phút)

```bash
# Bước 1: Tạo Kaggle account (free)
# kaggle.com → Sign up

# Bước 2: Create new notebook
# kaggle.com/code → New Notebook

# Bước 3: Enable GPU
# Settings → Accelerator → GPU T4 x2
# Settings → Internet → On

# Bước 4: Copy notebook này
# github.com/kayas881/WanGP-Kaggle → copy cells

# Bước 5: Run cells 1-5 (install)
# Restart kernel → Run final cell
# → Gradio URL xuất hiện → mở URL
```

---

## Models Trong WanGP

| Model | Tốt cho | VRAM |
|-------|---------|------|
| **Wan2.1 T2V 14B** | Text → video chất lượng cao | 12GB |
| **Wan2.1 I2V** | Ảnh → video | 12GB |
| **SkyReels** | Cinematic, landscape | 12GB |
| **VACE** | Video editing, inpainting | 14GB |
| **FLF2V** | First-last frame to video | 12GB |

---

## Workflow Tạo Video (Mỗi Tuần 30h Free)

```
Mỗi tuần:
→ Mở Kaggle notebook
→ Enable GPU T4
→ Run WanGP
→ Generate 20-40 videos trong 30h
→ Download về local
→ Dùng cho content TikTok/YouTube

Hết 30h → chờ tuần sau reset
```

---

## Alternatives Free GPU

| Platform | Free GPU | Limit |
|----------|----------|-------|
| **Kaggle** | T4 15GB | 30h/tuần |
| **Google Colab** | T4 (free tier) | Không stable |
| **Colab Pro** | A100 40GB | $10/tháng |
| **Hugging Face Spaces** | CPU/T4 | Shared, chậm |

---

## Kết Hợp Với Workflow Content

```
Thứ 2: Mở Kaggle, generate 20 video clips 5-10s
→ Download hết về local

Thứ 3-6: Edit + post lên TikTok/YouTube/Reels
→ Kết hợp với supertonic (voiceover free)
→ Kết hợp với html-video (text overlay free)

Thứ 7: Generate thêm nếu cần
→ Còn GPU quota thì dùng tiếp
```

---

*Nguồn: github.com/kayas881/WanGP-Kaggle | FREE T4 GPU | tháng 6/2026*
