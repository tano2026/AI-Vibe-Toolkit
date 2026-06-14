# magika — AI File Type Detection (15.2k⭐, Google)

**Repo:** github.com/google/magika | Apache 2.0 | Google
**Dùng trong:** Gmail, Google Drive, Google Safe Browsing

---

## Cài Nhanh

```bash
pip install magika
```

## Dùng Ngay

```python
from magika import Magika

m = Magika()

# Detect 1 file
result = m.identify_path("unknown_file")
print(result.output.ct_label)  # "python", "javascript", "pdf"...
print(result.output.score)     # 0.99 (confidence)
print(result.output.mime_type) # "text/x-python"

# Detect bytes (không cần save file)
result = m.identify_bytes(b"#!/usr/bin/env python3
print('hello')")
print(result.output.ct_label)  # "python"

# Batch detect nhiều files
files = ["file1.dat", "file2.bin", "file3.unknown"]
results = m.identify_paths(files)
for r in results:
    print(f"{r.path}: {r.output.ct_label} ({r.output.score:.2f})")
```

## CLI Usage

```bash
magika file.dat
magika --json file.dat
magika --recursive /folder/
magika --mime-type file.dat
```

## Tích Hợp Vào AI Workflow

```python
# Trước khi process file không rõ type
from magika import Magika
m = Magika()

def safe_process_file(filepath):
    result = m.identify_path(filepath)
    file_type = result.output.ct_label
    
    if file_type == "python":
        # process as code
    elif file_type == "pdf":
        # extract text
    elif file_type in ["jpeg", "png", "webp"]:
        # process as image
    elif file_type == "javascript":
        # analyze js
    else:
        print(f"Unknown type: {file_type}, confidence: {result.output.score}")
```

## 200+ File Types Detect Được

Code: Python, JavaScript, TypeScript, Go, Rust, Java, C/C++, PHP...
Docs: PDF, DOCX, PPTX, XLSX, ODS...
Media: JPEG, PNG, WebP, MP4, MP3, WAV...
Archive: ZIP, TAR, GZIP, 7Z...
Data: JSON, CSV, XML, YAML, SQLite...

## Tại Sao Dùng Magika Thay Vì Extension?

Extension `.py` có thể bị rename. Content-based detection bằng AI = reliable hơn 99%.

---
*skills/magika-skill.md | AI Vibe Toolkit | tháng 6/2026*
