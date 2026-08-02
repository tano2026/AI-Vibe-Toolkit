---
name: remotion-template-factory
description: >
  Use case: dựng sẵn bộ template video bằng Remotion, sau đó chỉ cần nhét text/data vào
  là tool tự render ra video MP4 — không cần mở lại timeline editor mỗi lần làm video mới.
---

# Remotion Template Factory — Nhét Text Vào, Ra Video Tự Động

## TL;DR
Thay vì mở Premiere/CapCut dựng từng video, mày build sẵn 1-2 template Remotion (React component nhận props), rồi viết 1 layer nhỏ nhận input text/data → nhồi vào props → gọi lệnh render → ra MP4. Xong 1 lần, dùng lại vô hạn cho content factory (Trùm Sân Bay, GMSP, ABTRIP...).

---

## Các tool trong stack

1. **Remotion** (đã có trong kho: `repos/remotion.md`, `skills/remotion-skill.md`) → engine render — viết video bằng React component, Remotion render từng frame ra ảnh rồi ghép MP4 thật.
2. **JSON/text input layer** → nơi mày định nghĩa nội dung động (title, script, số liệu, ảnh) dưới dạng object JSON, KHÔNG cần biết code để đổi nội dung.
3. **CLI hoặc Node.js render script** (`remotion render` / `renderMedia()`) → tool tự động chạy render, không cần mở Studio.
4. **(Tuỳ chọn) Claude/GPT làm layer sinh nội dung** → nếu muốn full auto, LLM sinh JSON props từ 1 câu lệnh text, script tự bơm vào template render luôn — đây chính là cách trong video TikTok mày gửi.

---

## Workflow ghép nối

```
[Input text/topic]
      ↓ (LLM sinh JSON props theo schema template, hoặc user tự điền JSON)
[props.json]
      ↓ (npx remotion render / renderMedia() nhận inputProps)
[Remotion render engine đọc React template + props]
      ↓
[Video MP4 ra lò]
```

**Bước cụ thể:**

1. Scaffold project 1 lần:
   ```bash
   npx create-video@latest my-video
   cd my-video && npm install
   ```

2. Viết 1-2 template component nhận props (không hardcode nội dung), ví dụ:
   ```tsx
   // Composition.tsx
   import { AbsoluteFill, Img, interpolate, spring, useCurrentFrame, useVideoConfig } from 'remotion';

   type Props = { title: string; subtitle: string; logo: string };

   export const MyTemplate: React.FC<Props> = ({ title, subtitle, logo }) => {
     const frame = useCurrentFrame();
     const { fps } = useVideoConfig();
     const scale = spring({ fps, frame, config: { damping: 200 } });
     return (
       <AbsoluteFill style={{ backgroundColor: '#0b0b0f' }}>
         <Img src={logo} style={{ transform: `scale(${scale})` }} />
         <h1>{title}</h1>
         <h2>{subtitle}</h2>
       </AbsoluteFill>
     );
   };
   ```

3. Test render bằng tay với props JSON:
   ```bash
   npx remotion render src/index.ts MyTemplate out/video.mp4 \
     --props='{"title":"Fast Track Nội Bài","subtitle":"Đặt SIM du lịch trong 2 phút","logo":"https://abtrip.vn/logo.png"}'
   ```

4. Đóng gói thành script tự động — 1 file Node nhận text đầu vào, gọi LLM (qua OmniRoute) để sinh JSON props đúng schema, rồi gọi `renderMedia()` từ `@remotion/renderer` để render server-side, không cần mở CLI thủ công:
   ```js
   const { renderMedia, selectComposition } = require('@remotion/renderer');
   const { bundle } = require('@remotion/bundler');

   async function renderFromText(inputText) {
     const props = await genPropsFromText(inputText); // gọi LLM sinh JSON theo schema
     const bundled = await bundle('./src/index.ts');
     const composition = await selectComposition({ serveUrl: bundled, id: 'MyTemplate', inputProps: props });
     await renderMedia({
       composition,
       serveUrl: bundled,
       codec: 'h264',
       outputLocation: `out/${Date.now()}.mp4`,
       inputProps: props,
     });
   }
   ```

5. Nối vào pipeline agent (Hermes/OpenClaw) → agent gọi hàm `renderFromText()` mỗi khi có nội dung mới cần ra video, không cần người mở máy dựng thủ công.

---

## Ví dụ thực tế

Case cho Trùm Sân Bay TikTok: mỗi lần có 1 tin tức/tip mới về Fast Track Nội Bài, thay vì dựng CapCut thủ công:
- Agent Writer sinh script text (đã có trong pipeline 9-agent).
- Text này được đẩy qua layer "genPropsFromText" → LLM tách ra title/subtitle/3 bullet point/số liệu.
- `renderFromText()` render ra video 15s theo đúng template brand đã set sẵn (logo, font, màu Tano).
- Video ra thẳng `/out`, agent Publisher lấy file này đăng luôn.

So với quay dựng tay: từ ~30-45 phút/video xuống còn thời gian render (~10-30s cho video ngắn) + thời gian LLM sinh props (~5-10s).

---

## Lưu ý / Lỗi thường gặp

- **License Remotion** — free cho cá nhân/dự án nhỏ, công ty 4+ người phải mua commercial license. Đã note trong kho (`repos/remotion.md`), kiểm tra lại trước khi scale sản xuất hàng loạt cho ABTRIP/Wonder Mart.
- **Props phải serializable JSON** — không nhét function, class instance vào props, chỉ string/number/array/object thuần.
- **LLM sinh JSON sai schema** → dùng `zod` validate props trước khi render, tránh render lỗi giữa chừng tốn compute.
- **Render nhiều video cùng lúc** — Remotion khuyến cáo không render song song nhiều video trên cùng máy vì ăn hết resource; nếu cần scale, deploy Remotion Lambda thay vì chạy local trên VPS chung với 3 agent khác (đúng cảnh báo RAM contention đã ghi trong kho).
- **Ảnh/asset dùng URL, không dùng file local** khi định deploy render thành service — asset phải public URL để renderer container đọc được.

---

## Đánh giá cá nhân

- **Điểm mạnh:** Làm 1 lần template, tái sử dụng vô hạn — đúng bài cho content factory cần ra video đều đặn (Trùm Sân Bay, GMSP). Version-control được video (component là code, review qua Git). Tách biệt hoàn toàn phần "nội dung" (JSON) khỏi phần "thiết kế" (component) — người không biết code vẫn đổi được nội dung.
- **Điểm yếu:** Setup ban đầu tốn thời gian hơn hẳn so với mở CapCut kéo thả — cần biết React cơ bản để viết template đầu tiên. Animation phức tạp (transition đẹp, motion graphic cầu kỳ) code React tay sẽ chậm hơn kéo thả trong tool chuyên video editing. Không hợp cho video cần edit "tay" nhiều (cắt cảnh linh hoạt theo raw footage) — hợp nhất cho video dạng template lặp lại (stat card, quote card, intro/outro, data visualization).
- **Có nên dùng: 8/10** — cực kỳ đáng đầu tư nếu content factory cần ra nhiều video cùng 1 format lặp lại; không đáng nếu chỉ làm vài video một lần rồi thôi.

---

## Link
- Repo Remotion: `repos/remotion.md`, `repos/remotion-superpowers.md`
- Skill sẵn có: `skills/remotion-skill.md`, `skills/remotion-skill/`, `skills/ecc-remotion-video-creation`
- Docs props: https://www.remotion.dev/docs/passing-props
- Docs render từ dataset: https://www.remotion.dev/docs/dataset-render
- Template gốc dạng prompt-to-video: https://github.com/remotion-dev/template-prompt-to-video

---

## 🤖 Agent Integration

### Hermes (Python)
```python
# Hermes gọi render service (Node) qua subprocess hoặc HTTP nếu đóng gói thành API riêng
import subprocess, json

def render_video_from_props(props: dict, output_path: str):
    props_json = json.dumps(props)
    subprocess.run([
        "npx", "remotion", "render", "src/index.ts", "MyTemplate", output_path,
        f"--props={props_json}"
    ], check=True, cwd="/path/to/remotion-project")
```

### OpenClaw
```bash
# Cài template project 1 lần trên VPS
npx create-video@latest content-templates
cd content-templates && npm install
# Sau đó gọi render qua script wrapper (renderFromText.js) mỗi khi có content mới
node renderFromText.js "Nội dung text cần render"
```

### Antigravity
```bash
# Nếu scale lên nhiều video/ngày, cân nhắc deploy Remotion Lambda thay vì render local trên VPS
# tránh RAM contention với 3 agent hiện tại (đã cảnh báo trong kho)
npx remotion lambda functions deploy
npx remotion lambda sites create src/index.ts
```
> ⚠️ Kiểm tra Remotion commercial license trước khi scale sản xuất hàng loạt cho khách B2B (ABTRIP).
