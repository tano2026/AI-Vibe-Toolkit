"""
brain.py — RIO Brain v2.0 (code-driven state machine)

Pipeline cố định — code quyết định flow, không phải LLM, không phải scraped content:

    INTAKE → PLAN → COLLECT → VALIDATE → ANALYZE → SYNTHESIZE → VERIFY → DELIVER

Wiring trong rio_bot.py:

    from brain import RIOBrain
    import ratelimit
    web_search.search = ratelimit.throttled_search(web_search.search)

    brain = RIOBrain(adapters={
        "search": web_search.search,           # (query) -> list[{title,url,snippet}]
        "cn":     cn_trends.get_trends,        # (platform) -> list[dict]     (optional)
        "video":  video_extract.extract,       # (url) -> {transcript, meta}  (optional)
        "report": report_gen.format_report,    # (dict) -> str                (optional)
    })
    text = brain.run("market", "thị trường fast track sân bay VN")
"""
import time, traceback
import memory, validator

# ---------------------------------------------------------------- sub-question templates

SUBQ_TEMPLATES = {
    "market": [
        "quy mô thị trường {topic}",
        "{topic} tăng trưởng CAGR",
        "đối thủ chính {topic}",
        "{topic} xu hướng 2026",
    ],
    "swot": [
        "{topic} điểm mạnh lợi thế",
        "{topic} điểm yếu hạn chế",
        "{topic} cơ hội thị trường",
        "{topic} rủi ro thách thức",
    ],
    "sentiment": [
        "{topic} đánh giá review",
        "{topic} phàn nàn complaint",
        "{topic} khen ngợi feedback tích cực",
    ],
    "forecast": [
        "{topic} dự báo forecast",
        "{topic} số liệu lịch sử",
        "{topic} yếu tố ảnh hưởng tương lai",
    ],
    "kpi": [
        "{topic} KPI benchmark ngành",
        "{topic} chỉ số trung bình industry average",
    ],
    "deep": [
        "{topic}",
        "{topic} là gì phân tích",
        "{topic} số liệu thống kê mới nhất",
        "{topic} chuyên gia nhận định",
        "{topic} case study thực tế",
    ],
}


class RIOBrain:
    def __init__(self, adapters):
        self.adapters = adapters
        self.max_stage_retry = 1

    # ------------------------------------------------------------ public

    def run(self, rtype, topic, cn_platform=None, video_url=None):
        """Entry point duy nhất. Trả về report text sẵn gửi Telegram."""
        state = {
            "rtype": rtype, "topic": topic,
            "cn_platform": cn_platform, "video_url": video_url,
            "subqs": [], "evidence": [], "claims": [],
            "analysis": {}, "report": "", "warnings": [],
            "t0": time.time(),
        }
        pipeline = [self._plan, self._collect, self._validate,
                    self._analyze, self._synthesize, self._verify]
        for stage in pipeline:
            ok = self._run_stage(stage, state)
            if not ok:
                state["warnings"].append(f"⚠️ Stage {stage.__name__} fail sau retry — output có thể thiếu.")
        return self._deliver(state)

    # ------------------------------------------------------------ stage runner

    def _run_stage(self, stage, state):
        for attempt in range(self.max_stage_retry + 1):
            try:
                stage(state)
                return True
            except Exception as e:
                memory.log_lesson(stage.__name__, f"{e} | {traceback.format_exc()[-300:]}")
                if attempt >= self.max_stage_retry:
                    return False
                time.sleep(1)

    # ------------------------------------------------------------ stages

    def _plan(self, s):
        tmpl = SUBQ_TEMPLATES.get(s["rtype"], SUBQ_TEMPLATES["deep"])
        s["subqs"] = [t.format(topic=s["topic"]) for t in tmpl]
        # tận dụng research cũ nếu có
        s["prior"] = memory.get_history(s["topic"], limit=2)

    def _collect(self, s):
        search = self.adapters["search"]
        for q in s["subqs"]:
            for r in (search(q) or [])[:5]:
                s["evidence"].append({
                    "query": q,
                    "url": r.get("url", ""),
                    "title": validator.sanitize(r.get("title", "")),
                    "snippet": validator.sanitize(r.get("snippet", "")),
                })
        # nguồn phụ — degrade nhẹ nhàng, không chết pipeline
        if s.get("cn_platform") and "cn" in self.adapters:
            try:
                for t in (self.adapters["cn"](s["cn_platform"]) or [])[:10]:
                    s["evidence"].append({"query": f"cn:{s['cn_platform']}", "url": "cn_trends",
                                          "title": validator.sanitize(str(t)), "snippet": ""})
            except Exception:
                s["warnings"].append("🔄 CN trends không truy cập được lúc này.")
        if s.get("video_url") and "video" in self.adapters:
            try:
                v = self.adapters["video"](s["video_url"]) or {}
                s["evidence"].append({"query": "video", "url": s["video_url"],
                                      "title": "video transcript",
                                      "snippet": validator.sanitize(v.get("transcript", ""))[:5000]})
            except Exception:
                s["warnings"].append("🔄 Nguồn video không truy cập được (yt-dlp fail).")

    def _validate(self, s):
        # chấm nguồn + bỏ nguồn rác
        kept = []
        for ev in s["evidence"]:
            if ev["url"].startswith("http"):
                score, domain = validator.score_source(ev["url"])
                ev["score"], ev["domain"] = score, domain
                memory.bump_source(domain, ok=score >= 0.4)
                if score >= 0.35:
                    kept.append(ev)
            else:
                ev["score"], ev["domain"] = 0.5, ev["url"]
                kept.append(ev)
        s["evidence"] = kept

        # gom claim số liệu: mỗi số tìm được trong snippet = 1 claim ứng viên
        num_map = {}
        for ev in s["evidence"]:
            for num in validator.extract_numbers(ev["snippet"]):
                num_map.setdefault(num, []).append(ev)
        s["claims"] = validator.rate_facts([
            {"text": num, "evidence": evs} for num, evs in num_map.items()
        ])

    def _analyze(self, s):
        by_q = {}
        for ev in s["evidence"]:
            by_q.setdefault(ev["query"], []).append(ev)
        s["analysis"] = {
            "n_sources": len({e.get("domain") for e in s["evidence"]}),
            "n_evidence": len(s["evidence"]),
            "coverage": {q: len(v) for q, v in by_q.items()},
            "confirmed": [c for c in s["claims"] if c["rating"] == "✅"],
            "single": [c for c in s["claims"] if c["rating"] == "🟡"],
            "avg_source_score": round(
                sum(e.get("score", 0.5) for e in s["evidence"]) / max(len(s["evidence"]), 1), 2),
        }

    def _synthesize(self, s):
        a = s["analysis"]
        lines = [f"📊 *RIO Research — {s['rtype'].upper()}: {s['topic']}*",
                 f"_Nguồn: {a['n_sources']} domain · {a['n_evidence']} evidence · "
                 f"độ tin cậy TB {a['avg_source_score']}_", ""]

        for q in s["subqs"]:
            evs = [e for e in s["evidence"] if e["query"] == q][:3]
            if not evs:
                lines.append(f"• {q}: 🔄 chưa tìm được nguồn đáng tin.")
                continue
            lines.append(f"*{q}*")
            for e in evs:
                snip = e["snippet"][:180]
                lines.append(f"  · {snip} — `{e['domain']}`")
            lines.append("")

        if a["confirmed"]:
            lines.append("*Số liệu xác nhận đa nguồn:*")
            for c in a["confirmed"][:8]:
                doms = ", ".join({e["domain"] for e in c["evidence"]})
                lines.append(f"  ✅ {c['text']} ({doms})")
        if a["single"]:
            lines.append("*Số liệu 1 nguồn (dùng thận trọng):*")
            for c in a["single"][:5]:
                lines.append(f"  🟡 {c['text']} ({c['evidence'][0]['domain']})")

        if s.get("prior"):
            lines.append("")
            lines.append(f"_📁 Có {len(s['prior'])} research cũ liên quan trong memory._")

        s["report"] = "\n".join(lines)
        # cho phép report_gen adapter format lại nếu có
        if "report" in self.adapters:
            try:
                s["report"] = self.adapters["report"]({"raw": s["report"], "state": s}) or s["report"]
            except Exception:
                pass  # giữ bản template

    def _verify(self, s):
        problems = []
        generic = validator.detect_generic(s["report"])
        if generic:
            problems.append(f"generic AI language: {generic}")
        ledger = {c["text"] for c in s["claims"]}
        orphans = validator.orphan_numbers(s["report"], ledger)
        # số mồ côi từ chính snippet nguồn thì không tính — chỉ cảnh báo khi nhiều bất thường
        if len(orphans) > len(ledger) * 2 + 10:
            problems.append(f"{len(orphans)} số liệu không có trong fact ledger")
        uncovered = [q for q, n in s["analysis"]["coverage"].items() if n == 0]
        if len(uncovered) == len(s["subqs"]):
            problems.append("không sub-question nào có evidence")
        if problems:
            raise RuntimeError("; ".join(problems))

    def _deliver(self, s):
        if s["warnings"]:
            s["report"] += "\n\n" + "\n".join(s["warnings"])
        quality = s["analysis"].get("avg_source_score", 0)
        memory.log_research(s["rtype"], s["topic"], quality,
                            len(s["claims"]), s["report"])
        s["report"] += f"\n\n_⏱ {round(time.time() - s['t0'], 1)}s_"
        return chunk_telegram(s["report"])


def chunk_telegram(text, limit=4000):
    """Telegram cap 4096 ký tự / message. Trả list chunk cắt theo dòng."""
    if len(text) <= limit:
        return [text]
    chunks, cur = [], ""
    for line in text.split("\n"):
        if len(cur) + len(line) + 1 > limit:
            chunks.append(cur)
            cur = line
        else:
            cur = f"{cur}\n{line}" if cur else line
    if cur:
        chunks.append(cur)
    return chunks
