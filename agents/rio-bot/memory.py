"""
memory.py — Long-term memory cho RIO Brain (SQLite, zero dependency ngoài stdlib)

4 bảng:
  research_history : lịch sử research (topic, type, quality, report)
  evidence_cache   : cache kết quả search/scrape, TTL 24h — đỡ gọi DDG lại
  source_scores    : điểm tin cậy từng domain, học dần qua thời gian
  lessons          : bài học rút ra (lỗi gặp, fix gì) — chống lặp lại sai lầm
"""
import sqlite3, json, time, hashlib, os

DB_PATH = os.environ.get("RIO_DB", os.path.join(os.path.dirname(__file__), "rio_memory.db"))
CACHE_TTL = 24 * 3600  # 24h


def _conn():
    c = sqlite3.connect(DB_PATH)
    c.execute("PRAGMA journal_mode=WAL")
    return c


def init_db():
    with _conn() as c:
        c.executescript("""
        CREATE TABLE IF NOT EXISTS research_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts REAL, rtype TEXT, topic TEXT,
            quality REAL, n_facts INTEGER, report TEXT);
        CREATE TABLE IF NOT EXISTS evidence_cache(
            qhash TEXT PRIMARY KEY, query TEXT, payload TEXT, ts REAL);
        CREATE TABLE IF NOT EXISTS source_scores(
            domain TEXT PRIMARY KEY, hits INTEGER DEFAULT 0,
            ok INTEGER DEFAULT 0, score REAL DEFAULT 0.5);
        CREATE TABLE IF NOT EXISTS lessons(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts REAL, context TEXT, lesson TEXT);
        CREATE INDEX IF NOT EXISTS idx_hist_topic ON research_history(topic);
        """)


# ---------- research history ----------

def log_research(rtype, topic, quality, n_facts, report):
    with _conn() as c:
        c.execute(
            "INSERT INTO research_history(ts,rtype,topic,quality,n_facts,report) VALUES(?,?,?,?,?,?)",
            (time.time(), rtype, topic, quality, n_facts, report[:20000]))


def get_history(topic_like, limit=5):
    """Tìm research cũ liên quan — dùng cho /deep để không research lại từ đầu."""
    with _conn() as c:
        rows = c.execute(
            "SELECT ts,rtype,topic,quality,report FROM research_history "
            "WHERE topic LIKE ? ORDER BY ts DESC LIMIT ?",
            (f"%{topic_like}%", limit)).fetchall()
    return [{"ts": r[0], "rtype": r[1], "topic": r[2], "quality": r[3], "report": r[4]} for r in rows]


# ---------- evidence cache ----------

def _qhash(query):
    return hashlib.sha256(query.lower().strip().encode()).hexdigest()[:16]


def cache_get(query):
    with _conn() as c:
        row = c.execute("SELECT payload, ts FROM evidence_cache WHERE qhash=?",
                        (_qhash(query),)).fetchone()
    if row and (time.time() - row[1]) < CACHE_TTL:
        return json.loads(row[0])
    return None


def cache_set(query, payload):
    with _conn() as c:
        c.execute("INSERT OR REPLACE INTO evidence_cache(qhash,query,payload,ts) VALUES(?,?,?,?)",
                  (_qhash(query), query, json.dumps(payload, ensure_ascii=False), time.time()))


# ---------- source reliability ----------

def bump_source(domain, ok=True):
    """Gọi mỗi lần dùng 1 nguồn. ok=False khi nguồn cho data mâu thuẫn/rác."""
    with _conn() as c:
        c.execute("INSERT OR IGNORE INTO source_scores(domain) VALUES(?)", (domain,))
        c.execute("UPDATE source_scores SET hits=hits+1, ok=ok+? WHERE domain=?",
                  (1 if ok else 0, domain))
        c.execute("UPDATE source_scores SET score = CAST(ok AS REAL)/hits WHERE domain=? AND hits>0",
                  (domain,))


def source_score(domain):
    with _conn() as c:
        row = c.execute("SELECT score, hits FROM source_scores WHERE domain=?", (domain,)).fetchone()
    if not row or row[1] < 3:  # chưa đủ mẫu → neutral
        return 0.5
    return row[0]


# ---------- lessons ----------

def log_lesson(context, lesson):
    with _conn() as c:
        c.execute("INSERT INTO lessons(ts,context,lesson) VALUES(?,?,?)",
                  (time.time(), context, lesson))


def retrieve_lessons(limit=10):
    with _conn() as c:
        rows = c.execute("SELECT ts,context,lesson FROM lessons ORDER BY ts DESC LIMIT ?",
                         (limit,)).fetchall()
    return [{"ts": r[0], "context": r[1], "lesson": r[2]} for r in rows]


init_db()
