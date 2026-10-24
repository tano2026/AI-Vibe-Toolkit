#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Company Engine: bộ máy giao việc + phối hợp cho công ty agent (ORG-v2 v3, COORDINATION-v2, DECISION-MATRIX).

Chỉ dùng thư viện chuẩn. KHÔNG gọi mạng, KHÔNG dùng credential. Trạng thái lưu 1 file JSON
(thay Airtable company-hq khi chạy thử; cùng tên trường để sau này đổi backend không đổi logic).
Việc "nghĩ" của agent được cắm qua `executor(role, job, ctx) -> str`; mặc định là bản giả để test.

Luật cứng lấy từ DECISION-MATRIX.md:
  - Không có approval `approved` thì KHÔNG thực thi hành động rủi ro (chi tiền / đăng / gửi ngoài / cam kết khách).
  - Không chắc mức nào -> coi là mức cao hơn (loại rủi ro lạ = L3).
  - Job có nội dung scrape -> mọi mức từ L1 trở lên tự nâng 1 mức.
  - Approval hết hạn 24h = KHÔNG làm.
  - Kẹt >24h hoặc lỗi lặp 3 lần -> escalation.

Lệnh demo:  python tools/company_engine.py demo
"""
import json
import sys
import time
from pathlib import Path

# ---- Sổ nhân sự: 9 agent thật (ORG-v2 v3). Không thêm role ngoài danh sách này. ----
ROLES = {
    "ceo": "dispatch",  # tầng Hermes: chia việc, không nhận job chuyên môn
    "research": "reasoning", "dev": "balanced", "sales": "balanced", "marketing": "creative",
    "media": "creative", "operations": "cheap", "support": "cheap", "analytics": "reasoning",
}
WORKERS = [r for r in ROLES if r != "ceo"]

# Review chéo: người làm -> người soát (COORDINATION-v2 mục 5). Dev không có reviewer chéo.
REVIEWER = {
    "marketing": "research", "media": "marketing", "sales": "marketing",
    "operations": "research", "analytics": "research", "support": "operations",
    "research": "analytics",
}

PRIORITY = {"P0": 0, "P1": 1, "P2": 2}
BRIEF_FIELDS = ("context", "yeu_cau", "input", "deadline", "done_khi")  # handoff 5 phần

# Loại rủi ro -> mức gốc (DECISION-MATRIX). Rỗng = L0. Loại không biết = L3.
RISK_LEVEL = {
    None: "L0", "internal": "L1",
    "spend_money": "L2", "publish": "L2", "send_external": "L2", "production": "L2",
    "commit_customer": "L3", "credential": "L3", "change_pricing": "L3", "delete_data": "L3",
}
LEVELS = ["L0", "L1", "L2", "L3"]
DAY = 24 * 3600
MAX_FAILS = 3


def risk_level(risk_type, scraped=False):
    """Mức quyết định của 1 job. Loại lạ -> L3; có scrape thì nâng 1 mức từ L1 trở lên."""
    lv = RISK_LEVEL.get(risk_type, "L3")
    if scraped and lv != "L0":
        lv = LEVELS[min(LEVELS.index(lv) + 1, 3)]
    return lv


def giao_viec_thieu(pack, role, brief):
    """EA Gate: trả MỘT câu hỏi duy nhất nếu thiếu thông tin, ngược lại None."""
    if not pack:
        return "Thiếu [PACK]: việc này cho client/domain nào?"
    if role not in WORKERS:
        return f"Role '{role}' không có trong 8 agent chuyên môn: {', '.join(WORKERS)}."
    for f in BRIEF_FIELDS:
        if not (brief or {}).get(f):
            return f"Brief thiếu phần '{f}'."
    return None


def executor_gia(role, job, ctx):
    """Agent giả cho test/demo: ghi lại role + brief + tên các đầu vào nhận từ role khác."""
    tu = ", ".join(f"{k}" for k in ctx["inputs"]) or "không"
    return f"[{role}] {job['brief']['yeu_cau']} (nhận từ: {tu})"


def reviewer_gia(reviewer, job, output):
    """Reviewer giả: đạt nếu output không rỗng. Thay bằng agent thật khi nối vào Hermes."""
    return (bool(output.strip()), "ok" if output.strip() else "output rỗng")


class Company:
    def __init__(self, path, executor=executor_gia, reviewer=reviewer_gia, actuator=None, clock=time.time):
        self.path = Path(path)
        self.executor, self.reviewer, self.actuator, self.clock = executor, reviewer, actuator, clock
        self.db = {"jobs": [], "approvals": [], "escalations": [], "activity_log": []}
        if self.path.exists():
            self.db = json.loads(self.path.read_text(encoding="utf-8"))

    # ---- nền tảng ----
    def _save(self):
        self.path.write_text(json.dumps(self.db, ensure_ascii=False, indent=1), encoding="utf-8")

    def _log(self, job_id, role, event, tokens=0):
        self.db["activity_log"].append({"ts": self.clock(), "job_id": job_id, "role": role,
                                        "event": event, "tokens": tokens})

    def job(self, job_id):
        return next(j for j in self.db["jobs"] if j["job_id"] == job_id)

    # ---- 1. giao việc (CEO hoặc role ngang hàng) ----
    def submit(self, pack, role, brief, priority="P1", depends_on=(), requested_by="ceo",
               risk_type=None, scraped=False):
        """Tạo job queued. Trả (job_id, None) hoặc (None, câu hỏi) khi EA Gate chặn."""
        cau_hoi = giao_viec_thieu(pack, role, brief)
        if cau_hoi:
            return None, cau_hoi
        if requested_by != "ceo" and requested_by not in WORKERS:
            return None, f"requested_by '{requested_by}' không phải ceo hay role hợp lệ."
        for d in depends_on:
            self.job(d)  # job phụ thuộc phải tồn tại
        lv = risk_level(risk_type, scraped)
        job = {"job_id": len(self.db["jobs"]) + 1, "pack": pack, "role": role, "brief": brief,
               "status": "queued", "priority": priority, "depends_on": list(depends_on),
               "requested_by": requested_by, "risk_type": risk_type, "risk_level": lv,
               "output": None, "review_note": None, "rounds": 0, "fails": 0,
               "created": self.clock(), "updated": self.clock()}
        self.db["jobs"].append(job)
        self._log(job["job_id"], requested_by, f"giao {role}: {brief['yeu_cau'][:60]}")
        if lv == "L3":  # L3 = hỏi TRƯỚC khi làm, không đặt sự đã rồi
            self._open_approval(job, "xin phép trước khi bắt đầu")
        self._save()
        return job["job_id"], None

    # ---- 2. điều phối ----
    def tick(self):
        """Một nhịp dispatch: chạy mọi job queued đã đủ điều kiện, ưu tiên P0 trước. Trả số job đã xử lý."""
        n = 0
        while True:
            ready = [j for j in self.db["jobs"] if j["status"] == "queued"
                     and all(self.job(d)["status"] == "done" for d in j["depends_on"])]
            if not ready:
                break
            ready.sort(key=lambda j: (PRIORITY[j["priority"]], j["job_id"]))
            self._run(ready[0])
            n += 1
        self._block_stale()
        self._save()
        return n

    def _run(self, job):
        job["status"], job["updated"] = "doing", self.clock()
        ctx = {"inputs": {f"job{d}:{self.job(d)['role']}": self.job(d)["output"] for d in job["depends_on"]},
               "review_note": job["review_note"]}  # đầu ra của role khác = đầu vào của role này
        try:
            job["output"] = self.executor(job["role"], job, ctx)
        except Exception as e:  # noqa: BLE001 — mọi lỗi executor đều tính vào ngưỡng escalation
            job["fails"] += 1
            job["status"] = "queued"
            self._log(job["job_id"], job["role"], f"lỗi lần {job['fails']}: {e}")
            if job["fails"] >= MAX_FAILS:
                self._escalate(job, f"lỗi lặp {MAX_FAILS} lần: {e}")
            return
        self._log(job["job_id"], job["role"], "làm xong, chờ review", tokens=len(job["output"]) // 4)
        job["status"] = "review"
        self._review(job)

    def _review(self, job):
        rv = REVIEWER.get(job["role"])
        ok, note = (True, "không cần review chéo") if rv is None else self.reviewer(rv, job, job["output"])
        job["review_note"] = note
        if not ok:
            if job["rounds"] >= 1:  # tối đa 1 vòng sửa, còn cấn thì kêu CEO
                self._escalate(job, f"review không đạt sau 1 vòng sửa: {note}")
            else:
                job["rounds"] += 1
                job["status"] = "queued"
                self._log(job["job_id"], rv, f"trả về sửa: {note}")
            return
        self._log(job["job_id"], rv or job["role"], f"review đạt: {note}")
        lv = job["risk_level"]
        if lv == "L2":
            self._open_approval(job, "xin duyệt trước khi thực thi")
        elif lv == "L3":
            job["status"] = "awaiting_approval"  # đã xin phép từ đầu; chờ approval còn hiệu lực
            self._ensure_pending_or_approved(job)
        else:
            self._finish(job)

    def _finish(self, job):
        """Chốt done. Hành động rủi ro chỉ chạy khi có approval `approved` (luật sắt)."""
        if job["risk_type"] in ("spend_money", "publish", "send_external", "commit_customer",
                                "production", "credential", "change_pricing", "delete_data"):
            if not self._approved(job):
                raise PermissionError(f"job {job['job_id']}: chưa có approval approved")
            if self.actuator:
                self.actuator(job)
        job["status"], job["updated"] = "done", self.clock()
        self._log(job["job_id"], job["role"], "done")

    # ---- 3. cổng duyệt ----
    def _open_approval(self, job, ly_do):
        self.db["approvals"].append({"job_id": job["job_id"], "action": job["brief"]["yeu_cau"],
                                     "risk_type": job["risk_type"], "risk_level": job["risk_level"],
                                     "status": "pending", "opened": self.clock(), "decided_at": None,
                                     "reminded": False})
        job["status"] = "awaiting_approval"
        self._log(job["job_id"], job["role"], f"mở approval ({job['risk_level']}): {ly_do}")

    def _approval(self, job_id):
        xs = [a for a in self.db["approvals"] if a["job_id"] == job_id]
        return xs[-1] if xs else None

    def _approved(self, job):
        a = self._approval(job["job_id"])
        return bool(a and a["status"] == "approved")

    def _ensure_pending_or_approved(self, job):
        a = self._approval(job["job_id"])
        if a and a["status"] == "approved":
            self._finish(job)

    def approve(self, job_id):
        """CEO gõ 'OK <id>'. Nếu job đã làm xong phần soạn thì chạy hành động và chốt done."""
        a = self._approval(job_id)
        if not a or a["status"] != "pending":
            return False
        a["status"], a["decided_at"] = "approved", self.clock()
        job = self.job(job_id)
        self._log(job_id, "ceo", "approved")
        if job["risk_level"] == "L3" and job["output"] is None:
            job["status"] = "queued"  # L3: được phép rồi mới bắt đầu làm
        else:
            self._finish(job)
        self._save()
        return True

    def reject(self, job_id, note):
        """CEO gõ 'NO <id>': job về queued kèm ghi chú để role sửa."""
        a = self._approval(job_id)
        if not a or a["status"] != "pending":
            return False
        a["status"], a["decided_at"] = "rejected", self.clock()
        job = self.job(job_id)
        job["status"], job["review_note"], job["output"] = "queued", f"CEO từ chối: {note}", None
        self._log(job_id, "ceo", f"rejected: {note}")
        self._save()
        return True

    def expire_approvals(self):
        """Im lặng quá 24h = expired = KHÔNG làm. Trả list job cần nhắc (đúng 1 lần)."""
        nhac = []
        for a in self.db["approvals"]:
            if a["status"] == "pending" and self.clock() - a["opened"] > DAY:
                a["status"], a["decided_at"] = "expired", self.clock()
                if not a["reminded"]:
                    a["reminded"] = True
                    nhac.append(a["job_id"])
                self._log(a["job_id"], "ceo", "approval expired — không thực thi")
        self._save()
        return nhac

    # ---- 4. leo thang ----
    def _escalate(self, job, ly_do):
        job["status"] = "blocked"
        self.db["escalations"].append({"ts": self.clock(), "job_id": job["job_id"],
                                       "role": job["role"], "reason": ly_do, "resolved": False})
        self._log(job["job_id"], job["role"], f"escalate: {ly_do}")

    def _block_stale(self):
        """Job doing/review mà không nhúc nhích >24h -> escalation (kẹt)."""
        for j in self.db["jobs"]:
            if j["status"] in ("doing", "review") and self.clock() - j["updated"] > DAY:
                self._escalate(j, "kẹt >24h")

    # ---- 5. CEO Cockpit: view duy nhất mỗi sáng ----
    def cockpit(self):
        now = self.clock()
        return {
            "cho_duyet": [j["job_id"] for j in self.db["jobs"] if j["status"] == "awaiting_approval"],
            "bi_ket": [e["job_id"] for e in self.db["escalations"] if not e["resolved"]],
            "xong_24h": [j["job_id"] for j in self.db["jobs"]
                         if j["status"] == "done" and now - j["updated"] <= DAY],
        }


# ---- Playbook: CEO chia 1 mục tiêu thành DAG job ----
PLAYBOOKS = {
    # (role, yêu cầu, phụ thuộc theo chỉ số bước, risk_type)
    "chien-dich-noi-dung": [
        ("research", "Quét thị trường + đối thủ + insight cho: {goal}", [], None),
        ("marketing", "Viết plan nội dung + bài đăng cho: {goal}", [0], None),
        ("media", "Làm visual theo plan nội dung cho: {goal}", [1], None),
        ("media", "Đăng bài đã duyệt cho: {goal}", [1, 2], "publish"),
        ("analytics", "Đo KPI sau đăng cho: {goal}", [3], None),
    ],
}


def run_playbook(company, pack, name, goal, deadline="T+7"):
    """Biến mục tiêu thành chuỗi job có phụ thuộc; trả list job_id (hoặc câu hỏi của EA Gate)."""
    ids = []
    for role, yc, deps, risk in PLAYBOOKS[name]:
        brief = {"context": goal, "yeu_cau": yc.format(goal=goal), "input": "đầu ra các bước trước",
                 "deadline": deadline, "done_khi": "output đủ để bước sau dùng"}
        jid, hoi = company.submit(pack, role, brief, depends_on=[ids[d] for d in deps], risk_type=risk)
        if hoi:
            return None, hoi
        ids.append(jid)
    return ids, None


def _demo():
    import tempfile
    c = Company(Path(tempfile.mkdtemp()) / "hq.json")
    ids, hoi = run_playbook(c, "trum-san-bay", "chien-dich-noi-dung", "tour Nhật 4N3Đ")
    print("Job:", ids, hoi or "")
    c.tick()
    print("Sau tick 1 (chờ duyệt đăng):", c.cockpit())
    for j in c.cockpit()["cho_duyet"]:
        c.approve(j)
    c.tick()
    print("Sau khi CEO OK:", c.cockpit())
    for e in c.db["activity_log"]:
        print(f"  job{e['job_id']} {e['role']:9} {e['event']}")


if __name__ == "__main__":
    if sys.argv[1:] == ["demo"]:
        _demo()
    else:
        print(__doc__)
