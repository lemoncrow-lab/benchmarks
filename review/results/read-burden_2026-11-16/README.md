# LemonCrow read-burden benchmark

How much a reviewer must read again when a coding agent pushes again, measured on 53 public, agent-written pull
requests (294 revisions, 241 revision-to-revision transitions), under three rule sets: GitHub's
file-level "Viewed", hunk level, and LemonCrow's. `report.md` is the result and its method.

This directory redistributes **no third-party file or code base**. The pull requests belong to their authors and stay
under their own licences (`ATTRIBUTION.md`). The only text of theirs in it is a few changed lines that `report.md` and
`expected.json` quote to explain findings (below). What is here is the report, the list of pull requests and revisions, and a script that
fetches them from GitHub and checks every file against a hash.

## Files

| File | What it is |
| --- | --- |
| `report.md` | The report: totals, per-pull-request rows, why parts were reopened, method, limitations. |
| `manifest.json` | How the corpus was selected: when, how many candidates, why candidates were rejected, the selection caps. |
| `sources.json` | The fetch list: for each pull request its revisions (base and head commit sha) and every changed file's path and git blob id, plus where each repository's licence files are. No file text. |
| `expected.json` | The per-transition counts the report is computed from. |
| `fetch_corpus.py` | The fetcher. Python 3.10+ standard library and `git`; nothing else. |
| `ATTRIBUTION.md` | Each pull request, its repository's licence and its attribution line. |

## 1. Fetch the pull requests

```bash
python3 fetch_corpus.py sources.json corpus/                      # all 53 pull requests
python3 fetch_corpus.py sources.json corpus/ --pr 'owner/repo#123' # one pull request (repeatable)
```

For each pull request the script fetches each revision's base and head commit with `git fetch --depth=1` over https
into a cache directory (`$XDG_CACHE_HOME/read-burden-fetch`, outside any checkout; `--cache` changes it), reads each
changed file with `git cat-file blob <sha>:<path>`, and keeps it only if its git blob id equals the one in `sources.json`.
No token is needed and no API rate limit applies. Nothing from a fetched repository is checked out, built or run.
Your own git configuration is not read, so a `url.insteadOf` rewrite there cannot redirect it; a proxy is taken from
`HTTPS_PROXY`. `corpus/` must be a separate directory, empty (or pass `--replace`: the files rebuilt are moved in only once fetching
is over, so a failed run deletes nothing). It may not be the directory that holds `sources.json`. A run with `--pr`
rebuilds only those pull requests and never refreshes `manifest.json` (it warns when one is already there); stale pull
request files are pruned only by a complete, unfiltered run.

It never guesses:

- A commit GitHub no longer serves (a force-pushed head, a deleted repository) is reported by name: pull request,
  revision, sha. It is not replaced by another commit, and that pull request is not written.
- A file whose hash differs from the manifest is reported by path and not used; that pull request is not written either.
- A network failure is reported for that pull request and the next one is tried.

The exit status is 0 when everything was rebuilt, 1 when anything was not, and 2 for an unusable argument or manifest.
Pull requests that were rebuilt are written as `corpus/prs/*.json.gz`, with `corpus/licences.json.gz`; a complete,
unfiltered fetch also copies `manifest.json` to `corpus/`.

## 2. Recompute the report

The numbers come from LemonCrow's own review engine, so recomputing them needs the LemonCrow product code. This bundle
does not contain it. From a checkout of the LemonCrow repository (Python 3.13, `uv`):

```bash
uv run python -m lemoncrow.pro.capabilities.review.evaluation.read_burden \
    --corpus /path/to/this/bundle/corpus --report /path/to/this/bundle/recomputed-report.md
diff recomputed-report.md report.md
```

The benchmark module is `src/lemoncrow/pro/capabilities/review/evaluation/read_burden.py`. For a complete fetch the two reports are identical byte for byte. The one line
that can differ on another machine is `stored size`: it is the size of the gzip files, and another zlib can compress the
same text differently. Every count must match regardless. A partial fetch (`--pr`, or pull requests that could not be
rebuilt) gives a report over those pull requests only; compare its rows with the same rows of `report.md` and
`expected.json`.

## Licences

Each pull request is of a public repository under a permissive licence (MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause
or ISC); the fetcher also fetches each repository's licence files at the commit named in `sources.json` and checks them
the same way. `ATTRIBUTION.md` lists them. `report.md` and `expected.json` quote a few changed lines of those pull
requests (about 30 lines each) where they explain a finding, such as why a part was reopened or
which changed line no part covers; they are quoted for that purpose and belong to their authors.
