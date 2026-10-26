# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `largepr-auto-score`, 2026-10-26T13:15:49+00:00. Scored 2 of 2 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report largepr-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 2 questions: 0 answered from the cache, 2 asked now (2 calls, $0.0371). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: no. No `benchmark_summary` was written because the run was limited to 2 pull request(s) with --pr; the benchmark ran on a checkout with uncommitted changes to tracked files, so its commit is not the code that ran.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 2 | 0 | 8 | 3 | 0 | 0 | 0 | 0 / 0 |
| language: python | 2 | 0 | 8 | 3 | 0 | 0 | 0 | 0 / 0 |
| repository: getsentry/sentry | 2 | 0 | 8 | 3 | 0 | 0 | 0 | 0 / 0 |

Comments posted 11; matched only to an excluded (Low) golden comment 3; golden comments counted 3, excluded 3; pull requests with at least one catch 0 of 2.

Recall by golden severity: Critical 0/0 (n/a%); High 0/1 (0%); Medium 0/2 (0%).

## Cost of the reviews (2 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 22 | 11.0 | 11.0 | 0 |
| Input tokens | 2587594 | 1293797.0 | 1293797.0 | 0 |
| Output tokens | 38592 | 19296.0 | 19296.0 | 0 |
| Dollars (the CLI's list-price estimate) | $3.12 | $1.56 | $1.56 | 0 |
| Wall seconds | 263.6 | 131.8 | 131.8 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-05 | python | 6 | 0 | 5 | 2 | 1+1 | 13 | 1850097/22339 | $1.97 | 170.6 |  |
| sentry-09 | python | 5 | 0 | 3 | 1 | 2+2 | 9 | 737497/16253 | $1.15 | 93.0 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
