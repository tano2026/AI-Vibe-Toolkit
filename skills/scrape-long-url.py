"""
scrape_long_url.py
==================
Hermes dùng script này để cào URL dài (landing page, sales page, etc.)
Gọi Firecrawl API — không cần MCP, không cần VPS, không bị giới hạn độ dài URL.

SETUP:
  export FIRECRAWL_API_KEY="fc-xxxx"   # lấy free tại firecrawl.dev
  python3 scrape_long_url.py "https://100xtourism.com/lp-7ngay.html"

OUTPUT:
  In ra Markdown sạch của trang — AI đọc được ngay.
"""

import urllib.request
import urllib.parse
import json
import sys
import os


FIRECRAWL_API = "https://api.firecrawl.dev/v1/scrape"


def scrape(url: str, api_key: str) -> str:
    """
    Scrape một URL bất kỳ, trả về Markdown sạch.
    Không giới hạn độ dài URL — Firecrawl xử lý hết.
    """
    payload = json.dumps({
        "url": url,
        "formats": ["markdown"],
        "onlyMainContent": True,     # bỏ header/footer/nav rác
        "waitFor": 2000,             # chờ JS render 2 giây (cho landing page)
        "timeout": 30000,
    }).encode("utf-8")

    req = urllib.request.Request(
        FIRECRAWL_API,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=35) as resp:
            result = json.loads(resp.read().decode("utf-8"))

        if result.get("success"):
            return result["data"]["markdown"]
        else:
            return f"[ERROR] Firecrawl trả về lỗi: {result}"

    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        return f"[HTTP ERROR {e.code}] {body}"
    except Exception as e:
        return f"[ERROR] {type(e).__name__}: {e}"


def scrape_with_meta(url: str, api_key: str) -> dict:
    """
    Scrape + trả về cả metadata (title, description, ogImage...)
    """
    payload = json.dumps({
        "url": url,
        "formats": ["markdown", "extract"],
        "onlyMainContent": True,
        "waitFor": 2000,
        "timeout": 30000,
        "extract": {
            "schema": {
                "type": "object",
                "properties": {
                    "title":       {"type": "string"},
                    "headline":    {"type": "string"},
                    "pain_points": {"type": "array", "items": {"type": "string"}},
                    "benefits":    {"type": "array", "items": {"type": "string"}},
                    "cta":         {"type": "string"},
                    "price":       {"type": "string"},
                }
            }
        }
    }).encode("utf-8")

    req = urllib.request.Request(
        FIRECRAWL_API,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=35) as resp:
            result = json.loads(resp.read().decode("utf-8"))

        if result.get("success"):
            return {
                "markdown": result["data"].get("markdown", ""),
                "metadata": result["data"].get("metadata", {}),
                "extract":  result["data"].get("extract", {}),
            }
        else:
            return {"error": result}

    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    # Lấy URL từ arg hoặc dùng URL mặc định để test
    url = sys.argv[1] if len(sys.argv) > 1 else "https://100xtourism.com/lp-7ngay.html"
    api_key = os.environ.get("FIRECRAWL_API_KEY", "")

    if not api_key:
        print("[ERROR] Chưa set FIRECRAWL_API_KEY")
        print("Chạy: export FIRECRAWL_API_KEY='fc-xxxx'")
        sys.exit(1)

    print(f"[INFO] Đang cào: {url[:80]}...")
    print("-" * 60)

    # Mode 1: Chỉ lấy markdown
    # markdown = scrape(url, api_key)
    # print(markdown)

    # Mode 2: Lấy markdown + extract structured data
    result = scrape_with_meta(url, api_key)

    if "error" in result:
        print(f"[ERROR] {result['error']}")
    else:
        print("=== EXTRACT (structured) ===")
        print(json.dumps(result["extract"], ensure_ascii=False, indent=2))
        print()
        print("=== MARKDOWN (full content) ===")
        print(result["markdown"][:5000])  # in 5000 ký tự đầu
        if len(result["markdown"]) > 5000:
            print(f"\n... (còn {len(result['markdown']) - 5000} ký tự nữa)")
