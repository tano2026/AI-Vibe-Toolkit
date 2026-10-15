# PLAYBOOK — Cách tận dụng kho Tano Agency

> Dành cho người và cho agent. Đọc trước khi bắt đầu **bất kỳ dự án nào**. Mất 10 phút, tiết kiệm cả tuần đi nhặt đồ.
> Danh mục đầy đủ: `catalog/CATALOG.csv` (import Notion/Sheets được) và trang tra cứu `catalog/catalog.json`. Sinh lại: `python3 tools/build_catalog.py`.

## 0. Sự thật cần nhìn thẳng (số đo ngày 15/10/2026)

- Kho có **915 mục** tra cứu được: 273 repo, 55 MCP, 18 stack, 27 skill kho, 82 skill của Pro Agent (`agents/*/skills`), 460 skill nhập hàng loạt (`skills/<tên>/SKILL.md`).
- **Chỉ ~14 mục** có chữ nói "đã chạy" (một phần hoặc đủ). **Không mục nào có bằng chứng Tano Agency đã dùng trong dự án thật** (chưa có USAGE-LOG).
- 350 mục có điểm x/10, trung bình **7,6**, và **200 mục ≥ 8**. Điểm đó là điểm sau khi **đọc**, không phải sau khi **dùng** → phồng. Đừng chọn tool chỉ vì 9/10.
- 404 mục chưa ai đánh giá (hầu hết skill nhập hàng loạt, chỉ có mô tả ngắn).

Hệ quả: kho đang là **thư viện để tra**, chưa phải **bộ đồ nghề đã kiểm**. Giá trị của một mục = số lần nó được dùng trong dự án thật, không phải số mục.

## 1. Trước khi bắt đầu một dự án (10 phút, theo thứ tự)

1. **Viết 1 câu**: "Làm [việc gì] → ra [đầu ra gì] → cho [ai] dùng". Không viết được = chưa sẵn sàng tra kho.
2. **Tách 3–5 khả năng cần** (ví dụ: nghiên cứu đối thủ, viết nội dung, làm video, lưu khách, gửi tin). Mỗi khả năng là một lượt tra.
3. **Tra từng khả năng** trong catalog: lọc `domain` + `uu_tien_agency = cao` rồi đọc cột `xac_minh`, `rui_ro`.
4. **Chọn theo thang nguồn** (tin cậy giảm dần):
   1. `agents/*/skills` — viết riêng cho Tano Agency, đã có luật
   2. `stacks/` — combo đã ghép sẵn
   3. `repos/` hoặc `mcps/` có mục **Agent Integration** và `xac_minh` ≠ `chưa chạy`
   4. `skills/*.md` của kho
   5. `skills/<tên>/SKILL.md` nhập hàng loạt — chỉ để **mượn ý**, không cài thẳng
5. **Mỗi khả năng chỉ chọn 1 ứng viên** (+1 dự phòng). Không có ứng viên nào đủ tốt → ghi vào `catalog/GAP-LOG.md`, đừng đi sưu tầm thêm ngay.
6. **Spike 30 phút trước khi cam kết**: chạy thử đúng ví dụ trong entry, ghi PASS/FAIL. FAIL thì bỏ, ghi lý do.
7. Ghi kết quả vào `catalog/USAGE-LOG.md` (mục 3 dưới đây).

## 2. Ba quy tắc chống "sưu tầm mà không dùng"

- **Quy tắc 1:3** — cứ 3 entry mới thêm vào kho phải có ít nhất 1 dòng mới trong `USAGE-LOG.md`. Chưa có thì dừng thêm.
- **Chỉ thêm khi có nhu cầu**: có dòng trong `GAP-LOG.md` hoặc có dự án sắp dùng trong 2 tuần. Còn lại → để link trong ghi chú, không viết entry.
- **Mượn ý, đừng cài hộ**: gặp repo hay → rút khung hoặc hàm hữu ích viết lại thành skill của Pro Agent (có luật, có PASS/FAIL), đừng cài nguyên bộ. Ví dụ `founder-skills`: chỉ mượn cơ chế `FOUNDER_CONTEXT.md`.

## 3. Đóng vòng sau mỗi dự án (5 phút)

Thêm 1 dòng vào `catalog/USAGE-LOG.md` cho **mỗi mục đã dùng**:

| Ngày | Mục (đường dẫn) | Dự án / khách | Kết quả (dùng được / phải sửa / bỏ) | Tiết kiệm được gì | Ghi chú |
|---|---|---|---|---|---|

Sau **2 lần "dùng được"** → đổi entry thành "đã dùng thật" và hạ/nâng điểm theo thực tế. Điểm trong kho nên dần chuyển từ "điểm đọc" sang "điểm dùng".

## 4. Dọn kho (không xoá, chỉ phân tầng)

- 158 mục có `uu_tien_agency = thấp` (chủ yếu skill ngôn ngữ/framework lập trình như Kotlin, Swift, Perl): ẩn khỏi tra cứu mặc định, **không xoá** (xoá cần Nobitano xác nhận).
- 404 mục `chưa đánh giá`: chỉ đánh giá khi có dự án sắp dùng chúng. Không ngồi chấm hàng loạt.

## 5. Cách agent dùng danh mục

```python
# Hermes: lọc catalog trong repo đã clone về VPS (không cần mạng, không cần API)
import csv

def tra_kho(domain, uu_tien="cao", bo_chua_chay=True, top=5, repo_dir="/opt/kho/AI-Vibe-Toolkit"):
    rows = list(csv.DictReader(open(f"{repo_dir}/catalog/CATALOG.csv", encoding="utf-8-sig")))
    out = [r for r in rows
           if domain in r["domain"].split(",")
           and r["uu_tien_agency"] == uu_tien
           and not (bo_chua_chay and r["xac_minh"] == "chưa chạy")]
    rank = {"có ghi đã chạy": 0, "một phần": 1, "đọc nguồn": 2, "chưa đánh giá": 3}
    out.sort(key=lambda r: (rank.get(r["xac_minh"], 9), -(float(r["diem"]) if r["diem"] else 0)))
    return [(r["ten"], r["loai"], r["xac_minh"], r["duong_dan"]) for r in out[:top]]

# vd: tra_kho("content")  →  trả 5 ứng viên + đường dẫn để đọc entry gốc trước khi dùng
```
Luật cho agent: tra xong **phải đọc entry gốc**; không cài/kích hoạt gì khi chưa có người duyệt; tìm không ra thì ghi GAP-LOG, không bịa.

## 6. Giới hạn của danh mục này

- `domain` và `uu_tien_agency` gán **tự động bằng từ khoá**, có thể sai; dùng để lọc, không phải kết luận.
- `xac_minh` đọc từ chữ trong file, là cận dưới: nhiều entry cũ có thể đã được chạy nhưng không ghi.
- Chưa có bảng "nhu cầu → mục đã tuyển chọn tay". Nên làm sau khi USAGE-LOG có vài chục dòng — chọn bằng dữ liệu dùng thật, không bằng điểm đọc.
- Catalog là ảnh chụp: chạy lại `python3 tools/build_catalog.py` sau mỗi lần thêm entry.
