# 11 — Drafter glossary (shared renderings for words the ontology doesn't handle)

Purpose: when a transliterated title/name or an unusual word has already been rendered somewhere in our TBTA work, **every drafter uses the same rendering** and the first drafter to find it records it here. Add a row whenever you find a precedent or settle a rendering; mention in your notes that you used it.

## Check this before inventing a rendering (any word the checker calls "not recognized" or that NASB transliterates but NIV translates)

1. **This file** (search the Hebrew/Greek transliteration and the English gloss).
2. **Compare translations.** If NASB transliterates and NIV translates (e.g. NASB *Rabshakeh* / NIV *field commander*), the NIV wording shows the meaning; then look for precedent.
3. **Ontology precedent:** `GET https://ontology.tabitha.bible/examples?concept=<word>&part_of_speech=<Noun|Verb|…>` lists where the concept is used (book, status, role) — e.g. `officer` is listed for 2 Kings 18:17-37, the Rabshakeh passage.
4. **Corpus precedent:** search `phase_1_encoding` in the corpus (CanIL-CA/tabitha, `tools/databases/`) for the phrase, in the same book and parallel passages (Kings/Isaiah, Samuel/Chronicles, Gospels).
5. Use the precedent exactly (rule 0.36: same wording at every occurrence), keep it ontology-valid, then add it below.

## Renderings

| Source word (NASB / NIV) | Use in Phase 1 | Referent form | Precedent / source | Checker |
|---|---|---|---|---|
| Rabshakeh — a title, not a personal name (NASB *Rabshakeh*; NIV *field commander*) | `the important officer` | `you(officer)`, `my(officer's)` | Earlier TBTA drafting already rendered it `important officer` (found by Yu Hui, 2026-11-17, in an earlier Kings draft; exact verse not confirmed here). The ontology `/examples?concept=officer` lists the concept in 2 Kings 18:17, 19, 23-28, 35-37 (the Rabshakeh passage). Same wording appears as `the 30 important officers` in 2 Samuel 23:23 (corpus sample). Isaiah 36:11-22 uses it (replaces my earlier `army leader of Assyria`). | `important` and `officer` are both level-1 ontology words; no errors |

## Notes

* A title that is not in the ontology (`Rabshakeh`) cascades errors if used bare; never write the transliteration as a name.
* Isaiah 36 parallels 2 Kings 18:17-37: keep the rendering identical in both.
