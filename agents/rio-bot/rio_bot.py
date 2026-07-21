"""
rio_bot.py — RIO Bot Telegram entry point (v3.0 "Trùm Research")

Wire adapters vào RIOBrain, poll Telegram getUpdates (long-polling, zero webhook cần domain
public), dispatch 10 command. Chạy local Windows, zero API key bắt buộc — chỉ cần
TELEGRAM_BOT_TOKEN. OMNIROUTE_URL là optional (degrade êm nếu thiếu, theo ARCHITECTURE.md).

Chạy:
    set TELEGRAM_BOT_TOKEN=xxx
    set RIO_ALLOWED_CHAT_ID=xxx   (chỉ Nobitano dùng được, chặn chat lạ)
    python rio_bot.py

10 command:
    /market <topic>      — quy mô, CAGR, đối thủ, xu hướng
    /swot <topic>        — điểm mạnh/yếu/cơ hội/rủi ro
    /sentiment <topic>   — review, complaint, feedback
    /forecast <topic>    — dự báo, số liệu lịch sử
    /kpi <topic>         — benchmark ngành
    /deep <topic>        — research sâu tổng quát
    /domain <tên domain> <topic> — auto map theo business domain (abtrip/tano cafe/wonder mart/gmsp)
    /cn <platform> <topic>       — kèm xu hướng mạng xã hội TQ (nếu adapter cn có)
    /history <topic>     — tra lịch sử research cũ về topic này (không research lại)
    /help                — liệt kê command
"""
import os
import time
import traceback
import urllib.request
import urllib.parse
import json

import memory
import ratelimit
import web_search
from brain import RIOBrain, resolve_rtype, SUBQ_TEMPLATES

BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN", "")
ALLOWED_CHAT_ID = os.environ.get("RIO_ALLOWED_CHAT_ID", "")  # rỗng = không lọc (chỉ nên để rỗng lúc test local)
API = f"https://api.telegram.org/bot{BOT_TOKEN}"

# search adapter được wrap ratelimit trước khi đưa vào brain — cache-first + backoff
web_search.search = ratelimit.throttled_search(web_search.search)

brain = RIOBrain(adapters={
    "search": web_search.search,
    # "cn": cn_trends.get_trends,        # bật khi có module cn_trends.py thật
    # "video": video_extract.extract,    # bật khi có module video_extract.py thật
    # "report": report_gen.format_report,# bật khi có module report_gen.py thật
})

HELP_TEXT = (
    "*RIO Bot — Research & Intelligence Officer v3.0*\n\n"
    "/market <chủ đề> — quy mô, CAGR, đối thủ, xu hướng\n"
    "/swot <chủ đề> — điểm mạnh/yếu/cơ hội/rủi ro\n"
    "/sentiment <chủ đề> — review, complaint, feedback\n"
    "/forecast <chủ đề> — dự báo, số liệu lịch sử\n"
    "/kpi <chủ đề> — benchmark ngành\n"
    "/deep <chủ đề> — research sâu tổng quát\n"
    "/domain <tên domain> <chủ đề> — tự map theo domain (abtrip/tano cafe/wonder mart/gmsp)\n"
    "/cn <platform> <chủ đề> — kèm xu hướng MXH Trung Quốc\n"
    "/history <chủ đề> — tra research cũ, không chạy lại\n"
    "/help — bảng lệnh này"
)


# ------------------------------------------------------------ Telegram thin client

def tg_call(method, **params):
    url = f"{API}/{method}"
    data = urllib.parse.urlencode(params).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode())


def send(chat_id, text):
    for chunk in [text] if len(text) <= 4000 else _chunk(text):
        try:
            tg_call("sendMessage", chat_id=chat_id, text=chunk, parse_mode="Markdown")
        except Exception:
            # Markdown parse lỗi (ký tự đặc biệt trong report) → gửi lại plain text
            tg_call("sendMessage", chat_id=chat_id, text=chunk)


def _chunk(text, limit=4000):
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


# ------------------------------------------------------------ command dispatch

def handle_command(chat_id, text):
    parts = text.strip().split(maxsplit=1)
    cmd = parts[0].lower()
    arg = parts[1].strip() if len(parts) > 1 else ""

    if cmd in ("/help", "/start"):
        send(chat_id, HELP_TEXT)
        return

    if cmd == "/history":
        if not arg:
            send(chat_id, "Dùng: /history <chủ đề>")
            return
        rows = memory.get_history(arg, limit=5)
        if not rows:
            send(chat_id, f"Chưa có research cũ nào về '{arg}'.")
            return
        lines = [f"📁 *{len(rows)} research cũ về '{arg}':*\n"]
        for r in rows:
            ts = time.strftime("%d/%m/%Y", time.localtime(r["ts"]))
            lines.append(f"• [{ts}] {r['rtype']} — chất lượng {r['quality']}")
        send(chat_id, "\n".join(lines))
        return

    if cmd == "/domain":
        dparts = arg.split(maxsplit=1)
        if len(dparts) < 2:
            send(chat_id, "Dùng: /domain <tên domain vd 'abtrip'> <chủ đề>")
            return
        domain_hint, topic = dparts[0], dparts[1]
        rtype = resolve_rtype(domain_hint)
        _run_research(chat_id, rtype, topic)
        return

    if cmd == "/cn":
        cparts = arg.split(maxsplit=1)
        if len(cparts) < 2:
            send(chat_id, "Dùng: /cn <platform> <chủ đề>")
            return
        platform, topic = cparts[0], cparts[1]
        _run_research(chat_id, "market", topic, cn_platform=platform)
        return

    rtype_map = {
        "/market": "market", "/swot": "swot", "/sentiment": "sentiment",
        "/forecast": "forecast", "/kpi": "kpi", "/deep": "deep",
    }
    if cmd in rtype_map:
        if not arg:
            send(chat_id, f"Dùng: {cmd} <chủ đề>")
            return
        _run_research(chat_id, rtype_map[cmd], arg)
        return

    send(chat_id, "Lệnh không nhận diện được. Gõ /help để xem danh sách lệnh.")


def _run_research(chat_id, rtype, topic, cn_platform=None):
    send(chat_id, f"🔍 Đang research *{rtype}*: {topic}...\n_(có thể mất 30-90s, tự đào sâu thêm nếu số liệu chưa đủ chắc)_")
    try:
        chunks = brain.run(rtype, topic, cn_platform=cn_platform)
        for c in chunks:
            send(chat_id, c)
    except Exception as e:
        memory.log_lesson("rio_bot_dispatch", f"{e} | {traceback.format_exc()[-500:]}")
        send(chat_id, f"⚠️ Research lỗi giữa chừng: {e}\nĐã ghi lesson vào memory để không lặp lại.")


# ------------------------------------------------------------ polling loop

def poll_forever():
    if not BOT_TOKEN:
        raise SystemExit("Thiếu TELEGRAM_BOT_TOKEN — set env var trước khi chạy.")
    print("RIO Bot v3.0 đang chạy — polling Telegram...")
    offset = 0
    while True:
        try:
            resp = tg_call("getUpdates", offset=offset, timeout=25)
            for update in resp.get("result", []):
                offset = update["update_id"] + 1
                msg = update.get("message") or {}
                chat_id = str(msg.get("chat", {}).get("id", ""))
                text = msg.get("text", "")
                if not text or not text.startswith("/"):
                    continue
                if ALLOWED_CHAT_ID and chat_id != ALLOWED_CHAT_ID:
                    continue  # chặn chat lạ, chỉ CEO dùng được
                handle_command(chat_id, text)
        except Exception as e:
            memory.log_lesson("rio_bot_poll", f"{e} | {traceback.format_exc()[-300:]}")
            time.sleep(5)  # tránh spam lỗi liên tục nếu mạng/Telegram API chập chờn


if __name__ == "__main__":
    poll_forever()
