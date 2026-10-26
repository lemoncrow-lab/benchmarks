# Review benchmark: replay-test

> **Basis: a replay of fixtures an earlier run recorded.** Nothing below is a result for a model. Do not quote it.

- Generated 2026-10-26T04:18:28+00:00 from corpus `golden-comment-prs` (1 pull requests, 0 labelled, 0 labels, digest `193810495c3c`).
- Route: claude / sonnet. Depths: auto.
- Ceiling: max USD n/a, max calls n/a; used 4 calls and $0.3423.
- Command: `lemoncrow dev eval review benchmark --corpus evals/review/golden_comment_prs.yaml --depth auto --driver replay --pr sentry-02 --no-pushes --workdir /home/user/bench-data/workdir --out-dir /home/user/bench-data/dev/scratch --name replay-test --fixtures-dir /home/user/bench-data/dev/records-run1`

_wall_seconds is the elapsed time of this replay and is not comparable; model_seconds sums the recorded latency of each call._ _the spending ceiling is checked before each call, so a run can pass it by the calls in flight (at most the investigators of the deepest depth)._

## Cost and speed per review

| Depth | Complete | Calls | No-call reviews | Tokens in | Tokens out | of which context | USD mean | USD median | USD p90 | Wall s |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | 1/1 | 4.0 | 0 | 152.0k | 4.6k | 0 | $0.3423 | $0.3423 | $0.3423 | 37.5 |

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
| auto | $0.3423 | n/a | n/a | n/a | n/a |

## Is a number ready to publish?

**Cost per review: not ready.**
- the basis is a replay of fixtures an earlier run recorded; only a live run can support a published figure
- only 1 repository; at least 2 are needed
- auto: 1 complete reviews with a known cost; at least 8 are needed

**Catch and noise: not ready.**
- the basis is a replay of fixtures an earlier run recorded; only a live run can support a published figure
- auto: 0 labelled pull requests scored; at least 8 are needed
- catch and noise are rates over a handful of pull requests; quote them with their intervals

**Head to head with the other reviewer: not ready.**
- the basis is a replay of fixtures an earlier run recorded; only a live run can support a published figure
- 0 pull requests carry the other reviewer's comments; at least 8 are needed
- no baseline comment has a verdict, so its precision is unknown

Figures a cost-per-review sentence would be built from (only when the cost block above is ready):

| Depth | Reviews | Mean | Median | p90 |
| --- | --- | --- | --- | --- |
| auto | 1 | $0.3423 | $0.3423 | $0.3423 |

Whatever is published:

- name the model and its price list date; the figure is for that model only
- state that it is the mean over this corpus, which is not the reader's code
- do not publish another reviewer's price from this report: it holds only what you supplied

## Per pull request

### sentry-02: Optimize spans buffer insertion with eviction during insert

getsentry/sentry; unlabelled (0 labels).

| Depth | Status | Calls | Tokens | USD | Wall s | P0 / P1 / P2 | Caught | Unmatched |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| auto | ran | 4 | 156.6k | $0.3423 | 37.5 | 0 / 0 / 0 | n/a | n/a |
