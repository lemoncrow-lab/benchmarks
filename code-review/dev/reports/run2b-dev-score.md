# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run2b-dev-score`, 2026-10-26T04:59:28+00:00. Scored 14 of 14 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run2b-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 13 questions: 0 answered from the cache, 13 asked now (13 calls, $0.2325). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 14 | 18 | 12 | 15 | 60 | 55 | 57 | 67 / 62 |
| language: go | 4 | 4 | 2 | 5 | 67 | 44 | 53 | 67 / 53 |
| language: python | 5 | 6 | 4 | 6 | 60 | 50 | 55 | 70 / 61 |
| language: typescript | 5 | 8 | 6 | 4 | 57 | 67 | 62 | 64 / 67 |
| repository: calcom/cal.com | 5 | 8 | 6 | 4 | 57 | 67 | 62 | 64 / 67 |
| repository: getsentry/sentry | 5 | 6 | 4 | 6 | 60 | 50 | 55 | 70 / 61 |
| repository: grafana/grafana | 4 | 4 | 2 | 5 | 67 | 44 | 53 | 67 / 53 |

Comments posted 30; matched only to an excluded (Low) golden comment 0; golden comments counted 33, excluded 8; pull requests with at least one catch 13 of 14.

Recall by golden severity: Critical 3/4 (75%); High 11/19 (58%); Medium 4/10 (40%).

## Cost of the reviews (14 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 48 | 3.4 | 3.0 | 0 |
| Input tokens | 2503556 | 178825.4 | 183500.0 | 0 |
| Output tokens | 77527 | 5537.6 | 5189.0 | 0 |
| Dollars (the CLI's list-price estimate) | $4.38 | $0.3127 | $0.3225 | 0 |
| Wall seconds | 697.9 | 49.8 | 53.1 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 2 | 1 | 1 | 2 | 0+1 | 1 | 45924/3071 | $0.1166 | 66.9 |  |
| sentry-02 | python | 4 | 2 | 2 | 1 | 0+0 | 4 | 328620/7355 | $0.4326 | 78.3 |  |
| sentry-06 | python | 2 | 1 | 1 | 3 | 0+1 | 3 | 189553/6233 | $0.3328 | 66.6 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 107793/2425 | $0.1778 | 56.7 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 294972/3795 | $0.4611 | 51.4 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 236501/4488 | $0.3199 | 26.8 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 5 | 264729/8298 | $0.5327 | 32.6 |  |
| calcom-06 | typescript | 3 | 1 | 2 | 1 | 0+0 | 9 | 329933/12633 | $0.5758 | 54.9 |  |
| calcom-09 | typescript | 3 | 1 | 2 | 1 | 0+0 | 6 | 129419/8698 | $0.3010 | 57.5 |  |
| calcom-10 | typescript | 3 | 2 | 1 | 2 | 0+1 | 3 | 177447/5890 | $0.3250 | 35.9 |  |
| grafana-06 | go | 4 | 2 | 2 | 1 | 0+0 | 4 | 215016/7729 | $0.4175 | 55.9 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 40221/1352 | $0.0601 | 32.9 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58129/2181 | $0.1321 | 36.8 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 85299/3379 | $0.1924 | 44.9 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
