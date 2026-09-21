# SWE-bench Lite release validation — 2026-09-21

Single-rep, LemonCrow-only validation on the repository's pinned 10-task SWE-bench Lite slice using `claude-opus-4-8`. Official SWE-bench grading resolved 10/10 tasks.

This directory is **validation/debug evidence, not a controlled headline A/B result**. The run used live bind-mounted LemonCrow source while fixes were landing, and the earlier July comparison run did not record its Claude Code CLI version. The retrospective `benchmark-manifest.json` therefore marks the run non-publishable as a controlled release comparison.

Aggregate observed result: $3.2270, 112 turns, 39,681 fresh input tokens, 116,941 cache-write tokens, 1,864,867 cache-read tokens, 37,069 output tokens, 602.5s wall time, 10/10 resolved.

Binary mitmproxy `.flow` captures are intentionally not published. Human-readable `*.flow_dump.txt`, patches, prompts, CSVs, and the report are included.
