# Full-Time MBA Eccles Career OS — MBA Interview Playbook Series

> **Full-Time MBA Program · David Eccles School of Business · MBA Career Coaching**
> A suite of self-contained, AI-powered interview-preparation tools for MBA students recruiting in finance, consulting, operations, and tech/product.

---

## Live Link

[Intv Playbook - MMB Consulting (vC)](https://coryjburk.github.io/mbb-playbook_vc/)

---


## Table of Contents

1. [What This Is](#1-what-this-is)
2. [The Four Tracks](#2-the-four-tracks)
3. [What's Inside Each Playbook](#3-whats-inside-each-playbook)
4. [The Shared Architecture](#4-the-shared-architecture)
5. [How to Use a Playbook (Student Guide)](#5-how-to-use-a-playbook-student-guide)
6. [Deploying to GitHub Pages](#6-deploying-to-github-pages)
7. [Setting Up the Live Insights Feed](#7-setting-up-the-live-insights-feed)
8. [Testing Locally](#8-testing-locally)
9. [Building a New Track](#9-building-a-new-track)
10. [File & Folder Structure](#10-file--folder-structure)
11. [Technical Reference](#11-technical-reference)
12. [For Advisors & Career Coaches](#12-for-advisors--career-coaches)

---

## 1. What This Is

The **Eccles Career OS** is a series of single-file HTML interview-preparation playbooks built for Eccles MBA students. Each tool is:

- **Self-contained** — one `.html` file with inline CSS and JS; no build step, no backend, no paid infrastructure.
- **Deployable anywhere** — works by double-clicking locally or hosting on GitHub Pages.
- **AI-powered** — generates structured coaching prompts students run in ChatGPT or Claude, then pastes the AI's scores back to drive a readiness dashboard automatically.
- **Private and persistent** — all progress (notes, readiness scores) saves in the student's browser via `localStorage`; nothing is stored on a server.

Each tool is designed to **complement, not replace**, the behavioral and personal coaching advisors provide directly. Students use these tools for self-service technical depth and repetition; advisors focus their time on story, strategy, and mock interviews.

---

## 2. The Four Tracks

| Track | Audience | Practice Library | Top Readiness Level | Build Prompt |
|---|---|---|---|---|
| **MBB Consulting** | MBA students recruiting at McKinsey, Bain, BCG | 30 full cases | MBB-Caliber | `Build_Prompt_MBB_Consulting.md` |
| **Investment Banking** | MBA students recruiting for IB Associate roles | 30 technical walk-throughs | Associate-Caliber | `Build_Prompt_Investment_Banking.md` |
| **Product Management** | MBA students recruiting for PM / APM roles in tech | 30 open PM prompts | PM-Caliber | `Build_Prompt_Product_Management.md` |
| **Operations / Supply Chain** | MBA students recruiting for Ops / SC Manager roles | 30 operational scenarios | Manager-Caliber | `Build_Prompt_Operations_Supply_Chain.md` |

Each track shares the same engine, design system, and feature set. Only the domain content and readiness competencies change. See [Section 9](#9-building-a-new-track) for how to add a fifth track.

---

## 3. What's Inside Each Playbook

Every playbook has the same ten tabs. The content is domain-specific; the structure is identical.

### Question Bank (120 questions)
Ten questions across each of twelve domain-specific categories, spanning four difficulty levels: **Foundational → Core → Advanced → Expert**. Each question card has four reveal tabs:

| Tab | What it shows |
|---|---|
| Conversational | A spoken-style model answer (how to say it in the room) |
| Deep Dive | The structured technical depth — formulas, frameworks, trade-offs |
| Coaching | A coach's note on delivery and how to elevate the answer |
| Red Flag | What makes a recruiter or hiring manager wince |

### Practice Library (30 prompts)
Thirty full practice scenarios — cases, technical walk-throughs, PM prompts, or operational scenarios depending on the track. Each includes: a realistic exhibit or data table, the analysis required, a strong-answer path, a final recommendation with key risk and next steps, likely follow-up probes, and a coaching note.

### Frameworks (20)
Domain-specific structures with guidance on how to **customize** them to the situation — not recite them. Each card covers when to use it, structure, a worked example, common mistakes, and how to make it your own.

### Quant / Metrics Drills (15–18)
The calculations candidates must perform cleanly under pressure: formulas, a worked example with real numbers, and how to verbalize the math aloud — because interviews are spoken, not written.

### Fit / Behavioral (20 prompts)
Behavioral and motivation prompts with the STAR structure, what the interviewer is assessing, how to elevate it to the target firm's standard, and the red flags for each.

### Battlecard (15 groups)
Quick-reference cards to review before every coffee chat and interview: must-know concepts, formula cheat sheets, opening checklists, power phrases, and last-minute review.

### Red Flags (20)
The twenty most common mistakes — each with the specific mistake and a concrete fix.

### Readiness Dashboard
AI-scored, not self-scored. See [Section 5](#5-how-to-use-a-playbook-student-guide) for how the closed-loop works.

### Sources (Live Feed)
Current headlines from domain-relevant publications, updated automatically by a GitHub Action. Requires setup — see [Section 7](#7-setting-up-the-live-insights-feed).

---

## 4. The Shared Architecture

The following is identical across all four tracks and should never be rebuilt when creating a new one — only the content arrays change.

### Engine
- Pure vanilla JS — no frameworks, no bundler.
- Content lives in typed JS arrays (`CONSULTING_QUESTIONS`, `CONSULTING_CASES`, etc.). Render functions loop over the arrays and write HTML.
- A `$` (querySelector) helper and `esc()` (HTML-escaper) keep the code compact.
- Every count displayed in the UI (hero stats, filter results) is derived from the arrays at runtime — nothing is hard-coded.

### Design System

| Token | Value | Used for |
|---|---|---|
| Background | `#FBF9F6` | Page warm off-white |
| Primary | `#CC0000` | Utah Red — headers, badges, accents |
| Gold | `#c9a84c` | Rules, highlights, dot markers |
| Slate | `#2C3A47` | Table headers, dark panels |
| Display face | Source Serif 4 | Headings (Google Fonts) |
| Body face | Source Sans 3 | Body text (Google Fonts) |

### Practice Modal
- **Web Speech API** — mic button, live transcription, editable transcript. Works in Chrome on `localhost` or `https://`. Does **not** work on `file://`.
- **Filler-word counter** — tracks "um," "uh," "like," "you know," "sort of," "kind of," "basically," "right," "so," and "actually" in real time.
- **Save note** — persists the student's answer to `localStorage` keyed by question text.

### AI Coaching (Copy/Paste Loop)
The tool generates a structured coaching prompt embedding the question and the student's transcript. The student copies it and runs it in ChatGPT or Claude. The AI returns:

1. Written feedback across structure, content, and delivery.
2. A machine-readable score block in this **exact** format:

```
[READINESS SCORES]
Competency name: <0-100 or NA>
...
[END READINESS SCORES]
```

The student pastes the full AI reply into the **Step 2** box in the practice window, clicks **Log to readiness dashboard**, and the tool parses and accumulates the scores.

> **Why copy/paste and not a live API?** This approach keeps the tool free, host-anywhere, and requires no API key or paid infrastructure. All student responses stay in their own ChatGPT/Claude session — nothing passes through a server. A live-API version using a Vercel serverless proxy is possible as a future enhancement.

### Closed-Loop Readiness Dashboard
- Scores accumulate across reps — each practice session adds to the per-competency average.
- The dashboard is **read-only** — the AI assesses, the tool tracks. No manual sliders.
- An overall index drives one of four levels: **Emerging (0) → Developing (45) → Interview-Ready (68) → [Track-Caliber] (85)**.
- A "Based on N logged reps" line keeps the picture honest.
- The parser tolerates colon or dash separators, reordered lines, labels with or without punctuation, and `NA` (skipped).

### Persistence
- All data lives in `localStorage` — notes, readiness scores, and filter state.
- **Export/Import** — students can download their progress as JSON and import it on another device.
- Storage key is versioned (e.g., `eccles_mbb_readiness_v2`) so future updates don't collide.

---

## 5. How to Use a Playbook (Student Guide)

### The core practice loop

**1 — Attempt first.** Read the question or case prompt and answer it *before* revealing anything. The struggle is the learning.

**2 — Reveal and compare.** Open the card and read the Conversational answer, then the Deep Dive, Coaching note, and Red Flag. Notice the gap between yours and the model.

**3 — Practice aloud.** Click **Practice this aloud**, then **Start recording** (or type). Interviews are spoken — train the spoken version. Watch the filler-word count.

**4 — Get AI coaching (Step 1).** Click **Generate AI coaching prompt**, then **Copy prompt**, and paste it into ChatGPT or Claude. You'll get written feedback plus a scored readiness block.

**5 — Feed it back (Step 2).** Copy the AI's **entire reply** and paste it into the **"Step 2 — paste the AI's reply"** box, then click **Log to readiness dashboard**. The tool reads the scores and updates your dashboard automatically. You never score yourself.

**6 — Let the dashboard guide you.** Over reps, the Readiness tab accumulates AI scores across eight competencies. Let your lowest competency decide what you drill next — not your comfort zone.

### Suggested 4-week plan

| Week | Focus | Goal |
|---|---|---|
| 1 | Fit stories, basic structure, core question types | A clean "why [role]" and a structured answer to the most common prompt |
| 2 | Intermediate cases/prompts, quant drills, frameworks | Drive a practice prompt confidently and do the math aloud |
| 3 | Advanced cases/prompts, synthesis, behavioral depth | Synthesize (not summarize) and land a crisp recommendation |
| 4 | Mocks, final-round scenarios, weakness repair | Interview-Ready or [Track]-Caliber across most competencies |

### Tips

- **Quantify everything.** If your answer has no numbers, it is not done.
- **Synthesize, don't summarize.** Lead with the recommendation, then reasons, key risk, and next steps.
- **Always do Step 2.** Pasting the AI's reply back is what builds your readiness picture — skip it and the dashboard stays empty.
- **Customize frameworks.** Reciting a textbook framework is a red flag. Build the structure from the actual situation.
- **Voice practice beats silent reading.** Use the mic, listen back, and watch your filler count fall.

---

## 6. Deploying to GitHub Pages

Every playbook deploys to GitHub Pages as a static site — no server, no config.

### Step 1 — Create a repository
1. Go to [github.com](https://github.com) and sign in.
2. Click **+** → **New repository**. Name it (e.g., `consulting-playbook`). Set it to **Public**.
3. Click **Create repository**.

### Step 2 — Upload the root files
Click **Add file → Upload files** and upload these four files to the **root** (do not put them in a subfolder):

```
Eccles_MBB_Consulting_Interview_Playbook.html
feeds.json
README.md
Student_Guide.md
```

> **Important:** `feeds.json` must sit in the same folder as the HTML file or the Sources tab will not load.

### Step 3 — Add the two files that need folders

**File 1 — the feed script:**
1. Click **Add file → Create new file**.
2. In the name box type: `scripts/build_feeds.py` (the `/` creates the folder automatically).
3. Paste the contents of your `build_feeds.py` file and click **Commit changes**.

**File 2 — the GitHub Action:**
1. Click **Add file → Create new file**.
2. In the name box type: `.github/workflows/update-feeds.yml`.
3. Paste the contents of your `update-feeds.yml` file and click **Commit changes**.

### Step 4 — Enable GitHub Pages
1. Go to **Settings → Pages** (left sidebar).
2. Set **Source** to **Deploy from a branch**, branch **main**, folder **/ (root)**.
3. Click **Save**. Wait ~2 minutes, then refresh — your published URL appears at the top.

Your playbook is live at:
```
https://<your-username>.github.io/<repo-name>/Eccles_MBB_Consulting_Interview_Playbook.html
```

> **Tip:** Rename the HTML file to `index.html` and the URL shortens to `https://<username>.github.io/<repo-name>/`.

---

## 7. Setting Up the Live Insights Feed

The Sources tab shows current headlines from domain-relevant publications, refreshed automatically every 6 hours by a GitHub Action.

### Step 1 — Enable workflow permissions
1. Go to **Settings → Actions → General**.
2. Under **Workflow permissions**, select **Read and write permissions**.
3. Click **Save**.

### Step 2 — Run the feed workflow
1. Click the **Actions** tab at the top of the repo.
2. On the left, click **Update insight feeds**.
3. Click **Run workflow → Run workflow** (green button).
4. Wait ~60 seconds. When the run shows a green checkmark, open the published playbook and visit the **Sources** tab — headlines should appear.

### How it works
The workflow runs `scripts/build_feeds.py` on a GitHub-hosted runner. That script fetches each publication's RSS feed server-side (bypassing the browser CORS restriction), writes the results to `feeds.json`, and commits the file back to the repo. The playbook reads `feeds.json` on load. Sources with no reliable public RSS show a **Visit** button linking directly to the publication.

---

## 8. Testing Locally

Voice input and live RSS feeds require the page to be served over `http://` — they do **not** work when the file is opened via `file://`. Everything else works by double-clicking.

### Start a local server

**Mac / Linux:**
```bash
python3 -m http.server 8000
```

**Windows:**
```
python -m http.server 8000
```

> **Opening a terminal in your folder on Windows:** Open File Explorer, navigate into the playbook folder, click the address bar, type `cmd`, press Enter.

Then open in Chrome:
```
http://localhost:8000/Eccles_MBB_Consulting_Interview_Playbook.html
```

Press **Ctrl + C** to stop the server.

### End-to-end test checklist

- [ ] All ten tabs load and render content
- [ ] Category, difficulty, and search filters work in the Question Bank
- [ ] Clicking a question reveals all four answer sub-tabs
- [ ] Practice modal opens; mic records; filler-word counter increments
- [ ] Generate AI coaching prompt produces a full prompt with a `[READINESS SCORES]` block
- [ ] Pasting an AI reply and clicking **Log to readiness dashboard** updates the Readiness tab
- [ ] Refreshing the page preserves readiness scores and saved notes
- [ ] Sources tab loads headlines (requires `localhost` or `https://` and a completed feed run)

---

## 9. Building a New Track

A new track takes roughly **6–8 Claude sessions** with computer use enabled.

### Pre-build decisions

| Decision | Notes |
|---|---|
| Role and domain | Be specific: "FP&A / Corporate Finance," not just "finance" |
| 12 question categories | Cover the domain's breadth; difficulty levels provide depth |
| 30 library types | One per distinct scenario or problem type in that interview |
| 8 readiness competencies | Named for what actually determines offer vs. ding |
| 5–8 feed sources | Domain-relevant publications with public RSS |
| Sub-function bias | Optional: e.g., "weight toward LevFin / LBOs" or "toward growth PM" |

### Session structure

| Session | Focus |
|---|---|
| 1 | Shell + engine: tabs, filter/search, modal, dashboard scaffolding |
| 2–3 | Question Bank in batches of 10; validate after each |
| 3–4 | Practice Library in batches of 5; validate after each |
| 4 | Frameworks (all 20) + Quant drills (all in one batch) |
| 5 | Behavioral module (two batches of 10) + Battlecard + Red Flags |
| 6 | Full validation, banner removal, end-to-end test |

### The nine swaps (from the build prompt)

| Element | What to change |
|---|---|
| Role line | Domain-expert persona (banker, PM, ops leader, etc.) |
| 12 categories | Domain-specific question topics |
| 30-item library | Cases → walk-throughs / PM prompts / scenarios |
| Quant drills | Case math → paper-LBO / metrics & estimation / ops formulas |
| Behavioral module depth | People-management weight scales with seniority |
| Frameworks | Domain toolkit (consulting / banking / PM / ops) |
| 8 competencies | Named for what gets candidates cut in that domain |
| Top-level label | MBB-Caliber / Associate-Caliber / PM-Caliber / Manager-Caliber |
| Live feed sources | Domain-relevant RSS |

### Build prompt files

Ready-to-run build prompts for all four tracks live in `build-prompts/`. Copy the closest one, make the nine swaps above, and paste it into a fresh Claude session with computer use enabled.

---

## 10. File & Folder Structure

```
eccles-career-os/
│
├── Eccles_MBB_Consulting_Interview_Playbook.html     ← playbook (one per track)
├── feeds.json                                         ← live feed data (auto-updated)
├── README.md                                          ← this file
├── Student_Guide.md                                   ← student one-pager (markdown)
├── Eccles_Consulting_Playbook_Student_Guide.pdf       ← student one-pager (PDF)
├── Eccles_Career_OS_Series_Playbook.pdf               ← advisor series reference
│
├── scripts/
│   └── build_feeds.py                                 ← RSS fetcher (run by the Action)
│
├── .github/
│   └── workflows/
│       └── update-feeds.yml                           ← GitHub Action (runs every 6h)
│
└── build-prompts/
    ├── Build_Prompt_MBB_Consulting.md
    ├── Build_Prompt_Investment_Banking.md
    ├── Build_Prompt_Product_Management.md
    └── Build_Prompt_Operations_Supply_Chain.md
```

> **Root-level rule:** The HTML file and `feeds.json` must sit at the same level. The Sources tab fetches `feeds.json` relative to the HTML file's location.

---

## 11. Technical Reference

### Browser compatibility

| Feature | Chrome | Firefox | Safari | Edge |
|---|---|---|---|---|
| All content tabs | ✅ | ✅ | ✅ | ✅ |
| Practice modal (text) | ✅ | ✅ | ✅ | ✅ |
| Voice / Web Speech API | ✅ | ❌ | ⚠️ partial | ✅ |
| Live RSS feed | ✅ | ✅ | ✅ | ✅ |
| localStorage | ✅ | ✅ | ✅ | ✅ |

Chrome is recommended for voice practice. All other features work in any modern browser.

### localStorage keys (MBB Consulting track)

| Key | Contents |
|---|---|
| `eccles_mbb_readiness_v2` | `{ entries: N, comp: { [competency]: [score, score, ...] } }` |
| `eccles_mbb_notes_v1` | `{ [question_text]: "student's saved answer" }` |

Keys are versioned. If a future update changes the data shape, bump the version number to avoid stale-data collisions.

### Readiness score parser (tolerates)
- Colon or dash as the separator (`Synthesis: 72` or `Synthesis - 72`)
- Reordered lines (sequence does not matter)
- `NA` values (skipped — competency not scored for that rep)
- Minor label variation (e.g., `Fit/PEI` vs. `Fit / PEI`)
- Extra whitespace or trailing punctuation

### GitHub Action schedule
The feed update workflow runs on:
- **Cron:** every 6 hours (`0 */6 * * *`)
- **Manual trigger:** Actions → Update insight feeds → Run workflow

Requires **Read and write permissions** under Settings → Actions → General → Workflow permissions.

### Graceful degradation

| Feature | No network | No mic | No AI |
|---|---|---|---|
| All content | ✅ Full access | ✅ Full access | ✅ Full access |
| Voice practice | ✅ Type instead | ❌ Type instead | ✅ Full access |
| AI coaching prompt | ✅ Generated locally | ✅ Generated locally | ❌ Copy prompt; run manually |
| Readiness dashboard | ✅ Shows prior scores | ✅ Shows prior scores | ❌ No new scores logged |
| Sources tab | ❌ Last cached feed | ✅ Full access | ✅ Full access |

---

## 12. For Advisors & Career Coaches

### What these tools do
Each playbook gives students high-quality, technically deep, self-service preparation for the content-heavy parts of recruiting — question frameworks, practice libraries, quant drills, and AI-tracked readiness. Students can log hundreds of practice reps and receive scored feedback between advisor meetings.

### What they don't do
They don't replace the behavioral coaching, story development, firm targeting, resume review, networking strategy, or real mock interviews that advisors provide. They're designed so students arrive at advisor meetings having already done the technical groundwork — freeing advisor time for higher-value conversations.

### Sharing a readiness snapshot
Students can export their readiness data as JSON (**Readiness tab → Export**) and share it with an advisor before a session. The JSON shows per-competency averages and rep counts, giving the advisor a data-grounded starting point.

### Advisor-recommended timeline

| Timeframe | Advisor recommendation |
|---|---|
| Weeks 1–2 | Direct students to Question Bank (Fit & Behavioral first, then core technical) and the Battlecard tab |
| Week 3 | Move to the Practice Library; ask students to share their readiness export before the next session |
| Week 4 | Use advisor time for real mocks, story refinement, and firm-specific coaching; the tool handles the reps |
| Ongoing | Encourage the Sources tab for current firm and industry news |

### Suggesting improvements
If a question answer is outdated, a framework needs updating, or a new case type should be added, raise a GitHub Issue in this repo or contact the MBA Career Coaching team directly. Content updates are a single array-object edit in the source file.

---

*Built and maintained by the Eccles MBA Career Coaching team.*
*David Eccles School of Business · University of Utah*
*Repository: [github.com/coryjburk/eccles-career-os](https://github.com/coryjburk/eccles-career-os)*
