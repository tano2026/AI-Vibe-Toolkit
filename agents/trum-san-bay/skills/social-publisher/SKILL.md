# Social Publisher — Multi-Platform Adapter

## Mô tả
Nhận 1 content core → adapt thành 5 version đúng format từng platform → package sẵn để Publisher Agent đăng.

## Quy tắc adapt

### Facebook
- Caption: đầy đủ, có thể dài (500-1500 ký tự)
- Ảnh: 1200x630px (landscape) hoặc 1080x1080 (square)
- Video: 16:9 hoặc 1:1, max 20 phút
- Hashtag: 3-5 cái, đặt cuối
- Đặc điểm: audience lớn tuổi hơn, thích nội dung có chiều sâu

### Instagram Feed
- Caption: hook + body (ẩn sau "more"), tối đa 2,200 ký tự
- Ảnh: 1080x1080 (square) hoặc 4:5 portrait
- Hashtag: 5-10, đặt sau caption hoặc comment đầu tiên
- Đặc điểm: visual quan trọng hơn text

### Instagram Reels / TikTok
- Caption: ngắn, punch, tối đa 150 ký tự hiển thị
- Video: 9:16 (1080x1920), TikTok 15-60s, Reels max 90s
- Hashtag: 3-5 trending + niche
- Hook video: 3 giây đầu quyết định xem tiếp hay không
- Text overlay trong video: quan trọng vì nhiều người xem không bật tiếng

### YouTube Shorts
- Title: 60-70 ký tự, có keyword
- Description: 2-3 dòng + link
- Video: 9:16, tối đa 60 giây
- Không cần hashtag nhiều, SEO quan trọng hơn

## Visual specs

### Ảnh template
```
Background: sân bay thật hoặc AI-gen realistic
Text overlay: hook ngắn, font bold, contrast cao
Logo: góc dưới phải, nhỏ vừa đủ
Color scheme: xanh navy + trắng + vàng (màu nhận diện Trùm Sân Bay)
```

### Video structure (9:16, 45-60s)
```
0-3s:   Hook mạnh — text overlay + voiceover
3-15s:  Problem/context
15-40s: Giải pháp / tip / hướng dẫn
40-55s: CTA
55-60s: Logo + tagline
```

## Prompt gen ảnh (SceneWorks)

```
Base prompt: "Vietnamese airport interior, modern terminal, [context], photorealistic, 
              cinematic lighting, professional photography"

Overlay: [hook text từ caption]
Style: clean, informative, không quá busy
```

## Package output format

```json
{
  "content_id": "tsb_2024_001",
  "topic": "tip check-in online",
  "pillar": "TOFU",
  "created_at": "2024-01-15T08:00:00",
  "platforms": {
    "facebook": {
      "caption": "...",
      "asset": "assets/tsb_2024_001_fb.jpg",
      "hashtags": ["#TrumSanBay", "#MeoMayBay", "#CheckIn"],
      "scheduled_time": "2024-01-16T10:00:00"
    },
    "instagram_feed": {
      "caption": "...",
      "asset": "assets/tsb_2024_001_ig.jpg",
      "hashtags": ["#TrumSanBay", "#Airport", "#TravelTips", "#MayBay", "#VietnamAirport"]
    },
    "tiktok": {
      "caption": "...",
      "video": "assets/tsb_2024_001_9x16.mp4",
      "hashtags": ["#TrumSanBay", "#MeoMayBay", "#fyp"]
    },
    "reels": {
      "caption": "...",
      "video": "assets/tsb_2024_001_9x16.mp4",
      "hashtags": ["#TrumSanBay", "#ReelsTips", "#Airport"]
    },
    "youtube_shorts": {
      "title": "Tip check-in online ít người biết | Trùm Sân Bay",
      "description": "...",
      "video": "assets/tsb_2024_001_9x16.mp4"
    }
  },
  "status": "PENDING_REVIEW"
}
```
