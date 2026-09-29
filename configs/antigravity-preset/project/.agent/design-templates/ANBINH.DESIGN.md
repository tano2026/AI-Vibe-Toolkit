---
name: An Bình
version: 0.1
status: draft — màu lấy từ logo; mục ghi "(đề xuất)" cần Nobitano chốt
tagline: "The quiet difference."
colors:
  primary: "#006885"          # teal logo. 6.33:1 trên trắng
  primary-dark: "#004A5E"     # (đề xuất) hover/pressed. 9.81:1
  gold: "#DBA410"             # ngôi sao logo. TRANG TRÍ/logo. KHÔNG làm chữ trên trắng (2.25:1) hay trên teal (2.81:1)
  surface-dark: "#00303D"     # (đề xuất) nền tối cho khối nhấn. Chữ vàng trên nền này 6.26:1
  ink: "#1B2B32"              # (đề xuất) chữ chính. 14.6:1
  ink-muted: "#5B6B73"        # (đề xuất) chữ phụ. 5.53:1
  surface: "#FFFFFF"
  surface-alt: "#F6F8F9"      # (đề xuất)
  border: "#DCE3E7"           # (đề xuất)
  # semantic (success / warning / error): CHƯA chốt — hỏi Nobitano trước khi dùng
typography:
  family: "Be Vietnam Pro"    # (đề xuất) đủ dấu tiếng Việt. Fallback: system-ui, sans-serif
  h1: { size: 32px, line: 40px, weight: 700 }
  h2: { size: 20px, line: 28px, weight: 600 }
  body: { size: 16px, line: 24px, weight: 400 }
  caption: { size: 14px, line: 20px, weight: 400 }
spacing:
  base: 8px
  scale: [4, 8, 12, 16, 24, 32, 48, 64]
radius: { sm: 6px, md: 10px, lg: 14px }   # (đề xuất) góc nhỏ hơn ABTRIP cho cảm giác nghiêm túc
elevation: "rất nhẹ — ưu tiên viền mảnh thay vì đổ bóng"
---

# An Bình — design system

## Giọng và cảm giác
Dịch vụ sân bay cho doanh nghiệp và cơ quan (B2B/B2G): trang trọng, chính xác, điềm tĩnh. Câu đầy đủ, lịch sự, không đùa. Tagline "The quiet difference." — tinh tế, không phô.

## Luật màu (không thương lượng)
- **Không dùng cam** trong thiết kế An Bình.
- Vàng chỉ làm điểm nhấn trang trí (ngôi sao, đường kẻ mảnh) hoặc chữ trên `surface-dark`. Không làm chữ trên nền trắng hoặc teal.
- Chữ thường luôn đạt ≥ 4.5:1 với nền.

## Layout
Nhiều khoảng trắng, lưới chặt, viền mảnh. Tối đa 2 font, 3 cấp hierarchy mỗi màn. Dữ liệu dạng bảng phải dễ quét: căn lề nhất quán, số căn phải.

## Chưa chốt (hỏi Nobitano)
Semantic colors, font chính thức, mẫu văn bản hành chính (B2G) có cần khổ giấy A4 riêng không.
