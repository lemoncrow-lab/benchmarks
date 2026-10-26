# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `ver1-dev-score`, 2026-10-26T06:09:54+00:00. Scored 30 of 30 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report ver1-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 28 questions: 24 answered from the cache, 4 asked now (4 calls, $0.0794). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 30 | 29 | 31 | 31 | 48 | 48 | 48 | 48 / 48 |
| language: go | 10 | 8 | 6 | 8 | 57 | 50 | 53 | 57 / 53 |
| language: python | 10 | 9 | 10 | 12 | 47 | 43 | 45 | 47 / 45 |
| language: typescript | 10 | 12 | 15 | 11 | 44 | 52 | 48 | 44 / 48 |
| repository: calcom/cal.com | 10 | 12 | 15 | 11 | 44 | 52 | 48 | 44 / 48 |
| repository: getsentry/sentry | 10 | 9 | 10 | 12 | 47 | 43 | 45 | 47 / 45 |
| repository: grafana/grafana | 10 | 8 | 6 | 8 | 57 | 50 | 53 | 57 / 53 |

Comments posted 64; matched only to an excluded (Low) golden comment 4; golden comments counted 60, excluded 25; pull requests with at least one catch 21 of 30.

Recall by golden severity: Critical 4/4 (100%); High 17/31 (55%); Medium 8/25 (32%).

## Cost of the reviews (30 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 176 | 5.9 | 4.0 | 0 |
| Input tokens | 10398690 | 346623.0 | 199211.5 | 0 |
| Output tokens | 235813 | 7860.4 | 5065.0 | 0 |
| Dollars (the CLI's list-price estimate) | $14.55 | $0.4849 | $0.2341 | 0 |
| Wall seconds | 953.5 | 31.8 | 28.2 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 2 | 77697/2371 | $0.0806 | 46.7 |  |
| sentry-02 | python | 1 | 1 | 0 | 2 | 0+0 | 5 | 199720/6030 | $0.1622 | 48.4 |  |
| sentry-03 | python | 2 | 0 | 2 | 1 | 0+2 | 6 | 367752/8888 | $0.5435 | 52.2 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 4 | 122926/4686 | $0.2875 | 40.4 |  |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 2112621/27330 | $2.78 | 63.0 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 4 | 172959/5185 | $0.1597 | 53.3 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 4 | 167886/2863 | $0.2757 | 41.4 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 3 | 114451/2781 | $0.0751 | 41.6 |  |
| sentry-09 | python | 6 | 0 | 5 | 1 | 1+2 | 10 | 992455/20540 | $1.37 | 65.7 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 5 | 387969/5161 | $0.1999 | 46.3 |  |
| calcom-01 | typescript | 7 | 0 | 6 | 1 | 1+1 | 20 | 1525246/26589 | $2.54 | 23.0 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 4 | 198703/3691 | $0.1149 | 9.7 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 11 | 333886/13393 | $0.7707 | 19.5 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 281942/7895 | $0.2052 | 21.0 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 86102/1963 | $0.1776 | 12.2 |  |
| calcom-06 | typescript | 4 | 1 | 3 | 1 | 0+0 | 10 | 382680/16158 | $0.4482 | 22.0 |  |
| calcom-07 | typescript | 1 | 1 | 0 | 1 | 0+0 | 3 | 65958/2521 | $0.1658 | 15.6 |  |
| calcom-08 | typescript | 4 | 2 | 2 | 3 | 0+0 | 12 | 599127/19023 | $1.13 | 19.0 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 7 | 139253/9488 | $0.2922 | 21.9 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 3 | 117620/5183 | $0.1107 | 13.8 |  |
| grafana-01 | go | 2 | 1 | 1 | 2 | 0+2 | 4 | 265675/4969 | $0.3685 | 25.2 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 3 | 86941/3198 | $0.2389 | 32.4 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 308050/4354 | $0.4057 | 15.4 |  |
| grafana-04 | go | 1 | 0 | 1 | 0 | 0+1 | 3 | 208854/4668 | $0.2294 | 31.5 |  |
| grafana-05 | go | 3 | 2 | 1 | 0 | 0+0 | 6 | 520118/8563 | $0.7398 | 35.4 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 257125/7405 | $0.2260 | 29.4 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 3 | 148554/4633 | $0.2831 | 28.8 |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 32231/1290 | $0.0410 | 25.2 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 65024/2478 | $0.0599 | 25.8 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 3 | 59165/2516 | $0.0681 | 27.6 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
