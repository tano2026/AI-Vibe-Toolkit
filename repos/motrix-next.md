# Motrix Next — Download Manager Rebuilt From Scratch (7.8k⭐)

**GitHub:** https://github.com/AnInsomniacy/motrix-next
**Stars:** 7.8k⭐ | **Forks:** 218 | **License:** MIT
**Stack:** Tauri 2 (Rust) + Vue 3 + TypeScript | **Size:** ~20MB
**Website:** motrix-next.pages.dev
**Cập nhật:** 8 tiếng trước (active cực kỳ)

---

## Đây Là Gì

Download manager đầy đủ tính năng — rebuild hoàn toàn từ Motrix gốc (bị abandoned 2023).

**Tại sao dùng thay IDM hay download bình thường:**
- Multi-protocol: HTTP, FTP, ED2K, **BitTorrent, Magnet**, .torrent
- Browser extension: tự capture link download từ Chrome/Edge/Firefox
- Speed scheduling: giới hạn tốc độ theo giờ/ngày trong tuần
- 4x nhỏ hơn: ~20MB thay vì ~80MB (Electron cũ)
- SQLite history + file organization tự động

---

## So Sánh Với Motrix Cũ

| | Motrix (cũ) | Motrix Next |
|--|-------------|-------------|
| Runtime | Electron | **Tauri 2 (Rust)** |
| Frontend | Vue 2 + Vuex | **Vue 3 + Pinia** |
| Bundle size | ~80MB | **~20MB** |
| Maintenance | Abandoned 2023 | ✅ Active daily |
| Auto-update | electron-updater | Tauri updater |
| ED2K support | Basic | **Native** |

---

## Cài Đặt

```bash
# Download từ Releases
# github.com/AnInsomniacy/motrix-next/releases

# macOS
brew install --cask motrix-next  # (nếu có)
# hoặc download .dmg từ releases

# Windows
# Download .exe installer từ releases

# Linux
# Download .AppImage hoặc .deb từ releases

# Build từ source
git clone https://github.com/AnInsomniacy/motrix-next
cd motrix-next
pnpm install
pnpm tauri dev
```

---

## Browser Extension

Cài extension → mọi link download trên browser tự intercept sang Motrix Next:

- Chrome: [Chrome Web Store](https://chromewebstore.google.com/detail/ofeajdebdjajhkmcmamagokecnbephhl)
- Edge: Edge Add-ons
- Firefox: Firefox Add-ons

**Tính năng extension:**
- Smart auto-submit (tự detect file type cần intercept)
- Filename hints từ Content-Disposition headers
- Referer + cookie forwarding (bypass hotlink protection)
- Real-time controls

---

## Features Đáng Chú Ý

**BitTorrent full-featured:**
- Selective file download (chỉ lấy 1 file trong torrent)
- DHT + peer exchange
- GeoIP peer flags (thấy peers từ quốc gia nào)
- Tracker probing

**Speed Scheduler:**
```
08:00-09:00 → unlimited (sáng ít dùng net)
09:00-18:00 → 500KB/s (giờ làm việc)
18:00-23:00 → 2MB/s (buổi tối)
```

**System Integration:**
- Protocol handlers: `magnet://`, `ed2k://`, `thunder://`
- macOS Dock badge + progress bar
- Tray speed display

---

## Tại Sao Đưa Vào AI Vibe Toolkit

Download manager nghe có vẻ không liên quan — nhưng:
- **Download models** (GGUF, weights lớn vài GB) nhanh hơn
- **Download datasets** với resume support
- **BitTorrent** các dataset academic
- **Batch download** assets cho projects

Tauri 2 architecture cũng là reference tốt cho ai muốn build desktop app bằng Rust + Vue 3.

---

## Đánh Giá Cá Nhân

7.8k stars trong thời gian ngắn — community đang đói 1 download manager tốt sau khi Motrix gốc abandoned.

Tauri 2 thay Electron = 4x nhỏ hơn, nhanh hơn đáng kể. Đây là pattern đúng cho desktop apps năm 2026.

Extension integration rất smooth — cài xong quên đi, mọi thứ tự chạy.

**Rating: 8.5/10** — Best open-source download manager hiện tại.

---
*Nguồn: github.com/AnInsomniacy/motrix-next | 7.8k⭐ | MIT | tháng 6/2026*
