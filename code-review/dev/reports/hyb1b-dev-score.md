# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `hyb1b-dev-score`, 2026-10-26T05:40:00+00:00. Scored 3 of 3 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report hyb1b-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 3 questions: 3 answered from the cache, 0 asked now (0 calls, n/a). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 3 | 4 | 4 | 1 | 50 | 80 | 62 | 62 / 71 |
| language: go | 3 | 4 | 4 | 1 | 50 | 80 | 62 | 62 / 71 |
| repository: grafana/grafana | 3 | 4 | 4 | 1 | 50 | 80 | 62 | 62 / 71 |

Comments posted 9; matched only to an excluded (Low) golden comment 1; golden comments counted 5, excluded 1; pull requests with at least one catch 2 of 3.

Recall by golden severity: Critical 0/0 (n/a%); High 2/2 (100%); Medium 2/3 (67%).

## Cost of the reviews (3 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 12 | 4.0 | 5 | 0 |
| Input tokens | 857248 | 285749.3 | 253791 | 0 |
| Output tokens | 18419 | 6139.7 | 6617 | 0 |
| Dollars (the CLI's list-price estimate) | $1.07 | $0.3552 | $0.2285 | 0 |
| Wall seconds | 59.6 | 19.9 | 20.1 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| grafana-05 | go | 4 | 2 | 2 | 0 | 0+0 | 5 | 481426/7632 | $0.6527 | 23.3 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 253791/6617 | $0.1842 | 20.1 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 2 | 122031/4170 | $0.2285 | 16.3 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
