# LemonCrow Benchmarks

Historical benchmark results, datasets, and evaluation artifacts for LemonCrow.

This repository stores the **data** produced by the benchmark suite that lives in
[lemoncrow-dev](https://github.com/lemoncrow-lab/lemoncrow-dev). Keeping results
separate keeps the main repo lightweight.

## Structure

```
codebench/
  data/            Gold-standard evaluation datasets (content, definition, semantic, session, swebench)
  competitors/     Competitor configuration (codegraph.json)
  results/         Historical codebench run results (exploration, SWE-bench, etc.)

harbor/
  results/         Terminal-Bench 2.1 run results (harbor harness)

embedding/
  corpus.jsonl     Semantic search training corpus
  queries.jsonl    Evaluation query set
```

## Usage

The benchmark **code** (runners, harnesses, CLI) lives in the main repo.
Clone this repo alongside `lemoncrow-dev` if you need access to historical results:

```bash
git clone git@github.com:lemoncrow-lab/lemoncrow-dev.git
git clone git@github.com:lemoncrow-lab/benchmarks.git
```

Then set the results path in your config or environment:

```bash
export LEMONECROW_BENCH_RESULTS_DIR=../benchmarks
```

## Adding Results

After a benchmark run, copy results into the appropriate directory and commit.
Keep `*.flow` files and raw state directories out (they may contain API keys).