# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `b7k-dev-score`, 2026-10-26T06:11:07+00:00. Scored 14 of 14 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report b7k-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 11 questions: 0 answered from the cache, 11 asked now (11 calls, $0.2029). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 14 | 15 | 12 | 18 | 56 | 45 | 50 | 63 / 55 |
| language: go | 4 | 0 | 3 | 7 | 0 | 0 | 0 | 0 / 0 |
| language: python | 5 | 8 | 2 | 7 | 80 | 53 | 64 | 90 / 69 |
| language: typescript | 5 | 7 | 7 | 4 | 50 | 64 | 56 | 57 / 62 |
| repository: calcom/cal.com | 5 | 7 | 7 | 4 | 50 | 64 | 56 | 57 / 62 |
| repository: getsentry/sentry | 5 | 8 | 2 | 7 | 80 | 53 | 64 | 90 / 69 |
| repository: grafana/grafana | 4 | 0 | 3 | 7 | 0 | 0 | 0 | 0 / 0 |

Comments posted 27; matched only to an excluded (Low) golden comment 0; golden comments counted 33, excluded 12; pull requests with at least one catch 9 of 14.

Recall by golden severity: Critical 2/2 (100%); High 5/15 (33%); Medium 8/16 (50%).

## Cost of the reviews (14 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 73 | 5.2 | 5.0 | 0 |
| Input tokens | 3055689 | 218263.5 | 221027.0 | 0 |
| Output tokens | 98301 | 7021.5 | 5963.0 | 0 |
| Dollars (the CLI's list-price estimate) | $4.95 | $0.3532 | $0.3575 | 0 |
| Wall seconds | 696.1 | 49.7 | 50.6 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 2 | 1 | 1 | 2 | 0+1 | 2 | 87406/4492 | $0.1723 | 65.0 |  |
| sentry-02 | python | 3 | 2 | 1 | 1 | 0+0 | 7 | 278977/9766 | $0.4361 | 65.7 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 6 | 228384/7792 | $0.4048 | 54.9 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 5 | 293641/7147 | $0.4326 | 62.7 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 6 | 245512/5673 | $0.3512 | 53.6 |  |
| calcom-03 | typescript | 6 | 1 | 5 | 1 | 0+2 | 13 | 570807/21307 | $0.9049 | 93.5 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 4 | 129969/4091 | $0.2702 | 22.8 |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | 3 | 107106/4723 | $0.1842 | 31.4 |  |
| calcom-09 | typescript | 3 | 1 | 2 | 1 | 0+0 | 6 | 121444/8365 | $0.2436 | 62.8 |  |
| calcom-10 | typescript | 3 | 3 | 0 | 1 | 0+1 | 4 | 213670/6415 | $0.3653 | 35.9 |  |
| grafana-01 | go | 2 | 0 | 2 | 3 | 0+2 | 4 | 245563/5767 | $0.3257 | 47.7 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 5 | 201380/5742 | $0.3638 | 35.3 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 7 | 305829/6159 | $0.4695 | 37.7 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 26001/862 | $0.0211 | 27.3 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
