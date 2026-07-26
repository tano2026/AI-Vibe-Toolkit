#!/bin/bash
# merge.sh
# Ghép scenes.webm (từ Playwright) + voice.mp3 (từ Supertonic/ElevenLabs) -> MP4 hoàn chỉnh.
# Ra 2 bản: 16x9 (YouTube/LinkedIn) và 9x16 (TikTok/Reels/Shorts) từ CÙNG 1 bản 16x9 gốc.
#
# Dùng: ./merge.sh scenes_16x9.webm voice.mp3 output_dir/
set -e

SCENES_WEBM="$1"
VOICE_MP3="$2"
OUT_DIR="${3:-./output}"

if [[ -z "$SCENES_WEBM" || -z "$VOICE_MP3" ]]; then
  echo "Dùng: ./merge.sh scenes_16x9.webm voice.mp3 output_dir/"
  exit 1
fi

mkdir -p "$OUT_DIR"

echo "[1/2] Ghép video + voiceover -> bản 16:9..."
ffmpeg -y -i "$SCENES_WEBM" -i "$VOICE_MP3" \
  -c:v libx264 -c:a aac -shortest \
  "$OUT_DIR/output_16x9.mp4"

echo "[2/2] Resize sang 9:16 cho TikTok/Reels/Shorts..."
ffmpeg -y -i "$OUT_DIR/output_16x9.mp4" \
  -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" \
  "$OUT_DIR/output_9x16.mp4"

echo "Xong. File ra:"
echo "  - $OUT_DIR/output_16x9.mp4  (YouTube/LinkedIn)"
echo "  - $OUT_DIR/output_9x16.mp4  (TikTok/Reels/Shorts)"
