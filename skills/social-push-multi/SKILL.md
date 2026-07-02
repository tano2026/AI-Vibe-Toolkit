---
name: social-push-multi
description: "Multi-platform social media posting via agent-browser. Hỗ trợ Xiaohongshu, X(Twitter), Weibo, WeChat, Juejin, Linux.do. Tự động đăng nhập, soạn thảo, lưu nháp."
allowed-tools:
  - Bash
user-invocable: true
---

# Social-Push — Multi-Platform Posting

Dùng **agent-browser** để đăng content lên nhiều nền tảng.

## Requirements
- `agent-browser` installed ✓ (v0.27.0)
- Chrome với remote debugging port 9222

## Core Workflow
```bash
# 1. Mở Chrome với --remote-debugging-port=9222

# 2. Kết nối
agent-browser --auto-connect open <platform_url>

# 3. Snapshot tìm element
agent-browser snapshot -i

# 4. Thao tác
agent-browser fill @ref "nội dung"
agent-browser click @ref

# 5. Chỉ lưu nháp - không auto-publish
```

## Supported Platforms

### X (Twitter)
- Compose: `agent-browser open https://x.com/compose/post`
- Fill text: `agent-browser fill @textbox "nội dung tweet"`
- Post: `agent-browser click @button "Post"`

### 小红书 (Xiaohongshu)
- URL: `https://www.xiaohongshu.com/upload`
- Upload ảnh + viết caption
- Lưu nháp trước khi publish

### 微博 (Weibo)
- URL: `https://weibo.com/` → compose area
- Post text/image

### 微信公众号 (WeChat)
- URL: `https://mp.weixin.qq.com/`
- Article editor → draft

### 掘金 (Juejin)
- URL: `https://juejin.cn/editor`
- Write article → save draft

### Linux.do
- URL: `https://linux.do/` → new topic
- Category + tags + content

## Rules
1. **Luôn snapshot để lấy ref mới** sau mỗi lần tương tác
2. **Chỉ lưu nháp**, không tự động bấm Publish
3. Dùng `agent-browser wait 2000` giữa các bước nếu trang chậm
4. Nếu thao tác fail → snapshot lại + eval JS để debug

## Debug
```bash
# Xem HTML element khi snapshot không đủ
agent-browser eval 'document.querySelector("button[type=submit]").outerHTML'

# Screenshot để verify
agent-browser screenshot --annotate
```