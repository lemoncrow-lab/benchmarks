"""Collect, with git only, the head and base commits of the 50 fork pull requests. Nothing is built or run."""
import json, subprocess, pathlib, sys
ROOT = pathlib.Path("/home/user/bench-repos")
SRC = pathlib.Path("/home/user/bench-data/greptile-comments")
REPOS = ["sentry", "cal.com", "grafana", "keycloak", "discourse"]

def git(repo, *a, check=False):
    r = subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, timeout=300)
    return r.returncode, r.stdout.strip(), r.stderr.strip()

facts = {}
for repo in REPOS:
    fork = ROOT / f"{repo}-greptile"
    up = ROOT / repo
    rc, out, err = git(fork, "ls-remote", "origin", "refs/pull/*/head", "refs/pull/*/merge", "refs/heads/*")
    if rc: print("ls-remote failed", repo, err); sys.exit(1)
    refs = {}
    for line in out.splitlines():
        sha, ref = line.split()
        refs[ref] = sha
    for n in range(1, 11):
        raw = json.loads((SRC / f"{repo}-{n:02d}.json").read_text())["extraction"]
        base_branch, head_branch = raw["base"], raw["head"]
        head = refs.get(f"refs/pull/{n}/head")
        merge = refs.get(f"refs/pull/{n}/merge")
        base_tip = refs.get(f"refs/heads/{base_branch}")
        head_branch_tip = refs.get(f"refs/heads/{head_branch}")
        facts[f"{repo}-{n:02d}"] = dict(repo=repo, pull=n, title=raw["title"], base_branch=base_branch, head_branch=head_branch,
                                         head=head, base_tip=base_tip, merge_ref=merge, head_branch_tip=head_branch_tip)
json.dump(facts, open("/home/user/bench-data/gitfacts_raw.json", "w"), indent=1)
for k, v in facts.items():
    print(k, (v["head"] or "")[:10], (v["base_tip"] or "NONE")[:10], (v["merge_ref"] or "-")[:10], "head==branchtip" if v["head"]==v["head_branch_tip"] else f"headbranch={ (v['head_branch_tip'] or 'NONE')[:10]}", v["base_branch"])
