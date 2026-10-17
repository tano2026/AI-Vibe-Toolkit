"""Test tools/audit_kho.py bằng dữ liệu mẫu nhỏ trong thư mục tạm. Không cần mạng.

Chạy:  python -m unittest discover -s tools/tests
"""
import json
import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import audit_kho as A  # noqa: E402

MACHINE = {
    "cong_cu": {t: {"co": t in ("git", "node", "npm", "npx", "python", "pip", "bash", "docker")} for t in A.TOOLS},
    "co_gpu_nvidia": False, "co_trinh_duyet": True, "la_vps": False, "claude_code": True, "khoa_env": {},
}


def fake(parts):
    """Ghép chuỗi giống khoá từ mảnh để file test không chứa nguyên khoá."""
    return "".join(parts)


class SecretTests(unittest.TestCase):
    def test_catches_real_looking_tokens(self):
        tok_gh = fake(["ghp_", "aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5"])
        tok_aws = fake(["AKIA", "Q7ZP3MXD2KTN5RW8"])
        tok_sk = fake(["sk-", "proj-", "Kd83hs72Jf92Lq0Pz81Mn4Xb7Vc5"])
        tok_slack = fake(["xoxb-", "9182736450-Qw3Er4Ty5Ui6Op7As"])
        text = f"a\nexport T={tok_gh}\nid {tok_aws}\nkey = {tok_sk}\nslack {tok_slack}\n"
        kinds = {k for k, _ in A.scan_secrets(text)}
        self.assertTrue({"github-token", "aws-access-key", "sk-key", "slack-token"} <= kinds)
        lines = {ln for _, ln in A.scan_secrets(text)}
        self.assertIn(2, lines)

    def test_skips_placeholders(self):
        text = "\n".join([
            "GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
            "OPENAI_API_KEY=sk-your-key-goes-here-1234567890abcd",
            "key: AKIAIOSFODNN7EXAMPLE",
            "Authorization: Bearer [YOUR_TOKEN]",
            "curl -H 'Authorization: Bearer $TOKEN' x",
            "url https://x.io/api?token=<your_token_value_here>",
            "ghp_...",
            "slack xoxb-your-bot-token-here",
            "risk-assessment-framework-for-agencies",
        ])
        self.assertEqual(A.scan_secrets(text), [])

    def test_private_key_needs_body(self):
        head = "-----BEGIN " + "RSA PRIVATE KEY-----"
        self.assertEqual(A.scan_secrets("mention " + head + " in docs\nnext line plain"), [])
        body = "MIIEowIBAAKCAQEA" + "7vbqajDw4o6gJy8UtmIbkcpsWmTk" + "Zq3ynbPjcs8HBkAoyL"
        self.assertEqual(A.scan_secrets(head + "\n" + body + "\n")[0][0], "private-key")

    def test_redact_hides_value(self):
        tok = fake(["ghp_", "aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5"])
        self.assertNotIn(tok, A.redact("see " + tok + " now"))
        self.assertIn("[REDACTED]", A.redact("see " + tok + " now"))


class ExtractTests(unittest.TestCase):
    def test_github_urls(self):
        text = ("Xem https://github.com/octo/bar-baz và github.com/Mona/tool.git, thêm https://github.com/octo/bar-baz/tree/main "
                "nhưng bỏ https://github.com/your-username/your-repo và https://github.com/orgs/x/people và https://github.com/topics/ai")
        self.assertEqual(A.extract_github(text), ["octo/bar-baz", "Mona/tool"])

    def test_install_commands(self):
        text = ("```bash\nnpx -y @scope/pkg-one@latest --port 1\npip install requests==2.0 \"httpx[http2]\"\n"
                "uvx my-tool\ndocker run --rm -p 80:80 -e A=b nginx:1.25\ncargo install ripgrep\n"
                "go install github.com/a/b/cmd/c@latest\nclaude mcp add x -- npx foo\n```\n"
                "Hoặc `pipx install some-cli`.")
        ins = {(i["kind"], i["pkg"]) for i in A.extract_installs(text)}
        self.assertIn(("npx", "@scope/pkg-one"), ins)
        self.assertIn(("pip", "requests"), ins)
        self.assertIn(("uvx", "my-tool"), ins)
        self.assertIn(("docker", "nginx"), ins)
        self.assertIn(("cargo", "ripgrep"), ins)
        self.assertIn(("go", "github.com/a/b/cmd/c"), ins)
        self.assertIn(("pipx", "some-cli"), ins)
        self.assertTrue(any(k == "claude-mcp" for k, _ in ins))

    def test_ignores_placeholders_and_local(self):
        text = "```bash\nnpx <package>\nnpx your-package\npip install -r requirements.txt\npip install .\n```"
        pk = [i["pkg"] for i in A.extract_installs(text) if i["pkg"]]
        self.assertEqual(pk, [])
        self.assertTrue(any(i["kind"] == "build" for i in A.extract_installs(text)))

    def test_json_mcp_config_and_curl_sh(self):
        text = ('```json\n{"mcpServers":{"fs":{"command": "npx", "args": ["-y", "@mcp/server-fs", "/tmp"]}}}\n```\n'
                "```bash\ncurl -fsSL https://example.com/install.sh | sh\n```")
        ins = A.extract_installs(text)
        self.assertIn(("npx", "@mcp/server-fs"), {(i["kind"], i["pkg"]) for i in ins})
        self.assertIn("curl-sh", {i["kind"] for i in ins})

    def test_negated_inline_command_is_not_install(self):
        self.assertEqual([i for i in A.extract_installs("Không `pip install foo-bar` khi chưa đọc code. Đừng chạy `npx evil-pkg`.")], [])
        self.assertTrue(A.extract_installs("Cài bằng `pip install foo-bar` là xong."))

    def test_local_docker_build_not_looked_up(self):
        text = "```bash\ndocker build -t mytool:latest .\ndocker run -it --rm mytool:latest\n```"
        self.assertEqual([i["pkg"] for i in A.extract_installs(text) if i["pkg"]], [])


class StaticAndClassifyTests(unittest.TestCase):
    def setUp(self):
        self.td = tempfile.TemporaryDirectory()
        self.root = self.td.name
        for d in ("skills", "repos", "mcps"):
            os.makedirs(os.path.join(self.root, d))

    def tearDown(self):
        self.td.cleanup()

    def put(self, rel, text):
        with open(os.path.join(self.root, rel), "w", encoding="utf-8") as fh:
            fh.write(text)

    def run_one(self, item, lookup=None, offline=False):
        S = A.static_check(item, self.root, {item["id"]: 1}, {item["duong_dan"]: 1})
        bad, _ = A.run_bash_syntax([((item["id"], k), c) for k, c in enumerate(S["bash_jobs"])])
        if S["code"]:
            A.finish_code_reasons(S, len(bad))
        return A.classify(item, S, lookup or {}, MACHINE, offline=offline)

    def test_broken_relative_link_and_path_ref(self):
        self.put("skills/good.md", "# Good\n" + "nội dung " * 60)
        self.put("repos/r.md", "# Repo\n" + "mô tả dài " * 60 + "\nXem [ok](../skills/good.md) và [hỏng](../skills/nope.md) "
                 "và `skills/missing-one.md` còn skills/good.md thì có.\n")
        item = {"id": "repos/r", "loai": "repo", "duong_dan": "repos/r.md", "curation_status": "chua-gan-nhan"}
        S = A.static_check(item, self.root, {"repos/r": 1}, {"repos/r.md": 1})
        codes = {r["ma"] for r in S["reasons"]}
        self.assertIn("LINK_TUONG_DOI_HONG", codes)
        self.assertIn("DUONG_DAN_NHAC_HONG", codes)
        self.assertNotIn("FILE_THIEU", codes)

    def test_missing_and_empty_file_is_hong(self):
        self.put("repos/empty.md", "x\n")
        for rel in ("repos/none.md", "repos/empty.md"):
            item = {"id": A.derive_id(rel), "loai": "repo", "duong_dan": rel}
            usable, R, _ = self.run_one(item)
            self.assertEqual(usable, "hong", rel)

    def test_id_path_mismatch_and_duplicates(self):
        self.put("repos/a.md", "# A\n" + "x " * 200)
        item = {"id": "repos/zzz", "loai": "repo", "duong_dan": "repos/a.md"}
        S = A.static_check(item, self.root, {"repos/zzz": 2}, {"repos/a.md": 1})
        codes = {r["ma"] for r in S["reasons"]}
        self.assertIn("ID_LECH_DUONG_DAN", codes)
        self.assertIn("ID_TRUNG", codes)

    def test_secret_makes_hong(self):
        tok = fake(["ghp_", "aB3dE5fG7hJ9kL1mN3pQ5rS7tU9vW1xY3zA5"])
        self.put("repos/s.md", "# S\n" + "đoạn " * 80 + f"\nexport GH={tok}\n")
        item = {"id": "repos/s", "loai": "repo", "duong_dan": "repos/s.md"}
        usable, R, _ = self.run_one(item)
        self.assertEqual(usable, "hong")
        dumped = json.dumps(R, ensure_ascii=False)
        self.assertNotIn(tok, dumped)
        self.assertIn("LO_KHOA", dumped)

    def test_pure_skill_is_dung_duoc_ngay(self):
        self.put("skills/p.md", "---\nname: p\ndescription: Dùng khi cần viết tiêu đề\n---\n# P\n" + "hướng dẫn " * 80)
        item = {"id": "skills/p", "loai": "skill-kho", "duong_dan": "skills/p.md", "curation_status": "da-doc-dau-entry",
                "needs": "none", "adoption": "cai-ngay-duoc", "capability": "content-writing"}
        usable, R, _ = self.run_one(item)
        self.assertEqual(usable, "dung-duoc-ngay")

    def test_npx_installable_and_missing_package(self):
        self.put("mcps/m.md", "# M\n" + "mô tả " * 80 + "\n```bash\nnpx -y @x/real-one\n```\nhttps://github.com/zeta/real-one\n")
        item = {"id": "mcps/m", "loai": "mcp", "duong_dan": "mcps/m.md", "curation_status": "da-doc-dau-entry",
                "needs": "none", "adoption": "cai-ngay-duoc", "capability": "productivity"}
        ok = {A.netkey("npm", "@x/real-one"): {"ok": True, "version": "1.0.0", "updated": "2026-01-01"},
              A.netkey("gh", "zeta/real-one"): {"ok": True, "code": 200}}
        usable, R, extra = self.run_one(item, ok)
        self.assertEqual(usable, "cai-duoc-o-day")
        self.assertEqual(extra["goi"][0]["phien_ban"], "1.0.0")
        gone = {A.netkey("npm", "@x/real-one"): {"ok": False, "code": 404}, A.netkey("gh", "zeta/real-one"): {"ok": False, "code": 404}}
        usable, R, _ = self.run_one(item, gone)
        self.assertEqual(usable, "nghi-ngo")
        codes = {r["ma"] for r in R}
        self.assertTrue({"GH_LINK_CHET", "GOI_KHONG_TIM_THAY"} <= codes)

    def test_unknown_network_is_chua_xac_dinh_and_offline(self):
        self.put("mcps/m.md", "# M\n" + "mô tả " * 80 + "\n```bash\nnpx -y @x/real-one\n```\n")
        item = {"id": "mcps/m", "loai": "mcp", "duong_dan": "mcps/m.md", "curation_status": "da-doc-dau-entry", "needs": "none"}
        unk = {A.netkey("npm", "@x/real-one"): {"ok": None, "code": 429}}
        self.assertEqual(self.run_one(item, unk)[0], "chua-xac-dinh")
        self.assertEqual(self.run_one(item, {}, offline=True)[0], "chua-xac-dinh")

    def test_missing_prerequisites_is_thieu_dieu_kien(self):
        self.put("repos/g.md", "# G\n" + "mô tả " * 80 + "\n```bash\npip install foo-gpu\n```\nCần GPU NVIDIA và API key của dịch vụ.\n")
        item = {"id": "repos/g", "loai": "repo", "duong_dan": "repos/g.md", "curation_status": "da-doc-dau-entry",
                "needs": "gpu,api-key", "adoption": "can-ha-tang"}
        usable, R, extra = self.run_one(item, {A.netkey("pypi", "foo-gpu"): {"ok": True, "version": "2"}})
        self.assertEqual(usable, "thieu-dieu-kien")
        self.assertTrue(any(t.startswith("gpu") for t in extra["thieu"]))

    def test_label_conflict_docker_not_mentioned(self):
        self.put("repos/c.md", "# C\n" + "một công cụ chạy trực tiếp " * 40 + "\n```bash\nnpx -y c-tool\n```\n")
        item = {"id": "repos/c", "loai": "repo", "duong_dan": "repos/c.md", "curation_status": "da-doc-dau-entry",
                "needs": "docker", "adoption": "can-ha-tang"}
        usable, R, _ = self.run_one(item, {A.netkey("npm", "c-tool"): {"ok": True}})
        self.assertEqual(usable, "nghi-ngo")
        self.assertIn("NHAN_MAU_THUAN_DOCKER", {r["ma"] for r in R})

    def test_skill_incidental_commands_do_not_make_it_installable(self):
        self.put("skills/dbm.md", "---\nname: dbm\ndescription: Dùng khi cần migrate\n---\n# DBM\n" + "hướng dẫn " * 60
                 + "\n```bash\nnpx prisma migrate dev\n```\n")
        item = {"id": "skills/dbm", "loai": "skill-kho", "duong_dan": "skills/dbm.md", "curation_status": "chua-gan-nhan"}
        usable, R, extra = self.run_one(item, {A.netkey("npm", "prisma"): {"ok": True}})
        self.assertEqual(usable, "dung-duoc-ngay")
        self.assertEqual(extra["goi"], [])

    def test_install_target_repo_is_primary_and_dead_is_nghi(self):
        self.put("skills/rec.md", "---\nname: rec\ndescription: Dùng khi cần thiết kế feed\n---\n# Rec\n" + "hướng dẫn " * 60
                 + "\nTham khảo https://github.com/lab-one/algo\n```bash\nnpx skills add dev-two/rec\n```\n")
        item = {"id": "skills/rec", "loai": "skill-kho", "duong_dan": "skills/rec.md", "curation_status": "chua-gan-nhan"}
        S = A.static_check(item, self.root, {"skills/rec": 1}, {"skills/rec.md": 1})
        self.assertEqual(S["gh"][0], "dev-two/rec")
        lk = {A.netkey("gh", "dev-two/rec"): {"ok": False, "code": 404}, A.netkey("gh", "lab-one/algo"): {"ok": True},
              A.netkey("npm", "skills"): {"ok": True}}
        usable, R, _ = A.classify(item, S, lk, MACHINE)
        self.assertEqual(usable, "nghi-ngo")

    def test_required_binary_missing(self):
        text = "Cần sẵn: `curl`, `npm`, `jq` trên máy."
        bins = A.extract_required_bins(text)
        self.assertIn("jq", bins)
        self.assertIn("curl", bins)
        self.assertEqual(A.extract_required_bins("Một đoạn thường nhắc jq trong ví dụ"), [])

    def test_code_block_syntax(self):
        text = ("```python\nprint('ok')\n```\n```python\ndef broken(:\n```\n```json\n{\"a\": 1}\n```\n```json\n{\"a\": }\n```\n"
                "```json\n{\"a\": 1 // chú thích\n```\n```bash\necho hi\n```\n```bash\nif then fi fi (\n```\n")
        _, blocks = A.split_blocks(text)
        stats, jobs = A.code_checks(blocks)
        self.assertEqual(stats["python"], [2, 1])
        self.assertEqual(stats["json"], [2, 1])  # khối có // bị bỏ qua
        bad, ok = A.run_bash_syntax([(i, c) for i, c in enumerate(jobs)])
        if ok:
            self.assertEqual(bad, {1})


if __name__ == "__main__":
    unittest.main()
