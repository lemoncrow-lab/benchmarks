# Golden-comment score: LemonCrow (claude/sonnet, auto)

Report `dev27-auto-score`, 2026-10-26T14:01:17+00:00. Scored 27 of 27 pull requests of corpus `golden-comment-prs`.

* Reviewer: LemonCrow's AI review at depth auto: the findings the bot would post (benchmark report dev27-auto.json).
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-haiku-5-5, claude-sonnet-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 22 questions: 0 answered from the cache, 22 asked now (22 calls, $0.3796). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.
* Ready to publish: no. No `benchmark_summary` was written because the run was limited to 27 pull request(s) with --pr; the benchmark ran on a checkout with uncommitted changes to tracked files, so its commit is not the code that ran.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 27 | 25 | 21 | 31 | 54 | 45 | 49 | 54 / 49 |
| language: go | 10 | 4 | 6 | 12 | 40 | 25 | 31 | 40 / 31 |
| language: python | 8 | 7 | 4 | 11 | 64 | 39 | 48 | 64 / 48 |
| language: typescript | 9 | 14 | 11 | 8 | 56 | 64 | 60 | 56 / 60 |
| repository: calcom/cal.com | 9 | 14 | 11 | 8 | 56 | 64 | 60 | 56 / 60 |
| repository: getsentry/sentry | 8 | 7 | 4 | 11 | 64 | 39 | 48 | 64 / 48 |
| repository: grafana/grafana | 10 | 4 | 6 | 12 | 40 | 25 | 31 | 40 / 31 |

Comments posted 47; matched only to an excluded (Low) golden comment 1; golden comments counted 56, excluded 21; pull requests with at least one catch 17 of 27.

Recall by golden severity: Critical 4/4 (100%); High 14/30 (47%); Medium 7/22 (32%).

## Cost of the reviews (27 pull requests)

| | Total | Mean per PR | Median | PRs unknown |
| --- | --- | --- | --- | --- |
| Model calls | 104 | 3.9 | 3 | 0 |
| Input tokens | 5492385 | 203421.7 | 146283 | 0 |
| Output tokens | 144484 | 5351.3 | 4227 | 0 |
| Dollars (the CLI's list-price estimate) | $9.50 | $0.3518 | $0.2971 | 0 |
| Wall seconds | 1539.7 | 57.0 | 58.3 | 0 |

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| sentry-01 | python | 1 | 1 | 0 | 2 | 0+1 | 1 | 45597/2199 | $0.1063 | 67.4 |  |
| sentry-02 | python | 2 | 1 | 1 | 2 | 0+0 | 4 | 159441/4898 | $0.3493 | 62.9 |  |
| sentry-03 | python | 2 | 0 | 2 | 1 | 0+2 | 5 | 381294/7517 | $0.4898 | 75.5 |  |
| sentry-04 | python | 1 | 0 | 1 | 3 | 0+0 | 3 | 146283/4894 | $0.2734 | 61.1 |  |
| sentry-06 | python | 2 | 2 | 0 | 2 | 0+1 | 3 | 135763/3898 | $0.2971 | 70.9 |  |
| sentry-07 | python | 1 | 1 | 0 | 1 | 0+2 | 3 | 145640/2932 | $0.2556 | 63.8 |  |
| sentry-08 | python | 1 | 1 | 0 | 0 | 0+1 | 2 | 135079/2815 | $0.1906 | 64.6 |  |
| sentry-10 | python | 1 | 1 | 0 | 0 | 0+1 | 4 | 359604/4416 | $0.4892 | 58.3 |  |
| calcom-02 | typescript | 1 | 1 | 0 | 0 | 0+1 | 3 | 204758/3915 | $0.3020 | 28.7 |  |
| calcom-03 | typescript | 3 | 1 | 2 | 1 | 0+2 | 10 | 397785/13105 | $0.7581 | 85.8 |  |
| calcom-04 | typescript | 4 | 3 | 1 | 0 | 0+2 | 6 | 314049/9153 | $0.5700 | 49.4 |  |
| calcom-05 | typescript | 0 | 0 | 0 | 1 | 0+1 | 2 | 108209/2020 | $0.1808 | 28.7 |  |
| calcom-06 | typescript | 4 | 1 | 3 | 1 | 0+0 | 9 | 318597/13383 | $0.5934 | 73.7 |  |
| calcom-07 | typescript | 2 | 2 | 0 | 0 | 0+0 | 2 | 71025/3787 | $0.1667 | 35.2 |  |
| calcom-08 | typescript | 6 | 3 | 3 | 2 | 0+0 | 11 | 544665/15314 | $1.05 | 92.0 |  |
| calcom-09 | typescript | 3 | 1 | 2 | 1 | 0+0 | 6 | 124904/7660 | $0.3159 | 79.5 |  |
| calcom-10 | typescript | 2 | 2 | 0 | 2 | 0+1 | 2 | 109321/4227 | $0.2487 | 45.8 |  |
| grafana-01 | go | 1 | 0 | 1 | 3 | 0+2 | 3 | 231114/4808 | $0.3334 | 57.9 |  |
| grafana-02 | go | 1 | 0 | 1 | 1 | 0+1 | 2 | 130456/2981 | $0.2381 | 45.2 |  |
| grafana-03 | go | 0 | 0 | 0 | 1 | 0+1 | 4 | 272920/3715 | $0.3987 | 53.0 |  |
| grafana-04 | go | 0 | 0 | 0 | 0 | 0+1 | 2 | 202941/4433 | $0.2098 | 57.2 |  |
| grafana-05 | go | 3 | 1 | 2 | 1 | 0+0 | 6 | 409909/6296 | $0.6365 | 61.1 |  |
| grafana-06 | go | 3 | 2 | 1 | 1 | 0+0 | 5 | 252810/7090 | $0.4649 | 69.8 |  |
| grafana-07 | go | 2 | 0 | 1 | 0 | 1+1 | 2 | 121225/3831 | $0.2231 | 46.4 |  |
| grafana-08 | go | 0 | 0 | 0 | 2 | 0+0 | 1 | 25887/679 | $0.0491 | 28.7 |  |
| grafana-09 | go | 1 | 1 | 0 | 1 | 0+0 | 1 | 58212/2036 | $0.1307 | 37.8 |  |
| grafana-10 | go | 0 | 0 | 0 | 2 | 0+0 | 2 | 84897/2482 | $0.1813 | 39.4 |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
