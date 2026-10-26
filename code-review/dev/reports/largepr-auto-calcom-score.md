# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `largepr-auto-calcom-score`, 2026-10-26T13:26:32+00:00. Scored 1 of 1 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report largepr-auto-calcom.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 1 questions: 0 answered from the cache, 1 asked now (1 calls, $0.0173). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: no. No `benchmark_summary` was written because the run was limited to 1 pull request(s) with --pr; the benchmark ran on a checkout with uncommitted changes to tracked files, so its commit is not the code that ran.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 1 | 0 | 5 | 1 | 0 | 0 | 0 | 0 / 0 |
| language: typescript | 1 | 0 | 5 | 1 | 0 | 0 | 0 | 0 / 0 |
| repository: calcom/cal.com | 1 | 0 | 5 | 1 | 0 | 0 | 0 | 0 / 0 |

Comments posted 5; matched only to an excluded (Low) golden comment 0; golden comments counted 1, excluded 1; pull requests with at least one catch 0 of 1.

Recall by golden severity: Critical 0/0 (n/a%); High 0/0 (n/a%); Medium 0/1 (0%).

## Cost of the reviews (1 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 15 | 15.0 | 15 | 0 |
| Input tokens | 1121738 | 1121738.0 | 1121738 | 0 |
| Output tokens | 19796 | 19796.0 | 19796 | 0 |
| Dollars (the CLI's list-price estimate) | $0.6123 | $0.6123 | $0.6123 | 0 |
| Wall seconds | 145.3 | 145.3 | 145.3 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| calcom-01 | typescript | 5 | 0 | 5 | 1 | 0+1 | 15 | 1121738/19796 | $0.6123 | 145.3 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
