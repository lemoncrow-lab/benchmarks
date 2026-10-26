# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run3-dev-score`, 2026-10-26T07:19:23+00:00. Scored 30 of 30 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run3-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 26 questions: 0 answered from the cache, 26 asked now (26 calls, $0.4897). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 30 | 27 | 26 | 33 | 51 | 45 | 48 | 53 / 49 |
| language: go | 10 | 6 | 5 | 10 | 55 | 38 | 44 | 55 / 44 |
| language: python | 10 | 9 | 7 | 12 | 56 | 43 | 49 | 56 / 49 |
| language: typescript | 10 | 12 | 14 | 11 | 46 | 52 | 49 | 50 / 52 |
| repository: calcom/cal.com | 10 | 12 | 14 | 11 | 46 | 52 | 49 | 50 / 52 |
| repository: getsentry/sentry | 10 | 9 | 7 | 12 | 56 | 43 | 49 | 56 / 49 |
| repository: grafana/grafana | 10 | 6 | 5 | 10 | 55 | 38 | 44 | 55 / 44 |

Comments posted 58; matched only to an excluded (Low) golden comment 5; golden comments counted 60, excluded 25; pull requests with at least one catch 19 of 30.

Recall by golden severity: Critical 4/4 (100%); High 14/31 (45%); Medium 9/25 (36%).

## Cost of the reviews (30 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 157 | 5.2 | 4.0 | 0 |
| Input tokens | 9723284 | 324109.5 | 180059.5 | 0 |
| Output tokens | 207296 | 6909.9 | 4288.0 | 0 |
| Dollars (the CLI's list-price estimate) | $15.87 | $0.5289 | $0.3083 | 0 |
| Wall seconds | 1738.2 | 57.9 | 54.3 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 22074/2052 | $0.0969 | 64.3 |  |
| sentry-02 | python | 1 | 1 | 0 | 2 | 0+0 | 4 | 154864/4590 | $0.3501 | 65.0 |  |
| sentry-03 | python | 3 | 0 | 2 | 1 | 1+2 | 6 | 333255/6942 | $0.4843 | 84.1 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 3 | 120808/3452 | $0.2494 | 51.0 |  |
| sentry-05 | python | 2 | 0 | 1 | 2 | 1+1 | 20 | 1988830/24334 | $2.79 | 124.3 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 4 | 178476/4220 | $0.3265 | 64.9 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 173205/2584 | $0.2553 | 56.4 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 108307/2659 | $0.1815 | 61.4 |  |
| sentry-09 | python | 5 | 0 | 4 | 1 | 1+2 | 10 | 762663/16299 | $1.18 | 94.6 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 302069/4356 | $0.4851 | 58.1 |  |
| calcom-01 | typescript | 7 | 0 | 6 | 1 | 1+1 | 20 | 1553302/26263 | $2.53 | 104.5 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 181643/3519 | $0.2901 | 31.3 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 388711/13256 | $0.7039 | 70.2 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 352084/10572 | $0.5936 | 54.1 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 110752/2201 | $0.1925 | 32.0 |  |
| calcom-06 | typescript | 1 | 0 | 1 | 2 | 0+0 | 9 | 306491/12307 | $0.5725 | 70.3 |  |
| calcom-07 | typescript | 1 | 1 | 0 | 1 | 0+0 | 2 | 58212/2926 | $0.1477 | 24.6 |  |
| calcom-08 | typescript | 6 | 3 | 3 | 2 | 0+0 | 11 | 595617/16433 | $1.06 | 79.4 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 6 | 141889/6001 | $0.2579 | 48.0 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 2 | 137073/4733 | $0.2662 | 43.8 |  |
| grafana-01 | go | 2 | 0 | 2 | 3 | 0+2 | 4 | 200908/4494 | $0.3375 | 44.2 |  |
| grafana-02 | go | 0 | 0 | 0 | 1 | 0+1 | 2 | 130165/2551 | $0.2326 | 37.6 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 224846/3264 | $0.3782 | 42.0 |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | 2 | 232800/4024 | $0.2230 | 53.1 |  |
| grafana-05 | go | 3 | 1 | 2 | 1 | 0+0 | 6 | 461961/7644 | $0.6695 | 54.6 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 235486/6619 | $0.4314 | 60.9 |  |
| grafana-07 | go | 1 | 0 | 0 | 0 | 1+1 | 2 | 97525/3268 | $0.2145 | 43.6 |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 26378/1294 | $0.0573 | 34.4 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58127/1990 | $0.1299 | 41.2 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 84763/2449 | $0.1804 | 44.1 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
