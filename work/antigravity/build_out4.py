import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")
repo = "D:/AI-Vibe-Toolkit"

out4_data = [
    {
        "id": "repos/genoffice",
        "capability": ["document-office"],
        "use_when": "Dùng khi cần chỉnh sửa và tương tác với tài liệu Word, Excel, PowerPoint qua AI agent nhúng trực tiếp trong file.",
        "skip_if": "Bỏ qua nếu cần ứng dụng ổn định cho production hoặc không muốn dùng credit tài khoản Genspark.",
        "adoption": "can-ha-tang",
        "vessel_fit": [],
        "needs": ["api-key"],
        "dup_group": "ai-office-suite",
        "confidence": "vua",
        "evidence": "Bộ office suite AI-native mã nguồn mở (Apache-2.0) của Genspark — Docs/Sheets/Slides/PDF",
    },
    {
        "id": "repos/gsap-skills",
        "capability": ["front-end", "prompt-skill-library"],
        "use_when": "Dùng khi cần hướng dẫn coding agent viết animation web bằng thư viện GSAP đúng chuẩn và tránh lỗi rò rỉ bộ nhớ.",
        "skip_if": "Bỏ qua nếu dự án không sử dụng thư viện GSAP cho giao diện web hoặc render animation.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "antigravity"],
        "needs": ["none"],
        "dup_group": "web-animation-skills",
        "confidence": "cao",
        "evidence": "Bộ skill **chính chủ GreenSock** (MIT) dạy coding agent dùng GSAP đúng cách: 8 skill",
    },
    {
        "id": "repos/hermes-skills-hub",
        "capability": ["agent-framework", "prompt-skill-library"],
        "use_when": "Dùng khi cần tìm kiếm, cài đặt và quản lý kho kỹ năng mở rộng cho hệ thống Hermes Agent.",
        "skip_if": "Bỏ qua nếu không sử dụng Hermes Agent hoặc ngại rủi ro bảo mật từ skill của bên thứ ba.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes"],
        "needs": ["none"],
        "dup_group": "agent-skills-hub",
        "confidence": "cao",
        "evidence": "Skills Hub là \"app store\" skill cho Hermes Agent — nơi tìm, xem và cài các gói giúp agent biết làm việc cụ thể",
    },
    {
        "id": "repos/hyperframes",
        "capability": ["video-render"],
        "use_when": "Dùng khi cần render cấu trúc giao diện HTML và chuyển động CSS thành file video MP4 tự động cho agent.",
        "skip_if": "Bỏ qua nếu máy chưa cài FFmpeg, Chromium hoặc không sử dụng môi trường Claude Code.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["browser"],
        "dup_group": "html-video-renderer",
        "confidence": "cao",
        "evidence": "Viết HTML → Claude render thành video MP4. Không cần biết edit video. Built for AI agents.",
    },
    {
        "id": "repos/langflow",
        "capability": ["agent-framework"],
        "use_when": "Dùng khi cần thiết kế và thử nghiệm quy trình AI đa agent dạng giao diện kéo thả trực quan không cần code.",
        "skip_if": "Bỏ qua nếu máy có RAM dưới 8GB hoặc muốn viết code pipeline thuần để tối ưu hiệu năng.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["openclaw", "hermes"],
        "needs": ["api-key"],
        "dup_group": "visual-agent-builder",
        "confidence": "cao",
        "evidence": "Visual builder để tạo AI agent và workflow — kéo thả component, không cần code.",
    },
    {
        "id": "repos/localminidrama",
        "capability": ["video-generation", "video-render"],
        "use_when": "Dùng khi cần sản xuất phim ngắn đoản kịch nhiều tập chạy trên máy Windows từ cốt truyện đến video hoàn chỉnh.",
        "skip_if": "Bỏ qua nếu không dùng Windows, ngại giao diện tiếng Trung hoặc không có API key sinh ảnh video.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["openclaw"],
        "needs": ["api-key"],
        "dup_group": "ai-movie-studio",
        "confidence": "cao",
        "evidence": "Công cụ tạo \"đoản kịch\"/phim ngắn nhiều tập bằng AI, chạy 100% local trên máy Windows",
    },
    {
        "id": "repos/mcp-use",
        "capability": ["agent-orchestration-memory", "backend"],
        "use_when": "Dùng khi cần thư viện Python kết nối nhiều MCP server cùng lúc và xây dựng agent tự gọi công cụ theo kịch bản.",
        "skip_if": "Bỏ qua nếu chỉ cần thư viện MCP SDK chính thức của Anthropic mà không cần thêm tầng agent.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes"],
        "needs": ["none"],
        "dup_group": "mcp-client-agent",
        "confidence": "cao",
        "evidence": "Thư viện Python (kèm bản TypeScript) gói gọn \"full stack MCP\" — vừa làm MCP Client",
    },
    {
        "id": "repos/motion-dev-animations-skill",
        "capability": ["front-end", "prompt-skill-library"],
        "use_when": "Dùng khi cần tạo code hiệu ứng chuyển động và cuộn trang web bằng thư viện Motion.dev qua Claude Code.",
        "skip_if": "Bỏ qua nếu dự án không dùng Motion.dev hoặc ngại rủi ro cú pháp cũ do skill nhắm bản v11+.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["claude-code-only"],
        "dup_group": "web-animation-skills",
        "confidence": "vua",
        "evidence": "sinh code animation cho web bằng thư viện Motion.dev: hero fade-up, scroll reveal, parallax, hover lift",
    },
    {
        "id": "repos/oh-my-pi",
        "capability": ["agent-framework"],
        "use_when": "Dùng khi cần coding agent trong terminal có khả năng tự động thừa hưởng cấu hình từ Cursor, Claude Code và Cline.",
        "skip_if": "Bỏ qua nếu máy chưa cài đặt cả Bun và Rust toolchain để build native addon.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["openclaw"],
        "needs": ["api-key"],
        "dup_group": "terminal-coding-agent",
        "confidence": "cao",
        "evidence": "Coding agent chạy trong terminal, fork từ pi-mono nhưng nhồi thêm cả bộ tool đầy đủ",
    },
    {
        "id": "repos/open-webui",
        "capability": ["local-llm", "front-end"],
        "use_when": "Dùng khi cần giao diện web tự host đa người dùng để tương tác với mô hình ngôn ngữ cục bộ qua Ollama.",
        "skip_if": "Bỏ qua nếu không thể chạy Docker hoặc máy không có GPU để xử lý mô hình cục bộ.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["antigravity"],
        "needs": ["docker", "gpu"],
        "dup_group": "llm-web-ui",
        "confidence": "cao",
        "evidence": "Giao diện web đẹp, self-hosted để chạy Ollama và mọi LLM local — thay thế ChatGPT UI",
    },
    {
        "id": "repos/openwork-different-ai",
        "capability": ["agent-orchestration-memory", "agent-framework"],
        "use_when": "Dùng khi cần một lớp kết nối MCP tập trung để chia sẻ kỹ năng và công cụ cho toàn bộ nhóm làm việc.",
        "skip_if": "Bỏ qua nếu không muốn phụ thuộc dịch vụ cloud điều phối ngoài của OpenWork Labs.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "openclaw"],
        "needs": ["api-key"],
        "dup_group": "agent-shared-workspace",
        "confidence": "vua",
        "evidence": "Bản mã nguồn mở thay thế Claude Cowork",
    },
    {
        "id": "repos/penpot",
        "capability": ["design-ui"],
        "use_when": "Dùng khi cần công cụ thiết kế giao diện UI/UX tự host mã nguồn mở thay thế Figma và quản lý file bằng chuẩn web.",
        "skip_if": "Bỏ qua nếu máy có RAM dưới 4GB hoặc không muốn tự vận hành hệ thống nhiều container Docker.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["antigravity"],
        "needs": ["docker"],
        "dup_group": "ui-design-tool",
        "confidence": "cao",
        "evidence": "Design tool mã nguồn mở thay Figma — tự host được, file lưu dạng SVG/CSS/JSON",
    },
    {
        "id": "repos/product-launch-motion",
        "capability": ["video-render", "prompt-skill-library"],
        "use_when": "Dùng khi cần tạo video giới thiệu sản phẩm 45-60 giây bằng mã nguồn GSAP và HTML Canvas tự động render qua agent.",
        "skip_if": "Bỏ qua nếu máy chưa cài FFmpeg, Chrome headless hoặc không dùng Claude Code.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["claude-code-only", "browser"],
        "dup_group": "html-canvas-video",
        "confidence": "cao",
        "evidence": "dạy Claude **đạo diễn** một video launch sản phẩm khoảng 45",
    },
    {
        "id": "repos/researchtikpy",
        "capability": ["scraping", "web-research", "social-media"],
        "use_when": "Dùng khi cần thu thập dữ liệu video, tài khoản và xu hướng bình luận từ TikTok Research API chính thức.",
        "skip_if": "Bỏ qua nếu không có tài khoản và quyền truy cập TikTok Research API được cấp phép.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes"],
        "needs": ["api-key"],
        "dup_group": "tiktok-analytics-api",
        "confidence": "cao",
        "evidence": "Python wrapper cho TikTok Research API chính thức",
    },
    {
        "id": "repos/shortcast",
        "capability": ["video-render", "social-media"],
        "use_when": "Dùng khi cần tự động cắt video dài thành nhiều clip ngắn định dạng 9:16 kèm phụ đề trên máy macOS.",
        "skip_if": "Bỏ qua nếu không sử dụng hệ điều hành macOS với vi xử lý Apple Silicon.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": [],
        "needs": ["none"],
        "dup_group": "video-highlight-clipper",
        "confidence": "cao",
        "evidence": "App macOS native: thả 1 video dài vào → AI tự cắt ra 3–6 đoạn dễ viral, tự caption, tự reframe dọc 9:16",
    },
    {
        "id": "repos/stirling-pdf",
        "capability": ["document-office"],
        "use_when": "Dùng khi cần công cụ tự host để gộp, tách, nén, chuyển đổi và OCR tài liệu PDF đảm bảo quyền riêng tư dữ liệu.",
        "skip_if": "Bỏ qua nếu không thể chạy Docker hoặc chỉ cần xử lý vài tài liệu đơn giản qua tiện ích có sẵn.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["antigravity"],
        "needs": ["docker"],
        "dup_group": "pdf-toolkit",
        "confidence": "cao",
        "evidence": "Self-hosted web app xử lý mọi thứ liên quan đến PDF: merge, split, compress, convert, OCR, sign",
    },
    {
        "id": "repos/swe-agent",
        "capability": ["agent-framework"],
        "use_when": "Dùng khi cần AI agent tự động đọc mã nguồn, định vị lỗi từ GitHub issue, sửa code và mở pull request.",
        "skip_if": "Bỏ qua nếu máy chưa cài Docker hoặc không có API key mô hình ngôn ngữ phù hợp.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["hermes"],
        "needs": ["docker", "api-key"],
        "dup_group": "autonomous-swe-agent",
        "confidence": "cao",
        "evidence": "Agent tự động sửa lỗi GitHub issue",
    },
    {
        "id": "repos/tradingagents",
        "capability": ["finance-accounting", "agent-framework"],
        "use_when": "Dùng khi cần mô phỏng phòng phân tích tài chính đa agent để đánh giá dữ liệu cổ phiếu và tiền số.",
        "skip_if": "Bỏ qua nếu không có API key tài chính hoặc không muốn trả chi phí gọi nhiều mô hình cùng lúc.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["hermes"],
        "needs": ["api-key"],
        "dup_group": "trading-agent-framework",
        "confidence": "cao",
        "evidence": "Framework đa-agent mô phỏng phòng giao dịch thật",
    },
    {
        "id": "repos/unsloth",
        "capability": ["local-llm"],
        "use_when": "Dùng khi cần tinh chỉnh (fine-tune) mô hình ngôn ngữ lớn nhanh hơn và tiết kiệm bộ nhớ VRAM của GPU.",
        "skip_if": "Bỏ qua nếu máy tính không có card đồ hoạ GPU NVIDIA hoặc không có nhu cầu huấn luyện mô hình.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["antigravity"],
        "needs": ["gpu"],
        "dup_group": "llm-finetuning",
        "confidence": "cao",
        "evidence": "Thư viện fine-tune LLM mã nguồn mở — tự viết lại kernel bằng Triton",
    },
    {
        "id": "repos/vieneu-tts",
        "capability": ["voice-tts"],
        "use_when": "Dùng khi cần tạo giọng đọc tiếng Việt tự nhiên và sao chép giọng nói chạy ngoại tuyến trên máy.",
        "skip_if": "Bỏ qua nếu máy có cấu hình phần cứng yếu không có GPU hỗ trợ hoặc cần dịch vụ cloud API sẵn.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "antigravity"],
        "needs": ["gpu"],
        "dup_group": "vietnamese-tts",
        "confidence": "cao",
        "evidence": "TTS tiếng Việt on-device, clone giọng tức thời",
    },
    {
        "id": "repos/yasgu",
        "capability": ["video-generation", "video-render"],
        "use_when": "Dùng khi cần tự động ráp video YouTube Shorts từ kịch bản gồm giọng đọc, video nền và phụ đề tự sinh.",
        "skip_if": "Bỏ qua nếu máy chưa cài FFmpeg và ImageMagick hoặc không có API key để sinh giọng đọc.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes"],
        "needs": ["api-key"],
        "dup_group": "text-to-short-video",
        "confidence": "cao",
        "evidence": "Auto tạo YouTube Shorts từ text/script",
    },
    {
        "id": "stacks/ai-content-stack-viet",
        "capability": ["content-writing", "prompt-skill-library"],
        "use_when": "Dùng khi cần bộ giải pháp phối hợp các công cụ AI để sản xuất nội dung bài viết tiếp thị tiếng Việt.",
        "skip_if": "Bỏ qua nếu chỉ cần một công cụ đơn lẻ hoặc không có nhu cầu làm quy trình content hoàn chỉnh.",
        "adoption": "chi-tham-khao",
        "vessel_fit": ["hermes", "openclaw", "claude-code"],
        "needs": ["none"],
        "dup_group": "content-marketing-stack",
        "confidence": "vua",
        "evidence": "Tạo content marketing chuyên nghiệp với AI — từ ý tưởng đến đăng",
    },
    {
        "id": "stacks/ploy-ai",
        "capability": ["ads", "seo", "content-writing"],
        "use_when": "Dùng khi cần tham khảo mô hình agent tự động vận hành toàn bộ hoạt động marketing trực tuyến cho website.",
        "skip_if": "Bỏ qua nếu cần giải pháp mã nguồn mở tự host hoàn chỉnh có thể triển khai sản xuất ngay.",
        "adoption": "chi-tham-khao",
        "vessel_fit": [],
        "needs": ["none"],
        "dup_group": "marketing-automation-stack",
        "confidence": "vua",
        "evidence": "AI agent tự chạy toàn bộ marketing của website",
    },
    {
        "id": "skills/ai-marketing-adoption-map",
        "capability": ["ads", "prompt-skill-library"],
        "use_when": "Dùng khi cần đánh giá hiện trạng tiếp thị của khách hàng và lập bản đồ lộ trình áp dụng công cụ AI phù hợp.",
        "skip_if": "Bỏ qua nếu không có thông tin chi tiết về hiện trạng vận hành tiếp thị của doanh nghiệp.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code", "hermes"],
        "needs": ["none"],
        "dup_group": "marketing-consulting-skill",
        "confidence": "cao",
        "evidence": "Skill tư vấn: nhận 1 mô tả về cách client (SME/cá nhân)",
    },
    {
        "id": "skills/content-research-writer",
        "capability": ["content-writing", "web-research"],
        "use_when": "Dùng khi cần quy trình viết bài chuyên sâu từ dữ liệu nghiên cứu có trích dẫn nguồn kiểm chứng rõ ràng.",
        "skip_if": "Bỏ qua nếu chỉ cần viết bài đăng ngắn đơn giản không yêu cầu kiểm chứng nguồn tài liệu.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "deepseek-harness", "hermes"],
        "needs": ["none"],
        "dup_group": "researched-content-writing",
        "confidence": "cao",
        "evidence": "Quy trình viết content (blog, báo cáo, newsletter, case study) từ nghiên cứu có nguồn rõ ràng",
    },
    {
        "id": "skills/markdown-converter",
        "capability": ["document-office", "productivity"],
        "use_when": "Dùng khi cần chuyển đổi tài liệu văn phòng (PDF, Word, Excel) sang định dạng Markdown cho AI xử lý.",
        "skip_if": "Bỏ qua nếu máy chưa cài thư viện markitdown qua công cụ quản lý gói Python.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes"],
        "needs": ["none"],
        "dup_group": "document-to-markdown",
        "confidence": "cao",
        "evidence": "Wrapper Python quanh thư viện MarkItDown (Microsoft)",
    },
    {
        "id": "skills/vox-director",
        "capability": ["video-render", "design-ui", "prompt-skill-library"],
        "use_when": "Dùng khi cần dựng video phong cách đồ họa cắt dán (Vox-style collage) từ một câu chủ đề cho agent.",
        "skip_if": "Bỏ qua nếu không sử dụng phong cách chuyển động giấy cắt dán hoặc thiếu công cụ render.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["claude-code-only"],
        "dup_group": "vox-motion-graphics",
        "confidence": "cao",
        "evidence": "Gõ 1 chủ đề (1 câu) → agent tự viết script, dựng poster collage giấy cắt dán kiểu Vox",
    },
    {
        "id": "agents/content-pro/skills/video-narrative-structure",
        "capability": ["content-writing", "video-generation", "prompt-skill-library"],
        "use_when": "Dùng khi cần dàn dựng cấu trúc kịch bản mạch lạc và cuốn hút cho video ngắn thời lượng dưới 60 giây.",
        "skip_if": "Bỏ qua nếu video thuộc dạng tin tức ngắn liệt kê hoặc tài liệu không cần cốt truyện.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code", "hermes"],
        "needs": ["none"],
        "dup_group": "short-video-script-structure",
        "confidence": "cao",
        "evidence": "Cấu trúc kể chuyện cho video ngắn (60 giây) — phân biệt Cốt truyện",
    },
    {
        "id": "agents/yt-cashcow/skills/trend-scout",
        "capability": ["web-research", "seo", "prompt-skill-library"],
        "use_when": "Dùng khi cần quét và phát hiện các chủ đề xu hướng video có tiềm năng lượt xem cao trên YouTube.",
        "skip_if": "Bỏ qua nếu hàng đợi chủ đề kịch bản vẫn còn đầy hoặc không làm nội dung video YouTube.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "claude-code"],
        "needs": ["none"],
        "dup_group": "youtube-trend-scout",
        "confidence": "cao",
        "evidence": "Dùng khi cần tìm topic mới cho video, đầu pipeline yt-cashcow",
    },
    {
        "id": "agents/trum-san-bay/skills/image-prompt-engineer",
        "capability": ["image-generation", "prompt-skill-library", "social-media"],
        "use_when": "Dùng khi cần viết câu lệnh (prompt) tạo ảnh thumbnail và bài đăng mạng xã hội theo chuẩn nhận diện thương hiệu.",
        "skip_if": "Bỏ qua nếu yêu cầu tạo video chuyển động hoặc hình ảnh không thuộc chủ đề sân bay du lịch.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code", "hermes"],
        "needs": ["none"],
        "dup_group": "brand-image-prompt",
        "confidence": "cao",
        "evidence": "Viết prompt gen ảnh chuẩn cho thumbnail Facebook/Instagram Feed — đúng bối cảnh sân bay Việt Nam",
    },
    {
        "id": "agents/trum-san-bay/skills/sentiment-classifier",
        "capability": ["customer-support", "social-media", "prompt-skill-library"],
        "use_when": "Dùng khi cần phân loại mức độ ưu tiên và cảm xúc của bình luận mạng xã hội trước khi đưa vào hàng đợi xử lý.",
        "skip_if": "Bỏ qua nếu kênh không có tương tác bình luận mới hoặc đã xử lý thủ công từng phản hồi.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "openclaw"],
        "needs": ["none"],
        "dup_group": "comment-sentiment-triage",
        "confidence": "cao",
        "evidence": "Phân loại nhanh mọi comment mới trước khi vào queue, để Reply Agent không phải đọc từng cái",
    },
    {
        "id": "agents/shorts-affiliate-system/skills/platform-disclosure-adapter",
        "capability": ["security-compliance", "social-media", "prompt-skill-library"],
        "use_when": "Dùng khi cần áp dụng quy định khai báo nội dung do AI tạo (disclosure) phù hợp với chính sách của từng nền tảng.",
        "skip_if": "Bỏ qua nếu video sản xuất hoàn toàn thủ công không sử dụng AI hoặc chưa qua bước kiểm duyệt.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "openclaw"],
        "needs": ["none"],
        "dup_group": "ai-disclosure-compliance",
        "confidence": "cao",
        "evidence": "Dùng NGAY SAU Compliance Gate, TRƯỚC khi Publisher đăng lên platform cụ thể.",
    },
    {
        "id": "agents/designer-pro/skills/design-quality-gate",
        "capability": ["design-ui", "prompt-skill-library"],
        "use_when": "Dùng khi cần kiểm tra chất lượng ấn phẩm thiết kế đồ họa (độ tương phản, vùng an toàn, bản quyền) trước khi bàn giao.",
        "skip_if": "Bỏ qua nếu ấn phẩm là bản nháp nội bộ chưa cần kiểm tra tiêu chuẩn phát hành chính thức.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "deepseek-harness"],
        "needs": ["none"],
        "dup_group": "design-qa-gate",
        "confidence": "cao",
        "evidence": "8 mục kiểm tra bắt buộc trước khi giao bất kỳ visual nào — lệch 1 mục là chưa xong",
    },
    {
        "id": "agents/infra-ops-agent/skills/production-signal-feedback-loop",
        "capability": ["devops", "agent-orchestration-memory", "prompt-skill-library"],
        "use_when": "Dùng khi cần tự động hóa việc bắt tín hiệu lỗi hạ tầng để kích hoạt nhiệm vụ xử lý sự cố trong hệ thống agent.",
        "skip_if": "Bỏ qua nếu hạ tầng chưa có hệ thống giám sát cảnh báo lỗi để cấp tín hiệu đầu vào.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["openclaw", "hermes"],
        "needs": ["none"],
        "dup_group": "ops-feedback-loop",
        "confidence": "cao",
        "evidence": "Vòng lặp khép kín — đúc kết từ infographic ADLC",
    },
    {
        "id": "agents/customer-satisfaction-pro/skills/critical-path-briefing",
        "capability": ["productivity", "customer-support", "prompt-skill-library"],
        "use_when": "Dùng khi cần lọc và tóm tắt báo cáo định kỳ của agent để chỉ nêu những việc cần người quản lý ra quyết định.",
        "skip_if": "Bỏ qua nếu người dùng yêu cầu báo cáo chi tiết toàn bộ nhật ký hoạt động của hệ thống.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code", "openclaw"],
        "needs": ["none"],
        "dup_group": "executive-briefing",
        "confidence": "cao",
        "evidence": "Nguyên tắc lọc báo cáo",
    },
    {
        "id": "agents/research-analytics-pro/skills/data-storytelling",
        "capability": ["data-dashboard", "content-writing", "prompt-skill-library"],
        "use_when": "Dùng khi cần diễn giải số liệu phân tích thành câu chuyện có hiểu biết sâu sắc và khuyến nghị hành động cụ thể.",
        "skip_if": "Bỏ qua nếu người dùng chỉ cần bảng số liệu thô hoặc biểu đồ mà không cần phần phân tích diễn giải.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code"],
        "needs": ["none"],
        "dup_group": "data-insight-storytelling",
        "confidence": "cao",
        "evidence": "Biến số liệu và analysis thành narrative có insight và recommendation hành động.",
    },
    {
        "id": "agents/anbinh-travel-ops-analyst/skills/source-evaluation",
        "capability": ["security-compliance", "web-research", "ticketing-aviation"],
        "use_when": "Dùng khi cần kiểm tra và đánh giá độ tin cậy của nguồn dữ liệu trước khi trích dẫn chính sách và quy định.",
        "skip_if": "Bỏ qua nếu câu hỏi thuộc dạng kiến thức phổ thông cố định không có khả năng bị thay đổi chính sách.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "claude-code", "hermes"],
        "needs": ["none"],
        "dup_group": "source-reliability-evaluation",
        "confidence": "cao",
        "evidence": "Chấm độ tin cậy nguồn trước khi dùng bất kỳ thông tin nào để trả lời.",
    },
]

# Validation
ALLOWED_CAPS = {
    "web-research", "scraping", "content-writing", "seo", "ads",
    "email-outreach", "crm-sales", "customer-support", "video-generation",
    "video-render", "image-generation", "voice-tts", "design-ui",
    "front-end", "backend", "database", "devops", "agent-framework",
    "agent-orchestration-memory", "prompt-skill-library",
    "browser-automation", "document-office", "data-dashboard",
    "finance-accounting", "ticketing-aviation", "security-compliance",
    "local-llm", "productivity", "reference", "social-media"
}
ALLOWED_ADOPTION = {"cai-ngay-duoc", "can-ha-tang", "chi-tham-khao", "unknown"}
ALLOWED_VESSELS = {"hermes", "openclaw", "deepseek-harness", "antigravity", "claude-code"}
ALLOWED_NEEDS = {"api-key", "tra-phi", "vps", "gpu", "docker", "claude-code-only", "browser", "none", "unknown"}
ALLOWED_CONFIDENCE = {"cao", "vua", "thap"}

# Check against batch4 items 20..57
with open(os.path.join(repo, "catalog/curation-draft/batch4-chua-gan-nhan.json"), encoding="utf-8") as f:
    batch4_rem = json.load(f)[20:]

assert len(out4_data) == 37, f"Expected 37 items, got {len(out4_data)}"
for i in range(37):
    assert out4_data[i]["id"] == batch4_rem[i]["id"], f"Mismatch at index {i}: {out4_data[i]['id']} != {batch4_rem[i]['id']}"

errors = []
for idx, it in enumerate(out4_data):
    iid = it["id"]
    p1 = os.path.join(repo, iid + ".md")
    p2 = os.path.join(repo, iid, "SKILL.md")
    entry_path = p1 if os.path.exists(p1) else p2
    if not os.path.exists(entry_path):
        errors.append(f"[{iid}] File not found: {entry_path}")
        continue
    with open(entry_path, encoding="utf-8") as fp:
        raw_text = fp.read()

    # 1. evidence check
    ev = it["evidence"]
    if len(ev) > 120:
        errors.append(f"[{iid}] evidence too long: {len(ev)} > 120")
    if ev not in raw_text:
        errors.append(f"[{iid}] evidence not exact substring of entry: {ev}")

    # 2. capability check
    caps = it["capability"]
    if not (1 <= len(caps) <= 3):
        errors.append(f"[{iid}] capability count invalid: {len(caps)}")
    for c in caps:
        if c not in ALLOWED_CAPS:
            errors.append(f"[{iid}] invalid capability: {c}")

    # 3. use_when check
    uw = it["use_when"]
    if len(uw) > 140:
        errors.append(f"[{iid}] use_when too long: {len(uw)} > 140")
    if not uw.startswith("Dùng khi cần "):
        errors.append(f"[{iid}] use_when does not start with 'Dùng khi cần ': {uw}")
    # marketing words check
    for bad in ["miễn phí", "không giới hạn", "tốt nhất", "hoàn toàn"]:
        if bad in uw.lower():
            errors.append(f"[{iid}] use_when contains marketing word '{bad}': {uw}")

    # 4. skip_if check
    si = it["skip_if"]
    if len(si) > 100:
        errors.append(f"[{iid}] skip_if too long: {len(si)} > 100")
    if not (si.startswith("Bỏ qua nếu ") or si == "unknown"):
        errors.append(f"[{iid}] skip_if does not start with 'Bỏ qua nếu ': {si}")

    # 5. adoption
    if it["adoption"] not in ALLOWED_ADOPTION:
        errors.append(f"[{iid}] invalid adoption: {it['adoption']}")

    # 6. vessel_fit
    for v in it["vessel_fit"]:
        if v not in ALLOWED_VESSELS:
            errors.append(f"[{iid}] invalid vessel: {v}")

    # 7. needs
    for n in it["needs"]:
        if n not in ALLOWED_NEEDS:
            errors.append(f"[{iid}] invalid need: {n}")

    # 8. confidence
    if it["confidence"] not in ALLOWED_CONFIDENCE:
        errors.append(f"[{iid}] invalid confidence: {it['confidence']}")

if errors:
    print(f"Validation FAILED with {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    sys.exit(1)
else:
    print("ALL 37 ITEMS IN OUT4 PASSED MECHANICAL VALIDATION!")

out_file = os.path.join(repo, "work/antigravity/out4.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(out4_data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(out4_data)} items to {out_file}")
