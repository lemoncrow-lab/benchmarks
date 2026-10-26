# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `frm1-dev-score`, 2026-10-26T06:45:32+00:00. Scored 14 of 14 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report frm1-dev-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 11 questions: 0 answered from the cache, 11 asked now (11 calls, $0.1910). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 14 | 11 | 10 | 22 | 52 | 33 | 41 | 57 / 44 |
| language: go | 4 | 1 | 3 | 6 | 25 | 14 | 18 | 25 / 18 |
| language: python | 5 | 6 | 3 | 9 | 67 | 40 | 50 | 67 / 50 |
| language: typescript | 5 | 4 | 4 | 7 | 50 | 36 | 42 | 62 / 50 |
| repository: calcom/cal.com | 5 | 4 | 4 | 7 | 50 | 36 | 42 | 62 / 50 |
| repository: getsentry/sentry | 5 | 6 | 3 | 9 | 67 | 40 | 50 | 67 / 50 |
| repository: grafana/grafana | 4 | 1 | 3 | 6 | 25 | 14 | 18 | 25 / 18 |

Comments posted 21; matched only to an excluded (Low) golden comment 0; golden comments counted 33, excluded 12; pull requests with at least one catch 10 of 14.

Recall by golden severity: Critical 2/2 (100%); High 6/15 (40%); Medium 3/16 (19%).

## Cost of the reviews (14 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 46 | 3.3 | 3.0 | 0 |
| Input tokens | 2043181 | 145941.5 | 124448.5 | 0 |
| Output tokens | 64980 | 4641.4 | 4118.5 | 0 |
| Dollars (the CLI's list-price estimate) | $3.90 | $0.2782 | $0.2638 | 0 |
| Wall seconds | 691.6 | 49.4 | 49.9 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 2 | 1 | 1 | 2 | 0+1 | 1 | 46427/3384 | $0.1212 | 82.2 |  |
| sentry-02 | python | 3 | 1 | 2 | 2 | 0+0 | 4 | 204541/5515 | $0.3644 | 64.7 |  |
| sentry-04 | python | 1 | 1 | 0 | 2 | 0+0 | 3 | 95505/4288 | $0.2529 | 53.0 |  |
| sentry-06 | python | 2 | 2 | 0 | 2 | 0+1 | 3 | 188947/4277 | $0.3205 | 73.7 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 124703/2752 | $0.2506 | 59.7 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 383882/14531 | $0.6894 | 56.4 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 86321/1905 | $0.1767 | 28.5 |  |
| calcom-07 | typescript | 1 | 1 | 0 | 1 | 0+0 | 2 | 69517/3747 | $0.1596 | 30.0 |  |
| calcom-09 | typescript | 3 | 1 | 2 | 1 | 0+0 | 6 | 124194/7047 | $0.2802 | 50.6 |  |
| calcom-10 | typescript | 1 | 1 | 0 | 3 | 0+1 | 2 | 138926/4925 | $0.2748 | 41.8 |  |
| grafana-01 | go | 3 | 1 | 2 | 2 | 0+2 | 3 | 177544/4618 | $0.3227 | 38.9 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 2 | 74760/3268 | $0.2237 | 35.4 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 301661/3960 | $0.4073 | 49.1 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 26253/763 | $0.0511 | 27.4 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
