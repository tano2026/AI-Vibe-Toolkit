---
name: info-product-claims-compliance-gate
description: >
  Gate bắt buộc chạy TRƯỚC KHI publish/bán bất kỳ digital product nào tạo ra từ
  digital-product-factory (hoặc quy trình tương tự) khi nội dung chạm ngách y tế,
  sức khoẻ, tài chính, giảm cân, làm đẹp. Chặn tuyên bố sai sự thật, thiếu
  disclaimer bắt buộc, cam kết thu nhập phi thực tế — theo đúng Nghị định
  38/2021/NĐ-CP và Nghị định 87/2026/NĐ-CP (hiệu lực 15/5/2026).
  KHÔNG nhầm với compliance-gate (agents/shorts-affiliate-system,
  agents/yt-cashcow) — cái đó lo policy "Inauthentic Content" của YouTube,
  skill này lo tuân thủ luật quảng cáo Việt Nam khi BÁN sản phẩm.
---

# Info-Product Claims Compliance Gate — Prompt Template / System Prompt

## TL;DR
Digital-product-factory (đã có trong kho) tạo ra PDF guide + trang bán hàng bằng AI trong vài phút — nhanh nhưng không tự kiểm tra nội dung có vi phạm luật quảng cáo không. Skill này là gate đứng giữa "AI viết xong" và "publish/bán", chặn các tuyên bố có thể bị phạt 5-80 triệu đồng hoặc truy cứu hình sự (Điều 197 BLHS) nếu chạm ngách y tế/tài chính.

## Khi nào dùng
- Ngay sau khi digital-product-factory (hoặc bất kỳ AI nào) tạo xong nội dung sản phẩm số, TRƯỚC KHI đăng trang bán hàng
- Đặc biệt bắt buộc với các ngách: giảm cân/giảm béo, thực phẩm chức năng, làm đẹp/da liễu, sức khoẻ tâm lý, đầu tư/tài chính cá nhân, "kiếm tiền online"
- Review lại content cũ đã đăng nếu chưa từng qua gate này

## Căn cứ pháp lý (research thật, không suy đoán)

Theo Nghị định 38/2021/NĐ-CP (Điều 34, 52) và Nghị định 87/2026/NĐ-CP (hiệu lực 15/5/2026):

| Vi phạm | Mức phạt |
|---|---|
| Quảng cáo TPCN thiếu cảnh báo "không phải là thuốc, không có tác dụng thay thế thuốc chữa bệnh" | 5-30 triệu đồng |
| Dùng trải nghiệm người bệnh/khách hàng để chứng minh hiệu quả (testimonial y tế) | 5-30 triệu đồng |
| Quảng cáo TPCN gây hiểu nhầm có tác dụng như thuốc chữa bệnh | 20-30 triệu đồng |
| Quảng cáo sai/gây nhầm lẫn về công dụng, chất lượng sản phẩm nói chung | 60-80 triệu đồng |
| Vi phạm nhiều lần trong 6 tháng | Tước giấy phép quảng cáo 22-24 tháng |
| Quảng cáo gian dối gây hậu quả nghiêm trọng | Truy cứu hình sự, Điều 197 BLHS, phạt tiền 10-100 triệu hoặc cải tạo không giam giữ tới 3 năm |

Case thật đã xảy ra: KOL bị xử phạt hành chính vì quảng cáo TPCN sai sự thật (2026); đường dây "Hoàng Minh Đường" bán ~87.000 đơn thuốc giảm cân qua mạng xã hội, mạo danh hiệp hội đông y, thu lợi bất chính hơn 227 tỷ đồng trước khi bị triệt phá.

## Nội dung skill / prompt

### Thuật toán chấm (áp code, không chỉ dặn AI "cẩn thận")

```python
def check_info_product_claims(content_text, niche):
    flags = []

    # Nhóm 1: Tuyên bố y tế/sức khoẻ tuyệt đối
    medical_absolute_terms = [
        "chữa khỏi", "trị dứt điểm", "khỏi hẳn", "chữa được bệnh",
        "thay thế thuốc", "không cần đi khám", "hiệu quả 100%"
    ]
    for term in medical_absolute_terms:
        if term in content_text.lower():
            flags.append(f"FAIL: chứa tuyên bố y tế tuyệt đối '{term}' — cần bỏ hoặc đổi thành ngôn ngữ có điều kiện")

    # Nhóm 2: Thiếu disclaimer bắt buộc (nếu niche = health/TPCN)
    if niche in ["health", "weight-loss", "supplement", "beauty"]:
        required_disclaimer = "không phải là thuốc"
        if required_disclaimer not in content_text.lower():
            flags.append("FAIL: thiếu disclaimer bắt buộc 'Sản phẩm này không phải là thuốc, "
                          "không có tác dụng thay thế thuốc chữa bệnh'")

    # Nhóm 3: Testimonial y tế không kiểm chứng được
    testimonial_patterns = ["tôi đã giảm", "bệnh nhân của tôi", "khách hàng của tôi khỏi"]
    for pattern in testimonial_patterns:
        if pattern in content_text.lower():
            flags.append(f"FAIL: dùng trải nghiệm cá nhân/bệnh nhân làm bằng chứng hiệu quả "
                          f"('{pattern}') — vi phạm dù có thật hay không, cần bỏ")

    # Nhóm 4: Cam kết thu nhập phi thực tế (niche kiếm tiền online)
    if niche == "make-money":
        income_guarantee_patterns = ["cam kết thu nhập", "chắc chắn kiếm được", "đảm bảo lợi nhuận"]
        for pattern in income_guarantee_patterns:
            if pattern in content_text.lower():
                flags.append(f"FAIL: cam kết thu nhập tuyệt đối ('{pattern}') — đổi thành "
                              f"'kết quả tuỳ thuộc nỗ lực cá nhân, không đảm bảo'")

    return ("PASS", []) if not flags else ("FAIL", flags)
```

### Nếu FAIL
Không tự sửa nội dung thay người dùng — trả về danh sách flag cụ thể, để Content Lead/Nobitano quyết định sửa câu nào. AI không tự quyết định "sửa sao cho qua" vì đây là rủi ro pháp lý, cần người chịu trách nhiệm cuối cùng xem qua.

### Nếu PASS
Vẫn khuyến nghị thêm 1 bước người thật đọc lại toàn bộ trước khi publish nếu sản phẩm thuộc niche y tế/tài chính — thuật toán trên bắt được các mẫu câu phổ biến, không bắt được mọi cách diễn đạt (paraphrase vẫn có thể lọt).

## Setup từng bước
1. Chạy ngay sau khi digital-product-factory xuất xong nội dung (Content Factory tab) và trước khi qua Copy Writer tab tạo sales page
2. Xác định `niche` của sản phẩm (health/weight-loss/supplement/beauty/make-money/khác)
3. Chạy `check_info_product_claims()` trên toàn bộ nội dung PDF + sales copy
4. FAIL → liệt kê flag cụ thể, gửi Content Lead sửa, chạy lại gate
5. PASS → nếu niche nhạy cảm, thêm bước người thật đọc lại 1 lần cuối trước khi publish

## Ví dụ thực tế
Áp cho ví dụ trong video "hanvanson" (ebook hướng dẫn giảm béo tạo bằng ChatGPT): chạy qua gate, phát hiện FAIL ở nhóm 2 (thiếu disclaimer "không phải là thuốc") nếu nội dung có nhắc tới cơ chế giảm cân, và có thể FAIL nhóm 1 nếu ChatGPT tự sinh ra câu kiểu "phương pháp này giúp giảm béo hiệu quả 100%" — cụm từ AI hay tự thêm vào để nghe thuyết phục hơn nhưng lại chính là cụm từ luật cấm.

## Lưu ý / Lỗi thường gặp
- AI (ChatGPT/Gemini/Claude) khi viết content bán hàng có xu hướng tự thêm các cụm từ tuyệt đối ("hiệu quả 100%", "chắc chắn thành công") để tăng tính thuyết phục — đây chính là cụm từ dễ vi phạm nhất, cần rà kỹ nhất
- Đừng chỉ dựa vào rule-based match cụm từ — paraphrase (nói cùng ý khác từ) vẫn lọt qua thuật toán trên, cần người đọc lại với niche nhạy cảm
- Disclaimer "không phải là thuốc" phải xuất hiện, không chỉ trong 1 dòng chữ nhỏ khó thấy — cần rõ ràng, dễ đọc
- Đừng nhầm skill này với `compliance-gate` (agents/shorts-affiliate-system, agents/yt-cashcow) — đó là gate khác, lo YouTube policy, không lo luật quảng cáo VN

## Đánh giá cá nhân
- Điểm mạnh: dựa trên nghị định thật, có số tiền phạt cụ thể để thấy rõ rủi ro không phải lý thuyết suông; thuật toán đơn giản, không cần hạ tầng nặng, chạy được ngay trong Hermes
- Điểm yếu: rule-based match cụm từ là proxy thô, không bắt được paraphrase hay ý nghĩa ngầm; cần cập nhật định kỳ khi Nghị định 87/2026 chính thức có hiệu lực đầy đủ (15/5/2026) và có thể có văn bản hướng dẫn chi tiết hơn
- Có nên dùng: 9/10 — không optional cho bất kỳ sản phẩm nào chạm ngách y tế/tài chính, đúng tinh thần "Rủi ro cao nhất" cần guardrail rõ trong Agentic Factory

## Link
- Nghị định 38/2021/NĐ-CP, Điều 34, 52
- Nghị định 87/2026/NĐ-CP (hiệu lực 15/5/2026)
- Điều 197 Bộ luật Hình sự 2015 (sửa đổi bổ sung 2017) — Tội quảng cáo gian dối

---

## 🤖 Agent Integration

### Hermes (Python, urllib thuần)
```python
# Thuật toán check_info_product_claims() ở trên là pure Python, không cần
# thư viện ngoài -- copy thẳng vào Hermes, chạy được ngay không cần pip install.

def gate_before_publish(content_text, niche):
    status, flags = check_info_product_claims(content_text, niche)
    if status == "FAIL":
        # Không tự sửa -- trả flag để người quyết định
        return {"status": "FAIL", "flags": flags, "action": "blocked_pending_human_review"}
    return {"status": "PASS", "action": "proceed_to_publish_with_final_human_check"}
```

### OpenClaw
```bash
# Gọi gate này như 1 bước bắt buộc trong pipeline digital-product-factory,
# đứng giữa Content Factory tab và Copy Writer tab (trước khi tạo sales page)
```

### Antigravity
Không cần — skill này chạy hoàn toàn trong Hermes, không đụng shell/VPS.

> ⚠️ Không bỏ qua gate này để "ra sản phẩm nhanh hơn" — mức phạt thấp nhất
> (5 triệu) đã cao hơn nhiều lợi nhuận 1 ebook bán vài chục bản, và case
> "Hoàng Minh Đường" (227 tỷ đồng, bị triệt phá hình sự) là lời nhắc thật
> về việc ngách y tế/giảm cân không phải chỗ để làm ẩu.
