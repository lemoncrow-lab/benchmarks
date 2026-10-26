"""Record the comments the 'Files changed' page showed that the conversation page did not (matched by hand).
python3 -I add_files_tab.py <repo> <n> <reported_count> <new_item_json_list>   (reads the list from stdin)"""
import json, sys, pathlib
repo, n, shown = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
items = json.loads(sys.stdin.read())
p = pathlib.Path("/home/user/bench-data/greptile-comments") / f"{repo}-{n:02d}.json"
d = json.loads(p.read_text())
d["files_tab"] = {
    "source_url": d["source_url"] + "/files",
    "fetched_on": "2026-10-26",
    "bot_comments_shown_on_page": shown,
    "note": "Second page read because the conversation page hid threads ('N hidden conversations'). Items below are the bot comments this page showed that matched no comment of the conversation page (matched by hand); the rest were the same comments.",
    "additions": [dict(kind="inline", date="Jul 2025", **it) for it in items],
}
p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n")
print("updated", p.name, len(items))
