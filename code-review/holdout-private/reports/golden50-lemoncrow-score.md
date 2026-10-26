# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `golden50-lemoncrow-score`, 2026-10-26T04:15:04+00:00. Scored 50 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report golden50-lemoncrow-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 27 questions: 0 answered from the cache, 27 asked now (27 calls, $0.4634). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 50 | 26 | 26 | 71 | 50 | 27 | 35 | 56 / 38 |
| language: go | 10 | 3 | 4 | 13 | 43 | 19 | 26 | 43 / 26 |
| language: java | 10 | 5 | 3 | 13 | 62 | 28 | 38 | 75 / 44 |
| language: python | 10 | 4 | 5 | 17 | 44 | 19 | 27 | 44 / 27 |
| language: ruby | 10 | 4 | 4 | 15 | 50 | 21 | 30 | 62 / 36 |
| language: typescript | 10 | 10 | 10 | 13 | 50 | 43 | 47 | 55 / 50 |
| repository: calcom/cal.com | 10 | 10 | 10 | 13 | 50 | 43 | 47 | 55 / 50 |
| repository: discourse/discourse | 10 | 4 | 4 | 15 | 50 | 21 | 30 | 62 / 36 |
| repository: getsentry/sentry | 10 | 4 | 5 | 17 | 44 | 19 | 27 | 44 / 27 |
| repository: grafana/grafana | 10 | 3 | 4 | 13 | 43 | 19 | 26 | 43 / 26 |
| repository: keycloak/keycloak | 10 | 5 | 3 | 13 | 62 | 28 | 38 | 75 / 44 |

Comments posted 55; matched only to an excluded (Low) golden comment 3; golden comments counted 97, excluded 40; pull requests with at least one catch 19 of 50.

Recall by golden severity: Critical 1/9 (11%); High 14/41 (34%); Medium 11/47 (23%).

## Cost of the reviews (50 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 238 | 4.8 | 3.0 | 0 |
| Input tokens | 13324485 | 266489.7 | 181642.5 | 0 |
| Output tokens | 302809 | 6056.2 | 3564.0 | 0 |
| Dollars (the CLI's list-price estimate) | $23.02 | $0.4604 | $0.3101 | 0 |
| Wall seconds | 2083.9 | 41.7 | 39.3 | 0 |

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
| keycloak-01 | java | 0 | 0 | 0 | 2 | 0+0 | 3 | 177956/3183 | $0.3239 | 23.5 |  |
| keycloak-02 | java | 0 | 0 | 0 | 2 | 0+0 | 2 | 89262/2586 | $0.1881 | 25.3 |  |
| keycloak-03 | java | 0 | 0 | 0 | 1 | 0+1 | 3 | 214848/5133 | $0.3134 | 42.7 |  |
| keycloak-04 | java | 0 | 0 | 0 | 1 | 0+0 | 2 | 115315/2037 | $0.1607 | 22.9 |  |
| keycloak-05 | java | 0 | 0 | 0 | 3 | 0+0 | 6 | 293213/6973 | $0.5611 | 27.0 |  |
| keycloak-06 | java | 0 | 0 | 0 | 2 | 0+0 | 6 | 393453/6775 | $0.5694 | 34.3 |  |
| keycloak-07 | java | 4 | 2 | 2 | 0 | 0+2 | 6 | 305201/8670 | $0.7068 | 40.3 |  |
| keycloak-08 | java | 3 | 2 | 1 | 0 | 0+2 | 9 | 690890/16133 | $1.12 | 70.3 |  |
| keycloak-09 | java | 0 | 0 | 0 | 1 | 0+1 | 3 | 213977/3249 | $0.3365 | 27.2 |  |
| keycloak-10 | java | 1 | 1 | 0 | 1 | 0+0 | 2 | 55566/2763 | $0.1227 | 29.0 |  |
| discourse-01 | ruby | 1 | 1 | 0 | 1 | 0+1 | 1 | 33267/906 | $0.0656 | 16.1 |  |
| discourse-02 | ruby | 1 | 1 | 0 | 0 | 0+1 | 9 | 412798/13356 | $0.6286 | 58.0 |  |
| discourse-03 | ruby | 0 | 0 | 0 | 2 | 0+0 | 3 | 93439/1992 | $0.1768 | 15.4 |  |
| discourse-04 | ruby | 0 | 0 | 0 | 6 | 0+0 | 8 | 272576/8601 | $0.5279 | 47.3 |  |
| discourse-05 | ruby | 0 | 0 | 0 | 0 | 0+2 | 1 | 16423/689 | $0.0601 | 11.1 |  |
| discourse-06 | ruby | 1 | 1 | 0 | 0 | 0+0 | 2 | 50564/2005 | $0.1100 | 16.4 |  |
| discourse-07 | ruby | 4 | 0 | 1 | 0 | 3+3 | 4 | 233747/6950 | $0.5112 | 24.6 |  |
| discourse-08 | ruby | 2 | 1 | 1 | 2 | 0+0 | 8 | 319779/10207 | $0.5434 | 38.9 |  |
| discourse-09 | ruby | 0 | 0 | 0 | 0 | 0+2 | 1 | 33755/1267 | $0.0724 | 15.7 |  |
| discourse-10 | ruby | 2 | 0 | 2 | 4 | 0+0 | 10 | 439407/12316 | $0.7306 | 48.4 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
