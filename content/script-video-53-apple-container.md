# Script Video #53 — apple/container: Apple Làm Docker Riêng Cho Mac

**Repo:** https://github.com/apple/container | 37k⭐

## 🎬 SCRIPT

**[HOOK 0:00-0:08]**
Apple. Vừa release tool chạy Linux containers.
Native Swift. Apple Silicon. Nhanh hơn Docker Desktop.

**[PROBLEM 0:08-0:20]**
Docker Desktop trên Mac = nặng, chậm, tốn RAM.
Phải emulate Linux kernel. Apple biết. Họ fix.

**[SOLUTION 0:20-0:45]**
apple/container. Lightweight VMs, không phải emulation.
OCI compatible — dùng được mọi Docker image.

```bash
container pull ubuntu:24.04
container run -it ubuntu:24.04 bash
container build -t my-app .
```

Giống Docker syntax. Nhưng native. Nhanh hơn.

**[CATCH 0:45-1:00]**
Cần: Apple Silicon + macOS 26 (đang beta, stable tháng 9).
Theo dõi ngay. Link bio.

*Script #53 | AI Vibe Toolkit*
