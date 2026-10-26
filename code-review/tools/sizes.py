import json, subprocess, yaml, statistics
corpus = yaml.safe_load(open("/home/user/wt-golden/evals/review/golden_comment_prs.yaml"))
ROOT = "/home/user/bench-repos"
dirs = {"getsentry/sentry": "sentry", "calcom/cal.com": "cal.com", "grafana/grafana": "grafana", "keycloak/keycloak": "keycloak", "discourse/discourse": "discourse"}
rows = {}
for pr in corpus["prs"]:
    repo = f"{ROOT}/{dirs[pr['repository']]}"
    r = subprocess.run(["git", "-C", repo, "diff", "--numstat", pr["base_sha"], pr["head_sha"]], capture_output=True, text=True, timeout=900)
    if r.returncode != 0:
        # planted commits live in the fork clone
        fork = repo + "-greptile"
        r = subprocess.run(["git", "-C", fork, "diff", "--numstat", pr["base_sha"], pr["head_sha"]], capture_output=True, text=True, timeout=900)
    files = adds = dels = 0
    for line in r.stdout.splitlines():
        a, d, _p = line.split("\t", 2)
        files += 1
        adds += int(a) if a.isdigit() else 0
        dels += int(d) if d.isdigit() else 0
    rows[pr["id"]] = (files, adds, dels, r.returncode)
json.dump(rows, open("/home/user/bench-data/pr_sizes.json", "w"), indent=1)
lines = sorted(a + d for f, a, d, rc in rows.values())
print("n", len(rows), "rc!=0:", [k for k, v in rows.items() if v[3]])
print("changed lines: min", lines[0], "median", statistics.median(lines), "p75", lines[int(len(lines)*.75)], "p90", lines[int(len(lines)*.9)], "max", lines[-1], "mean", round(statistics.fmean(lines)))
print("files: median", statistics.median(f for f, a, d, rc in rows.values()), "max", max(f for f, a, d, rc in rows.values()))
print("<=60 lines:", sum(1 for l in lines if l <= 60), " 61-300:", sum(1 for l in lines if 60 < l <= 300), " 301-1500:", sum(1 for l in lines if 300 < l <= 1500), " >1500:", sum(1 for l in lines if l > 1500))
for k, v in rows.items(): print(k, v[:3])
