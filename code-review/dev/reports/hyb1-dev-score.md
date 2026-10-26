# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `hyb1-dev-score`, 2026-10-26T05:39:59+00:00. Scored 11 of 11 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report hyb1-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 11 questions: 7 answered from the cache, 4 asked now (4 calls, $0.0802). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 11 | 11 | 29 | 15 | 28 | 42 | 33 | 28 / 33 |
| language: go | 1 | 1 | 2 | 2 | 33 | 33 | 33 | 33 / 33 |
| language: python | 3 | 0 | 10 | 4 | 0 | 0 | 0 | 0 / 0 |
| language: typescript | 7 | 10 | 17 | 9 | 37 | 53 | 43 | 37 / 43 |
| repository: calcom/cal.com | 7 | 10 | 17 | 9 | 37 | 53 | 43 | 37 / 43 |
| repository: getsentry/sentry | 3 | 0 | 10 | 4 | 0 | 0 | 0 | 0 / 0 |
| repository: grafana/grafana | 1 | 1 | 2 | 2 | 33 | 33 | 33 | 33 / 33 |

Comments posted 43; matched only to an excluded (Low) golden comment 3; golden comments counted 26, excluded 13; pull requests with at least one catch 7 of 11.

Recall by golden severity: Critical 1/1 (100%); High 9/14 (64%); Medium 1/11 (9%).

Scored although the review was partial: `sentry-05`, `calcom-01`, `grafana-01`.

## Cost of the reviews (11 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 103 | 9.4 | 9 | 0 |
| Input tokens | 6954540 | 632230.9 | 343571 | 0 |
| Output tokens | 150512 | 13682.9 | 12383 | 0 |
| Dollars (the CLI's list-price estimate) | $10.18 | $0.9251 | $0.4994 | 0 |
| Wall seconds | 244.5 | 22.2 | 14.9 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-03 | python | 2 | 0 | 2 | 1 | 0+2 | 5 | 345192/8355 | $0.4994 | 39.5 |  |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 2158451/27293 | $2.84 | 50.7 | the model-call budget ran out |
| sentry-09 | python | 6 | 0 | 5 | 1 | 1+2 | 10 | 925352/18962 | $1.27 | 51.1 |  |
| calcom-01 | typescript | 7 | 0 | 6 | 1 | 1+1 | 20 | 1525246/26589 | $2.54 | 21.0 | the model-call budget ran out |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 323510/12383 | $0.7280 | 10.0 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 272560/6785 | $0.1558 | 9.8 |  |
| calcom-06 | typescript | 4 | 1 | 3 | 1 | 0+0 | 9 | 343571/14363 | $0.3899 | 8.5 |  |
| calcom-08 | typescript | 6 | 2 | 4 | 3 | 0+0 | 11 | 564125/17731 | $1.07 | 11.4 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 6 | 136439/8624 | $0.2594 | 15.7 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 3 | 115266/4915 | $0.0982 | 12.0 |  |
| grafana-01 | go | 3 | 1 | 2 | 2 | 0+2 | 3 | 244828/4512 | $0.3281 | 14.9 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
