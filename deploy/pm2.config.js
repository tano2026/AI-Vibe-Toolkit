// PM2 Ecosystem Config
// Chạy: pm2 start pm2.config.js
// Monitor: pm2 status | pm2 logs | pm2 monit

require('dotenv').config({ path: `${process.env.HOME}/ai-vibe-toolkit/.env` });

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
