# llama_index — GitHub Repo

## TL;DR
Biến kho tài liệu riêng thành agent trả lời được thật — xương sống cho RAG (Retrieval-Augmented Generation) đúng nghĩa. 51,9k sao, 8,1k fork.

## Repo này dùng để làm gì
Kết nối dữ liệu riêng (PDF, docs, database, kho markdown...) với LLM để build agent/chatbot tra cứu tài liệu, pipeline truy xuất thông minh. Khác GPT thường (chỉ biết kiến thức đã train), llama_index cho AI đọc đúng tài liệu của mày rồi mới trả lời — không bịa, có nguồn.

## Setup từng bước
1. Cài: `pip install llama-index`
2. Đưa tài liệu vào 1 thư mục (`data/`)
3. Code cơ bản:
```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("data").load_data()
index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Câu hỏi về tài liệu của mày")
print(response)
```
4. Có thể đổi vector store (Pinecone, Chroma, Weaviate...) và LLM backend tuỳ nhu cầu

## Ví dụ thực tế
Áp cho kho AI-Vibe-Toolkit: đưa toàn bộ 320+ file .md vào llama_index, hỏi "skill nào xử lý deal scoring" — trả lời đúng chỗ trong `sales-ceo/skills/deal-scoring-forecast-discipline` kèm trích đoạn, thay vì phải tự search GitHub API như đang làm thủ công.

## Lưu ý / Lỗi thường gặp
- Cần vector store để scale — bản mặc định (in-memory) chỉ hợp thử nghiệm, kho lớn cần Pinecone/Chroma
- Chi phí embedding tính theo token — kho càng lớn, lần index đầu càng tốn
- Update tài liệu phải re-index (không tự động đồng bộ)

## Đánh giá cá nhân
- Điểm mạnh: chuẩn công nghiệp cho RAG, cộng đồng lớn, tài liệu đầy đủ, tích hợp được hầu hết vector store/LLM phổ biến
- Điểm yếu: setup production (chunking strategy, re-rank, vector store) cần đọc kỹ hơn code mẫu — không phải cắm là chạy tối ưu ngay
- Có nên dùng: 9/10 — đúng công cụ nếu muốn Research Pro/Content Pro tự tra cứu kho thay vì gọi GitHub API từng lần

## Link
- Repo: https://github.com/run-llama/llama_index
