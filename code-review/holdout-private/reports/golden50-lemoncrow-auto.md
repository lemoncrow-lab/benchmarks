# Review benchmark: golden50-lemoncrow-auto

- Generated 2026-10-26T03:37:19+00:00 from corpus `golden-comment-prs` (50 pull requests, 0 labelled, 0 labels, digest `0cb96eadf6de`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD 40.0, max calls 400; used 238 calls and $23.02.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --max-usd 40.0 --max-calls 400 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/reports --name golden50-lemoncrow-auto --record-dir /home/user/bench-data/records/run1`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 50/50 | 4.8 | 0 | 266.5k | 6.1k | 0 | $0.4604 | $0.3101 | $0.7656 | 41.2 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 6 / 49 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| auto | $0.4604 | n/a | n/a | n/a | n/a |

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
| auto | 50 | $0.4604 | $0.3101 | $0.7656 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 69.6k | $0.1204 | 59.2 | 0 / 0 / 1 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 156.6k | $0.3423 | 70.2 | 0 / 0 / 0 | n/a | n/a |

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 280.6k | $0.4419 | 70.6 | 0 / 0 / 0 | n/a | n/a |

### sentry-04: GitHub OAuth Security Enhancement

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 110.8k | $0.2414 | 45.4 | 0 / 0 / 1 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 20 | 2015.6k | $2.72 | 109.5 | 0 / 0 / 2 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 184.6k | $0.2948 | 57.3 | 0 / 0 / 1 | n/a | n/a |

### sentry-07: feat(ecosystem): Implement cross-system issue synchronization

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 138.3k | $0.2432 | 47.4 | 0 / 0 / 1 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 110.6k | $0.1770 | 56.0 | 0 / 0 / 0 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 518.8k | $0.9898 | 70.7 | 0 / 0 / 3 | n/a | n/a |

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 328.9k | $0.4774 | 49.8 | 0 / 0 / 0 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 20 | 1382.9k | $2.47 | 86.9 | 0 / 0 / 5 | n/a | n/a |

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 191.2k | $0.2794 | 21.1 | 0 / 0 / 0 | n/a | n/a |

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 354.6k | $0.7406 | 51.2 | 0 / 1 / 1 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 331.0k | $0.5527 | 34.7 | 0 / 1 / 3 | n/a | n/a |

### calcom-05: feat: convert InsightsBookingService to use Prisma.sql raw queries

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 111.6k | $0.1857 | 24.6 | 0 / 0 / 0 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 388.0k | $0.5979 | 56.6 | 0 / 0 / 2 | n/a | n/a |

### calcom-07: Advanced date override handling and timezone compatibility improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 35.2k | $0.1309 | 19.4 | 0 / 0 / 1 | n/a | n/a |

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 569.8k | $0.9933 | 58.5 | 0 / 2 / 2 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 173.0k | $0.3069 | 42.8 | 0 / 0 / 1 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 123.7k | $0.2761 | 29.3 | 0 / 0 / 1 | n/a | n/a |

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 185.3k | $0.2901 | 33.2 | 0 / 0 / 0 | n/a | n/a |

### grafana-02: AuthZService: improve authz caching

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 108.0k | $0.2280 | 39.2 | 0 / 0 / 1 | n/a | n/a |

### grafana-03: Plugins: Chore: Renamed instrumentation middleware to metrics middleware

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 202.2k | $0.3578 | 28.8 | 0 / 0 / 0 | n/a | n/a |

### grafana-04: Advanced Query Processing Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 92.8k | $0.1383 | 33.7 | 0 / 0 / 0 | n/a | n/a |

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 339.1k | $0.5794 | 37.9 | 0 / 0 / 2 | n/a | n/a |

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 259.4k | $0.4456 | 52.0 | 0 / 0 / 3 | n/a | n/a |

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 122.7k | $0.2200 | 47.5 | 0 / 0 / 1 | n/a | n/a |

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 25.9k | $0.0481 | 25.6 | 0 / 0 / 0 | n/a | n/a |

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 59.5k | $0.1296 | 39.2 | 0 / 0 / 0 | n/a | n/a |

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 85.8k | $0.1773 | 34.0 | 0 / 0 / 0 | n/a | n/a |

### keycloak-01: Fixing Re-authentication with passkeys

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 181.1k | $0.3239 | 23.0 | 0 / 0 / 0 | n/a | n/a |

### keycloak-02: Add caching support for IdentityProviderStorageProvider.getForLogin operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 91.8k | $0.1881 | 25.0 | 0 / 0 / 0 | n/a | n/a |

### keycloak-03: Add AuthzClientCryptoProvider for authorization client cryptographic operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 220.0k | $0.3134 | 42.4 | 0 / 0 / 0 | n/a | n/a |

### keycloak-04: Add rolling-updates feature flag and compatibility framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 117.4k | $0.1607 | 22.6 | 0 / 0 / 0 | n/a | n/a |

### keycloak-05: Add Client resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 300.2k | $0.5611 | 26.7 | 0 / 0 / 0 | n/a | n/a |

### keycloak-06: Add Groups resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 400.2k | $0.5694 | 33.6 | 0 / 0 / 0 | n/a | n/a |

### keycloak-07: Add HTML sanitizer for translated message resources

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 313.9k | $0.7068 | 39.7 | 0 / 0 / 4 | n/a | n/a |

### keycloak-08: Implement access token context encoding framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 707.0k | $1.12 | 69.7 | 0 / 0 / 3 | n/a | n/a |

### keycloak-09: Implement recovery key support for user storage providers

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 217.2k | $0.3365 | 26.9 | 0 / 0 / 0 | n/a | n/a |

### keycloak-10: Fix concurrent group access to prevent NullPointerException

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 58.3k | $0.1227 | 28.7 | 0 / 0 / 1 | n/a | n/a |

### discourse-01: FEATURE: automatically downsize large images

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 34.2k | $0.0656 | 15.9 | 0 / 1 / 0 | n/a | n/a |

### discourse-02: FEATURE: per-topic unsubscribe option in emails

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 426.2k | $0.6286 | 57.4 | 0 / 0 / 1 | n/a | n/a |

### discourse-03: Add comprehensive email validation for blocked users

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 95.4k | $0.1768 | 15.1 | 0 / 0 / 0 | n/a | n/a |

### discourse-04: Enhance embed URL handling and validation system

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 8 | 281.2k | $0.5279 | 46.9 | 0 / 0 / 0 | n/a | n/a |

### discourse-05: Optimize header layout performance with flexbox mixins

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 17.1k | $0.0601 | 10.9 | 0 / 0 / 0 | n/a | n/a |

### discourse-06: UX: show complete URL path if website domain is same as instance domain

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 52.6k | $0.1100 | 16.3 | 0 / 0 / 1 | n/a | n/a |

### discourse-07: scale-color $lightness must use $secondary for dark themes

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 240.7k | $0.5112 | 24.3 | 0 / 0 / 4 | n/a | n/a |

### discourse-08: FIX: proper handling of group memberships

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 8 | 330.0k | $0.5434 | 38.3 | 0 / 0 / 2 | n/a | n/a |

### discourse-09: FEATURE: Localization fallbacks (server-side)

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 35.0k | $0.0724 | 15.5 | 0 / 0 / 0 | n/a | n/a |

### discourse-10: FEATURE: Can edit category/host relationships for embedding

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 451.7k | $0.7306 | 47.5 | 0 / 1 / 1 | n/a | n/a |
