# DeepSeek-R1 Local — GitHub Repo

## TL;DR
Chạy model lý luận (reasoning) DeepSeek-R1 ngay trên máy cá nhân, 100% miễn phí, không cần internet sau khi tải xong. MIT license — dùng thương mại thoải mái, không giới hạn user, không cần credit tác giả. Tháng 1/2025 là model open-weight đầu tiên ngang tầm OpenAI o1.

## Repo này dùng để làm gì
DeepSeek-R1 bản đầy đủ có 671 tỷ tham số (Mixture-of-Experts), cần ~376GB VRAM — không máy cá nhân nào chạy nổi. Nhưng DeepSeek đã "chưng cất" (distill) khả năng lý luận của nó vào 6 model nhỏ hơn nhiều (1.5B → 70B), fine-tune trên nền Qwen2.5 và Llama 3, học từ 800.000 mẫu chuỗi suy luận của bản gốc. Model nhỏ vẫn giữ được phần lớn khả năng "suy nghĩ từng bước" (hiện <think> token) trước khi trả lời — khác hẳn LLM thường chỉ nhả thẳng câu trả lời.

Cài qua **Ollama** là nhanh nhất — 1 lệnh tải, 1 lệnh chạy, có REST API sẵn để tích hợp vào code/agent.

## Setup từng bước
1. Cài Ollama (nếu chưa có) — 1 dòng lệnh theo OS, xem `repos/ollama.md` trong kho
2. Chọn size khớp phần cứng máy — bảng dưới đây là mốc thật (Q4_K_M quantization mặc định):

| Model | VRAM/RAM cần | GPU tối thiểu | Chất lượng |
|---|---|---|---|
| `deepseek-r1:1.5b` | ~2GB | Gần như máy nào cũng chạy | Thấp — chỉ để test setup |
| `deepseek-r1:7b`/`8b` | ~5.5GB VRAM, 8GB RAM | RTX 4060, RTX 3060 | Khá — mức tối thiểu nên dùng thật |
| `deepseek-r1:14b` | ~8.5GB VRAM, 16GB RAM | RTX 4070/Arc B580 12GB | Tốt |
| `deepseek-r1:32b` | ~18-20GB VRAM | RTX 3090/4090 24GB | Rất tốt — điểm ngọt cho 1 GPU |
| `deepseek-r1:70b` | ~36.5GB VRAM/RAM | Dual-GPU hoặc Mac Studio M4 Max 64GB | Cao nhất khả thi tại nhà |
| `deepseek-r1:671b` (full) | ~376GB+ | Cluster nhiều GPU | Không hợp máy cá nhân |

3. Pull model:
```bash
ollama pull deepseek-r1:8b
```
4. Chạy chat trực tiếp trong terminal:
```bash
ollama run deepseek-r1:8b
```
5. Muốn context dài hơn (mặc định 4096 token, distill hỗ trợ tới 128K, bản 671B tới 160K):
```bash
ollama run deepseek-r1:8b --num-ctx 16384
```
> Lưu ý: tăng context = tăng VRAM cần, gần như gấp đôi mỗi lần tăng context

6. Gọi qua REST API (để tích hợp code/agent) — Ollama tự expose ở `http://localhost:11434`

## Ví dụ thực tế
Máy Windows hiện tại (4 core, ~15.7GB RAM, không rõ GPU rời) — dựa bảng trên, nên bắt đầu với `deepseek-r1:7b` hoặc `8b` để test trước, đừng nhảy thẳng lên 14b/32b nếu chưa xác nhận có GPU đủ VRAM. Dùng làm brain phụ trong OmniRoute cho route "reasoning" thay/song song DeepSeek R1 API — request nào không cần tốc độ, ưu tiên tiết kiệm chi phí hoàn toàn (không tốn 1 đồng API nào), phù hợp task research/phân tích nội bộ không gấp.

## Lưu ý / Lỗi thường gặp
- Model bị Ollama tự unload khỏi RAM sau vài phút không dùng, lần gọi tiếp theo load lại chậm → set `OLLAMA_KEEP_ALIVE=30m` hoặc `-1` (giữ mãi) nếu dùng liên tục
- Đừng nhầm giữa "671B full" và "distill" — nhiều video/bài viết ẩu gọi chung là "DeepSeek-R1" khiến người xem tưởng chạy được bản full trên máy thường, thực tế 99% người dùng chỉ chạy được bản distill
- Bản 8B từ tháng 5/2025 (`deepseek-r1:8b`, cập nhật 0528) đổi nền sang Qwen3-8B, cải thiện đa ngôn ngữ — các size khác (1.5B/7B/14B/32B/70B) vẫn giữ nguyên weight gốc tháng 1/2025, chưa cập nhật
- Windows cần WSL2 hoặc bản Ollama native Windows (đều hỗ trợ, không bắt buộc WSL2 nữa)

## Đánh giá cá nhân
- Điểm mạnh: MIT license thật sự thoải mái (không giới hạn user như Llama, không cấm train model cạnh tranh như Gemma) — hợp dùng thương mại cho agency; chi phí vận hành bằng 0 sau khi tải xong, không lo rate limit hay leak API key; khả năng lý luận distill 7B/8B vẫn đủ dùng cho task phân tích không đòi hỏi cực cao
- Điểm yếu: bản mạnh nhất chạy nổi trên máy cá nhân (32B/70B) vẫn cần GPU cao cấp (RTX 4090/dual-GPU) — máy văn phòng thường không đáp ứng; tốc độ chậm hơn model thường cùng size vì phải "suy nghĩ" qua nhiều bước trước khi trả lời; distill nhỏ (1.5B-7B) chất lượng thật sự thấp hơn đáng kể so với bản full, đừng kỳ vọng ngang GPT/Claude cho task phức tạp
- Có nên dùng không: 8/10 cho use case tiết kiệm chi phí — không nên coi là thay thế hoàn toàn Claude/GPT cho việc quan trọng, nhưng làm "brain rẻ" cho task nội bộ số lượng lớn (batch research, phân loại, tóm tắt) thì rất đáng

## Link
- Repo: https://github.com/deepseek-ai/DeepSeek-R1
- Docs/Demo: https://ollama.com/library/deepseek-r1
