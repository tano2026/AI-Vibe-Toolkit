"""
research_agent.py
=================
Agent #1 trong SMB AI Team — Research & Data Intelligence
Nhiệm vụ: Nhận câu hỏi → fetch data thật → trả Markdown report chuẩn
Được gọi bởi: Orchestrator, Nobitano qua Telegram, agents khác trong team

CHẠY:
  python3 research_agent.py "Pain points của công ty du lịch SMB Việt Nam"
  python3 research_agent.py "Phân tích landing page https://100xtourism.com/lp-7ngay.html"
  python3 research_agent.py "Đối thủ cạnh tranh của ABTRIP travel"

OUTPUT: Markdown report — lưu vào /tmp/research_output.md + in ra stdout
"""

import urllib.request
import urllib.parse
import json
import sys
import os
import time
from datetime import datetime

# ============================================================
# CONFIG
# ============================================================
FIRECRAWL_KEY = os.environ.get("FIRECRAWL_API_KEY", "")
DEEPSEEK_KEY  = os.environ.get("DEEPSEEK_API_KEY", "")
OUTPUT_FILE   = "/tmp/research_output.md"

# ============================================================
# LAYER 1: DATA COLLECTORS (Tầng Tay)
# ============================================================

def search_duckduckgo(query: str, max_results: int = 8) -> list:
    """Search DuckDuckGo — free, không cần key"""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://api.duckduckgo.com/?q={encoded}&format=json&no_redirect=1&no_html=1"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        results = []
        # Abstract (summary)
        if data.get("Abstract"):
            results.append({
                "title": data.get("Heading", ""),
                "snippet": data["Abstract"],
                "url": data.get("AbstractURL", ""),
                "source": "duckduckgo_abstract"
            })
        # Related topics
        for topic in data.get("RelatedTopics", [])[:max_results]:
            if isinstance(topic, dict) and topic.get("Text"):
                results.append({
                    "title": topic.get("Text", "")[:100],
                    "snippet": topic.get("Text", ""),
                    "url": topic.get("FirstURL", ""),
                    "source": "duckduckgo_related"
                })
        return results
    except Exception as e:
        return [{"error": str(e), "source": "duckduckgo"}]


def search_google_news_rss(query: str, max_results: int = 5) -> list:
    """Google News RSS — free, không cần key"""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://news.google.com/rss/search?q={encoded}&hl=vi&gl=VN&ceid=VN:vi"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req, timeout=10).read().decode("utf-8")
        # Parse RSS thủ công (không dùng xml lib)
        import re
        items = re.findall(r"<item>(.*?)</item>", content, re.DOTALL)
        results = []
        for item in items[:max_results]:
            title = re.search(r"<title>(.*?)</title>", item)
            link  = re.search(r"<link>(.*?)</link>", item)
            desc  = re.search(r"<description>(.*?)</description>", item)
            results.append({
                "title": title.group(1).strip() if title else "",
                "url": link.group(1).strip() if link else "",
                "snippet": re.sub(r"<[^>]+>", "", desc.group(1)) if desc else "",
                "source": "google_news"
            })
        return results
    except Exception as e:
        return [{"error": str(e), "source": "google_news"}]


def search_reddit(query: str, max_results: int = 5) -> list:
    """Reddit JSON search — free"""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://www.reddit.com/search.json?q={encoded}&sort=relevance&limit={max_results}"
        req = urllib.request.Request(url, headers={"User-Agent": "research-agent/1.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        results = []
        for post in data.get("data", {}).get("children", []):
            p = post.get("data", {})
            results.append({
                "title": p.get("title", ""),
                "snippet": p.get("selftext", "")[:300],
                "url": f"https://reddit.com{p.get('permalink', '')}",
                "score": p.get("score", 0),
                "source": "reddit"
            })
        return results
    except Exception as e:
        return [{"error": str(e), "source": "reddit"}]


def fetch_wikipedia(query: str) -> dict:
    """Wikipedia summary — background context"""
    try:
        encoded = urllib.parse.quote(query)
        url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded}"
        req = urllib.request.Request(url, headers={"User-Agent": "research-agent/1.0"})
        data = json.loads(urllib.request.urlopen(req, timeout=10).read())
        return {
            "title": data.get("title", ""),
            "summary": data.get("extract", ""),
            "url": data.get("content_urls", {}).get("desktop", {}).get("page", ""),
            "source": "wikipedia"
        }
    except Exception as e:
        return {"error": str(e), "source": "wikipedia"}


def scrape_url(url: str) -> str:
    """
    Scrape URL bất kỳ → Markdown sạch.
    Dùng Firecrawl nếu có key, fallback urllib nếu không.
    """
    if FIRECRAWL_KEY:
        try:
            payload = json.dumps({
                "url": url,
                "formats": ["markdown"],
                "onlyMainContent": True,
                "waitFor": 2000,
                "timeout": 30000,
            }).encode()
            req = urllib.request.Request(
                "https://api.firecrawl.dev/v1/scrape",
                data=payload,
                headers={
                    "Authorization": f"Bearer {FIRECRAWL_KEY}",
                    "Content-Type": "application/json"
                }
            )
            result = json.loads(urllib.request.urlopen(req, timeout=35).read())
            if result.get("success"):
                return result["data"]["markdown"][:8000]
        except Exception as e:
            pass  # Fallback bên dưới

    # Fallback: urllib đơn giản
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        content = urllib.request.urlopen(req, timeout=15).read().decode("utf-8", errors="ignore")
        # Strip HTML tags thô
        import re
        text = re.sub(r"<[^>]+>", " ", content)
        text = re.sub(r"\s+", " ", text).strip()
        return text[:6000]
    except Exception as e:
        return f"[SCRAPE ERROR] {e}"


# ============================================================
# LAYER 2: VALIDATOR (Tầng Não — source-evaluation)
# ============================================================

def evaluate_sources(results: list) -> list:
    """
    Chấm điểm tin cậy cho từng source.
    Loại bỏ kết quả rác trước khi đưa vào LLM.
    """
    scored = []
    for r in results:
        if "error" in r:
            continue
        score = 0
        snippet = r.get("snippet", "") + r.get("title", "")
        # Có URL thật
        if r.get("url", "").startswith("http"):
            score += 2
        # Có nội dung đủ dài
        if len(snippet) > 100:
            score += 2
        # Nguồn uy tín hơn
        url = r.get("url", "")
        if any(d in url for d in ["wikipedia", "reuters", "vnexpress", "cafef", "gov.vn"]):
            score += 3
        # Reddit — community insight
        if r.get("source") == "reddit" and r.get("score", 0) > 10:
            score += 1
        r["trust_score"] = score
        if score >= 2:
            scored.append(r)

    # Sort theo trust score
    return sorted(scored, key=lambda x: x.get("trust_score", 0), reverse=True)


# ============================================================
# LAYER 3: SYNTHESIZER — gọi LLM để tổng hợp
# ============================================================

def synthesize_with_deepseek(query: str, data_context: str) -> str:
    """
    Gọi DeepSeek V3 để tổng hợp data thành report.
    Fallback: trả raw data nếu không có key.
    """
    if not DEEPSEEK_KEY:
        # Không có LLM — trả structured raw data
        return f"# Research Report (Raw)\n\n**Query:** {query}\n\n{data_context}"

    system_prompt = """Mày là Research Pro — analyst cấp cao trong AI agency.
Nhiệm vụ: Tổng hợp data đã thu thập thành báo cáo Markdown chuẩn.

NGUYÊN TẮC BẮT BUỘC:
1. Mọi số liệu PHẢI có nguồn (URL hoặc tên nguồn)
2. Nếu không có data thật → nói rõ "Chưa tìm được data, cần research thêm"
3. Không bịa số, không hallucinate
4. Output phải agents khác đọc được ngay — cấu trúc rõ ràng
5. Kết thúc bằng section "## Khuyến nghị tiếp theo" — 3 action items cụ thể

OUTPUT FORMAT:
# [Tên báo cáo]
**Ngày:** [date] | **Query:** [query]

## Tóm tắt (TL;DR)
[3-5 bullet points chính]

## Data & Insights
[Phân tích có nguồn]

## Cơ hội / Rủi ro
[Dựa trên data tìm được]

## Khuyến nghị tiếp theo
1. ...
2. ...
3. ...

---
*Sources: [list URLs]*"""

    payload = json.dumps({
        "model": "deepseek-chat",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Query: {query}\n\nData thu thập được:\n{data_context}"}
        ],
        "max_tokens": 2000,
        "temperature": 0.3,
    }).encode()

    try:
        req = urllib.request.Request(
            "https://api.deepseek.com/v1/chat/completions",
            data=payload,
            headers={
                "Authorization": f"Bearer {DEEPSEEK_KEY}",
                "Content-Type": "application/json"
            }
        )
        result = json.loads(urllib.request.urlopen(req, timeout=60).read())
        return result["choices"][0]["message"]["content"]
    except Exception as e:
        return f"[LLM ERROR] {e}\n\nRaw data:\n{data_context}"


# ============================================================
# MAIN ORCHESTRATOR
# ============================================================

def research(query: str) -> str:
    """
    Main flow: query → collect → validate → synthesize → report
    """
    print(f"[Research Pro] Query: {query[:80]}...")
    print("[1/4] Collecting data...")

    all_results = []

    # Detect nếu query là URL → scrape trực tiếp
    if query.strip().startswith("http"):
        url = query.strip().split(" ")[0]
        content = scrape_url(url)
        # Lấy phần text query còn lại (nếu có)
        extra = query.replace(url, "").strip()
        data_context = f"## Scraped content từ {url}\n\n{content}"
        if extra:
            data_context += f"\n\n**Yêu cầu phân tích:** {extra}"
        report = synthesize_with_deepseek(query, data_context)
    else:
        # Search đa nguồn song song (sequential vì không có asyncio)
        time.sleep(0.3)
        ddg = search_duckduckgo(query, 6)
        all_results.extend(ddg)

        time.sleep(0.3)
        news = search_google_news_rss(query, 5)
        all_results.extend(news)

        time.sleep(0.3)
        wiki = fetch_wikipedia(query)
        if not "error" in wiki:
            all_results.append(wiki)

        # Reddit cho community insights (optional)
        if any(kw in query.lower() for kw in ["pain", "problem", "khó khăn", "review", "compare"]):
            time.sleep(0.3)
            reddit = search_reddit(query + " Vietnam", 3)
            all_results.extend(reddit)

        print(f"[2/4] Collected {len(all_results)} raw results")

        # Validate
        validated = evaluate_sources(all_results)
        print(f"[3/4] Validated: {len(validated)} trusted sources")

        # Build context cho LLM
        context_parts = []
        for i, r in enumerate(validated[:10], 1):
            context_parts.append(
                f"### Source {i} [{r['source']}] (trust: {r.get('trust_score', 0)})\n"
                f"**Title:** {r.get('title', '')}\n"
                f"**URL:** {r.get('url', '')}\n"
                f"**Content:** {r.get('snippet', r.get('summary', ''))[:500]}\n"
            )
        data_context = "\n".join(context_parts)

        print("[4/4] Synthesizing report...")
        report = synthesize_with_deepseek(query, data_context)

    # Thêm metadata
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    final_report = f"{report}\n\n---\n*Generated by Research Pro | {timestamp}*"

    # Lưu file
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(final_report)
    print(f"[Done] Report saved to {OUTPUT_FILE}")

    return final_report


# ============================================================
# ENTRY POINTS
# ============================================================

def handle_telegram_command(text: str) -> str:
    """
    OpenClaw gọi function này khi nhận lệnh Telegram.
    Ví dụ: /research pain points công ty du lịch VN
    """
    query = text.replace("/research", "").strip()
    if not query:
        return "Usage: /research [câu hỏi hoặc URL cần research]"
    return research(query)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 research_agent.py 'query hoặc URL'")
        print("Examples:")
        print("  python3 research_agent.py 'Pain points công ty du lịch SMB VN'")
        print("  python3 research_agent.py 'https://100xtourism.com/lp-7ngay.html Phân tích landing page'")
        sys.exit(1)

    query = " ".join(sys.argv[1:])
    report = research(query)
    print("\n" + "="*60)
    print(report)
