# Script Video 108 — AWS Agent Toolkit: Deploy AWS Bằng AI Không Cần Viết Code

## Thông tin
- Repo liên quan: /repos/agent-toolkit-for-aws.md
- Platform: TikTok / YouTube Shorts
- Thời lượng dự kiến: ~50 giây

## Hook (3 giây đầu)
"Deploy Lambda, tạo S3 bucket, config IAM — bằng một câu prompt. Official từ AWS."

## Script voiceover (ElevenLabs-ready)
[Đoạn 1 — pain point]
Deploy app lên AWS mà nhờ AI: nó hay hallucinate tên service, viết sai IAM policy, quên config region. Annoying.

[Đoạn 2 — giải pháp]
AWS vừa release Agent Toolkit chính thức — bộ MCP servers cho AI agent hiểu đúng cách dùng từng AWS service. S3, Lambda, EC2, CloudFormation — có tools sẵn, không cần AI đoán mò.

[Đoạn 3 — demo]
Prompt Claude Code: "Tạo S3 bucket này, bật versioning, block public access." Agent gọi thẳng AWS API, làm đúng, xong. Không viết một dòng boto3.

[Đoạn 4 — kết + CTA]
Official từ Amazon, không phải third-party. Đang build trên AWS? Tool này không thể thiếu. Link trong bio.

## Ghi chú quay (OBS)
- Cảnh 1: Màn hình Claude Code nhận prompt AWS
- Cảnh 2: Agent gọi MCP tools → AWS console update real-time
- Cảnh 3: S3 bucket/Lambda đã tạo xong trong console

## Thumbnail idea (Canva)
Logo AWS + Logo Claude Code + mũi tên. Text: "Deploy AWS bằng 1 câu prompt"

## CTA cuối video
"Follow để xem thêm MCP tools xịn. Link AWS Agent Toolkit trong bio."
