# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run2-dev-score`, 2026-10-26T05:30:23+00:00. Scored 30 of 30 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run2-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 28 questions: 0 answered from the cache, 28 asked now (28 calls, $0.5115). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 30 | 30 | 38 | 30 | 44 | 50 | 47 | 50 / 52 |
| language: go | 10 | 8 | 8 | 8 | 50 | 50 | 50 | 56 / 55 |
| language: python | 10 | 9 | 11 | 12 | 45 | 43 | 44 | 45 / 44 |
| language: typescript | 10 | 13 | 19 | 10 | 41 | 57 | 47 | 50 / 55 |
| repository: calcom/cal.com | 10 | 13 | 19 | 10 | 41 | 57 | 47 | 50 / 55 |
| repository: getsentry/sentry | 10 | 9 | 11 | 12 | 45 | 43 | 44 | 45 / 44 |
| repository: grafana/grafana | 10 | 8 | 8 | 8 | 50 | 50 | 50 | 56 / 55 |

Comments posted 74; matched only to an excluded (Low) golden comment 6; golden comments counted 60, excluded 25; pull requests with at least one catch 21 of 30.

Recall by golden severity: Critical 4/4 (100%); High 18/31 (58%); Medium 8/25 (32%).

## Cost of the reviews (30 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 150 | 5.0 | 3.0 | 0 |
| Input tokens | 9897215 | 329907.2 | 180014.0 | 0 |
| Output tokens | 218512 | 7283.7 | 4376.0 | 0 |
| Dollars (the CLI's list-price estimate) | $13.46 | $0.4485 | $0.1980 | 0 |
| Wall seconds | 1574.5 | 52.5 | 50.0 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 68203/1903 | $0.0372 | 58.8 |  |
| sentry-02 | python | 1 | 1 | 0 | 2 | 0+0 | 4 | 191610/5546 | $0.1341 | 64.9 |  |
| sentry-03 | python | 2 | 0 | 2 | 1 | 0+2 | 5 | 345192/8355 | $0.4994 | 71.6 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 3 | 95019/4255 | $0.2517 | 52.8 |  |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 2158451/27293 | $2.84 | 118.8 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 3 | 135366/4250 | $0.1041 | 62.1 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 162112/2711 | $0.2605 | 51.0 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 108611/2634 | $0.0597 | 59.2 |  |
| sentry-09 | python | 9 | 0 | 6 | 1 | 3+2 | 9 | 906261/18539 | $1.23 | 95.2 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 354644/4398 | $0.1605 | 60.0 |  |
| calcom-01 | typescript | 7 | 0 | 6 | 1 | 1+1 | 20 | 1525246/26589 | $2.54 | 100.4 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 191278/3526 | $0.0928 | 23.4 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 322771/12383 | $0.7249 | 49.6 |  |
| calcom-04 | typescript | 5 | 3 | 2 | 0 | 0+2 | 5 | 267037/6650 | $0.1415 | 28.9 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 86102/1963 | $0.1776 | 25.6 |  |
| calcom-06 | typescript | 4 | 1 | 3 | 1 | 0+0 | 9 | 348823/14442 | $0.3888 | 58.9 |  |
| calcom-07 | typescript | 1 | 1 | 0 | 1 | 0+0 | 2 | 58039/2357 | $0.1416 | 19.1 |  |
| calcom-08 | typescript | 7 | 3 | 4 | 2 | 0+0 | 11 | 566828/17853 | $1.06 | 76.5 |  |
| calcom-09 | typescript | 3 | 1 | 2 | 1 | 0+0 | 6 | 129534/8529 | $0.2527 | 47.2 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 2 | 109580/4861 | $0.0843 | 42.4 |  |
| grafana-01 | go | 3 | 1 | 2 | 2 | 0+2 | 3 | 244828/4512 | $0.3281 | 38.2 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 2 | 74239/2895 | $0.2184 | 34.0 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 308050/4354 | $0.4057 | 35.3 |  |
| grafana-04 | go | 1 | 0 | 1 | 0 | 0+1 | 2 | 168750/3734 | $0.1766 | 47.8 |  |
| grafana-05 | go | 4 | 2 | 2 | 0 | 0+0 | 5 | 481426/7632 | $0.6527 | 53.7 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 4 | 241677/6552 | $0.1640 | 50.4 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 2 | 122031/4170 | $0.2285 | 44.4 |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 25730/1133 | $0.0227 | 28.8 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58159/2315 | $0.0401 | 40.0 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 41618/2178 | $0.0369 | 35.5 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
