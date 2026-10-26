# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `dd2-dev-score`, 2026-10-26T06:19:07+00:00. Scored 11 of 11 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report dd2-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 11 questions: 10 answered from the cache, 1 asked now (1 calls, $0.0206). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 11 | 13 | 27 | 13 | 32 | 50 | 39 | 32 / 39 |
| language: go | 3 | 5 | 3 | 3 | 62 | 62 | 62 | 62 / 62 |
| language: python | 2 | 0 | 8 | 3 | 0 | 0 | 0 | 0 / 0 |
| language: typescript | 6 | 8 | 16 | 7 | 33 | 53 | 41 | 33 / 41 |
| repository: calcom/cal.com | 6 | 8 | 16 | 7 | 33 | 53 | 41 | 33 / 41 |
| repository: getsentry/sentry | 2 | 0 | 8 | 3 | 0 | 0 | 0 | 0 / 0 |
| repository: grafana/grafana | 3 | 5 | 3 | 3 | 62 | 62 | 62 | 62 / 62 |

Comments posted 43; matched only to an excluded (Low) golden comment 3; golden comments counted 26, excluded 10; pull requests with at least one catch 8 of 11.

Recall by golden severity: Critical 0/0 (n/a%); High 10/15 (67%); Medium 3/11 (27%).

## Cost of the reviews (11 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 107 | 9.7 | 9 | 0 |
| Input tokens | 7193635 | 653966.8 | 351978 | 0 |
| Output tokens | 151329 | 13757.2 | 12476 | 0 |
| Dollars (the CLI's list-price estimate) | $10.39 | $0.9444 | $0.6783 | 0 |
| Wall seconds | 312.9 | 28.4 | 24.5 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 2082783/26300 | $2.74 | 57.5 |  |
| sentry-09 | python | 6 | 0 | 5 | 1 | 1+2 | 10 | 915976/18772 | $1.26 | 52.5 |  |
| calcom-01 | typescript | 7 | 0 | 6 | 1 | 1+1 | 20 | 1525246/26589 | $2.54 | 24.5 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 331167/12476 | $0.7364 | 15.6 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 274500/6785 | $0.1638 | 12.2 |  |
| calcom-06 | typescript | 4 | 1 | 3 | 1 | 0+0 | 9 | 351978/14557 | $0.3969 | 17.3 |  |
| calcom-08 | typescript | 5 | 2 | 3 | 3 | 0+0 | 11 | 574938/18048 | $1.08 | 21.1 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 6 | 136623/8624 | $0.2598 | 21.6 |  |
| grafana-01 | go | 2 | 1 | 1 | 2 | 0+2 | 4 | 257335/4719 | $0.3506 | 28.6 |  |
| grafana-05 | go | 3 | 2 | 1 | 0 | 0+0 | 6 | 495300/7853 | $0.6783 | 36.8 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 247789/6606 | $0.1794 | 25.1 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
