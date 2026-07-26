---
name: web-app-dev
description: Build, serve, and debug web applications — Flask, React+Vite+Express, or any Node/frontend framework. Covers startup, port conflict resolution, health checks, and Gemini/API key integration.
tags: [flask, web-app, react, vite, express, nodejs, gemini, html-css, playwright, debug-mode, fullstack]
---

# Web App Development

Class-level guidelines for building, serving, and debugging web applications on this Hermes setup. Covers Flask (Python), React+Vite+Express (Node), and general full-stack patterns.

## Framework-Specific Sections

- [Flask Server Setup](#flask-server-setup)
- [React + Vite + Express Setup](#react--vite--express-setup)
- [General Startup Patterns](#general-startup-patterns)
- [Port Conflict Resolution](#port-conflict-resolution)
- [API Key Integration](#api-key-integration)
- [Health Checks & Verification](#health-checks--verification)
- [Common Pitfalls](#common-pitfalls)

### Reference Patterns
- **Translating a Chinese-Language SPA Bundle to Vietnamese** (`references/translate-chinese-spa-bundle.md`) — Technique for finding and replacing inline JS locale objects in monolithic 20-30MB index.html bundles (Vue/React). Covers detection of vue-i18n inline locale, brace-counting extraction, translation strategy, and pitfalls for large-file bundle patching.
- **Task Tracker with Anti-Cheat Time Windows** (`references/task-tracker-anti-cheat.md`) — Flask + SQLite app for child daily routines with time-window validation preventing "tick the whole week" cheating. Covers server-side validation, frontend UX disable, mandatory note modal, reward/penalty gamification, and Windows process management.
- **Multi-Route Architecture (Role-Based Views)** (`references/flask-multi-route-architecture.md`) — Flask app with separate routes for kids (single-user view, no tabs) and admin (dashboard with auth). Covers basic auth decorator, per-child theming, Nginx subpath JS base-path pattern, and admin API endpoints.

---

## Flask Server Setup

### Startup
- Run with `python app.py` (not `flask run`)
- Server binds to `0.0.0.0:5000` for LAN access

### Access
- Local: `http://127.0.0.1:5000`
- LAN: `http://<local-ip>:5000` (check with `ipconfig` on Windows)
- Firewall: ensure port 5000-5020 open via Windows Firewall

---

## React + Vite + Express Setup

For apps using Vite for frontend bundling + Express for backend API (common Gemini AI web app pattern).

### Prerequisites
- Node.js (check: `node -v`)
- `package.json` with `scripts.dev` = `"tsx server.ts"` (or similar)
- `.env` file with API keys in `KEY=VALUE` format

### Install & Start
```bash
cd /path/to/project
npm install            # install all deps
npm run dev            # starts Vite dev server + Express backend
```

### Integrating New Full-Stack Features (API + UI)

When adding a new feature that spans both frontend (React) and backend (Express) and involves external Node.js scripts or AI API calls, follow this systematic workflow:

1.  **Backend API Endpoint (server.ts):**
    *   Define a new `POST` or `GET` API endpoint in `server.ts` to handle the new feature's logic.
    *   Include necessary `import` statements at the top of `server.ts` for modules like `child_process` (for `exec` calls to external scripts) and `fs` (for file system operations).
    *   Implement the API logic: receive parameters from the frontend, call external Node.js scripts (e.g., `bazi-ziwei-engine/calculator/dist/run-chart.js`), process their output, use AI models (Gemini) for further analysis/generation, and return the structured result.
    *   **Pitfall: Missing `import` statements:** Ensure all required Node.js modules are imported at the top of `server.ts`. Failure to do so will result in runtime errors.
    *   **Pitfall: Pathing for external scripts:** When calling external Node.js scripts via `child_process.exec`, construct paths using `path.join(process.cwd(), "../<external_repo>/...")` to ensure correct relative path resolution from the current working directory of the `bikipkimco` server.
    *   **Pitfall: File `server.ts` missing/corrupted:** If `server.ts` is accidentally deleted or corrupted, it must be restored from version control (Git) or re-created manually based on known API endpoints and configurations. Refer to `windows-dev-workflow` for general file recovery tips on Windows.

2.  **Frontend UI (App.tsx / components):**
    *   **State Management:** Declare new `useState` variables in `App.tsx` (or a relevant component) to store user input (e.g., `birthYear`, `gender`) and the results from the new backend API (e.g., `horoscopeAnalysis`, `isAnalyzing`).
    *   **Input Fields:** Add `input` fields, `select` dropdowns, and `button` components to `App.tsx` (or a component) to allow users to provide input for the new feature.
    *   **API Call Function:** Create an asynchronous function (e.g., `handleAnalyzeHoroscope`) to make `fetch` requests to the new backend API endpoint. This function should manage loading states (`isAnalyzing`) and error handling.
    *   **Display Results:** Implement logic to display the results returned from the backend. This might involve conditional rendering (e.g., showing analysis if `horoscopeAnalysis` is not null) and rendering different formats (e.g., `dangerouslySetInnerHTML` for HTML output, plain text for Markdown).
    *   **Integration Point:** Integrate the new UI elements and API call function into an existing section of `App.tsx` (e.g., alongside other feature controls) or create a dedicated new component if the feature is substantial.

3.  **Restart Backend:** After making changes to `server.ts`, the Node.js application must be restarted for the new API endpoints and logic to take effect. If running in the background, `kill` the existing process and run `npm run dev` again.
    *   **Pitfall: Port Conflict (`EADDRINUSE`):** If the server fails to restart due to `EADDRINUSE`, another process is occupying the port. Refer to the `Port Conflicts (EADDRINUSE)` section in the `windows-dev-workflow` skill for steps to identify and terminate the offending process.

1.  **Backend API Endpoint (server.ts):**
    *   Define a new `POST` or `GET` API endpoint in `server.ts` to handle the new feature's logic.
    *   Include necessary `import` statements at the top of `server.ts` for modules like `child_process` (for `exec` calls to external scripts) and `fs` (for file system operations).
    *   Implement the API logic: receive parameters from the frontend, call external Node.js scripts (e.g., `bazi-ziwei-engine/calculator/dist/run-chart.js`), process their output, use AI models (Gemini) for further analysis/generation, and return the structured result.
    *   **Pitfall: Missing `import` statements:** Ensure all required Node.js modules are imported at the top of `server.ts`. Failure to do so will result in runtime errors.
    *   **Pitfall: Pathing for external scripts:** When calling external Node.js scripts via `child_process.exec`, construct paths using `path.join(process.cwd(), "../<external_repo>/...")` to ensure correct relative path resolution from the current working directory of the `bikipkimco` server.

2.  **Frontend UI (App.tsx / components):**
    *   **State Management:** Declare new `useState` variables in `App.tsx` (or a relevant component) to store user input (e.g., `birthYear`, `gender`) and the results from the new backend API (e.g., `horoscopeAnalysis`, `isAnalyzing`).
    *   **Input Fields:** Add `input` fields, `select` dropdowns, and `button` components to `App.tsx` (or a component) to allow users to provide input for the new feature.
    *   **API Call Function:** Create an asynchronous function (e.g., `handleAnalyzeHoroscope`) to make `fetch` requests to the new backend API endpoint. This function should manage loading states (`isAnalyzing`) and error handling.
    *   **Display Results:** Implement logic to display the results returned from the backend. This might involve conditional rendering (e.g., showing analysis if `horoscopeAnalysis` is not null) and rendering different formats (e.g., `dangerouslySetInnerHTML` for HTML output, plain text for Markdown).
    *   **Integration Point:** Integrate the new UI elements and API call function into an existing section of `App.tsx` (e.g., alongside other feature controls) or create a dedicated new component if the feature is substantial.

3.  **Restart Backend:** After making changes to `server.ts`, the Node.js application must be restarted for the new API endpoints and logic to take effect. If running in the background, `kill` the existing process and run `npm run dev` again.

4.  **Verification:** Test the new feature end-to-end: input data in the frontend, verify the API call is made, and confirm the correct results are displayed.
- Default: port **3000**
- Vite HMR WebSocket: port **24678**
- When 3000 is in use, change `const PORT = 3000` → `const PORT = 3001` in server.ts

---

## General Startup Patterns

### Background Process
```bash
# Example for Python/FastAPI on Windows with bash
source "/path/to/venv/Scripts/activate" && \
cd "/path/to/project/root" && \
python backend/main.py
```
- Run with `background=true` + `notify_on_complete=true`
- Wait a few seconds, then verify with health check

**Pitfall**: Hermes Agent cannot directly access local network addresses (e.g., `http://127.0.0.1:8000`) due to security policies. You must verify the application's functionality by accessing the URL from your local browser.

### Re-Starting After Error
1. Kill stale process on port (see Port Conflict)
2. Verify port is free: `netstat -ano | grep :PORT`
3. Start fresh with background mode

---

## Port Conflict Resolution

**Symptom:** `EADDRINUSE: address already in use 0.0.0.0:PORT`

### Step 1: Find the PID
```bash
netstat -ano | grep :PORT
# Output: TCP    0.0.0.0:PORT   0.0.0.0:0    LISTENING   PID
```

### Step 2: Kill by PID
```bash
# First try (may work)
kill -9 <PID>
# If that fails (orphan Windows process)
cmd.exe /c "taskkill /F /PID <PID>"
# Alternative
taskkill -f -pid <PID>  # via git-bash
```

### Step 3: Verify + Restart
```bash
netstat -ano | grep :PORT || echo "port PORT is free now"
```

### Step 4: If Can't Kill — Change Port
Some processes (system services, Vite HMR sockets on 24678, orphaned node daemons from other sessions) resist `kill`. When port 3000 won't free:
- Edit `const PORT = 3000;` → `const PORT = 3001;` in the server file
- Restart on the new port

---

## API Key Integration

### .env File Setup
```bash
# File: .env (in project root)
GEMINI_API_KEY=your_key_here
```

### Verification
After `npm run dev` starts, test the API endpoint:
```bash
curl -s http://localhost:PORT/ | head -5
# Should return HTML, not error
```

### Secret Handling
- `.env` is auto-secret-detected by Hermes `read_file` (returns "Access denied")
- Use terminal to verify existence: `ls -la .env` and `head -1 .env | sed 's/=.*/=***REDACTED***/'`
- Never expose full key values in response

---

## Health Checks & Verification

### HTTP Status Check
```bash
curl -s -o /dev/null -w "%{http_code}" http://localhost:PORT/
# Returns 200 = running
```

### Page Content Check
```bash
curl -s http://localhost:PORT/ | head -10
```

### API Endpoint Test
```bash
curl -s -X POST http://localhost:PORT/api/endpoint \
  -H "Content-Type: application/json" \
  -d '{"query": "test"}' | head -20
```

### Browser Verification
- Open `http://localhost:PORT` in browser
- Check for React dev tools / Vite HMR indicator
- Test UI interactions

---

## Common Pitfalls

### 1. CSS Variables Missing `:root` Declaration
**Symptom:** Page renders blank (white screen) on any browser.
**Cause:** CSS uses `var(--bg)` / `var(--text)` etc. without defining them in `:root {}`.
**Fix:** Always define before use:
```css
:root {
    --bg: #0a0a1a;
    --text: #e0e0e0;
    --primary: #667eea;
    --border: #333;
    --card-bg: #1a1a2e;
    --hover: rgba(255,255,255,0.05);
}
```

### 2. Flask Debug Mode + Playwright Conflict
**Symptom:** Server crashes when Playwright called; debug reloader forks cause browser context confusion.
**Fix:** `app.run(debug=True, use_reloader=False)` or run non-debug mode.

### 3. Duplicate Flask Route Definitions
**Symptom:** `AssertionError: View function mapping is overwriting...`
**Fix:** Rename function or use explicit `endpoint=` parameter.

### 4. Stale Port — EADDRINUSE
**Symptom:** `Error: listen EADDRINUSE: address already in use`
**Fix:** See [Port Conflict Resolution](#port-conflict-resolution) above.

### 5. TypeScript Lint Errors ≠ Runtime Failures
**Symptom:** `tsx server.ts` shows TS errors in node_modules but runs fine.
**Cause:** `tsx` (TypeScript runner) ignores type errors during execution. Only Vite build fails on TS errors. If `npm run dev` uses `tsx`, it runs regardless.
**Fix:** Ignore node_modules TS errors during dev; only fix source-file errors.

### 6. npm-run-dev Exits Immediately
**Symptom:** `npm run dev` exits with code 1 / 0 immediately.
**Cause:** Either port in use (check pitfall #4) or script runs `tsx server.ts` directly without Vite.
**Fix:** Use `background=true` and verify with health check. If `server.ts` integrates Vite (uses `createViteServer`), it becomes a long-lived dev server — run in background.

### 7. Stale Flask Process Serving Old Code (404 on New Routes)

**Symptom:** You added new routes to `app.py`, restart the Flask server, but new routes return 404.

**Root Cause 1 — old process still running:**
```
netstat -ano | grep 5000
# Multiple LISTENING PIDs = multiple Flask processes
```
The old process (loaded before your edit) is still handling requests. Kill ALL PIDs:
```bash
# Find all
netstat -ano | grep LISTENING | grep 5000
# Kill each
taskkill //F //PID 1234
# Verify
netstat -ano | grep LISTENING | grep 5000 || echo "port free"
```

**Root Cause 2 — wrong WorkingDirectory (VPS deploy):**
When deploying code via scp/tar to a NEW directory (e.g. `/home/ubuntu/thoigianbieu/`) but systemd service still points to OLD directory:
```
WorkingDirectory=/home/ubuntu/thoigianbieu-app  # ← old
```
Fix: copy files to the original directory OR update systemd service:
```bash
cp /new/path/app.py /old/path/app.py
sudo systemctl restart thoigianbieu
```
Or verify with `cat /etc/systemd/system/<service>.service | grep WorkingDirectory`.

**Prevention:**
- Before deploying: check `systemd service file` or `Dockerfile` for actual paths
- After copying: test locally on the server via curl localhost:PORT, not just via Nginx (to isolate Nginx vs Flask issues)
- Use `find . -type f` on the server to verify files landed correctly

### 8. WebSocket Server Error on Port 24678
**Symptom:** `WebSocket server error: Port 24678 is already in use`
**Cause:** Vite HMR WebSocket — orphan node process left it open.
**Fix:** Non-blocking error; Vite auto-retries. App functions normally. Only kills the process if port 3000 is also blocked.

## Frontend Architecture

### Single-File Approach (Flask)
- All HTML, CSS, and JS in one `templates/index.html` file
- Served via Flask's `render_template('index.html')`
- No static files directory needed initially

### React Component Architecture (Vite)
- `src/App.tsx` often contains full dashboard UI (can be 95KB+)
- Tailwind CSS + motion library common
- Vite HMR auto-reloads frontend changes

### Mobile Responsiveness
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
```
- Max-width on messages: 85% (90% on small screens)
- Use `flex-wrap: wrap` for form rows

### Subpath-Aware fetch() Pattern (Nginx Reverse Proxy)

When a Flask app is served behind Nginx at a subpath (e.g. `/thoigianbieu/`), the browser's JS `fetch()` calls must include the subpath prefix:

```javascript
// ❌ HARDCODED — breaks behind Nginx subpath
fetch('/api/today/' + userId)

// ✅ DYNAMIC — works everywhere
const base = window.location.pathname.replace(/\/+$/, '');
fetch(`${base}/api/today/${userId}`)
```

This pattern is mandatory for any Flask app deployed at a subpath. Never hardcode `/api/` paths in JS. See `references/flask-multi-route-architecture.md` for the full rationale.

## Watcher System Integration (Flask-specific)
When building a Flask app that includes a background watcher/scheduler:
- Watcher state must persist across server restarts (JSON files)
- Worker interval: 10+ minutes minimum to avoid rate limiting

## Date Format (Travel apps)
- API B2B uses `DDMMYYYY` (no separators)
- Frontend sends `YYYY-MM-DD` from `<input type="date">` — must convert on server side
- Display: `DD/MM` or `DD/MM/YYYY` for user-facing output
