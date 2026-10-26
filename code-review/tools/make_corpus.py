"""Write evals/review/golden_comment_prs.yaml from the git facts and the page extractions. Ids and commit ids only."""
import json, re, sys, pathlib, yaml

facts = json.load(open("/home/user/bench-data/gitfacts_raw.json"))
GOLD = pathlib.Path("/home/user/bench-repos/golden_comments/code_review_benchmarks")
FILES = {"sentry": "sentry.json", "cal.com": "cal_dot_com.json", "grafana": "grafana.json", "keycloak": "keycloak.json", "discourse": "discourse.json"}
UPSTREAM = {"sentry": "getsentry/sentry", "cal.com": "calcom/cal.com", "grafana": "grafana/grafana", "keycloak": "keycloak/keycloak", "discourse": "discourse/discourse"}
LICENSE = {"sentry": "FSL-1.1-Apache-2.0", "cal.com": "AGPL-3.0", "grafana": "AGPL-3.0", "keycloak": "Apache-2.0", "discourse": "GPL-2.0"}
LANG = {"sentry": "python", "cal.com": "typescript", "grafana": "go", "keycloak": "java", "discourse": "ruby"}
SLUG = {"sentry": "sentry", "cal.com": "calcom", "grafana": "grafana", "keycloak": "keycloak", "discourse": "discourse"}
# The reviewed range is merge-base(base branch, head)..head. For 46 of 50 the base branch tip is that merge base.
BASE_OVERRIDE = {
    "sentry-01": "74618671bff8114fcec8fe77c6260c9a2bc2864a",
    "sentry-03": "83f40559985e1365a43f35ba3febb7ea4fabb5d5",
    "grafana-03": "abd2c9c287630e8aebdec94714af3ce97f1fab11",
}
norm = lambda s: re.sub(r"\s+", " ", s).strip().lower()
prs, mismatches = [], []
for key, v in facts.items():
    repo, n = v["repo"], v["pull"]
    gold = json.load(open(GOLD / FILES[repo]))
    idx = [i for i, g in enumerate(gold) if norm(g["pr_title"]) == norm(v["title"])]
    if len(idx) == 1:
        gi = idx[0]
    elif key == "cal.com-01":
        gi = 9  # matched by content, see the note below
    else:
        raise SystemExit(f"{key}: no golden entry for title {v['title']!r}")
    note = f"fork pull request {n} (base branch {v['base_branch']}, head branch {v['head_branch']}); base_sha is the merge base of the two"
    if key in BASE_OVERRIDE:
        note += " (the base branch has moved since; the merge base is the range the reviewers saw)"
    if key == "cal.com-01":
        note += ("; the pull request's title differs from the answer key's ('" + gold[gi]["pr_title"] +
                 "'): matched by content (the key's comments are about this diff) and by elimination")
        mismatches.append(key)
    prs.append({
        "id": f"{SLUG[repo]}-{n:02d}",
        "repository": UPSTREAM[repo],
        "pull": 0,
        "title": v["title"],
        "license": LICENSE[repo],
        "provenance": {"source": "public_repository", "repository": f"https://github.com/{UPSTREAM[repo]}",
                       "commit": v["head"], "note": note},
        "base_sha": BASE_OVERRIDE.get(key, v["base_tip"]),
        "head_sha": v["head"],
        "labelled": False,
        "golden": {"file": FILES[repo], "index": gi + 1, "title": gold[gi]["pr_title"], "language": LANG[repo], "source_pull": n},
    })
header = """\
# Golden-comment corpus (private): the 50 pull requests of a public benchmark set, scored against an independently
# expanded answer key. Five repositories in five languages (getsentry/sentry Python, calcom/cal.com TypeScript,
# grafana/grafana Go, keycloak/keycloak Java, discourse/discourse Ruby), ten pull requests each. Each pull request is a
# real change that a benchmark author re-opened as a pull request in a fork; this file pins the exact range a reviewer
# was shown (`base_sha`..`head_sha`, both commits fetchable by id from the repository's own URL, because a fork shares
# its parent's objects) and the entry of the answer key that lists the issues in it (`golden`).
#
# What is NOT in this file: any source code, and any golden comment. The answer key has no licence, so it is read at
# run time from its own checkout (`golden_comments.repository`), pinned by commit, and never copied into this
# repository. `lc dev eval review golden-score` refuses a checkout at another commit.
#
# Five heads are single small commits that exist in no upstream history (sentry-01, sentry-02, sentry-03,
# keycloak-01, calcom-01 contain them); the other 45 are unchanged upstream commits. `labelled: false` throughout:
# there is no fix-derived label here, the ground truth is the answer key, and the unit of score is a comment, not a
# label (see docs/reference/review-benchmark.md, "The golden-comment benchmark").
#
# Licence. The repositories are not permissively licensed (FSL-1.1-Apache-2.0, AGPL-3.0, GPL-2.0, Apache-2.0), and the
# answer key has none, so this is a `visibility: private` corpus excluded from the public mirror
# (scripts/public-paths.txt). Write its reports outside the checkout (`--out-dir`).
#
# Provenance of the ids: fork pull request refs and branch tips read with `git ls-remote`; base = merge base of the pull
# request's base branch and head, checked with git against full upstream history; titles read from the pull request
# pages. Who produced the set, and the vendor numbers, are in research_notes/ (private), not here.
"""
doc = {
    "version": 1,
    "id": "golden-comment-prs",
    "visibility": "private",
    "description": "50 pull requests of a public benchmark set, scored against its independently expanded answer key. Not mirrored; see the header.",
    "line_tolerance": 3,
    "match": "either",
    "golden_comments": {
        "repository": "https://github.com/ai-code-review-evaluations/golden_comments",
        "commit": "3f2c8ab794b4ed71c099cbf0a7670555e90906dc",
        "directory": "code_review_benchmarks",
        "licence": "none published: used as a read-only answer key at run time, never copied into this repository",
    },
    "prs": prs,
}
out = pathlib.Path(sys.argv[1])
out.write_text(header + yaml.safe_dump(doc, sort_keys=False, width=118, allow_unicode=True), encoding="utf-8")
print("wrote", out, len(prs), "prs; title mismatches:", mismatches)
