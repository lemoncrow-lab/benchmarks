# Review benchmark: run2b-dev-auto

- Generated 2026-10-26T04:46:30+00:00 from corpus `golden-comment-prs` (14 pull requests, 0 labelled, 0 labels, digest `22a292e95c0b`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD 20.0, max calls 200; used 48 calls and $4.38.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --max-usd 20.0 --max-calls 200 --pr sentry-01 --pr sentry-02 --pr sentry-06 --pr sentry-08 --pr sentry-10 --pr calcom-02 --pr calcom-04 --pr calcom-06 --pr calcom-09 --pr calcom-10 --pr grafana-06 --pr grafana-08 --pr grafana-09 --pr grafana-10 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/dev/reports --name run2b-dev-auto --record-dir /home/user/bench-data/dev/records-run2b`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 14/14 | 3.4 | 0 | 178.8k | 5.5k | 0 | $0.3127 | $0.3225 | $0.5112 | 49.4 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 2 / 28 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| auto | $0.3127 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: ready.**

**Catch and noise: not ready.**
- auto: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| auto | 14 | $0.3127 | $0.3225 | $0.5112 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 49.0k | $0.1166 | 66.6 | 0 / 0 / 2 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 336.0k | $0.4326 | 77.9 | 0 / 1 / 3 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 195.8k | $0.3328 | 66.3 | 0 / 0 / 2 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 110.2k | $0.1778 | 56.4 | 0 / 0 / 1 | n/a | n/a |

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 298.8k | $0.4611 | 51.1 | 0 / 0 / 1 | n/a | n/a |

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 241.0k | $0.3199 | 26.4 | 0 / 0 / 1 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 273.0k | $0.5327 | 31.4 | 0 / 1 / 3 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 342.6k | $0.5758 | 54.4 | 0 / 0 / 3 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 138.1k | $0.3010 | 57.3 | 0 / 0 / 3 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 183.3k | $0.3250 | 35.3 | 0 / 0 / 3 | n/a | n/a |

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 222.7k | $0.4175 | 55.5 | 0 / 0 / 4 | n/a | n/a |

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 41.6k | $0.0601 | 32.7 | 0 / 0 / 0 | n/a | n/a |

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 60.3k | $0.1321 | 36.3 | 0 / 0 / 1 | n/a | n/a |

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 88.7k | $0.1924 | 44.5 | 0 / 0 / 1 | n/a | n/a |
