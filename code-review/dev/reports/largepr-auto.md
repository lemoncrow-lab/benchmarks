# Review benchmark: largepr-auto

- Generated 2026-10-26T13:04:58+00:00 from corpus `golden-comment-prs` (3 pull requests, 0 labelled, 0 labels, digest `be3498c7fe97`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD 3.0, max calls n/a; used 22 calls and $3.12; **stopped: the spending ceiling of $3.00 was reached**
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --max-usd 3.0 --pr calcom-01 --pr sentry-09 --pr sentry-05 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/dev/reports --name largepr-auto --record-dir /home/user/bench-data/dev/records-largepr-auto --input-usd-per-mtok 3.0 --output-usd-per-mtok 15.0`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 2/3 | 11.0 | 0 | 1293.8k | 19.3k | 0 | $1.56 | $1.56 | $1.89 | 130.2 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 2 / 9 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

Catch and noise are scored only on labelled pull requests, by the rules in the corpus (`match`). A finding catches a label by `location` (near a line the fix edited) or `symbol` (it names an identifier the fix edited); the per-pull-request tables say which. Noise is a finding that matches no label, so it is an upper bound on false positives wherever the labels are incomplete; some of it repeats a bug already caught (the same problem reported on two targets of one function).

## Follow-up pushes

| Depth | Pushes | Calls with carry-forward | Calls re-reviewing all | USD with carry-forward | USD re-reviewing all | Saved |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 | n/a | n/a | n/a | n/a | n/a |

A push is the fix commit applied on top of the reviewed head. "Re-reviewing all" is what a per-push reviewer spends; "with carry-forward" is what this reviewer spends when it reuses the first review.

## Reference team (a projection)

10 developers, 300 pull requests a month, 1.2 reviews each. a projection from this report's mean cost per review and per push, not a quote and not a price.

| Depth | First review | Push (carry-forward) | Push (re-review all) | Month (carry-forward) | Month (re-review all) |
| --- | --- | --- | --- | --- | --- |
| auto | $1.56 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: not ready.**
- the run stopped early: the spending ceiling of $3.00 was reached
- auto: 2 complete reviews with a known cost; at least 8 are needed
- auto: 0 incomplete, 0 errored, 1 skipped

**Catch and noise: not ready.**
- the run stopped early: the spending ceiling of $3.00 was reached
- auto: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- the run stopped early: the spending ceiling of $3.00 was reached
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| auto | 2 | $1.56 | $1.56 | $1.89 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 13 | 1872.4k | $1.97 | 167.7 | 0 / 1 / 5 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 753.8k | $1.15 | 92.7 | 0 / 1 / 4 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- auto: the spending ceiling of $3.00 was reached
