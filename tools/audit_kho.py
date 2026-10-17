#!/usr/bin/env python3
"""KIỂM TOÁN TỰ ĐỘNG toàn kho: mục nào "sử dụng được"? (chỉ kiểm TĨNH + truy vấn mạng CHỈ-ĐỌC)

Chạy:   python tools/audit_kho.py                       # đủ 2 tầng, có mạng
        python tools/audit_kho.py --offline             # bỏ phần mạng
        python tools/audit_kho.py --only repos/         # chỉ id bắt đầu bằng tiền tố
        python tools/audit_kho.py --json-out X --md-out Y --cache scratch/cache.json
Ra:     catalog/audit.json  (id -> kết quả + hồ sơ máy + thời điểm)
        catalog/AUDIT.md    (bản đọc nhanh)

LUẬT CỨNG của công cụ này:
- KHÔNG chạy / cài / import bất kỳ mã nào lấy từ entry hay internet. Khối mã chỉ được parse (ast.parse,
  json.loads, bash -n = chỉ kiểm cú pháp, yaml.safe_load). Không pip/npm/npx/docker run/curl|sh.
- Mạng: chỉ GET/HEAD chỉ-đọc, tối đa 4 kết nối song song, timeout 10 giây, nghỉ giữa lượt, 429 -> "chưa xác định".
- Không in/không lưu giá trị khoá bí mật: chỉ ghi loại + số dòng, che bằng [REDACTED].
- Kết quả KHÔNG chứng minh công cụ chạy đúng, chỉ chứng minh điều kiện cần (chua_chay_that = true ở mọi mục).

Chỉ dùng thư viện chuẩn (PyYAML là tuỳ chọn: có thì kiểm cú pháp yaml, không có thì bỏ).
"""
import argparse
import ast
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

try:  # tuỳ chọn
    import yaml as _yaml
except Exception:  # pragma: no cover
    _yaml = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA = "audit-kho/1.0 (read-only link and registry check)"
VERSION = 1

# ===================================================================== đọc file / khối mã
def read_text(path):
    """Trả (text, lỗi). Lỗi: 'missing' | 'decode'."""
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except OSError:
        return None, "missing"
    try:
        return raw.decode("utf-8-sig").replace("\r\n", "\n"), None
    except UnicodeDecodeError:
        return raw.decode("utf-8", errors="replace").replace("\r\n", "\n"), "decode"


FENCE = re.compile(r"^(\s*)(`{3,}|~{3,})\s*([A-Za-z0-9_+.#-]*)[^\n]*$")


def split_blocks(text):
    """Tách (prose_without_blocks, [ (lang, code, start_line) ])."""
    blocks, prose = [], []
    lines = text.split("\n")
    i = 0
    while i < len(lines):
        m = FENCE.match(lines[i])
        if m:
            fence, lang = m.group(2), m.group(3).lower()
            j = i + 1
            body = []
            while j < len(lines):
                s = lines[j].strip()
                if s.startswith(fence[0] * len(fence)) and set(s) <= {fence[0]}:
                    break
                body.append(lines[j])
                j += 1
            blocks.append((lang, "\n".join(body), i + 1))
            prose.append("")
            i = j + 1
        else:
            prose.append(lines[i])
            i += 1
    return "\n".join(prose), blocks


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---(?:\n|$)", text, re.S)
    if not m:
        return None, text
    return m.group(1), text[m.end():]


# ===================================================================== khoá bí mật
PH_WORDS = ("xxx", "your", "example", "placeholder", "sample", "redacted", "dummy", "fake", "demo", "changeme",
            "replace", "insert", "token_here", "key_here", "abc123", "1234", "****", "....", "<", ">", "{", "}", "$",
            "...", "…")
SEQS = ("abcdefghij", "0123456789", "1234567890", "qwerty", "aaaaaaa")

SECRET_PATTERNS = [
    ("github-token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{30,}\b")),
    ("github-pat", re.compile(r"\bgithub_pat_[A-Za-z0-9_]{22,}\b")),
    ("sk-key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("hf-token", re.compile(r"\bhf_[A-Za-z0-9]{30,}\b")),
    ("npm-token", re.compile(r"\bnpm_[A-Za-z0-9]{36}\b")),
    ("gitlab-pat", re.compile(r"\bglpat-[A-Za-z0-9_-]{20,}")),
    ("stripe-live", re.compile(r"\b[sr]k_live_[A-Za-z0-9]{16,}")),
    ("bearer", re.compile(r"\bBearer\s+([A-Za-z0-9._~+/=-]{30,})")),
    ("token-in-url", re.compile(r"https?://[^\s\"')>]*[?&](?:token|access_token|api_key|apikey|key|secret)=([A-Za-z0-9_%.\-]{16,})", re.I)),
    ("password-in-url", re.compile(r"https?://[^/\s:@]+:([^/\s@]{6,})@")),
]
PRIVKEY = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |DSA |PGP )?PRIVATE KEY(?: BLOCK)?-----")
B64LINE = re.compile(r"^[A-Za-z0-9+/=]{40,}$")


def is_placeholder(tok):
    low = tok.lower()
    if any(w in low for w in PH_WORDS):
        return True
    if any(s in low for s in SEQS):
        return True
    body = re.sub(r"^(?:sk-ant-api\d+-|sk-proj-|sk-|github_pat_|gh[pousr]_|xox[a-z]-|AKIA|AIza|hf_|npm_|glpat-|[sr]k_live_)", "", tok)
    if len(set(body.lower())) <= 6:
        return True
    return False


def scan_secrets(text):
    """Trả list (loai, so_dong). KHÔNG trả giá trị."""
    found = []
    lines = text.split("\n")
    for ln, line in enumerate(lines, 1):
        for name, rx in SECRET_PATTERNS:
            for m in rx.finditer(line):
                tok = m.group(1) if m.groups() else m.group(0)
                if is_placeholder(tok):
                    continue
                if name == "sk-key" and len(re.findall(r"\d", tok)) < 2:
                    continue  # slug kebab-case, không phải khoá
                if name == "bearer" and (not re.search(r"\d", tok) or not re.search(r"[A-Za-z]", tok) or len(set(tok)) < 10):
                    continue
                if name in ("token-in-url", "password-in-url") and len(set(tok)) < 8:
                    continue
                found.append((name, ln))
        if PRIVKEY.search(line):
            body = [x.strip() for x in lines[ln:ln + 4]]
            if any(B64LINE.match(b) and not is_placeholder(b) for b in body):
                found.append(("private-key", ln))
    return found


def redact(s):
    """Che mọi thứ giống khoá trong một chuỗi dùng làm căn cứ."""
    for name, rx in SECRET_PATTERNS:
        s = rx.sub("[REDACTED]", s)
    return s


# ===================================================================== GitHub / gói cài
GH_RX = re.compile(r"(?<![\w.@-])(?:https?://)?(?:www\.)?github\.com/([A-Za-z0-9](?:[A-Za-z0-9-]{0,38}))/([A-Za-z0-9._-]+)")
GH_BAD_OWNER = {"orgs", "topics", "sponsors", "marketplace", "features", "settings", "apps", "login", "pricing", "about",
                "explore", "collections", "trending", "notifications", "search", "issues", "pulls", "new", "organizations",
                "enterprise", "security", "readme", "blog", "site", "contact", "customer-stories", "codespaces", "events",
                "user", "owner", "username", "your-username", "your-org", "yourname", "org", "you", "example", "your_username",
                "your-name", "yourusername", "your-github-username", "xxx", "foo", "me", "myuser", "my-org", "account",
                "your-account", "your-handle", "handle", "name", "company", "acme", "your-company", "organization", "x"}
GH_BAD_REPO = {"repo", "repository", "your-repo", "project", "repo-name", "name", "reponame", "xxx", "your-repo-name",
               "my-repo", "your-project", "my-project", "repo.git", "app", "yourrepo", "foo", "bar", "example", "reponame.git",
               "project-name", "repository-name", "your-fork", "fork", "my-app", "myrepo", "repo_name", "your_repo", "xyz"}


def extract_github(text):
    """Danh sách owner/repo duy nhất theo thứ tự xuất hiện (chữ thường để so sánh, giữ nguyên hoa/thường đầu tiên)."""
    seen, out = set(), []
    for m in GH_RX.finditer(text):
        owner, repo = m.group(1), m.group(2)
        repo = re.sub(r"\.git$", "", repo).rstrip(".-_")
        if not repo or owner.lower() in GH_BAD_OWNER or repo.lower() in GH_BAD_REPO:
            continue
        if "xxx" in repo.lower() or "your" in owner.lower() or "your" in repo.lower():
            continue
        key = f"{owner}/{repo}".lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(f"{owner}/{repo}")
    return out


PLACEHOLDER_PKG = {"package", "pkg", "package-name", "your-package", "your_package", "name", "foo", "bar", "my-package",
                   "mypackage", "x", "xxx", "module", "packagename", "pkgname", "package_name", "my_package", "some-package",
                   "example", "example-package", "mcp-server-name", "server-name", "tool", "tool-name", "skill-name",
                   "my-mcp-server", "my-server", "project", "app", "my-app", "your-tool", "mcp-package", "your-mcp-server"}
NPM_NAME = re.compile(r"^(?:@[A-Za-z0-9][\w.-]*/)?[A-Za-z0-9][\w.~-]*$")
PY_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
SEG_SPLIT = re.compile(r"\s*(?:&&|\|\||;|\||>|<|\s#\s)\s*")
PIP_ARG_FLAGS = {"-r", "-e", "-c", "-i", "--index-url", "--extra-index-url", "-t", "--target", "--prefix", "--constraint",
                 "--requirement", "--editable", "-f", "--find-links", "--python", "--root", "--platform", "--only-binary"}
DOCKER_ARG_FLAGS = {"-p", "-v", "-e", "--name", "--network", "-w", "-u", "--env-file", "--restart", "--gpus", "--entrypoint",
                    "-m", "--memory", "--cpus", "-l", "--label", "--mount", "--add-host", "--platform", "--hostname", "-h",
                    "--user", "--workdir", "--publish", "--volume", "--env", "--shm-size", "--device", "--pull", "--log-driver",
                    "--net", "--ip", "--cap-add", "--security-opt", "--ulimit", "--runtime", "--pid", "--ipc", "--cpuset-cpus"}
BUILD_RX = re.compile(r"^(?:make|cmake|cargo build|go build|npm run build|pnpm (?:run )?build|yarn build|mvn|gradle|\./gradlew|"
                      r"npm install|npm i|npm ci|pnpm install|yarn install|yarn|pip install -r|pip3 install -r|pip install -e|"
                      r"pip3 install -e|pip install \.|uv sync|poetry install|bundle install|composer install)\b")


def _clean_pkg_token(tok):
    return tok.strip("\"'`,)(")


def _npm_pkg(tok):
    tok = _clean_pkg_token(tok)
    if not tok or tok.startswith((".", "/", "~", "-")) or ":" in tok or "$" in tok or "<" in tok or "[" in tok:
        return None
    m = re.match(r"^(@[^/@]+/[^/@]+|[^/@]+)(?:@.*)?$", tok)
    if not m:
        return None
    name = m.group(1)
    if not NPM_NAME.match(name) or name.lower() in PLACEHOLDER_PKG or "your" in name.lower() or "xxx" in name.lower() or name.endswith((".js", ".json", ".sh", ".md", ".py", ".ts")):
        return None
    return name


def _py_pkg(tok):
    tok = _clean_pkg_token(tok)
    if not tok or tok.startswith((".", "/", "~", "-")) or "://" in tok or tok.startswith("git+") or "$" in tok or "<" in tok:
        return None
    name = re.sub(r"\[.*?\]", "", tok)
    name = re.split(r"[=<>!~;@ ]", name)[0]
    if not name or not PY_NAME.match(name) or name.lower() in PLACEHOLDER_PKG or "your" in name.lower() or "xxx" in name.lower():
        return None
    if name.endswith((".txt", ".py", ".whl", ".zip", ".gz", ".toml", ".cfg", ".md")):
        return None
    return name


def _docker_image(tokens):
    i = 0
    while i < len(tokens):
        t = tokens[i]
        if t.startswith("-"):
            if "=" not in t and t in DOCKER_ARG_FLAGS:
                i += 2
            else:
                i += 1
            continue
        return t
    return None


def _split_image(img):
    img = _clean_pkg_token(img)
    if not img or "$" in img or "<" in img or "{" in img or img.startswith((".", "/")):
        return None
    img = img.split("@")[0]
    last = img.rsplit("/", 1)[-1]
    if ":" in last:
        img = img[:len(img) - len(last)] + last.split(":")[0]
    return img if re.match(r"^[A-Za-z0-9][A-Za-z0-9._/-]*$", img) else None


def parse_install_segment(seg):
    """Một đoạn lệnh -> dict {kind, reg, pkg, raw} hay None. kind: npx|npm|pip|uvx|pipx|docker|go|cargo|claude-mcp|clone|build."""
    seg = seg.strip()
    seg = re.sub(r"^\$\s+", "", seg)
    seg = re.sub(r"^(?:sudo|time|env)\s+", "", seg)
    seg = re.sub(r"^(?:[A-Z_][A-Z0-9_]*=\S*\s+)+", "", seg)
    if not seg:
        return None
    toks = seg.split()
    raw = redact(seg)[:110]
    t0 = toks[0]

    def mk(kind, reg=None, pkg=None):
        return {"kind": kind, "reg": reg, "pkg": pkg, "raw": raw}

    if t0 in ("npx", "bunx") or (t0 == "pnpm" and len(toks) > 1 and toks[1] == "dlx") or (t0 == "npm" and len(toks) > 1 and toks[1] == "exec"):
        rest = toks[1:]
        if t0 in ("pnpm", "npm") and rest:
            rest = rest[1:]
        i = 0
        while i < len(rest):
            t = rest[i]
            if t in ("-p", "--package") and i + 1 < len(rest):
                return mk("npx", "npm", _npm_pkg(rest[i + 1]))
            if t.startswith("--package="):
                return mk("npx", "npm", _npm_pkg(t.split("=", 1)[1]))
            if t.startswith("-"):
                i += 1
                continue
            return mk("npx", "npm", _npm_pkg(t))
        return None
    if t0 in ("npm", "pnpm", "yarn", "bun") and len(toks) > 1:
        sub = toks[1:]
        if t0 == "yarn" and sub[0] == "global" and len(sub) > 1:
            sub = sub[1:]
        if sub[0] in ("i", "install", "add", "global"):
            args = [t for t in sub[1:] if not t.startswith("-")]
            if not args:
                return mk("build") if sub[0] in ("i", "install") else None
            for a in args:
                p = _npm_pkg(a)
                if p:
                    return mk("npm", "npm", p)
            return mk("npm", "npm", None)
        if t0 in ("npm", "pnpm") and sub[0] == "run" and len(sub) > 1 and sub[1] == "build":
            return mk("build")
        return None
    # pip family
    pip_idx = None
    for k, t in enumerate(toks[:5]):
        if t in ("pip", "pip3") or (t == "-m" and k + 1 < len(toks) and toks[k + 1] == "pip"):
            pip_idx = k + 1 if t == "-m" else k
            break
    if pip_idx is not None and pip_idx + 1 < len(toks) and toks[pip_idx + 1] == "install":
        args, i = toks[pip_idx + 2:], 0
        while i < len(args):
            a = args[i]
            if a in PIP_ARG_FLAGS:
                if a in ("-r", "-e", "--requirement", "--editable") or a in ("-c", "--constraint"):
                    return mk("build")
                i += 2
                continue
            if a.startswith("-"):
                i += 1
                continue
            if a == ".":
                return mk("build")
            p = _py_pkg(a)
            if p:
                return mk("pip", "pypi", p)
            i += 1
        return mk("pip", "pypi", None)
    if t0 == "uv" and len(toks) > 2 and toks[1] == "tool" and toks[2] == "install":
        args = [t for t in toks[3:] if not t.startswith("-")]
        return mk("uvx", "pypi", _py_pkg(args[0]) if args else None)
    if t0 == "uv" and len(toks) > 1 and toks[1] in ("sync", "pip"):
        return mk("build") if toks[1] == "sync" else None
    if t0 == "uvx":
        rest = toks[1:]
        i = 0
        while i < len(rest):
            if rest[i] == "--from" and i + 1 < len(rest):
                return mk("uvx", "pypi", _py_pkg(rest[i + 1]))
            if rest[i].startswith("-"):
                i += 1
                continue
            return mk("uvx", "pypi", _py_pkg(rest[i]))
        return None
    if t0 == "pipx" and len(toks) > 2 and toks[1] in ("install", "run"):
        args = [t for t in toks[2:] if not t.startswith("-")]
        return mk("pipx", "pypi", _py_pkg(args[0]) if args else None)
    if t0 == "docker" and len(toks) > 1:
        if toks[1] in ("pull", "run"):
            img = _docker_image(toks[2:])
            img = _split_image(img) if img else None
            return mk("docker", "dockerhub", img)
        if toks[1] == "compose" or toks[1] == "build":
            return mk("docker", None, None)
        return None
    if t0 == "docker-compose":
        return mk("docker", None, None)
    if t0 == "go" and len(toks) > 2 and toks[1] == "install":
        mod = _clean_pkg_token(toks[2]).split("@")[0]
        if "." in mod.split("/")[0] and "<" not in mod and "$" not in mod and "..." not in mod and "xxx" not in mod:
            return mk("go", "go", mod)
        return mk("go", "go", None)
    if t0 == "cargo" and len(toks) > 2 and toks[1] == "install":
        args = [t for t in toks[2:] if not t.startswith("-")]
        name = _clean_pkg_token(args[0]) if args else None
        if name and re.match(r"^[A-Za-z0-9][A-Za-z0-9_-]*$", name) and name.lower() not in PLACEHOLDER_PKG:
            return mk("cargo", "crates", name)
        return mk("cargo", "crates", None)
    if t0 == "claude" and len(toks) > 2 and toks[1] in ("mcp", "plugin") and toks[2] in ("add", "install", "marketplace"):
        return mk("claude-mcp")
    if t0 == "git" and len(toks) > 1 and toks[1] == "clone":
        return mk("clone")
    if BUILD_RX.match(" ".join(toks[:3])) or BUILD_RX.match(seg):
        return mk("build")
    return None


LINE_STARTS_INSTALL = re.compile(r"^\s*(?:\$\s+)?(?:npx|bunx|npm|pnpm|yarn|pip3?|uvx|pipx|uv|docker|docker-compose|go install|cargo install|claude (?:mcp|plugin)|git clone)\b")
NEG_BEFORE_CMD = re.compile(r"(?:không|đừng|chớ|tránh|cấm|never|don'?t|do not|avoid|without)\b[^.\n]{0,35}$", re.I)
SHORTHAND_ADD = re.compile(r"\b(?:skills|plugin|plugins|marketplace)\s+add\s+(?:-\S+\s+)*([\w.-]+/[\w.-]+)", re.I)
BIN_LINE = re.compile(r"cần sẵn|requires?|yêu cầu|prerequisites?|điều kiện|\bbins?\b|phải có|cài sẵn", re.I)
BIN_WORDS = ("jq", "curl", "ffmpeg", "git", "node", "python3", "python", "docker", "gh", "make", "uv", "bun", "pnpm", "pandoc", "java", "cargo", "go")


def extract_required_bins(text):
    """Nhị phân mà entry nói là cần sẵn (dòng có từ khoá 'cần sẵn/requires/prerequisites')."""
    out = []
    for line in text.split("\n"):
        if len(line) < 400 and BIN_LINE.search(line):
            for b in BIN_WORDS:
                if re.search(r"(?<![\w/.-])" + re.escape(b) + r"(?![\w/.-])", line) and b not in out:
                    out.append("python" if b == "python3" else b)
    return list(dict.fromkeys(out))


JSON_CMD_RX = re.compile(r"\"command\"\s*:\s*\"([^\"]+)\"\s*,\s*\"args\"\s*:\s*\[([^\]]*)\]")
CURL_SH_RX = re.compile(r"(?:\b(?:curl|wget)\b[^|]*\|\s*(?:sudo\s+)?(?:ba)?sh\b)|(?:\b(?:irm|iwr|Invoke-RestMethod)\b.*\|\s*iex\b)", re.I)
SHELL_LANGS = {"", "bash", "sh", "shell", "zsh", "console", "terminal", "text", "txt", "cmd", "powershell", "ps1", "bat",
               "shell-session", "sh-session", "fish"}


def extract_installs(text):
    """Lệnh cài trong khối mã shell và code inline. Trả list dict (xem parse_install_segment), bỏ trùng."""
    prose, blocks = split_blocks(text)
    chunks = []
    for lang, code, _ in blocks:
        if lang in SHELL_LANGS:
            chunks.extend(code.split("\n"))
        else:  # khối ghi nhãn sai (vd ```python chứa `pip install`): chỉ lấy dòng BẮT ĐẦU bằng lệnh cài
            chunks.extend(x for x in code.split("\n") if LINE_STARTS_INSTALL.match(x))
    for m in re.finditer(r"`([^`\n]{4,200})`", prose):
        before = prose[max(0, m.start() - 45):m.start()]
        if NEG_BEFORE_CMD.search(before):
            continue  # "không pip install ...", "never run ..." không phải hướng dẫn cài
        chunks.append(m.group(1))
    out, seen = [], set()
    for lang, code, _ in blocks:
        for m in JSON_CMD_RX.finditer(code):
            args = re.findall(r"\"([^\"]*)\"", m.group(2))
            chunks.append(m.group(1) + " " + " ".join(args))
    for line in chunks:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if CURL_SH_RX.search(line):
            rec = {"kind": "curl-sh", "reg": None, "pkg": None, "raw": redact(line)[:110]}
            if rec not in out:
                out.append(rec)
            continue
        for seg in SEG_SPLIT.split(line):
            r = parse_install_segment(seg)
            if r:
                key = (r["kind"], r["reg"], r["pkg"], r["raw"])
                if key not in seen:
                    seen.add(key)
                    out.append(r)
    local = set(re.findall(r"docker\s+build\b[^\n]*?(?:-t|--tag)[ =]([\w./-]+)", text))
    local |= set(re.findall(r"docker\s+build\b[^\n]*?(?:-t|--tag)[ =]([\w./-]+):", text))
    if local:
        for r in out:
            if r["kind"] == "docker" and r["pkg"] and (r["pkg"] in local or r["pkg"].split("/")[-1] in local):
                r["pkg"] = None  # ảnh tự build tại chỗ
    return out


KEYNAME_RX = re.compile(r"\b([A-Z][A-Z0-9]{1,}(?:_[A-Z0-9]+)*_(?:API_KEY|API_TOKEN|ACCESS_TOKEN|SECRET_KEY|TOKEN|KEY))\b")


def extract_key_names(text):
    names = []
    for m in KEYNAME_RX.finditer(text):
        n = m.group(1)
        if n not in names and n not in ("PRIVATE_KEY", "API_KEY", "SECRET_KEY", "ACCESS_TOKEN", "SSH_KEY", "PUBLIC_KEY", "YOUR_API_KEY"):
            names.append(n)
    return names[:8]


# ===================================================================== kiểm tĩnh một mục
MOJIBAKE = re.compile(r"(?:Ã[\u0080-\u00bf]|Ä[\u0090\u2018\u2019]|áº|á»|â€|Ã¡|Ã©|Ã³|ðŸ|Â[\u00a0-\u00bf])")
WHEN_RX = re.compile(r"(when to (?:use|activate)|khi nào dùng|dùng khi|use (?:this )?(?:skill )?when|use when|trigger|kích hoạt|"
                     r"use (?:this )?(?:skill )?(?:for|to)|should be used|activate when|whenever|sử dụng khi|dùng (?:cho|để)|"
                     r"nên dùng|khi (?:người dùng|user|bạn)|when (?:the )?(?:user|you)|if (?:the )?user|helps? (?:you|with)|"
                     r"use cases?|tình huống|dùng skill)", re.I)
PATHREF_RX = re.compile(r"(?<![\w/.<{*-])((?:skills|repos|agents|mcps|stacks)/[A-Za-z0-9_./-]+?\.md)(?![\w/-])")
LINK_RX = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")


def mkr(ma, muc, mo_ta):
    return {"ma": ma, "muc": muc, "mo_ta": mo_ta}


def derive_id(path):
    return re.sub(r"\.md$", "", path).replace("/SKILL", "")


def code_checks(blocks):
    """Phân tích cú pháp tĩnh. Trả (stats, bash_jobs). stats[lang] = [kiem, loi]; bash_jobs = list code để bash -n sau."""
    stats = {"python": [0, 0], "json": [0, 0], "yaml": [0, 0], "bash": [0, 0]}
    bash_jobs = []
    for lang, code, _ in blocks:
        body = code
        ph = re.search(r"<[A-Za-z_ -]{2,30}>|^\s*\.\.\.\s*$|\u2026", body, re.M)
        if lang in ("python", "py", "python3"):
            if ph and not re.search(r"^\s*\.\.\.\s*$", body, re.M):
                pass
            if re.search(r"<[A-Za-z_ -]{2,30}>", body) or re.search(r"^\s*\.\.\.\s*$", body, re.M) or "\u2026" in body:
                continue
            body = re.sub(r"^(?:>>>|\.\.\.) ?", "", body, flags=re.M) if re.search(r"^>>> ", body, re.M) else body
            stats["python"][0] += 1
            try:
                ast.parse(body)
            except (SyntaxError, ValueError, RecursionError, MemoryError):
                stats["python"][1] += 1
        elif lang in ("json", "jsonc", "json5"):
            if "//" in re.sub(r"\"[^\"\n]*\"", "", body) or "/*" in body or "..." in body or "\u2026" in body or lang != "json":
                continue
            if re.search(r"^\s*<", body, re.M):
                continue
            stats["json"][0] += 1
            try:
                json.loads(body)
            except ValueError:
                stats["json"][1] += 1
        elif lang in ("yaml", "yml"):
            if _yaml is None or "..." in body or "\u2026" in body or re.search(r"<[A-Za-z_ -]{2,30}>", body):
                continue
            stats["yaml"][0] += 1
            try:
                list(_yaml.safe_load_all(body))
            except Exception:
                stats["yaml"][1] += 1
        elif lang in ("bash", "sh", "shell", "zsh"):
            if ph or re.search(r"\.\.\.", body):
                continue
            nocomment = "\n".join(x for x in body.split("\n") if not x.lstrip().startswith("#")).strip()
            if nocomment.startswith(("{", "[", "\"")):
                continue  # khối ghi nhãn bash nhưng thực chất là JSON cấu hình
            body = re.sub(r"^\s*\$ ", "", body, flags=re.M)
            bash_jobs.append(body)
            stats["bash"][0] += 1
    return stats, bash_jobs


def run_bash_syntax(jobs):
    """jobs: list[(key, code)] -> set key lỗi. Chỉ `bash -n` (không thực thi)."""
    bad = set()
    bash = shutil.which("bash")
    if not bash or not jobs:
        return bad, bool(bash)
    with tempfile.TemporaryDirectory(prefix="auditsh_") as td:
        names = {}
        for n, (key, code) in enumerate(jobs):
            fn = f"b{n:06d}.sh"
            names[fn] = key
            with open(os.path.join(td, fn), "w", encoding="utf-8", newline="\n") as fh:
                fh.write(code + "\n")
        script = 'for f in b*.sh; do bash -n "$f" >/dev/null 2>&1 || echo "$f"; done'
        try:
            r = subprocess.run([bash, "-c", script], cwd=td, capture_output=True, text=True, timeout=1200)
            for line in r.stdout.split("\n"):
                line = line.strip()
                if line in names:
                    bad.add(names[line])
        except Exception:
            return bad, False
    return bad, True


def static_check(item, root, id_count, path_count):
    """Tầng 0 cho một mục. Trả dict S (không có mạng)."""
    rid, kind, rel = item["id"], item["loai"], item.get("duong_dan", "")
    S = {"reasons": [], "text": None, "blocks": [], "bash_jobs": [], "code": {}, "installs": [], "gh": [], "gh_total": 0,
         "key_names": [], "nolines": 0, "install_repos": [], "bins": []}
    R = S["reasons"]
    if id_count.get(rid, 0) > 1:
        R.append(mkr("ID_TRUNG", "hong", f"id '{rid}' xuất hiện {id_count[rid]} lần trong catalog"))
    if path_count.get(rel, 0) > 1:
        R.append(mkr("DUONG_DAN_TRUNG", "hong", f"duong_dan '{rel}' bị {path_count[rel]} mục dùng chung"))
    if derive_id(rel) != rid:
        R.append(mkr("ID_LECH_DUONG_DAN", "hong", f"id '{rid}' không khớp duong_dan '{rel}'"))
    full = os.path.join(root, rel) if rel else ""
    if not rel or not os.path.isfile(full):
        R.append(mkr("FILE_THIEU", "hong", f"file '{rel}' không tồn tại"))
        return S
    text, err = read_text(full)
    if err == "decode":
        R.append(mkr("FILE_KHONG_UTF8", "hong", "file không giải mã được UTF-8"))
    if text is None or len(text.strip()) < 80:
        R.append(mkr("FILE_RONG", "hong", f"file rỗng hay quá ngắn ({len((text or '').strip())} ký tự)"))
        return S
    S["text"] = text
    if len(text.strip()) < 300:
        R.append(mkr("FILE_NGAN", "nhe", f"file chỉ {len(text.strip())} ký tự, rất ít thông tin"))
    moj = len(MOJIBAKE.findall(text))
    repl = text.count("\ufffd")
    if moj >= 3 or repl >= 3:
        R.append(mkr("MA_HOA_LOI", "nghi", f"nghi lỗi mã hoá chữ (mojibake {moj}, ký tự thay thế {repl})"))

    prose, blocks = split_blocks(text)
    S["blocks"] = blocks
    fm_raw, body = parse_frontmatter(text)
    is_skill = kind.startswith("skill")
    if is_skill:
        if fm_raw is None:
            R.append(mkr("FM_THIEU", "nhe", "skill không có frontmatter"))
        else:
            if not re.search(r"^name:\s*\S", fm_raw, re.M):
                R.append(mkr("FM_THIEU_NAME", "nhe", "frontmatter thiếu name"))
            if not re.search(r"^description:\s*(\S|[>|])", fm_raw, re.M):
                R.append(mkr("FM_THIEU_DESC", "nhe", "frontmatter thiếu description"))
            if _yaml is not None:
                try:
                    _yaml.safe_load(fm_raw)
                except Exception:
                    R.append(mkr("FM_YAML_LOI", "nhe", "frontmatter không parse được YAML"))
        desc = ""
        if fm_raw:
            m = re.search(r"^description:\s*(.*(?:\n[ \t]+.*)*)", fm_raw, re.M)
            desc = m.group(1) if m else ""
        if not WHEN_RX.search(desc + "\n" + body[:6000]):
            R.append(mkr("SKILL_THIEU_KHI_NAO_DUNG", "nhe", "skill không có phần mô tả khi nào dùng"))

    for name, ln in scan_secrets(text):
        R.append(mkr("LO_KHOA", "hong", f"nghi lộ khoá bí mật loại {name} tại dòng {ln} [REDACTED]"))

    # link tương đối
    base = os.path.dirname(full)
    broken = []
    for m in LINK_RX.finditer(prose):
        tg = m.group(1)
        if re.match(r"^(?:[a-z][a-z0-9+.-]*:|#|/|\$|\{|<)", tg, re.I) or any(c in tg for c in "*{}$<>|"):
            continue
        tg2 = urllib.parse.unquote(tg.split("#")[0].split("?")[0])
        if not tg2:
            continue
        if not os.path.exists(os.path.normpath(os.path.join(base, tg2))):
            broken.append(tg)
    if broken:
        muc = "nghi" if len(set(broken)) >= 5 else "nhe"
        R.append(mkr("LINK_TUONG_DOI_HONG", muc, f"{len(set(broken))} link tương đối trỏ file không tồn tại (vd {broken[0][:60]})"))
    brefs = []
    for m in PATHREF_RX.finditer(text):
        p = m.group(1)
        if any(x in p.lower() for x in ("xxx", "yyy", "your", "example", "<", "tên")):
            continue
        if os.path.exists(os.path.join(root, p)) or os.path.exists(os.path.normpath(os.path.join(base, p))):
            continue
        if p not in brefs:
            brefs.append(p)
    if brefs:
        R.append(mkr("DUONG_DAN_NHAC_HONG", "nhe", f"{len(brefs)} đường dẫn kho được nhắc nhưng không tồn tại (vd {brefs[0]})"))

    # khối mã
    stats, bash_jobs = code_checks(blocks)
    S["code"], S["bash_jobs"] = stats, bash_jobs
    S["installs"] = extract_installs(text)
    gh = extract_github(text)
    S["gh_total"] = len(gh)
    inst_repos = []
    for ins in S["installs"]:
        found = extract_github(ins["raw"])
        m = SHORTHAND_ADD.search(ins["raw"])
        if m and m.group(1).split("/")[0].lower() not in GH_BAD_OWNER:
            found.append(m.group(1))
        for g in found:
            if g.lower() not in [x.lower() for x in inst_repos]:
                inst_repos.append(g)
    S["install_repos"] = inst_repos
    S["gh"] = list(dict.fromkeys(inst_repos[:3] + gh))[:4 + min(2, len(inst_repos))]
    S["bins"] = extract_required_bins(text)
    S["key_names"] = extract_key_names(text)
    return S


def finish_code_reasons(S, bash_bad_count):
    """Gọi sau khi biết số khối bash lỗi."""
    st = S["code"]
    st["bash"][1] = bash_bad_count
    labels = {"python": "CODE_PY_LOI", "json": "CODE_JSON_LOI", "yaml": "CODE_YAML_LOI", "bash": "CODE_SH_LOI"}
    bad_tot = chk_tot = 0
    for lang, (chk, bad) in st.items():
        chk_tot += chk
        bad_tot += bad
        if bad:
            S["reasons"].append(mkr(labels[lang], "nhe", f"{bad}/{chk} khối {lang} lỗi cú pháp (nhiều khối là mã minh hoạ)"))
    if bad_tot >= 5 and chk_tot and bad_tot / chk_tot >= 0.5:
        S["reasons"].append(mkr("CODE_NHIEU_KHOI_LOI", "nghi", f"{bad_tot}/{chk_tot} khối mã lỗi cú pháp, quá nhiều"))


# ===================================================================== nhãn mâu thuẫn
def _evidence(text, rx):
    """Đoạn ngắn quanh chỗ khớp đầu tiên (đã che khoá)."""
    m = re.search(rx, text, re.I)
    if not m:
        return ""
    a, b = max(0, m.start() - 50), min(len(text), m.end() + 50)
    return redact(re.sub(r"\s+", " ", text[a:b]).strip())


NEG_PHRASE = re.compile(r"(không|khỏi|no|without|chẳng)\s+(cần|need|requires?|yêu cầu)?\s*(docker|gpu|cuda|api[ -]?key|vps|trả phí)", re.I)


def label_conflicts(item, S):
    """Trả list reason cho mâu thuẫn nhãn <-> entry. Chỉ cho mục đã gắn nhãn."""
    out = []
    if item.get("curation_status", "chua-gan-nhan") == "chua-gan-nhan" or S["text"] is None:
        return out
    text = S["text"]
    needs = {n for n in (item.get("needs") or "").split(",") if n and n != "unknown"}
    low = text.lower()
    adoption = item.get("adoption", "")

    def add(ma, claim, ev):
        out.append(mkr(ma, "nghi", f"nhãn {claim}; căn cứ: {ev}"))

    if "docker" in needs and not re.search(r"docker|container|compose|podman", low):
        add("NHAN_MAU_THUAN_DOCKER", "needs=docker", "entry không hề nhắc docker/container")
    if "gpu" in needs and not re.search(r"\bgpu\b|cuda|vram|nvidia|metal|apple silicon|mps\b|rocm", low):
        add("NHAN_MAU_THUAN_GPU", "needs=gpu", "entry không nhắc GPU/CUDA/VRAM")
    if "api-key" in needs and not re.search(r"api[ _-]?key|token|secret|bearer|oauth|đăng nhập|login|credential|\.env|_key\b|khoá|khóa|key\b", low):
        add("NHAN_MAU_THUAN_APIKEY", "needs=api-key", "entry không nhắc khoá/token/đăng nhập")
    if "tra-phi" in needs and not re.search(r"trả phí|paid|\$\s?\d|credit|subscription|pricing|giá|phí|price|plan|billing|premium|enterprise|cost|chi phí|miễn phí|free", low):
        add("NHAN_MAU_THUAN_TRAPHI", "needs=tra-phi", "entry không nhắc phí/giá/credit")
    if "vps" in needs and not re.search(r"vps|server|máy chủ|self-host|deploy|ssh|systemd|24/7|cloud|hosting|daemon|service", low):
        add("NHAN_MAU_THUAN_VPS", "needs=vps", "entry không nhắc VPS/máy chủ/deploy")
    if not needs or needs == {"none"}:
        ev = _evidence(text, r"(cần|yêu cầu|bắt buộc|requires?|need(?:s|ed)?)\s+(?:một\s+|an?\s+|the\s+)?(?:api[ -]?key|khoá api|khóa api|openai key|anthropic key)")
        if ev and not NEG_PHRASE.search(ev):
            add("NHAN_MAU_THUAN_APIKEY2", f"needs={','.join(sorted(needs)) or 'rỗng'}", f"entry ghi “{ev}”")
        ev = _evidence(text, r"(cần|yêu cầu|bắt buộc|requires?|need(?:s|ed)?)\s+(?:một\s+|an?\s+)?(?:nvidia\s+)?(?:gpu|cuda)")
        if ev and not NEG_PHRASE.search(ev) and not re.search(r"\bcpu\b|optional|tuỳ chọn|tùy chọn|không bắt buộc", ev, re.I):
            add("NHAN_MAU_THUAN_GPU2", f"needs={','.join(sorted(needs)) or 'rỗng'}", f"entry ghi “{ev}”")
        routes = [i for i in S["installs"] if i["kind"] in ("npx", "npm", "pip", "uvx", "pipx", "docker", "go", "cargo", "claude-mcp", "clone", "build")]
        if routes and all(i["kind"] == "docker" for i in routes):
            add("NHAN_MAU_THUAN_DOCKER2", f"needs={','.join(sorted(needs)) or 'rỗng'}", f"mọi lệnh cài trong entry đều qua docker, vd “{routes[0]['raw']}”")
    if adoption == "cai-ngay-duoc" and needs & {"vps", "gpu"}:
        out.append(mkr("NHAN_NOI_BO_ADOPTION", "nhe", f"adoption=cai-ngay-duoc nhưng needs={','.join(sorted(needs))} (cần hạ tầng)"))
    if adoption == "can-ha-tang" and (not needs or needs <= {"none", "claude-code-only", "browser"}):
        out.append(mkr("NHAN_NOI_BO_ADOPTION", "nhe", f"adoption=can-ha-tang nhưng needs={','.join(sorted(needs)) or 'rỗng'} (không cần gì thêm)"))
    return out


# ===================================================================== mạng chỉ-đọc
class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):
        return None


_OPEN_NR = urllib.request.build_opener(NoRedirect)
_OPEN_FOLLOW = urllib.request.build_opener()


class Net:
    HOST_GAP = {"github.com": 0.35, "registry.npmjs.org": 0.15, "pypi.org": 0.15, "hub.docker.com": 0.4,
                "crates.io": 1.0, "proxy.golang.org": 0.2}

    def __init__(self, workers=4, timeout=10, cache_path=None, offline=False, log=None):
        self.workers = min(4, max(1, workers))
        self.timeout = timeout
        self.offline = offline
        self.cache_path = cache_path
        self.cache = {}
        self.log = log or (lambda *_: None)
        self.lock = threading.Lock()
        self.host_last = defaultdict(float)
        self.host_block = {}
        self.host_429 = Counter()
        if cache_path and os.path.exists(cache_path):
            try:
                self.cache = json.load(open(cache_path, encoding="utf-8"))
            except Exception:
                self.cache = {}

    # ----- một request lịch sự
    def _wait_host(self, host):
        gap = self.HOST_GAP.get(host, 0.2)
        with self.lock:
            now = time.time()
            until = self.host_block.get(host, 0)
            if now < until:
                return False
            t = max(now, self.host_last[host] + gap)
            self.host_last[host] = t
        d = t - time.time()
        if d > 0:
            time.sleep(d)
        return True

    def request(self, url, method="GET", headers=None, follow=False, max_bytes=3_000_000):
        host = urllib.parse.urlsplit(url).netloc
        if not self._wait_host(host):
            return {"code": None, "err": "cooldown", "body": b""}
        h = {"User-Agent": UA, "Accept": "*/*"}
        h.update(headers or {})
        req = urllib.request.Request(url, headers=h, method=method)
        opener = _OPEN_FOLLOW if follow else _OPEN_NR
        try:
            with opener.open(req, timeout=self.timeout) as r:
                body = r.read(max_bytes) if method == "GET" else b""
                return {"code": r.status, "err": None, "body": body}
        except urllib.error.HTTPError as e:
            if e.code == 429:
                ra = e.headers.get("Retry-After", "")
                wait = int(ra) if ra.isdigit() else 60
                with self.lock:
                    self.host_429[host] += 1
                    self.host_block[host] = time.time() + min(wait, 90)
            return {"code": e.code, "err": None, "body": b""}
        except Exception as e:  # timeout, DNS, SSL...
            return {"code": None, "err": type(e).__name__, "body": b""}

    # ----- từng loại
    def _gh(self, repo):
        r = self.request(f"https://github.com/{repo}", method="HEAD")
        c = r["code"]
        if c in (200, 301, 302, 307, 308):
            return {"ok": True, "code": c}
        if c in (404, 410):
            return {"ok": False, "code": c}
        return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}

    def _npm(self, name):
        enc = name.replace("/", "%2F")
        r = self.request(f"https://registry.npmjs.org/{enc}", headers={"Accept": "application/vnd.npm.install-v1+json"}, follow=True, max_bytes=8_000_000)
        c = r["code"]
        if c == 200:
            ver = upd = None
            try:
                j = json.loads(r["body"].decode("utf-8", "replace"))
                ver = (j.get("dist-tags") or {}).get("latest")
                upd = (j.get("modified") or "")[:10] or None
            except Exception:
                m = re.search(rb'"latest":"([^"]+)"', r["body"])
                ver = m.group(1).decode() if m else None
            return {"ok": True, "code": 200, "version": ver, "updated": upd}
        if c in (404, 410):
            return {"ok": False, "code": c}
        return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}

    def _pypi(self, name):
        r = self.request(f"https://pypi.org/pypi/{urllib.parse.quote(name)}/json", follow=True, max_bytes=8_000_000)
        c = r["code"]
        if c == 200:
            try:
                j = json.loads(r["body"].decode("utf-8", "replace"))
                ver = (j.get("info") or {}).get("version")
                upd = None
                urls = j.get("urls") or []
                if urls:
                    upd = (urls[0].get("upload_time_iso_8601") or urls[0].get("upload_time") or "")[:10] or None
                return {"ok": True, "code": 200, "version": ver, "updated": upd}
            except Exception:
                return {"ok": True, "code": 200}
        if c in (404, 410):
            return {"ok": False, "code": c}
        return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}

    def _docker(self, image):
        parts = image.split("/")
        if len(parts) == 1:
            ns, nm = "library", parts[0]
        elif len(parts) == 2 and "." not in parts[0] and ":" not in parts[0]:
            ns, nm = parts
        else:
            return {"ok": None, "code": None, "err": "registry-khac"}
        r = self.request(f"https://hub.docker.com/v2/repositories/{ns}/{nm}/", follow=True)
        c = r["code"]
        if c == 200:
            try:
                j = json.loads(r["body"].decode("utf-8", "replace"))
                return {"ok": True, "code": 200, "updated": (j.get("last_updated") or "")[:10] or None}
            except Exception:
                return {"ok": True, "code": 200}
        if c in (404, 410):
            return {"ok": False, "code": c}
        return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}

    def _crates(self, name):
        r = self.request(f"https://crates.io/api/v1/crates/{urllib.parse.quote(name)}", follow=True)
        c = r["code"]
        if c == 200:
            try:
                j = json.loads(r["body"].decode("utf-8", "replace"))
                cr = j.get("crate") or {}
                return {"ok": True, "code": 200, "version": cr.get("max_version"), "updated": (cr.get("updated_at") or "")[:10] or None}
            except Exception:
                return {"ok": True, "code": 200}
        if c in (404, 410):
            return {"ok": False, "code": c}
        return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}

    def _go(self, mod):
        segs = mod.split("/")
        cands = [mod]
        for _ in range(2):
            if len(segs) > 3:
                segs = segs[:-1]
                cands.append("/".join(segs))
        last = None
        for cand in dict.fromkeys(cands):
            esc = re.sub(r"[A-Z]", lambda m: "!" + m.group(0).lower(), cand)
            r = self.request(f"https://proxy.golang.org/{esc}/@latest", follow=True)
            c = r["code"]
            if c == 200:
                try:
                    j = json.loads(r["body"].decode("utf-8", "replace"))
                    return {"ok": True, "code": 200, "version": j.get("Version"), "updated": (j.get("Time") or "")[:10] or None}
                except Exception:
                    return {"ok": True, "code": 200}
            last = r
            if c not in (404, 410):
                return {"ok": None, "code": c, "err": r["err"] or f"http{c}"}
        return {"ok": False, "code": last["code"] if last else 404}

    def lookup(self, reg, name):
        key = f"{reg}:{name.lower() if reg != 'go' else name}"
        if key in self.cache:
            return self.cache[key]
        fn = {"gh": self._gh, "npm": self._npm, "pypi": self._pypi, "dockerhub": self._docker, "crates": self._crates, "go": self._go}[reg]
        res = fn(name)
        if res.get("ok") is not None:
            with self.lock:
                self.cache[key] = res
        return res

    def prefetch(self, keys, progress_every=100):
        """keys: iterable (reg, name). Trả dict key_str -> kết quả. Offline: không gọi gì."""
        keys = list(dict.fromkeys(keys))
        results = {}
        if self.offline:
            return results

        def one(k):
            return k, self.lookup(*k)
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=self.workers) as ex:
            for n, (k, res) in enumerate(ex.map(one, keys), 1):
                results[f"{k[0]}:{k[1].lower() if k[0] != 'go' else k[1]}"] = res
                if n % progress_every == 0:
                    self.log(f"  mạng {n}/{len(keys)} ({time.time()-t0:.0f}s)")
        # lượt 2: thử lại tuần tự các mục chưa xác định, sau khi hết thời gian chờ 429
        unk = [k for k in keys if results.get(f"{k[0]}:{k[1].lower() if k[0] != 'go' else k[1]}", {}).get("ok") is None]
        if unk:
            self.log(f"  lượt 2: {len(unk)} mục chưa xác định, chờ rồi thử lại tuần tự")
            now = time.time()
            wait = max([self.host_block.get(h, 0) - now for h in self.host_block] + [0])
            if wait > 0:
                time.sleep(min(wait + 1, 95))
            for k in unk:
                host = {"gh": "github.com", "npm": "registry.npmjs.org", "pypi": "pypi.org", "dockerhub": "hub.docker.com",
                        "crates": "crates.io", "go": "proxy.golang.org"}[k[0]]
                if self.host_429[host] >= 6 and time.time() < self.host_block.get(host, 0):
                    continue  # đã bị 429 nhiều lần: không dồn
                res = self.lookup(*k)
                results[f"{k[0]}:{k[1].lower() if k[0] != 'go' else k[1]}"] = res
                time.sleep(0.8)
        return results

    def save_cache(self):
        if self.cache_path:
            os.makedirs(os.path.dirname(os.path.abspath(self.cache_path)), exist_ok=True)
            with open(self.cache_path, "w", encoding="utf-8") as fh:
                json.dump(self.cache, fh, ensure_ascii=False)


def netkey(reg, name):
    return f"{reg}:{name.lower() if reg != 'go' else name}"


# ===================================================================== hồ sơ máy
ENV_KEYS = ["ANTHROPIC_API_KEY", "OPENAI_API_KEY", "GEMINI_API_KEY", "GOOGLE_API_KEY", "GOOGLE_GENERATIVE_AI_API_KEY",
            "ELEVENLABS_API_KEY", "FIRECRAWL_API_KEY", "GITHUB_TOKEN", "GH_TOKEN", "HF_TOKEN", "HUGGINGFACE_API_KEY",
            "REPLICATE_API_TOKEN", "FAL_KEY", "OPENROUTER_API_KEY", "DEEPSEEK_API_KEY", "GROQ_API_KEY", "TAVILY_API_KEY",
            "BRAVE_API_KEY", "SERPAPI_API_KEY", "PERPLEXITY_API_KEY", "NOTION_API_KEY", "SLACK_BOT_TOKEN", "STRIPE_API_KEY",
            "SUPABASE_KEY", "VERCEL_TOKEN", "CLOUDFLARE_API_TOKEN", "APIFY_TOKEN", "EXA_API_KEY"]
TOOLS = ["git", "node", "npm", "npx", "python", "pip", "docker", "ffmpeg", "gh", "bash", "uv", "uvx", "pipx", "go", "cargo",
         "make", "cmake", "claude", "nvidia-smi", "jq", "curl", "bun", "pnpm", "pandoc", "java"]


def machine_profile(run_versions=True):
    prof = {"he_dieu_hanh": sys.platform, "python_dang_chay": sys.version.split()[0], "cong_cu": {}, "khoa_env": {}}
    for t in TOOLS:
        p = shutil.which(t)
        info = {"co": bool(p)}
        if p and run_versions:
            args = [p, "-L"] if t == "nvidia-smi" else [p, "--version"]
            try:
                r = subprocess.run(args, capture_output=True, text=True, timeout=8)
                out = (r.stdout or r.stderr or "").strip().split("\n")[0][:80]
                info["phien_ban"] = out
            except Exception:
                info["phien_ban"] = "(không đọc được)"
        prof["cong_cu"][t] = info
    p = shutil.which("docker")
    prof["docker_daemon_tra_loi"] = None
    if p and run_versions:
        try:
            r = subprocess.run([p, "version", "--format", "{{.Server.Version}}"], capture_output=True, text=True, timeout=8)
            prof["docker_daemon_tra_loi"] = r.returncode == 0 and bool(r.stdout.strip())
        except Exception:
            prof["docker_daemon_tra_loi"] = False
    prof["co_gpu_nvidia"] = prof["cong_cu"].get("nvidia-smi", {}).get("co", False)
    prof["co_trinh_duyet"] = bool(shutil.which("chrome") or shutil.which("msedge") or shutil.which("firefox")
                                  or os.path.exists(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
                                  or os.path.exists(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"))
    prof["la_vps"] = False
    prof["claude_code"] = bool(shutil.which("claude")) or ("CLAUDECODE" in os.environ) or ("CLAUDE_CODE_ENTRYPOINT" in os.environ)
    for k in ENV_KEYS:
        prof["khoa_env"][k] = k in os.environ  # chỉ có/không, KHÔNG ghi giá trị
    return prof


# ===================================================================== phân loại
TOOL_FOR_KIND = {"curl-sh": "bash", "npx": "npx", "npm": "npm", "pip": "pip", "uvx": "uvx", "pipx": "pipx", "docker": "docker", "go": "go",
                 "cargo": "cargo", "claude-mcp": None, "clone": "git", "build": None}
PURE_CAPS = {"reference", "prompt-skill-library"}


def relevant_installs(item, S):
    """Với skill: lệnh trong thân skill phần lớn là ví dụ về thứ khác (prisma, playwright...), không phải cách cài skill.
    Chỉ giữ lệnh nhắm đúng mục này (nhắc tên/slug/repo của nó) hay lệnh kiểu `skills add`, `claude mcp add`, `plugin install`."""
    ins = S["installs"]
    if not item["loai"].startswith("skill"):
        return ins
    base = re.sub(r"[^a-z0-9]", "", item["id"].split("/")[-1].lower())
    own = {base}
    for g in list(S.get("install_repos", [])) + S["gh"][:1]:
        own.add(re.sub(r"[^a-z0-9]", "", g.split("/")[-1].lower()))
    own = {o for o in own if len(o) >= 4}
    out = []
    for i in ins:
        raw = re.sub(r"[^a-z0-9]", "", i["raw"].lower())
        pk = re.sub(r"[^a-z0-9]", "", (i["pkg"] or "").split("/")[-1].lower())
        if (any(o in raw for o in own) or (len(pk) >= 4 and any(pk in o or o in pk for o in own))
                or SHORTHAND_ADD.search(i["raw"]) or re.search(r"(mcp|plugin)\s+(add|install|marketplace)", i["raw"])):
            out.append(i)
    return out


def classify(item, S, lookup, machine, offline=False):
    """Trả (usable, reasons, extra). lookup: dict netkey -> kết quả. Thuần hàm, dùng được trong test."""
    R = list(S["reasons"])
    extra = {"cach_cai": [], "thieu": [], "github": [], "goi": []}
    kind = item["loai"]
    labeled = item.get("curation_status", "chua-gan-nhan") != "chua-gan-nhan"
    R.extend(label_conflicts(item, S))

    # --- mạng
    unknown_net = False
    ghs = S["gh"]
    for n, repo in enumerate(ghs):
        res = lookup.get(netkey("gh", repo)) if not offline else None
        st = "chua-kiem" if res is None else ("song" if res["ok"] else ("chet" if res["ok"] is False else "chua-xac-dinh"))
        extra["github"].append({"repo": repo, "trang_thai": st, "ma_http": (res or {}).get("code")})
        if st == "chet":
            if n == 0:
                R.append(mkr("GH_LINK_CHET", "nghi", f"repo GitHub chính {repo} trả 404 (link chết/đổi tên/riêng tư)"))
            else:
                R.append(mkr("GH_LINK_CHET_PHU", "nhe", f"repo GitHub phụ {repo} trả 404"))
        elif st == "chua-xac-dinh" and n == 0:
            unknown_net = True
    pk_missing = []
    pk_seen = set()
    insts = relevant_installs(item, S)
    for ins in insts:
        if not ins["pkg"] or not ins["reg"]:
            continue
        key = netkey(ins["reg"], ins["pkg"])
        if key in pk_seen:
            continue
        pk_seen.add(key)
        res = lookup.get(key) if not offline else None
        rec = {"reg": ins["reg"], "ten": ins["pkg"]}
        if res is None:
            rec["ton_tai"] = "chua-kiem"
        elif res["ok"] is True:
            rec.update(ton_tai=True, phien_ban=res.get("version"), cap_nhat=res.get("updated"))
        elif res["ok"] is False:
            rec["ton_tai"] = False
            pk_missing.append(ins["pkg"])
        else:
            rec["ton_tai"] = "chua-xac-dinh"
            unknown_net = True
        extra["goi"].append(rec)
    if pk_missing:
        base = re.sub(r"[^a-z0-9]", "", item["id"].split("/")[-1].lower())
        ok_match = False
        for rec in extra["goi"]:
            if rec.get("ton_tai") is True:
                nm = re.sub(r"[^a-z0-9]", "", rec["ten"].split("/")[-1].lower())
                if nm and base and (nm in base or base in nm):
                    ok_match = True
        names = ", ".join(dict.fromkeys(pk_missing[:4]))
        if ok_match:
            R.append(mkr("GOI_PHU_KHONG_TIM_THAY", "nhe", f"gói phụ không có trên registry: {names} (entry còn lệnh cài khác có gói tồn tại)"))
        else:
            R.append(mkr("GOI_KHONG_TIM_THAY", "nghi", f"gói cài không có trên registry: {names}"))

    codes = {r["muc"] for r in R}
    if "hong" in codes:
        return "hong", R, extra
    if "nghi" in codes:
        return "nghi-ngo", R, extra

    # --- cách cài + điều kiện
    routes = list(insts)
    kinds = {i["kind"] for i in routes}
    cach = []
    needs = {n for n in (item.get("needs") or "").split(",") if n and n != "unknown"}
    if kind.startswith("skill") and not (kinds - {"clone"}):
        cach.append("chep-file/prompt-thuan")
    for k in sorted(kinds):
        cach.append({"npx": "npx-mot-lenh", "npm": "npm", "pip": "pip", "uvx": "uvx-mot-lenh", "pipx": "pipx", "docker": "can-docker",
                     "go": "go-install", "cargo": "cargo-install", "claude-mcp": "claude-mcp-add", "clone": "tai-ma-nguon", "curl-sh": "curl-pipe-sh",
                     "build": "can-build"}[k])
    thieu = []
    hints = set()
    if labeled:
        req = set(needs)
    else:
        req = set()
        text = S["text"] or ""
        route_kinds = [i["kind"] for i in routes]
        if route_kinds and all(k == "docker" for k in route_kinds):
            req.add("docker")
        if re.search(r"(cần|yêu cầu|bắt buộc|requires?|need(?:s|ed)?)\s+(?:một\s+|an?\s+)?(?:nvidia\s+)?(?:gpu|cuda)", text, re.I):
            hints.add("gpu")
        if S["key_names"]:
            hints.add("api-key")
        fm_desc = re.search(r"^description:\s*(.*(?:\n[ \t]+.*)*)", text.split("\n---", 2)[0], re.M) if text.startswith("---") else None
        if fm_desc and re.search(r"\b(?:via|using|through|requires?|connected)\b[^.\n]{0,40}\b(?:MCP|tools?)\b", fm_desc.group(1), re.I) and kind.startswith("skill"):
            hints.add("mcp-ngoai")
        if re.search(r"(cần|yêu cầu|requires?)\s+(?:một\s+)?vps\b|chạy trên vps|deploy lên vps", text, re.I):
            hints.add("vps")
        if re.search(r"trả phí|paid plan|subscription required|\bcredits?\b.*(required|bắt buộc)", text, re.I):
            hints.add("tra-phi")
    tools = machine.get("cong_cu", {})
    for i in routes:
        tool = TOOL_FOR_KIND.get(i["kind"])
        if i["kind"] == "build":
            m = re.match(r"(\S+)", i["raw"])
            first = m.group(1) if m else ""
            tool = {"make": "make", "cmake": "cmake", "cargo": "cargo", "go": "go", "npm": "npm", "pnpm": "npm", "yarn": "npm",
                    "pip": "pip", "pip3": "pip", "uv": "uv", "mvn": "make", "gradle": "make"}.get(first)
        if tool and not tools.get(tool, {}).get("co") and tool not in thieu:
            if tool == "pip" and tools.get("python", {}).get("co"):
                continue
            thieu.append(tool)
    for b in S.get("bins", []):
        if not tools.get(b, {}).get("co") and b not in thieu:
            thieu.append(b)
    if "docker" in req and not tools.get("docker", {}).get("co"):
        thieu.append("docker")
    if "gpu" in req and not machine.get("co_gpu_nvidia"):
        thieu.append("gpu")
    if "vps" in req and not machine.get("la_vps"):
        thieu.append("vps")
    if "tra-phi" in req:
        thieu.append("tra-phi")
    if "browser" in req and not machine.get("co_trinh_duyet"):
        thieu.append("browser")
    if "api-key" in req:
        names = S["key_names"]
        env = machine.get("khoa_env", {})
        if not names or not all(os.environ.get(n) is not None if n not in env else env[n] for n in names):
            thieu.append("api-key" + (f"({','.join(names[:3])})" if names else ""))
    if "claude-code-only" in req and not machine.get("claude_code"):
        thieu.append("claude-code")
    if "claude-mcp" in kinds and not machine.get("claude_code"):
        thieu.append("claude-code")
    if "docker" in kinds and not any(k in kinds for k in ("npx", "npm", "pip", "uvx", "pipx", "go", "cargo", "claude-mcp")) and "docker" not in req:
        req.add("docker")
        if not tools.get("docker", {}).get("co"):
            thieu.append("docker")
    extra["cach_cai"] = cach + sorted(f"can-{r}" for r in req if r in ("vps", "gpu", "api-key", "tra-phi", "docker", "browser") and f"can-{r}" not in cach)
    thieu = list(dict.fromkeys(thieu))
    extra["thieu"] = thieu
    if "curl-sh" in kinds:
        R.append(mkr("CAI_CURL_PIPE_SH", "nhe", "cài bằng curl|sh (tải script rồi chạy): đọc script trước khi chạy"))
    for t in thieu:
        R.append(mkr("THIEU_" + re.sub(r"[^A-Za-z0-9]+", "_", t.split("(")[0]).strip("_").upper(), "thieu", f"máy này thiếu/không đáp ứng: {t}"))

    # --- quyết định cuối
    if thieu:
        return "thieu-dieu-kien", R, extra
    if unknown_net:
        R.append(mkr("MANG_CHUA_XAC_DINH", "mo", "mạng không trả lời rõ (403/429/timeout) cho repo hay gói chính"))
        return "chua-xac-dinh", R, extra
    verified_pkg = any(r.get("ton_tai") is True for r in extra["goi"])
    net_checked = not offline and (any(g["trang_thai"] != "chua-kiem" for g in extra["github"]) or extra["goi"] and any(r.get("ton_tai") != "chua-kiem" for r in extra["goi"]))
    if offline and (ghs or extra["goi"]):
        R.append(mkr("BO_QUA_MANG", "mo", "chạy --offline: chưa kiểm GitHub/gói"))
        has_net_need = True
    else:
        has_net_need = False
    if hints and not labeled:
        R.append(mkr("CHUA_NHAN_GOI_Y", "mo", "chưa gắn nhãn; nội dung gợi ý cần " + ", ".join(sorted(hints)) + " nhưng chưa xác nhận"))
        return "chua-xac-dinh", R, extra
    heavy = kinds - {"clone"}
    is_pure = (not heavy and (kind.startswith("skill") or bool(set((item.get("capability") or "").split(",")) & PURE_CAPS))) \
        or item.get("adoption") == "chi-tham-khao"
    if is_pure and not has_net_need:
        return "dung-duoc-ngay", R, extra
    if routes and not has_net_need:
        return "cai-duoc-o-day", R, extra
    if is_pure:  # offline nhưng thuần tài liệu cũng không cần mạng
        return "dung-duoc-ngay", R, extra
    if not routes:
        R.append(mkr("KHONG_CO_LENH_CAI", "mo", "không tìm thấy lệnh cài/chạy trong entry, không đủ thông tin để kết luận"))
    return "chua-xac-dinh", R, extra


# ===================================================================== điều phối
def load_items(catalog_path):
    d = json.load(open(catalog_path, encoding="utf-8"))
    return d["items"] if isinstance(d, dict) else d


def audit(items, root, net, machine, only=None, log=print):
    t0 = time.time()
    all_ids = Counter(i["id"] for i in items)
    all_paths = Counter(i.get("duong_dan", "") for i in items)
    sel = [i for i in items if not only or i["id"].startswith(only)]
    log(f"Tầng 0: kiểm tĩnh {len(sel)}/{len(items)} mục")
    statics, jobs = {}, []
    for n, it in enumerate(sel, 1):
        try:
            S = static_check(it, root, all_ids, all_paths)
        except Exception as e:  # không để một mục làm sập cả đợt
            S = {"reasons": [mkr("LOI_CONG_CU", "mo", f"công cụ lỗi khi kiểm mục này: {type(e).__name__}")], "text": None, "blocks": [],
                 "bash_jobs": [], "code": {}, "installs": [], "gh": [], "gh_total": 0, "key_names": [], "nolines": 0, "install_repos": [], "bins": []}
        statics[it["id"]] = S
        for k, code in enumerate(S["bash_jobs"]):
            jobs.append(((it["id"], k), code))
    bad, bash_ok = run_bash_syntax(jobs)
    log(f"  bash -n: {len(jobs)} khối, {len(bad)} lỗi (bash {'có' if bash_ok else 'KHÔNG có'})")
    for it in sel:
        S = statics[it["id"]]
        if S["code"]:
            nbad = sum(1 for (i, _k) in bad if i == it["id"]) if bad else 0
            finish_code_reasons(S, nbad)
    # tầng 1: gom khoá mạng
    keys = []
    for it in sel:
        S = statics[it["id"]]
        if any(r["muc"] == "hong" for r in S["reasons"]):
            continue
        for g in S["gh"]:
            keys.append(("gh", g))
        for ins in relevant_installs(it, S):
            if ins["pkg"] and ins["reg"]:
                keys.append((ins["reg"], ins["pkg"]))
    uniq = list(dict.fromkeys(keys))
    log(f"Tầng 1: {len(uniq)} tài nguyên ngoài duy nhất" + (" (bỏ qua: --offline)" if net.offline else ""))
    lookup = net.prefetch(uniq, progress_every=100) if not net.offline else {}
    # các khoá đã nằm cache nhưng chưa có trong lookup (offline thì không dùng)
    out = {}
    for it in sel:
        S = statics[it["id"]]
        usable, R, extra = classify(it, S, lookup, machine, offline=net.offline)
        out[it["id"]] = {
            "loai": it["loai"],
            "usable": usable,
            "ly_do": R,
            "chua_chay_that": True,
            "nguon_phan_loai": "nhan" if it.get("curation_status", "chua-gan-nhan") != "chua-gan-nhan" else "noi-dung",
            "cach_cai": extra["cach_cai"],
            "thieu": extra["thieu"],
            "github": extra["github"],
            "github_tong_so_link": S["gh_total"],
            "goi": extra["goi"],
            "khoi_ma": {k: {"kiem": v[0], "loi": v[1]} for k, v in S["code"].items() if v[0]},
        }
    net.save_cache()
    return out, time.time() - t0


# ===================================================================== báo cáo
USABLE_ORDER = ["dung-duoc-ngay", "cai-duoc-o-day", "thieu-dieu-kien", "nghi-ngo", "hong", "chua-xac-dinh"]
KIND_ORDER = ["mcp", "repo", "stack", "skill-kho", "skill-import", "skill-agent"]


def write_md(path, results, items, machine, meta):
    by_id = {i["id"]: i for i in items}
    L = []
    w = L.append
    w("# AUDIT — KIỂM TOÁN TỰ ĐỘNG TOÀN KHO")
    w("")
    w("> Sinh tự động bằng `tools/audit_kho.py`. Đừng sửa tay. Dữ liệu đầy đủ: `catalog/audit.json`.")
    w(f"> Chạy lúc {meta['generated']}, {meta['so_muc']} mục, {meta['thoi_gian_chay_giay']:.0f} giây, "
      f"{'KHÔNG có mạng (--offline)' if meta['offline'] else 'có mạng (chỉ-đọc)'}.")
    w("")
    w("## Đọc trước khi tin")
    w("")
    w("- **Kết quả này KHÔNG chứng minh công cụ chạy đúng.** Kiểm toán chỉ đọc file, parse cú pháp và hỏi mạng chỉ-đọc "
      "(GitHub còn sống không, gói có trên npm/PyPI/Docker Hub không). Không mục nào được cài hay chạy: mọi mục đều `chua_chay_that: true`. "
      "`cai-duoc-o-day` nghĩa là *điều kiện cần* được đáp ứng (có lệnh cài hợp lệ, gói tồn tại, máy này có công cụ), không nghĩa là công cụ chạy tốt.")
    w("- `dung-duoc-ngay` = tài liệu/prompt/skill thuần, tĩnh sạch (không lộ khoá, không file hỏng). Chưa ai kiểm skill đó có hiệu quả.")
    w("- Link GitHub trả 404 có thể là repo đổi tên hay chuyển riêng tư, không chắc đã chết hẳn. 403/429/timeout ghi `chua-xac-dinh`.")
    w("- Cột lý do có mã: `LO_KHOA`, `FILE_THIEU`... (hong); `GH_LINK_CHET`, `GOI_KHONG_TIM_THAY`, `NHAN_MAU_THUAN_*` (nghi-ngo); `THIEU_*` (thieu-dieu-kien).")
    w("")
    # bảng loại x usable
    cnt = defaultdict(Counter)
    for rid, r in results.items():
        cnt[r["loai"]][r["usable"]] += 1
    w("## 1. Đếm theo loại và usable")
    w("")
    w("| Loại | " + " | ".join(USABLE_ORDER) + " | Tổng |")
    w("|---|" + "---|" * (len(USABLE_ORDER) + 1))
    tot = Counter()
    for k in KIND_ORDER + [k for k in cnt if k not in KIND_ORDER]:
        if k not in cnt:
            continue
        row = [cnt[k][u] for u in USABLE_ORDER]
        for u in USABLE_ORDER:
            tot[u] += cnt[k][u]
        w(f"| {k} | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    w("| **Tổng** | " + " | ".join(f"**{tot[u]}**" for u in USABLE_ORDER) + f" | **{sum(tot.values())}** |")
    w("")
    # theo capability
    w("## 2. Theo capability (chỉ mục đã gắn nhãn)")
    w("")
    ccount = defaultdict(Counter)
    for rid, r in results.items():
        it = by_id.get(rid, {})
        for c in (it.get("capability") or "").split(","):
            if c:
                ccount[c][r["usable"]] += 1
    w("| Capability | " + " | ".join(USABLE_ORDER) + " | Tổng |")
    w("|---|" + "---|" * (len(USABLE_ORDER) + 1))
    for c in sorted(ccount, key=lambda x: -sum(ccount[x].values())):
        row = [ccount[c][u] for u in USABLE_ORDER]
        w(f"| {c} | " + " | ".join(map(str, row)) + f" | {sum(row)} |")
    w("")
    # link chết
    dead = []
    for rid, r in results.items():
        for x in r["ly_do"]:
            if x["ma"] in ("GH_LINK_CHET", "GOI_KHONG_TIM_THAY"):
                dead.append((0, rid, x["ma"], x["mo_ta"]))
            elif x["ma"] in ("GH_LINK_CHET_PHU", "GOI_PHU_KHONG_TIM_THAY"):
                dead.append((1, rid, x["ma"], x["mo_ta"]))
    dead.sort()
    n_main = sum(1 for d in dead if d[0] == 0)
    dead = [d[1:] for d in dead]
    w(f"## 3. Link chết hay gói không tìm thấy ({n_main} dòng chính làm mục thành nghi-ngo, {len(dead) - n_main} dòng phụ; liệt kê 30 đầu, chính trước)")
    w("")
    if dead:
        w("| Mục | Mã | Chi tiết |")
        w("|---|---|---|")
        for rid, ma, mt in dead[:30]:
            w(f"| `{rid}` | {ma} | {mt} |")
    else:
        w("_Không có._")
    w("")
    # lộ khoá
    leak = [(rid, x["mo_ta"]) for rid, r in results.items() for x in r["ly_do"] if x["ma"] == "LO_KHOA"]
    w(f"## 4. Mục nghi lộ khoá bí mật ({len(leak)})")
    w("")
    w("Chỉ ghi loại và dòng; giá trị đã che. Cần mở file đối chiếu bằng mắt (có thể là khoá mẫu trong tài liệu).")
    w("")
    if leak:
        for rid, mt in sorted(leak):
            w(f"- `{rid}`: {mt}")
    else:
        w("_Không phát hiện._")
    w("")
    # nhãn mâu thuẫn
    conf = [(rid, x["mo_ta"]) for rid, r in results.items() for x in r["ly_do"] if x["ma"].startswith("NHAN_MAU_THUAN")]
    w(f"## 5. Mục nhãn mâu thuẫn với entry ({len(conf)}; mỗi mục 1 căn cứ)")
    w("")
    if conf:
        w("| Mục | Mâu thuẫn |")
        w("|---|---|")
        for rid, mt in sorted(conf):
            w(f"| `{rid}` | {mt.replace('|', '/')} |")
    else:
        w("_Không phát hiện._")
    w("")
    # tốt nhất theo capability
    w("## 6. Dùng ngay / cài được ở đây, tốt nhất theo capability")
    w("")
    w("Xếp theo: điểm trong entry (nếu có), độ tin cậy nhãn, `cai-ngay-duoc`. Điểm là điểm sau khi ĐỌC, không phải sau khi DÙNG.")
    w("")
    w("| Capability | Mục | Usable | Điểm | Cách cài |")
    w("|---|---|---|---|---|")
    best = defaultdict(list)
    for rid, r in results.items():
        if r["usable"] not in ("dung-duoc-ngay", "cai-duoc-o-day"):
            continue
        it = by_id.get(rid, {})
        for c in (it.get("capability") or "").split(","):
            if c:
                best[c].append((rid, r, it))

    def rk(x):
        rid, r, it = x
        d = it.get("diem")
        d = d if isinstance(d, (int, float)) else -1
        return (-d, 0 if it.get("confidence") == "cao" else 1, 0 if it.get("adoption") == "cai-ngay-duoc" else 1, rid)
    for c in sorted(best):
        for rid, r, it in sorted(best[c], key=rk)[:3]:
            d = it.get("diem")
            w(f"| {c} | `{rid}` | {r['usable']} | {d if d != '' else ''} | {', '.join(r['cach_cai'][:3])} |")
    w("")
    # hồ sơ máy
    w("## 7. Hồ sơ máy đã dùng để kết luận")
    w("")
    w("| Công cụ | Có | Phiên bản |")
    w("|---|---|---|")
    for t, i in machine["cong_cu"].items():
        w(f"| {t} | {'có' if i['co'] else 'không'} | {i.get('phien_ban', '')} |")
    w("")
    w(f"- Docker daemon trả lời: {machine.get('docker_daemon_tra_loi')}; GPU NVIDIA: {machine.get('co_gpu_nvidia')}; trình duyệt: {machine.get('co_trinh_duyet')}; "
      f"là VPS: {machine.get('la_vps')}; Claude Code: {machine.get('claude_code')}.")
    present = [k for k, v in machine["khoa_env"].items() if v]
    w(f"- Khoá API có trong biến môi trường (chỉ tên): {', '.join(present) if present else 'không có khoá phổ biến nào'}.")
    w("")
    w("## 8. Chạy lại")
    w("")
    w("```bash")
    w("python tools/audit_kho.py                       # cả hai tầng, có mạng (≈ vài phút)")
    w("python tools/audit_kho.py --offline             # chỉ tầng 0 tĩnh")
    w("python tools/audit_kho.py --only repos/         # chỉ id bắt đầu bằng tiền tố")
    w("python tools/audit_kho.py --cache .audit-cache.json   # dùng lại kết quả mạng đã chắc chắn")
    w("python tools/audit_kho.py --md-only             # chỉ sinh lại AUDIT.md từ audit.json")
    w("python tools/build_catalog.py                   # đưa kiem_tu_dong / kiem_ly_do vào CATALOG.csv + catalog.json")
    w("python -m unittest discover -s tools/tests      # test công cụ (không cần mạng)")
    w("```")
    w("")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write("\n".join(L))


def main(argv=None):
    ap = argparse.ArgumentParser(description="Kiểm toán tự động kho (tĩnh + mạng chỉ-đọc)")
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--catalog", default=None)
    ap.add_argument("--offline", action="store_true", help="bỏ phần mạng (tầng 1)")
    ap.add_argument("--only", default=None, help="chỉ kiểm id bắt đầu bằng tiền tố này")
    ap.add_argument("--json-out", default=None)
    ap.add_argument("--md-out", default=None)
    ap.add_argument("--cache", default=None, help="file cache kết quả mạng chắc chắn (ngoài git)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--md-only", action="store_true", help="chỉ sinh lại AUDIT.md từ audit.json đã có (không kiểm lại)")
    a = ap.parse_args(argv)
    root = a.root
    cat = a.catalog or os.path.join(root, "catalog", "catalog.json")
    jout = a.json_out or os.path.join(root, "catalog", "audit.json")
    mout = a.md_out or os.path.join(root, "catalog", "AUDIT.md")
    items = load_items(cat)
    log = lambda *x: print(*x, file=sys.stderr, flush=True)
    if a.md_only:
        d = json.load(open(jout, encoding="utf-8"))
        write_md(mout, d["items"], items, d["may"], d["meta"])
        print(f"đã sinh lại {mout} từ {jout}")
        return
    machine = machine_profile()
    net = Net(workers=a.workers, cache_path=a.cache, offline=a.offline, log=log)
    results, secs = audit(items, root, net, machine, only=a.only, log=log)
    meta = {"generated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "tool": "tools/audit_kho.py", "phien_ban": VERSION,
            "offline": a.offline, "so_muc": len(results), "thoi_gian_chay_giay": round(secs, 1),
            "luu_y": "Kiem tinh + mang chi-doc. KHONG chay ma nao. Ket qua khong chung minh cong cu chay dung, chi chung minh dieu kien can."}
    os.makedirs(os.path.dirname(os.path.abspath(jout)), exist_ok=True)
    with open(jout, "w", encoding="utf-8") as fh:
        json.dump({"meta": meta, "may": machine, "items": results}, fh, ensure_ascii=False, indent=0)
    write_md(mout, results, items, machine, meta)
    c = Counter(r["usable"] for r in results.values())
    print(json.dumps(dict(c), ensure_ascii=False))
    print(f"xong {len(results)} mục trong {secs:.0f}s -> {jout}")


if __name__ == "__main__":
    main()
