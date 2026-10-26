# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run2s-dev-score`, 2026-10-26T04:45:56+00:00. Scored 14 of 14 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run2s-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 13 questions: 0 answered from the cache, 13 asked now (13 calls, $0.2290). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 14 | 22 | 6 | 11 | 79 | 67 | 72 | 82 / 74 |
| language: go | 4 | 4 | 2 | 5 | 67 | 44 | 53 | 67 / 53 |
| language: python | 5 | 7 | 0 | 5 | 100 | 58 | 74 | 100 / 74 |
| language: typescript | 5 | 11 | 4 | 1 | 73 | 92 | 81 | 80 / 86 |
| repository: calcom/cal.com | 5 | 11 | 4 | 1 | 73 | 92 | 81 | 80 / 86 |
| repository: getsentry/sentry | 5 | 7 | 0 | 5 | 100 | 58 | 74 | 100 / 74 |
| repository: grafana/grafana | 4 | 4 | 2 | 5 | 67 | 44 | 53 | 67 / 53 |

Comments posted 28; matched only to an excluded (Low) golden comment 0; golden comments counted 33, excluded 8; pull requests with at least one catch 13 of 14.

Recall by golden severity: Critical 4/4 (100%); High 12/19 (63%); Medium 6/10 (60%).

## Cost of the reviews (14 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 49 | 3.5 | 3.0 | 0 |
| Input tokens | 2233121 | 159508.6 | 138898.0 | 0 |
| Output tokens | 69263 | 4947.4 | 4204.5 | 0 |
| Dollars (the CLI's list-price estimate) | $4.25 | $0.3035 | $0.3088 | 0 |
| Wall seconds | 665.1 | 47.5 | 50.8 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 22200/1764 | $0.0945 | 57.1 |  |
| sentry-02 | python | 1 | 1 | 0 | 2 | 0+0 | 4 | 129117/3957 | $0.3381 | 60.4 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 3 | 136275/4326 | $0.3020 | 59.2 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 111106/2593 | $0.1870 | 56.1 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 298821/4083 | $0.4769 | 60.8 |  |
| calcom-02 | typescript | 3 | 1 | 2 | 0 | 0+1 | 3 | 195319/4857 | $0.3156 | 27.1 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 5 | 353566/9281 | $0.5702 | 36.5 |  |
| calcom-06 | typescript | 3 | 2 | 1 | 0 | 0+0 | 9 | 299434/13257 | $0.5591 | 56.5 |  |
| calcom-09 | typescript | 2 | 2 | 0 | 0 | 0+0 | 7 | 141521/7499 | $0.3204 | 45.6 |  |
| calcom-10 | typescript | 3 | 3 | 0 | 1 | 0+1 | 3 | 161529/4721 | $0.2991 | 44.0 |  |
| grafana-06 | go | 4 | 2 | 2 | 1 | 0+0 | 4 | 224847/7439 | $0.4247 | 56.2 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 26123/912 | $0.0520 | 27.4 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58334/1907 | $0.1295 | 36.6 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 74929/2667 | $0.1794 | 41.7 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
