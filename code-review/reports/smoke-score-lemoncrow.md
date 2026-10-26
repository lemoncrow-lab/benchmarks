# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `smoke-score-lemoncrow`, 2026-10-26T01:51:00+00:00. Scored 2 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report smoke-lemoncrow-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: n/a), prompt `golden-judge-1` / `cfe685620f23bc1a`. 0 questions: 0 answered from the cache, 0 asked now (0 calls, n/a). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 2 | 0 | 0 | 4 | n/a | 0 | 0 | n/a / 0 |
| language: go | 1 | 0 | 0 | 2 | n/a | 0 | 0 | n/a / 0 |
| language: typescript | 1 | 0 | 0 | 2 | n/a | 0 | 0 | n/a / 0 |
| repository: calcom/cal.com | 1 | 0 | 0 | 2 | n/a | 0 | 0 | n/a / 0 |
| repository: grafana/grafana | 1 | 0 | 0 | 2 | n/a | 0 | 0 | n/a / 0 |

Comments posted 0; matched only to an excluded (Low) golden comment 0; golden comments counted 4, excluded 0; pull requests with at least one catch 0 of 2.

Recall by golden severity: Critical 0/0 (n/a%); High 0/3 (0%); Medium 0/1 (0%).

## Cost of the reviews (2 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 4 | 2.0 | 2.0 | 0 |
| Input tokens | 65651 | 32825.5 | 32825.5 | 0 |
| Output tokens | 3909 | 1954.5 | 1954.5 | 0 |
| Dollars (the CLI's list-price estimate) | $0.1623 | $0.0812 | $0.0812 | 0 |
| Wall seconds | 58.9 | 29.5 | 29.5 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| calcom-09 | typescript | 0 | 0 | 0 | 2 | 0+0 | 3 | 44706/3290 | $0.1198 | 35.8 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 20945/619 | $0.0425 | 23.1 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
