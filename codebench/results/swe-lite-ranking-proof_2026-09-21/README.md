# SWE-bench Lite ranking-fix proof — 2026-09-21

Targeted LemonCrow-only smoke after the multi-symbol ranking fix, using `django__django-14007` and `pallets__flask-5014`, `claude-opus-4-8`, one rep each. Official SWE-bench grading resolved 2/2 tasks at $0.6597 total.

This is **targeted regression evidence, not a headline benchmark**. It exists to show the ranking fix moved the pathological Django trajectory from $0.7390 / 25 turns in the earlier validation run to $0.5180 / 20 turns while remaining correct; Flask resolved at $0.1418 / 6 turns.

The retrospective manifest marks this as debug/validation evidence because the surrounding development session still had live source changes. Future CodeBench runs pin Claude Code and record start/end source fingerprints automatically.

Binary mitmproxy `.flow` captures are intentionally not published.
