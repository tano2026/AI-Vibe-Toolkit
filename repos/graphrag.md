# graphrag — GitHub Repo

## TL;DR
RAG dựng knowledge graph trước khi truy xuất — cách Microsoft xử lý dữ liệu riêng tư. 35,7k sao, 3,8k fork.

## Repo này dùng để làm gì
Khác RAG thường (chỉ tìm đoạn text gần giống câu hỏi), GraphRAG trích xuất thực thể (người, tổ chức, sự kiện, quan hệ giữa chúng) từ dữ liệu, dựng thành đồ thị tri thức TRƯỚC, rồi mới truy xuất trả lời. Trả lời được câu hỏi cần hiểu MỐI QUAN HỆ giữa nhiều thông tin, không chỉ tìm đoạn giống nhất.

## Setup từng bước
1. Cài: `pip install graphrag`
2. Khởi tạo workspace: `python -m graphrag.index --init --root ./ragtest`
3. Đưa tài liệu vào `ragtest/input/`, cấu hình API key trong `.env`
4. Chạy index (trích thực thể + dựng graph): `python -m graphrag.index --root ./ragtest`
5. Truy vấn: `python -m graphrag.query --root ./ragtest --method global "câu hỏi"`

## Ví dụ thực tế
Research Pro cần trả lời "các đối thủ Fast Track Nội Bài có quan hệ hợp tác/cạnh tranh với nhau ra sao" — RAG thường chỉ tìm đoạn text nhắc tên từng đối thủ riêng lẻ, GraphRAG dựng được đồ thị quan hệ (đối thủ A từng hợp tác với B, C là công ty con của D...) rồi trả lời câu hỏi cần nối nhiều mảnh thông tin lại.

## Lưu ý / Lỗi thường gặp
- Chi phí index cao hơn RAG thường nhiều — bước trích thực thể + dựng graph tốn nhiều lệnh gọi LLM hơn embedding thường
- Hợp cho câu hỏi cần hiểu MỐI QUAN HỆ tổng thể (global query), không phải câu hỏi tra cứu đơn giản (dùng RAG thường rẻ hơn, đủ dùng)
- Cần dữ liệu đủ lớn mới thấy lợi thế — dữ liệu nhỏ thì overhead dựng graph không đáng

## Đánh giá cá nhân
- Điểm mạnh: giải quyết đúng hạn chế của RAG thường (không thấy được quan hệ giữa các mảnh thông tin), từ Microsoft nên có nghiên cứu/support nghiêm túc
- Điểm yếu: chi phí index cao, phức tạp hơn llama_index nhiều — không nên dùng nếu chỉ cần tra cứu đơn giản
- Có nên dùng: 6/10 — chỉ đáng dùng khi câu hỏi thật sự cần hiểu quan hệ phức tạp (bản đồ cạnh tranh, quan hệ đối tác), không cần cho tra cứu thông thường

## Link
- Repo: https://github.com/microsoft/graphrag
