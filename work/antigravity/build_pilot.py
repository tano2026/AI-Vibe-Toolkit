import json
import os
import sys

sys.stdout.reconfigure(encoding="utf-8")

repo = "D:/AI-Vibe-Toolkit"

pilot_data = [
    {
        "id": "mcps/buffer-mcp",
        "capability": ["productivity"],
        "use_when": "Dùng khi cần tự động lên lịch và đăng bài viết lên nhiều kênh mạng xã hội như Twitter, LinkedIn, Facebook từ chat hoặc agent.",
        "skip_if": "Bỏ qua nếu không có tài khoản Buffer hoặc không có mã BUFFER_ACCESS_TOKEN.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "openclaw", "antigravity", "claude-code"],
        "needs": ["api-key"],
        "dup_group": "social-media-post",
        "confidence": "cao",
        "evidence": "Schedule Social Media Posts Qua Claude (Buffer GraphQL)",
    },
    {
        "id": "mcps/crawl4ai",
        "capability": ["scraping", "web-research"],
        "use_when": "Dùng khi cần cào dữ liệu web số lượng lớn hoàn toàn miễn phí và chuyển đổi thành Markdown cho AI đọc.",
        "skip_if": "Bỏ qua nếu không thể chạy Docker Desktop nền hoặc máy có RAM trống dưới 4GB.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["hermes", "openclaw", "antigravity", "claude-code"],
        "needs": ["docker"],
        "dup_group": "web-scraper",
        "confidence": "cao",
        "evidence": "Scrape web không giới hạn, chuyển thành Markdown cho AI đọc",
    },
    {
        "id": "mcps/granola",
        "capability": ["productivity", "document-office"],
        "use_when": "Dùng khi cần truy vấn trực tiếp ghi chú cuộc họp, transcript và action item từ app ghi chú họp Granola.",
        "skip_if": "Bỏ qua nếu không dùng app Granola hoặc chạy trên VPS headless không có desktop app.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["tra-phi"],
        "dup_group": "meeting-notes",
        "confidence": "cao",
        "evidence": "cho Claude đọc thẳng ghi chú cuộc họp, transcript, action item từ Granola.",
    },
    {
        "id": "mcps/mcp-youtube",
        "capability": ["web-research", "content-writing"],
        "use_when": "Dùng khi cần tải transcript phụ đề từ link video YouTube để tóm tắt và trích xuất nội dung nhanh.",
        "skip_if": "Bỏ qua nếu video không có phụ đề (caption) hoặc cần tìm kiếm video theo từ khóa.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "openclaw", "hermes"],
        "needs": ["none"],
        "dup_group": "youtube-transcript",
        "confidence": "cao",
        "evidence": "MCP cho Claude tự đọc transcript YouTube và tóm tắt video chỉ bằng cách dán link",
    },
    {
        "id": "mcps/notebooklm-mcp-roomifields",
        "capability": ["productivity", "web-research", "document-office"],
        "use_when": "Dùng khi cần kết nối NotebookLM qua MCP, REST API hoặc Docker để truy vấn tài liệu và tự động hóa kiến thức.",
        "skip_if": "Bỏ qua nếu chỉ cần truy vấn đơn giản trong Claude Code hoặc không có tài khoản Google.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["openclaw", "claude-code"],
        "needs": ["browser", "docker"],
        "dup_group": "notebooklm-integration",
        "confidence": "cao",
        "evidence": "Power User Version: MCP + HTTP REST API + Docker",
    },
    {
        "id": "mcps/scrptly",
        "capability": ["video-generation"],
        "use_when": "Dùng khi cần tạo video AI từ mô tả văn bản kèm ảnh tham chiếu ngữ cảnh và giới hạn ngân sách chi phí.",
        "skip_if": "Bỏ qua nếu không có API key của Scrptly hoặc cần kết quả đồng bộ tức thì không qua polling.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "openclaw", "claude-code", "antigravity"],
        "needs": ["api-key", "tra-phi"],
        "dup_group": "ai-video-generation",
        "confidence": "cao",
        "evidence": "1 prompt văn bản + ảnh ngữ cảnh tùy chọn ra video chuyên nghiệp, có cơ chế duyệt ngân sách token",
    },
    {
        "id": "mcps/tiktok-mcp",
        "capability": ["ads", "productivity"],
        "use_when": "Dùng khi cần đăng bài, lên lịch nội dung video và theo dõi quảng cáo TikTok qua dịch vụ bên thứ ba như Outstand hoặc Pipeboard.",
        "skip_if": "Bỏ qua nếu tìm MCP chính thức từ TikTok hoặc không muốn trả phí thuê bao bên thứ ba.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code"],
        "needs": ["api-key", "tra-phi"],
        "dup_group": "social-media-post",
        "confidence": "cao",
        "evidence": "Muốn dùng THẬT ngay bây giờ phải qua bên thứ 3: **Outstand** (post nội dung, đã live từ 3/2026) hoặc **Pipeboard**",
    },
    {
        "id": "repos/agent-browser",
        "capability": ["browser-automation"],
        "use_when": "Dùng khi cần tự động mở trình duyệt thật để kiểm thử giao diện, click form và xác minh luồng web cho AI agent.",
        "skip_if": "Bỏ qua nếu cần tính năng kiểm thử phức tạp như network mock, multi-tab hoặc xuất file PDF.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["openclaw", "claude-code"],
        "needs": ["browser"],
        "dup_group": "browser-testing",
        "confidence": "cao",
        "evidence": "CLI browser automation cho AI agent — Claude Code tự mở trình duyệt thật, click, test app vừa code",
    },
    {
        "id": "repos/ai-auto-generate-video",
        "capability": ["video-render", "video-generation", "voice-tts"],
        "use_when": "Dùng khi cần tự động chuyển bài viết tiếng Việt thành video ngắn 9:16 có voiceover và template đồ họa hoàn chỉnh.",
        "skip_if": "Bỏ qua nếu máy chưa cài FFmpeg, Chrome và chưa khởi chạy server OmniVoice local.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["claude-code", "openclaw"],
        "needs": ["browser"],
        "dup_group": "text-to-short-video",
        "confidence": "cao",
        "evidence": "Pipeline tu dong: bai viet tieng Viet (URL hoac .txt) → video 9:16 hoan chinh trong vai phut.",
    },
    {
        "id": "repos/ai-video-generator-claude",
        "capability": ["prompt-skill-library", "video-generation"],
        "use_when": "Dùng khi cần bộ skill tạo prompt quay video chuyên nghiệp (góc máy, ánh sáng, âm thanh) cho mô hình sinh video.",
        "skip_if": "Bỏ qua nếu tìm công cụ tự render ra video hoặc không có tài khoản dịch vụ sinh video như Higgsfield.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "deepseek-harness"],
        "needs": ["claude-code-only"],
        "dup_group": "video-prompt-generator",
        "confidence": "cao",
        "evidence": "10 skill viết prompt cho Seedance 2.0 (qua Higgsfield) — mô tả ý tưởng ngắn, ra prompt 15-25 dòng chuẩn production",
    },
    {
        "id": "repos/aos-ce",
        "capability": ["agent-framework", "security-compliance"],
        "use_when": "Dùng khi cần lớp hạ tầng quản lý quyền hạn (least-privilege capsule), audit trail và phê duyệt an toàn cho AI agent.",
        "skip_if": "Bỏ qua nếu chỉ cần một agent độc lập hoặc chạy trên VPS headless chưa cấu hình UI phê duyệt.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["antigravity", "openclaw", "hermes"],
        "needs": ["none"],
        "dup_group": "agent-runtime-os",
        "confidence": "cao",
        "evidence": "\"Hệ điều hành cho agent\" — một CLI/HTTP API viết bằng Rust, quản lý agent như OS quản lý process: capsule",
    },
    {
        "id": "repos/awesome-gpt-image-2",
        "capability": ["prompt-skill-library", "image-generation", "reference"],
        "use_when": "Dùng khi cần tham khảo hơn 2000 mẫu prompt chuẩn kèm ảnh preview để sinh ảnh chất lượng cao với GPT Image 2.",
        "skip_if": "Bỏ qua nếu tìm công cụ tự sinh ảnh hoặc không có API key để gọi model GPT Image 2.",
        "adoption": "chi-tham-khao",
        "vessel_fit": ["hermes", "openclaw", "deepseek-harness"],
        "needs": ["none"],
        "dup_group": "image-prompt-library",
        "confidence": "cao",
        "evidence": "Kho prompt lớn nhất cho GPT Image 2",
    },
    {
        "id": "repos/bitfun",
        "capability": ["agent-framework", "productivity"],
        "use_when": "Dùng khi cần một ứng dụng desktop tích hợp sẵn 4 AI agent đa năng và có thể điều khiển từ xa qua Telegram.",
        "skip_if": "Bỏ qua nếu cần giải pháp headless ổn định cho production hoặc ngại tự build từ Rust và Tauri.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["antigravity"],
        "needs": ["api-key"],
        "dup_group": "desktop-ai-agent",
        "confidence": "cao",
        "evidence": "Desktop app AI agent viết bằng Rust + Tauri, đóng gói sẵn 4 agent khác nhau",
    },
    {
        "id": "repos/capcut-tts-api",
        "capability": ["voice-tts"],
        "use_when": "Dùng khi cần tạo voiceover tiếng Việt tự nhiên bằng giọng đọc CapCut (BV074) qua script Python mà không cần mở app.",
        "skip_if": "Bỏ qua nếu cần API chính thức ổn định lâu dài hoặc không có tài khoản CapCut hợp lệ để cấu hình.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["hermes", "antigravity"],
        "needs": ["none"],
        "dup_group": "vietnamese-tts",
        "confidence": "cao",
        "evidence": "Python client goi thang CapCut TTS API — lay giong doc CapCut (giong BV074 va nhieu giong khac) ma khong can mo app.",
    },
    {
        "id": "repos/claude-code-skills-list",
        "capability": ["prompt-skill-library", "reference"],
        "use_when": "Dùng khi cần tra cứu danh sách 20 skill tuyển chọn cho Claude Code theo 6 nhóm nghiệp vụ để tăng năng lực cho agent.",
        "skip_if": "Bỏ qua nếu không sử dụng Claude Code làm môi trường làm việc chính.",
        "adoption": "chi-tham-khao",
        "vessel_fit": ["claude-code"],
        "needs": ["claude-code-only"],
        "dup_group": "claude-skills-collection",
        "confidence": "cao",
        "evidence": "List 20 skills tốt nhất cho Claude Code chia theo 6 categories.",
    },
    {
        "id": "repos/claude-remotion-skill",
        "capability": ["video-render", "prompt-skill-library"],
        "use_when": "Dùng khi cần dạy Claude Code dựng video motion graphics, reel và typography bằng Remotion theo quy tắc chuyển động chuẩn.",
        "skip_if": "Bỏ qua nếu không dùng Remotion hoặc muốn tránh ràng buộc bản quyền thương mại của Remotion.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["claude-code", "openclaw"],
        "needs": ["claude-code-only"],
        "dup_group": "remotion-motion-skills",
        "confidence": "cao",
        "evidence": "Dạy Claude dựng motion graphics, reel/Shorts, caption chạy chữ, kinetic typography bằng Remotion",
    },
    {
        "id": "repos/continue",
        "capability": ["agent-framework", "reference"],
        "use_when": "Dùng khi cần tham khảo kiến trúc coding agent mã nguồn mở hoặc cấu trúc thư mục quy tắc .continue cho IDE.",
        "skip_if": "Bỏ qua nếu cần một coding agent đang được bảo trì tích cực cho môi trường production.",
        "adoption": "chi-tham-khao",
        "vessel_fit": [],
        "needs": ["none"],
        "dup_group": "coding-agent",
        "confidence": "cao",
        "evidence": "Pioneering open-source coding agent từ 2023",
    },
    {
        "id": "repos/deepseek-harness",
        "capability": ["agent-framework", "devops"],
        "use_when": "Dùng khi cần harness mã nguồn mở điều phối coding agent với kiến trúc plugin toàn diện (model, tool, sandbox, UI).",
        "skip_if": "Bỏ qua nếu cần hệ thống ổn định cho production ngay hoặc ngại đối mặt với breaking changes liên tục.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "openclaw", "hermes", "antigravity"],
        "needs": ["api-key"],
        "dup_group": "coding-agent-harness",
        "confidence": "cao",
        "evidence": "Đối thủ mã nguồn mở của Claude Code, do chính DeepSeek AI làm",
    },
    {
        "id": "repos/dramaclaw",
        "capability": ["video-generation", "video-render"],
        "use_when": "Dùng khi cần sản xuất phim ngắn hoặc đoản kịch AI tự động từ kịch bản văn học (tạo storyboard, lồng tiếng và dựng clip).",
        "skip_if": "Bỏ qua nếu không thể chạy Docker, VPS dưới 4GB RAM hoặc không có DC gateway key.",
        "adoption": "can-ha-tang",
        "vessel_fit": ["hermes", "openclaw", "antigravity"],
        "needs": ["docker", "api-key"],
        "dup_group": "ai-movie-studio",
        "confidence": "cao",
        "evidence": "Xưởng phim AI mã nguồn mở: đưa vào manuscript",
    },
    {
        "id": "repos/fabric",
        "capability": ["prompt-skill-library", "productivity"],
        "use_when": "Dùng khi cần áp dụng các mẫu prompt (pattern) tối ưu sẵn từ dòng lệnh để tóm tắt, trích xuất insight hoặc xử lý văn bản.",
        "skip_if": "Bỏ qua nếu không có API key LLM hoặc cần thư viện gọi trực tiếp từ code Python không qua CLI.",
        "adoption": "cai-ngay-duoc",
        "vessel_fit": ["deepseek-harness", "openclaw"],
        "needs": ["api-key"],
        "dup_group": "prompt-pattern-cli",
        "confidence": "cao",
        "evidence": "Kho prompt AI đã qua kiểm chứng, chạy thẳng từ terminal — mỗi tác vụ chỉ cần 1 lệnh.",
    },
]

ALLOWED_CAPS = {
    "web-research", "scraping", "content-writing", "seo", "ads",
    "email-outreach", "crm-sales", "customer-support", "video-generation",
    "video-render", "image-generation", "voice-tts", "design-ui",
    "front-end", "backend", "database", "devops", "agent-framework",
    "agent-orchestration-memory", "prompt-skill-library",
    "browser-automation", "document-office", "data-dashboard",
    "finance-accounting", "ticketing-aviation", "security-compliance",
    "local-llm", "productivity", "reference"
}
ALLOWED_ADOPTION = {"cai-ngay-duoc", "can-ha-tang", "chi-tham-khao", "unknown"}
ALLOWED_VESSELS = {"hermes", "openclaw", "deepseek-harness", "antigravity", "claude-code"}
ALLOWED_NEEDS = {"api-key", "tra-phi", "vps", "gpu", "docker", "claude-code-only", "browser", "none", "unknown"}
ALLOWED_CONFIDENCE = {"cao", "vua", "thap"}

# Check against batch4 order and count
with open(os.path.join(repo, "catalog/curation-draft/batch4-chua-gan-nhan.json"), encoding="utf-8") as f:
    batch4 = json.load(f)[:20]

assert len(pilot_data) == 20, f"Expected 20, got {len(pilot_data)}"
for i in range(20):
    assert pilot_data[i]["id"] == batch4[i]["id"], f"Mismatch at index {i}: {pilot_data[i]['id']} != {batch4[i]['id']}"

errors = []
for idx, it in enumerate(pilot_data):
    iid = it["id"]
    entry_path = os.path.join(repo, iid + ".md")
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
    print("ALL 20 ITEMS PASSED MECHANICAL VALIDATION!")

out_file = os.path.join(repo, "work/antigravity/pilot20.json")
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(pilot_data, f, ensure_ascii=False, indent=2)

print(f"Successfully wrote {len(pilot_data)} items to {out_file}")
