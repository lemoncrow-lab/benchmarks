# Review benchmark: golden50-plan-fake

> **Basis: the scripted driver (no model was called): the numbers describe the harness, not a model.** Nothing below is a result for a model. Do not quote it.

- Generated 2026-10-26T03:18:47+00:00 from corpus `golden-comment-prs` (50 pull requests, 0 labelled, 0 labels, digest `0cb96eadf6de`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD n/a, max calls n/a; used 218 calls and $2.07.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --driver fake --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/reports --name golden50-plan-fake`

_wall_seconds is the elapsed time of the AI stage; model_seconds sums each call's latency._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 49/49 | 4.4 | 0 | 37.4k | 980 | 0 | $0.0423 | $0.0290 | $0.0713 | 15.8 |

Means over complete reviews. A review whose tokens or dollars the provider did not report is left out of those columns, and counted in the checklist below, never read as zero.

## Findings, catch and noise

| Depth | P0 / P1 / P2 | Caught | Catch rate (95% interval) | Unmatched | Noise rate (95% interval) | USD per catch |
| --- | --- | --- | --- | --- | --- | --- |
| auto | 0 / 0 / 0 | 0/0 | n/a | 0/0 (0 repeat a caught bug) | n/a | n/a |

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
| auto | $0.0423 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: not ready.**
- the basis is the scripted driver (no model was called): the numbers describe the harness, not a model; only a live run can support a published figure

**Catch and noise: not ready.**
- the basis is the scripted driver (no model was called): the numbers describe the harness, not a model; only a live run can support a published figure
- auto: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- the basis is the scripted driver (no model was called): the numbers describe the harness, not a model; only a live run can support a published figure
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| auto | 49 | $0.0423 | $0.0290 | $0.0713 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-01: Enhanced Pagination Performance for High-Volume Audit Logs

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 10.2k | $0.0107 | 38.5 | 0 / 0 / 0 | n/a | n/a |

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 35.4k | $0.0377 | 39.6 | 0 / 0 / 0 | n/a | n/a |

### sentry-03: feat(upsampling) - Support upsampled error count with performance optimizations

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 41.9k | $0.0440 | 39.7 | 0 / 0 / 0 | n/a | n/a |

### sentry-04: GitHub OAuth Security Enhancement

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 25.5k | $0.0270 | 32.6 | 0 / 0 / 0 | n/a | n/a |

### sentry-05: Replays Self-Serve Bulk Delete System

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 20 | 275.5k | $0.2910 | 46.9 | 0 / 0 / 0 | n/a | n/a |

### sentry-06: Span Buffer Multiprocess Enhancement with Health Monitoring

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 28.5k | $0.0299 | 39.5 | 0 / 0 / 0 | n/a | n/a |

### sentry-07: feat(ecosystem): Implement cross-system issue synchronization

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 26.4k | $0.0283 | 38.2 | 0 / 0 / 0 | n/a | n/a |

### sentry-08: ref(crons): Reorganize incident creation / issue occurrence logic

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 16.7k | $0.0175 | 39.6 | 0 / 0 / 0 | n/a | n/a |

### sentry-09: feat(uptime): Add ability to use queues to manage parallelism

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 107.6k | $0.1131 | 41.7 | 0 / 0 / 0 | n/a | n/a |

### sentry-10: feat(workflow_engine): Add in hook for producing occurrences from the stateful detector

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 47.1k | $0.0500 | 33.1 | 0 / 0 / 0 | n/a | n/a |

### calcom-01: Optimize cache key overflow management with performance improvements

calcom/cal.com; unlabelled (0 labels).

Skipped: could not fetch the pinned commits: git -c protocol.version=2 fetch failed in repo: fatal: remote error: upload-pack: not our ref 7269aca1c02cb34a6f6526d81fc7662d8bf214ba

### calcom-02: Async import of the appStore packages

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 27.3k | $0.0288 | 4.8 | 0 / 0 / 0 | n/a | n/a |

### calcom-03: feat: 2fa backup codes

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 61.2k | $0.0729 | 6.2 | 0 / 0 / 0 | n/a | n/a |

### calcom-04: fix: handle collective multiple host on destinationCalendar

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 52.6k | $0.0551 | 7.6 | 0 / 0 / 0 | n/a | n/a |

### calcom-05: feat: convert InsightsBookingService to use Prisma.sql raw queries

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 17.3k | $0.0183 | 13.0 | 0 / 0 / 0 | n/a | n/a |

### calcom-06: Comprehensive workflow reminder management for booking lifecycle events

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 8 | 40.5k | $0.0444 | 3.9 | 0 / 0 / 0 | n/a | n/a |

### calcom-07: Advanced date override handling and timezone compatibility improvements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 12.3k | $0.0130 | 4.5 | 0 / 0 / 0 | n/a | n/a |

### calcom-08: OAuth credential sync and app integration enhancements

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 96.2k | $0.1379 | 7.1 | 0 / 0 / 0 | n/a | n/a |

### calcom-09: SMS workflow reminder retry count tracking

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 19.7k | $0.0228 | 9.3 | 0 / 0 / 0 | n/a | n/a |

### calcom-10: Add guest management functionality to existing bookings

calcom/cal.com; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 27.1k | $0.0290 | 9.6 | 0 / 0 / 0 | n/a | n/a |

### grafana-01: Anonymous: Add configurable device limit

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 24.0k | $0.0257 | 14.4 | 0 / 0 / 0 | n/a | n/a |

### grafana-02: AuthZService: improve authz caching

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 19.9k | $0.0212 | 18.6 | 0 / 0 / 0 | n/a | n/a |

### grafana-03: Plugins: Chore: Renamed instrumentation middleware to metrics middleware

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 34.4k | $0.0369 | 16.0 | 0 / 0 / 0 | n/a | n/a |

### grafana-04: Advanced Query Processing Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 9.8k | $0.0104 | 20.8 | 0 / 0 / 0 | n/a | n/a |

### grafana-05: Notification Rule Processing Engine

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 5 | 57.3k | $0.0605 | 20.1 | 0 / 0 / 0 | n/a | n/a |

### grafana-06: Dual Storage Architecture

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 30.6k | $0.0320 | 17.7 | 0 / 0 / 0 | n/a | n/a |

### grafana-07: Database Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 17.7k | $0.0186 | 16.7 | 0 / 0 / 0 | n/a | n/a |

### grafana-08: Frontend Asset Optimization

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 3.5k | $0.0038 | 17.2 | 0 / 0 / 0 | n/a | n/a |

### grafana-09: Advanced SQL Analytics Framework

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 10.9k | $0.0118 | 20.0 | 0 / 0 / 0 | n/a | n/a |

### grafana-10: Unified Storage Performance Optimizations

grafana/grafana; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 15.4k | $0.0166 | 19.4 | 0 / 0 / 0 | n/a | n/a |

### keycloak-01: Fixing Re-authentication with passkeys

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 33.8k | $0.0354 | 9.5 | 0 / 0 / 0 | n/a | n/a |

### keycloak-02: Add caching support for IdentityProviderStorageProvider.getForLogin operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 19.6k | $0.0203 | 9.3 | 0 / 0 / 0 | n/a | n/a |

### keycloak-03: Add AuthzClientCryptoProvider for authorization client cryptographic operations

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 26.5k | $0.0278 | 9.1 | 0 / 0 / 0 | n/a | n/a |

### keycloak-04: Add rolling-updates feature flag and compatibility framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 14.1k | $0.0150 | 10.2 | 0 / 0 / 0 | n/a | n/a |

### keycloak-05: Add Client resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 57.4k | $0.0596 | 10.1 | 0 / 0 / 0 | n/a | n/a |

### keycloak-06: Add Groups resource type and scopes to authorization schema

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 53.9k | $0.0563 | 9.8 | 0 / 0 / 0 | n/a | n/a |

### keycloak-07: Add HTML sanitizer for translated message resources

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 6 | 67.7k | $0.0709 | 10.6 | 0 / 0 / 0 | n/a | n/a |

### keycloak-08: Implement access token context encoding framework

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 91.8k | $0.1239 | 9.8 | 0 / 0 / 0 | n/a | n/a |

### keycloak-09: Implement recovery key support for user storage providers

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 35.9k | $0.0375 | 8.7 | 0 / 0 / 0 | n/a | n/a |

### keycloak-10: Fix concurrent group access to prevent NullPointerException

keycloak/keycloak; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 9.3k | $0.0099 | 6.3 | 0 / 0 / 0 | n/a | n/a |

### discourse-01: FEATURE: automatically downsize large images

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 6.2k | $0.0066 | 4.4 | 0 / 0 / 0 | n/a | n/a |

### discourse-02: FEATURE: per-topic unsubscribe option in emails

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 9 | 43.6k | $0.0488 | 4.6 | 0 / 0 / 0 | n/a | n/a |

### discourse-03: Add comprehensive email validation for blocked users

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 3 | 15.8k | $0.0172 | 2.4 | 0 / 0 / 0 | n/a | n/a |

### discourse-04: Enhance embed URL handling and validation system

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 8 | 44.5k | $0.0490 | 3.4 | 0 / 0 / 0 | n/a | n/a |

### discourse-05: Optimize header layout performance with flexbox mixins

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 5.9k | $0.0065 | 4.6 | 0 / 0 / 0 | n/a | n/a |

### discourse-06: UX: show complete URL path if website domain is same as instance domain

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 2 | 9.7k | $0.0104 | 5.4 | 0 / 0 / 0 | n/a | n/a |

### discourse-07: scale-color $lightness must use $secondary for dark themes

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 49.8k | $0.0542 | 5.2 | 0 / 0 / 0 | n/a | n/a |

### discourse-08: FIX: proper handling of group memberships

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 8 | 41.4k | $0.0459 | 4.0 | 0 / 0 / 0 | n/a | n/a |

### discourse-09: FEATURE: Localization fallbacks (server-side)

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 1 | 6.1k | $0.0065 | 4.3 | 0 / 0 / 0 | n/a | n/a |

### discourse-10: FEATURE: Can edit category/host relationships for embedding

discourse/discourse; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 10 | 55.3k | $0.0620 | 4.9 | 0 / 0 / 0 | n/a | n/a |
