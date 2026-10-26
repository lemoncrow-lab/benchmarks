# Review benchmark: run3-dev-auto

- Generated 2026-10-26T06:46:50+00:00 from corpus `golden-comment-prs` (30 pull requests, 0 labelled, 0 labels, digest `ad4bc96aa265`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD 20.0, max calls 200; used 157 calls and $15.87.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --max-usd 20.0 --max-calls 200 --pr sentry-01 --pr sentry-02 --pr sentry-03 --pr sentry-04 --pr sentry-05 --pr sentry-06 --pr sentry-07 --pr sentry-08 --pr sentry-09 --pr sentry-10 --pr calcom-01 --pr calcom-02 --pr calcom-03 --pr calcom-04 --pr calcom-05 --pr calcom-06 --pr calcom-07 --pr calcom-08 --pr calcom-09 --pr calcom-10 --pr grafana-01 --pr grafana-02 --pr grafana-03 --pr grafana-04 --pr grafana-05 --pr grafana-06 --pr grafana-07 --pr grafana-08 --pr grafana-09 --pr grafana-10 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/dev/reports --name run3-dev-auto --record-dir /home/user/bench-data/dev/records-run3`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 30/30 | 5.2 | 0 | 324.1k | 6.9k | 0 | $0.5289 | $0.3083 | $1.07 | 57.3 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 7 / 51 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| auto | $0.5289 | n/a | n/a | n/a | n/a |

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
| auto | 30 | $0.5289 | $0.3083 | $1.07 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 24.1k | $0.0969 | 64.0 | 0 / 0 / 1 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 159.5k | $0.3501 | 64.6 | 0 / 0 / 1 | n/a | n/a |

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 340.2k | $0.4843 | 83.3 | 0 / 0 / 3 | n/a | n/a |

### sentry-04: GitHub OAuth Security Enhancement

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 124.3k | $0.2494 | 50.7 | 0 / 0 / 1 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 20 | 2013.2k | $2.79 | 121.4 | 0 / 0 / 2 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 182.7k | $0.3265 | 64.6 | 0 / 0 / 3 | n/a | n/a |

### sentry-07: feat(ecosystem): Implement cross-system issue synchronization

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 175.8k | $0.2553 | 56.2 | 0 / 0 / 1 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 111.0k | $0.1815 | 61.2 | 0 / 0 / 1 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 779.0k | $1.18 | 94.3 | 0 / 1 / 4 | n/a | n/a |

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 306.4k | $0.4851 | 57.8 | 0 / 0 / 1 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 20 | 1579.6k | $2.53 | 101.7 | 0 / 0 / 7 | n/a | n/a |

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 185.2k | $0.2901 | 30.6 | 0 / 0 / 1 | n/a | n/a |

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 402.0k | $0.7039 | 69.5 | 0 / 0 / 3 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 362.7k | $0.5936 | 53.0 | 0 / 2 / 2 | n/a | n/a |

### calcom-05: feat: convert InsightsBookingService to use Prisma.sql raw queries

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 113.0k | $0.1925 | 31.7 | 0 / 0 / 0 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 318.8k | $0.5725 | 69.5 | 0 / 0 / 1 | n/a | n/a |

### calcom-07: Advanced date override handling and timezone compatibility improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 61.1k | $0.1477 | 24.3 | 0 / 0 / 1 | n/a | n/a |

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 11 | 612.0k | $1.06 | 78.8 | 0 / 3 / 3 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 147.9k | $0.2579 | 47.8 | 0 / 0 / 2 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 141.8k | $0.2662 | 43.2 | 0 / 0 / 2 | n/a | n/a |

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 205.4k | $0.3375 | 43.6 | 0 / 0 / 2 | n/a | n/a |

### grafana-02: AuthZService: improve authz caching

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 132.7k | $0.2326 | 37.2 | 0 / 0 / 0 | n/a | n/a |

### grafana-03: Plugins: Chore: Renamed instrumentation middleware to metrics middleware

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 228.1k | $0.3782 | 41.6 | 0 / 0 / 0 | n/a | n/a |

### grafana-04: Advanced Query Processing Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 236.8k | $0.2230 | 52.8 | 0 / 0 / 0 | n/a | n/a |

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 469.6k | $0.6695 | 53.3 | 0 / 0 / 3 | n/a | n/a |

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 242.1k | $0.4314 | 60.3 | 0 / 1 / 2 | n/a | n/a |

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 100.8k | $0.2145 | 43.3 | 0 / 0 / 1 | n/a | n/a |

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 27.7k | $0.0573 | 34.2 | 0 / 0 / 1 | n/a | n/a |

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 60.1k | $0.1299 | 40.8 | 0 / 0 / 1 | n/a | n/a |

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 87.2k | $0.1804 | 43.7 | 0 / 0 / 1 | n/a | n/a |
