# -*- coding: utf-8 -*-
"""Test cho tools/company_engine.py. Không mạng, không credential.

Chạy: python -m unittest discover -s tools/tests -p "test_company_engine.py" -v
"""
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import company_engine as ce  # noqa: E402

BRIEF = {"context": "c", "yeu_cau": "làm X", "input": "i", "deadline": "T5", "done_khi": "xong"}


class Dong_ho:
    def __init__(self):
        self.t = 1000.0

    def __call__(self):
        return self.t


class CompanyTest(unittest.TestCase):
    def setUp(self):
        self.clock = Dong_ho()
        self.path = Path(tempfile.mkdtemp()) / "hq.json"
        self.da_gui = []
        self.c = ce.Company(self.path, actuator=self.da_gui.append, clock=self.clock)

    def test_ea_gate_hoi_dung_mot_cau(self):
        self.assertIn("PACK", self.c.submit("", "research", BRIEF)[1])
        self.assertIn("không có trong", self.c.submit("p", "ceo", BRIEF)[1])
        thieu = dict(BRIEF, deadline="")
        self.assertIn("deadline", self.c.submit("p", "research", thieu)[1])

    def test_dau_ra_chay_ngang_giua_cac_role(self):
        a, _ = self.c.submit("p", "research", dict(BRIEF, yeu_cau="quét thị trường"))
        b, _ = self.c.submit("p", "marketing", dict(BRIEF, yeu_cau="viết plan"), depends_on=[a])
        self.c.tick()
        self.assertEqual(self.c.job(b)["status"], "done")
        self.assertIn(f"job{a}:research", self.c.job(b)["output"])  # marketing nhận đầu ra của research

    def test_phu_thuoc_chua_xong_thi_khong_chay(self):
        a, _ = self.c.submit("p", "research", BRIEF, risk_type="spend_money")  # dừng ở approval
        b, _ = self.c.submit("p", "marketing", BRIEF, depends_on=[a])
        self.c.tick()
        self.assertEqual(self.c.job(a)["status"], "awaiting_approval")
        self.assertEqual(self.c.job(b)["status"], "queued")

    def test_uu_tien_p0_truoc(self):
        thu_tu = []
        c = ce.Company(self.path.with_name("o.json"), clock=self.clock,
                       executor=lambda role, job, ctx: thu_tu.append(job["priority"]) or "ok")
        c.submit("p", "research", BRIEF, priority="P2")
        c.submit("p", "dev", BRIEF, priority="P0")
        c.tick()
        self.assertEqual(thu_tu, ["P0", "P2"])

    def test_l2_khong_thuc_thi_khi_chua_duyet(self):
        j, _ = self.c.submit("p", "media", BRIEF, risk_type="publish")
        self.c.tick()
        self.assertEqual(self.c.job(j)["status"], "awaiting_approval")
        self.assertEqual(self.da_gui, [])  # chưa approved = actuator không được gọi
        self.assertTrue(self.c.approve(j))
        self.assertEqual(self.c.job(j)["status"], "done")
        self.assertEqual(len(self.da_gui), 1)

    def test_tu_choi_dua_ve_sua(self):
        j, _ = self.c.submit("p", "media", BRIEF, risk_type="publish")
        self.c.tick()
        self.c.reject(j, "caption sai")
        self.assertEqual(self.c.job(j)["status"], "queued")
        self.assertIn("caption sai", self.c.job(j)["review_note"])
        self.assertEqual(self.da_gui, [])

    def test_approval_het_han_24h_thi_khong_lam_va_nhac_mot_lan(self):
        j, _ = self.c.submit("p", "media", BRIEF, risk_type="publish")
        self.c.tick()
        self.clock.t += ce.DAY + 1
        self.assertEqual(self.c.expire_approvals(), [j])
        self.assertEqual(self.c.expire_approvals(), [])
        self.assertFalse(self.c.approve(j))  # đã expired, duyệt muộn không có hiệu lực
        self.assertEqual(self.da_gui, [])

    def test_l3_phai_xin_phep_truoc_khi_lam(self):
        j, _ = self.c.submit("p", "sales", BRIEF, risk_type="commit_customer")
        self.c.tick()
        self.assertIsNone(self.c.job(j)["output"])  # chưa được phép thì chưa làm
        self.c.approve(j)
        self.assertEqual(self.c.job(j)["status"], "queued")
        self.c.tick()
        self.assertEqual(self.c.job(j)["status"], "done")

    def test_muc_rui_ro(self):
        self.assertEqual(ce.risk_level(None), "L0")
        self.assertEqual(ce.risk_level("publish"), "L2")
        self.assertEqual(ce.risk_level("loai_la"), "L3")  # không chắc -> mức cao hơn
        self.assertEqual(ce.risk_level("internal", scraped=True), "L2")  # scrape nâng 1 mức
        self.assertEqual(ce.risk_level(None, scraped=True), "L0")
        self.assertEqual(ce.risk_level("commit_customer", scraped=True), "L3")

    def test_review_khong_dat_sua_mot_vong_roi_leo_thang(self):
        c = ce.Company(self.path.with_name("r.json"), clock=self.clock,
                       reviewer=lambda rv, job, out: (False, "thiếu nguồn"))
        j, _ = c.submit("p", "marketing", BRIEF)
        c.tick()
        self.assertEqual(c.job(j)["status"], "blocked")
        self.assertEqual(c.job(j)["rounds"], 1)
        self.assertIn("thiếu nguồn", c.db["escalations"][0]["reason"])

    def test_loi_executor_ba_lan_thi_leo_thang(self):
        def hong(role, job, ctx):
            raise RuntimeError("API sập")
        c = ce.Company(self.path.with_name("e.json"), clock=self.clock, executor=hong)
        j, _ = c.submit("p", "dev", BRIEF)
        c.tick()
        self.assertEqual(c.job(j)["fails"], ce.MAX_FAILS)
        self.assertEqual(c.job(j)["status"], "blocked")

    def test_ket_qua_24h_thi_leo_thang(self):
        j, _ = self.c.submit("p", "dev", BRIEF)
        self.c.job(j)["status"] = "doing"
        self.clock.t += ce.DAY + 1
        self.c.tick()
        self.assertEqual(self.c.job(j)["status"], "blocked")

    def test_luu_va_nap_lai_trang_thai(self):
        j, _ = self.c.submit("p", "research", BRIEF)
        self.c.tick()
        c2 = ce.Company(self.path, clock=self.clock)
        self.assertEqual(c2.job(j)["status"], "done")

    def test_playbook_chay_het_voi_mot_lan_duyet(self):
        ids, hoi = ce.run_playbook(self.c, "trum-san-bay", "chien-dich-noi-dung", "tour Nhật")
        self.assertIsNone(hoi)
        self.c.tick()
        self.assertEqual(self.c.cockpit()["cho_duyet"], [ids[3]])  # chỉ bước "đăng" cần CEO
        self.assertEqual(self.c.job(ids[4])["status"], "queued")   # analytics đợi bước đăng
        self.c.approve(ids[3])
        self.c.tick()
        self.assertTrue(all(self.c.job(i)["status"] == "done" for i in ids))
        self.assertEqual(len(self.da_gui), 1)


if __name__ == "__main__":
    unittest.main()
