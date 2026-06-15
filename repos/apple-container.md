# apple/container — Linux Containers Trên Mac, By Apple (37k⭐)

**GitHub:** https://github.com/apple/container
**Stars:** 37k⭐ | **License:** Apache 2.0 | **By:** Apple
**Requires:** macOS 26 + Apple Silicon

---

## Đây Là Gì

Apple's native tool chạy Linux containers như lightweight VMs trên Mac. OCI-compatible — dùng được mọi Docker image. Nhanh hơn Docker Desktop vì native Swift.

---

## Commands

```bash
container pull ubuntu:24.04
container run -it ubuntu:24.04 bash
container build -t my-app .
container push my-app registry.example.com/my-app:latest
```

---

## Dùng Cho AI Dev

```bash
container run -it python:3.12 bash  # Python env cô lập
container run -p 11434:11434 ollama/ollama  # Ollama trong container
container run -v $(pwd):/workspace -it ubuntu:24.04 bash
```

---

## So Sánh

| | apple/container | Docker Desktop |
|--|----------------|----------------|
| Speed | Faster (native) | Slower |
| Resource | Light | Heavy |
| macOS requirement | 26+ only | All |
| GUI | CLI only | Yes |

---

## Đánh Giá: 8/10

Cần macOS 26 (beta) — stable tháng 9/2026. Theo dõi ngay, khi stable là có tool thay Docker Desktop.

---
*github.com/apple/container | 37k⭐ | Apache 2.0 | Apple | tháng 6/2026*
