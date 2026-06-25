# Eccles MBA — Consulting Interview Playbook

A single-file, self-contained MBB consulting interview playbook with a data-driven engine,
practice tools (voice input, filler-word tracking, AI coaching-prompt generator), a readiness
dashboard, and a live insight-source library.

### Executive Operations & Navigation Manual

Welcome to the central documentation command node for the **Eccles MBA Consulting Interview Playbook Ecosystem**. This platform is engineered specifically for University of Utah David Eccles School of Business MBA candidates and experienced professionals preparing for high-stakes strategic selection rounds at McKinsey, Bain, BCG (MBB), and top-tier boutique groups.

Moving away from static, linear text documents, this platform is built as an interactive, distributed web application. A permanent global navigation sidebar anchors the left boundary of every module, permitting candidates to traverse the entire ecosystem smoothly inside a **single active browser tab** without dropping state or fracturing focus across multiple windows.

---

## 🗺️ 1. Ecosystem Map & Directory

The training suite is composed of ten interlinked vanilla web files. To ensure uncompromised platform performance, all files must reside within the same directory level on your local machine or your remote deployment branch.

| Module Filename | Platform Component Title | Primary Strategic & Analytical Target |
| :--- | :--- | :--- |
| **`index.html`** | Executive Landing Portal | Core landing dashboard. Houses the Aggregated Strategy Flight Score, localized Readiness Cockpit, 4-Week Prep Plan, and Partner Round defenses. |
| **`playbook_frameworks.html`** | 20 Case Frameworks Vault | Scaffolding diagnostic engine. Explores 20 industry-specific custom issue trees, candidate pitfalls, and elite customization scripts. |
| **`playbook_math.html`** | 15 Spoken Analytics Drills | Quantitative workout engine. Calibrates math logic verbalization structures, core financial formulas, and fast rounding shortcuts. |
| **`playbook_battlecard.html`** | MBB Reference & Red Flags | High-density quick-reference ledger. Packs 15 procedural checklists, tactical power phrases, and the 20 Fatal Red Flags safety vault. |
| **`playbook_sprint_01.html`** | Practice Sprint 1 | **Theme:** Profitability Decline & Market Entry Essentials.<br>Includes 5 target cases and 20 paired questions. |
| **`playbook_sprint_02.html`** | Practice Sprint 2 | **Theme:** M&A, Corporate Valuation, and Strategic Investments.<br>Includes 5 target cases and 20 paired questions. |
| **`playbook_sprint_03.html`** | Practice Sprint 3 | **Theme:** Supply Chain, Operations, and Cost Restructuring.<br>Includes 5 target cases and 20 paired questions. |
| **`playbook_sprint_04.html`** | Practice Sprint 4 | **Theme:** Digital Transformation, Tech/SaaS, and AI Strategy.<br>Includes 5 target cases and 20 paired questions. |
| **`playbook_sprint_05.html`** | Practice Sprint 5 | **Theme:** International Expansion, Go-To-Market, and Commercial Pricing.<br>Includes 5 target cases and 20 paired questions. |
| **`playbook_sprint_06.html`** | Practice Sprint 6 | **Theme:** Advanced Estimation, Standalone Market Sizing, and Partner Edge Cases.<br>Includes 5 target cases and 20 paired questions. |

---

## 🎛️ 2. Interface Components & Definitions

Every module across this ecosystem leverages identical custom UI controls. Understanding these mechanisms is required for efficient navigation:

* **Permanent Global Sidebar Menu:** The primary navigation array anchoring the left side of the screen. Utilizing absolute internal routing links, it enables instant jumping between core assets while permanently preserving your tab environment.
* **Horizontal Local Sub-Toolbars:** Located directly beneath the content headers of internal files, these toolbars host contextual filters. They toggle visibility boundaries (such as switching views between full Case Prompts and the Paired Question Bank) without executing slow page refreshes.
* **Tabbed Case Progression Cards:** In-page navigation matrices built inside case containers. They segment information into distinct phases—*Objectives, Structure, Data/Exhibit, Ideal Solution,* and *Partner Notes*—directly tracking the physical timing milestones of an active live interview run.
* **Spoken Voice Transcription Engine:** A Web Speech API integration built natively into the practice dashboards. It converts incoming verbal microphone streams into running text strings, forcing candidates to practice out loud rather than reading text boxes in silence.
* **Automated Filler-Word Tracker:** A real-time text-scanning compiler linked straight to the audio capture window. It measures occurrences of high-frequency verbal hesitations (*um, uh, like, basically, actually, you know, sort of, kind of*) and outputs a live scorecard to target a clean, authoritative speaking pace.

---

## 🔄 3. The Closed-Loop Training Framework

The platform runs on an interactive, closed-loop loop that links your verbal interview delivery with a partner-grade AI grading engine. Follow this exact sequence for every practice module:

## Files

| File | What it is |
|---|---|
| `Eccles_MBB_Consulting_Interview_Playbook.html` | The playbook. Open it directly or host it. |
| `feeds.json` | Headlines for the Sources tab. Auto-refreshed by the Action. |
| `scripts/build_feeds.py` | Fetches the RSS feeds and writes `feeds.json`. |
| `.github/workflows/update-feeds.yml` | Runs the script every 6 hours and commits `feeds.json`. |

## Deploy on GitHub Pages

1. Put all four files in a repo (keep the folder structure: `scripts/` and `.github/workflows/`).
2. **Settings → Pages →** deploy from your default branch, root folder.
3. Your link will be `https://coryjburk.github.io/<repo-name>/Eccles_MBB_Consulting_Interview_Playbook.html`
   (or rename the HTML to `index.html` to drop the filename from the URL).

## Turn on the live source feed

1. **Settings → Actions → General →** Workflow permissions → enable **Read and write permissions**
   (lets the Action commit the refreshed `feeds.json`).
2. **Actions** tab → select **Update insight feeds** → **Run workflow** once to populate it now.
   After that it runs itself every 6 hours.

### Why it works this way
Browsers block a hosted page from fetching another site's RSS directly (CORS). So the GitHub
Action fetches the feeds server-side, writes `feeds.json` into the repo, and the playbook just
reads that local file. Sources without a working public feed (Bain, EY, Kearney, Oliver Wyman,
Strategy&) fall back to a direct link automatically — the page never breaks.

### Source feed status (verified)
- **Live feed:** McKinsey, BCG, HBR, HBR Podcasts, MIT Sloan, Knowledge at Wharton, Deloitte (the Action confirms each on first run).
- **Link-only (no reliable public RSS):** Bain, Strategy& (PwC), EY, Kearney, Oliver Wyman.

## Adding content
All content lives in the JS data arrays near the top of the `<script>` block
(`CONSULTING_QUESTIONS`, `CONSULTING_CASES`, `CONSULTING_FRAMEWORKS`, `CONSULTING_MATH`,
`CONSULTING_FIT`, `CONSULTING_BATTLECARD`, `CONSULTING_REDFLAGS`). Each build batch just extends
these arrays — the rendering, filters, and practice tools never change.
