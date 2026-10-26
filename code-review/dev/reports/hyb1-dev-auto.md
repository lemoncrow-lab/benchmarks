# Review benchmark: hyb1-dev-auto

- Generated 2026-10-26T05:34:09+00:00 from corpus `golden-comment-prs` (14 pull requests, 0 labelled, 0 labels, digest `6b5fb6bc3f32`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD 10.0, max calls 200; used 103 calls and $10.18; **stopped: the spending ceiling of $10.00 was reached**
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --max-usd 10.0 --max-calls 200 --pr calcom-01 --pr calcom-03 --pr calcom-04 --pr calcom-06 --pr calcom-08 --pr calcom-09 --pr calcom-10 --pr grafana-01 --pr grafana-05 --pr grafana-06 --pr grafana-07 --pr sentry-03 --pr sentry-05 --pr sentry-09 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/dev/reports --name hyb1-dev-auto --record-dir /home/user/bench-data/dev/records-hyb1`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 8/14 | 7.5 | 0 | 378.3k | 11.5k | 0 | $0.5581 | $0.4446 | $1.13 | 19.1 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 5 / 24 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| auto | $0.5581 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: not ready.**
- the run stopped early: the spending ceiling of $10.00 was reached
- auto: 3 incomplete, 0 errored, 3 skipped

**Catch and noise: not ready.**
- the run stopped early: the spending ceiling of $10.00 was reached
- auto: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- the run stopped early: the spending ceiling of $10.00 was reached
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| auto | 8 | $0.5581 | $0.4446 | $1.13 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 353.5k | $0.4994 | 38.5 | 0 / 0 / 2 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran (incomplete) | 20 | 2185.7k | $2.84 | 48.0 | 0 / 0 / 4 | n/a | n/a |
- auto: the model-call budget ran out

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 944.3k | $1.27 | 50.7 | 0 / 0 / 6 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran (incomplete) | 20 | 1551.8k | $2.54 | 18.5 | 0 / 0 / 7 | n/a | n/a |
- auto: the model-call budget ran out

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 335.9k | $0.7280 | 9.5 | 0 / 1 / 2 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 279.3k | $0.1558 | 9.0 | 0 / 1 / 3 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 357.9k | $0.3899 | 7.9 | 0 / 0 / 4 | n/a | n/a |

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 11 | 581.9k | $1.07 | 10.7 | 0 / 3 / 3 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 145.1k | $0.2594 | 15.5 | 0 / 0 / 2 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 120.2k | $0.0982 | 11.3 | 0 / 0 / 2 | n/a | n/a |

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran (incomplete) | 3 | 249.3k | $0.3281 | 14.4 | 0 / 0 / 3 | n/a | n/a |
- auto: errors: BudgetStop: the spending ceiling of $10.00 was reached

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- auto: the spending ceiling of $10.00 was reached

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- auto: the spending ceiling of $10.00 was reached

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- auto: the spending ceiling of $10.00 was reached
