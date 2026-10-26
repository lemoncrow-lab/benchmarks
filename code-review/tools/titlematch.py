import json, re, pathlib
GOLD = pathlib.Path("/home/user/bench-repos/golden_comments/code_review_benchmarks")
FILES = {"sentry": "sentry.json", "cal.com": "cal_dot_com.json", "grafana": "grafana.json", "keycloak": "keycloak.json", "discourse": "discourse.json"}
facts = json.load(open("/home/user/bench-data/gitfacts_raw.json"))
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
used = {}
for key, v in facts.items():
    gold = json.load(open(GOLD / FILES[v["repo"]]))
    idx = [i for i, g in enumerate(gold) if norm(g["pr_title"]) == norm(v["title"])]
    status = "EXACT" if len(idx) == 1 else ("AMBIGUOUS" if idx else "NO MATCH")
    print(f'{key:14s} {status:9s} golden#{[i+1 for i in idx]}  fork title: {v["title"][:70]}')
    if idx: used.setdefault(v["repo"], []).append(idx[0])
for repo, u in used.items():
    gold = json.load(open(GOLD / FILES[repo]))
    left = [i+1 for i in range(len(gold)) if i not in u]
    print(repo, "golden entries unmatched by title:", left, [gold[i-1]["pr_title"][:60] for i in left])
