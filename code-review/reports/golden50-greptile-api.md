# Golden-comment score: Greptile (its own comments)

Report `golden50-greptile-api`, 2026-10-26T18:24:52+00:00. Scored 50 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: another reviewer's saved comments (greptile-comments-api-normalised); same judge and rule.
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 47 questions: 47 answered from the cache, 0 asked now (0 calls, n/a). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: yes. This report carries a `benchmark_summary`; `make benchmark-publish RUN=<out-dir>/golden50-greptile-api.json RESCORED=greptile` merges it.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 50 | 49 | 196 | 48 | 20 | 51 | 29 | 24 / 33 |
| language: go | 10 | 9 | 23 | 7 | 28 | 56 | 38 | 38 / 47 |
| language: java | 10 | 10 | 34 | 8 | 23 | 56 | 32 | 27 / 38 |
| language: python | 10 | 7 | 19 | 14 | 27 | 33 | 30 | 27 / 30 |
| language: ruby | 10 | 13 | 69 | 6 | 16 | 68 | 26 | 17 / 27 |
| language: typescript | 10 | 10 | 51 | 13 | 16 | 43 | 24 | 21 / 30 |
| repository: calcom/cal.com | 10 | 10 | 51 | 13 | 16 | 43 | 24 | 21 / 30 |
| repository: discourse/discourse | 10 | 13 | 69 | 6 | 16 | 68 | 26 | 17 / 27 |
| repository: getsentry/sentry | 10 | 7 | 19 | 14 | 27 | 33 | 30 | 27 / 30 |
| repository: grafana/grafana | 10 | 9 | 23 | 7 | 28 | 56 | 38 | 38 / 47 |
| repository: keycloak/keycloak | 10 | 10 | 34 | 8 | 23 | 56 | 32 | 27 / 38 |

Comments posted 267; matched only to an excluded (Low) golden comment 22; golden comments counted 97, excluded 40; pull requests with at least one catch 33 of 50.

Recall by golden severity: Critical 5/9 (56%); High 19/41 (46%); Medium 25/47 (53%).

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 3 | 0 | 2 | 3 | 1+1 | n/a | n/a | n/a | n/a |  |
| sentry-02 | python | 3 | 0 | 3 | 3 | 0+0 | n/a | n/a | n/a | n/a |  |
| sentry-03 | python | 6 | 0 | 5 | 1 | 1+2 | n/a | n/a | n/a | n/a |  |
| sentry-04 | python | 0 | 0 | 0 | 3 | 0+0 | n/a | n/a | n/a | n/a |  |
| sentry-05 | python | 5 | 1 | 4 | 1 | 0+1 | n/a | n/a | n/a | n/a |  |
| sentry-06 | python | 3 | 2 | 1 | 2 | 0+1 | n/a | n/a | n/a | n/a |  |
| sentry-07 | python | 3 | 1 | 0 | 1 | 2+2 | n/a | n/a | n/a | n/a |  |
| sentry-08 | python | 2 | 1 | 1 | 0 | 0+1 | n/a | n/a | n/a | n/a |  |
| sentry-09 | python | 2 | 1 | 1 | 0 | 0+2 | n/a | n/a | n/a | n/a |  |
| sentry-10 | python | 3 | 1 | 2 | 0 | 0+1 | n/a | n/a | n/a | n/a |  |
| calcom-01 | typescript | 19 | 1 | 17 | 0 | 1+1 | n/a | n/a | n/a | n/a |  |
| calcom-02 | typescript | 1 | 0 | 0 | 1 | 1+1 | n/a | n/a | n/a | n/a |  |
| calcom-03 | typescript | 9 | 0 | 7 | 2 | 2+2 | n/a | n/a | n/a | n/a |  |
| calcom-04 | typescript | 6 | 2 | 3 | 1 | 1+2 | n/a | n/a | n/a | n/a |  |
| calcom-05 | typescript | 1 | 0 | 1 | 1 | 0+1 | n/a | n/a | n/a | n/a |  |
| calcom-06 | typescript | 7 | 2 | 5 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| calcom-08 | typescript | 11 | 2 | 9 | 3 | 0+0 | n/a | n/a | n/a | n/a |  |
| calcom-09 | typescript | 2 | 0 | 2 | 2 | 0+0 | n/a | n/a | n/a | n/a |  |
| calcom-10 | typescript | 9 | 1 | 7 | 3 | 1+1 | n/a | n/a | n/a | n/a |  |
| grafana-01 | go | 6 | 1 | 3 | 2 | 2+2 | n/a | n/a | n/a | n/a |  |
| grafana-02 | go | 0 | 0 | 0 | 1 | 0+1 | n/a | n/a | n/a | n/a |  |
| grafana-03 | go | 5 | 0 | 5 | 1 | 0+1 | n/a | n/a | n/a | n/a |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | n/a | n/a | n/a | n/a |  |
| grafana-05 | go | 5 | 1 | 4 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| grafana-06 | go | 8 | 3 | 5 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| grafana-07 | go | 3 | 0 | 2 | 0 | 1+1 | n/a | n/a | n/a | n/a |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| grafana-09 | go | 6 | 2 | 4 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| grafana-10 | go | 1 | 1 | 0 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-01 | java | 3 | 1 | 2 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-02 | java | 3 | 2 | 1 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-03 | java | 5 | 1 | 3 | 0 | 1+1 | n/a | n/a | n/a | n/a |  |
| keycloak-04 | java | 1 | 0 | 1 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-05 | java | 6 | 0 | 6 | 3 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-06 | java | 5 | 1 | 4 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| keycloak-07 | java | 8 | 1 | 6 | 1 | 1+2 | n/a | n/a | n/a | n/a |  |
| keycloak-08 | java | 7 | 2 | 3 | 0 | 2+2 | n/a | n/a | n/a | n/a |  |
| keycloak-09 | java | 7 | 1 | 6 | 0 | 0+1 | n/a | n/a | n/a | n/a |  |
| keycloak-10 | java | 3 | 1 | 2 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| discourse-01 | ruby | 4 | 1 | 2 | 1 | 1+1 | n/a | n/a | n/a | n/a |  |
| discourse-02 | ruby | 5 | 1 | 2 | 0 | 2+1 | n/a | n/a | n/a | n/a |  |
| discourse-03 | ruby | 13 | 2 | 11 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| discourse-04 | ruby | 28 | 5 | 23 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| discourse-05 | ruby | 3 | 0 | 3 | 0 | 0+2 | n/a | n/a | n/a | n/a |  |
| discourse-06 | ruby | 2 | 1 | 1 | 0 | 0+0 | n/a | n/a | n/a | n/a |  |
| discourse-07 | ruby | 2 | 0 | 1 | 0 | 1+3 | n/a | n/a | n/a | n/a |  |
| discourse-08 | ruby | 14 | 2 | 12 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |
| discourse-09 | ruby | 1 | 0 | 0 | 0 | 1+2 | n/a | n/a | n/a | n/a |  |
| discourse-10 | ruby | 15 | 1 | 14 | 3 | 0+0 | n/a | n/a | n/a | n/a |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
