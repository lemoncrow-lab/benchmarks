"""Collect the competitor bot's comments on each fork pull request through the GitHub REST API (exact text).

python3 -I tools/gh_collect.py <code-review dir>
Reads the (repo, pull) list from greptile-comments/*.json; writes greptile-comments-api/<repo>-<NN>.json (raw API
items, bot only) and greptile-comments-api-normalised/<corpus id>.json (the scorer's input). Rules, same contract as
normalise.py: only inline review comments are findings; only the bot's first review (the benchmark period, Jun/Jul
2025); replies and exact (path, text) repeats are dropped. Needs an authenticated `gh`.
"""
import json, pathlib, subprocess, sys

BOT = "greptile-apps[bot]"
root = pathlib.Path(sys.argv[1])
raw_dir, norm_dir = root / "greptile-comments-api", root / "greptile-comments-api-normalised"
raw_dir.mkdir(exist_ok=True); norm_dir.mkdir(exist_ok=True)


def gh(path):
    out = subprocess.run(["gh", "api", "--paginate", "--slurp", path], check=True, capture_output=True, text=True).stdout
    return [item for page in json.loads(out) for item in page]


rows = []
for f in sorted((root / "greptile-comments").glob("*.json")):
    src = json.loads(f.read_text())
    fork, n = src["fork"], src["pull"]
    pr = json.loads(subprocess.run(["gh", "api", f"repos/{fork}/pulls/{n}"], check=True, capture_output=True, text=True).stdout)
    reviews = [r for r in gh(f"repos/{fork}/pulls/{n}/reviews") if r["user"]["login"] == BOT]
    comments = [c for c in gh(f"repos/{fork}/pulls/{n}/comments") if c["user"]["login"] == BOT]
    in_period = [r for r in reviews if r["submitted_at"][:7] in ("2025-06", "2025-07")]
    first = min(in_period, key=lambda r: r["submitted_at"]) if in_period else None
    raw = {"fork": fork, "pull": n, "source_url": src["source_url"], "fetched_with": "gh api (REST), exact text",
           "title": pr["title"], "base": pr["base"]["ref"], "head": pr["head"]["ref"],
           "reviews": [{k: r[k] for k in ("id", "submitted_at", "state", "body")} for r in reviews],
           "comments": [{k: c.get(k) for k in ("id", "pull_request_review_id", "in_reply_to_id", "created_at", "path",
                                               "start_line", "line", "original_start_line", "original_line", "body")}
                        for c in comments]}
    (raw_dir / f.name).write_text(json.dumps(raw, indent=1, ensure_ascii=False) + "\n")
    out, seen, dropped = [], set(), []
    for c in raw["comments"]:
        text = (c["body"] or "").strip()
        reason = None
        if first is None or c["pull_request_review_id"] != first["id"]:
            reason = "not the first review in the benchmark period"
        elif c["in_reply_to_id"]:
            reason = "reply"
        elif (c["path"], text) in seen:
            reason = "exact repeat"
        if reason:
            dropped.append({"id": c["id"], "reason": reason})
            continue
        seen.add((c["path"], text))
        end = c["line"] or c["original_line"]
        start = c["start_line"] or c["original_start_line"] or end
        lines = "" if end is None else (f"{start}-{end}" if start != end else str(end))
        out.append({"id": f"c{len(out)+1}", "path": c["path"], "lines": lines, "text": text})
    rec = {"reviewer": f"competitor bot (author {BOT})", "repo": src["repo"], "pull": n, "title": pr["title"],
           "base_branch": pr["base"]["ref"], "head_branch": pr["head"]["ref"], "source_url": src["source_url"],
           "fetched_with": "gh api (REST), exact text",
           "extraction": {"first_review_id": first and first["id"], "bot_comments": len(comments),
                          "unique_inline_kept": len(out), "page_truncated": False, "dropped": dropped},
           "comments": out}
    (norm_dir / f.name.replace("cal.com-", "calcom-")).write_text(json.dumps(rec, indent=1, ensure_ascii=False) + "\n")
    old = json.loads((root / "greptile-comments-normalised" / f.name.replace("cal.com-", "calcom-")).read_text())
    rows.append((f.stem, len(old["comments"]), len(out), len(dropped)))
    print(*rows[-1], flush=True)
print("TOTAL page-extraction", sum(r[1] for r in rows), "api", sum(r[2] for r in rows), "dropped", sum(r[3] for r in rows))
