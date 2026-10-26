"""Save one WebFetch extraction: python3 -I save.py <repo> <n>  < json. Adds the fetch envelope; never alters the text."""
import json, sys, pathlib, datetime
repo, n = sys.argv[1], int(sys.argv[2])
raw = sys.stdin.read().strip()
if raw.startswith("```"):
    raw = raw.strip("`")
    raw = raw[raw.index("{"):]
data = json.loads(raw)
out = {
    "repo": repo,
    "fork": f"ai-code-review-evaluation/{repo}-greptile",
    "pull": n,
    "source_url": f"https://github.com/ai-code-review-evaluation/{repo}-greptile/pull/{n}",
    "fetched_on": "2026-10-26",
    "fetched_with": "WebFetch (page converted to markdown, answered by a small model; quotes capped at 125 characters, so long comments are faithful paraphrases)",
    "extraction": data,
}
p = pathlib.Path("/home/user/bench-data/greptile-comments") / f"{repo}-{n:02d}.json"
p.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
print("saved", p.name, len(data.get("greptile", [])))
