# AI Agents for Beginners — GitHub Repo

## TL;DR
Giáo trình miễn phí 18 bài của Microsoft dạy build AI agent từ con số 0: mỗi bài có phần đọc, ví dụ code Python (Jupyter Notebook), phần lớn có video. License MIT. Bản hiện tại dùng **Microsoft Agent Framework + Microsoft Foundry** (không còn là bản Semantic Kernel/AutoGen như nhiều bài tóm tắt cũ trên mạng). **Cảnh báo lớn nhất:** chạy code mẫu cần tài khoản Azure + model deploy trên Foundry (tốn tiền theo token), và GitHub Models (đường chạy miễn phí hồi đầu) đã bị tài liệu setup ghi là deprecated.

## Repo này dùng để làm gì
Đây là **giáo trình**, không phải thư viện hay tool để cài vào agent. Mày dùng nó để:
- Học các mẫu thiết kế agent (tool use, planning, multi-agent, metacognition, agentic RAG, memory...) theo thứ tự có hệ thống thay vì lượm lặt từ blog.
- Có sẵn notebook chạy được để chép cấu trúc: tạo agent, gắn tool, giữ hội thoại nhiều lượt, workflow nhiều bước.
- Dạy đội ngũ mới (nhân viên, cộng tác viên) cùng một nền tảng khái niệm về agent trước khi giao việc build.

Mỗi bài tự đứng được ("start wherever you like" theo README), không bắt buộc học tuần tự.

## Số liệu đã kiểm (2026-10-10)
| Mục | Giá trị | Nguồn / mức kiểm |
|---|---|---|
| Sao | ~69,8k | 📖 đọc từ trang GitHub qua fetch, **chưa đối chiếu bằng API** |
| Fork | ~23,1k | 📖 cùng nguồn |
| License | MIT | 📖 trang repo |
| Ngôn ngữ | Jupyter Notebook 99,7% | 📖 trang repo |
| Số bài | 18 (bảng trong README) | 📖 README gốc |
| Bản dịch | bảng liệt kê 54 ngôn ngữ, README ghi "50+" | 📖 trang repo |
| Release | không có | 📖 trang repo |
| Commit gần nhất | **chưa đo** (trang commits chặn robots, API từ chối) | ❓ |
| Tổng commit | 1.803 trên `main` | 📖 trang repo |

Lưu ý: có bài tóm tắt cũ ghi ~38,8k sao và 10 bài (dùng Semantic Kernel + AutoGen + GitHub Models free). Đó là ảnh chụp cũ, **không dùng được nữa**.

Trạng thái 18 bài (đọc từ bảng README): bài 1–13 đều có video; **bài 14–18 chưa có link video** (README không ghi "coming soon", chỉ để trống ô). Chưa mở từng bài để xem nội dung đã đầy đủ chưa — trừ bài 14 đã đọc.

| # | Bài |
|---|---|
| 1 | Intro to AI Agents and Agent Use Cases |
| 2 | Exploring AI Agentic Frameworks |
| 3 | Understanding AI Agentic Design Patterns |
| 4 | Tool Use Design Pattern |
| 5 | Agentic RAG |
| 6 | Building Trustworthy AI Agents |
| 7 | Planning Design Pattern |
| 8 | Multi-Agent Design Pattern |
| 9 | Metacognition Design Pattern |
| 10 | AI Agents in Production |
| 11 | Using Agentic Protocols (MCP, A2A and NLWeb) |
| 12 | Context Engineering for AI Agents |
| 13 | Managing Agentic Memory |
| 14 | Exploring Microsoft Agent Framework |
| 15 | Building Computer Use Agents (CUA) |
| 16 | Deploying Scalable Agents |
| 17 | Creating Local AI Agents |
| 18 | Securing AI Agents |

## Setup
Theo `00-course-setup/README.md` (📖 đọc từ nguồn, **chưa chạy**):

**Yêu cầu môi trường**
- Python 3.12+ (tạo venv).
- Azure CLI để đăng nhập.
- 1 Azure subscription + 1 project Microsoft Foundry có model đã deploy (ví dụ `gpt-5-mini`).
- .NET 10 SDK chỉ cần nếu chạy mẫu .NET. README chính chỉ nói "Python code samples" nên **chưa kiểm** có đủ mẫu .NET không.

**Các bước**
```bash
# 1. Clone nhẹ (bỏ thư mục bản dịch cho nhanh) rồi lấy đúng thư mục cần
git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
cd ai-agents-for-beginners
git sparse-checkout set 00-course-setup 14-microsoft-agent-framework

# 2. Python venv + thư viện
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt

# 3. Đăng nhập Azure (trên server/Codespaces dùng --use-device-code)
az login

# 4. Tạo .env từ mẫu rồi điền 2 biến chính
cp .env.example .env
#   AZURE_AI_PROJECT_ENDPOINT=<lấy ở trang Overview của project Foundry>
#   AZURE_AI_MODEL_DEPLOYMENT_NAME=<tên deployment, vd gpt-5-mini>
```
Sau đó mở notebook `*-python-agent-framework.ipynb` trong VS Code (nhớ chọn đúng Python interpreter).

**Biến tuỳ chọn theo bài** (chỉ cần khi chạy bài đó)
- Bài 5 chạy knowledge base in-memory mặc định; bài 16 chuyển sang Azure AI Search khi có cả `AZURE_SEARCH_SERVICE_ENDPOINT` và `AZURE_SEARCH_API_KEY`.
- Bài 6 và 8: `AZURE_OPENAI_ENDPOINT`, `AZURE_OPENAI_DEPLOYMENT`, `AZURE_OPENAI_API_KEY` (key là tuỳ chọn).
- Bài 8 (workflow có điều kiện, Bing grounding): `BING_CONNECTION_ID`.
- Provider tương thích OpenAI: MiniMax (`MINIMAX_API_KEY`, `MINIMAX_BASE_URL`, `MINIMAX_MODEL_ID`) tự nhận trong mẫu dùng `OpenAIChatClient`; Novita (`NOVITA_*`) thì **phải truyền tay**, mẫu không tự đọc.
- Chạy local: Foundry Local (`foundry model run phi-4-mini`) — chỉ hỗ trợ Chat Completions, không đủ Responses API.

## ⚠️ License / Bảo mật / Quyền riêng tư
- **License:** MIT, dùng và sửa tự do. Logo/nhãn hiệu Microsoft theo Trademark Guidelines riêng.
- **Chi phí:** model chạy trên Foundry tính tiền theo token. **Chưa đo** tổng chi phí để chạy hết 18 bài. Nên đặt budget alert trên Azure trước khi chạy.
- **Đường chạy miễn phí đã đổi:** tài liệu setup ghi GitHub Models là deprecated và không hỗ trợ Responses API, nên các mẫu đã chuyển hướng. Hướng dẫn cũ nào còn bảo "dùng GitHub token chạy free" thì bỏ qua.
- **Xác thực:** đa số notebook dùng `AzureCliCredential` / `DefaultAzureCredential` nên không cần API key trong `.env`. Chỉ vài bài tuỳ chọn mới cần key (Search, Azure OpenAI, MiniMax, Novita). Không commit `.env`.
- **Gửi dữ liệu ra ngoài:** dùng MiniMax/Novita nghĩa là prompt đi tới bên thứ ba. Đừng chạy dữ liệu khách hàng thật qua notebook học tập.
- **Cảnh báo SSL trên macOS:** tài liệu gợi ý tắt xác minh chứng chỉ (`connection_verify=False`) ở bài 6. Tài liệu tự nói nó giảm bảo mật. **Đừng làm vậy**; cài chứng chỉ Python (`Install Certificates.command`) hoặc dùng `truststore`.

## Ví dụ thực tế
Tình huống minh hoạ (📖 dựng từ nội dung bài, **chưa chạy**): [TÊN SẢN PHẨM] muốn có agent tư vấn khách trả lời theo chính sách nội bộ.

Lộ trình học tối thiểu, đúng thứ tự cần cho việc đó:
1. Bài 1 + 3: hiểu agent là gì, các mẫu thiết kế.
2. Bài 4 (Tool Use): cho agent gọi hàm tra cứu giá/chính sách.
3. Bài 5 (Agentic RAG): cho agent đọc tài liệu chính sách trước khi trả lời.
4. Bài 6 (Trustworthy): chặn trả lời bậy, kiểm soát đầu ra.
5. Bài 10 + 18: đưa lên production và khoá bảo mật.

Mẫu code gốc của bài 14 (📖 trích từ bài): tạo agent bằng
`AzureOpenAIChatClient(credential=AzureCliCredential()).create_agent(instructions="You are good at recommending trips to customers based on their preferences.", name="TripRecommender")`
— đổi `instructions` và `name` cho nghiệp vụ của mày là có khung đầu tiên. Bài 14 còn dạy: gắn tool là hàm Python thường, giữ hội thoại bằng thread, workflow gồm executor nối bằng edge (direct / conditional / switch-case / fan-out / fan-in), checkpoint, OpenTelemetry, và host agent LangChain/LangGraph lên Foundry.

## Lưu ý / Lỗi thường gặp
- **Tài liệu cũ trên mạng lệch bản mới:** bài viết cũ nói 10 bài, Semantic Kernel/AutoGen, GitHub Models free. Bản hiện tại là 18 bài, Microsoft Agent Framework + Foundry Agent Service V2.
- **Bài 14–18 chưa có video** → tự đọc nhiều hơn. Chưa kiểm chất lượng nội dung các bài này.
- **Tên package có thể đổi:** bài 14 không in đủ dòng import cho vài đoạn code (nguồn của `AzureOpenAIChatClient`, `OpenAIChatClient` không rõ), nên nếu chép thì phải đối chiếu `requirements.txt` của repo.
- **macOS lỗi `CERTIFICATE_VERIFY_FAILED`:** xem mục bảo mật ở trên.
- **Tải nặng nếu clone full** vì có ~54 thư mục bản dịch → luôn dùng sparse clone như ở phần Setup.
- Đây là bộ học, không phải khung production sẵn dùng: muốn chạy thật phải tự thêm xác thực, giới hạn chi phí, log, test.

## Đánh giá cá nhân
- **Điểm mạnh:** nguồn chính chủ Microsoft, miễn phí, MIT; đi từ khái niệm tới mẫu thiết kế tới production và bảo mật; có video; bản dịch nhiều thứ tiếng; cập nhật theo framework mới nhất.
- **Điểm yếu:** dính hệ sinh thái Azure (cần subscription, tính phí); toàn notebook nên khó đưa thẳng vào dự án; một số mẫu chỉ chạy trọn vẹn với Foundry; nội dung bài mới chưa có video.
- **Có nên dùng:** **8/10 làm tài liệu học**, **chưa chấm** như công cụ chạy thật vì tao chưa chạy notebook nào (chỉ đọc nguồn). Dùng khi: cần nền tảng có hệ thống về agent, hoặc dạy người mới trong đội. KHÔNG dùng khi: chỉ cần 1 agent chạy ngay (lấy framework gọn hơn), hoặc không muốn dính Azure.

## Link
- Repo: https://github.com/microsoft/ai-agents-for-beginners
- Bài setup: https://github.com/microsoft/ai-agents-for-beginners/blob/main/00-course-setup/README.md
- Khoá nền trước đó của Microsoft: Generative AI for Beginners (21 bài)
- Entry liên quan trong kho: `repos/500-ai-agents-projects.md` (danh sách agent có code theo ngành), `repos/swe-agent.md` (agent sửa issue)

---

## 🤖 Agent Integration

> Đây là giáo trình, **không có API hay endpoint**. Phần dưới chỉ giúp agent lấy đúng bài học về để đọc và kiểm môi trường trước khi chạy notebook.

### Hermes (Python)
```python
# ✅ Đã chạy thật 2026-10-10: tải README bài setup bằng urllib, thấy đủ AZURE_AI_PROJECT_ENDPOINT,
#    AZURE_AI_MODEL_DEPLOYMENT_NAME, "Python 3.12", "deprecated". Dùng làm nguồn tri thức cho agent.
import urllib.request

RAW = "https://raw.githubusercontent.com/microsoft/ai-agents-for-beginners/main"

def fetch_lesson(path: str) -> str:
    """vd: fetch_lesson('14-microsoft-agent-framework/README.md')"""
    with urllib.request.urlopen(f"{RAW}/{path}", timeout=30) as r:
        return r.read().decode("utf-8")

setup_text = fetch_lesson("00-course-setup/README.md")
```

```python
# ❓ Chưa chạy: clone nhẹ chỉ vài thư mục bài học
import subprocess

def sparse_clone(dest: str, folders: list[str]):
    url = "https://github.com/microsoft/ai-agents-for-beginners.git"
    subprocess.run(["git", "clone", "--filter=blob:none", "--sparse", url, dest], check=True)
    subprocess.run(["git", "-C", dest, "sparse-checkout", "set", *folders], check=True)

# sparse_clone("/opt/ai-agents-course", ["00-course-setup", "04-tool-use", "05-agentic-rag"])
```
> Tên thư mục bài học (ví dụ `04-tool-use`) mới chỉ suy ra từ mẫu `NN-lesson-name`; **chưa kiểm** tên thật, hãy mở bảng README để lấy đúng đường dẫn trước khi `set`.

### OpenClaw
```bash
git clone --filter=blob:none --sparse https://github.com/microsoft/ai-agents-for-beginners.git
cd ai-agents-for-beginners && git sparse-checkout set 00-course-setup
```

### Antigravity
```bash
# Kiểm môi trường trước khi chạy notebook (❓ chưa chạy). Không in giá trị biến, chỉ báo có/không.
python3 --version                     # cần 3.12+
az --version | head -1                 # cần Azure CLI
python3 - <<'EOF'
import os
for k in ("AZURE_AI_PROJECT_ENDPOINT", "AZURE_AI_MODEL_DEPLOYMENT_NAME"):
    print(k, "OK" if os.environ.get(k) else "THIẾU")
EOF
```
> ⚠️ Chưa test notebook nào trên VPS. Không đặt khoá Azure vào file trong kho; `.env` giữ ngoài git. Chạy trên VPS cần `az login --use-device-code`. Đặt budget alert Azure trước khi cho agent chạy lặp.
