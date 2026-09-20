# PrintFilm — Research Notes (cho SaaS tương lai, KHÔNG hành động ngay)

> ⚠️ File này là GHI CHÚ NGHIÊN CỨU, không phải hướng dẫn triển khai. PrintFilm không cài đặt/dùng ngay — lưu lại kiến trúc tham khảo cho khi Tano Agency cân nhắc xây SaaS video riêng.

## TL;DR
PrintFilm là 1 platform SaaS video AI tự host — khác hẳn FlowKit (script cá nhân tự động hoá Google Flow). PrintFilm là kiến trúc **multi-user, có billing, có admin** — đáng tham khảo kiến trúc khi Tano Agency muốn làm sản phẩm SaaS bán cho khách, không phải công cụ dùng nội bộ ngay.

## Bối cảnh — nhiều fork, mục đích hơi khác nhau

| Fork | Đặc điểm |
|---|---|
| `yuanzhongqiao/printfilm` | Nền tảng "短剧" (phim ngắn/drama ngắn) — có DramaForge pipeline + canvas vô hạn (React Flow node editor) |
| `yuanzhongqiao/printfilm-pro` | Next.js 15 + Better Auth + PostgreSQL, BYOK qua GitCC API, hỗ trợ Sora 2/Veo 3.1/Wan 2.6 |
| `yi1108/printfilm` | AI popular-science video + comic platform, dùng 火山方舟 (Volcano Engine) Seedream/Seedance |
| `neuravibe-mmo/printfilm` | "AI video khách hàng + phim ngắn AI" — hướng thương mại/lead-gen rõ hơn |

## Kiến trúc đáng học (từ printfilm-pro, chi tiết nhất)

```
Frontend: Next.js 15 + Better Auth (multi-user auth có sẵn)
Backend: FastAPI (task runtime: scheduler/executor/poller)
Database: PostgreSQL (chính) + Redis (cache/session)
AI Provider: BYOK qua GitCC API (aggregator — user tự lưu key riêng,
             billing xảy ra ở phía nhà cung cấp API, không phải PrintFilm tự thu tiền model)
Storage: S3-compatible (R2/S3) + PostgreSQL fallback
Compose cuối: FFmpeg
```

## Pipeline sản xuất (DramaForge, từ yuanzhongqiao/printfilm)

```
剧本解析 (phân tích kịch bản) → 资产设计 (thiết kế nhân vật/bối cảnh/đạo cụ,
có ảnh tham chiếu để giữ nhất quán) → 分镜 (storyboard/chia cảnh) →
镜头视频 (video từng cảnh) → 合成导出 (ghép + xuất, SSE real-time progress)
```

Đúng mô hình FlowKit đã thấy (story → entity → scene → video → render), nhưng PrintFilm làm ở tầng **SaaS đa người dùng** thay vì script cá nhân.

## Mô hình kinh doanh (BYOK — đáng chú ý)

PrintFilm KHÔNG tự trả tiền model AI thay khách — khách tự lưu API key riêng (GitCC/TokenFree), billing xảy ra trực tiếp giữa khách và nhà cung cấp model. PrintFilm chỉ thu phí (nếu có) cho phần platform/hạ tầng, không gánh chi phí compute AI. Đây là mô hình đáng cân nhắc nếu Tano Agency làm SaaS tương tự — giảm rủi ro tài chính (không phải gánh chi phí AI compute biến động theo lượng dùng của khách).

## Việc cần làm khi thật sự cân nhắc xây SaaS (chưa làm bây giờ)

1. Đọc kỹ source `yuanzhongqiao/printfilm-pro` (bản Next.js, dễ đọc hơn bản FastAPI thuần Trung)
2. Đánh giá mô hình BYOK có hợp thị trường VN không (khách SMB có sẵn sàng tự quản API key riêng không, hay muốn "trọn gói" trả 1 lần)
3. So sánh chi phí tự host (PostgreSQL + Redis + S3 + compute) với việc dùng lại OpenShorts/google-flow-mcp làm backend cho sản phẩm riêng, thay vì clone nguyên PrintFilm

## Đánh giá cá nhân
- Điểm mạnh: kiến trúc BYOK giảm rủi ro tài chính, đáng học; pipeline DramaForge rõ ràng, có thể tham khảo tên gọi các bước
- Điểm yếu: toàn bộ docs tiếng Trung, nhiều fork mục đích hơi khác nhau gây khó chọn bản gốc; phụ thuộc nhà cung cấp AI Trung Quốc (火山方舟) ở 1 số fork — cần xác nhận có API tương đương dễ dùng ở VN không
- Có nên dùng NGAY: Không — đây là ghi chú cho tương lai, không phải việc cần làm bây giờ

## Link
- https://github.com/yuanzhongqiao/printfilm
- https://github.com/yuanzhongqiao/printfilm-pro
- https://github.com/yi1108/printfilm
- https://github.com/neuravibe-mmo/printfilm
- DeepWiki (đọc kiến trúc nhanh không cần đọc code): https://deepwiki.com/yuanzhongqiao/printfilm-pro
