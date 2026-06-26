# Agent Toolkit for AWS — GitHub Repo

## TL;DR
Bộ MCP servers + skills + plugins chính thức của AWS — giúp AI agent build, deploy, và manage ứng dụng trên AWS. Official từ Amazon, không phải third-party. 1.1K stars nhưng đây là tool enterprise-grade.

## Repo này dùng để làm gì
Khi mày nhờ Claude Code deploy app lên AWS, nó hay bị confused: S3 bucket tên gì? Region nào? IAM role cần gì? Agent Toolkit for AWS giải quyết bằng cách cung cấp MCP servers có sẵn context về:
- **S3:** Upload/download, bucket management
- **Lambda:** Deploy function, invoke, logs
- **EC2:** Spin up instances, security groups
- **CloudFormation:** Infrastructure as code
- **IAM:** Role và policy management

AI agent có tool này → hiểu AWS services đúng cách, ít hallucinate hơn.

## Setup từng bước
```bash
# 1. Clone
git clone https://github.com/aws/agent-toolkit-for-aws
cd agent-toolkit-for-aws

# 2. Cài AWS CLI (nếu chưa có)
pip install awscli
aws configure  # nhập Access Key, Secret, Region

# 3. Cài toolkit
pip install -e .

# 4. Thêm vào Claude Code config
# Trong .claude/settings.json:
{
  "mcpServers": {
    "aws-toolkit": {
      "command": "python",
      "args": ["-m", "aws_agent_toolkit.server"]
    }
  }
}

# 5. Test với Claude Code
# "Deploy Lambda function từ file handler.py này lên us-east-1"
```

## Ví dụ thực tế
**Input prompt:** "Tạo S3 bucket tên 'abtrip-media-2026' ở region ap-southeast-1, bật versioning, block public access"

**Output:** Agent tự gọi AWS API → tạo bucket → config versioning → apply bucket policy. Mày không cần viết một dòng boto3 nào.

## Lưu ý / Lỗi thường gặp
- Cần AWS credentials có đủ permission — dùng IAM user riêng, không dùng root account
- Agent có thể tạo resource tốn tiền (EC2, RDS) — review trước khi confirm
- Hiện tại support tốt nhất: S3, Lambda, CloudFormation — EC2/RDS còn hạn chế
- Chỉ tương thích với Claude Code và một số agent platform chính thức

## Đánh giá cá nhân
- Điểm mạnh: Official AWS support, không lo deprecated; integration sâu với AWS SDK; guardrails có sẵn
- Điểm yếu: Còn mới (1.1K stars), một số service chưa đầy đủ; không có UI; cần biết AWS cơ bản mới dùng hiệu quả
- Có nên dùng không: **7/10** — Nếu mày đang build trên AWS và dùng Claude Code, đây là MCP bắt buộc phải có. Nếu không dùng AWS thì skip.

## Link
- Repo: https://github.com/aws/agent-toolkit-for-aws
- Docs: https://github.com/aws/agent-toolkit-for-aws#readme
