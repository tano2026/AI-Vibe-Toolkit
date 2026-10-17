# INSTALL-PLAN — kế hoạch cài KHÔ (không thực thi)

> Kế hoạch này chỉ để người duyệt đọc. Agent Factory KHÔNG cài gì, KHÔNG chạy lệnh nào. Người duyệt đọc từng mục, đồng ý rồi tự cài.
> Mỗi mục phải qua spike 30 phút trên việc thật trước khi cam kết (ghi `catalog/USAGE-LOG.md`).

## Hồ sơ máy của người dựng hồ sơ

Đây là máy đã chạy công cụ, KHÔNG phải máy đích của khách. Chạy lại `thu_kho.machine_profile()` trên máy đích trước khi duyệt cài. Chỉ liệt kê những gì cần để đọc kế hoạch; đường dẫn, tên người dùng và biến môi trường của máy dựng được lược bỏ.

- **he_dieu_hanh**: Windows 11
- **kien_truc**: AMD64
- **python**: 3.14.4
- **cong_cu_co_san**:
  - git
  - node
  - npm
  - python
  - pip
  - docker
  - ffmpeg
- **cong_cu_thieu**: []

## `kho:skills/social-media-skills`

- **id**: skills/social-media-skills
- **ten**: Social Media Skills
- **loai_muc**: skill-kho
- **chua_chay_that**: True
- **thong_bao**: CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. Cần người duyệt trước khi cài.
- **nguon**: skills/social-media-skills.md
- **doc_entry_goc**: True
- **buoc**:
  -
    - **loai**: chep-file
    - **lenh**: (sao chép) skills/social-media-skills.md -> thư mục skills của vessel (xem agents/*-GUIDE.md của vessel)
    - **kieu**: mo-ta
    - **nguon_muc**: suy ra từ loại muc
    - **co_do**: []
    - **canh_bao_vang**: []
    - **can_nguoi_doc_ky**: False
    - **chua_chay**: True
    - **mo_ta**: Skill là file Markdown: chép thư mục skill vào nơi vessel đọc skill. Chưa kiểm cách vessel nạp.
    - **so**: 1
- **dieu_kien_tien_quyet**:
  - **can**: []
  - **thieu**: []
  - **co**: {}
  - **can_khac**: []
- **bien_moi_truong**: []
- **co_rui_ro**:
  -
    - **loai**: license
    - **noi_dung**: License chưa ghi trong kho - kiểm trước khi dùng cho khách.
  -
    - **loai**: nhan
    - **noi_dung**: Nhãn chưa dựa trên đọc nguyên entry (da-doc-dau-entry).
- **co_do**: []
- **muc_duyet**:
  - **muc**: L2
  - **ly_do**:
    - cài tool nội bộ/dự án: L1 (ghi log)
    - nhãn chưa chắc (không phải đã-đọc-entry-gốc) -> nâng lên L2 (không chắc thì coi là mức cao hơn)
  - **ghi_chu**: Không chắc mức nào thì coi là mức cao hơn. Mọi hành động đăng bài/gửi tin/chi tiền sau khi cài vẫn đi qua lằn ranh đỏ.
- **kiem_tra**:
  - **tieu_chi**: PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).
  - **vi_du_trong_entry**: Chạy `voice-builder` cho kênh **Airfare Decoded** (tiếng Anh, B2B, aviation) riêng biệt với kênh **Trùm Sân Bay** (tiếng Việt, TikTok, casual) — 2 file `voice.md` khác nhau. Sau đó mọi skill viết caption/script cho từng kênh tự động bám đúng giọng riêng, không lẫn giữa 2 kênh dù dùng chung bộ skill.
  - **lenh_goi_y**: []
- **go_cai_dat**:
  - xoá/khôi phục file đã chép (người tự làm, sao lưu trước)
- **canh_bao**:
  - Entry không có mục Setup/Cài đặt chứa khối lệnh; lệnh lấy từ mục Ví dụ - cần người đọc kỹ.
  - Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
- **lan_ranh_do**:
  - AI không tự chi tiền
  - AI không tự publish public content
  - AI không tự cam kết với khách

## `kho:skills/natural-writing`

- **id**: skills/natural-writing
- **ten**: Natural Writing — Chống văn phong "nghe như AI"
- **loai_muc**: skill-kho
- **chua_chay_that**: True
- **thong_bao**: CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. Cần người duyệt trước khi cài.
- **nguon**: skills/natural-writing.md
- **doc_entry_goc**: True
- **buoc**:
  -
    - **loai**: chep-file
    - **lenh**: (sao chép) skills/natural-writing.md -> thư mục skills của vessel (xem agents/*-GUIDE.md của vessel)
    - **kieu**: mo-ta
    - **nguon_muc**: suy ra từ loại muc
    - **co_do**: []
    - **canh_bao_vang**: []
    - **can_nguoi_doc_ky**: False
    - **chua_chay**: True
    - **mo_ta**: Skill là file Markdown: chép thư mục skill vào nơi vessel đọc skill. Chưa kiểm cách vessel nạp.
    - **so**: 1
- **dieu_kien_tien_quyet**:
  - **can**: []
  - **thieu**: []
  - **co**: {}
  - **can_khac**: []
- **bien_moi_truong**: []
- **co_rui_ro**:
  -
    - **loai**: license
    - **noi_dung**: License chưa ghi trong kho - kiểm trước khi dùng cho khách.
  -
    - **loai**: nhan
    - **noi_dung**: Nhãn chưa dựa trên đọc nguyên entry (da-doc-dau-entry).
- **co_do**: []
- **muc_duyet**:
  - **muc**: L2
  - **ly_do**:
    - cài tool nội bộ/dự án: L1 (ghi log)
    - nhãn chưa chắc (không phải đã-đọc-entry-gốc) -> nâng lên L2 (không chắc thì coi là mức cao hơn)
  - **ghi_chu**: Không chắc mức nào thì coi là mức cao hơn. Mọi hành động đăng bài/gửi tin/chi tiền sau khi cài vẫn đi qua lằn ranh đỏ.
- **kiem_tra**:
  - **tieu_chi**: PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).
  - **vi_du_trong_entry**: **Trước (script cho video ABTRIP về Fast Track):** > "Fast Track không chỉ là một dịch vụ, mà còn là biểu tượng cho sự tận tâm của ABTRIP trong việc mang đến trải nghiệm sân bay liền mạch và đẳng cấp cho hành khách, phản ánh cam kết không ngừng nghỉ về chất lượng dịch vụ." **Sau khi áp skill:** > "Fast Track của ABTRIP đưa mày qua an ninh trong 5 phút, không phải xếp hàng 40 phút như bình thường." Ngắn hơn, cụ thể hơn (5 phút vs 40 phút), không có từ "biểu tượng/đẳng cấp/liền mạch/cam kết" nào c
  - **lenh_goi_y**: []
- **go_cai_dat**:
  - xoá/khôi phục file đã chép (người tự làm, sao lưu trước)
- **canh_bao**:
  - Entry không có mục Setup/Cài đặt chứa khối lệnh; lệnh lấy từ mục Ví dụ - cần người đọc kỹ.
  - Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
- **lan_ranh_do**:
  - AI không tự chi tiền
  - AI không tự publish public content
  - AI không tự cam kết với khách

## `kho:agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline`

- **id**: agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline
- **ten**: Churn Risk & Escalation Discipline
- **loai_muc**: skill-agent
- **chua_chay_that**: True
- **thong_bao**: CHƯA CHẠY THẬT - đây chỉ là kế hoạch đọc từ entry. Không có lệnh nào được thực thi. Cần người duyệt trước khi cài.
- **nguon**: agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline/SKILL.md
- **doc_entry_goc**: True
- **buoc**:
  -
    - **loai**: chep-file
    - **lenh**: (sao chép) agents/customer-satisfaction-pro/skills/churn-risk-escalation-discipline -> thư mục skills của vessel (xem agents/*-GUIDE.md của vessel)
    - **kieu**: mo-ta
    - **nguon_muc**: suy ra từ loại muc
    - **co_do**: []
    - **canh_bao_vang**: []
    - **can_nguoi_doc_ky**: False
    - **chua_chay**: True
    - **mo_ta**: Skill là file Markdown: chép thư mục skill vào nơi vessel đọc skill. Chưa kiểm cách vessel nạp.
    - **so**: 1
- **dieu_kien_tien_quyet**:
  - **can**: []
  - **thieu**: []
  - **co**: {}
  - **can_khac**: []
- **bien_moi_truong**: []
- **co_rui_ro**:
  -
    - **loai**: license
    - **noi_dung**: License chưa ghi trong kho - kiểm trước khi dùng cho khách.
- **co_do**: []
- **muc_duyet**:
  - **muc**: L1
  - **ly_do**:
    - cài tool nội bộ/dự án: L1 (ghi log)
  - **ghi_chu**: Không chắc mức nào thì coi là mức cao hơn. Mọi hành động đăng bài/gửi tin/chi tiền sau khi cài vẫn đi qua lằn ranh đỏ.
- **kiem_tra**:
  - **tieu_chi**: PASS nếu lệnh kiểm chạy xong không lỗi VÀ đầu ra khớp ví dụ trong entry; FAIL nếu lỗi, thiếu công cụ, hoặc kết quả khác ví dụ (ghi lý do, bỏ mục đó).
  - **vi_du_trong_entry**: Khách Wonder Mart nhắn "đặt hàng 3 ngày chưa thấy, định huỷ luôn không mua nữa" — dù đây là LẦN ĐẦU khách phàn nàn, câu "định huỷ" là tín hiệu rời bỏ thật → escalate ngay, không đợi xem có phàn nàn lần 2 không. Ngược lại, khách hỏi "shop có ship COD không" 3 lần liên tiếp (không phải dấu hiệu rời bỏ) → áp luật thường, escalate ở lần thứ 3 để xem lại vì sao câu trả lời cũ không rõ.
  - **lenh_goi_y**: []
- **go_cai_dat**:
  - xoá/khôi phục file đã chép (người tự làm, sao lưu trước)
- **canh_bao**:
  - Entry không có mục Setup/Cài đặt chứa khối lệnh; lệnh lấy từ mục Ví dụ - cần người đọc kỹ.
  - Nhãn trong kho do model/agent gắn, không phải kết luận; chưa mục nào có bằng chứng dùng thật trong dự án của Tano Agency (xem catalog/USAGE-LOG.md).
- **lan_ranh_do**:
  - AI không tự chi tiền
  - AI không tự publish public content
  - AI không tự cam kết với khách

