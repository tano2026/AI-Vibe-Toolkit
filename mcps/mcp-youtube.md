# YouTube MCP (mcp-youtube) — MCP Server

## TL;DR
MCP cho Claude tự đọc transcript YouTube và tóm tắt video chỉ bằng cách dán link — không cần YouTube API key, chỉ cần yt-dlp cài local.

## Tool này dùng để làm gì
Server này dùng `yt-dlp` để tải subtitle/transcript của 1 video YouTube, đẩy nội dung đó vào context cho Claude xử lý. Không search video, không lấy view/like/metadata kênh — chỉ làm đúng 1 việc: lấy transcript để Claude tóm tắt hoặc phân tích nội dung. Hợp để research nhanh: dán link video review tool mới vào chat, Claude đọc transcript và rút điểm chính, khỏi ngồi xem hết video dài.

## Setup từng bước
1. Cài `yt-dlp` local (macOS: `brew install yt-dlp`, Windows: `winget install yt-dlp`)
2. Mở file config Claude Desktop:
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
3. Thêm đoạn này vào:
```json
{
  "mcpServers": {
    "mcp-youtube": {
      "command": "npx",
      "args": ["-y", "@anaisbetts/mcp-youtube"]
    }
  }
}
```
4. Quit hẳn Claude Desktop (không chỉ minimize) rồi mở lại
5. Check icon hammer 🔨 ở khung chat — nếu tool xuất hiện trong list là đã connect
6. Với Claude Code thì gọn hơn, chạy thẳng: `claude mcp add-json "mcp-youtube" '{"command":"npx","args":["-y","@anaisbetts/mcp-youtube"]}'`

## Ví dụ thực tế
Gõ: `Summarize the YouTube video https://youtu.be/xxxxx`
→ MCP tự gọi yt-dlp tải transcript, Claude đọc và trả tóm tắt nội dung chính trong vài giây, không cần xem hết video.

Áp vào AI Vibe Toolkit: dán link video review 1 tool/repo mới mà người khác đã làm → Claude tự rút insight, pain point, ví dụ thực tế từ transcript để viết nhanh phần "đánh giá cá nhân", đỡ phải tự ngồi xem hết video gốc.

## Lưu ý / Lỗi thường gặp
- Video transcript quá dài → lỗi `result exceeds maximum length of 1048576` (issue #1 trên repo). Bản mới đã strip bớt timestamp trong output để gọn hơn, nhưng video cực dài (1-2h+) vẫn có khả năng bị tràn.
- Trên Windows từng gặp lỗi `WinError 5: Access is denied` khi server tạo folder downloads — liên quan quyền ghi file, đổi thư mục lưu hoặc chạy với quyền phù hợp để fix.
- Chỉ lấy được transcript khi video CÓ caption (auto-caption hoặc creator tự upload) — video không caption thì không tóm tắt được.
- Đang có request mở (chưa merge) xin support multi-language tốt hơn — hiện tại pick ngôn ngữ chưa linh hoạt.
- Mỗi lần gọi tool, yt-dlp chạy nền có thể pop cửa sổ terminal — có issue mở xin ẩn cửa sổ này, chưa fix.

## Đánh giá cá nhân
- Điểm mạnh: setup siêu nhẹ, không cần đụng Google Cloud Console để lấy API key, đúng 5 dòng JSON là chạy, repo vẫn active (commit gần nhất chỉ vài ngày trước thời điểm viết bài).
- Điểm yếu: chỉ làm đúng 1 việc — lấy transcript để tóm tắt. Không search video theo từ khóa, không lấy số liệu kênh (view/sub/like). Nếu cần search + transcript cùng lúc thì phải dùng bản `bendelpino/youtube-mcp` (cần YouTube Data API key) thay vì cái này.
- Có nên dùng: 7/10 — rất hợp cho việc tóm tắt nhanh 1 video cụ thể trong lúc research, không phải tool research toàn diện.

## Link
- Repo: https://github.com/anaisbetts/mcp-youtube
- Docs: README trong repo (ngắn, kèm issues là đủ hiểu hết)
- MCP installer của cùng tác giả: https://github.com/anaisbetts/mcp-installer

---

## 🤖 Agent Integration

> Section này dành cho Hermes/OpenClaw/Antigravity — không phải cho human đọc.

### Hermes (Python — gọi thẳng, không cần MCP)
```python
import urllib.request, json, urllib.parse

def youtube_search(query, api_key, max_results=10):
    q = urllib.parse.quote(query)
    url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&q={q}&maxResults={max_results}&type=video&key={api_key}"
    req = urllib.request.Request(url)
    r = json.loads(urllib.request.urlopen(req).read())
    return [{"title": x["snippet"]["title"],
             "videoId": x["id"]["videoId"],
             "url": f"https://youtube.com/watch?v={x['id']['videoId']}",
             "desc": x["snippet"]["description"][:200]} for x in r["items"]]

def youtube_video_stats(video_id, api_key):
    url = f"https://www.googleapis.com/youtube/v3/videos?part=statistics,snippet&id={video_id}&key={api_key}"
    req = urllib.request.Request(url)
    r = json.loads(urllib.request.urlopen(req).read())
    item = r["items"][0]
    return {"title": item["snippet"]["title"],
            "views": item["statistics"]["viewCount"],
            "likes": item["statistics"]["likeCount"],
            "comments": item["statistics"]["commentCount"]}

# Dùng: results = youtube_search("AI tools 2026", os.environ["YOUTUBE_API_KEY"])
```

### OpenClaw (npm/ClawHub)
```bash
npx -y @modelcontextprotocol/server-youtube
# Set YOUTUBE_API_KEY trong env
```

### Antigravity (deploy nếu cần self-host)
```bash
# Không cần deploy — Google API public
# Lấy key: console.cloud.google.com → YouTube Data API v3
```
> ⚠️ Free 10,000 units/ngày. 1 search = 100 units. Đủ cho ~100 search/ngày.
