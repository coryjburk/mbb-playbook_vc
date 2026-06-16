# Eccles MBA — Consulting Interview Playbook

A single-file, self-contained MBB consulting interview playbook with a data-driven engine,
practice tools (voice input, filler-word tracking, AI coaching-prompt generator), a readiness
dashboard, and a live insight-source library.

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
