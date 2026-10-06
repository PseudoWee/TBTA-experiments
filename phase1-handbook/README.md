# Phase 1 Handbook — the single source of truth

**Audience:** someone who has never seen this project and is reading it for the first time.
**Goal:** after reading this folder you can (1) explain what TBTA Phase 1 encoding is and why it exists, (2) write or review a Phase 1 encoding of a Bible verse that passes the TaBiThA checker, and (3) know what has been learned so far, and what is still unsettled.

This folder consolidates:

| Origin | What it is | Where it ended up |
|---|---|---|
| `+00 How to learn to do semantic representations` | The reading-order map and philosophy | `01-orientation.md` |
| `+01 Introduction to TBTA grammar` | Words → phrases → clauses, semantic roles, signal words | `02-grammar-foundations.md` |
| `+02 Phase 1 Checklist of Essential Information` | Checklist items -1.x, 0.1–0.53, and numbered sections 1–35 | `03-rules-checklist.md` |
| `+03 Summary of Specialized Notation for TBTA` | Every tag, bracket and alternate notation | `04-notation-reference.md` |
| `+04 Longman Defining Vocabulary` | The ~2,000-word list that defines "simple" | `05-vocabulary-and-complexity.md` |
| `+05 How to handle Complex Terms` (spreadsheet) | 1,469-row pairing / explication lookup | `05-vocabulary-and-complexity.md` + the full table at `skills/niv-to-phase1/references/complex-terms.md` |
| Everything learned by running the pipeline (editor API, review passes, scheduled-task runs, user corrections) | Failure patterns, cascades, corrected misconceptions | `07-lessons-learned.md` |
| The skills, scripts and dashboard in this repo | How to actually do the work | `06-checker-and-api.md`, `08-playbooks.md` |

## Read in this order

1. **`01-orientation.md`** — what this is, vocabulary (P1, P2, He1, He2, ontology, TBTA…), the pipeline, the tools. *Start here.*
2. **`02-grammar-foundations.md`** — the grammar model underneath all the rules. Without it the bracket rules look arbitrary.
3. **`03-rules-checklist.md`** — the rules themselves, grouped by theme, each with correct/incorrect examples.
4. **`04-notation-reference.md`** — the exact spelling of every tag (`_implicitNecessary`, `(imp)`, `(rhetorical)`, `(complex)`…).
5. **`05-vocabulary-and-complexity.md`** — which words you may use bare, and how to handle the rest (pairings, explications, complex alternates).
6. **`06-checker-and-api.md`** — how to run your encoding through the TaBiThA editor and read what it says.
7. **`07-lessons-learned.md`** — the long tail of real mistakes and their fixes. Read after you have tried a few verses; it will make much more sense then.
8. **`08-playbooks.md`** — step-by-step procedures (encode a new verse, review an existing one, use AI-assist), with full worked examples.
9. **`09-open-questions.md`** — known inconsistencies, unsettled judgment calls, and gaps in the sources. Read before you trust anything as final.
10. **`10-sources-and-provenance.md`** — where each fact came from, for when you need to check.

## Two reading tracks

* **"I need to understand it"** → 01, 02, 03 (skim), 05.
* **"I need to encode a verse today"** → 01 (glossary only), 08 (playbook), keep 03 and 07 open as reference, run everything through 06.

## Conventions used in this handbook

* `monospace` = text you would literally type in a Phase 1 encoding.
* ✅ = valid / preferred. ❌ = invalid or discouraged. ⚠️ = allowed with caveats.
* Rule numbers like **0.18** come from the "+02 Phase 1 Checklist" (renumbered, see below). Section numbers like **§19** are the numbered sections further down that same document. The source numbering had quirks (two items numbered 0.3, no 0.35/0.46, no §27); this handbook **renumbers into one running sequence (0.1–0.53, §1–§35)**. A crosswalk to the source numbers is at the top of `03-rules-checklist.md`. Repo skills and checker messages use the source numbers.
* **He1** vs **full notation (He2 / "phase 1")** — see `01-orientation.md`. Where a rule differs for He1 it says so; otherwise it applies to both.
* Examples marked *(source)* come from the original documents. Examples marked *(corpus)* come from reviewed verses in the project corpus. Unmarked examples were written for this handbook and illustrate a rule; they have not been separately verified against the checker.

## Status

Snapshot compiled 2026-10-06. The editor and ontology are live services that change; anything in `07-lessons-learned.md` about checker behaviour should be re-tested before relying on it (the lessons file explains why).
