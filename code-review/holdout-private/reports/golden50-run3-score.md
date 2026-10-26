# Golden-comment score: LemonCrow (claude/sonnet, thorough)

Report `golden50-run3-score`, 2026-10-26T11:45:22+00:00. Scored 50 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth thorough: the findings the bot would post (benchmark report golden50-run3-thorough.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 45 questions: 0 answered from the cache, 45 asked now (45 calls, $0.8252). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: yes. This report carries a `benchmark_summary`; `make benchmark-publish RUN=<out-dir>/golden50-run3-score.json` merges it.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 50 | 47 | 62 | 50 | 43 | 48 | 46 | 49 / 50 |
| language: go | 10 | 7 | 9 | 9 | 44 | 44 | 44 | 50 / 48 |
| language: java | 10 | 10 | 7 | 8 | 59 | 56 | 57 | 59 / 57 |
| language: python | 10 | 11 | 19 | 10 | 37 | 52 | 43 | 47 / 52 |
| language: ruby | 10 | 6 | 10 | 13 | 38 | 32 | 34 | 38 / 34 |
| language: typescript | 10 | 13 | 17 | 10 | 43 | 57 | 49 | 50 / 55 |
| repository: calcom/cal.com | 10 | 13 | 17 | 10 | 43 | 57 | 49 | 50 / 55 |
| repository: discourse/discourse | 10 | 6 | 10 | 13 | 38 | 32 | 34 | 38 / 34 |
| repository: getsentry/sentry | 10 | 11 | 19 | 10 | 37 | 52 | 43 | 47 / 52 |
| repository: grafana/grafana | 10 | 7 | 9 | 9 | 44 | 44 | 44 | 50 / 48 |
| repository: keycloak/keycloak | 10 | 10 | 7 | 8 | 59 | 56 | 57 | 59 / 57 |

Comments posted 119; matched only to an excluded (Low) golden comment 10; golden comments counted 97, excluded 40; pull requests with at least one catch 32 of 50.

Recall by golden severity: Critical 5/9 (56%); High 22/41 (54%); Medium 20/47 (43%).

## Cost of the reviews (50 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 350 | 7.0 | 7.0 | 0 |
| Input tokens | 18965094 | 379301.9 | 330763.5 | 0 |
| Output tokens | 501871 | 10037.4 | 9523.5 | 0 |
| Dollars (the CLI's list-price estimate) | $28.75 | $0.5751 | $0.5157 | 0 |
| Wall seconds | 3454.9 | 69.1 | 70.4 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 4 | 2 | 2 | 1 | 0+1 | 7 | 269588/10959 | $0.3642 | 96.6 |  |
| sentry-02 | python | 3 | 2 | 1 | 1 | 0+0 | 10 | 380582/13015 | $0.4212 | 95.9 |  |
| sentry-03 | python | 4 | 1 | 2 | 0 | 1+2 | 11 | 636236/15683 | $0.5746 | 123.4 |  |
| sentry-04 | python | 4 | 2 | 2 | 1 | 0+0 | 8 | 267579/11245 | $0.3238 | 84.1 |  |
| sentry-05 | python | 4 | 0 | 3 | 2 | 1+1 | 20 | 1977826/23903 | $0.7820 | 147.9 |  |
| sentry-06 | python | 1 | 1 | 0 | 3 | 0+1 | 3 | 160125/3604 | $0.1005 | 71.1 |  |
| sentry-07 | python | 2 | 1 | 1 | 1 | 0+2 | 3 | 177473/3101 | $0.0884 | 67.3 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 212508/3165 | $0.0816 | 85.3 |  |
| sentry-09 | python | 9 | 0 | 8 | 1 | 1+2 | 15 | 1068097/27652 | $2.00 | 144.1 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 390146/4881 | $0.5040 | 55.0 |  |
| calcom-01 | typescript | 8 | 0 | 7 | 1 | 1+1 | 20 | 1658568/25591 | $2.56 | 120.1 |  |
| calcom-02 | typescript | 2 | 1 | 1 | 0 | 0+1 | 8 | 388460/12979 | $0.6515 | 65.5 |  |
| calcom-03 | typescript | 2 | 0 | 2 | 2 | 0+2 | 10 | 384844/11683 | $0.7546 | 57.2 |  |
| calcom-04 | typescript | 5 | 3 | 2 | 0 | 0+2 | 11 | 513205/16940 | $0.9079 | 73.6 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 136158/2645 | $0.2065 | 43.7 |  |
| calcom-06 | typescript | 2 | 1 | 1 | 1 | 0+0 | 8 | 395433/13869 | $0.5899 | 79.4 |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | 3 | 99465/5654 | $0.2762 | 60.8 |  |
| calcom-08 | typescript | 6 | 3 | 3 | 2 | 0+0 | 11 | 552386/16890 | $1.06 | 95.9 |  |
| calcom-09 | typescript | 2 | 1 | 1 | 1 | 0+0 | 7 | 169281/7068 | $0.3519 | 66.1 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 7 | 326739/9710 | $0.5183 | 83.7 |  |
| grafana-01 | go | 3 | 1 | 1 | 2 | 1+2 | 9 | 385415/12592 | $0.6880 | 76.3 |  |
| grafana-02 | go | 2 | 0 | 2 | 1 | 0+1 | 7 | 338503/13169 | $0.6979 | 88.7 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 7 | 329944/6968 | $0.5279 | 55.1 |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | 5 | 412213/10669 | $0.4919 | 77.6 |  |
| grafana-05 | go | 4 | 2 | 2 | 0 | 0+0 | 6 | 476815/7408 | $0.6758 | 63.2 |  |
| grafana-06 | go | 4 | 2 | 2 | 1 | 0+0 | 5 | 238362/7572 | $0.4561 | 70.8 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 8 | 292521/13012 | $0.6089 | 80.8 |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | 4 | 117135/4665 | $0.2006 | 52.1 |  |
| grafana-09 | go | 2 | 1 | 1 | 1 | 0+0 | 4 | 140284/6438 | $0.2720 | 74.0 |  |
| grafana-10 | go | 0 | 0 | 0 | 2 | 0+0 | 7 | 242383/9741 | $0.5131 | 82.7 |  |
| keycloak-01 | java | 1 | 1 | 0 | 1 | 0+0 | 3 | 156800/2682 | $0.3233 | 28.0 |  |
| keycloak-02 | java | 2 | 1 | 1 | 1 | 0+0 | 7 | 394304/14438 | $0.6598 | 81.6 |  |
| keycloak-03 | java | 3 | 0 | 2 | 1 | 1+1 | 9 | 402011/16020 | $0.8197 | 84.0 |  |
| keycloak-04 | java | 0 | 0 | 0 | 1 | 0+0 | 2 | 127207/2092 | $0.1816 | 36.9 |  |
| keycloak-05 | java | 2 | 1 | 1 | 2 | 0+0 | 11 | 725283/18049 | $1.25 | 107.8 |  |
| keycloak-06 | java | 2 | 2 | 0 | 0 | 0+0 | 11 | 725209/18484 | $1.10 | 92.7 |  |
| keycloak-07 | java | 3 | 2 | 1 | 0 | 0+2 | 7 | 340455/8802 | $0.7633 | 45.3 |  |
| keycloak-08 | java | 2 | 2 | 0 | 0 | 0+2 | 10 | 474891/15467 | $1.06 | 80.4 |  |
| keycloak-09 | java | 2 | 0 | 2 | 1 | 0+1 | 8 | 416127/9337 | $0.7223 | 50.8 |  |
| keycloak-10 | java | 1 | 1 | 0 | 1 | 0+0 | 6 | 169783/7717 | $0.3232 | 44.7 |  |
| discourse-01 | ruby | 1 | 1 | 0 | 1 | 0+1 | 1 | 34070/1076 | $0.0692 | 18.7 |  |
| discourse-02 | ruby | 1 | 1 | 0 | 0 | 0+1 | 7 | 262868/7449 | $0.4648 | 33.2 |  |
| discourse-03 | ruby | 1 | 0 | 1 | 2 | 0+0 | 2 | 84168/2252 | $0.1510 | 19.0 |  |
| discourse-04 | ruby | 3 | 0 | 3 | 6 | 0+0 | 6 | 331583/6543 | $0.4676 | 40.5 |  |
| discourse-05 | ruby | 1 | 0 | 1 | 0 | 0+2 | 1 | 34601/1333 | $0.0738 | 22.6 |  |
| discourse-06 | ruby | 1 | 1 | 0 | 0 | 0+0 | 2 | 69820/2743 | $0.1268 | 27.0 |  |
| discourse-07 | ruby | 4 | 0 | 1 | 0 | 3+3 | 5 | 251730/7835 | $0.5488 | 43.5 |  |
| discourse-08 | ruby | 2 | 1 | 1 | 2 | 0+0 | 8 | 386108/11625 | $0.5703 | 66.9 |  |
| discourse-09 | ruby | 1 | 0 | 1 | 0 | 0+2 | 1 | 34228/1670 | $0.0770 | 23.7 |  |
| discourse-10 | ruby | 4 | 2 | 2 | 2 | 0+0 | 11 | 405574/13786 | $0.7492 | 69.9 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
