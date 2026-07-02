---
name: x-com-playbook
description: "X.com (Twitter) platform operations via agent-browser. 7 sections: Browse & Read, Engagement, Content Creation, Social Graph, Profile, Navigation, Lists."
allowed-tools:
  - Bash
user-invocable: true
---

# X.com (Twitter) — Agent Browser Playbook

**agent-browser** installed ✓ (v0.27.0). Chrome CDP required.

## 1. Browse & Read

| Action | Command |
|--------|---------|
| Open timeline | `agent-browser open https://x.com/home` |
| Open tweet by URL | `agent-browser open "https://x.com/user/status/<id>"` |
| Search tweets | `agent-browser open "https://x.com/search?q=<query>&src=typed_query"` |
| Search latest | `agent-browser open "https://x.com/search?q=<query>&src=typed_query&f=live"` |
| View profile | `agent-browser open "https://x.com/<username>"` |
| Read replies | snapshot + scroll down 800, read `article` elements |
| Notifications | `agent-browser open https://x.com/notifications` |
| DMs | `agent-browser open https://x.com/messages` (redirects to /i/chat) |

**Scroll loop for profile posts:**
```bash
for i in $(seq 1 5); do
  agent-browser scroll down 3000 && sleep 2 && agent-browser snapshot -i -s 'article'
done
```

## 2. Engagement

| Action | Steps |
|--------|-------|
| Like | snapshot → click `button "N Likes. Like"` |
| Unlike | snapshot → click `button "N Likes. Liked"` |
| Retweet | click repost button → snapshot → click `menuitem "Repost"` |
| Undo retweet | click reposted button → click `menuitem "Undo repost"` |
| Bookmark | click `button "Bookmark"` |
| Remove bookmark | click `button "Bookmarked"` |

## 3. Content Creation

| Action | Steps |
|--------|-------|
| Post tweet | `agent-browser open https://x.com/compose/post` → fill textbox → click `button "Post"` |
| Post with image | Same + click `input[type="file"]` → upload → post |
| Reply | Open tweet → find reply textbox → type → click Reply button |
| Quote tweet | Open tweet → click repost button → click `menuitem "Quote"` |
| Delete tweet | Open tweet → click `button "More"` → click `menuitem "Delete"` → confirm |

## 4. Social Graph

| Action | Command |
|--------|---------|
| Follow | Profile → click `button "Follow"` |
| Unfollow | Profile → click `button "Following"` → confirm |
| View followers | `agent-browser open "https://x.com/<username>/followers"` |
| View following | `agent-browser open "https://x.com/<username>/following"` |

## 5. Profile Management

| Action | Steps |
|--------|-------|
| View own profile | `agent-browser open "https://x.com/<username>"` |
| Edit bio | Settings → profile → edit → save |
| Pin tweet | Open tweet → More menu → `menuitem "Pin to profile"` |

## 6. Navigation & Utility

| Action | Command |
|--------|---------|
| Switch tabs | click `tab "For you"` or `tab "Following"` |
| Scroll | `agent-browser scroll down <px>` |
| Handle popups | `agent-browser press Escape` |
| Cookie consent | click `button "Accept"` or `button "Refuse"` |

## 7. Lists

| Action | Command |
|--------|---------|
| View lists | `agent-browser open "https://x.com/<username>/lists"` |
| View list timeline | Open list → click its link |
| Create list | Lists page → click `button "Create new list"` → fill name/description → save |
| Add member | Profile → More menu → `menuitem "Add/remove @<username> from Lists"` |
| Delete list | Lists page → click list → More → `menuitem "Delete list"` |

## Pitfalls
- **Refs change after every interaction** — always re-snapshot
- **Quote tweet click trap**: clicking article body navigates to quoted post, not the quote tweet. Click **timestamp link** instead
- **Pinned tweet is first article** on profile — scroll to see real recent posts
- **Virtualized DOM** — only 1-2 articles in viewport at a time
- **Rate limiting** on rapid likes/follows
- Retweet is **2-step**: click button → opens dropdown → click menuitem