/**
 * scrape_long_url.js
 * ==================
 * OpenClaw dùng script này để cào URL dài.
 * Gọi Crawl4AI self-hosted (Antigravity đã deploy Docker).
 * Không tốn credit, không giới hạn.
 *
 * SETUP:
 *   Antigravity chạy: docker run -d -p 11235:11235 unclecode/crawl4ai:latest
 *   node scrape_long_url.js "https://100xtourism.com/lp-7ngay.html"
 *
 * FALLBACK: Nếu chưa có Crawl4AI, dùng Firecrawl API (cần key)
 */

const CRAWL4AI_URL = process.env.CRAWL4AI_URL || "http://localhost:11235";
const FIRECRAWL_KEY = process.env.FIRECRAWL_API_KEY || "";

/**
 * Scrape bằng Crawl4AI self-hosted
 * Ưu tiên dùng cái này — free unlimited
 */
async function scrapeWithCrawl4AI(url) {
  const payload = {
    urls: [url],
    crawler_params: {
      headless: true,
      verbose: false,
      wait_for: "body",
      page_timeout: 30000,
    },
    extra: {
      word_count_threshold: 10,
      only_text: false,
    },
  };

  const resp = await fetch(`${CRAWL4AI_URL}/crawl`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(payload),
  });

  if (!resp.ok) {
    throw new Error(`Crawl4AI HTTP ${resp.status}: ${await resp.text()}`);
  }

  const data = await resp.json();

  if (data.results && data.results[0]) {
    return {
      markdown: data.results[0].markdown?.raw_markdown || "",
      html: data.results[0].html || "",
      metadata: data.results[0].metadata || {},
      source: "crawl4ai",
    };
  }

  throw new Error("Crawl4AI: không có kết quả");
}

/**
 * Fallback: Firecrawl API
 * Dùng khi Crawl4AI chưa setup
 */
async function scrapeWithFirecrawl(url, apiKey) {
  const payload = {
    url,
    formats: ["markdown"],
    onlyMainContent: true,
    waitFor: 2000,
    timeout: 30000,
  };

  const resp = await fetch("https://api.firecrawl.dev/v1/scrape", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
  });

  if (!resp.ok) {
    throw new Error(`Firecrawl HTTP ${resp.status}: ${await resp.text()}`);
  }

  const data = await resp.json();

  if (data.success) {
    return {
      markdown: data.data.markdown || "",
      metadata: data.data.metadata || {},
      source: "firecrawl",
    };
  }

  throw new Error(`Firecrawl error: ${JSON.stringify(data)}`);
}

/**
 * Main function — tự chọn engine
 * Thử Crawl4AI trước, fallback sang Firecrawl
 */
async function scrape(url) {
  console.log(`[INFO] Scraping: ${url.substring(0, 80)}...`);

  // Thử Crawl4AI trước (free)
  try {
    const result = await scrapeWithCrawl4AI(url);
    console.log(`[OK] Crawl4AI — ${result.markdown.length} chars`);
    return result;
  } catch (e) {
    console.warn(`[WARN] Crawl4AI failed: ${e.message}`);
  }

  // Fallback Firecrawl
  if (FIRECRAWL_KEY) {
    try {
      const result = await scrapeWithFirecrawl(url, FIRECRAWL_KEY);
      console.log(`[OK] Firecrawl — ${result.markdown.length} chars`);
      return result;
    } catch (e) {
      console.error(`[ERROR] Firecrawl failed: ${e.message}`);
    }
  }

  throw new Error("Cả 2 engine đều fail. Check Crawl4AI Docker hoặc FIRECRAWL_API_KEY.");
}

// CLI entry point
const url = process.argv[2] || "https://100xtourism.com/lp-7ngay.html";

scrape(url)
  .then((result) => {
    console.log("\n=== METADATA ===");
    console.log(JSON.stringify(result.metadata, null, 2));
    console.log("\n=== MARKDOWN (5000 chars) ===");
    console.log(result.markdown.substring(0, 5000));
    if (result.markdown.length > 5000) {
      console.log(`\n... (còn ${result.markdown.length - 5000} chars)`);
    }
  })
  .catch((err) => {
    console.error("[FATAL]", err.message);
    process.exit(1);
  });

// Export cho OpenClaw import
module.exports = { scrape, scrapeWithCrawl4AI, scrapeWithFirecrawl };
