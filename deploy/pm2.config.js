// PM2 Ecosystem Config
// Chạy: pm2 start pm2.config.js
// Monitor: pm2 status | pm2 logs | pm2 monit

// Đọc .env bằng mã thuần (fs) — KHÔNG dùng gói npm `dotenv` vì setup-vps.sh
// chỉ cài `python-dotenv`; require('dotenv') sẽ lỗi ngay khi `pm2 start`.
// Quy tắc giống dotenv: bỏ dòng trống/#, cho phép `export KEY=...`, bỏ cặp nháy
// bao ngoài, bỏ chú thích ` # ...` ở giá trị không nháy, KHÔNG ghi đè biến đã có.
function loadEnvFile(file) {
  let text;
  try {
    text = require('fs').readFileSync(file, 'utf8');
  } catch (e) {
    console.warn(`[pm2.config] Không đọc được ${file}: ${e.code || e.message}`);
    return;
  }
  for (const rawLine of text.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line || line.startsWith('#')) continue;
    const m = line.match(/^(?:export\s+)?([\w.-]+)\s*=\s*(.*)$/);
    if (!m) continue;
    const key = m[1];
    let val = m[2];
    const q = val[0];
    if ((q === '"' || q === "'") && val.lastIndexOf(q) > 0) {
      val = val.slice(1, val.lastIndexOf(q));
    } else {
      val = val.replace(/\s+#.*$/, '').trim();
    }
    if (process.env[key] === undefined) process.env[key] = val;
  }
}

loadEnvFile(`${process.env.HOME}/ai-vibe-toolkit/.env`);

module.exports = {
  apps: [
    // --------------------------------------------------------
    // OpenClaw Gateway — nhận lệnh từ Telegram
    // --------------------------------------------------------
    {
      name: 'openclaw',
      script: 'openclaw',
      args: 'start --detached',
      interpreter: 'none',
      cwd: `${process.env.HOME}/ai-vibe-toolkit`,
      env: {
        NODE_ENV: 'production',
        GITHUB_TOKEN: process.env.GITHUB_TOKEN,
        ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY,
        TELEGRAM_BOT_TOKEN: process.env.TELEGRAM_BOT_TOKEN,
        TELEGRAM_CHAT_ID: process.env.TELEGRAM_CHAT_ID,
      },
      // Restart nếu crash
      restart_delay: 5000,
      max_restarts: 10,
      autorestart: true,
      // Logs
      log_file: `${process.env.HOME}/logs/openclaw.log`,
      error_file: `${process.env.HOME}/logs/openclaw-error.log`,
      time: true,
    },

    // --------------------------------------------------------
    // Hermes Agent — brain xử lý tasks
    // --------------------------------------------------------
    {
      name: 'hermes',
      script: 'hermes',
      args: 'serve --port 4242',
      interpreter: 'none',
      cwd: `${process.env.HOME}/ai-vibe-toolkit`,
      env: {
        NODE_ENV: 'production',
        ANTHROPIC_API_KEY: process.env.ANTHROPIC_API_KEY,
        GITHUB_TOKEN: process.env.GITHUB_TOKEN,
      },
      restart_delay: 5000,
      max_restarts: 10,
      autorestart: true,
      log_file: `${process.env.HOME}/logs/hermes.log`,
      error_file: `${process.env.HOME}/logs/hermes-error.log`,
      time: true,
    },

    // --------------------------------------------------------
    // Kho Sync — tự động pull GitHub mỗi 6h
    // --------------------------------------------------------
    {
      name: 'kho-sync',
      script: `${process.env.HOME}/ai-vibe-toolkit/deploy/auto-sync.sh`,
      interpreter: 'bash',
      cron_restart: '0 */6 * * *',  // mỗi 6h
      autorestart: false,
      watch: false,
      log_file: `${process.env.HOME}/logs/kho-sync.log`,
      time: true,
    },
  ],
};
