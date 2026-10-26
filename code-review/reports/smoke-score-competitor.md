# Golden-comment score: competitor bot (its own comments)

Report `smoke-score-competitor`, 2026-10-26T01:51:11+00:00. Scored 2 of 2 pull requests of corpus `golden-comment-prs`.

* Reviewer: another reviewer's saved comments (greptile-comments-normalised); same judge and rule.
* Answer key: https://github.com/ai-code-review-evaluations/golden_comments at `3f2c8ab794b4` (read at run time, not stored here).
* Judge: `claude` `sonnet` (reported by the CLI: claude-sonnet-5-5, claude-sonnet-5-5, claude-haiku-5-5), prompt `golden-judge-1` / `cfe685620f23bc1a`. 2 questions: 0 answered from the cache, 2 asked now (2 calls, $0.0352). 0 judge pairs named an unknown id and were ignored.
* Rule: A reviewer comment is a true positive when the judge says it names the same underlying issue as a golden comment and the one-to-one assignment gives it that comment; a false positive when it matches none (strict: or only one another comment already holds); a golden comment nobody holds is a false negative. Golden comments of severity Low are excluded from all three. Counts are summed over pull requests.

Precision, recall and F are percentages. `lenient` counts a comment that repeats an issue another comment already caught as a true positive instead of a false positive.

| Group | PRs | TP | FP | FN | Precision | Recall | F | Lenient P / F |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **All** | 2 | 1 | 2 | 3 | 33 | 25 | 29 | 33 / 29 |
| language: go | 1 | 1 | 0 | 1 | 100 | 50 | 67 | 100 / 67 |
| language: typescript | 1 | 0 | 2 | 2 | 0 | 0 | 0 | 0 / 0 |
| repository: calcom/cal.com | 1 | 0 | 2 | 2 | 0 | 0 | 0 | 0 / 0 |
| repository: grafana/grafana | 1 | 1 | 0 | 1 | 100 | 50 | 67 | 100 / 67 |

Comments posted 3; matched only to an excluded (Low) golden comment 0; golden comments counted 4, excluded 0; pull requests with at least one catch 1 of 2.

Recall by golden severity: Critical 0/0 (n/a%); High 0/3 (0%); Medium 1/1 (100%).

## Per pull request

| PR | Language | Comments | TP | FP | FN | Excl. | Calls | Tokens in/out | USD | Wall s | Note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| calcom-09 | typescript | 2 | 0 | 2 | 2 | 0+0 | n/a | n/a | n/a | n/a |  |
| grafana-08 | go | 1 | 1 | 0 | 1 | 0+0 | n/a | n/a | n/a | n/a |  |

`Excl.` is comments matched only to a Low golden comment + Low golden comments, both outside the totals.
