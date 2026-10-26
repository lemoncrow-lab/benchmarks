# Code review: golden-comment benchmark data

Run data behind LemonCrow's published code-review benchmark: the public 50-pull-request
golden-comment set (answer key: https://github.com/ai-code-review-evaluations/golden_comments,
read at run time and not stored here). The harness, corpus file and published result live in
[lemoncrow-dev](https://github.com/lemoncrow-lab/lemoncrow-dev): `evals/review/golden_comment_prs.yaml`,
`evals/review/published/` and `docs/reference/review-benchmark.md`.

Every run below used Sonnet through the `claude` CLI, and every score used the same judge
(`claude` / `sonnet`, prompt `golden-judge-1`, digest `cfe685620f23bc1a…`). Dates are 2026-10-26.

## Main runs (all 50 pull requests)

| Run | Depth | TP / FP / FN | Precision / Recall / F | Files |
| --- | --- | --- | --- | --- |
| **run 3, published** | thorough | 47 / 62 / 50 | 43 / 48 / 46 | `holdout-private/reports/golden50-run3-{thorough,score}.*`, `holdout-private/records-run3/` |
| run 2 | auto | 41 / 48 / 56 | 46 / 42 / 44 | `holdout-private/reports/golden50-run2-{auto,score,score-v2}.*`, `holdout-private/records-run2/` |
| run 1 (earlier engine) | auto | 26 / 26 / 71 | 50 / 27 / 35 | `holdout-private/reports/golden50-lemoncrow-{auto,score}.*`, `holdout-private/records-run1/` |
| other reviewer, same judge | n/a | 49 / 175 / 48 | 22 / 51 / 31 | `reports/golden50-competitor.*`, input `greptile-comments-normalised/` |

`holdout-private/` is a historical name. Keycloak and Discourse (20 pull requests) were held out
of tuning until the result was published on 2026-10-26, so they no longer count as a hold-out;
future tuning needs a fresh one. `holdout-private/attempts/run3-argv-fail/` is an aborted
first attempt at run 3, kept for the record (not scored into anything published).

## Layout

| Path | What |
| --- | --- |
| `greptile-comments/<repo>-<NN>.json` | one raw extraction per fork pull request (`NN` is the number in `ai-code-review-evaluation/<repo>-greptile`), read from the public pages on 2026-10-26. The reading tool quotes at most 125 characters, so long comments are faithful paraphrases. Holds the bot's summary line, every bot item with date and path, other authors seen, and `files_tab` additions where the conversation page hid threads. Three pages came back cut off; re-collecting them with `gh api` is still open. |
| `greptile-comments-normalised/<id>.json` | the same reduced by `tools/normalise.py` to the scorer's input (`{"comments": [{id, path, lines, text}], "extraction": {...}}`), named by corpus id. Inline items from the first review only; collapsed placeholders, items marked duplicate and exact (path, text) repeats dropped. |
| `gitfacts_raw.json`, `gitcheck.json`, `pr_sizes.json` | head, base-branch tip, merge ref, merge base and diff size of each pull request, from git. |
| `tools/` | the scripts that made the files above (`save.py`, `add_files_tab.py`, `normalise.py`, `gitfacts.py`, `gitcheck.py`, `titlematch.py`, `make_corpus.py`, `sizes.py`). |
| `judge-cache/` | judge answers keyed by request digest: re-scoring with the same judge prompt is free (`golden-score --cached-only` never calls the judge). |
| `holdout-private/` | the three full 50-PR runs above: benchmark reports, score reports, run logs and per-PR records. |
| `dev/` | tuning runs on the 30-pull-request development set: `reports/<name>-dev-{auto,score}.*` and `records-<name>/`. `largepr-*` are the large-PR call-budget study (`research_notes/LemonCrow strategy memo assessment/large_pr_tuning.md` in lemoncrow-dev); the rest feed `recall_tuning.md` and `head_to_head.md` there. `scratch/` holds run logs, prompt statistics and replay traces. |
| `reports/`, `records/run1/` | the smoke run, scripted-model plan runs (`*-fake.*`, `golden50-plan-fake.*`, not quotable) and the other reviewer's score. |

Not stored: the fetched pull request checkouts (about 3.7 GB, re-fetched by the harness from the
corpus) and the scratch LemonCrow store the runs used.

Research notes in lemoncrow-dev cite these files as `/home/user/bench-data/<path>`; that is
`code-review/<path>` here. Reports and logs also carry the absolute paths of the machine that made
them.

## Re-scoring

From a lemoncrow-dev checkout, with this directory beside it:

```bash
uv run lemoncrow dev eval review golden-score --corpus evals/review/golden_comment_prs.yaml ...
```

See `docs/reference/review-benchmark.md` there for the flags (`--reviewer-comments`,
`--reviewer-label`, `--cached-only`, `--out-dir`) and `make benchmark-publish` for the importer.
