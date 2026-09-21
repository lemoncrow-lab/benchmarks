# LemonCrow local lexical retrieval — 2026-09-21

This is the current **local** retrieval benchmark. Local LemonCrow uses lexical retrieval; hosted-only Zoekt and semantic channels are intentionally not part of this published result.

## Result

| Metric | Result |
| --- | ---: |
| Overall MRR | **0.6425** |
| hit@1 | **0.5701** |
| hit@3 | **0.7009** |
| p95 latency | **141 ms** |
| Scored cases | **6,292** |
| Repositories | **14** |

Per-gold MRR: definition **0.8658**, content **0.8732**, semantic-intent **0.2251**, SWE-bench **0.4981**, sessions **0.5581**.

Representative definition MRR: Django **0.8424**, Astropy **0.9550**, Requests **0.9390**, Xarray **0.9350**, Pytest **0.9850**, SymPy **0.7475**, Linux **0.9222**, LemonCrow **0.7840**.

## Integrity fixes applied before this run

The September audit found that the old harness could silently mis-score retrieval because frozen DB routing still pointed at the pre-July global workspace store, most frozen snapshots were empty, and hundreds of independent MRR queries shared one MCP session where near-duplicate suppression could blank later searches. The repaired harness now routes the frozen snapshot to the actual project-local store, rejects empty snapshots, and sends independent benchmark queries with hidden `force=true` to bypass session deduplication.

A controlled direct-engine check on Django showed July and current ranking were effectively unchanged (**0.8408 vs 0.8396 MRR**); after the harness repair, the real MCP benchmark returned **0.8424** definition MRR.

`lexical.json` contains the complete per-repo/per-gold result. `lexical.csv` is a lexical-only flattened export. `snapshot_counts.json` records the populated file/symbol counts used for the frozen fixtures. `benchmark-manifest.json` records commit, command, gold hashes, and headline metrics.

The older 7,213-pair cross-tool comparison uses a different historical corpus and remains published separately under `retrieval_2026_07_05`; do not directly compare its absolute MRR with this current 6,292-case release result.
