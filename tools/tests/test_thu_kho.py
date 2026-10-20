"""Test cho tools/thu_kho.py. Chay: python -m unittest discover -s tools/tests -v
Khong can mang. Phan tra kho dung catalog that cua repo; phan ke hoach cai dung kho gia trong thu muc tam."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import thu_kho as tk  # noqa: E402


def _kho_gia(entries):
    """Tao repo gia: entries = {id: (meta, noi_dung_md)} -> duong dan thu muc."""
    d = Path(tempfile.mkdtemp(prefix="thukho_test_"))
    (d / "catalog").mkdir()
    items = []
    for id_, (meta, md) in entries.items():
        rel = id_ + ".md"
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(md, encoding="utf-8")
        base = {"id": id_, "loai": "repo", "ten": id_, "tom_tat": "", "capability": "scraping", "use_when": "",
                "skip_if": "", "adoption": "cai-ngay-duoc", "needs": "none", "vessel_fit": "claude-code,hermes",
                "dup_group": "", "confidence": "cao", "evidence": "", "curation_status": "da-doc-entry-goc",
                "duong_dan": rel, "rui_ro": "", "license": "MIT", "diem": ""}
        base.update(meta)
        items.append(base)
    (d / "catalog" / "catalog.json").write_text(json.dumps({"count": len(items), "items": items}), encoding="utf-8")
    return d


class TraKho(unittest.TestCase):
    def test_cao_web_co_scraping_trong_top5(self):
        res = tk.search("cào web", top=5)
        self.assertTrue(res)
        self.assertTrue(any("scraping" in r["capability"].split(",") for r in res), [r["id"] for r in res])

    def test_cac_truong_bat_buoc(self):
        r = tk.search("cào web", top=1)[0]
        for k in ("id", "ten", "score", "ly_do_khop", "capability", "adoption", "needs", "vessel_fit",
                  "curation_status", "confidence", "use_when", "skip_if", "evidence", "audit_usable", "duong_dan"):
            self.assertIn(k, r)
        json.dumps(r)

    def test_bo_can_gpu_loai_het(self):
        co_gpu = [r for r in tk.search("chạy model local llm", top=200) if "gpu" in r["needs"].split(",")]
        self.assertTrue(co_gpu, "Tiền đề test: truy vấn này phải có mục cần gpu khi không lọc")
        res = tk.search("chạy model local llm", exclude_needs=("gpu",), top=200)
        self.assertTrue(res)
        self.assertFalse([r["id"] for r in res if "gpu" in r["needs"].split(",")])

    def test_bo_can_gpu_qua_cli(self):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = tk._main(["tim", "chạy model local llm", "--bo-can", "gpu", "--top", "50", "--json"])
        self.assertEqual(rc, 0)
        out = json.loads(buf.getvalue())["ket_qua"]
        self.assertTrue(out)
        self.assertFalse([r["id"] for r in out if "gpu" in r["needs"].split(",")])

    def test_khong_gpu_trong_cau_hoi_tu_bo_gpu(self):
        res = tk.search("làm video ngắn không GPU", top=100)
        self.assertFalse([r["id"] for r in res if "gpu" in r["needs"].split(",")])

    def test_vessel_hermes_loc_dung_va_giu_muc_rong(self):
        res = tk.search("dashboard", vessel="hermes", top=300)
        self.assertTrue(res)
        for r in res:
            vf = [x for x in r["vessel_fit"].split(",") if x]
            self.assertTrue(not vf or "hermes" in vf, r["id"])
        rong = [r for r in res if not r["vessel_fit"]]
        self.assertTrue(rong, "Mục vessel_fit rỗng phải vẫn hiện")
        self.assertTrue(all(any("chưa rõ" in g for g in r["ghi_chu"]) for r in rong))
        # muc chi cho claude-code phai bi loai khi loc hermes
        ngoai = [r for r in tk.search("dashboard", vessel="openclaw", top=300) if r["vessel_fit"] == "hermes"]
        self.assertFalse(ngoai)

    def test_co_dau_va_khong_dau_cung_ket_qua(self):
        for q in ("cào web đối thủ", "giọng đọc tiếng Việt", "đăng bài Facebook có lịch", "CRM quản lý khách hàng"):
            a = [r["id"] for r in tk.search(q, top=5)]
            b = [r["id"] for r in tk.search(tk.bo_dau(q), top=5)]
            self.assertEqual(a, b, q)

    def test_muc_chua_gan_nhan_chi_hien_khi_yeu_cau(self):
        mac_dinh = tk.search("cold email outreach", top=50)
        self.assertFalse([r for r in mac_dinh if r["curation_status"] == "chua-gan-nhan"])
        them = tk.search("cold email outreach", include_unlabeled=True, top=50)
        # Kho đã gắn nhãn hết (919/919): include_unlabeled không được làm xuất hiện thêm mục nào bị bỏ sót.
        self.assertLessEqual(len(mac_dinh), len(them))

    def test_xep_hang_goc_truoc_dau_entry_khi_ngang_bac(self):
        d = _kho_gia({
            "repos/a": ({"curation_status": "da-doc-dau-entry", "ten": "alpha scraper"}, "# a"),
            "repos/b": ({"curation_status": "da-doc-entry-goc", "ten": "beta scraper"}, "# b"),
        })
        res = tk.search("cào web", repo_root=d, top=2)
        self.assertEqual([r["id"] for r in res], ["repos/b", "repos/a"])

    def _caps_cua(self, q):
        return [c["capability"] for c in tk.phan_tich_truy_van(q)["capabilities"]]

    def test_nhan_ra_nhu_cau_tra_loi_binh_luan_cskh_zalo_affiliate(self):
        for q in ("trả lời bình luận", "tra loi binh luan", "CSKH", "chăm sóc khách", "cham soc khach"):
            self.assertIn("customer-support", self._caps_cua(q), q)
        for q in ("Zalo", "zalo"):
            self.assertIn("customer-support", self._caps_cua(q), q)
            self.assertIn("social-media", self._caps_cua(q), q)
        for q in ("affiliate", "làm affiliate", "tiếp thị liên kết", "tiep thi lien ket"):
            self.assertIn("ads", self._caps_cua(q), q)
        # truy van that ra ket qua, co dau va khong dau giong nhau
        for a, b in (("trả lời bình luận", "tra loi binh luan"), ("chăm sóc khách", "cham soc khach"),
                     ("tiếp thị liên kết", "tiep thi lien ket")):
            ra = [r["id"] for r in tk.search(a, top=5)]
            self.assertTrue(ra, a)
            self.assertEqual(ra, [r["id"] for r in tk.search(b, top=5)], a)
        self.assertIn("agents/trum-san-bay/skills/affiliate-injector",
                      [r["id"] for r in tk.search("affiliate", top=3)])

    def test_xep_hang_confidence_cao_truoc_khi_khop_capability_ngang(self):
        d = _kho_gia({
            "repos/a": ({"curation_status": "da-doc-entry-goc", "confidence": "vua", "ten": "alpha scraper"}, "# a"),
            "repos/b": ({"curation_status": "da-doc-dau-entry", "confidence": "cao", "ten": "beta scraper"}, "# b"),
        })
        res = tk.search("cào web", repo_root=d, top=2)
        self.assertEqual([r["id"] for r in res], ["repos/b", "repos/a"])

    def test_xep_hang_khop_capability_chinh_truoc_confidence(self):
        d = _kho_gia({
            "repos/a": ({"capability": "seo,scraping", "confidence": "cao", "ten": "alpha scraper"}, "# a"),
            "repos/b": ({"capability": "scraping", "confidence": "vua", "ten": "beta scraper"}, "# b"),
        })
        res = tk.search("cào web", repo_root=d, top=2)
        self.assertEqual(res[0]["id"], "repos/b")

    def test_dang_bai_facebook_page_meta_social_api_truoc_buffer_mcp(self):
        for q in ("đăng bài lên Facebook Page", "dang bai len Facebook Page"):
            ids = [r["id"] for r in tk.search(q, top=10)]
            self.assertIn("mcps/meta-social-api", ids, q)
            self.assertIn("mcps/buffer-mcp", ids, q)
            self.assertLess(ids.index("mcps/meta-social-api"), ids.index("mcps/buffer-mcp"), q)

    def test_audit_json_neu_co_thi_dung_neu_khong_thi_bo_qua(self):
        d = _kho_gia({
            "repos/a": ({"ten": "alpha scraper"}, "# a"),
            "repos/b": ({"ten": "beta scraper", "curation_status": "da-doc-dau-entry"}, "# b"),
        })
        self.assertIsNone(tk.load_catalog(d)["repos/a"]["audit"])
        (d / "catalog" / "audit.json").write_text(
            json.dumps({"repos/a": {"usable": False, "ly_do": "repo đã xoá"}}), encoding="utf-8")
        tk._CACHE.clear()
        cat = tk.load_catalog(d)
        self.assertEqual(cat["repos/a"]["audit"]["usable"], False)
        res = tk.search("cào web", repo_root=d, top=2)
        self.assertEqual([r["id"] for r in res], ["repos/b", "repos/a"])  # a bi day xuong du la 'goc'
        self.assertIs(res[1]["audit_usable"], False)
        self.assertTrue(any("audit" in g for g in res[1]["ghi_chu"]))

    def test_bang_dong_nghia_du_30_capability(self):
        caps = ("web-research scraping content-writing seo ads social-media email-outreach crm-sales customer-support "
                "video-generation video-render image-generation voice-tts design-ui front-end backend database devops "
                "agent-framework agent-orchestration-memory prompt-skill-library browser-automation document-office "
                "data-dashboard finance-accounting ticketing-aviation security-compliance local-llm productivity reference").split()
        self.assertEqual(len(caps), 30)
        self.assertEqual(set(caps), set(tk.CAPABILITY_SYNONYMS))
        pq = tk.phan_tich_truy_van("cào web, scrape, crawl")
        self.assertEqual([c["capability"] for c in pq["capabilities"]], ["scraping"])
        self.assertEqual([c["capability"] for c in tk.phan_tich_truy_van("giọng đọc tts")["capabilities"]], ["voice-tts"])
        self.assertIn("social-media", [c["capability"] for c in tk.phan_tich_truy_van("đăng bài facebook fanpage")["capabilities"]])


class TruyVanZalo(unittest.TestCase):
    """Truy van Zalo phai dua guide/playbook Zalo that (ten co 'zalo') len top 3, khong bi
    sentiment-classifier / chatwoot (chi trung capability customer-support) day xuong."""
    GUIDE = "agents/company/skills/zalo-channel-connection-guide"
    PLAYBOOK = "skills/zalo-oa-du-lich-luu-tru-playbook"

    def _top3(self, q):
        return [r["id"] for r in tk.search(q, top=3)]

    def test_zalo_co_dau_va_khong_dau_len_top3(self):
        for q in ("bot Zalo chăm sóc khách", "bot zalo cham soc khach", "tích hợp zalo OA",
                  "tich hop zalo oa", "zalo oa"):
            top = self._top3(q)
            self.assertIn(self.GUIDE, top, (q, top))
            self.assertIn(self.PLAYBOOK, top, (q, top))

    def test_ten_rieng_nen_tang_o_ten_thang_confidence_cao_hon(self):
        # muc co 'zalo' o ten (confidence vua) phai dung truoc muc chi trung capability chung (confidence cao)
        d = _kho_gia({
            "repos/chung": ({"ten": "generic helpdesk", "capability": "customer-support", "confidence": "cao",
                             "curation_status": "da-doc-entry-goc"}, "# helpdesk"),
            "repos/zalo-bot": ({"ten": "Zalo connector", "capability": "customer-support", "confidence": "vua",
                                "curation_status": "da-doc-entry-goc"}, "# zalo"),
        })
        tk._CACHE.clear()
        res = tk.search("bot zalo chăm sóc khách", repo_root=d, top=2)
        self.assertEqual([r["id"] for r in res][0], "repos/zalo-bot")

    def test_truy_van_khac_khong_bi_hong(self):
        top = self._top3("đăng bài lên Facebook Page")
        self.assertEqual(top[0], "mcps/meta-social-api")
        self.assertIn("skills/social-publisher", top)
        self.assertEqual(self._top3("trả lời bình luận khách")[0], "agents/trum-san-bay/skills/reply-agent-prompt")
        self.assertEqual(self._top3("làm affiliate du lịch")[0], "agents/trum-san-bay/skills/affiliate-injector")


class KeHoachCai(unittest.TestCase):
    ENTRY = (
        "# X\n\n## Setup từng bước\n\n```bash\npip install foo-sdk\nnpx -y @acme/bar-mcp\n"
        "export ACME_API_KEY=sk-live-1234567890abcdef\n```\n\n## Ví dụ thực tế\nChạy thử: foo --help\n"
    )

    def _may(self):
        return {"cong_cu": {"pip": {"co": True}, "node": {"co": True}, "python": {"co": True},
                            "git": {"co": False}, "npm": {"co": True}, "docker": {"co": False}, "ffmpeg": {"co": False}},
                "bien_khoa_dang_dat": []}

    def test_pip_npx_tra_buoc_kem_co_va_khong_chay_gi(self):
        d = _kho_gia({"repos/x": ({"needs": "api-key", "rui_ro": "tốn tiền"}, self.ENTRY)})
        with mock.patch.object(tk.subprocess, "run", side_effect=AssertionError("không được chạy subprocess")) as run, \
                mock.patch.object(tk.subprocess, "Popen", side_effect=AssertionError("Popen cấm")), \
                mock.patch.object(tk.os, "system", side_effect=AssertionError("os.system cấm")):
            plan = tk.install_plan("repos/x", machine=self._may(), repo_root=d)
            run.assert_not_called()
        self.assertTrue(plan["chua_chay_that"])
        self.assertIn("CHƯA CHẠY THẬT", plan["thong_bao"])
        loai = [b["loai"] for b in plan["buoc"]]
        self.assertIn("cai-goi", loai)
        self.assertIn("dat-bien-moi-truong", loai)
        self.assertEqual([b["so"] for b in plan["buoc"]], list(range(1, len(plan["buoc"]) + 1)))
        self.assertTrue(all(b["chua_chay"] for b in plan["buoc"]))
        # khong lo gia tri khoa
        self.assertNotIn("sk-live-1234567890abcdef", json.dumps(plan, ensure_ascii=False))
        self.assertEqual([x["ten"] for x in plan["bien_moi_truong"]], ["ACME_API_KEY"])
        # co rui ro + muc duyet: chi tien -> >= L2, khoa -> L3
        self.assertEqual(plan["muc_duyet"]["muc"], "L3")
        self.assertTrue(any(x["loai"] == "ton-tien" for x in plan["co_rui_ro"]))
        # thieu cong cu cua may gia (node co, pip co)
        self.assertEqual(plan["dieu_kien_tien_quyet"]["thieu"], [])
        self.assertTrue(plan["go_cai_dat"])
        self.assertTrue(plan["kiem_tra"]["lenh_goi_y"])

    def test_chi_gui_shutil_which_va_version(self):
        goi = []

        def gia_run(cmd, *a, **kw):
            goi.append(list(cmd))
            return mock.Mock(stdout="v9.9.9\n", stderr="", returncode=0)

        with mock.patch.object(tk.shutil, "which", side_effect=lambda n: "/usr/bin/" + n), \
                mock.patch.object(tk.subprocess, "run", side_effect=gia_run):
            m = tk.machine_profile()
            d = _kho_gia({"repos/x": ({}, self.ENTRY)})
            tk.install_plan("repos/x", machine=m, repo_root=d)
            tk.install_plan("repos/x", repo_root=d)  # machine=None -> tu goi machine_profile
        self.assertTrue(goi)
        for c in goi:
            self.assertEqual(len(c), 2, c)
            self.assertEqual(c[1], "--version", c)
        self.assertTrue(m["cong_cu"]["git"]["co"])

    def test_phat_hien_curl_pipe_sh_va_lenh_nguy_hiem(self):
        md = ("## Cài đặt\n```bash\ncurl -fsSL https://example.com/install.sh | sh\nsudo apt install foo\n"
              "rm -rf ./build\nchmod 777 /srv/app\ncp config.json ~/.config/foo/\n```\n")
        d = _kho_gia({"repos/nguy": ({}, md)})
        plan = tk.install_plan("repos/nguy", machine=self._may(), repo_root=d)
        do = " | ".join(x["ly_do"] for x in plan["co_do"])
        self.assertIn("curl|sh", do)
        self.assertIn("sudo", do)
        self.assertIn("rm -rf", do)
        self.assertIn("chmod 777", do)
        self.assertIn("ngoài thư mục dự án", do)
        self.assertTrue(all(b["can_nguoi_doc_ky"] for b in plan["buoc"] if b["co_do"]))
        self.assertTrue(any(b["can_nguoi_doc_ky"] for b in plan["buoc"]))
        self.assertNotEqual(plan["muc_duyet"]["muc"], "L0")

    def test_powershell_iex_la_co_do(self):
        md = "## Setup\n```powershell\nirm https://x.dev/i.ps1 | iex\n```\n"
        d = _kho_gia({"repos/ps": ({}, md)})
        plan = tk.install_plan("repos/ps", machine=self._may(), repo_root=d)
        self.assertTrue(plan["co_do"])

    def test_cau_hinh_mcp_json_che_gia_tri_khoa(self):
        md = ("## Setup\n```json\n{\"mcpServers\": {\"a\": {\"command\": \"npx\", \"args\": [\"-y\", \"a-mcp\"],"
              " \"env\": {\"A_TOKEN\": \"ghp_abcdefghijklmnop12345\"}}}}\n```\n")
        d = _kho_gia({"mcps/a": ({"loai": "mcp"}, md)})
        plan = tk.install_plan("mcps/a", machine=self._may(), repo_root=d)
        txt = json.dumps(plan, ensure_ascii=False)
        self.assertNotIn("ghp_abcdefghijklmnop12345", txt)
        self.assertIn("A_TOKEN", [x["ten"] for x in plan["bien_moi_truong"]])
        self.assertEqual(plan["muc_duyet"]["muc"], "L3")

    def test_vps_co_khach_la_L2(self):
        md = "## Setup\n```bash\ndocker compose up -d\n```\n"
        d = _kho_gia({"repos/v": ({"needs": "docker,vps"}, md)})
        m = self._may()
        m["vps_co_khach"] = True
        plan = tk.install_plan("repos/v", machine=m, repo_root=d)
        self.assertEqual(plan["muc_duyet"]["muc"], "L2")
        self.assertIn("docker", plan["dieu_kien_tien_quyet"]["thieu"])

    def test_entry_that_tu_catalog(self):
        plan = tk.install_plan("mcps/crawl4ai", machine=self._may())
        self.assertTrue(plan["doc_entry_goc"])
        self.assertTrue(any(b["loai"] == "chay-docker" for b in plan["buoc"]))
        self.assertTrue(any(b["loai"] == "sua-cau-hinh" for b in plan["buoc"]))


class MayVaSo(unittest.TestCase):
    def test_machine_profile_khong_lo_gia_tri_khoa(self):
        with mock.patch.dict(os.environ, {"THUKHO_FAKE_API_KEY": "GIATRI-BI-MAT-987"}):
            m = tk.machine_profile(lay_phien_ban=False)
        self.assertIn("THUKHO_FAKE_API_KEY", m["bien_khoa_dang_dat"])
        self.assertNotIn("GIATRI-BI-MAT-987", json.dumps(m, ensure_ascii=False))

    def test_usage_line_tu_choi_ket_qua_sai(self):
        with self.assertRaises(ValueError):
            tk.usage_line("mcps/buffer-mcp", "Dự án A", "tốt", "1 giờ", "")
        with self.assertRaises(ValueError):
            tk.usage_line("mcps/buffer-mcp", "Dự án A", "ok", "1 giờ", "")
        for kq, can in (("dung duoc", "dùng được"), ("phải sửa", "phải sửa"), ("bo", "bỏ")):
            line = tk.usage_line("mcps/buffer-mcp", "Dự án A", kq, "2 giờ", "ghi chú | có gạch")
            self.assertIn("| %s |" % can, line)
            self.assertEqual(line.count("|"), 7)  # 6 cot, ky tu | trong ghi chu da bi thay
        with self.assertRaises(KeyError):
            tk.usage_line("mcps/khong-co", "A", "bo", "", "")

    def test_gap_line_dung_cot(self):
        line = tk.gap_line("lập trình robot hút bụi", "Khách X", "kho không có")
        self.assertTrue(line.startswith("| ") and line.endswith(" |"))
        self.assertEqual(len(line.strip("|").split(" | ")), 6)
        self.assertTrue(line.rstrip().endswith("| mở |"))


class GoiY(unittest.TestCase):
    def test_vo_ly_tra_hong(self):
        g = tk.recommend("lập trình robot hút bụi")
        self.assertTrue(g["hong"])
        self.assertEqual(g["kha_nang"], [])
        self.assertIn("GAP-LOG", g["hong"][0]["hanh_dong"])

    def test_yeu_cau_dai_tach_kha_nang(self):
        g = tk.recommend("Làm kênh Facebook: cào web đối thủ, đăng bài có lịch, làm video ngắn không GPU, báo cáo dashboard",
                         vessel="hermes")
        caps = [k["capability"] for k in g["kha_nang"]]
        for c in ("scraping", "social-media", "video-generation", "data-dashboard"):
            self.assertIn(c, caps)
        for k in g["kha_nang"]:
            self.assertTrue(k["chinh"])
            if k["du_phong"]:
                self.assertNotEqual(k["du_phong"]["dup_group"] or "x1", k["chinh"][0]["dup_group"] or "x2")
        self.assertFalse([it for k in g["kha_nang"] for it in k["chinh"] if "gpu" in it["needs"].split(",")])
        self.assertTrue(any("chưa mục nào" in w for w in g["canh_bao"]))
        json.dumps(g)

    def test_hong_khi_het_ung_vien(self):
        d = _kho_gia({"repos/a": ({"capability": "scraping"}, "# a")})
        g = tk.recommend("cào web và làm video ngắn", repo_root=d)
        self.assertTrue([h for h in g["hong"] if h.get("capability") == "video-generation"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
