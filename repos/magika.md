# Magika â€” AI detect file type chÃ­nh xÃ¡c 99%, Google dÃ¹ng cho Gmail vÃ  Drive

**GitHub:** https://github.com/google/magika
**Stars:** 15.2k | **License:** Apache 2.0
**TÃ¡c giáº£:** Google | **Release:** python-v1.0.2
**NgÃ´n ngá»¯:** Python, Rust, JavaScript/TypeScript, Go (WIP)

---

## Váº¥n Ä‘á» nÃ³ giáº£i quyáº¿t

M y upload file lÃªn web app â€” lÃ m sao biáº¿t Ä‘Ã³ thá»±c sá»± lÃ  file gÃ¬?

Extension `.jpg` khÃ´ng Ä‘Ã¡ng tin. Ai cÅ©ng cÃ³ thá»ƒ Ä‘á»•i tÃªn `virus.exe` thÃ nh `photo.jpg`. CÃ¡ch cÅ© lÃ  dÃ¹ng "magic bytes" â€” Ä‘á»c vÃ i byte Ä‘áº§u file rá»“i so vá»›i database. Váº¥n Ä‘á»: khÃ´ng Ä‘á»§ chÃ­nh xÃ¡c vá»›i textual files nhÆ° code, config, CSV.

Magika giáº£i quyáº¿t báº±ng deep learning â€” train trÃªn **100 triá»‡u files, 200+ content types**, Ä‘áº¡t **~99% precision vÃ  recall**. Nhanh hÆ¡n, chÃ­nh xÃ¡c hÆ¡n, Ä‘áº·c biá»‡t vá»›i file text.

Google Ä‘Ã£ dÃ¹ng nÃ³ á»Ÿ production Ä‘á»ƒ scan hÃ ng trÄƒm tá»· file má»—i tuáº§n trÃªn Gmail, Drive, vÃ  Safe Browsing.

---

## CÃ¡ch hoáº¡t Ä‘á»™ng

Magika khÃ´ng Ä‘á»c toÃ n bá»™ file â€” chá»‰ Ä‘á»c **má»™t pháº§n nhá» ná»™i dung** (header + footer + middle), Ä‘Æ°a vÃ o model Keras nhá» (~vÃ i MB), inference trong **~5ms/file trÃªn CPU thÆ°á»ng**.

```
File input â†’ TrÃ­ch header/footer/middle â†’ Keras model â†’ Content type + confidence score
```

Confidence threshold cÃ³ thá»ƒ Ä‘iá»u chá»‰nh:
- `high-confidence` â†’ cháº¯c cháº¯n cao
- `medium-confidence` â†’ cháº¥p nháº­n Ä‘Æ°á»£c
- `best-guess` â†’ Ä‘oÃ¡n tá»‘t nháº¥t dÃ¹ uncertain

---

## CÃ i & DÃ¹ng

**Python:**
```bash
pip install magika
```

**CLI:**
```bash
magika examples/
# examples/README.md: Markdown document (text)
# examples/bmp.bmp: BMP image data (image)
# examples/code.py: Python source (code)
# examples/doc.docx: Microsoft Word 2007+ document (document)
# examples/doc.ini: INI configuration file (text)
# examples/elf64.elf: ELF executable (executable)
# examples/flac.flac: FLAC audio bitstream data (audio)
```

**Python API:**
```python
from magika import Magika
m = Magika()
result = m.identify_bytes(b"# Example\nThis is a markdown file.")
print(result.output.ct_label)  # "markdown"
print(result.output.score)     # 0.9998...
```

**Scan Ä‘á»‡ quy cáº£ thÆ° má»¥c:**
```bash
magika -r /path/to/directory
```

---

## Äiá»ƒm ná»•i báº­t

**Cháº¡y trÃªn CPU, khÃ´ng cáº§n GPU** â€” model chá»‰ ~vÃ i MB, inference 5ms/file

**200+ content types** â€” cover gáº§n háº¿t má»i loáº¡i file thá»±c táº¿: code, documents, images, audio, video, executables, archives...

**Äa ngÃ´n ngá»¯** â€” Python, Rust CLI, JavaScript/TypeScript npm package, Go (Ä‘ang dev)

**ÄÃ£ production-tested** â€” Gmail + Drive scan hÃ ng trÄƒm tá»· file/tuáº§n

**TÃ­ch há»£p VirusTotal** â€” dÃ¹ng lÃ m pre-filter trÆ°á»›c khi phÃ¢n tÃ­ch malware

---

## Use Cases Thá»±c Táº¿

**Báº£o máº­t web app:**
```python
# Validate file upload thá»±c sá»± lÃ  gÃ¬
result = magika.identify_bytes(uploaded_file.read())
if result.output.ct_label not in ALLOWED_TYPES:
    raise ValueError("File type not allowed")
```

**Security scanning pipeline:**
- Route files Ä‘áº¿n Ä‘Ãºng scanner (PDF scanner, Office scanner, executable scanner...)
- PhÃ¡t hiá»‡n file giáº£ máº¡o extension

**Data processing:**
- Auto-detect format trÆ°á»›c khi parse
- PhÃ¢n loáº¡i large dataset

---

## á»¨ng dá»¥ng vá»›i Vibe Coding

Khi build web app cÃ³ upload file:
```python
# Thay vÃ¬ check extension (dá»… bá»‹ bypass)
if file.name.endswith('.jpg'):  # âŒ khÃ´ng Ä‘Ã¡ng tin

# DÃ¹ng Magika check content thá»±c sá»±
from magika import Magika
m = Magika()
result = m.identify_bytes(file.read(4096))
if result.output.ct_label == 'jpeg':  # âœ… check content
    process_image(file)
```

---

## ÄÃ¡nh GiÃ¡ CÃ¡ NhÃ¢n

Magika lÃ  má»™t trong nhá»¯ng open source release Ä‘Ã¡ng giÃ¡ nháº¥t cá»§a Google trong máº¥y nÄƒm gáº§n Ä‘Ã¢y â€” khÃ´ng hype, khÃ´ng demo Ä‘áº¹p, chá»‰ lÃ  má»™t tool giáº£i quyáº¿t Ä‘Ãºng váº¥n Ä‘á» cá»¥ thá»ƒ vÃ  giáº£i quyáº¿t tá»‘t.

99% accuracy trÃªn 200+ file types vá»›i model chá»‰ vÃ i MB cháº¡y trÃªn CPU lÃ  con sá»‘ áº¥n tÆ°á»£ng. Viá»‡c Google deploy nÃ³ á»Ÿ scale Gmail/Drive rá»“i má»›i open source cho tháº¥y Ä‘Ã¢y lÃ  production-grade, khÃ´ng pháº£i research toy.

Vá»›i vibe coders: mÃ y sáº½ cáº§n Magika báº¥t cá»© lÃºc nÃ o build app cÃ³ file upload. CÃ i 1 láº§n, dÃ¹ng mÃ£i.

Háº¡n cháº¿ duy nháº¥t: khÃ´ng detect polyglot files (file há»£p lá»‡ vá»›i nhiá»u format cÃ¹ng lÃºc) â€” nhÆ°ng Ä‘Ã¢y lÃ  edge case hiáº¿m gáº·p trong thá»±c táº¿.

**Rating: 9/10**

---

*Nguá»“n: github.com/google/magika*
*Cáº­p nháº­t: thÃ¡ng 6/2026*

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# pip install magika
from magika import Magika

m = Magika()

def detect_filetype(file_path):
    """Detect chính xác loại file bất kể extension"""
    result = m.identify_path(file_path)
    return {
        "type": result.output.ct_label,
        "mime": result.output.mime_type,
        "confidence": result.output.score,
        "is_text": result.output.is_text
    }

def batch_detect(file_paths):
    from pathlib import Path
    return [detect_filetype(p) for p in file_paths]

# Use case cho Hermes:
# Trước khi process file → detect type → chọn đúng tool
# PDF → MarkItDown, Image → fal.ai, Video → ffmpeg, Audio → TTS tools
```

### OpenClaw
```bash
# Python only — không có npm package
```

### Antigravity
```bash
pip install magika
# Test: python3 -c "from magika import Magika; print('OK')"
```
> ⚠️ Dùng để routing: nhận file bất kỳ → detect type → gọi đúng processing tool.
