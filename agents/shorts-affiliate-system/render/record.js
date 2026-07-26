/**
 * record.js
 * Dùng Playwright quay lại render.html thành video WebM, ở đúng viewport 16:9 hoặc 9:16.
 * Gọi cho mỗi định dạng riêng (2 lần chạy cho 1 storyboard: 16x9 và 9x16).
 *
 * Cài: npm install playwright && npx playwright install chromium
 * Chạy: node record.js --input render_16x9.html --output scenes_16x9.webm --width 1920 --height 1080 --duration 28
 */
const { chromium } = require("playwright");
const path = require("path");

function parseArgs() {
  const args = {};
  process.argv.slice(2).forEach((arg, i, arr) => {
    if (arg.startsWith("--")) args[arg.slice(2)] = arr[i + 1];
  });
  return args;
}

(async () => {
  const { input, output, width = 1920, height = 1080, duration = 30 } = parseArgs();
  if (!input || !output) {
    console.error("Thiếu --input hoặc --output");
    process.exit(1);
  }

  const outDir = path.dirname(output);
  const browser = await chromium.launch();
  const context = await browser.newContext({
    viewport: { width: Number(width), height: Number(height) },
    recordVideo: { dir: outDir, size: { width: Number(width), height: Number(height) } },
  });
  const page = await context.newPage();

  await page.goto(`file://${path.resolve(input)}`);
  // Đợi đúng tổng duration của storyboard để quay hết toàn bộ scene transitions
  await page.waitForTimeout(Number(duration) * 1000);

  await context.close();
  await browser.close();

  console.log(`Đã ghi video vào thư mục: ${outDir} (đổi tên file .webm thành ${output} nếu cần)`);
})();
