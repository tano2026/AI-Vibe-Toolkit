# -*- coding: utf-8 -*-
"""Test cho tools/agent_factory.py. Không mạng, không credential, dùng thu_kho GIẢ.

Chạy: python -m unittest discover -s tools/tests -p "test_agent_factory.py" -v
(từ gốc repo; PYTHONIOENCODING=utf-8 trên Windows)
"""
import contextlib
import hashlib
import io
import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
REPO = TOOLS.parent
sys.path.insert(0, str(TOOLS))
import agent_factory as af  # noqa: E402

CATALOG = json.loads((REPO / "catalog" / "catalog.json").read_text(encoding="utf-8"))["items"]


class ThuKhoGia:
    """Thủ kho giả đúng chữ ký hợp đồng; lấy mục thật từ catalog.json để id tồn tại."""

    def __init__(self, recommend_loi=False):
        self.recommend_loi = recommend_loi
        self.goi = []

    def _tim(self, cap, top=2):
        if cap.startswith("khong-co"):
            return []
        rs = [i for i in CATALOG if cap in (i.get("capability") or "").split(",") and i.get("adoption") != "chi-tham-khao"]
        return rs[:top]

    def load_catalog(self, repo_root=None):
        return CATALOG

    def search(self, query, *, vessel=None, exclude_needs=(), include_unlabeled=False,
               adoption_not=("chi-tham-khao",), capability=None, top=5, repo_root=None):
        self.goi.append(("search", query))
        return [dict(i, score=1.0) for i in self._tim(capability or query, top)]

    def card(self, id):
        return {"id": id}

    def install_plan(self, id, *, machine=None):
        self.goi.append(("install_plan", id))
        return {"id": id, "buoc": ["đọc entry gốc", "KHÔ: không thực thi"], "may": bool(machine)}

    def machine_profile(self):
        return {"os": "gia", "python": "x"}

    def gap_line(self, query, du_an="", ghi_chu=""):
        return f"| 2026-10-17 | {query} | {du_an} | {ghi_chu} |"

    def usage_line(self, *a, **k):
        return ""

    def recommend(self, brief, *, vessel=None, exclude_needs=(), per_need=1):
        self.goi.append(("recommend", brief))
        if self.recommend_loi:
            raise RuntimeError("recommend hỏng")
        rs = self._tim(brief)
        if not rs:
            return {"kha_nang": [], "hong": [{"capability": brief, "mo_ta": "không có ứng viên"}], "canh_bao": ["chung"]}
        return {"kha_nang": [{"capability": brief, "chinh": [rs[0]], "du_phong": rs[1] if len(rs) > 1 else None}],
                "hong": [], "canh_bao": [f"{rs[0]['id']}: mới đọc phần đầu entry", "cảnh báo chung"]}


def chay(argv, tk=None):
    buf, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(err):
        rc = af.main(argv, tk=tk)
    return rc, buf.getvalue(), err.getvalue()


class Co(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp(prefix="af-test-"))
        self.addCleanup(shutil.rmtree, self.tmp, True)
        self.tk = ThuKhoGia()

    def moi_agent(self, slug="fb-agent", extra=()):
        rc, out, err = chay(["moi-agent", "--slug", slug, "--job", "đăng bài và trả lời bình luận → bài nháp → CEO duyệt",
                             "--kha-nang", "social-media,content-writing", "--tu-chu", "L1", "--vessel", "hermes",
                             "--kenh", "facebook", "--dau-ra", str(self.tmp), *extra], tk=self.tk)
        return rc, out, err, self.tmp / slug

    def moi_opc(self, slug="demo-opc", extra=()):
        rc, out, err = chay(["moi-opc", "--slug", slug, "--thuong-hieu", "Thương Hiệu Thử", "--doanh-thu", "affiliate,dich-vu",
                             "--kenh", "facebook,zalo,instagram", "--goi-mo-rong", "tai-chinh,doi-tac",
                             "--dau-ra", str(self.tmp), *extra], tk=self.tk)
        return rc, out, err, self.tmp / slug

    def kiem(self, d):
        return {k.ten: k for k in af.kiem(d)}


class TestDungAgent(Co):
    def test_dung_va_kiem_pass(self):
        rc, out, err, d = self.moi_agent()
        self.assertEqual(rc, 0, out + err)
        ket = af.kiem(d)
        fails = [str(k) for k in ket if k.trang_thai == "FAIL"]
        self.assertEqual(fails, [])
        cm = json.loads((d / "capability-map.json").read_text(encoding="utf-8"))
        self.assertEqual([e["capability"] for e in cm["kha_nang"]], ["social-media", "content-writing"])
        self.assertTrue(all(e["chinh"] for e in cm["kha_nang"]))
        # thủ kho giả được gọi đúng hợp đồng
        self.assertIn(("recommend", "social-media"), self.tk.goi)
        self.assertTrue(any(g[0] == "install_plan" for g in self.tk.goi))
        plan = (d / "INSTALL-PLAN.md").read_text(encoding="utf-8")
        self.assertIn("KHÔ", plan)
        self.assertIn("không thực thi", plan.lower())

    def test_tenant_config_va_che_do_nhap(self):
        _, _, _, d = self.moi_agent()
        tj = json.loads((d / "tenant-config.json").read_text(encoding="utf-8"))
        self.assertIsNone(tj["compliance_overrides"])
        self.assertEqual(tj["agent"]["launch_mode"]["mode"], "draft_only")
        self.assertFalse(tj["agent"]["kill_switch"]["implemented"])
        self.assertTrue(tj["roles_enabled"]["marketing"])

    def test_khong_thu_kho_de_todo(self):
        rc, out, err, d = self.moi_agent("khong-tk", ["--khong-thu-kho"])
        self.assertEqual(rc, 0, out + err)
        ket = self.kiem(d)
        self.assertEqual(ket["nguồn-thủ-kho"].trang_thai, "WARN")
        self.assertIn("TODO", (d / "INSTALL-PLAN.md").read_text(encoding="utf-8"))
        cm = json.loads((d / "capability-map.json").read_text(encoding="utf-8"))
        self.assertTrue(all(e["hong"] for e in cm["kha_nang"]))

    def test_thieu_thu_kho_khong_co_co_khong_thu_kho(self):
        old = af.nap_thu_kho
        af.nap_thu_kho = lambda: None
        try:
            rc, out, err = chay(["moi-agent", "--slug", "x1", "--job", "a → b → c", "--kha-nang", "social-media",
                                 "--dau-ra", str(self.tmp)])
        finally:
            af.nap_thu_kho = old
        self.assertEqual(rc, 3)
        self.assertIn("--khong-thu-kho", err)

    def test_hong_khi_khong_co_ung_vien(self):
        rc, out, err = chay(["moi-agent", "--slug", "hong-1", "--job", "a → b → c", "--kha-nang", "khong-co-gi,social-media",
                             "--dau-ra", str(self.tmp)], tk=self.tk)
        self.assertEqual(rc, 0, out + err)
        cm = json.loads((self.tmp / "hong-1" / "capability-map.json").read_text(encoding="utf-8"))
        e = {x["capability"]: x for x in cm["kha_nang"]}
        self.assertTrue(e["khong-co-gi"]["hong"])
        self.assertIn("khong-co-gi", e["khong-co-gi"]["gap_line"])
        self.assertFalse(e["social-media"]["hong"])
        self.assertEqual(self.kiem(self.tmp / "hong-1")["hổng"].trang_thai, "WARN")

    def test_recommend_loi_thi_dung_search(self):
        tk = ThuKhoGia(recommend_loi=True)
        rc, out, err = chay(["moi-agent", "--slug", "fb-2", "--job", "a → b → c", "--kha-nang", "social-media",
                             "--dau-ra", str(self.tmp)], tk=tk)
        self.assertEqual(rc, 0, out + err)
        cm = json.loads((self.tmp / "fb-2" / "capability-map.json").read_text(encoding="utf-8"))
        self.assertEqual(cm["kha_nang"][0]["nguon"], "thu_kho.search")
        self.assertIsNotNone(cm["kha_nang"][0]["chinh"])

    def test_banner_va_kpi_rieng(self):
        rc, out, err, d = self.moi_agent("co-banner", ["--banner", "DEMO thử", "--kpi", "Số bài nháp=|đếm nháp|hàng đợi",
                                                       "--khong-lam", "không inbox;không boost"])
        self.assertEqual(rc, 0, out + err)
        self.assertIn("> **DEMO thử**", (d / "README.md").read_text(encoding="utf-8"))
        self.assertIn("> **DEMO thử**", (d / "HANDOVER.md").read_text(encoding="utf-8"))
        jd = (d / "JD-KPI-SOP-ESCALATION.md").read_text(encoding="utf-8")
        self.assertIn("| Số bài nháp |", jd)
        self.assertNotIn("Thời gian từ brief đến nháp", jd)  # có KPI riêng thì bỏ KPI mặc định
        self.assertIn("Số vi phạm ba lằn ranh đỏ", jd)       # KPI bắt buộc luôn có
        self.assertIn("- không boost", jd)

    def test_tham_so_sai(self):
        for argv in (["--slug", "Sai Slug"], ["--vessel", "khong-co"], ["--tu-chu", "L9"]):
            base = ["moi-agent", "--slug", "ok-1", "--job", "a → b → c", "--kha-nang", "social-media", "--dau-ra", str(self.tmp)]
            rc, _, err = chay(base + argv, tk=self.tk)
            self.assertEqual(rc, 3, argv)
            self.assertIn("LỖI", err)


class TestKiemFail(Co):
    def setUp(self):
        super().setUp()
        _, _, _, self.d = self.moi_agent()

    def sua(self, rel, ham):
        p = self.d / rel
        p.write_text(ham(p.read_text(encoding="utf-8")), encoding="utf-8")

    def test_fail_xoa_escalation(self):
        import re
        self.sua("JD-KPI-SOP-ESCALATION.md", lambda t: re.sub(r"(?s)## 4\. Escalation.*?(?=## 5\.)", "", t))
        self.assertEqual(self.kiem(self.d)["jd-kpi-sop-escalation"].trang_thai, "FAIL")

    def test_fail_thieu_lan_ranh_do(self):
        self.sua("system-prompt.md", lambda t: t.replace("AI không tự chi tiền", "AI cân nhắc chi tiền"))
        k = self.kiem(self.d)["ba-lằn-ranh-đỏ"]
        self.assertEqual(k.trang_thai, "FAIL")
        self.assertIn("chi tiền", k.chi_tiet)

    def test_fail_id_kho_khong_ton_tai(self):
        self.sua("README.md", lambda t: t + "\nDùng `kho:mcps/khong-bao-gio-ton-tai-xyz` cho việc này.\n")
        k = self.kiem(self.d)["mục-kho"]
        self.assertEqual(k.trang_thai, "FAIL")
        self.assertIn("khong-bao-gio-ton-tai-xyz", k.chi_tiet)

    def test_fail_id_tran_khong_ton_tai(self):
        self.sua("README.md", lambda t: t + "\nXem repos/khong-co-that-xyz để biết thêm.\n")
        self.assertEqual(self.kiem(self.d)["mục-kho"].trang_thai, "FAIL")

    def test_fail_khoa_bi_mat_gia(self):
        gia = "sk-" + "A1b2C3d4" * 4  # dựng động, không phải khoá thật
        self.sua("HANDOVER.md", lambda t: t + f"\nGhi nhầm: {gia}\n")
        self.assertEqual(self.kiem(self.d)["khóa-bí-mật"].trang_thai, "FAIL")

    def test_fail_khoa_dang_gan_gia_tri(self):
        gia = "tok" + "X9y8Z7" * 5
        self.sua("README.md", lambda t: t + f"\nAPI_KEY={gia}\n")
        self.assertEqual(self.kiem(self.d)["khóa-bí-mật"].trang_thai, "FAIL")

    def test_pass_ten_bien_khong_phai_khoa(self):
        self.sua("README.md", lambda t: t + "\nBiến cần có: TELEGRAM_BOT_TOKEN=ZALO_ACCESS_TOKEN_NAME_ONLY_TEXT\n")
        self.assertEqual(self.kiem(self.d)["khóa-bí-mật"].trang_thai, "PASS")

    def test_fail_cho_trong_chua_dien(self):
        self.sua("README.md", lambda t: t + "\nGiá trị: {{chua_dien_gi_ca}}\n")
        self.assertEqual(self.kiem(self.d)["chỗ-trống"].trang_thai, "FAIL")

    def test_pass_cho_trong_co_danh_dau(self):
        self.sua("README.md", lambda t: t + "\nGiá trị: {{x}} CHƯA CÓ — hỏi CEO\n")
        self.assertEqual(self.kiem(self.d)["chỗ-trống"].trang_thai, "PASS")

    def test_fail_hardcode_mau(self):
        self.sua("system-prompt.md", lambda t: t + "\nDùng màu #1A2B3C cho mọi bài.\n")
        self.assertEqual(self.kiem(self.d)["không-hardcode-brand-màu"].trang_thai, "FAIL")

    def test_fail_hardcode_ten_thuong_hieu(self):
        self.sua("skills/social-media/SKILL.md", lambda t: t + "\nViết như Trùm Sân Bay.\n")
        self.assertEqual(self.kiem(self.d)["không-hardcode-brand-màu"].trang_thai, "FAIL")

    def test_pass_mau_trong_readme_duoc_phep(self):
        self.sua("README.md", lambda t: t + "\nMàu #1A2B3C chỉ để minh hoạ.\n")
        self.assertEqual(self.kiem(self.d)["không-hardcode-brand-màu"].trang_thai, "PASS")

    def test_fail_compliance_overrides_khac_null(self):
        p = self.d / "tenant-config.json"
        j = json.loads(p.read_text(encoding="utf-8"))
        j["compliance_overrides"] = {"ha_nguong": True}
        p.write_text(json.dumps(j, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(self.kiem(self.d)["tenant-config"].trang_thai, "FAIL")

    def test_fail_thieu_test_lan_ranh_do(self):
        p = self.d / "tests" / "test-cases.json"
        cs = json.loads(p.read_text(encoding="utf-8"))
        for c in cs:
            c["nhan"] = [n for n in c["nhan"] if n != "lan-ranh-do"]
        p.write_text(json.dumps(cs, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(self.kiem(self.d)["kế-hoạch-cài-và-test"].trang_thai, "FAIL")

    def test_fail_thieu_file(self):
        (self.d / "INSTALL-PLAN.md").unlink()
        self.assertEqual(self.kiem(self.d)["cấu-trúc"].trang_thai, "FAIL")

    def test_fail_thieu_nut_dung(self):
        self.sua("JD-KPI-SOP-ESCALATION.md", lambda t: t.replace("/stop", "dung"))
        self.assertEqual(self.kiem(self.d)["nút-dừng-khẩn"].trang_thai, "FAIL")

    def test_cli_kiem_exit_code(self):
        rc, out, _ = chay(["kiem", str(self.d)])
        self.assertEqual(rc, 0, out)
        (self.d / "INSTALL-PLAN.md").unlink()
        rc, out, _ = chay(["kiem", str(self.d)])
        self.assertEqual(rc, 1)
        self.assertIn("KẾT QUẢ: FAIL", out)


class TestOpc(Co):
    def test_dung_va_kiem_pass(self):
        rc, out, err, d = self.moi_opc()
        self.assertEqual(rc, 0, out + err)
        fails = [str(k) for k in af.kiem(d) if k.trang_thai == "FAIL"]
        self.assertEqual(fails, [])
        self.assertTrue((d / "domain-packs" / "demo-opc" / "PACK.md").exists())
        man = json.loads((d / "factory-manifest.json").read_text(encoding="utf-8"))
        for a in ("ceo", "marketing", "media", "sales", "support", "operations", "analytics"):
            self.assertIn(a, man["agents"])

    def test_airtable_schema_dung_orgv3(self):
        _, _, _, d = self.moi_opc()
        s = json.loads((d / "airtable-schema.json").read_text(encoding="utf-8"))
        self.assertEqual([t["name"] for t in s["tables"]],
                         ["agents", "jobs", "sops", "kpis", "approvals", "escalations", "activity_log"])
        ext = {t["name"] for t in s["extension_tables"]}
        self.assertEqual(ext, {"partners", "orders", "payouts", "refunds"})
        self.assertTrue(all(a["status"] == "paused" for a in s["seed"]["agents"]))
        jobs = [t for t in s["tables"] if t["name"] == "jobs"][0]
        self.assertIn("demo-opc", [f for f in jobs["fields"] if f["name"] == "pack"][0]["options"])

    def test_chi_bat_goi_duoc_chon(self):
        rc, out, err = chay(["moi-opc", "--slug", "chi-affiliate", "--thuong-hieu", "X Thử", "--doanh-thu", "affiliate",
                             "--kenh", "facebook", "--dau-ra", str(self.tmp)], tk=self.tk)
        self.assertEqual(rc, 0, out + err)
        d = self.tmp / "chi-affiliate"
        s = json.loads((d / "airtable-schema.json").read_text(encoding="utf-8"))
        self.assertEqual(s["extension_tables"], [])
        g = (d / "GATES.md").read_text(encoding="utf-8")
        self.assertIn("KHÔNG ÁP DỤNG", g)
        man = json.loads((d / "factory-manifest.json").read_text(encoding="utf-8"))
        self.assertNotIn("operations", man["agents"])

    def test_goi_chua_co_file_duoc_ghi_ro(self):
        _, _, _, d = self.moi_opc()
        r = (d / "OPC-ROSTER.md").read_text(encoding="utf-8")
        self.assertIn("CHƯA CÓ trong kho", r)
        self.assertIn("ĐỀ XUẤT", r)

    def test_fail_xoa_escalation_roster(self):
        _, _, _, d = self.moi_opc()
        p = d / "OPC-ROSTER.md"
        t = p.read_text(encoding="utf-8")
        import re
        p.write_text(re.sub(r"(?m)^- \*\*Escalation:\*\*.*$", "", t), encoding="utf-8")
        self.assertEqual(self.kiem(d)["jd-kpi-sop-escalation"].trang_thai, "FAIL")

    def test_fail_thieu_lan_ranh_do_gates(self):
        _, _, _, d = self.moi_opc()
        p = d / "GATES.md"
        p.write_text(p.read_text(encoding="utf-8").replace("AI không tự publish public content", "AI cân nhắc đăng"), encoding="utf-8")
        self.assertEqual(self.kiem(d)["ba-lằn-ranh-đỏ"].trang_thai, "FAIL")

    def test_fail_thieu_cong_g5(self):
        _, _, _, d = self.moi_opc()
        p = d / "GATES.md"
        p.write_text("\n".join(l for l in p.read_text(encoding="utf-8").splitlines() if not l.startswith("| G5 ")), encoding="utf-8")
        self.assertEqual(self.kiem(d)["cổng-duyệt"].trang_thai, "FAIL")

    def test_fail_schema_link_hong(self):
        _, _, _, d = self.moi_opc()
        p = d / "airtable-schema.json"
        s = json.loads(p.read_text(encoding="utf-8"))
        s["tables"][1]["fields"][2]["linked_table"] = "bang_khong_co"
        p.write_text(json.dumps(s, ensure_ascii=False), encoding="utf-8")
        self.assertEqual(self.kiem(d)["airtable-schema"].trang_thai, "FAIL")

    def test_fail_brand_trong_gates(self):
        _, _, _, d = self.moi_opc()
        p = d / "GATES.md"
        p.write_text(p.read_text(encoding="utf-8") + "\nChỉ dành cho Thương Hiệu Thử.\n", encoding="utf-8")
        self.assertEqual(self.kiem(d)["không-hardcode-brand-màu"].trang_thai, "FAIL")

    def test_tham_so_sai(self):
        rc, _, err = chay(["moi-opc", "--slug", "o1", "--thuong-hieu", "X", "--doanh-thu", "khong-co", "--dau-ra", str(self.tmp)], tk=self.tk)
        self.assertEqual(rc, 3)
        rc, _, err = chay(["moi-opc", "--slug", "o1", "--thuong-hieu", "X", "--doanh-thu", "affiliate", "--kenh", "mxh-la",
                           "--dau-ra", str(self.tmp)], tk=self.tk)
        self.assertEqual(rc, 3)


class TestGhiDeVaBanGiao(Co):
    def test_ghi_de_bi_tu_choi(self):
        rc, _, _, d = self.moi_agent()
        self.assertEqual(rc, 0)
        (d / "ghi-chu-nguoi-dung.txt").write_text("đừng mất", encoding="utf-8")
        rc, out, err, _ = self.moi_agent()
        self.assertEqual(rc, 3)
        self.assertIn("đã tồn tại", err)
        self.assertTrue((d / "ghi-chu-nguoi-dung.txt").exists())
        rc, out, err, _ = self.moi_opc("opc-1")
        self.assertEqual(rc, 0)
        rc, out, err, _ = self.moi_opc("opc-1")
        self.assertEqual(rc, 3)

    def test_ghi_de_chi_voi_co_va_dung_thu_muc_factory(self):
        rc, _, _, d = self.moi_agent()
        rc, out, err, _ = self.moi_agent(extra=["--ghi-de"])
        self.assertEqual(rc, 0, out + err)
        la = self.tmp / "thu-muc-la"
        la.mkdir()
        (la / "quan-trong.txt").write_text("x", encoding="utf-8")
        rc, out, err, _ = self.moi_agent("thu-muc-la", ["--ghi-de"])
        self.assertEqual(rc, 3)
        self.assertTrue((la / "quan-trong.txt").exists())

    def test_mac_dinh_khong_ghi_vao_repo(self):
        dich = af.chuan_hoa_dich(None, "abc", False)
        self.assertNotIn(str(REPO), str(dich))

    def test_ban_giao_tao_checksum(self):
        _, _, _, d = self.moi_agent()
        out_dir = self.tmp / "bg"
        rc, out, err = chay(["ban-giao", str(d), "--dau-ra", str(out_dir)])
        self.assertEqual(rc, 0, out + err)
        pkg = out_dir / "fb-agent"
        cs = (pkg / "CHECKSUMS.sha256").read_text(encoding="utf-8").strip().splitlines()
        files = [p for p in pkg.rglob("*") if p.is_file() and p.name != "CHECKSUMS.sha256"]
        self.assertEqual(len(cs), len(files))
        for line in cs:
            h, rel = line.split("  ", 1)
            self.assertEqual(h, hashlib.sha256((pkg / rel).read_bytes()).hexdigest(), rel)
        ho = (pkg / "HANDOVER.md").read_text(encoding="utf-8")
        self.assertIn("Kết quả kiểm lúc bàn giao", ho)
        self.assertIn("KẾT QUẢ: PASS", ho)
        self.assertNotIn("(Phần này do `ban-giao` điền", ho)
        self.assertTrue((pkg / "KET-QUA-KIEM.txt").exists())
        # nguồn không bị đụng
        self.assertIn("(Phần này do `ban-giao` điền", (d / "HANDOVER.md").read_text(encoding="utf-8"))
        # ghi đè bị từ chối
        rc, _, err = chay(["ban-giao", str(d), "--dau-ra", str(out_dir)])
        self.assertEqual(rc, 3)

    def test_ban_giao_tu_choi_khi_kiem_fail(self):
        _, _, _, d = self.moi_agent()
        (d / "INSTALL-PLAN.md").unlink()
        rc, out, err = chay(["ban-giao", str(d), "--dau-ra", str(self.tmp / "bg2")])
        self.assertEqual(rc, 3)
        self.assertFalse((self.tmp / "bg2" / "fb-agent").exists())

    def test_ban_giao_opc(self):
        _, _, _, d = self.moi_opc()
        rc, out, err = chay(["ban-giao", str(d), "--dau-ra", str(self.tmp / "bg3")])
        self.assertEqual(rc, 0, out + err)
        self.assertTrue((self.tmp / "bg3" / "demo-opc" / "CHECKSUMS.sha256").exists())


class TestHongKhongVot(Co):
    def test_recommend_noi_hong_thi_khong_goi_search(self):
        rc, out, err = chay(["moi-agent", "--slug", "hong-2", "--job", "a → b → c", "--kha-nang", "khong-co-gi",
                             "--dau-ra", str(self.tmp)], tk=self.tk)
        self.assertEqual(rc, 0, out + err)
        self.assertNotIn(("search", "khong-co-gi"), self.tk.goi)
        cm = json.loads((self.tmp / "hong-2" / "capability-map.json").read_text(encoding="utf-8"))
        self.assertTrue(cm["kha_nang"][0]["hong"])
        self.assertEqual(cm["kha_nang"][0]["nguon"], "thu_kho.recommend")

    def test_canh_bao_thieu_tay(self):
        # thủ kho giả cho 'content-writing' mục Não; kiểm cảnh báo chưa có công cụ tác động ra ngoài khi không có Tay
        kq = [{"capability": "x", "hong": False, "canh_bao": [], "nguon": "t", "gap_line": "",
               "chinh": {"id": "skills/abc", "ten": "", "ly_do": "", "dieu_kien_can": "", "bo_qua_neu": "", "evidence": "",
                         "adoption": "", "confidence": "", "curation_status": "", "duong_dan": "", "capability": ""},
               "du_phong": None}]
        self.assertIn("chưa có mục loại Tay", af.md_nao_tay_co(kq, "hermes"))


def _co_thu_kho_that():
    try:
        return af.nap_thu_kho()
    except Exception:
        return None


@unittest.skipIf(_co_thu_kho_that() is None, "chưa có tools/thu_kho.py")
class TestThuKhoThat(Co):
    """Chạy với tools/thu_kho.py thật (đọc catalog/catalog.json thật, không mạng)."""

    def test_agent_voi_thu_kho_that(self):
        rc, out, err = chay(["moi-agent", "--slug", "that-1", "--job", "đăng bài → nháp → CEO", "--kha-nang",
                             "social-media,content-writing", "--dau-ra", str(self.tmp)])
        self.assertEqual(rc, 0, out + err)
        d = self.tmp / "that-1"
        cm = json.loads((d / "capability-map.json").read_text(encoding="utf-8"))
        ids = {i["id"] for i in CATALOG}
        for e in cm["kha_nang"]:
            self.assertEqual(e["nguon"], "thu_kho.recommend")
            self.assertIn(e["chinh"]["id"], ids)
        plan = (d / "INSTALL-PLAN.md").read_text(encoding="utf-8")
        self.assertIn("CHƯA CHẠY THẬT", plan)
        self.assertNotIn("Nguyen Ngoc", plan)
        self.assertNotIn("bien_khoa", plan)

    def test_opc_voi_thu_kho_that(self):
        rc, out, err = chay(["moi-opc", "--slug", "that-opc", "--thuong-hieu", "Thương Hiệu Mẫu", "--doanh-thu", "affiliate",
                             "--kenh", "facebook", "--dau-ra", str(self.tmp)])
        self.assertEqual(rc, 0, out + err)


class TestTaiLieu(unittest.TestCase):
    def test_liet_ke_chay_duoc(self):
        rc, out, _ = chay(["liet-ke"])
        self.assertEqual(rc, 0)
        self.assertIn("system-prompt.md", out)
        self.assertIn("airtable-schema.json", out)

    def test_duong_dan_package_orgv3_ton_tai(self):
        thieu = []
        for a, d in af.ORG9.items():
            for p in d["pkg"]:
                if not (REPO / p).exists():
                    thieu.append(f"{a}: {p}")
        for g, d in af.GOI_MO_RONG.items():
            if d["ton_tai"] and not (REPO / d["file"]).exists():
                thieu.append(f"{g}: {d['file']}")
        self.assertEqual(thieu, [])

    def test_vessel_doc_ton_tai(self):
        for k, v in af.VESSELS.items():
            for p in [x.strip() for x in v["doc"].split("->") if x.strip().startswith("agents/")]:
                self.assertTrue((REPO / p.split(" ")[0]).exists(), f"{k}: {p}")

    def test_mau_khong_chua_khoa_va_brand(self):
        for p in (af.TEMPLATES).rglob("*"):
            if p.is_file():
                t = p.read_text(encoding="utf-8")
                for ten, rg in af.REGEX_BI_MAT:
                    self.assertIsNone(rg.search(t), f"{p}: {ten}")


if __name__ == "__main__":
    unittest.main()
