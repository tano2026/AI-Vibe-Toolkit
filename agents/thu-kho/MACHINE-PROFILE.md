# MACHINE-PROFILE — Hồ sơ máy (mẫu)

> Mỗi máy/VPS một bản. Lấy số liệu từ `python tools/thu_kho.py may --json`. **Không ghi giá trị khoá** — chỉ tên biến và có/không. File này an toàn để commit vì không chứa bí mật; nếu có hồ sơ chứa IP/tên khách thì đừng commit.

## Thông tin chung
| Mục | Giá trị |
|---|---|
| Tên máy | `<vd: local-win-nobitano | vps-hermes-01>` |
| Vai trò | `<máy dev cá nhân | VPS nội bộ | VPS có khách dùng>` |
| VPS có khách? | `<có/không>` → nếu có: mọi cài đặt tối thiểu L2; dùng `ke-hoach-cai --vps-co-khach` |
| Hệ điều hành | `<vd: Windows 11 (AMD64) | Ubuntu 22.04>` |
| GPU | `<không | tên GPU>` (công cụ không tự dò GPU; điền tay) |
| RAM trống điển hình | `<vd: 8GB>` (nhiều entry loại trừ khi RAM < 4GB) |
| Vessel chạy trên máy | `<hermes | openclaw | claude-code | antigravity>` |
| Ngày cập nhật | `<YYYY-MM-DD>` |

## Công cụ (từ `thu_kho.py may`)
| Công cụ | Có? | Phiên bản |
|---|---|---|
| git | `<có/không>` | `<...>` |
| node | | |
| npm | | |
| python | | |
| pip | | |
| docker | | |
| ffmpeg | | |

## Biến môi trường khoá (chỉ tên, đã đặt hay chưa)
| Tên biến | Đã đặt? | Dùng cho | Nơi giữ khoá thật |
|---|---|---|---|
| `ANTHROPIC_API_KEY` | | | `<pm2 ecosystem | .env ngoài repo | trình quản lý bí mật>` |
| `OPENAI_API_KEY` | | | |
| `GEMINI_API_KEY` | | | |
| `AIRTABLE_API_KEY` | | | |
| `TELEGRAM_BOT_TOKEN` | | | |
| `APIFY_TOKEN` | | | |
| ... | | | |

## Ràng buộc để lọc kho
Dán vào lệnh tra: `--vessel <...> --bo-can <gpu,vps,docker,...>`

| Ràng buộc | Giá trị |
|---|---|
| `--bo-can` | `<vd: gpu (nếu máy không GPU)>` |
| `--vessel` | `<vd: hermes>` |
| Ngân sách chi trả thêm | `<0đ = loại mục tra-phi; có = chờ CEO duyệt L2>` |

## Ghi chú
- Thay đổi hạ tầng (nâng VPS, thêm subscription) là L3, ghi lại ngày và người duyệt tại đây
- Hồ sơ này là *ảnh chụp tại một thời điểm*; chạy lại `thu_kho.py may` trước mỗi kế hoạch cài
