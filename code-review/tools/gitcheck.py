import json, subprocess, pathlib
ROOT = pathlib.Path("/home/user/bench-repos")
facts = json.load(open("/home/user/bench-data/gitfacts_raw.json"))
def git(repo, *a):
    r = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=600)
    return r.returncode, r.stdout.strip(), r.stderr.strip()
res = {}
for k, v in facts.items():
    up = ROOT / v["repo"]; fork = ROOT / f'{v["repo"]}-greptile'
    h, b = v["head"], v["base_tip"]
    where = None
    for name, repo in (("upstream", up), ("fork", fork)):
        if git(repo, "cat-file", "-e", f"{h}^{{commit}}")[0] == 0 and git(repo, "cat-file", "-e", f"{b}^{{commit}}")[0] == 0:
            where = (name, repo); break
    if not where:
        res[k] = dict(where=None); print(k, "NOT AVAILABLE locally"); continue
    name, repo = where
    rc, p1, _ = git(repo, "rev-parse", f"{h}^1")
    rc2, mb, err = git(repo, "merge-base", b, h)
    rc3, cnt, _ = git(repo, "rev-list", "--count", f"{b}..{h}")
    res[k] = dict(where=name, parent1=p1 if rc == 0 else None, merge_base=mb if rc2 == 0 else None, ahead=cnt)
    print(k, name, "p1==base" if p1 == b else f"p1={p1[:10]}", "mb==base" if mb == b else f"mb={mb[:10] if mb else err[:40]}", "ahead", cnt)
json.dump(res, open("/home/user/bench-data/gitcheck.json", "w"), indent=1)
