#!/usr/bin/env python3
"""smoke_sandbox.py - chay thu CACH LY cac muc kho la cong cu ben thu ba (npm/pip/docker...).

LUAT: khong agent nao tu cai hay chay ma ben thu ba tren may nguoi dung. Cong cu nay chi de NGUOI DUNG chay,
sau khi da doc catalog/smoke-specs.json va tu doi trang_thai_duyet sang "da-duyet" cho tung muc.

- Mac dinh la --dry-run: chi in ke hoach va cac lenh docker se chay. KHONG goi tien trinh ngoai nao.
- Chay that can CA HAI co: --chay-that va --toi-da-doc-spec, va phai co Docker (docker version).
  Khong co Docker thi tu choi (cai Docker Desktop hoac WSL2). Khong bao gio chay truc tiep tren may chu.
- Moi muc: giai doan 1 cai (co mang, nguoi dung khong root, chi mount 1 thu muc tam rieng, khong truyen bien moi
  truong may chu, gioi han CPU/RAM/pid/thoi gian); giai doan 2 chay lenh_thu_nhe voi --network none. Xoa container.
- Ghi ket qua vao catalog/smoke/third-party.json. KHONG ghi USAGE-LOG (chay cach ly khong phai dung that trong du an).

Chi dung thu vien chuan Python.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SPECS_MAC_DINH = ROOT / "catalog" / "smoke-specs.json"
OUT_MAC_DINH = ROOT / "catalog" / "smoke" / "third-party.json"

CACH_CAI = {"npm", "pip", "npx", "docker", "binary", "khac"}
TRANG_THAI = {"chua-duyet", "da-duyet", "can-nguoi-doc-ky"}
IMAGE_MAC_DINH = {"npm": "node:22-bookworm-slim", "npx": "node:22-bookworm-slim", "pip": "python:3.12-slim"}
UID_GID = "1000:1000"               # nguoi dung khong root trong container
MOUNT_DICH = "/work"
CPUS_MAC_DINH = "1"
PIDS = "256"
BANG_CHUNG_TOI_DA = 600
GOI_RE = re.compile(r"^[A-Za-z0-9@][A-Za-z0-9@._/:\[\]=<>~^+-]*$")
KY_TU_SHELL = re.compile(r"[;&|<>`$\n\r]")
# lenh_thu_nhe phai la loai "nhe": chi hoi phien ban / tro giup / liet ke goi da cai
THU_NHE_RE = re.compile(r"(--version|--help|(^|\s)-h(\s|$)|^npm ls |^pip show |^docker image inspect |\brev-parse\b)")
CHUONG_TRINH_BUOC = {"git", "npm", "pip", "python3", "node"}
THOI_GIAN_TOI_DA = 3600

CO_DO_RE = [
    (re.compile(r"(?:curl|wget)\b[^\n|]*\|\s*(?:sudo\s+)?(?:ba|z|da|k)?sh\b", re.I), "curl|sh"),
    (re.compile(r"\|\s*(?:iex|invoke-expression)\b", re.I), "tai roi chay luon (| iex)"),
    (re.compile(r"\bsudo\b", re.I), "sudo"),
    (re.compile(r"--break-system-packages|--privileged|--insecure|--no-check-certificate|docker\.sock", re.I), "tat/giam bao mat"),
    (re.compile(r"\brm\s+-[a-z]*r[a-z]*f", re.I), "rm -rf"),
]
SECRET_RE = re.compile(r"((?:api[_-]?key|token|secret|password|authorization|bearer)\"?\s*[:=]\s*\"?)([^\s\",}]{6,})", re.I)

NHAN_SO_MOT = (
    "Chay cach ly KHONG phai dung that trong du an: khong ghi USAGE-LOG. Chi khi ban da dung that muc nay trong "
    "mot du an/khach that moi tao dong nhat ky bang: python -c \"import sys; sys.path.insert(0,'tools'); import thu_kho; "
    "print(thu_kho.usage_line('<id muc>', '<du an that>', 'dung duoc', '<tiet kiem gi>', ''))\" "
    "(in ra de ban tu dan vao catalog/USAGE-LOG.md; cong cu nay khong tu ghi)."
)


# ------------------------------------------------------------------ doc va kiem spec

def doc_specs(path):
    p = Path(path)
    raw = p.read_bytes()
    data = json.loads(raw.decode("utf-8"))
    specs = data["specs"] if isinstance(data, dict) else data
    return specs, hashlib.sha256(raw).hexdigest()


def kiem_spec(s):
    """Tra ve danh sach loi (rong = hop le). Chan lenh tiem nhiem: ten goi bat dau bang '-', ky tu shell, v.v."""
    loi = []
    for k in ("id", "cach_cai", "lenh_cai", "lenh_thu_nhe", "mau_pass", "timeout_giay", "can_mang_khi_cai",
              "can_khoa_api", "co_co_do", "ghi_chu", "trang_thai_duyet"):
        if k not in s:
            loi.append("thieu truong %s" % k)
    if loi:
        return loi
    if s["cach_cai"] not in CACH_CAI:
        loi.append("cach_cai khong hop le: %r" % s["cach_cai"])
    if s["trang_thai_duyet"] not in TRANG_THAI:
        loi.append("trang_thai_duyet khong hop le: %r" % s["trang_thai_duyet"])
    if not isinstance(s["timeout_giay"], int) or not (5 <= s["timeout_giay"] <= THOI_GIAN_TOI_DA):
        loi.append("timeout_giay phai la so nguyen 5..%d" % THOI_GIAN_TOI_DA)
    try:
        re.compile(s["mau_pass"])
    except re.error as e:
        loi.append("mau_pass khong phai regex: %s" % e)
    for g in s.get("goi", []):
        if not GOI_RE.match(g):
            loi.append("ten goi/image khong an toan: %r" % g)
    t = s["lenh_thu_nhe"]
    if t:
        if KY_TU_SHELL.search(t):
            loi.append("lenh_thu_nhe chua ky tu shell")
        elif not THU_NHE_RE.search(t):
            loi.append("lenh_thu_nhe phai la lenh nhe (--version, --help, npm ls, pip show, docker image inspect)")
    elif s["trang_thai_duyet"] != "can-nguoi-doc-ky":
        loi.append("lenh_thu_nhe rong chi cho phep voi can-nguoi-doc-ky")
    for b in s.get("buoc_cai", []):
        if not isinstance(b, list) or not b or b[0] not in CHUONG_TRINH_BUOC:
            loi.append("buoc_cai chi cho phep chuong trinh %s" % sorted(CHUONG_TRINH_BUOC))
            continue
        if any(KY_TU_SHELL.search(x) for x in b):
            loi.append("buoc_cai chua ky tu shell: %r" % b)
        if b[0] == "git" and not (len(b) > 1 and b[1] == "clone" and any(x.startswith("https://github.com/") for x in b)):
            loi.append("git chi duoc clone tu https://github.com/")
    return loi


def co_do_cua(s):
    """Cac ly do khong duoc chay tu dong (co do, can khoa, tra phi, spec chua duyet ky)."""
    ly_do = []
    for c in s.get("co_co_do") or []:
        ly_do.append("co do: %s" % c)
    for rx, ten in CO_DO_RE:
        if rx.search(s.get("lenh_cai", "")) and not any(ten in x for x in ly_do) and not s.get("co_co_do"):
            ly_do.append("co do (quet lai): %s" % ten)
    if s.get("can_khoa_api"):
        ly_do.append("can khoa API (%s)" % ", ".join(s.get("ten_bien_khoa") or ["?"]))
    if s.get("tra_phi"):
        ly_do.append("tra phi")
    return ly_do


def ly_do_bo_qua(s):
    """None neu duoc chay; nguoc lai chuoi ly do bo qua."""
    if s["trang_thai_duyet"] == "can-nguoi-doc-ky":
        return "can-nguoi-doc-ky: bo qua mac dinh (nguoi dung doc ky va tu chay tay neu muon)"
    if s["trang_thai_duyet"] != "da-duyet":
        return "chua duyet (doi trang_thai_duyet thanh da-duyet sau khi doc spec)"
    cd = co_do_cua(s)
    if cd:
        return "bo qua du da-duyet: " + "; ".join(cd)
    if s["cach_cai"] == "docker" and not s.get("goi"):
        return "bo chay khong ho tro muc docker khong co image don le (vd docker compose)"
    return None


# ------------------------------------------------------------------ dung lenh docker

def kiem_mount(host_dir):
    """Chi cho mount thu muc tam rieng nam duoi thu muc tam he thong, khong phai thu muc tam goc, khong nam trong repo/home."""
    p = Path(host_dir).resolve()
    tmp = Path(tempfile.gettempdir()).resolve()
    if p == tmp or tmp not in p.parents:
        raise ValueError("thu muc mount phai la thu muc con rieng cua thu muc tam: %s" % p)
    if p == ROOT.resolve() or ROOT.resolve() in p.parents:
        raise ValueError("khong mount thu muc cua repo: %s" % p)
    return str(p)


def _co_so(name, host_dir, ram, mang, env, cpus=CPUS_MAC_DINH, chi_doc=False):
    host = kiem_mount(host_dir)
    a = ["docker", "run", "--rm", "--name", name,
         "--user", UID_GID,
         "--cap-drop", "ALL", "--security-opt", "no-new-privileges",
         "--read-only", "--tmpfs", "/tmp:rw,size=256m",
         "--cpus", str(cpus), "--memory", ram, "--memory-swap", ram, "--pids-limit", PIDS,
         "--network", mang,
         "--mount", "type=bind,source=%s,target=%s%s" % (host, MOUNT_DICH, ",readonly" if chi_doc else ""),
         "-w", MOUNT_DICH]
    for k, v in env.items():      # chi KEY=VALUE hang so, tuyet doi khong "-e KEY" (se lay tu may chu)
        a += ["-e", "%s=%s" % (k, v)]
    return a


ENV_CO_BAN = {"HOME": MOUNT_DICH + "/home", "npm_config_update_notifier": "false", "CI": "1"}
ENV_THU_NHE = dict(ENV_CO_BAN, **{
    "HOME": "/tmp",
    "PATH": "/work/npm/node_modules/.bin:/work/pylib/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin",
    "PYTHONPATH": "/work/pylib",
})


def image_cua(s):
    if s.get("image"):
        return s["image"]
    return IMAGE_MAC_DINH.get(s["cach_cai"], "python:3.12-slim")


def lenh_cai_an_toan(s):
    """Dich spec sang lenh cai an toan (argv, khong qua shell). KHONG chay lenh_cai nguyen van."""
    ca = s["cach_cai"]
    goi = list(s.get("goi") or [])
    if s.get("buoc_cai"):
        return [list(b) for b in s["buoc_cai"]]
    if ca in ("npm", "npx"):
        a = ["npm", "install", "--no-audit", "--no-fund", "--prefix", MOUNT_DICH + "/npm"]
        if not s.get("cho_phep_script"):
            a.insert(2, "--ignore-scripts")
        return [a + goi]
    if ca == "pip":
        a = ["pip", "install", "--no-input", "--disable-pip-version-check", "--target", MOUNT_DICH + "/pylib"]
        if not s.get("cho_phep_sdist"):
            a.insert(2, "--only-binary=:all:")
        return [a + goi]
    return []


def ke_hoach(s, host_dir=None):
    """Tra ve danh sach buoc (moi buoc: {pha, mo_ta, argv}). Khong chay gi."""
    ten = re.sub(r"[^a-z0-9]+", "-", s["id"].lower()).strip("-")[:40]
    host = host_dir or os.path.join(tempfile.gettempdir(), "smoke-" + ten)
    ram = s.get("ram", "1g")
    nhan = "smoke-%s-%d" % (ten, os.getpid())
    steps = []
    if s["cach_cai"] == "docker":
        for img in s.get("goi") or []:
            steps.append({"pha": "1", "mo_ta": "keo image (co mang, khong chay container)", "argv": ["docker", "pull", img], "ten": None})
        steps.append({"pha": "2", "mo_ta": "kiem image (khong chay ma ben thu ba)", "argv": shlex.split(s["lenh_thu_nhe"]) if s["lenh_thu_nhe"] else [], "ten": None})
        return steps
    img = image_cua(s)
    for i, argv in enumerate(lenh_cai_an_toan(s), 1):
        name = "%s-p1-%d" % (nhan, i)
        steps.append({"pha": "1", "mo_ta": "cai (co mang, user khong root)", "ten": name,
                      "argv": _co_so(name, host, ram, "bridge", ENV_CO_BAN) + [img] + argv})
    name2 = "%s-p2" % nhan
    steps.append({"pha": "2", "mo_ta": "chay lenh nhe (--network none)", "ten": name2,
                  "argv": _co_so(name2, host, ram, "none", ENV_THU_NHE, chi_doc=True) + [img] + shlex.split(s["lenh_thu_nhe"])})
    return steps


# ------------------------------------------------------------------ chay

def docker_san_sang():
    """True neu `docker version` chay duoc (co ca server)."""
    try:
        r = subprocess.run(["docker", "version", "--format", "{{.Server.Version}}"], capture_output=True, text=True, timeout=30)
        return r.returncode == 0 and bool((r.stdout or "").strip())
    except (OSError, subprocess.SubprocessError):
        return False


def _rut_gon(text):
    t = SECRET_RE.sub(r"\1[REDACTED]", text or "")
    t = re.sub(r"\s+", " ", t).strip()
    return t[-BANG_CHUNG_TOI_DA:] if len(t) > BANG_CHUNG_TOI_DA else t


def _chay(argv, timeout):
    try:
        r = subprocess.run(argv, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout)
        return r.returncode, (r.stdout or "") + (r.stderr or ""), False
    except subprocess.TimeoutExpired as e:
        out = e.stdout if isinstance(e.stdout, str) else ""
        return None, out or "", True
    except OSError as e:
        return None, "khong chay duoc: %s" % e, False


def _don_container(ten):
    if not ten:
        return
    try:
        subprocess.run(["docker", "rm", "-f", ten], capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.SubprocessError):
        pass


def chay_mot_spec(s):
    """Chay that 1 spec da duoc phep. Tra ve ban ghi ket qua."""
    t0 = time.time()
    steps_ten = []
    host = tempfile.mkdtemp(prefix="smoke-")
    existed_images = {}
    try:
        os.chmod(host, 0o777)      # cho uid 1000 trong container ghi duoc
        steps = ke_hoach(s, host)
        ban_ghi = []
        mo = {"keo": False}
        if s["cach_cai"] == "docker":
            for st in steps:
                if st["pha"] == "1":
                    img = st["argv"][-1]
                    rc0, _, _ = _chay(["docker", "image", "inspect", img], 60)
                    existed_images[img] = (rc0 == 0)
        for st in steps:
            if not st["argv"]:
                continue
            if st["ten"]:
                steps_ten.append(st["ten"])
            rc, out, het_gio = _chay(st["argv"], s["timeout_giay"])
            ban_ghi.append("[pha %s] %s" % (st["pha"], _rut_gon(out)))
            if het_gio:
                _don_container(st["ten"])
                return _kq(s, "fail", "het thoi gian (%ds) o pha %s. %s" % (s["timeout_giay"], st["pha"], " ".join(ban_ghi)), t0)
            if st["pha"] == "1" and rc != 0:
                return _kq(s, "fail", "cai that bai (ma thoat %s). %s" % (rc, " ".join(ban_ghi)), t0)
            if st["pha"] == "2":
                khop = re.search(s["mau_pass"], out, re.M) is not None
                if rc == 0 and khop:
                    return _kq(s, "pass", "ma thoat 0, khop mau_pass. %s" % " ".join(ban_ghi), t0)
                return _kq(s, "fail", "ma thoat %s, %s mau_pass. %s" % (rc, "khop" if khop else "KHONG khop", " ".join(ban_ghi)), t0)
        return _kq(s, "fail", "khong co buoc kiem nao", t0)
    finally:
        for n in steps_ten:
            _don_container(n)
        if s["cach_cai"] == "docker":
            for img, tonTai in existed_images.items():
                if not tonTai:      # chi xoa image do chinh lan chay nay keo ve
                    try:
                        subprocess.run(["docker", "rmi", "-f", img], capture_output=True, text=True, timeout=120)
                    except (OSError, subprocess.SubprocessError):
                        pass
        shutil.rmtree(host, ignore_errors=True)


def _kq(s, verdict, bang_chung, t0):
    return {"id": s["id"], "verdict": verdict, "bang_chung": _rut_gon(bang_chung) if len(bang_chung) > BANG_CHUNG_TOI_DA else bang_chung,
            "thoi_gian": round(time.time() - t0, 1)}


def ghi_ket_qua(path, ket_qua, spec_sha):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    cu = {}
    if path.is_file():
        try:
            cu = {x["id"]: x for x in json.loads(path.read_text(encoding="utf-8")).get("ket_qua", [])}
        except (ValueError, OSError):
            cu = {}
    for k in ket_qua:
        cu[k["id"]] = k
    doc = {"lo": "third-party-sandbox", "ngay": datetime.date.today().isoformat(),
           "phuong_phap": "chay-cach-ly-docker", "spec_sha256": spec_sha, "ket_qua": list(cu.values())}
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ main

def main(argv=None, out=None):
    out = out or sys.stdout

    def p(*a):
        print(*a, file=out)

    ap = argparse.ArgumentParser(description="Chay thu cach ly (Docker) cac cong cu ben thu ba trong kho. Mac dinh la --dry-run.")
    ap.add_argument("--specs", default=str(SPECS_MAC_DINH))
    ap.add_argument("--out", default=str(OUT_MAC_DINH))
    ap.add_argument("--ids", default="", help="chi cac id nay (phan cach bang dau phay)")
    ap.add_argument("--limit", type=int, default=0, help="chi chay N muc dau tien du dieu kien")
    ap.add_argument("--dry-run", action="store_true", help="(mac dinh) chi in ke hoach")
    ap.add_argument("--xem-ca-chua-duyet", action="store_true", help="dry-run: in ca lenh docker cua muc chua duyet")
    ap.add_argument("--chay-that", action="store_true", help="chay that trong Docker (can them --toi-da-doc-spec)")
    ap.add_argument("--toi-da-doc-spec", action="store_true", help="xac nhan ban da doc catalog/smoke-specs.json")
    a = ap.parse_args(argv)

    chay_that = a.chay_that and not a.dry_run
    try:
        specs, sha = doc_specs(a.specs)
    except (OSError, ValueError, KeyError) as e:
        p("Khong doc duoc spec: %s" % e)
        return 2
    if a.ids:
        want = [x.strip() for x in a.ids.split(",") if x.strip()]
        specs = [s for s in specs if s.get("id") in want]
    loi_all = {s.get("id", "?"): kiem_spec(s) for s in specs}
    xau = {k: v for k, v in loi_all.items() if v}
    if xau:
        for k, v in xau.items():
            p("SPEC LOI %s: %s" % (k, "; ".join(v)))
        p("Dung lai: sua spec cho hop le roi chay lai.")
        return 2

    if chay_that:
        if not a.toi_da_doc_spec:
            p("TU CHOI: chay that can them --toi-da-doc-spec (xac nhan ban da doc catalog/smoke-specs.json).")
            return 2
        if not docker_san_sang():
            p("TU CHOI: khong thay Docker dang chay (`docker version` that bai). Cai Docker Desktop (Windows/macOS) hoac "
              "WSL2 + Docker Engine roi chay lai. Cong cu nay KHONG bao gio chay truc tiep tren may chu; "
              "luc nay chi ho tro --dry-run.")
            return 3

    chay_duoc, bo_qua = [], []
    for s in specs:
        ld = ly_do_bo_qua(s)
        (bo_qua if ld else chay_duoc).append((s, ld))
    if a.limit > 0:
        chay_duoc = chay_duoc[:a.limit]

    p("== smoke_sandbox: %s | %d spec | chay duoc %d | bo qua %d ==" % (
        "CHAY THAT" if chay_that else "DRY-RUN (khong chay gi)", len(specs), len(chay_duoc), len(bo_qua)))
    p("spec sha256: %s" % sha)

    if not chay_that:
        hien = list(chay_duoc)
        if a.xem_ca_chua_duyet:
            hien += list(bo_qua)
        for s, ld in hien:
            p("\n- %s [%s] cach_cai=%s%s" % (s["id"], s["trang_thai_duyet"], s["cach_cai"], ("  (SE BO QUA: %s)" % ld) if ld else ""))
            if ld and not a.xem_ca_chua_duyet:
                continue
            for st in ke_hoach(s):
                if st["argv"]:
                    p("    pha %s - %s:\n      %s" % (st["pha"], st["mo_ta"], " ".join(shlex.quote(x) for x in st["argv"])))
        if not a.xem_ca_chua_duyet:
            for s, ld in bo_qua:
                p("\n- %s [%s] BO QUA: %s" % (s["id"], s["trang_thai_duyet"], ld))
        p("\nDay chi la ke hoach. De chay that: them --chay-that --toi-da-doc-spec (can Docker) va chi cac spec da-duyet moi chay.")
        return 0

    ket_qua = []
    for s, ld in bo_qua:
        ket_qua.append({"id": s["id"], "verdict": "bo-qua", "bang_chung": ld, "thoi_gian": 0})
    for s, _ in chay_duoc:
        p("Dang chay %s ..." % s["id"])
        kq = chay_mot_spec(s)
        ket_qua.append(kq)
        p("  -> %s (%.1fs): %s" % (kq["verdict"], kq["thoi_gian"], kq["bang_chung"][:200]))
    ghi_ket_qua(a.out, ket_qua, sha)
    p("\nDa ghi ket qua: %s" % a.out)
    p(NHAN_SO_MOT)
    return 0


if __name__ == "__main__":
    sys.exit(main())
