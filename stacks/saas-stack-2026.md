# SaaS Stack 2026 — GitHub Repo / Infographic Series

## TL;DR
Bộ tổng hợp công nghệ đầy đủ nhất để build SaaS từ zero — cover Frontend, Backend, Database, Auth, Payments, Email, Storage, Deployment, Analytics, Monitoring và DevOps. Được thiết kế bởi cộng đồng dev Việt, format infographic tiếng Việt dễ hiểu.

## Stack này dùng để làm gì
Đây không phải 1 tool — đây là **bản đồ** giúp mày chọn đúng công nghệ cho từng tầng khi build SaaS. Thay vì mày phải Google "nên dùng auth gì", "payment nào tốt nhất" → bộ này đã curate sẵn lựa chọn tốt nhất theo từng category.

4 nhóm chính:
- **Core Stack** — nền tảng bắt buộc phải có (FE/BE/DB)
- **Product Essentials** — để product hoạt động & kiếm tiền (Auth/Payments/Email/Storage)
- **Scale & Infra** — để vận hành ổn định và mở rộng (Deploy/Analytics/Monitor/DevOps)

---

## Breakdown từng layer

### 🖥️ FRONTEND
| Tool | Role | Khi nào dùng |
|------|------|--------------|
| **React** | UI library | Base của mọi thứ, ecosystem lớn nhất |
| **Next.js** | React framework | SEO cần thiết, full-stack trong 1 project |
| **Vue** | Framework linh hoạt | Nhẹ hơn React, học nhanh hơn |
| **TailwindCSS** | CSS utility | Styling nhanh, không cần viết CSS thuần |
| **Shadcn UI** | Component library | Copy component đẹp vào project, không cài package |

### ⚙️ BACKEND
| Tool | Role | Khi nào dùng |
|------|------|--------------|
| **Node.js + Express** | JS runtime + framework | Nhanh, ecosystem npm khổng lồ |
| **FastAPI** | Python API | Cần tốc độ + auto docs + type safety |
| **Django** | Python full-stack | Cần admin panel, ORM mạnh |
| **Laravel** | PHP framework | Team quen PHP, rapid development |

### 🗄️ DATABASE
| Tool | Role | Khi nào dùng |
|------|------|--------------|
| **PostgreSQL** | SQL mạnh nhất | Default cho mọi production SaaS |
| **MySQL** | SQL phổ biến | Legacy project, hosting rẻ |
| **MongoDB** | NoSQL linh hoạt | Data schema thay đổi nhiều |
| **Redis** | In-memory cache | Session, cache, queue |
| **Supabase** | BaaS với Postgres | Không muốn setup DB từ đầu |

### 🔐 AUTH
| Tool | Khi nào dùng |
|------|--------------|
| **Clerk** | Best DX, UI đẹp, setup 5 phút — recommend nhất 2026 |
| **Supabase Auth** | Đã dùng Supabase DB rồi thì dùng luôn |
| **NextAuth** | Next.js project, cần custom nhiều |
| **Auth0** | Enterprise, cần compliance |
| **Firebase Auth** | Google ecosystem, mobile app |

### 💳 PAYMENTS
| Tool | Khi nào dùng |
|------|--------------|
| **Stripe** | Default global, hỗ trợ VN 2024+ |
| **Paddle** | Tự handle thuế, merchant of record |
| **Lemon Squeezy** | Digital products, indie dev, đơn giản hơn Stripe |
| **Polar** | Open-source, B2B subscriptions |

### 📧 EMAIL
| Tool | Khi nào dùng |
|------|--------------|
| **Resend** | Transactional email cho dev, DX tốt nhất |
| **SendGrid** | Volume lớn, marketing + transactional |
| **Postmark** | Deliverability cao nhất, transactional only |
| **Mailgun** | API mạnh, flexible |
| **Amazon SES** | Volume khủng, giá rẻ nhất |

### ☁️ STORAGE
| Tool | Khi nào dùng |
|------|--------------|
| **Cloudflare R2** | Rẻ nhất, no egress fee — recommend |
| **Supabase Storage** | Đã dùng Supabase rồi |
| **AWS S3** | Enterprise, ecosystem AWS |
| **Uploadcare** | Upload widget đẹp, transform ảnh |

### 🚀 DEPLOYMENT
| Tool | Khi nào dùng |
|------|--------------|
| **Vercel** | Next.js/frontend, zero-config, nhanh nhất |
| **Railway** | Full-stack, có DB luôn, DX tốt |
| **Render** | Background workers, cron jobs |
| **Netlify** | Static sites, edge functions |
| **AWS** | Enterprise, cần control toàn bộ |

### 📊 ANALYTICS
| Tool | Khi nào dùng |
|------|--------------|
| **PostHog** | Open-source, self-host được, product analytics |
| **Plausible** | Privacy-first, đơn giản, EU compliant |
| **Mixpanel** | Funnel phức tạp, retention analysis |
| **Google Analytics** | Free, SEO insights |

### 🔍 MONITORING
| Tool | Khi nào dùng |
|------|--------------|
| **Sentry** | Error tracking, must-have |
| **LogRocket** | Session replay, debug UX |
| **UptimeRobot** | Uptime alert miễn phí |
| **Datadog** | Enterprise observability |

### 🔧 DEVOPS
| Tool | Role |
|------|------|
| **Docker** | Container hóa app |
| **GitHub Actions** | CI/CD miễn phí |
| **Terraform** | Infrastructure as code |
| **Kubernetes** | Orchestrate containers quy mô lớn |

---

## Setup từng bước — Stack khởi đầu nhanh nhất 2026

Stack nhanh nhất để bắt đầu SaaS (tao recommend):

```bash
# 1. Tạo Next.js project với TypeScript + Tailwind
npx create-next-app@latest my-saas --typescript --tailwind --app

# 2. Cài Shadcn UI
npx shadcn@latest init

# 3. Cài Supabase client (DB + Auth + Storage trong 1)
npm install @supabase/supabase-js @supabase/ssr

# 4. Cài Clerk (Auth)
npm install @clerk/nextjs

# 5. Cài Stripe
npm install stripe @stripe/stripe-js

# 6. Cài Resend (Email)
npm install resend
```

Biến môi trường cần thiết:
```env
# Supabase
NEXT_PUBLIC_SUPABASE_URL=
NEXT_PUBLIC_SUPABASE_ANON_KEY=
SUPABASE_SERVICE_ROLE_KEY=

# Clerk
NEXT_PUBLIC_CLERK_PUBLISHABLE_KEY=
CLERK_SECRET_KEY=

# Stripe
STRIPE_SECRET_KEY=
NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY=
STRIPE_WEBHOOK_SECRET=

# Resend
RESEND_API_KEY=

# Deploy (Vercel tự detect)
```

---

## Ví dụ thực tế

**Case: Build SaaS đặt vé tour du lịch (ABTRIP)**

| Layer | Chọn | Lý do |
|-------|------|-------|
| Frontend | Next.js + Shadcn | SEO tốt cho trang tour, UI component đẹp |
| Backend | Next.js API Routes | Monorepo tiện, không cần server riêng |
| Database | Supabase (Postgres) | Row Level Security cho user data, real-time |
| Auth | Clerk | Social login (Google/Facebook) cho khách VN |
| Payment | Stripe | Hỗ trợ VND, webhook đáng tin |
| Email | Resend | Gửi booking confirmation |
| Storage | Supabase Storage | Ảnh tour, tài liệu |
| Deploy | Vercel | Deploy Next.js siêu nhanh |
| Monitor | Sentry + UptimeRobot | Bắt lỗi + alert down |

---

## Lưu ý / Lỗi thường gặp

- **Đừng dùng Supabase Auth + Clerk cùng lúc** — chọn 1 cái, không cần cả 2
- **Railway free tier bị sleep** — production thì upgrade hoặc dùng Render
- **Stripe chưa fully support VN** — test kỹ trước khi go-live, dùng test mode nhiều
- **MongoDB cho SaaS thường là wrong choice** — relationship data cần SQL, không cần NoSQL
- **Vercel free tier limit** — serverless function 10s timeout, cẩn thận với long-running tasks
- **Kubernetes overkill** cho MVP/indie — chỉ cần khi scale thật sự lớn

---

## Đánh giá cá nhân

- **Điểm mạnh:** Cover toàn bộ lifecycle của SaaS product, không thiếu layer nào. Mỗi category đều có 3-5 lựa chọn với explanation rõ ràng bằng tiếng Việt.
- **Điểm yếu:** Một số tool mới (Polar, DataFast) còn chưa battle-tested ở VN. Stack này heavy JavaScript/TypeScript — ai quen Python-only cần điều chỉnh BE layer.
- **Có nên dùng không:** 8/10 — Đây là bản đồ chuẩn nhất để bắt đầu SaaS 2026. Recommend stack nhanh: Next.js + Supabase + Clerk + Stripe + Resend + Vercel + Sentry.

## Link
- Infographic nguồn: Series 4 ảnh tiếng Việt (SaaS Stack 2026)
- Shadcn UI: https://ui.shadcn.com
- Supabase: https://supabase.com
- Clerk: https://clerk.com
- Railway: https://railway.app
- PostHog: https://posthog.com
