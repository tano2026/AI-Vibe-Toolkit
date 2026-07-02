---
name: short-form-pipeline
description: "Short-form video clip pipeline: YouTube long-form → TikTok/Reels/Shorts clips. Download, transcribe (Whisper), AI segment (Claude), vertical crop, caption burn-in."
allowed-tools:
  - Bash
  - Python
user-invocable: true
---

# Short-Form Video Pipeline

YouTube video → viral short clips (TikTok, Reels, Shorts).

## Prerequisites
```bash
pip install -r "D:/AI Store/digital-marketing-repos/ai-marketing-skills/requirements.txt"
# yt-dlp + ffmpeg required
```

## Usage

### Full pipeline (Claude-based segmentation)
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/short-form-pipeline/scripts/shortform_pipeline.py" \
  --url "https://www.youtube.com/watch?v=VIDEO_ID" \
  --max-clips 3 \
  --output-dir ./output
```

### Standalone clipper (no Claude, heuristic scoring)
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/short-form-pipeline/scripts/video_clipper.py" \
  --url "https://www.youtube.com/watch?v=VIDEO_ID"
```

## Pipeline Steps
1. **Download** — yt-dlp fetches video + VTT captions
2. **Transcribe** — Whisper word-level timestamps
3. **Segment** — Claude picks 2-5 best 30-60s moments (hook ≥ 7/10)
4. **Cut** — FFmpeg extracts clips
5. **Vertical crop** — Layout-aware 16:9 → 9:16 (face detection với MediaPipe)
6. **Caption burn** — TikTok-style word-highlighted captions

## Layout Types (auto-detected)
| Layout | Strategy |
|--------|----------|
| talking_head | Face-detected center crop |
| screen_share_overlay | Screen on top, webcam on bottom |
| side_by_side | Stack screen on top, face on bottom |
| gallery_view | Active speaker quadrant |

## Output
- 1080×1920 (9:16 vertical)
- H.264 + AAC
- Word-highlighted captions
- Ready for TikTok/Reels/Shorts

## Tips
- **FFmpeg error**: don't use `-c:v copy` with `-filter_complex`
- **Caption sync**: run Whisper on cut clip, not source
- **Long clips**: auto-trimmed >90s → 75s
- Requires `ANTHROPIC_API_KEY` for AI segmentation