---
name: clone-site
description: "Website cloning tool: download full site (HTML, CSS, JS, assets) for offline viewing or analysis. Uses wget mirror."
allowed-tools:
  - Bash
user-invocable: true
---

# Clone Site — Website Downloader

Từ ai-marketing-skills repo.

## Usage
```bash
python "D:/AI Store/digital-marketing-repos/ai-marketing-skills/clone-site/clone_site.py" --url https://example.com --output ./clones/example
```

## Features
- Full site download (HTML, CSS, JS, images, fonts)
- Respects robots.txt (can bypass with --force)
- Concurrent downloads for speed
- Preserves directory structure
- Converts absolute links to relative
- Skips media files with --text-only flag

## Options
| Flag | Description |
|------|-------------|
| `--url` | Target URL (required) |
| `--output` | Output directory |
| `--depth` | Max link depth (default: 3) |
| `--text-only` | Skip images/videos |
| `--force` | Ignore robots.txt |
| `--delay` | Seconds between requests (default: 1) |

## Use Cases
- Competitor landing page analysis
- Design inspiration reference
- Offline backup
- Static site mirror