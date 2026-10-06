# 10 — Sources and provenance

| Handbook file | Built from | Notes |
|---|---|---|
| `01-orientation.md` | +00 *How to learn to do semantic representations*; TaBiThA monorepo `README.md`; repo `README.md`; `docs/scheduled-task-prompt.md`; project memory overview | Worked before/after taken from `niv-to-phase1/SKILL.md` |
| `02-grammar-foundations.md` | +01 *Introduction to TBTA Grammar* | Examples (`able-B`, Proverbs 26:6, §10 mistakes) from the source |
| `03-rules-checklist.md` | +02 *Phase 1 Checklist of Essential Information* (checklist −1.x, source 0.1–0.54 / §1–§36, renumbered here to 0.1–0.53 / §1–§35); repo `references/phase1-rules.md` | Regrouped by theme; crosswalk to source numbers at top of file |
| `04-notation-reference.md` | +03 *Summary of Specialized Notation for TBTA* + notation sections of +02 | |
| `05-vocabulary-and-complexity.md` | +04 *Longman Defining Vocabulary*; +05 *How to handle Complex Terms* (via `references/complex-terms.md`); +02 §1 | Fix table from review skill |
| `06-checker-and-api.md` | TaBiThA monorepo `apps/editor/README.md` and `apps/editor/src/lib/rules/checker_rules.ts` (rule-ID table, rate limit, AI-assist pipeline); `skills/tabitha-editor-api/SKILL.md`, `references/api-reference.md`, `skills/phase1-ai-assist/SKILL.md`, `tools/*`, run `summary.json` | AI-assist request/response shape corrected per live call 2026-09-10 |
| `07-lessons-learned.md` | `skills/phase1-encoding-review/SKILL.md` (≈84 KB of confirmed patterns), `skills/niv-to-phase1/SKILL.md` "mechanical pass", dashboard "Corrected understanding" | Verse references are the real corpus cases cited there |
| `08-playbooks.md` | `niv-to-phase1`, `phase1-encoding-review`, `phase1-ai-assist` workflows; scheduled-task prompt | Worked example 7 (donkey shape) and the Joshua 24:12 review table are *illustrative shapes*, not verified outputs |
| `09-open-questions.md` | Cross-reading all of the above | New analysis (inconsistencies are the compiler's observations) |

## Source links for +00 to +05

**No URLs exist for these in the Claude Project, the repo, or memory.** They are uploaded files in the Claude Project "Presciencelabs". What the documents themselves point to:

| Doc | File in project | Links / pointers found inside |
|---|---|---|
| +00 | `00 How to learn to do semantic representations.pdf` | Video: <https://youtu.be/wY5qipCMUgA>; names the Google Drive folder **"Helpful documents for semantic representations"** and the **"Start here TBTA Resource Guide"** (video playlists 1–4) — no URLs given |
| +01 | `01 Introduction to TBTA grammar.pdf` | none |
| +02 | `02 Phase 1 Checklist of Essential Information.pdf` | ontology <https://ontology.tabitha.bible> |
| +03 | `03 Summary of Specialized Notation for TBTA.docx.pdf` | refers to the Analysis Conventions document |
| +04 | `04 Longmans Defining Vocabulary.pdf` | <https://www.ldoceonline.com/> |
| +05 | `05 How to handle Complex Terms.xlsx` | none (repo copy: `skills/niv-to-phase1/references/complex-terms.md`) |

**To fill in:** the Drive folder link and the Start-here guide link (owner: whoever shared the folder with you).

## Where "Analysis Conventions" comes from

It is not a file in the project or repo. It is referenced only by +00 (the Drive folder "shows some ways of doing things") and +03 ("conventions for pronouns and clause brackets are described there"). It most likely lives in the same Google Drive folder, "Helpful documents for semantic representations". Not found in earlier conversation material either; supply the link or file to add it.

## Original documents (in the Claude Project "Presciencelabs")

* `00 How to learn to do semantic representations.pdf`
* `01 Introduction to TBTA grammar.pdf`
* `02 Phase 1 Checklist of Essential Information.pdf`
* `03 Summary of Specialized Notation for TBTA.docx.pdf`
* `04 Longmans Defining Vocabulary.pdf`
* `05 How to handle Complex Terms.xlsx`
* `NIV1984 - original.doc` (raw NIV; **not** redistributed)

## Repo components referenced

* `skills/niv-to-phase1/` — SKILL.md, `references/phase1-rules.md`, `complex-terms.md`, `feature-codes.md`, `scripts/get_verse.py`, `scripts/analyze_corpus.py`
* `skills/phase1-encoding-review/SKILL.md`
* `skills/phase1-ai-assist/SKILL.md`
* `skills/tabitha-editor-api/` (SKILL.md, `references/api-reference.md`)
* `tools/` — editor client, sampler, aggregators, `examples/verify_fix_*.py`
* `data/runs/2026-09-10T12-18/` — one calibration run; `data/corpus-sample/chunk_36.json` — one 471-verse slice
* `dashboard/index.html` — snapshot of the "Phase 1 Encoding Watch" artifact
* `docs/scheduled-task-prompt.md`

## Not covered (and why)

* `skills/niv-to-phase1/references/feature-codes.md` — the position-coded `semantic_encoding` feature table (877 rows): background for the stage *after* Phase 1; not needed to write Phase 1.
* The corpus itself — public at `presciencelabs/tabitha-databases`.
* Videos, the Paratext setup, the "Analysis Conventions" document (not supplied).

## Reference source: the TaBiThA monorepo

<https://github.com/CanIL-CA/tabitha> (MIT). Used as a reference alongside the project documents:

* `README.md` — app map, API rules (60 req/min per IP), architecture, the TBTA worked example.
* `apps/editor/README.md` — endpoint docs, User-Agent guidance.
* `apps/editor/src/lib/rules/checker_rules.ts` — the authoritative list of checker rules (basis of file 06 §3).
* `apps/editor/src/lib/server/ai_assist/` — `system_instruction.md`, `phase1_rules.md`, `repair_instruction.md`.
* `docs/tbta-to-tabitha.md`, `docs/decisions/` — background.

**Note:** the Editor's `phase1_rules.md` header says it was adapted from `PseudoWee/TBTA-experiments` (`skills/niv-to-phase1/references/phase1-rules.md`), so it still has the **source numbering** (two 0.3 items). The handbook's renumbered rules are not what the checker or AI prompt use; use the crosswalk in file 03.

## External links

* Ontology: <https://ontology.tabitha.bible>
* Monorepo: <https://github.com/CanIL-CA/tabitha>
* Editor: <https://editor.tabitha.bible> · source <https://github.com/CanIL-CA/tabitha/tree/main/apps/editor>
* Corpus/databases: <https://github.com/presciencelabs/tabitha-databases>
* Longman dictionary: <https://www.ldoceonline.com/>
* Live dashboard: <https://claude.ai/code/artifact/1cd587fd-95af-4303-b727-72970a21ffd3>

## Licensing note

The repo's original code and skill docs are MIT-licensed. The TBTA ontology, the Phase 1 notation system and the underlying corpus belong to the TaBiThA / PresienceLabs project; the NIV is copyrighted (Biblica/Zondervan). This handbook reproduces rules and short worked examples for training and reference; it does not include the NIV text beyond the few short phrases used as examples.
