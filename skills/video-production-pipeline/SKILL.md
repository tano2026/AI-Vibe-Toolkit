---
name: video-production-pipeline
category: media
description: Automated video production workflow for 'Giải Mã Số Phận' project, covering AI script, voice, image, subtitles, rendering, and multi-channel publishing.
---

# 🎥 QUY TRÌNH SẢN XUẤT VIDEO TỰ ĐỘNG DỰ ÁN \"GIẢI MÃ SỐ PHẬN\"

Skill này tổng hợp các phương pháp, khắc phục sự cố và quy trình cụ thể cho việc sản xuất video tự động trong dự án \"Giải Mã Số Phận\", từ kịch bản AI đến xuất bản.

## 0. BRAND IDENTITY & NỘI DUNG CỐT LÕI (Giải Mã Số Phận)

### Định vị thương hiệu
- **Tên kênh:** Giải Mã Số Phận (KHÔNG dùng "Bí Kíp Cổ Kim")
- **Định vị:** "Nhân tướng học & Mệnh lý học ứng dụng phong cách Cổ học tinh hoa"
- **Persona:** "Người Trải Đời Tuổi 30+" — trầm lạnh, lột trần sự thật của "The Hidden Self"
- **Văn phong:** Điềm đạm, ấm áp, chững chạc, mang tính chiêm nghiệm và thức tỉnh

### Công thức viết kịch bản (Trần trụi - Thấu suốt - Chỉ đường)
1. **TRẦN TRỤI (The Shadow):** Mở đầu bằng đòn giáng tâm lý trực diện, bóc trần sự thật tàn nhẫn. Câu đầu phải gây "giật mình".
2. **THẤU SUỐT (Mệnh lý & Cố nhân):** Dùng Tử Vi, Nhân Tướng Học + điển tích cố nhân + tâm lý học hành vi để giải mã.
3. **CHỈ ĐƯỜNG (Thức tỉnh & Cải mệnh):** Đưa ra giải pháp cải mệnh thực chiến, rõ ràng.

### Công thức tiêu đề (Hook)
"Nhận diện tướng mạo/hành vi + Dự báo vận mệnh" — kích thích sự tò mò đối chiếu bản thân.

### Phong cách hình ảnh
- Ảnh chân dung AI (nhân tướng học) sắc nét, bí ẩn
- Hiệu ứng Parallax 2.5D và khói sương chuyển động
- Học hỏi từ: Thuật Cổ Nhân & The Hidden Self

## Brand Audit (hậu rebranding / pre-launch)

Khi rebrand hoặc trước launch, audit 4 tầng song song via `delegate_task`:

| Tầng | Giao cho | Kiểm tra |
|------|---------|----------|
| Scripts | content_writer | Brand còn sót trong CTA, tags, header, persona, target |
| Strategy | research_analyst | Tài liệu + codebase search dư lượng brand cũ |
| Visuals | art_director | Logo, thumbnail, background, watermark, BGM |
| Backend | ops_manager | Server chạy được không? Engine build? Landing có form + payment? |

Mỗi đệ tử trả báo cáo chi tiết + đề xuất P0/P1/P2. Xem thêm `references/brand-audit-checklist.md`.

### Tối ưu thời lượng
- Video dài trên 45 phút ("Nghe trước khi ngủ")
- Nhịp độ đọc chậm rãi 0.85x
- Nhạc nền tần số chữa lành 432Hz ghim dưới tiếng mưa rơi

### Mô hình doanh thu (Phễu)
1. **Phễu 1:** Affiliate sách cổ học, nhân tướng phong thủy
2. **Phễu 2:** Tư vấn/Giải mã bản đồ vận mệnh cá nhân 1-1 (Mô hình High-ticket)

### Framework 6 Trụ Cột Nội Dung
Tham khảo file `references/6-pillar-content-framework.md` — 6 pillar: Tử Vi Nhập Môn, Kinh Dịch Ứng Dụng, Nhân Tướng Học, Cổ Nhân Thuật, Dưỡng Sinh & Tâm Tính, Đối Thoại Cổ Kim. Mỗi pillar có dilemma mẫu + monetization angle. Dùng để chọn chủ đề khi lên kế hoạch nội dung.

### Ánh xạ vai trò sản xuất → Subagents
| Vai trò trong KHO_SAN_XUAT | Subagent thực tế (C:\Users\...\.agents\agents\) |
|----------------------------|--------------------------------------------------|
| AI Content Strategist | research_analyst (Hoàng Trung) |
| AI Script Writer & Editor | content_writer (Bàng Thống) |
| AI Visual Asset Creator | art_director (Triệu Vân) |
| Video Renderer & Publisher | media_editor (Trương Phi) + ops_manager (Quan Vũ) |
| Auto Responder | auto_responder (Khương Duy) |
| Sales & Marketing | sales_mkt (Mã Siêu) |

Các vai trò không có subagent riêng (AI Voice & Subtitle Producer, Tử Vi & BaZi Engine Developer, Landing Page & Web Developer) do Hermes đảm nhiệm trực tiếp.

### Hyper / Storyboard Pipeline

Pipeline storyboard mới nhất (v3) với karaoke + Ken Burns + pool background.

```bash
# V3 — karaoke + Ken Burns + pool (khuyên dùng)
python scripts/hyper_v3.py "episodes/ep06-sao-menh/script-06-sao-menh.md" --pool 10

# Render đơn giản (đã test ổn định nhất cho quick run)
python scripts/render_all.py
```

Xem chi tiết: `references/hyper-karaoke-v3-pipeline.md`

Full episode test (Jul 2026):
- Script: `episodes/ep06-sao-menh/script-06-sao-menh.md`
- 10 scenes / 199s runtime / 18MB / 245s total gen time
- Imagen 4 pool (10 ảnh), Edge TTS CLI, Ken Burns scale+crop, Karaoke word-by-word ASS
- Output: `output/giai_ma_so_phan_ep06-sao-menh_hyper.mp4`

**Pipeline timing breakdown:**
```
[  0s] Parse script
[105s] Imagen 4 backgrounds (10/10, sequential, 1s delay giữa calls)
[180s] TTS (10/10, edge-tts CLI subprocess)
[201s] Ken Burns (10/10, ultrafast preset, scale+crop)
[245s] Concat + Karaoke ASS + Render cuối
```

Xem chi tiết: `references/hyper-karaoke-v3-pipeline.md`

Đối với các tác vụ phức tạp, nhiều bước đã được đóng gói trong `make.py`, **luôn ưu tiên chạy `make.py` trực tiếp qua `terminal`** thay vì cố gắng gọi các module con qua `execute_code`. Điều này đảm bảo môi trường Python và các dependency được xử lý chính xác.

**Lệnh chạy chính:**
```bash
cd "D:/MMO Du an/Giai ma so phan" && python make.py run [episode_name] --format [shorts|podcast] [--force]
```
*   Sử dụng `--force` để ép buộc tạo lại từ đầu, bỏ qua cache.
*   Luôn chạy ở chế độ nền (`background=True`) và thông báo khi hoàn thành (`notify_on_complete=True`) cho các tác vụ dài.

**Các bước chính trong `make.py`:**
1.  **AI Script Extraction** (`script_parser.py`): Chuyển kịch bản thô thành `narration` và `bg_prompt` bằng AI (Claude/Gemini).
2.  **AI Voice Generation** (`voice_generator.py`): Sinh giọng nói AI (Edge-TTS hoặc ElevenLabs).
3.  **Speech Transcription & Alignment** (`transcriber.py`): Chạy Whisper để chuyển ngữ và khớp thời gian.
4.  **AI Image Generation** (`image_generator.py`): Sinh ảnh nền AI (Imagen 4).
5.  **ASS Subtitle Building** (`subtitle_builder.py`): Tạo file phụ đề ASS với hiệu ứng karaoke.
6.  **Video Rendering** (`video_renderer.py`): Ghép nối video bằng FFmpeg.
7.  **Publishing** (`publisher.py`): Gửi video lên Telegram và phân phối đa kênh.

## II. VẬN HÀNH & BẢO TRÌ DỰ ÁN

### 0. Delivery preference: Telegram gửi file sau render

User yêu cầu: "gửi tele cho tao. máy tao ko có audio. nhớ lần sau gửi qua tele tao nghe nhé."

→ Sau mỗi lần render xong video, **bắt buộc gửi file qua Telegram** (không chỉ báo "đã render xong"). Dùng `send_message(file_path=...)` nếu Hermes có tool gửi file, nếu không thì hướng dẫn user cách lấy file hoặc thiết lập delivery.

### 1. Episode Inventory & Pipeline Status Check

Khi chủ hỏi "dự án đến đâu rồi", workflow kiểm tra nhanh:

```bash
# 1. Liệt kê episodes + số lượng file
for d in episodes/*/; do name=$(basename "$d"); scripts=$(ls "$d"*.md "$d"*.txt "$d"cache/ 2>/dev/null | wc -l); echo "$name: $scripts files"; done

# 2. Kiểm tra video đã render
ls output/*.mp4 2>/dev/null

# 3. Kiểm tra cấu trúc tổng thể (backend, engine, landing page)
ls backend/src/ 2>/dev/null
ls bazi-ziwei-engine/calculator/ 2>/dev/null
```

**Bảng tổng kết nhanh:**
| Trục | Trạng thái | Chi tiết |
|------|-----------|----------|
| Pipeline `make.py` | ✅ Đầy đủ 7 bước | script_parser → voice → whisper → image → subtitle → render → publish |
| Episodes scripts | ✅ 16 tập có script | ep01–ep15 + ep16-sao-menh-tai-chinh |
| Video đã render | ⚠️ ~6/16 tập | ep01, ep02, ep06, ep07, ep08 + podcast |
| Backend Node.js | ✅ Code xong | 4 agents + engine service, chưa build/deploy |
| Engine Tử Vi | ✅ TypeScript | calculator + prompts + templates, ra PDF được |
| Landing page | ⚠️ Sơ sài | index.html + style.css, chưa tích hợp API |

### 1. Đổi tên thương hiệu (Find & Replace hàng loạt)
Khi cần đổi tên kênh/thương hiệu trong toàn bộ dự án:
```python
# Cách 1: search_files + patch (nhanh, an toàn)
from hermes_tools import search_files, patch

results = search_files(pattern="TÊN_CŨ", target="content", path="D:/MMO Du an/Giai ma so phan", output_mode="files_only")
for file in results.get("matches", []):
    patch(path=file["path"], old_string="TÊN_CŨ", new_string="TÊN_MỚI", replace_all=True)
```
- Đã áp dụng thành công: "Bí Kíp Cổ Kim" → "Giải Mã Số Phận" (14 files, Jun 2026)

### 2. Dọn dẹp thư mục cũ (Legacy cleanup workflow)

**Quy tắc vàng:** KHÔNG xoá trước khi inspect. Luôn đọc nội dung trước, quyết định giữ gì, migrate, rồi mới xoá.

**Workflow 4 bước (demonstrated Jun 2026, cleaned ~212MB rác):**

**Bước 1 — Kiểm tra tổng quan:**
```bash
# Xem kích thước + cấu trúc
for d in dir1 dir2 dir3; do echo "=== $d ==="; du -sh "$d"; find "$d" -maxdepth 2 -type f | wc -l; done
```

**Bước 2 — Đọc nội dung từng file để đánh giá:**
- Dùng `read_file` để đọc script, code, tài liệu
- Kiểm tra xem chủ đề/chất liệu đã có trong episodes/ chưa
- Đặc biệt chú ý: script hoàn chỉnh, ý tưởng độc, media gốc, framework nội dung

**Bước 3 — Migrate đồ tốt vào cấu trúc mới:**
- Script → `drafts/imported/` hoặc `episodes/epXX-/`
- Media → `assets/backgrounds/`, `assets/branding/`
- Tool Python độc lập → `tools/`
- Framework/kiến trúc → `drafts/imported/`
- Code web app → kiểm tra xem có utility/tool hữu ích không

**Bước 4 — Xoá thư mục cũ:**
```bash
rm -rf dir1 dir2 dir3
```

**Các thư mục cũ đã dọn (Jun 2026):**
| Thư mục | Dung lượng | Nội dung | Xử lý |
|---------|-----------|---------|-------|
| `bi-kip-co-kim/` | 26MB | Script gốc + media bài 01 | Migrate script → `drafts/imported/`, media → `assets/` |
| `bikipkimco/` | 184MB | Web React cũ (chủ yếu node_modules) | Lấy `src/types.ts` (6-pillar framework) → `drafts/imported/` |
| `series-sao-menh/` | 1.9MB | Script Sao Mệnh & Tài Chính | Migrate → `episodes/ep16-sao-menh-tai-chinh/` |
| `tri-thuc-cua-toi/` | 93KB | Tool gen câu hỏi Python | Migrate → `tools/tri-thuc-cua-toi/` |
| `giai-ma-so-phan/` | 27KB | Duplicate backend | Xoá |
| `demo-hyperframes/`, `demo-video/`, `hyper_sample/`, `pipeline-test/`, `remotion-podcast/` | — | Thử nghiệm | Kiểm tra trước khi xoá |

### 3. Phục hồi bộ nhớ (Memory drift recovery)
Khi MEMORY.md bị lỗi "drift" (không thể dùng memory tool):
1. Sao lưu file cũ: `cp MEMORY.md MEMORY.md.bak`
2. Xoá nội dung: `write_file` với content rỗng
3. Thêm lại entries bằng `memory(action='add', ...)` — tóm tắt thay vì copy nguyên văn để tiết kiệm dung lượng
4. File gốc KHO-INDEX.md và HERMES-PLAYBOOK.md có trong GitHub repo `tano2026/AI-Vibe-Toolkit`

## III. KHẮC PHỤC SỰ CỐ & TỐI ƯU HÓA

### 1. Lỗi `ModuleNotFoundError` trong `execute_code` (Môi trường Python)
*   **Nguyên nhân:** Hermes `execute_code` có thể sử dụng một môi trường Python khác với môi trường mà thư viện (`google-generativeai`) đã được cài đặt.
*   **Cách khắc phục:**
    1.  Xác định Python interpreter của Hermes:
        ```bash
        python -c "import sys; print(sys.executable); print(sys.path)"
        ```
    2.  Cài đặt thư viện vào đúng interpreter đó:
        ```bash
        C:\Python314\python.exe -m pip install google-generativeai
        ```
*   **Bài học:** Đối với các workflow phức tạp của dự án, ưu tiên chạy script gốc (`make.py`) qua `terminal` thay vì gọi logic nội bộ qua `execute_code` để tránh các vấn đề về môi trường.

### 2. Lỗi "Không tìm thấy tập phim" (`make.py` Episode Name)
*   **Nguyên nhân:** Tên thư mục tập phim truyền vào `make.py` không khớp với tên thực tế.
*   **Cách khắc phục:**
    1.  Liệt kê chính xác các thư mục tập phim:
        ```bash
        ls -d "D:/MMO Du an/Giai ma so phan/episodes"/*/
        ```
    2.  Sử dụng tên chính xác (ví dụ: `ep01-giai-ma-so-phan`).

### 3. Lỗi Phụ đề không khớp Giọng đọc / Tốc độ đọc không phù hợp
*   **Nguyên nhân:** Tốc độ đọc của TTS quá nhanh hoặc lỗi căn khớp thời gian.
*   **Cách khắc phục (Điều chỉnh tốc độ TTS):**
    1.  Kiểm tra `src/voice_generator.py` (dòng 96): `rate_val = "+15%" if format_type == "shorts" else config.TTS_RATE`
    2.  **Vá file `src/voice_generator.py`** để thay đổi giá trị `config.TTS_RATE` thành một giá trị cụ thể và chậm hơn cho podcast, ví dụ:
        ```python
        # old_string:    rate_val = "+15%" if format_type == "shorts" else config.TTS_RATE
        # new_string:    rate_val = "+15%" if format_type == "shorts" else "+5%"
        ```
    3.  Chạy lại `make.py` với `--force` để tạo lại audio và phụ đề.

### 4. Lỗi `SyntaxWarning: "\k"` trong `subtitle_builder.py`
*   **Nguyên nhân:** Chuỗi `\k` trong code Python được hiểu là một escape sequence không hợp lệ.
*   **Cách khắc phục:**
    1.  Vá file `src/subtitle_builder.py` để thay `\kf` bằng `\\kf`.
        ```python
        # old_string:    Sinh file phụ đề ASS với hiệu ứng karaoke cao cấp \kf.
        # new_string:    Sinh file phụ đề ASS với hiệu ứng karaoke cao cấp \\kf.
        ```

### 5. Lỗi Telegram `Request Entity Too Large` (Code 413)
*   **Nguyên nhân:** Kích thước file video (.mp4) vượt quá giới hạn cho phép của Telegram API (thường khoảng 50MB).
*   **Cách khắc phục:**
    1.  Sử dụng FFmpeg để nén video xuống kích thước nhỏ hơn (ví dụ: dưới 40MB):
        ```bash
        ffmpeg -y -i "input.mp4" -fs 40M -c:v libx264 -preset fast -crf 28 -c:a aac -b:a 96k "output_compressed.mp4"
        ```
    2.  Gửi file đã nén.

### 6. Vấn đề Giao tiếp Telegram (Nhóm Chat vs. Chat Riêng)
*   **Nguyên nhân:** Hermes mặc định gửi vào "home channel". Gửi vào ID chat riêng có thể gặp lỗi nếu ID đó là của bot hoặc có cài đặt bảo mật.
*   **Cách khắc phục:** Sử dụng ID của một nhóm chat mà cả Hermes và người dùng đều có mặt. Hermes sẽ được cấp quyền gửi vào nhóm đó.
*   **Bài học:** Khi gửi tin nhắn quan trọng, nên dùng ID của một nhóm chat chung để đảm bảo tin nhắn được nhận.

### 8. FFmpeg Windows — Subtitles Filter Path Escape

**Vấn đề:** Path Windows có dấu `:` (D:/) và space → FFmpeg `subtitles=path:original_size=...` filter lỗi.

**Fix (đã test OK trên FFmpeg 8.1 Windows build):**

```python
# Copy file subtitle ra short path (không space, không ký tự đặc biệt)
ass_short = Path("D:/_ka.ass")

# Escape: forward slashes + backslash trước colon
fs = str(ass_short).replace("\\", "/").replace(":", "\\:")
# → 'D\\:/_ka.ass':original_size=1080x1920

cmd = ["ffmpeg", "-i", "video.mp4", "-i", "audio.wav",
       "-vf", f"subtitles='{fs}':original_size=1080x1920", ...]
```

Luôn copy ASS/SRT ra short path `D:/` trước render. Xoá sau khi hoàn tất.

### 9. Imagen 4 API Key — Tự động đọc từ Hermes Config

Khi chạy script độc lập (ngoài Hermes context), key Gemini cần được đọc tự động:

```python
import yaml
from pathlib import Path

cfg_path = Path.home() / "AppData/Local/hermes/config.yaml"
cfg = yaml.safe_load(cfg_path.read_text(encoding="utf-8"))
api_key = cfg["providers"]["google"]["gemini"]["api_key"]
os.environ["GOOGLE_API_KEY"] = api_key
```

Cần `pip install pyyaml`. Xem chi tiết: `references/imagen-4-key-from-hermes-config.md`.

### 10. Edge TTS — Không có WordBoundary cho tiếng Việt

Edge TTS Python stream API trả về các chunk types:
- ✅ `"audio"` — dữ liệu âm thanh
- ✅ `"SentenceBoundary"` — ranh giới câu (kèm offset)
- ❌ `"WordBoundary"` — **KHÔNG có** cho giọng vi-VN-NamMinhNeural

→ Karaoke word-by-word highlight phải estimate thời gian từ SentenceBoundary:
```python
words = seg["text"].split()
word_dur = len(seg["text"]) / 20 / len(words)  # ước lượng
for w in words:
    dur_cs = int(word_dur * 100)
    karaoke += f"{{\\k{dur_cs}}}{w} "
```

Nếu cần word timestamps chính xác: dùng Whisper transcribe audio sau khi gen.
### 11. Lỗi OmniRoute Read Timed Out

### 12. ASS Timecode Format — lỗi phổ biến trong Python

ASS yêu cầu timecode dạng `0:00:00,00` (dấu phẩy phân cách giây/milligiây). Khi gen ASS bằng Python string format, dễ sai thứ tự tính toán:

```python
# ✅ ĐÚNG: tính ss TRƯỚC khi += dur
ss = f"0:00:{t:05.2f}".replace(".", ",")
t += dur
es = f"0:00:{t:05.2f}".replace(".", ",")

# ❌ SAI — ss và es trùng nhau
t += dur
ss = f"0:00:{t:05.2f}".replace(".", ",")  # đã += dur rồi
es = f"0:00:{t:05.2f}".replace(".", ",")
```

### 13. Edge TTS CLI vs Python API — chọn cho background tasks

Trong Hermes background process (`terminal(background=True)`), Python asyncio (edge_tts.Communicate) dễ treo không output. Luôn dùng CLI subprocess cho background tasks:

```python
# ✅ Ổn định trong background
subprocess.run(["edge-tts", "--voice", "vi-VN-NamMinhNeural", 
                "--text", text, "--write-media", str(out)], timeout=60)

# ⚠️ Dễ treo trong background
import edge_tts
communicate = edge_tts.Communicate(text, "vi-VN-NamMinhNeural")
```

### 14. Whisper trên Windows CPU — model download lần đầu chậm

Whisper base model ~140MB, download về `~/.cache/whisper/` lần đầu. Trên Windows, `whisper.load_model("base")` mất ~10-20s. Pre-download trước nếu cần chạy nhanh:

```bash
python -c "import whisper; whisper.load_model('base')"
```

### 15. User Style Preference: Visual Variety

User prefers "hyper/storyboard style" (mỗi scene 1 ảnh AI riêng) hơn static backgrounds. Khi có lựa chọn giữa background tĩnh và gen ảnh AI — luôn chọn gen ảnh. User thích thay đổi hình ảnh thường xuyên, không thích 1 background xuyên suốt video dài.

### 16. Imagen 4 Pool + Ken Burns (Tiết kiệm ảnh)

Thay vì gen 20-30 ảnh Imagen 4 cho video 30 phút:
1. Gen pool ~10 backgrounds Imagen 4 đẹp (tốn 1 lần)
2. Mỗi scene chọn background phù hợp từ pool
3. Thêm Ken Burns effect (scale+crop, không zoompan) → cảm giác động
4. Kết quả: 10 ảnh xoay vòng đủ cho 16 tập

Pool backgrounds pattern:
```python
BG = Path("assets/backgrounds")
pool = sorted(BG.glob("bg_*.png"))
bg = pool[scene_index % len(pool)]

# Ken Burns (scale+crop, nhanh trên Windows)
subprocess.run(["ffmpeg","-y","-loop","1","-i",str(bg),
    "-vf","scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,setsar=1,format=yuv420p",
    "-c:v","libx264","-preset","ultrafast","-crf","23",
    "-t",f"{duration:.3f}","-an",str(output)])
```

### 17. Karaoke Subtitle Preferences

User yêu cầu:
- Word-by-word karaoke highlight (`{\k}` tags trong ASS)
- 1 hàng duy nhất (alignment=2, bottom center)
- Font size 52, Segoe UI Semibold
- Primary white, secondary gold `&H00C9A84C`
- Outline đen, shadow đen bán trong suốt

### 18. Render Strategy: 1 tập test trước khi batch

User yêu cầu chạy 1 tập cho mượt trước khi chạy 16 tập. Never batch-all trước khi 1 tập xác nhận OK.

### 19. FFmpeg Windows build quirks

| Issue | Fix |
|-------|-----|
| Zoompan quá chậm với ảnh >1MB | Dùng scale+crop thay zoompan |
| Path có space trong concat list | Copy file ra short path D:/ |
| ASS timecode sai format | `f"0:00:{t:05.2f}"` dùng dấu chấm |
| Subtitles filter path colon | Escape: `'D\\:/_hfn.ass':original_size=1080x1920` |

### 20. Short path pattern for FFmpeg Windows

Copy file tạm ra `D:/` root (short path, không space):
```python
ass_short = Path("D:/_hfn.ass")
shutil.copy2(ass_path, ass_short)
# render
ass_short.unlink(missing_ok=True)
```

### 21. Video Delivery — Telegram sau khi render

User yêu cầu gửi file video qua Telegram ngay sau khi render xong (không chỉ báo \"đã xong\"). Khi render hoàn tất, cần:

1. Kiểm tra file output: `ls -lh output/*.mp4`
2. Gửi file qua Telegram kèm thông số (thời lượng, dung lượng, scene count)
3. Nếu không có `send_message` tool, hướng dẫn user đường dẫn file hoặc thiết lập Telegram bridge

Telegram ID người dùng: 8647881602 (chat riêng, gửi qua `telegram:8647881602`)

### 22. TTS alternatives — khi edge-tts không ổn định

Xem `references/tts-alternatives-from-repo.md` cho danh sách TTS engine thay thế:
- Kokoro-82M (300MB, chạy CPU, load 3s) — test trước
- ChatTTS (39K⭐, conversational, [laugh] tags)
- F5-TTS (14.8K⭐, voice clone 3s audio)

Cả 3 đều có trong kho `tano2026/AI-Vibe-Toolkit`.

### 23. Viral Hooks — 100 formula cho script

Xem `references/viral-hooks-from-repo.md`. Skill `viral-hooks` trong kho có 100 công thức hook chia 10 psychology triggers. Dùng cho phần mở đầu video và CTA.

### 24. `render_all.py` — pipeline ổn định nhất

File `scripts/render_all.py` là phiên bản pipeline đã test thành công:
- Standalone (không phụ thuộc module khác)
- Sequential steps (tránh rate limit Imagen 4)
- CLI TTS (tránh treo asyncio)
- Short path ASS (tránh lỗi FFmpeg Windows)
- Dùng làm base cho production chạy batch

Whisper base model ~140MB, download về `~/.cache/whisper/` lần đầu. Trên Windows, `whisper.load_model("base")` mất ~10-20s. Pre-download trước nếu cần chạy nhanh:

```bash
python -c "import whisper; whisper.load_model('base')"
```