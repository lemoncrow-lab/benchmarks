# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `golden50-run2-score-v2`, 2026-10-26T11:37:41+00:00. Scored 50 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report golden50-run2-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 43 questions: 43 answered from the cache, 0 asked now (0 calls, n/a). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: yes. This report carries a `benchmark_summary`; `make benchmark-publish RUN=<out-dir>/golden50-run2-score-v2.json` merges it.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 50 | 41 | 48 | 56 | 46 | 42 | 44 | 47 / 45 |
| language: go | 10 | 5 | 10 | 11 | 33 | 31 | 32 | 33 / 32 |
| language: java | 10 | 8 | 5 | 10 | 62 | 44 | 52 | 62 / 52 |
| language: python | 10 | 9 | 12 | 12 | 43 | 43 | 43 | 43 / 43 |
| language: ruby | 10 | 6 | 7 | 13 | 46 | 32 | 38 | 54 / 42 |
| language: typescript | 10 | 13 | 14 | 10 | 48 | 57 | 52 | 48 / 52 |
| repository: calcom/cal.com | 10 | 13 | 14 | 10 | 48 | 57 | 52 | 48 / 52 |
| repository: discourse/discourse | 10 | 6 | 7 | 13 | 46 | 32 | 38 | 54 / 42 |
| repository: getsentry/sentry | 10 | 9 | 12 | 12 | 43 | 43 | 43 | 43 / 43 |
| repository: grafana/grafana | 10 | 5 | 10 | 11 | 33 | 31 | 32 | 33 / 32 |
| repository: keycloak/keycloak | 10 | 8 | 5 | 10 | 62 | 44 | 52 | 62 / 52 |

Comments posted 93; matched only to an excluded (Low) golden comment 4; golden comments counted 97, excluded 40; pull requests with at least one catch 31 of 50.

Recall by golden severity: Critical 4/9 (44%); High 18/41 (44%); Medium 19/47 (40%).

## Cost of the reviews (50 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 243 | 4.9 | 3.0 | 0 |
| Input tokens | 14680953 | 293619.1 | 179725.5 | 0 |
| Output tokens | 335277 | 6705.5 | 4570.5 | 0 |
| Dollars (the CLI's list-price estimate) | $14.03 | $0.2805 | $0.1621 | 0 |
| Wall seconds | 2675.3 | 53.5 | 45.9 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 45677/2245 | $0.0385 | 63.2 |  |
| sentry-02 | python | 2 | 1 | 1 | 2 | 0+0 | 4 | 172331/4739 | $0.1024 | 67.0 |  |
| sentry-03 | python | 1 | 0 | 1 | 1 | 0+2 | 5 | 387601/6970 | $0.1933 | 95.4 |  |
| sentry-04 | python | 2 | 1 | 1 | 2 | 0+0 | 3 | 147182/4402 | $0.0905 | 62.2 |  |
| sentry-05 | python | 7 | 0 | 6 | 2 | 1+1 | 20 | 2171584/28401 | $0.8641 | 134.7 |  |
| sentry-06 | python | 3 | 3 | 0 | 1 | 0+1 | 4 | 177616/4889 | $0.1306 | 66.7 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 159763/3080 | $0.0739 | 65.6 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 110729/2682 | $0.0638 | 72.3 |  |
| sentry-09 | python | 4 | 0 | 3 | 1 | 1+2 | 10 | 839692/16650 | $0.4804 | 113.3 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 463717/5985 | $0.2159 | 78.7 |  |
| calcom-01 | typescript | 5 | 0 | 5 | 1 | 0+1 | 20 | 1363492/23144 | $0.6726 | 108.3 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 235161/3897 | $0.1103 | 31.8 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 412731/14472 | $0.4503 | 93.3 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 317287/9248 | $0.1993 | 43.9 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 133122/2121 | $0.0653 | 35.1 |  |
| calcom-06 | typescript | 2 | 1 | 1 | 1 | 0+0 | 8 | 285543/9882 | $0.2907 | 65.3 |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | 2 | 71259/3845 | $0.0728 | 35.1 |  |
| calcom-08 | typescript | 5 | 2 | 3 | 3 | 0+0 | 11 | 578093/13622 | $0.4625 | 92.0 |  |
| calcom-09 | typescript | 3 | 2 | 1 | 0 | 0+0 | 7 | 179425/11071 | $0.3356 | 67.3 |  |
| calcom-10 | typescript | 2 | 1 | 1 | 3 | 0+1 | 2 | 109674/3661 | $0.0717 | 43.1 |  |
| grafana-01 | go | 2 | 0 | 2 | 3 | 0+2 | 3 | 207190/4313 | $0.1165 | 40.0 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 2 | 139436/2986 | $0.0677 | 48.4 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 393033/4151 | $0.1470 | 57.9 |  |
| grafana-04 | go | 2 | 0 | 2 | 0 | 0+1 | 2 | 216842/5151 | $0.1541 | 57.3 |  |
| grafana-05 | go | 4 | 1 | 3 | 1 | 0+0 | 6 | 578489/8187 | $0.2994 | 67.1 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 193826/6469 | $0.1600 | 70.8 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 2 | 122342/4379 | $0.0850 | 48.0 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 26033/852 | $0.0207 | 29.9 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58236/2104 | $0.0378 | 42.9 |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | 2 | 85015/2762 | $0.0568 | 44.6 |  |
| keycloak-01 | java | 1 | 1 | 0 | 1 | 0+0 | 3 | 180026/3193 | $0.3274 | 21.8 |  |
| keycloak-02 | java | 1 | 1 | 0 | 1 | 0+0 | 2 | 145335/3060 | $0.2167 | 34.4 |  |
| keycloak-03 | java | 2 | 0 | 2 | 1 | 0+1 | 3 | 115202/6373 | $0.2987 | 36.1 |  |
| keycloak-04 | java | 0 | 0 | 0 | 1 | 0+0 | 2 | 119234/1846 | $0.1641 | 29.8 |  |
| keycloak-05 | java | 1 | 0 | 1 | 3 | 0+0 | 6 | 272997/6482 | $0.5740 | 29.3 |  |
| keycloak-06 | java | 1 | 1 | 0 | 1 | 0+0 | 6 | 465605/9487 | $0.6344 | 36.1 |  |
| keycloak-07 | java | 3 | 2 | 1 | 0 | 0+2 | 7 | 358714/9566 | $0.8034 | 47.2 |  |
| keycloak-08 | java | 3 | 2 | 1 | 0 | 0+2 | 10 | 607728/16248 | $1.10 | 78.3 |  |
| keycloak-09 | java | 0 | 0 | 0 | 1 | 0+1 | 3 | 162533/3827 | $0.3438 | 26.8 |  |
| keycloak-10 | java | 1 | 1 | 0 | 1 | 0+0 | 2 | 57206/3002 | $0.1252 | 30.1 |  |
| discourse-01 | ruby | 1 | 1 | 0 | 1 | 0+1 | 1 | 34125/1054 | $0.0692 | 16.3 |  |
| discourse-02 | ruby | 1 | 1 | 0 | 0 | 0+1 | 7 | 233397/7715 | $0.4549 | 36.4 |  |
| discourse-03 | ruby | 1 | 1 | 0 | 1 | 0+0 | 2 | 59781/2263 | $0.1444 | 21.3 |  |
| discourse-04 | ruby | 3 | 0 | 3 | 6 | 0+0 | 6 | 209090/5206 | $0.4280 | 34.7 |  |
| discourse-05 | ruby | 0 | 0 | 0 | 0 | 0+2 | 1 | 53497/1115 | $0.0778 | 19.3 |  |
| discourse-06 | ruby | 1 | 1 | 0 | 0 | 0+0 | 2 | 51896/2360 | $0.1163 | 21.7 |  |
| discourse-07 | ruby | 1 | 0 | 0 | 0 | 1+3 | 5 | 251817/7930 | $0.5503 | 42.0 |  |
| discourse-08 | ruby | 2 | 1 | 1 | 2 | 0+0 | 8 | 411808/9865 | $0.5594 | 54.3 |  |
| discourse-09 | ruby | 0 | 0 | 0 | 0 | 0+2 | 1 | 34238/1472 | $0.0751 | 23.2 |  |
| discourse-10 | ruby | 4 | 1 | 3 | 3 | 0+0 | 11 | 474603/16853 | $0.8316 | 94.9 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
