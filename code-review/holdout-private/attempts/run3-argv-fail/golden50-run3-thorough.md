# Review benchmark: golden50-run3-thorough

- Generated 2026-10-26T09:59:23+00:00 from corpus `golden-comment-prs` (50 pull requests, 0 labelled, 0 labels, digest `0cb96eadf6de`).
- Route: claude / sonnet. Depths: thorough.
- Ceiling: max USD 90.0, max calls 700; used 64 calls and $2.60; **stopped: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls**
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth thorough --max-usd 90.0 --max-calls 700 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/holdout-private/reports --name golden50-run3-thorough --record-dir /home/user/bench-data/holdout-private/records-run3 --input-usd-per-mtok 3.0 --output-usd-per-mtok 15.0`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | 8/50 | 7.9 | 0 | 484.9k | 10.5k | 0 | $0.3245 | $0.2832 | $0.6146 | 91.4 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| thorough | 0 / 2 / 19 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

Catch and noise are scored only on labelled pull requests, by the rules in the corpus (`match`). A finding catches a label by `location` (near a line the fix edited) or `symbol` (it names an identifier the fix edited); the per-pull-request tables say which. Noise is a finding that matches no label, so it is an upper bound on false positives wherever the labels are incomplete; some of it repeats a bug already caught (the same problem reported on two targets of one function).

## Follow-up pushes

| Depth | Pushes | Calls with carry-forward | Calls re-reviewing all | USD with carry-forward | USD re-reviewing all | Saved |
| --- | --- | --- | --- | --- | --- | --- |
| thorough | 0 | n/a | n/a | n/a | n/a | n/a |

A push is the fix commit applied on top of the reviewed head. "Re-reviewing all" is what a per-push reviewer spends; "with carry-forward" is what this reviewer spends when it reuses the first review.

## Reference team (a projection)

10 developers, 300 pull requests a month, 1.2 reviews each. a projection from this report's mean cost per review and per push, not a quote and not a price.

| Depth | First review | Push (carry-forward) | Push (re-review all) | Month (carry-forward) | Month (re-review all) |
| --- | --- | --- | --- | --- | --- |
| thorough | $0.3245 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: not ready.**
- the run stopped early: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
- thorough: 1 incomplete, 0 errored, 41 skipped

**Catch and noise: not ready.**
- the run stopped early: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
- thorough: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- the run stopped early: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| thorough | 8 | $0.3245 | $0.2832 | $0.6146 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 225.2k | $0.3415 | 98.9 | 0 / 1 / 2 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 10 | 406.4k | $0.4572 | 121.6 | 0 / 1 / 4 | n/a | n/a |

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 648.0k | $0.5400 | 118.5 | 0 / 0 / 3 | n/a | n/a |

### sentry-04: GitHub OAuth Security Enhancement

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 200.1k | $0.2249 | 79.5 | 0 / 0 / 3 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 20 | 2075.9k | $0.7888 | 135.8 | 0 / 0 / 3 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 147.8k | $0.1163 | 59.2 | 0 / 0 / 2 | n/a | n/a |

### sentry-07: feat(ecosystem): Implement cross-system issue synchronization

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 148.6k | $0.0701 | 58.9 | 0 / 0 / 1 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 110.9k | $0.0574 | 58.6 | 0 / 0 / 1 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran (incomplete) | 1 | n/a | n/a | 45.2 | 0 / 0 / 0 | n/a | n/a |
- thorough: errors: InternalLLMError: claude intelligence execution failed: [Errno 7] Argument list too long: '/opt/node22/bin/claude'; BudgetStop: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-cal

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-05: feat: convert InsightsBookingService to use Prisma.sql raw queries

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-07: Advanced date override handling and timezone compatibility improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-02: AuthZService: improve authz caching

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-03: Plugins: Chore: Renamed instrumentation middleware to metrics middleware

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-04: Advanced Query Processing Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-01: Fixing Re-authentication with passkeys

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-02: Add caching support for IdentityProviderStorageProvider.getForLogin operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-03: Add AuthzClientCryptoProvider for authorization client cryptographic operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-04: Add rolling-updates feature flag and compatibility framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-05: Add Client resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-06: Add Groups resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-07: Add HTML sanitizer for translated message resources

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-08: Implement access token context encoding framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-09: Implement recovery key support for user storage providers

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### keycloak-10: Fix concurrent group access to prevent NullPointerException

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-01: FEATURE: automatically downsize large images

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-02: FEATURE: per-topic unsubscribe option in emails

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-03: Add comprehensive email validation for blocked users

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-04: Enhance embed URL handling and validation system

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-05: Optimize header layout performance with flexbox mixins

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-06: UX: show complete URL path if website domain is same as instance domain

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-07: scale-color $lightness must use $secondary for dark themes

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-08: FIX: proper handling of group memberships

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-09: FEATURE: Localization fallbacks (server-side)

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls

### discourse-10: FEATURE: Can edit category/host relationships for embedding

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | skipped (incomplete) | 0 | 0 | $0.0000 | 0.0 | 0 / 0 / 0 | n/a | n/a |
- thorough: a call to sonnet reported no cost and the local price table has none, so --max-usd cannot be enforced; pass --input-usd-per-mtok and --output-usd-per-mtok, or use --max-calls
