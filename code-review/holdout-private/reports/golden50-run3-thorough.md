# Review benchmark: golden50-run3-thorough

- Generated 2026-10-26T10:39:04+00:00 from corpus `golden-comment-prs` (50 pull requests, 0 labelled, 0 labels, digest `0cb96eadf6de`).
- Route: claude / sonnet. Depths: thorough.
- Ceiling: max USD 90.0, max calls 700; used 350 calls and $28.75.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth thorough --max-usd 90.0 --max-calls 700 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/holdout-private/reports --name golden50-run3-thorough --record-dir /home/user/bench-data/holdout-private/records-run3 --input-usd-per-mtok 3.0 --output-usd-per-mtok 15.0`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | 50/50 | 7.0 | 0 | 379.3k | 10.0k | 0 | $0.5751 | $0.5157 | $1.06 | 66.7 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| thorough | 0 / 10 / 109 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| thorough | $0.5751 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: ready.**

**Catch and noise: not ready.**
- thorough: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| thorough | 50 | $0.5751 | $0.5157 | $1.06 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 280.5k | $0.3642 | 96.3 | 0 / 0 / 4 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 10 | 393.6k | $0.4212 | 95.5 | 0 / 0 / 3 | n/a | n/a |

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 651.9k | $0.5746 | 122.5 | 0 / 0 / 4 | n/a | n/a |

### sentry-04: GitHub OAuth Security Enhancement

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 278.8k | $0.3238 | 83.8 | 0 / 0 / 4 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 20 | 2001.7k | $0.7820 | 145.2 | 0 / 0 / 4 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 163.7k | $0.1005 | 70.8 | 0 / 0 / 1 | n/a | n/a |

### sentry-07: feat(ecosystem): Implement cross-system issue synchronization

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 180.6k | $0.0884 | 67.0 | 0 / 0 / 2 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 215.7k | $0.0816 | 85.1 | 0 / 0 / 1 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 15 | 1095.7k | $2.00 | 143.8 | 0 / 1 / 8 | n/a | n/a |

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 4 | 395.0k | $0.5040 | 52.7 | 0 / 1 / 0 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 20 | 1684.2k | $2.56 | 111.0 | 0 / 0 / 8 | n/a | n/a |

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 401.4k | $0.6515 | 62.7 | 0 / 0 / 2 | n/a | n/a |

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 10 | 396.5k | $0.7546 | 54.2 | 0 / 0 / 2 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 530.1k | $0.9079 | 69.6 | 0 / 1 / 4 | n/a | n/a |

### calcom-05: feat: convert InsightsBookingService to use Prisma.sql raw queries

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 138.8k | $0.2065 | 38.6 | 0 / 0 / 0 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 409.3k | $0.5899 | 75.6 | 0 / 0 / 2 | n/a | n/a |

### calcom-07: Advanced date override handling and timezone compatibility improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 105.1k | $0.2762 | 58.1 | 0 / 0 / 2 | n/a | n/a |

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 569.3k | $1.06 | 91.3 | 0 / 3 / 3 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 176.3k | $0.3519 | 61.7 | 0 / 0 / 2 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 336.4k | $0.5183 | 79.1 | 0 / 0 / 2 | n/a | n/a |

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 9 | 398.0k | $0.6880 | 72.9 | 0 / 0 / 3 | n/a | n/a |

### grafana-02: AuthZService: improve authz caching

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 351.7k | $0.6979 | 85.4 | 0 / 0 / 2 | n/a | n/a |

### grafana-03: Plugins: Chore: Renamed instrumentation middleware to metrics middleware

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 336.9k | $0.5279 | 52.4 | 0 / 0 / 0 | n/a | n/a |

### grafana-04: Advanced Query Processing Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 5 | 422.9k | $0.4919 | 74.7 | 0 / 0 / 0 | n/a | n/a |

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 6 | 484.2k | $0.6758 | 58.6 | 0 / 0 / 4 | n/a | n/a |

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 5 | 245.9k | $0.4561 | 67.3 | 0 / 0 / 4 | n/a | n/a |

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 305.5k | $0.6089 | 78.0 | 0 / 0 / 2 | n/a | n/a |

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 4 | 121.8k | $0.2006 | 50.1 | 0 / 0 / 1 | n/a | n/a |

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 4 | 146.7k | $0.2720 | 70.9 | 0 / 0 / 2 | n/a | n/a |

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 252.1k | $0.5131 | 78.9 | 0 / 0 / 0 | n/a | n/a |

### keycloak-01: Fixing Re-authentication with passkeys

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 3 | 159.5k | $0.3233 | 26.0 | 0 / 1 / 0 | n/a | n/a |

### keycloak-02: Add caching support for IdentityProviderStorageProvider.getForLogin operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 408.7k | $0.6598 | 79.5 | 0 / 0 / 2 | n/a | n/a |

### keycloak-03: Add AuthzClientCryptoProvider for authorization client cryptographic operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 9 | 418.0k | $0.8197 | 80.9 | 0 / 0 / 3 | n/a | n/a |

### keycloak-04: Add rolling-updates feature flag and compatibility framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 129.3k | $0.1816 | 35.3 | 0 / 0 / 0 | n/a | n/a |

### keycloak-05: Add Client resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 743.3k | $1.25 | 106.2 | 0 / 0 / 2 | n/a | n/a |

### keycloak-06: Add Groups resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 743.7k | $1.10 | 90.3 | 0 / 1 / 1 | n/a | n/a |

### keycloak-07: Add HTML sanitizer for translated message resources

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 349.3k | $0.7633 | 42.9 | 0 / 0 / 3 | n/a | n/a |

### keycloak-08: Implement access token context encoding framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 10 | 490.4k | $1.06 | 78.5 | 0 / 0 / 2 | n/a | n/a |

### keycloak-09: Implement recovery key support for user storage providers

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 425.5k | $0.7223 | 49.3 | 0 / 0 / 2 | n/a | n/a |

### keycloak-10: Fix concurrent group access to prevent NullPointerException

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 6 | 177.5k | $0.3232 | 43.1 | 0 / 0 / 1 | n/a | n/a |

### discourse-01: FEATURE: automatically downsize large images

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 1 | 35.1k | $0.0692 | 16.5 | 0 / 1 / 0 | n/a | n/a |

### discourse-02: FEATURE: per-topic unsubscribe option in emails

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 7 | 270.3k | $0.4648 | 31.8 | 0 / 0 / 1 | n/a | n/a |

### discourse-03: Add comprehensive email validation for blocked users

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 86.4k | $0.1510 | 18.4 | 0 / 0 / 1 | n/a | n/a |

### discourse-04: Enhance embed URL handling and validation system

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 6 | 338.1k | $0.4676 | 39.6 | 0 / 0 / 3 | n/a | n/a |

### discourse-05: Optimize header layout performance with flexbox mixins

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 1 | 35.9k | $0.0738 | 21.7 | 0 / 0 / 1 | n/a | n/a |

### discourse-06: UX: show complete URL path if website domain is same as instance domain

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 2 | 72.6k | $0.1268 | 25.2 | 0 / 0 / 1 | n/a | n/a |

### discourse-07: scale-color $lightness must use $secondary for dark themes

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 5 | 259.6k | $0.5488 | 42.3 | 0 / 0 / 4 | n/a | n/a |

### discourse-08: FIX: proper handling of group memberships

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 8 | 397.7k | $0.5703 | 65.1 | 0 / 0 / 2 | n/a | n/a |

### discourse-09: FEATURE: Localization fallbacks (server-side)

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 1 | 35.9k | $0.0770 | 21.8 | 0 / 0 / 1 | n/a | n/a |

### discourse-10: FEATURE: Can edit category/host relationships for embedding

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| thorough | ran | 11 | 419.4k | $0.7492 | 67.3 | 0 / 1 / 3 | n/a | n/a |
