# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run1-dev-score`, 2026-10-26T04:16:01+00:00. Scored 30 of 30 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run1-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 18 questions: 18 answered from the cache, 0 asked now (0 calls, n/a). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 30 | 17 | 19 | 43 | 47 | 28 | 35 | 50 / 37 |
| language: go | 10 | 3 | 4 | 13 | 43 | 19 | 26 | 43 / 26 |
| language: python | 10 | 4 | 5 | 17 | 44 | 19 | 27 | 44 / 27 |
| language: typescript | 10 | 10 | 10 | 13 | 50 | 43 | 47 | 55 / 50 |
| repository: calcom/cal.com | 10 | 10 | 10 | 13 | 50 | 43 | 47 | 55 / 50 |
| repository: getsentry/sentry | 10 | 4 | 5 | 17 | 44 | 19 | 27 | 44 / 27 |
| repository: grafana/grafana | 10 | 3 | 4 | 13 | 43 | 19 | 26 | 43 / 26 |

Comments posted 36; matched only to an excluded (Low) golden comment 0; golden comments counted 60, excluded 25; pull requests with at least one catch 12 of 30.

Recall by golden severity: Critical 0/4 (0%); High 12/31 (39%); Medium 5/25 (20%).

## Cost of the reviews (30 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 149 | 5.0 | 3.0 | 0 |
| Input tokens | 8869049 | 295635.0 | 173292.0 | 0 |
| Output tokens | 187018 | 6233.9 | 3564.0 | 0 |
| Dollars (the CLI's list-price estimate) | $15.19 | $0.5064 | $0.2924 | 0 |
| Wall seconds | 1449.5 | 48.3 | 46.6 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 67418/2211 | $0.1204 | 59.5 |  |
| sentry-02 | python | 0 | 0 | 0 | 3 | 0+0 | 4 | 152015/4555 | $0.3423 | 70.5 |  |
| sentry-03 | python | 0 | 0 | 0 | 1 | 0+2 | 5 | 274337/6299 | $0.4419 | 71.4 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 3 | 107485/3285 | $0.2414 | 45.7 |  |
| sentry-05 | python | 2 | 0 | 2 | 2 | 0+1 | 20 | 1992318/23237 | $2.72 | 112.2 |  |
| sentry-06 | python | 1 | 1 | 0 | 3 | 0+1 | 3 | 181236/3403 | $0.2948 | 57.5 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 135817/2467 | $0.2432 | 47.6 |  |
| sentry-08 | python | 0 | 0 | 0 | 1 | 0+1 | 2 | 108394/2181 | $0.1770 | 56.2 |  |
| sentry-09 | python | 3 | 0 | 3 | 1 | 0+2 | 9 | 507101/11659 | $0.9898 | 71.1 |  |
| sentry-10 | python | 0 | 0 | 0 | 1 | 0+1 | 4 | 324739/4155 | $0.4774 | 50.0 |  |
| calcom-01 | typescript | 5 | 0 | 5 | 1 | 0+1 | 20 | 1360815/22044 | $2.47 | 89.3 |  |
| calcom-02 | typescript | 0 | 0 | 0 | 1 | 0+1 | 3 | 188169/3048 | $0.2794 | 21.7 |  |
| calcom-03 | typescript | 2 | 1 | 1 | 1 | 0+2 | 10 | 341476/13095 | $0.7406 | 51.6 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 5 | 321731/9305 | $0.5527 | 35.6 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 109742/1856 | $0.1857 | 24.8 |  |
| calcom-06 | typescript | 2 | 0 | 2 | 2 | 0+0 | 9 | 374924/13087 | $0.5979 | 57.2 |  |
| calcom-07 | typescript | 1 | 1 | 0 | 1 | 0+0 | 2 | 32726/2499 | $0.1309 | 19.6 |  |
| calcom-08 | typescript | 4 | 3 | 1 | 2 | 0+0 | 10 | 556201/13638 | $0.9933 | 59.4 |  |
| calcom-09 | typescript | 1 | 1 | 0 | 1 | 0+0 | 5 | 165348/7687 | $0.3069 | 42.9 |  |
| calcom-10 | typescript | 1 | 1 | 0 | 3 | 0+1 | 3 | 119955/3725 | $0.2761 | 29.9 |  |
| grafana-01 | go | 0 | 0 | 0 | 3 | 0+2 | 3 | 182049/3284 | $0.2901 | 33.7 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 2 | 104695/3271 | $0.2280 | 39.5 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 199145/3037 | $0.3578 | 29.1 |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | 2 | 90680/2093 | $0.1383 | 34.0 |  |
| grafana-05 | go | 2 | 1 | 1 | 1 | 0+0 | 5 | 333364/5754 | $0.5794 | 39.0 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 4 | 252516/6914 | $0.4456 | 52.5 |  |
| grafana-07 | go | 1 | 0 | 1 | 0 | 0+1 | 2 | 118691/3961 | $0.2200 | 47.8 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 25187/721 | $0.0481 | 25.8 |  |
| grafana-09 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 57408/2117 | $0.1296 | 39.6 |  |
| grafana-10 | go | 0 | 0 | 0 | 2 | 0+0 | 2 | 83367/2430 | $0.1773 | 34.4 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
