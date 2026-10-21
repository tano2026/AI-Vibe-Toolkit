# Kho đang private: cấp quyền đọc cho từng máy

Repo `tano2026/AI-Vibe-Toolkit` là private. Máy nào chạy agent (VPS Hermes/OpenClaw, máy phụ) cần một **deploy key chỉ đọc**. Không dùng token cá nhân, không dán khoá vào prompt hay file trong repo.

## Mỗi máy làm một lần
1. Tạo khoá riêng cho máy đó (không đặt passphrase nếu chạy tự động bằng PM2):
   `ssh-keygen -t ed25519 -f ~/.ssh/kho_deploy -C "kho-readonly-<ten-may>" -N ""`
2. Trên GitHub: repo > Settings > Deploy keys > Add deploy key. Dán nội dung `~/.ssh/kho_deploy.pub`. **Không tích** "Allow write access".
3. Trỏ khoá này vào GitHub cho máy đó, thêm vào `~/.ssh/config`:
   ```
   Host github.com
     IdentityFile ~/.ssh/kho_deploy
     IdentitiesOnly yes
   ```
   (Nếu máy còn dùng GitHub cho repo khác, đặt alias `Host kho-github` và clone bằng `git@kho-github:tano2026/AI-Vibe-Toolkit.git`, đặt biến `TOOLKIT_REPO` cho `setup-vps.sh`.)
4. Kiểm: `git ls-remote git@github.com:tano2026/AI-Vibe-Toolkit.git HEAD` phải in ra một mã commit.
5. Máy đã clone bằng địa chỉ https cũ thì đổi: `git remote set-url origin git@github.com:tano2026/AI-Vibe-Toolkit.git`.

## Vì sao
- `deploy/auto-sync.sh` chạy `git fetch origin main` mỗi 6 giờ. Thiếu khoá thì mỗi lượt lỗi, ghi log rồi bỏ qua, skill đứng yên.
- Mỗi deploy key chỉ đọc được đúng repo này. Lộ khoá cũng không ai sửa được kho.
- Link raw.githubusercontent.com và link web không dùng được cho agent nữa. Agent tra kho bằng bản clone: `python tools/thu_kho.py tim "<việc cần làm>"`.
