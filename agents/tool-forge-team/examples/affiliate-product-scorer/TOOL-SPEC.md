# TOOL-SPEC — Affiliate Product Scorer (VÍ DỤ MINH HOẠ)

> Ví dụ dựng từ một quy trình affiliate 4 giai đoạn của chủ. Đây là **spec**, chưa có code, chưa chạy. Chỗ gắn `GIẢ ĐỊNH` là Claude đề xuất, chưa kiểm chứng. Chủ phải duyệt trước khi giao tay.

- **Task id:** TF-EXAMPLE-01-affiliate-scorer
- **Mức:** B (công cụ nội bộ lặp lại; có thể lên C nếu đóng gói cho khách). Lý do: chủ dùng hằng tuần để lọc sản phẩm, chưa có dữ liệu nhạy cảm.

## 1. Một câu

**Nhập số liệu một sản phẩm affiliate → ra điểm khả thi, giá trị kỳ vọng mỗi 1.000 lượt xem và kết luận GO / HOLD / NO-GO kèm lý do → cho chủ và người làm kênh chọn sản phẩm làm video.**

## 2. Vấn đề thật

Quy trình chấm điểm có sẵn nhưng phải tính tay từng sản phẩm và dễ cảm tính. Công thức EV1000 và MVS còn trống ở bản copy; kết luận GO/NO-GO không lưu lại để so sánh.

## 3. Đầu vào (mỗi sản phẩm một dòng)

Tên sản phẩm; nền tảng (tiktok_shop | shopee | cpa); loại (ecom | digital); CTR_link (%); CVR_product (%); hoa hồng ròng một đơn (VNĐ hoặc USD); tỉ lệ hoa hồng (%); điểm vendor (sao); tỉ lệ phản hồi chat (%); tỉ lệ hủy/hoàn (%); tồn kho; điểm C, V, L, P (1 đến 10); tỉ lệ đánh giá 1-2 sao về chất lượng (%); cờ kill-switch (danh mục cấm; vendor giảm hoa hồng đơn phương).

## 4. Đầu ra

Bảng xếp hạng các sản phẩm đã chấm, mỗi dòng: FS, EV1000, kết luận, lý do, các ngưỡng cứng không đạt. Xuất CSV.

## 5. Hợp đồng JSON

Đầu vào một sản phẩm:
```json
{
  "ten": "Giá đỡ laptop gập",
  "nen_tang": "tiktok_shop",
  "loai": "ecom",
  "ctr_link": 2.5,
  "cvr_product": 3.0,
  "hoa_hong_rong": 60000,
  "ti_le_hoa_hong": 15,
  "vendor_sao": 4.8,
  "phan_hoi_chat": 92,
  "ti_le_huy_hoan": 4,
  "ton_kho": 2000,
  "diem": { "C": 6, "V": 9, "L": 8, "P": 7 },
  "danh_gia_xau_chat_luong": 5,
  "kill_switch": { "danh_muc_cam": false, "vendor_giam_hoa_hong": false }
}
```
Đầu ra:
```json
{
  "ten": "Giá đỡ laptop gập",
  "fs": 7.70,
  "ev1000": 45000,
  "ket_luan": "HOLD",
  "ly_do": ["FS 7.70 nằm trong khoảng 6.5 đến 8.0", "V = 9 đạt, nhưng C = 6 kéo điểm xuống"],
  "khong_dat_nguong_cung": []
}
```
Lỗi: `{ "loi": "Điểm V phải từ 1 đến 10", "truong": "diem.V" }`

## 6. Công thức

| Tên | Công thức | Trạng thái |
|---|---|---|
| FS | FS = 0.20 × C + 0.35 × V + 0.20 × L + 0.25 × P | Trọng số lấy từ tài liệu gốc |
| EV1000 | EV1000 = 1000 × (ctr_link / 100) × (cvr_product / 100) × hoa_hong_rong | Suy ra từ định nghĩa CTR, CVR, hoa hồng ròng trong tài liệu gốc. Đơn vị theo tiền đầu vào |
| MVS | MVS = 0.40 × D + 0.35 × U + 0.25 × L_ngách (D: dung lượng, U: unit economics, L_ngách: vòng đời, mỗi trục 1 đến 10) | **GIẢ ĐỊNH.** Tài liệu gốc không ghi trọng số. Chủ chỉnh |

Kiểm tay ca ví dụ ở mục 5: FS = 0.20×6 + 0.35×9 + 0.20×8 + 0.25×7 = 1.2 + 3.15 + 1.6 + 1.75 = **7.70** → HOLD. EV1000 = 1000 × 0.025 × 0.03 × 60000 = **45.000 VNĐ**.

## 7. Ngưỡng (vào `config.json`)

| Khoá | Giá trị | Trạng thái |
|---|---|---|
| go_fs_min, go_v_min | 8.0 và 8 | Từ tài liệu gốc |
| hold_fs_min | 6.5 | Từ tài liệu gốc |
| vendor_sao_min | 4.7 | Từ tài liệu gốc |
| phan_hoi_chat_min | 85 | Từ tài liệu gốc |
| ti_le_huy_hoan_max | 6 | Từ tài liệu gốc |
| ton_kho_min | 1000 | Từ tài liệu gốc |
| danh_gia_xau_max | 8 | Từ tài liệu gốc (kill-switch) |
| ti_le_hoa_hong_min | ecom 12, digital 30 | Từ tài liệu gốc; **chưa kiểm chứng với thị trường VN** |
| ctr_chuan, cvr_chuan | 1.5 đến 4 và 2 đến 6 | Từ tài liệu gốc; chỉ để cảnh báo ngoài khoảng, không dùng để loại |
| nguong_khac | nhiều ngưỡng khác của tài liệu gốc (vd tìm kiếm tối thiểu 50.000 lượt/tháng cho từ khoá hạt nhân) | **Đề xuất, chưa kiểm chứng, có thể quá cao với ngách tiếng Việt.** Chủ chỉnh |

## 8. Ca kiểm

| # | Đầu vào | Mong đợi |
|---|---|---|
| 1 | Ví dụ mục 5 nhưng điểm {C:8, V:9, L:8, P:8} | FS = 0.20×8 + 0.35×9 + 0.20×8 + 0.25×8 = 8.35; V = 9 ≥ 8 → **GO** |
| 2 | Ví dụ mục 5 nhưng điểm {C:4, V:5, L:4, P:5} | FS = 0.8 + 1.75 + 0.8 + 1.25 = 4.6 → **NO-GO** |
| 3 | Điểm {C:7, V:7, L:7, P:7} | FS = 7.0 → **HOLD** (giữa khoảng 6.5 đến 8.0) |
| 4 | Điểm như ca 1 nhưng `danh_gia_xau_chat_luong` = 9 | **NO-GO ngay** (kill-switch, bất kể FS) |
| 5 | Điểm {C:10, V:7, L:10, P:10} | FS = 2.0 + 2.45 + 2.0 + 2.5 = 8.95 nhưng V = 7 < 8 → **HOLD**, không GO |
| 6 | Điểm {C:8, V:8, L:8, P:8} (sát ngưỡng) | FS = 8.0 đúng bằng ngưỡng, V = 8 → **GO** |

## 9. Tool KHÔNG làm

- Không tự lấy số liệu từ TikTok Shop/Shopee (chủ nhập tay hoặc dán CSV).
- Không tự gắn link affiliate hay đăng bài. Phần video, disclosure, compliance đi qua `agents/shorts-affiliate-system/` và `agents/yt-cashcow/` (công cụ này chỉ là cổng chọn sản phẩm phía trước).
- Không đưa ra lời khuyên đầu tư hay cam kết doanh thu.

## 10. Dữ liệu và bảo mật

Không dữ liệu nhạy cảm. Lưu danh sách đã chấm trên Supabase hoặc file cục bộ, chủ chọn (`CHƯA CÓ — hỏi CEO`). Không gọi LLM (logic thuần code). Không gói ngoài ngoài thư viện chuẩn và một thư viện đọc CSV.

## 11. Giao việc

| Tay | Vùng | Việc |
|---|---|---|
| DSH | `logic/` | Hàm chấm FS, EV1000, kill-switch, ngưỡng cứng; test 5 ca; đọc ngưỡng từ `config.json` |
| Antigravity | `ui/`, `deploy/` | Trang một file: form nhập, bảng xếp hạng, xuất CSV, dùng được trên điện thoại; deploy sau QA ĐẠT và OK |

## 12. Giả định

- Trọng số MVS (mục 6).
- Tool dùng một tiền tệ cho `hoa_hong_rong` mỗi lần chạy, chủ tự chọn VNĐ hoặc USD.
- Ngưỡng ở mục 7 chưa kiểm chứng với thị trường Việt Nam.

## 13. Liên quan kho

`agents/shorts-affiliate-system/`, `agents/yt-cashcow/` (phần video và tuân thủ phía sau). Chưa tra Thủ Kho cho phần chấm điểm: **cần tra trước khi giao dựng mới.**
