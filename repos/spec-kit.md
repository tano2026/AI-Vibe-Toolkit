# GitHub Spec Kit — GitHub Repo

## TL;DR
Toolkit chinh thuc cua GitHub day Spec-Driven Development — giai phap cho van de "vibe coding" lam AI code loi lien tuc. 116.6K stars, MIT license. Thay vi mo ta mo ho, viet spec ro rang truoc → AI code dung ngay tu dau.

## Repo nay dung de lam gi
Vibe coding (go prompt mo ho, AI doan y) hay dan den: code sai huong, phai sua di sua lai, AI quen context giua cac session. Spec Kit flip lai cach lam:

**4 buoc chinh:**
1. **SPEC** — Viet specification ro rang: muon gi, lam gi, dieu kien thanh cong
2. **PLAN** — AI lap ke hoach ky thuat tu spec
3. **TASKS** — Breakdown thanh tung task nho, co thu tu
4. **IMPLEMENT** — AI code tung task, theo dung spec da duyet

**Khac vibe coding o cho:**
- Spec la nguon su that — AI khong tu doan, luon doi chieu lai spec
- Multi-session: spec luu lai, session sau AI doc lai spec, khong mat context
- Review duoc truoc khi code — duyet plan truoc khi AI bat tay vao lam

## Ho tro AI coding agent

Spec Kit tich hop voi: Claude Code, GitHub Copilot, Cursor, Gemini CLI, Windsurf, va nhieu agent khac qua `specify` CLI.

## Setup tung buoc

```bash
# Cai Specify CLI
uvx --from git+https://github.com/github/spec-kit.git specify init my-project
cd my-project

# Hoac neu da co project
specify init --here

# Workflow trong Claude Code / Cursor:
/specify   → Viet spec cho feature
/plan      → AI lap ke hoach ky thuat
/tasks     → Breakdown thanh task
/implement → AI code tung task theo spec
```

## Vi du thuc te

**Thay vi vibe code mo ho:**
```
Prompt cu: "Lam cho tao tinh nang dat tour"
→ AI doan: form don gian, khong ro field nao, khong ro validation
```

**Voi Spec Kit:**
```
/specify
"Tinh nang dat tour ABTRIP:
- User chon tour, ngay di, so nguoi
- Validate: ngay phai > hom nay, so nguoi 1-20
- Sau khi submit: tao booking record, gui email confirm
- Edge case: tour het cho phai bao loi ro rang"

/plan → AI de xuat: database schema, API endpoint, validation logic
/tasks → Breakdown: [1] tao model, [2] tao API, [3] validation,
         [4] email service, [5] frontend form
/implement → AI code tung task, doi chieu spec lien tuc
```

Ket qua: code dung ngay lan dau, it phai sua lai.

## Ung dung cho Hermes/Claude Code

Ket hop voi HERMES-AGENTS.md (harness da co trong kho):
```
AGENTS.md dinh nghia rules cua Hermes
    +
Spec Kit dinh nghia spec cho tung task cu the
    =
Hermes code dung scope, dung yeu cau, it sai sot
```

## Danh gia ca nhan
- Diem manh: Chinh thuc tu GitHub — se duoc maintain lau dai; 116K stars; tich hop hau het AI coding tool pho bien; giai quyet dung pain point cua vibe coding
- Diem yeu: Them buoc viet spec truoc khi code — cham hon vibe code thuan tuy cho task nho; learning curve ban dau
- Co nen dung khong: **9/10** — Dung cho feature lon, phuc tap. Task nho/quick fix thi vibe code van nhanh hon. Ket hop voi HERMES-AGENTS.md de Hermes code chinh xac hon.

## Link
- Repo: https://github.com/github/spec-kit
- Docs: https://github.github.io/spec-kit/
- License: MIT
