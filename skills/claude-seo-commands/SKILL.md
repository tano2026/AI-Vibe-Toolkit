---
name: claude-seo-commands
description: 25 /seo commands for SEO: keyword research, on-page optimization, competitor analysis, content strategy.
category: seo
---

# claude-seo — Cheat Sheet 25 Lệnh /seo (Dùng Ngay Trong Claude Code)

**Nguồn:** github.com/AgriciDaniel/claude-seo (8.8k⭐) | MIT
**Cài:** `/plugin marketplace add AgriciDaniel/claude-seo` → `/plugin install claude-seo@agricidaniel-claude-seo`
**Cập nhật:** tháng 6/2026

---

## Cài Nhanh (Claude Code 1.0.33+)

```bash
/plugin marketplace add AgriciDaniel/claude-seo
/plugin install claude-seo@agricidaniel-claude-seo
```

Hoặc manual:
```bash
git clone --depth 1 https://github.com/AgriciDaniel/claude-seo.git
bash claude-seo/install.sh
```

---

## 25 Lệnh /seo — Full Reference

### 🔍 AUDIT & PHÂN TÍCH TỔNG QUAN

```bash
# Full site audit — 18 agent song song, ra ACTION-PLAN.md
/seo audit https://your-site.com

# Phân tích sâu 1 trang cụ thể
/seo page https://your-site.com/about

# Technical SEO — 9 categories (crawl, index, speed, mobile...)
/seo technical https://your-site.com
```

### 📝 CONTENT & E-E-A-T

```bash
# Đánh giá E-E-A-T + content quality
/seo content https://your-site.com/blog/post

# Tạo content brief đầy đủ (keywords, outline, internal links)
/seo content-brief "best running shoes for flat feet"
/seo content-brief https://your-site.com/existing-post
```

### 🤖 AI SEARCH (GEO) — Xuất Hiện Trong ChatGPT/Gemini

```bash
# Tối ưu cho AI Overviews — citability score, entity clarity
/seo geo https://your-site.com/blog/guide
```

### 📐 SCHEMA & STRUCTURED DATA

```bash
# Detect, validate, generate JSON-LD schema
/seo schema https://your-site.com
```

### 🗺️ LOCAL SEO & MAPS

```bash
# Local SEO — GBP, citations, reviews, map pack
/seo local https://your-site.com

# Maps intelligence
/seo maps geogrid "coffee shop hanoi"
/seo maps audit https://maps.google.com/maps/place/...
/seo maps reviews <place_id>
/seo maps competitors "cafe hanoi" 5km
```

### 🌐 TECHNICAL DEEP DIVE

```bash
# Hreflang / international SEO
/seo hreflang https://your-site.com

# Images optimization — alt text, WebP, lazy load, CLS
/seo images https://your-site.com

# Sitemap validate hoặc generate mới
/seo sitemap https://your-site.com/sitemap.xml
/seo sitemap generate

# Programmatic SEO
/seo programmatic https://your-site.com/tools/
/seo programmatic plan
```

### 🔗 BACKLINKS & COMPETITORS

```bash
# Backlink profile (Moz + Common Crawl + DataForSEO optional)
/seo backlinks https://your-site.com
/seo backlinks setup

# Competitor comparison pages
/seo competitor-pages https://your-site.com/vs/competitor
/seo competitor-pages generate

# Semantic clustering từ SERP thật
/seo cluster "claude code skills"
```

### 📊 MONITORING & STRATEGY

```bash
# SEO drift monitoring — detect regressions (17 rules, SQLite)
/seo drift baseline https://your-site.com
/seo drift compare https://your-site.com
/seo drift history https://your-site.com

# SXO — Search Experience Optimization
/seo sxo https://your-site.com/blog/how-to-x

# Strategic plan theo loại site
/seo plan saas
/seo plan local
/seo plan ecommerce
/seo plan publisher
/seo plan agency

# E-commerce SEO
/seo ecommerce https://shop.example.com/product/x
```

### 🔌 GOOGLE APIs (Cần Setup)

```bash
# Setup credentials
/seo google setup
/seo google check

# PageSpeed Insights + CrUX (free, chỉ cần API key)
/seo google psi https://your-site.com

# Search Console (cần OAuth)
/seo google gsc-queries https://your-site.com

# Full report PDF
/seo google report full
```

### 🔌 EXTENSIONS (Cài Thêm Nếu Cần)

```bash
# DataForSEO — live SERP, keyword research, backlinks
/seo dataforseo serp "keyword"
/seo dataforseo keywords "seed keyword"
/seo dataforseo volume "keyword1, keyword2"
/seo dataforseo backlinks yourdomain.com
/seo dataforseo competitors yourdomain.com
/seo dataforseo ai-mentions "brand name"    # AI visibility tracking

# Firecrawl — full site crawl
/seo firecrawl crawl https://your-site.com
/seo firecrawl map https://your-site.com

# AI Image Generation (cần Banana extension)
/seo image-gen og "hero image for AI tools comparison post"
/seo image-gen hero "minimalist tech blog header"
```

### 🌊 FLOW FRAMEWORK

```bash
/seo flow find "topic"
/seo flow leverage https://your-site.com
/seo flow optimize "target keyword"
```

---

## Quick Decision Guide

| Mục tiêu | Lệnh |
|----------|------|
| Audit nhanh toàn site | `/seo audit <url>` |
| Fix 1 trang cụ thể | `/seo page <url>` |
| Xuất hiện trong ChatGPT/Gemini | `/seo geo <url>` |
| Fix schema markup | `/seo schema <url>` |
| Research content mới | `/seo content-brief <topic>` |
| Track thay đổi SEO | `/seo drift baseline` → `/seo drift compare` |
| Local business | `/seo local <url>` + `/seo maps geogrid` |
| Site mới cần strategy | `/seo plan <type>` |
| Phân tích từ khóa | `/seo cluster <seed>` |

---

*Nguồn: AgriciDaniel/claude-seo docs/COMMANDS.md*
*Distilled bởi AI Vibe Toolkit | tháng 6/2026*

