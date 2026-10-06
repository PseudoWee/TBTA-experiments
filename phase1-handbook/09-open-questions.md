# 09 — Open questions, inconsistencies and gaps

A single source of truth must say where it is *not* certain. Everything below was noticed while consolidating.

## A. Numbering quirks in the source checklist (now resolved in this handbook)

The source had: two items numbered **0.3**; no **0.35** or **0.46**; no **§27** (numbering jumps 26 → 28); and a "See item 27 below" reference in 0.33 (now 0.34) with nothing to point to. The handbook **renumbers to 0.1–0.53 and §1–§35**; crosswalk at the top of file 03. Still open:

| Question | Note |
|---|---|
| Were 0.35, 0.46 and §27 retired, or missing from the PDF? | Confirm with the document owner. The dangling "See item 27" is likely stale. |
| §2.1 (can/able) vs "P1 Checklist 2.1" in the review skill | Likely the same item (the "XXXCan" item); reconcile. |
| Repo skills, `phase1-rules.md`, **and the Editor's own `phase1_rules.md`/AI prompt** use **source** numbers | Either renumber them to match, or keep the crosswalk. Checker IDs ↔ rules table now exists in file 06 §3 (from `checker_rules.ts`); mapping to checklist items is best-effort. |
| Page numbers (1–30) vs section numbers in the PDF | Different things. |

## B. Content that differs between sources

1. **Rules the SKILL.md carries that the rules file doesn't:** footnote-vs-comment distinction, digits-for-numbers, `(alt)` fix, pairing-order rule. The skill's own note says these "live only in this SKILL.md for now". This handbook now has them (files 04, 05, 07); **the repo's `phase1-rules.md` should be updated or retired** so the two don't drift.
2. **Doc +03 vs +02 on `(comment-begin)`.** +03 lists `(comment-begin)/(comment-end)` with `(begin-comment)/(end-comment)` as OK; +02 0.52 uses `(begin-poetry)/(end-poetry)` and §11 says `(poetry-begin)`… both orders are accepted by the checker (+03 says so).
3. **Paragraph notation.** +02 §11: `_paragraph` in P1; +03 and +02 0.52 writes `(paragraph)`. Treat `(paragraph)` as the external marker (the 0.52 text distinguishes internal/external markers) and `_paragraph` as the older note form. Confirm against the checker.
4. **`_explainName` vs `_implicitExplainName`; `_explainMetonymy` vs `_dynamicExpansion`.** Renamed over time (+03 notes). Which spelling the checker prefers is untested here.
5. **Rhetorical `(norhetorical)`** is mentioned in +03 and +02 but the +02 §33 survey of rhetorical types only covers "yes"-expected questions.
6. **Checker rule IDs are positional** (`checker:35` = the 36th JSON rule in `checker_rules.ts`), so they shift if rules are added or reordered. File 06 §3 reflects the source as read on 2026-10-06.
7. **Corpus entries and the live checker disagree frequently** (only 57 of 200 sampled corpus verses were fully clean). The corpus predates rules or the checker is stricter; no one has documented which.
8. **Level definitions disagree slightly.** +02 says blue = level 0 = "supposed to be available in every language"; +03 warns blue can also mean "nobody set the level". Treat a blue word with suspicion.

## C. Genuinely unsettled judgement calls

* **0.34 / `checker:48`** — negative verb + purpose/causal clause. The checker warns; the rule allows exceptions. No decision procedure beyond "context decides / too awkward otherwise". Flag every time.
* **Distributive `each … one`** — only a meaning-narrowing plural rewrite validates. Decide whether to ask for a checker/ontology change.
* **Literal vs dynamic vs implicit expansion** — when a multi-sentence expansion is justified vs drift. Working test: is it tagged `(implicit-situational)` and shown as `<<…>>`, or does a literal version fail to validate?
* **Perfect tense** — "recently AND previously both adequate" is a judgement.
* **Level 3 words** — Tod's intention is to restrict them to complex alternates eventually; today they're treated like level 2. Policy may change.
* **`way`** — "limited uses"; no definitive list.
* **He1 specifics** — the full He1 → He2 conversion process (and playlist 4) was not available; only the notation differences are documented.

## D. Known upstream bugs / gaps (not this project's to fix)

* Halah, Gozan, Habor not recognised as locations (logged upstream 2026-09-18).
* Verbs with no theta grid (`bring-D`, `be-Y`, `promise-C`) — warning is expected.
* Back-translator doesn't render `_past` on `come-out`.
* The `status` field can read `error` with no error messages.
* Sense-letter-tag outage on 2026-09-12 ~08:03 (resolved).
* `references/api-reference.md` still shows the stale AI-assist shape (`message`, `finish_reason`). The Editor README documents the current shape (`text` → `phase_1`, `notes`, `check`).
* Analyzer currently ignores `/Y` in pairings and doesn't auto-interpret `-B` tags — P2 handles them.

## E. Suggested clean-up tasks for the repo

1. ~~Update or retire `skills/niv-to-phase1/references/phase1-rules.md`~~ — **done 2026-10-06**: replaced with a copy of file 03 (renumbered).
2. Fix `tools/tabitha_editor_client.py` docs / `references/api-reference.md` AI-assist shape.
3. ~~Extract +01 and +03 into the skills' references~~ — **done 2026-10-06, by reference**: handbook files 02 and 04 are the extractions, and the `niv-to-phase1` skill (step 8 and the "Companion documents" section of `references/phase1-rules.md`) links to them by GitHub URL, so there is one copy to maintain.
4. ~~Build a checker-ID ↔ checklist-rule table~~ — **done**: file 06 §3 (best-effort mapping).
5. Decide the home of the NIV 1984 source (cannot be committed; keep as a project file).
6. Consider adding this handbook's rules index to the skills so each SKILL.md links here rather than restating.
