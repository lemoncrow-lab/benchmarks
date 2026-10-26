# Golden-comment score: LemonCrow (claude/sonnet, thorough)

Report `golden50-run3-score`, 2026-10-26T10:13:40+00:00. Scored 9 of 50 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth thorough: the findings the bot would post (benchmark report golden50-run3-thorough.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 8 questions: 0 answered from the cache, 8 asked now (8 calls, $0.1589). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 9 | 13 | 6 | 7 | 68 | 65 | 67 | 68 / 67 |
| language: python | 9 | 13 | 6 | 7 | 68 | 65 | 67 | 68 / 67 |
| repository: getsentry/sentry | 9 | 13 | 6 | 7 | 68 | 65 | 67 | 68 / 67 |

Comments posted 21; matched only to an excluded (Low) golden comment 2; golden comments counted 20, excluded 10; pull requests with at least one catch 7 of 9.

Recall by golden severity: Critical 1/1 (100%); High 8/9 (89%); Medium 4/10 (40%).

Not scored (in no total):

* `sentry-10`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-01`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-02`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-03`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-04`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-05`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-06`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-07`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-08`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-09`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `calcom-10`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-01`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-02`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-03`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-04`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-05`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-06`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-07`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-08`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-09`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `grafana-10`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-01`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-02`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-03`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-04`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-05`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-06`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-07`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-08`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-09`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `keycloak-10`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-01`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-02`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-03`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-04`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-05`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-06`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-07`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-08`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-09`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
* `discourse-10`: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

Scored although the review was partial: `sentry-09`.

## Cost of the reviews (9 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 64 | 7.1 | 7 | 0 |
| Input tokens | 3878971 | 484871.4 | 203374.0 | 1 |
| Output tokens | 83970 | 10496.2 | 9290.5 | 1 |
| Dollars (the CLI's list-price estimate) | $2.60 | $0.3245 | $0.2832 | 1 |
| Wall seconds | 783.8 | 87.1 | 79.7 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 3 | 3 | 0 | 0 | 0+1 | 7 | 214692/10554 | $0.3415 | 101.4 |  |
| sentry-02 | python | 5 | 3 | 2 | 0 | 0+0 | 10 | 390387/15985 | $0.4572 | 121.9 |  |
| sentry-03 | python | 3 | 1 | 1 | 0 | 1+2 | 11 | 633903/14121 | $0.5400 | 119.2 |  |
| sentry-04 | python | 3 | 2 | 1 | 1 | 0+0 | 7 | 192056/8027 | $0.2249 | 79.7 |  |
| sentry-05 | python | 3 | 0 | 2 | 2 | 1+1 | 20 | 2050634/25289 | $0.7888 | 138.6 |  |
| sentry-06 | python | 2 | 2 | 0 | 2 | 0+1 | 3 | 143280/4498 | $0.1163 | 59.4 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 145642/2978 | $0.0701 | 59.1 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 108377/2518 | $0.0574 | 58.8 |  |
| sentry-09 | python | 0 | 0 | 0 | 1 | 0+2 | 1 | n/a/n/a | n/a | 45.6 |  |
| sentry-10 | python | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-01 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-02 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-03 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-04 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-05 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-06 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-07 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-08 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-09 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| calcom-10 | typescript | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-01 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-02 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-03 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-04 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-05 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-06 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-07 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-08 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-09 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| grafana-10 | go | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-01 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-02 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-03 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-04 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-05 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-06 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-07 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-08 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-09 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| keycloak-10 | java | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-01 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-02 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-03 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-04 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-05 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-06 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-07 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-08 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-09 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |
| discourse-10 | ruby | | | | | | | | | | not scored: the review did not run: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
