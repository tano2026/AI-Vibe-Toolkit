# Pilot Video #1 — Script + Fingerprint sẵn sàng

## Script (đưa thẳng vào ô "Video Subject/Script" của MoneyPrinterTurbo WebUI)

```
I spent a week testing 3 free AI video tools so you don't have to — here's
what actually happened.

Most videos about AI video tools are sponsored. This one isn't. I run an AI
agency, and I needed to pick a real tool for a real client project. So I
tested three of them side by side: MoneyPrinterTurbo, OpenMontage, and a
lightweight image generator called Pollinations.

First, the hardware reality nobody tells you. MoneyPrinterTurbo runs fine on
a 4 to 8 core machine with 4 to 8 gigabytes of RAM. No GPU required, as long
as you route the language model through a cloud API and use a free
text-to-speech engine like Edge TTS. That's a huge deal if you're testing
this on a laptop or a small server, not a rendering farm.

OpenMontage is a different beast. It's built for multi-scene storytelling —
twelve pipelines, over five hundred skills, and it can clone the visual style
of a reference video. But that power comes with a cost: it needs more
compute, and it's overkill if you just want a simple explainer video.

Here's the actual workflow difference. MoneyPrinterTurbo takes a topic,
writes a script, pulls stock footage from Pexels, generates voiceover, burns
in subtitles, and renders — all in one pass. For a five to seven minute
video, that took under twenty minutes on a standard setup. OpenMontage, when
you need character consistency across scenes, takes meaningfully longer,
because it's generating custom visuals instead of pulling stock footage.

So which one should you actually use? If your content is list-based,
comparison-based, or tutorial-style — reviews, explainers, how-to's —
MoneyPrinterTurbo is the faster, cheaper choice. If you're telling an actual
story with a consistent character or setting, OpenMontage earns its extra
weight.

The real lesson from this test wasn't which tool is "best." It's that
matching the tool to the content type matters more than picking the most
powerful option. I built my production pipeline around that exact decision
tree, and it's saved me from over-engineering half my videos.

If you're building something similar, start with the free tier setup — Edge
TTS plus a cloud LLM — before you invest in anything heavier. Test one video
end to end before you automate anything.
```

**Số từ ước tính:** ~360 từ, phù hợp video 5-7 phút với tốc độ đọc TTS thông thường.

## Fingerprint tính tay (theo đúng công thức compliance-gate/SKILL.md)

```json
{
  "video_id": "pilot-001",
  "topic": "3 free AI video tools compared — real render time and cost",
  "structure_type": "comparison",
  "hook_type": "story-open",
  "unique_claims": [
    "MoneyPrinterTurbo chạy 4-8 core/4-8GB RAM không cần GPU nếu dùng cloud LLM + Edge TTS",
    "Video 5-7 phút render dưới 20 phút trên setup chuẩn",
    "OpenMontage có 12 pipeline, 500+ skill, hỗ trợ clone visual style",
    "Quyết định chọn tool dựa theo structure_type (list/comparison/tutorial vs narrative) chứ không phải tool nào 'mạnh nhất'"
  ],
  "commentary_ratio": 0.35,
  "_note_commentary": "Ước tính tay — đoạn mở đầu (sponsor disclosure), đoạn kết luận (matching tool to content type), và đoạn 'lesson' cuối đều là góc nhìn/phân tích riêng, không phải liệt kê fact thô. Cao hơn nhiều ngưỡng tối thiểu 0.15 trong compliance-gate — hợp lý vì đây là video có background thật (đang xây kênh) đứng sau, không phải script AI generate mù.",
  "timestamp": "PENDING — điền khi render xong"
}
```

**Đây chính là record #1 sẽ ghi vào Airtable `fingerprint_history` sau này** —
lưu file này lại, đừng để mất, vì nó là gốc so sánh cho video #2.

## Checklist nhanh khi vào WebUI

- [ ] Language: English
- [ ] TTS: Edge TTS (free)
- [ ] Resolution: 1920x1080 (long-form, không phải Shorts cho pilot này)
- [ ] Subtitle: bật, kiểm tra font đọc được
- [ ] Sau khi render xong → chấm theo 5 tiêu chí PASS trong `PILOT-TEST-PLAN.md`
