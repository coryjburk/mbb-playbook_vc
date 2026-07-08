#!/usr/bin/env python3
"""
build_feeds.py — fetch consulting/business RSS feeds and write feeds.json.

*** PLACEMENT MATTERS: this file MUST live at  <repo_root>/scripts/build_feeds.py  ***
OUT_PATH below resolves two levels up from this file. If this script sits at the
repo root instead, feeds.json gets written OUTSIDE the repo and the Action's
commit step silently commits nothing.

Runs in GitHub Actions (full internet) where browser CORS does not apply, so it
can pull McKinsey/BCG/etc. directly. Feeds that fail or have no public RSS are
skipped gracefully — the playbook falls back to a direct link for those sources.
Local use:  pip install feedparser && python scripts/build_feeds.py
"""
import json
import socket
import sys
import datetime
import pathlib
import feedparser

ITEMS_PER_SOURCE = 6

# Some publishers time out or hang on slow responses; don't let one feed
# stall the whole Action run.
socket.setdefaulttimeout(20)

# Corporate sites (BCG, Deloitte) sometimes block feedparser's default
# user-agent. Present a browser-ish UA with a contact URL.
AGENT = (
    "Mozilla/5.0 (compatible; MBB-Playbook-FeedBot/1.0; "
    "+https://coryjburk.github.io/mbb-playbook_vc/)"
)

# Output path is explicit relative to this script, regardless of working directory.
# Resolves to: <repo_root>/feeds.json  (assumes this file is in <repo_root>/scripts/)
OUT_PATH = pathlib.Path(__file__).resolve().parent.parent / "feeds.json"

# key, display name, candidate feed URL(s) tried in order.
# Verified live (Action run + direct fetch, 2026-07-08): mckinsey (first URL),
# hbr_pod (harvardbusiness.org URL), sloan, wharton, strategy_simplified.
# Confirmed NOT working at these URLs as of 2026-07-08 (kept as best-effort;
# playbook links these sources directly): bcg (returns HTML, not XML),
# deloitte (HTML page / redirect loop), feeds.hbr.org URLs (TLS rejected).
SOURCES = [
    ("mckinsey", "McKinsey Insights", [
        "https://www.mckinsey.com/insights/rss",
        "http://www.mckinsey.com/insights/rss.aspx",
    ]),
    ("bcg", "BCG Publications", [
        "https://www.bcg.com/publications/rss",
    ]),
    ("hbr", "Harvard Business Review", [
        "https://feeds.hbr.org/harvardbusiness",
        "http://feeds.harvardbusiness.org/harvardbusiness",
    ]),
    ("hbr_pod", "HBR Podcasts (IdeaCast)", [
        "http://feeds.harvardbusiness.org/harvardbusiness/ideacast",
        "https://feeds.hbr.org/harvardbusiness/ideacast",
        "https://rss.art19.com/hbr-ideacast",
    ]),
    ("sloan", "MIT Sloan Management Review", [
        "https://sloanreview.mit.edu/feed/",
    ]),
    ("wharton", "Knowledge at Wharton", [
        "https://knowledge.wharton.upenn.edu/feed/",
    ]),
    ("deloitte", "Deloitte Insights", [
        "https://www2.deloitte.com/us/en/insights/rss-feeds.rss",
        "https://www2.deloitte.com/insights/us/en/rss.xml",
    ]),
    # Case-practice audio: live MBB-style case walkthroughs + recruiting intel.
    # NOTE: this podcast feed has no per-item <link> (audio is in <enclosure>,
    # guid is not a URL), so entry_link() below falls back to the enclosure —
    # clicking a headline opens the episode audio directly.
    ("strategy_simplified", "Strategy Simplified (Case Practice)", [
        "https://feeds.buzzsprout.com/1002655.rss",
        "https://rss.buzzsprout.com/1002655.rss",
    ]),
]


def parse_date(entry):
    for attr in ("published_parsed", "updated_parsed"):
        t = entry.get(attr)
        if t:
            try:
                return datetime.datetime(*t[:6], tzinfo=datetime.timezone.utc).isoformat()
            except Exception:
                pass
    return None


def entry_link(e):
    """
    Best available URL for an entry. Article feeds provide a per-item <link>.
    Podcast feeds (e.g. Buzzsprout) often provide only an <enclosure> with the
    audio URL and a non-URL guid — fall back to the enclosure so those items
    aren't silently dropped.
    """
    link = (e.get("link") or "").strip()
    if link:
        return link
    for enc in e.get("enclosures", []) or []:
        href = (enc.get("href") or "").strip()
        if href:
            return href
    return ""


def fetch(urls):
    """
    Try each URL in order. Returns (items, used_url) for the first URL that
    yields at least one valid item, or ([], None) if all fail.

    feedparser almost never raises exceptions — network errors and bad XML
    come back as d.bozo=True with empty or partial entries. We check both
    the bozo flag and entry content, and log a warning for bozo feeds so
    failures don't silently look like successes.
    """
    for url in urls:
        try:
            d = feedparser.parse(url, agent=AGENT)
        except Exception as ex:
            # Genuine exceptions are rare but possible (e.g. SSL errors on
            # some platforms). Log and try the next URL.
            print(f"  ! {url}: exception — {ex}", file=sys.stderr)
            continue

        if d.get("bozo") and not d.entries:
            # bozo=True with no entries almost always means a network error,
            # 404, or completely malformed document. Log the cause if available.
            exc = d.get("bozo_exception")
            print(f"  ! {url}: feed error — {exc}", file=sys.stderr)
            continue

        items = []
        for e in d.entries[:ITEMS_PER_SOURCE]:
            title = (e.get("title") or "").strip()
            link = entry_link(e)
            if title and link:
                items.append({"title": title, "link": link, "date": parse_date(e)})

        if items:
            return items, url

        # Parsed without a fatal error but produced no usable items. This path
        # was previously silent, which hid a real bug — always say why a URL
        # yielded nothing (HTTP status and entry count point at the cause).
        print(
            f"  ! {url}: parsed but 0 usable items "
            f"(HTTP status={d.get('status')}, entries={len(d.entries)})",
            file=sys.stderr,
        )

    return [], None


def main():
    out_sources = []

    for key, name, urls in SOURCES:
        items, used = fetch(urls)
        if items:
            print(f"{name}: {len(items)} items via {used}")
        else:
            print(f"{name}: no feed — link-only fallback")
        out_sources.append({"key": key, "name": name, "items": items})

    total = sum(len(s["items"]) for s in out_sources)

    # Fail loudly if every feed missed. A silent all-empty write would let
    # the playbook display nothing while Actions shows a green run.
    if total == 0:
        print(
            "ERROR: no items fetched from any source. "
            "Check feed URLs and network access.",
            file=sys.stderr,
        )
        sys.exit(1)

    payload = {
        # datetime.utcnow() is deprecated in Python 3.12+; use timezone-aware form.
        "updated": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "note": "Auto-generated by scripts/build_feeds.py via GitHub Actions.",
        "sources": out_sources,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)

    print(f"\nWrote {OUT_PATH} with {total} total items across {len(out_sources)} sources.")


if __name__ == "__main__":
    main()
