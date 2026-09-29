---
name: ABTRIP
version: 0.1
status: draft — màu lấy từ logo; mục ghi "(đề xuất)" cần Nobitano chốt
colors:
  primary: "#177A99"          # teal, chữ "ab" của logo. Chữ/nút chính. 4.91:1 trên trắng
  accent: "#E8601C"           # cam, chữ "trip" của logo. CHỈ điểm nhấn, chữ lớn >=24px, icon, nền lớn. 3.43:1 trên trắng
  accent-strong: "#B8470F"    # (đề xuất) cam đậm cho chữ nhỏ hoặc nút chữ nhỏ. 5.32:1 trên trắng
  primary-dark: "#0E5A73"     # (đề xuất) hover/pressed. 7.7:1
  ink: "#1B2B32"              # (đề xuất) chữ chính. 14.6:1
  ink-muted: "#5B6B73"        # (đề xuất) chữ phụ. 5.53:1
  surface: "#FFFFFF"
  surface-alt: "#F6F8F9"      # (đề xuất)
  border: "#DCE3E7"           # (đề xuất)
  # semantic (success / warning / error): CHƯA chốt — hỏi Nobitano trước khi dùng
typography:
  family: "Be Vietnam Pro"    # (đề xuất) thiết kế cho tiếng Việt, đủ dấu. Fallback: system-ui, sans-serif
  h1: { size: 32px, line: 40px, weight: 700 }
  h2: { size: 20px, line: 28px, weight: 600 }
  body: { size: 16px, line: 24px, weight: 400 }
  caption: { size: 14px, line: 20px, weight: 400 }
spacing:
  base: 8px
  scale: [4, 8, 12, 16, 24, 32, 48, 64]
radius: { sm: 8px, md: 12px, lg: 16px }   # (đề xuất) theo Material Design 3
elevation: "nhẹ — 1 lớp bóng mờ cho card, không đổ bóng dày"
---

# ABTRIP — design system

## Giọng và cảm giác
Du lịch và đặt vé cho khách cá nhân: ấm, thân thiện, dễ hiểu. Câu ngắn, không thuật ngữ hàng không nếu không cần. Giao diện hiện đại, đơn giản, thông thoáng.

## Luật màu (không thương lượng)
- Logo viết thường: "ab" teal + "trip" cam.
- **Không dùng vàng** trong thiết kế ABTRIP.
- Cam `#E8601C` không làm chữ body. Nút CTA có chữ nhỏ dùng nền `primary` (chữ trắng 4.91:1) hoặc `accent-strong`.
- Chữ thường luôn đạt ≥ 4.5:1 với nền.

## Layout
Tối đa 2 font, 3 cấp hierarchy mỗi màn. Card nền trắng trên `surface-alt`, viền `border`, radius `md`.

## Chưa chốt (hỏi Nobitano)
Semantic colors, font chính thức, có dark mode không.
