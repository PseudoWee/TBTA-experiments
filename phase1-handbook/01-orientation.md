# 01 — Orientation: what this is and why

## The one-paragraph version

Bible translation teams working into many languages need a source text that is **unambiguous, simple, and easy to translate from mechanically**. **TBTA — The Bible Translator's Assistant** — takes a carefully prepared English "semantic representation" of the Bible and generates draft text in a target language from it. The first human-written layer of that representation is **Phase 1** ("P1"): ordinary-looking English rewritten under strict rules — one verb per clause, no third-person pronouns, no hard words, every subordinate clause bracketed, implicit information labelled. This project asks whether a modern LLM, helped by a rule-checker API, can take a raw **NIV** verse and produce a compliant Phase 1 encoding automatically.

## A tiny before / after

Raw NIV (1 Chronicles 10:2) *(from the project's `niv-to-phase1` skill)*:

> The Philistines pressed hard after Saul and his sons, and they killed his sons Jonathan, Abinadab and Malki-Shua.

Phase 1:

> The Philistines chased Saul and Saul's sons. And the Philistines came near Saul and Saul's sons. And the Philistines killed Saul's sons named Jonathan, named Abinadab, and named Malki-Shua.

Everything that changed is a rule at work:

| NIV | Phase 1 | Why |
|---|---|---|
| "pressed hard after" (one idiom) | "chased … came near" (two clauses) | Idioms are decomposed into simple events; each clause has exactly one verb (0.4) |
| "they", "his" | "the Philistines", "Saul's" | No third-person pronouns (0.1); same noun written the same way every time (0.36) |
| "his sons Jonathan, Abinadab…" | "Saul's sons named Jonathan, named Abinadab…" | Apposition is not allowed (0.40); "named" construction (0.24) |
| one sentence, two verb-phrases joined by "and" | three sentences, each starting "And" | You cannot glue independent clauses together (0.23) |
| "Abinadab and Malki-Shua" | "…, and named Malki-Shua" | Oxford comma in coordinate lists (0.42) |

## Glossary (read this once, refer back)

| Term | Meaning |
|---|---|
| **TBTA** | The Bible Translator's Assistant — software that generates target-language text from a semantic representation. *TaBiThA* is the web-era name for the same ecosystem (editor, ontology, databases). |
| **Phase 1 / P1 / "He2"** | The human-written, bracketed, fully-controlled English text. Strictest form. "He2" is the name used when contrasted with He1. |
| **He1** | A lighter-weight, natural-sounding English draft written *first* under the "new method". No brackets, pronouns allowed after the first mention, `<<…>>` / `<…>` for implicit information, complex words allowed. It is later *converted* to He2. |
| **Phase 2 / P2** | The computer-internal, more abstract representation. A person ("P2") converts P1 into it, setting features by hand where the analyzer cannot. Notes starting with `_` in P1 are messages to P2. |
| **Phase 3 / P3 / "English back translation"** | What TBTA generates in English from P2. Used to check that P1 meant what you intended. |
| **Analyzer** | The TBTA program step that automatically converts P1 → P2. It reads your English and guesses sentence structure, word senses and features. Its guesses are why some notation (signal words, `-B` sense tags) matter. |
| **Ontology** | The dictionary of every word TBTA understands, with senses (`go-A`, `go-B`), a complexity level, and argument structures ("theta grids"). Online at <https://ontology.tabitha.bible>. |
| **Theta grid** | A verb sense's list of arguments (Agent-like, Patient-like, Source, Destination, Instrument, Beneficiary…), which are required and which optional. Using a verb with a role not on its grid can never validate. |
| **Sense letter** | `-A`, `-B`… distinguishing senses of one word, e.g. `able-A` (ability) vs `able-B` (circumstantial). |
| **Complexity level 0–4** | 0 = semantic primitive, 1 = simple (mostly Longman Defining Vocabulary), 2 = complex, 3 = very complex/abstract, 4 = names and key terms. See file 05. |
| **Pairing** | `simple/complex`, e.g. `son/descendant`. Use the complex word if the target language has it, otherwise the simple one. |
| **Explication** | A phrase of simple words standing in for a complex word, e.g. `hard hat` for "helmet". |
| **Alternate** | A second version of a sentence — literal/dynamic, complex/simple, rhetorical/statement, meaning alternates. |
| **Implicit information** | Meaning that is not literally in the verse but helps the reader. Marked so a translator can switch it on or off. |
| **Corpus** | ~18,830 professionally reviewed Phase 1 encodings (of roughly 31,000 verses) held in the public repo `presciencelabs/tabitha-databases`. The calibration set for this project. |
| **TND / TNN** | Translator's notes sources used to settle interpretation (SIL Translator's Notes are the authoritative reference when available; the UBS Translator's Handbook is second). |
| **LDV** | Longman Defining Vocabulary (the ~2,000-word list used as the definition of "simple"). |

## The pipeline, end to end

```
 raw NIV verse
      │   (this project's LLM skills: niv-to-phase1, phase1-ai-assist)
      ▼
 Phase 1 encoding  ───────────►  TaBiThA Editor API /check
      ▲                            returns: status, per-word messages, back-translation
      │  fix & re-check                          │
      └──────────────────────────────────────────┘
      ▼   (human reviewers; "P2" person)
 Phase 2 semantic representation  ───►  TBTA generates target-language draft
```

Key idea: **the checker is the loop's judge, but it is not an oracle.** It validates syntax and case frames; it cannot tell you whether you dropped a clause or invented one. Content fidelity needs a human (or careful LLM) reading the back-translation against the NIV. File 07 has many examples of "passes the checker, wrong anyway".

## Philosophy in five sentences

1. **Literal first, dynamic as an alternate.** Represent what the text says; add dynamic/implicit versions so a translator can choose.
2. **Simple vocabulary.** Words are simple enough that nearly any language has them, or are paired/explicated to simple ones.
3. **Unambiguous structure.** Every clause has one verb and an explicit agent; every modifier attaches where you put it (relations modify verbs, so noun-modifiers go in relative clauses).
4. **Don't hide anything the target language might need.** E.g. no passives without an agent (some languages have no passive), no perfect tense unless "recently" and "previously" both work.
5. **Be teachable.** The source documents' own first piece of advice: the most important quality is being teachable — this process is "significantly different from any other translation process."

## The recommended learning path (from the original guide)

The original author recommends this order; the handbook mirrors it.

1. Set up resources (Paratext, Chrome, ontology app, editor).
2. Watch the intro videos (playlists 1 and 2 in the *Start here* guide; some are dated — early advice recommending Easy English/ICB as primary sources has been replaced by **NIV, NCV and NASB**).
3. Read the grammar introduction (file 02) — initially the red-text material too; later, for He1, the magenta material.
4. Watch the team demo videos (playlist 3).
5. Read the Phase 1 checklist (file 03).
6. Do the exercises in the "More Instructional Documents" folder.
7. Read the specialized-notation summary (file 04) and become familiar with the LDV list and complex-terms table (file 05).
8. Read existing P1 text — Matthew, Mark, Proverbs are recommended (final P1 lives in the TBTAP1 Paratext project; the English back translation in TBTAP3).
9. Write your own and get reviewer feedback.
10. Only later: switch to He1 (playlist 4).

## Tools and where they live

| Tool | URL / location | Used for |
|---|---|---|
| Ontology app | <https://ontology.tabitha.bible> | Look up words, complexity level, senses, theta grids. REST: `/search`, `/simplification_hints`, `/examples` |
| Editor | <https://editor.tabitha.bible> | Check encodings: `/check`, `/analyze`, `/ai-assist/generate` |
| Editor source | <https://github.com/presciencelabs/tabitha-editor> | Open-source code of the checker |
| Corpus | <https://github.com/presciencelabs/tabitha-databases> (`databases/`, Git LFS) | The 18,830 verified encodings (`Sources_…tabitha.sqlite`) |
| Longman dictionary | <https://www.ldoceonline.com/> | Check a sense of an LDV word |
| This repo | `PseudoWee/TBTA-experiments` | Skills, scripts, dashboard, run data |

## What the repo's automation does (so you recognise it when you see it)

* **Four Claude skills** (`skills/`): `niv-to-phase1` (raw verse → encoding), `phase1-encoding-review` (existing encoding → Was/Now/Reason table), `phase1-ai-assist` (ask the editor's own AI for a first draft), `tabitha-editor-api` (the HTTP client the other three use).
* **A scheduled task** (about every three hours): samples 200 not-yet-checked verses from the corpus, runs `/check`, ranks the rules that fire most, proposes verified fixes for a few verses, and stores everything in an artifact database shown on the "Phase 1 Encoding Watch" dashboard. See `docs/scheduled-task-prompt.md`.
* **Deliberate omissions:** the NIV 1984 text itself is not in the repo (copyright), nor is the full corpus (it already lives in `tabitha-databases`).
