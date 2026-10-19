"""Test cho các lỗi mã first-party đã sửa (catalog/smoke/CODE-REPORT.md):
render stats, compliance-gate history[:5], script triển khai, pm2.config.js, .gitattributes/.gitignore.
Không mạng: git chỉ chạy trên repo tạm cục bộ, node/bash chạy file cục bộ.
Chạy: python -m unittest discover -s tools/tests"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def find_bash():
    cands = [r"C:\Program Files\Git\bin\bash.exe", r"C:\Program Files\Git\usr\bin\bash.exe"]
    for c in cands:
        if os.path.exists(c):
            return c
    b = shutil.which("bash")
    if b and "system32" not in b.lower():
        return b
    return None


BASH = find_bash()
NODE = shutil.which("node")


def lf_copy(src, dst):
    data = Path(src).read_bytes().replace(b"\r\n", b"\n")
    Path(dst).parent.mkdir(parents=True, exist_ok=True)
    Path(dst).write_bytes(data)


def posix(p):
    """Đường dẫn dạng bash hiểu được (Git Bash chấp nhận C:/...)."""
    return str(p).replace("\\", "/")


# ---------------------------------------------------------------- render
class RenderStatsTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        path = ROOT / "agents/shorts-affiliate-system/render/build_render_html.py"
        spec = importlib.util.spec_from_file_location("build_render_html", path)
        cls.brh = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.brh)

    def _storyboard(self, d):
        sb = {"scenes": [{"type": "stats-grid", "duration": 3, "content": {"stats": [
            {"label": "Tốc độ", "value": "10x"}, {"label": "Giá", "value": "$0"}]}}]}
        p = Path(d) / "sb.json"
        p.write_text(json.dumps(sb, ensure_ascii=False), encoding="utf-8")
        return p

    def test_full_render_has_no_template_leftovers_or_garbage(self):
        with tempfile.TemporaryDirectory() as d:
            out = Path(d) / "render.html"
            self.brh.build(str(self._storyboard(d)), str(out))
            html = out.read_text(encoding="utf-8")
        self.assertNotIn("{{#stats}}", html)
        self.assertNotIn("{{/stats}}", html)
        self.assertNotIn("{{", html)
        self.assertNotIn("label/value -->", html)
        self.assertEqual(html.count('class="stat-item"'), 2)
        for s in ("10x", "Tốc độ", "$0", "Giá"):
            self.assertIn(s, html)
        self.assertNotIn("<!--", html.split("<body>")[1])

    def test_comment_mentioning_loop_tag_is_ignored_even_in_old_template(self):
        # chính xác chú thích gây lỗi trước đây, kiểm riêng phần sửa regex
        old = ("<div><!-- render_template.html lặp {{#stats}} label/value -->\n"
               "{{#stats}}<i>{{value}}|{{label}}</i>{{/stats}}</div>")
        out = self.brh.fill_scene(old, {"stats": [{"label": "L", "value": "V"}]})
        self.assertNotIn("{{", out)
        self.assertNotIn("label/value", out)
        self.assertEqual(out.count("<i>"), 1)
        self.assertIn("<i>V|L</i>", out)

    def test_template_file_comment_no_longer_contains_loop_tag(self):
        raw = (ROOT / "agents/shorts-affiliate-system/scenes/scene-templates.html").read_text(encoding="utf-8")
        for c in re.findall(r"<!--.*?-->", raw, re.S):
            self.assertNotIn("{{#", c)
            self.assertNotIn("{{/", c)


# ---------------------------------------------------------------- compliance-gate
class ComplianceGateTest(unittest.TestCase):
    PATHS = [ROOT / "agents/yt-cashcow/skills/compliance-gate/SKILL.md",
             ROOT / "agents/shorts-affiliate-system/skills/compliance-gate/SKILL.md"]

    def _namespace(self):
        text = self.PATHS[0].read_text(encoding="utf-8")
        ns = {}
        for block in re.findall(r"```python\n(.*?)```", text, re.S):
            exec(compile(block, "SKILL.md", "exec"), ns)
        return ns

    def test_two_copies_byte_identical(self):
        self.assertEqual(self.PATHS[0].read_bytes(), self.PATHS[1].read_bytes())

    def test_uses_newest_five_from_newest_first_history(self):
        ns = self._namespace()
        new_fp = {"structure_type": "narrative", "hook_type": "question",
                  "unique_claims": ["a", "b", "c"], "commentary_ratio": 0.5}
        types = ["tutorial", "comparison", "case-study"]
        hooks = ["shock-stat", "story-open", "controversy", "how-to"]
        history = []
        for i in range(15):  # i=0 là MỚI NHẤT (get_fingerprint_history sort desc)
            history.append({"structure_type": types[i % 3], "hook_type": hooks[i % 4],
                            "unique_claims": ["a", "b", "c"] if i < 5 else [f"old{i}"]})
        res, why = ns["check_compliance"](new_fp, history)
        self.assertEqual(res, "FAIL")  # 5 video mới nhất trùng claims
        self.assertIn("trùng lặp", why)
        # đảo lại: claims trùng nằm ở 5 video CŨ NHẤT -> không được tính
        res2, _ = ns["check_compliance"](new_fp, list(reversed(history)))
        self.assertEqual(res2, "PASS")

    def test_doc_documents_ordering_and_no_negative_slice(self):
        text = self.PATHS[0].read_text(encoding="utf-8")
        blocks = re.findall(r"```python\n(.*?)```", text, re.S)
        code = "\n".join(blocks)
        code = "\n".join(l for l in code.splitlines() if not l.lstrip().startswith("#"))
        self.assertNotIn("history[-5:]", code)
        self.assertIn("history[:5]", code)
        self.assertIn("direction]=desc", text)


# ---------------------------------------------------------------- shell scripts
@unittest.skipUnless(BASH, "cần Git Bash/bash")
class ShellScriptsTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.home = self.root / "home"
        self.home.mkdir()
        self.env = {**os.environ, "HOME": posix(self.home),
                    "GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@t.test",
                    "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@t.test",
                    "TELEGRAM_BOT_TOKEN": "", "TELEGRAM_CHAT_ID": ""}

    def run_sh(self, script, cwd=None):
        return subprocess.run([BASH, posix(script)], capture_output=True, text=True,
                              encoding="utf-8", env=self.env, cwd=cwd)

    def git(self, cwd, *args):
        r = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True,
                           encoding="utf-8", env=self.env)
        self.assertEqual(r.returncode, 0, r.stderr)
        return r.stdout.strip()

    def test_all_scripts_pass_bash_n_after_lf(self):
        for rel in ["deploy/setup-vps.sh", "deploy/auto-sync.sh", "configs/sync-to-openclaw.sh"]:
            dst = self.root / "chk" / Path(rel).name
            lf_copy(ROOT / rel, dst)
            r = subprocess.run([BASH, "-n", posix(dst)], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(r.returncode, 0, f"{rel}: {r.stderr}")

    def test_sync_to_openclaw_skips_missing_ecc(self):
        repo = self.root / "repo"
        lf_copy(ROOT / "configs/sync-to-openclaw.sh", repo / "configs/sync-to-openclaw.sh")
        (repo / "configs/openclaw-ai-vibe-skill.md").write_text("skill", encoding="utf-8")
        (repo / "skills/agent-skills").mkdir(parents=True)
        (repo / "skills/agent-skills/a.md").write_text("a", encoding="utf-8")
        (repo / "skills/root.md").write_text("r", encoding="utf-8")
        # KHÔNG có skills/ecc
        r = self.run_sh(repo / "configs/sync-to-openclaw.sh")
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertIn("Bỏ qua ecc", r.stdout)
        sk = self.home / ".openclaw/skills"
        self.assertTrue((sk / "agent-skills/a.md").exists())  # các bước sau ecc vẫn chạy
        self.assertTrue((sk / "root.md").exists())
        self.assertTrue((sk / "ai-vibe-toolkit.md").exists())

    def _make_remote_and_clone(self):
        origin = self.root / "origin.git"
        work = self.root / "work"
        self.git(self.root, "init", "-q", "--bare", "-b", "main", str(origin))
        self.git(self.root, "clone", "-q", str(origin), str(work))
        self.git(work, "checkout", "-q", "-B", "main")
        (work / "skills/viral-hooks").mkdir(parents=True)
        (work / "skills/viral-hooks/h.md").write_text("h1", encoding="utf-8")
        (work / "skills/top.md").write_text("t", encoding="utf-8")
        self.git(work, "add", "-A")
        self.git(work, "commit", "-q", "-m", "c1")
        self.git(work, "push", "-q", "origin", "main")
        clone = self.home / "ai-vibe-toolkit"
        self.git(self.root, "clone", "-q", "-b", "main", str(origin), str(clone))
        # commit mới trên remote
        (work / "skills/viral-hooks/h2.md").write_text("h2", encoding="utf-8")
        self.git(work, "add", "-A")
        self.git(work, "commit", "-q", "-m", "c2")
        self.git(work, "push", "-q", "origin", "main")
        script = self.root / "auto-sync.sh"
        lf_copy(ROOT / "deploy/auto-sync.sh", script)
        return clone, script

    def test_auto_sync_creates_logs_dir_and_tolerates_missing_ecc(self):
        clone, script = self._make_remote_and_clone()
        self.assertFalse((self.home / "logs").exists())  # trước đây thiếu mkdir ~/logs
        r = self.run_sh(script)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)
        self.assertTrue((self.home / "logs/kho-sync.log").exists())
        sk = self.home / ".openclaw/skills"
        self.assertTrue((sk / "viral-hooks/h2.md").exists())  # sync vẫn chạy dù không có skills/ecc
        self.assertTrue((sk / "top.md").exists())
        stamp = (self.home / ".openclaw/.kho-synced-sha").read_text().strip()
        self.assertEqual(stamp, self.git(clone, "rev-parse", "HEAD"))
        log = (self.home / "logs/kho-sync.log").read_text(encoding="utf-8")
        self.assertIn("skills/ecc", log)

    def test_auto_sync_resyncs_after_failed_sync_even_without_new_commits(self):
        clone, script = self._make_remote_and_clone()
        sk = self.home / ".openclaw/skills"
        sk.mkdir(parents=True)
        (sk / "viral-hooks").write_text("tôi là file nên mkdir/cp thư mục sẽ lỗi", encoding="utf-8")
        r1 = self.run_sh(script)
        self.assertNotEqual(r1.returncode, 0)  # sync lỗi sau khi đã pull
        self.assertFalse((self.home / ".openclaw/.kho-synced-sha").exists())
        (sk / "viral-hooks").unlink()  # sửa sự cố; remote KHÔNG có commit mới
        r2 = self.run_sh(script)
        self.assertEqual(r2.returncode, 0, r2.stdout + r2.stderr)
        self.assertTrue((sk / "viral-hooks/h2.md").exists())  # trước đây: không bao giờ đồng bộ lại
        r3 = self.run_sh(script)  # đã đồng bộ xong thì lượt sau không làm gì
        self.assertIn("Không có gì mới", (self.home / "logs/kho-sync.log").read_text(encoding="utf-8"))
        self.assertEqual(r3.returncode, 0)

    def test_setup_vps_has_no_pipe_to_shell(self):
        text = (ROOT / "deploy/setup-vps.sh").read_text(encoding="utf-8")
        code = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
        self.assertIsNone(re.search(r"curl[^\n]*\|\s*(sudo\s+)?bash", code))
        self.assertIsNone(re.search(r"\|\s*(sudo\s+)?bash\b", code))
        self.assertIn("NODESOURCE_REVIEWED", code)


# ---------------------------------------------------------------- pm2.config.js
@unittest.skipUnless(NODE, "cần node")
class Pm2ConfigTest(unittest.TestCase):
    def test_loads_env_without_dotenv_package(self):
        src = (ROOT / "deploy/pm2.config.js").read_text(encoding="utf-8")
        code_lines = [l for l in src.splitlines() if not l.lstrip().startswith("//")]
        self.assertNotIn("require('dotenv')", "\n".join(code_lines))
        with tempfile.TemporaryDirectory() as d:
            home = Path(d)
            (home / "ai-vibe-toolkit").mkdir()
            (home / "ai-vibe-toolkit/.env").write_text(
                "# comment\nANTHROPIC_API_KEY=sk-test-123 # inline\nexport TELEGRAM_BOT_TOKEN=\"tg test\"\n"
                "TELEGRAM_CHAT_ID='42'\nGITHUB_TOKEN=keep-existing\n", encoding="utf-8")
            code = ("const c=require(process.argv[1]);"
                    "console.log(JSON.stringify(c.apps.map(a=>a.name)));"
                    "console.log(JSON.stringify(c.apps[0].env));")
            env = {k: v for k, v in os.environ.items()
                   if k not in ("ANTHROPIC_API_KEY", "TELEGRAM_BOT_TOKEN", "TELEGRAM_CHAT_ID")}
            env.update({"HOME": str(home), "GITHUB_TOKEN": "already-set"})
            r = subprocess.run([NODE, "-e", code, str(ROOT / "deploy/pm2.config.js")],
                               capture_output=True, text=True, encoding="utf-8", env=env, cwd=d)
        self.assertEqual(r.returncode, 0, r.stderr)
        names, envs = [json.loads(x) for x in r.stdout.strip().splitlines()]
        self.assertEqual(names, ["openclaw", "hermes", "kho-sync"])
        self.assertEqual(envs["ANTHROPIC_API_KEY"], "sk-test-123")
        self.assertEqual(envs["TELEGRAM_BOT_TOKEN"], "tg test")
        self.assertEqual(envs["TELEGRAM_CHAT_ID"], "42")
        self.assertEqual(envs["GITHUB_TOKEN"], "already-set")  # không ghi đè biến có sẵn

    def test_missing_env_file_does_not_crash(self):
        with tempfile.TemporaryDirectory() as d:
            r = subprocess.run([NODE, "-e", "require(process.argv[1])", str(ROOT / "deploy/pm2.config.js")],
                               capture_output=True, text=True, encoding="utf-8",
                               env={**os.environ, "HOME": d}, cwd=d)
        self.assertEqual(r.returncode, 0, r.stderr)


# ---------------------------------------------------------------- repo hygiene
class RepoHygieneTest(unittest.TestCase):
    def test_gitattributes_forces_lf(self):
        text = (ROOT / ".gitattributes").read_text(encoding="utf-8")
        self.assertRegex(text, r"\*\.sh\s+.*eol=lf")
        self.assertRegex(text, r"\*\.py\s+.*eol=lf")

    def test_gitignore_has_pycache(self):
        self.assertIn("__pycache__/", (ROOT / ".gitignore").read_text(encoding="utf-8").splitlines())

    def test_no_pycache_tracked(self):
        r = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8")
        if r.returncode != 0:
            self.skipTest("không phải git repo")
        self.assertEqual([f for f in r.stdout.splitlines() if "__pycache__" in f or f.endswith(".pyc")], [])


if __name__ == "__main__":
    unittest.main()
