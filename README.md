# TBTA experiments

Tooling, skills, and calibration data for encoding NIV Bible verses into
**TBTA/TaBiThA "Phase 1" encoding** — a controlled, unambiguous semantic
representation used in Bible translation — and for checking that encoding
against the [TaBiThA editor API](https://editor.tabitha.bible).

This repo is the working snapshot of a Claude-driven pipeline: a scheduled
task samples 200 verses from an 18,830-verse corpus every ~3 hours, runs
them through the editor's rule checker, reports which rules dominate, and
proposes verified corrections for a few verses. Everything below was
produced by that pipeline (or the skills/tools it runs on) rather than
hand-written from scratch.

## Layout

```
skills/                  Claude skills — how to talk to the editor API and how to encode/review verses
  tabitha-editor-api/       Thin client for /check, /analyze, /ai-assist/generate
  niv-to-phase1/            Converts raw NIV text into a new Phase 1 encoding
  phase1-encoding-review/   Reviews an existing encoding, proposes a Was/Now/Reason fix table
  phase1-ai-assist/         Wraps the editor's own AI-assist endpoint

tools/                   Standalone scripts the skills' instructions describe, kept runnable on their own
  tabitha_editor_client.py  The /check, /analyze, /ai-assist/generate client (also inlined in the skill)
  sample_and_check.py       Sample N verses from a corpus slice and batch-check them
  aggregate.py               Turn batch-check results into the run/suggestions JSON shapes
  build_run_doc.py           Assemble a "runs" collection document
  build_suggestions.py       Assemble a "suggestions" collection document
  examples/                  Isolated before/after checks used to verify specific fixes

data/                    One calibration run's raw output, kept as a worked example
  runs/2026-09-10T12-18/    run.json, suggestions.json, summary.json, sampled_verses.json, per_verse_results.json
  runs/skill_notes_pending_snapshot.json
  corpus-sample/chunk_36.json  One 471-verse slice of the corpus (see "Corpus data" below)

dashboard/index.html     Static snapshot of the "Phase 1 Encoding Watch" dashboard artifact
docs/scheduled-task-prompt.md  The exact prompt the scheduled task runs every ~3 hours
```

## The live dashboard

The data in `data/` and `dashboard/` is a point-in-time snapshot. The live,
continuously-updated version — Overview / Sample runs / Suggested changes /
Skill notes / Changelog tabs, aggregating every run since 2026-09-09 — is
published as a Claude Artifact:

https://claude.ai/code/artifact/1cd587fd-95af-4303-b727-72970a21ffd3

## Corpus data

The full 18,830-row corpus (`Sources_2026-07-27.tabitha.sqlite`) is **not**
mirrored in this repo. It already lives in the public
[`presciencelabs/tabitha-databases`](https://github.com/presciencelabs/tabitha-databases)
repository; `data/corpus-sample/chunk_36.json` here is just the one
471-verse slice this session happened to sample from, kept as a concrete
worked example rather than a redundant copy of the whole corpus.

## What's deliberately not in this repo

- **`NIV1984 - original.doc`** (the raw NIV 1984 source text some of the
  skills reference for verse lookup) is not included. NIV 1984 is a
  copyrighted modern translation (Biblica/Zondervan), and this repo is
  public — redistributing the full text here isn't something to do
  regardless of how it's obtained. `skills/niv-to-phase1/scripts/get_verse.py`
  is included because it's just a lookup utility with no Bible text
  embedded in it; point it at your own licensed copy of the docx.
- **Full batch-check output** from the 12:18 run (`check_results.json`,
  ~18 MB of raw per-verse API responses) is summarized instead, via
  `per_verse_results.json` and `summary.json` — the aggregated shapes
  actually used downstream.

## Running it yourself

```bash
# Check one encoding string against the editor API
python3 tools/tabitha_editor_client.py   # import check()/batch_check()/ai_assist_generate() from this module

# Re-run the same 200-verse sample this repo's data/ came from
python3 tools/sample_and_check.py
```

Each skill's `SKILL.md` under `skills/` is self-contained and documents the
Cloudflare User-Agent requirement, the request/response shapes, and (for
`phase1-encoding-review`) the recurring failure patterns worth checking for
before assuming a fresh case-frame problem.

## License

Original code and skill documentation in this repo (everything under
`skills/`, `tools/`, `docs/`) is MIT-licensed — see [`LICENSE`](LICENSE).
That covers the tooling only, not the TBTA ontology, the Phase 1 notation
system itself, or the underlying verse corpus, which belong to the
[TaBiThA / PresienceLabs](https://github.com/presciencelabs) project.
