# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `run4-dev-score`, 2026-10-26T07:58:13+00:00. Scored 30 of 30 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report run4-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 25 questions: 0 answered from the cache, 25 asked now (25 calls, $0.4545). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 30 | 27 | 30 | 33 | 47 | 45 | 46 | 47 / 46 |
| language: go | 10 | 7 | 6 | 9 | 54 | 44 | 48 | 54 / 48 |
| language: python | 10 | 8 | 10 | 13 | 44 | 38 | 41 | 44 / 41 |
| language: typescript | 10 | 12 | 14 | 11 | 46 | 52 | 49 | 46 / 49 |
| repository: calcom/cal.com | 10 | 12 | 14 | 11 | 46 | 52 | 49 | 46 / 49 |
| repository: getsentry/sentry | 10 | 8 | 10 | 13 | 44 | 38 | 41 | 44 / 41 |
| repository: grafana/grafana | 10 | 7 | 6 | 9 | 54 | 44 | 48 | 54 / 48 |

Comments posted 60; matched only to an excluded (Low) golden comment 3; golden comments counted 60, excluded 25; pull requests with at least one catch 20 of 30.

Recall by golden severity: Critical 3/4 (75%); High 17/31 (55%); Medium 7/25 (28%).

## Cost of the reviews (30 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 155 | 5.2 | 3.0 | 0 |
| Input tokens | 10248022 | 341600.7 | 199386.0 | 0 |
| Output tokens | 218426 | 7280.9 | 3984.0 | 0 |
| Dollars (the CLI's list-price estimate) | $6.12 | $0.2040 | $0.1095 | 0 |
| Wall seconds | 1816.6 | 60.6 | 58.5 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 22082/1845 | $0.0263 | 56.9 |  |
| sentry-02 | python | 1 | 1 | 0 | 2 | 0+0 | 4 | 186545/5464 | $0.1129 | 69.9 |  |
| sentry-03 | python | 3 | 1 | 2 | 0 | 0+2 | 6 | 329405/8343 | $0.2175 | 83.2 |  |
| sentry-04 | python | 2 | 1 | 1 | 2 | 0+0 | 3 | 134018/5485 | $0.0980 | 65.8 |  |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 2491390/27414 | $0.9199 | 147.4 |  |
| sentry-06 | python | 1 | 1 | 0 | 3 | 0+1 | 3 | 154147/3565 | $0.0990 | 63.1 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 124220/2871 | $0.0650 | 58.3 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 159966/2842 | $0.0702 | 69.3 |  |
| sentry-09 | python | 5 | 0 | 4 | 1 | 1+2 | 10 | 769055/17252 | $0.4483 | 97.8 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 270812/3968 | $0.1374 | 58.6 |  |
| calcom-01 | typescript | 7 | 0 | 7 | 1 | 0+1 | 20 | 1598795/26862 | $0.8039 | 110.3 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 205576/3638 | $0.1061 | 31.1 |  |
| calcom-03 | typescript | 4 | 1 | 3 | 1 | 0+2 | 10 | 398498/14699 | $0.4437 | 65.7 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 327419/8947 | $0.2125 | 61.5 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 110383/2175 | $0.0638 | 27.5 |  |
| calcom-06 | typescript | 1 | 0 | 1 | 2 | 0+0 | 8 | 237313/9231 | $0.2687 | 44.0 |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | 2 | 83073/4000 | $0.0744 | 34.3 |  |
| calcom-08 | typescript | 4 | 3 | 1 | 2 | 0+0 | 11 | 538261/14008 | $0.4467 | 64.8 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 7 | 163445/11009 | $0.3340 | 69.9 |  |
| calcom-10 | typescript | 1 | 1 | 0 | 3 | 0+1 | 2 | 193196/3805 | $0.0994 | 33.2 |  |
| grafana-01 | go | 2 | 1 | 1 | 2 | 0+2 | 3 | 223935/3962 | $0.1188 | 50.6 |  |
| grafana-02 | go | 0 | 0 | 0 | 1 | 0+1 | 2 | 106392/2964 | $0.0610 | 44.4 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 244506/3650 | $0.1027 | 47.1 |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | 2 | 217457/4106 | $0.1568 | 55.5 |  |
| grafana-05 | go | 5 | 2 | 3 | 0 | 0+0 | 6 | 408074/8451 | $0.2405 | 66.4 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 260429/8044 | $0.2020 | 88.3 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 2 | 120154/3898 | $0.0721 | 43.7 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 25874/784 | $0.0194 | 27.4 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58260/1965 | $0.0365 | 36.7 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 85342/3179 | $0.0623 | 44.1 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
