# Anthropic Cybersecurity Skills — GitHub Repo

## TL;DR
817 structured cybersecurity skill files cho AI agent — mapped với 6 framework bảo mật lớn nhất (MITRE ATT&CK, NIST CSF, MITRE ATLAS...). Chạy được với Claude Code, Cursor, Copilot, Gemini CLI và 20+ platform. 21.2K stars.

## Repo này dùng để làm gì
Security engineer hay dùng AI hỗ trợ nhưng AI thường thiếu context bảo mật chuyên sâu. Bộ skill này cung cấp 817 file prompt được cấu trúc theo từng domain:
- **Threat Intelligence:** OSINT, threat hunting, IOC analysis
- **Penetration Testing:** Recon, exploitation, post-exploitation
- **Incident Response:** Detection, containment, eradication
- **Cloud Security:** AWS/GCP/Azure security posture
- **Malware Analysis:** Static/dynamic analysis workflow
- **DevSecOps:** Security trong CI/CD pipeline

Mỗi skill map với framework chuẩn → output theo standard security community công nhận.

## Setup từng bước
```bash
# 1. Clone repo
git clone https://github.com/mukul975/Anthropic-Cybersecurity-Skills
cd Anthropic-Cybersecurity-Skills

# 2. Xem cấu trúc thư mục
ls skills/
# → threat-intel/ pentest/ incident-response/ cloud-security/ malware/ devsecops/

# 3. Dùng với Claude Code
cp -r skills/ your-project/.claude/skills/

# 4. Hoặc load skill trực tiếp
claude --skill skills/threat-intel/osint-recon.md

# 5. Dùng với Cursor
# Copy skill vào .cursor/rules/
cp skills/devsecops/sast-review.md .cursor/rules/

# 6. Chạy security audit
# Prompt: "Review code này theo OWASP Top 10"
# Prompt: "Analyze suspicious file này theo MITRE ATT&CK"
```

**29 security domains cover:**
Threat Intel, OSINT, Red Team, Blue Team, Pentest, Malware Analysis, Cloud Security, AppSec, Network Security, Cryptography, Forensics, Compliance, DevSecOps...

## Ví dụ thực tế
**Use case:** Code review bảo mật cho web app

**Skill:** `skills/devsecops/secure-code-review.md`

**Prompt:** "Review authentication module này theo OWASP Top 10 và NIST guidelines"

**Output:**
- A2: Broken Authentication → JWT không có expiry
- A3: Injection → SQL query chưa parameterize
- A7: XSS → User input render trực tiếp vào DOM
- Severity: HIGH, MEDIUM, MEDIUM
- Fix code cho từng lỗi

## Lưu ý / Lỗi thường gặp
- 817 skill là rất nhiều — không cần load hết, chọn domain liên quan
- Một số skill pentest chứa technique nhạy cảm — dùng cho ethical hacking/CTF, không phải tấn công thật
- Skill được viết theo context US/global — legal framework khác VN một số điểm
- Cần Claude Code Pro hoặc API key riêng — free tier context window không đủ cho nhiều skill

## Đánh giá cá nhân
- Điểm mạnh: Chuẩn framework thật (MITRE, NIST); 29 domain cover hầu hết mọi case; community đang đóng góp nhiều
- Điểm yếu: Overwhelming với người mới; cần background security mới dùng hiệu quả; update lag so với threat landscape mới nhất
- Có nên dùng không: **8/10** — Developer nào cũng nên có skill devsecops và OWASP review trong Claude Code setup. Full 817 skills thì cho security professional.

## Link
- Repo: https://github.com/mukul975/Anthropic-Cybersecurity-Skills
- Docs: agentskills.io standard
- Topics: mitre-attack, nist-csf, claude-code, cybersecurity, ethical-hacking
