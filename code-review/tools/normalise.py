"""Turn the raw page extractions into the scorer's reviewer-comments files. Deterministic; the rules are the contract:

 1. only `inline` comments are findings (a review summary is not a finding; it is kept in the raw file);
 2. only the first review, dated July 2025 (the benchmark period); later re-reviews and notices are dropped;
 3. collapsed placeholders ('Text not visible') and items that say they duplicate another are dropped;
 4. exact repeats of (path, text) are dropped (the page repeats a thread in two places);
 5. comments the 'Files changed' page added (matched by hand) are appended.
"""
import json, pathlib, re, glob

SRC = pathlib.Path("/home/user/bench-data/greptile-comments")
DST = pathlib.Path("/home/user/bench-data/greptile-comments-normalised")
DST.mkdir(exist_ok=True)

def in_benchmark_period(date: str) -> bool:
    return not date or bool(re.search(r"\b(Jul|Jun)\b.*2025", date))

def numbers(counts: str):
    m = re.search(r"(\d+) comments?", counts or "")
    return int(m.group(1)) if m else (0 if "no comment" in (counts or "") else None)

rows = []
for f in sorted(SRC.glob("*.json")):
    d = json.loads(f.read_text())
    ex = d["extraction"]
    out, seen, dropped = [], set(), []
    items = [c for c in ex["greptile"] if c["kind"] == "inline"]
    items += (d.get("files_tab") or {}).get("additions", [])
    for c in items:
        text = c["text"].strip()
        reason = None
        if not in_benchmark_period(c.get("date", "")):
            reason = "later than the benchmark period"
        elif text.startswith("[Collapsed") or "Text not visible" in text:
            reason = "collapsed placeholder"
        elif text.startswith("Duplicate of the same comment"):
            reason = "marked as duplicate"
        elif (c["path"], text) in seen:
            reason = "exact repeat"
        if reason:
            dropped.append({"text": text[:80], "reason": reason})
            continue
        seen.add((c["path"], text))
        out.append({"id": f"c{len(out)+1}", "path": c["path"], "lines": c.get("lines", ""), "text": text})
    stated = numbers(ex.get("summary_counts", ""))
    rec = {
        "reviewer": "competitor bot (author greptile-apps[bot])",
        "repo": d["repo"], "pull": d["pull"], "title": ex["title"], "base_branch": ex["base"], "head_branch": ex["head"],
        "source_url": d["source_url"], "fetched_on": d["fetched_on"],
        "extraction": {"stated_by_summary": ex.get("summary_counts", ""), "stated_comments": stated,
                       "unique_inline_kept": len(out), "page_truncated": bool(ex.get("truncated")),
                       "files_tab_read": "files_tab" in d, "dropped": dropped},
        "comments": out,
    }
    (DST / (f.name.replace("cal.com-", "calcom-"))).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    rows.append((f.stem, stated, len(out), bool(ex.get("truncated")), len(dropped)))
print("pr stated kept truncated dropped")
for r in rows: print(*r)
tot_kept = sum(r[2] for r in rows); tot_stated = sum(r[1] or 0 for r in rows)
print("TOTAL kept", tot_kept, "stated", tot_stated)
