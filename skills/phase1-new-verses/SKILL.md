---
name: "phase1-new-verses"
description: "Use when drafting Phase 1 encodings for Bible verses that have NO prior corpus work (the ~13,000 of ~31,000 verses not yet in the 18,830-verse corpus), and logging them to the Phase 1 Encoding Watch dashboard."
---

# Encoding verses with no prior corpus work

The 18,830-verse corpus covers most, but not all, of the ~31,000 verses in the
Bible. This skill is for picking up the remainder — verses that have never
been encoded before at all — as opposed to `phase1-encoding-review`, which
fixes verses the corpus already has.

This is a recurring, incremental job: there are ~13,000 verses left, so
expect to run this skill many times across many sessions, each time picking
up a fresh small batch (5-20 verses is a reasonable size — enough to make
progress, small enough to hand-review every one against `/check`).

## Step 1 — pick the next batch of zero-coverage verses

Don't reconstruct and diff the full ~31,000-verse canonical Bible against the
corpus every time — that's expensive and has already been done once. Instead:

1. Read the Phase 1 Encoding Watch dashboard's Overview tab (or query its
 `missing_ontology_words`/`new_verses` collections via `ArtifactData`) for
 the list of books already confirmed to have **zero** rows in the corpus.
 As of 2026-09-23 that list was: 2 Chronicles, Job, Song of Songs,
 Lamentations, Amos, Obadiah, Zephaniah, Zechariah — but re-check the
 dashboard, since earlier runs of this skill will have started working
 through them.
2. Also check the `new_verses` collection (via `ArtifactData` "list" or
 "query") for which verses within those zero-coverage books have already
 been logged by a previous run of this skill, so you don't redo them.
3. Once every zero-coverage book has been exhausted, move to books that are
 only *partially* covered: pull that book's corpus rows (the `corpus`
 collection's `chunk_NN` docs, each `{count, index, verses:[{enc, ref,
 status}]}`) and diff its covered refs against the book's full verse list
 (from the raw NIV source) to find the gaps.

## Step 2 — draft, validate, iterate

For each verse in the batch:

1. Pull the raw NIV text via the `niv-to-phase1` skill's sourcing method
 (the project's `NIV1984 - original.doc`) — extract only the verse(s) in
 this batch, never more (copyright).
2. Draft a Phase 1 encoding following `niv-to-phase1`'s full workflow
 (pronoun elimination, apposition/`named X`, one-verb clauses, word
 complexity checks against the ontology, the mechanical pass), then apply
 the reviewer conventions and the literal/dynamic rule in Step 2a below.
3. Validate with `tabitha-editor-api`'s `/check` (load that skill for the
 client code and the browser-UA gotcha). Iterate on the checker's actual
 feedback — don't guess. Watch for the case-frame/bracket-adjacency
 parser quirks documented in that skill (e.g. a bracket starting with a
 numeral, or two clause-brackets placed back to back, both trigger a
 false inserted-"that").
4. Stop iterating once you hit `status: ok`, or `status: warning` with only
 residual messages that are genuinely unfixable (an ontology-absent proper
 noun, an ambiguous-part-of-speech warning with no better tag available).
 Don't chase warnings the ontology itself can't resolve.
5. Generate an AI-assist comparison via `/ai-assist/generate` on the same
 raw text, for the side-by-side column in the dashboard. Use a generous
 timeout (150-200s) per call — some verses are slow, and a batched script
 with the default 120s bash timeout can silently drop the last item's
 write.
6. If a word turns out to have zero ontology entries (confirmed via a
 direct `/search?q=<word>`), or an existing sense doesn't cover the way
 this verse uses it (e.g. only a person-name sense when the verse needs a
 place-name sense), that's a genuine ontology gap — log it in Step 4.

## Step 2a — Reviewer conventions and literal/dynamic pairs

These come from reviewer feedback (Isa 24:20 draft review). A first draft that
is structurally strong (clauses, tense, `_adj`, `bad-B`) still gets revised
on these points, so build them in from the start. When unsure, compare with
how Reviewers/Checkers changed earlier first drafts in the Zoho-drafted verses.

### Word choice: "method", not "way"

Avoid "way" (as in "in the same way that"). Prefer "method", or restructure
(`just-like`, be-U). "Way" survives mainly in early drafts (Exodus, 1 Kings)
and in the recently revised Luke, so usage is **not fully settled**. Default
to avoiding it; if a verse genuinely seems to need it, flag it in the batch
`note` for Richard/Mikayla to confirm rather than silently using it.

### Literal vs dynamic pairs (use for poetry and figurative language)

TBTA can carry both readings so field translators can choose, like
NLT vs KJV vs NASB.

- **(literal)** = what the text actually says. Any figurative clause, or any
  clause whose predicate only has its physical sense in the ontology, counts
  as literal. Test: look up the sense in the ontology. If the definition is
  the physical sense ("to be heavy" = has weight), using it of sins is
  literal. Same for "the earth will fall" and "the earth will never rise
  again".
- **(dynamic)** = an equivalent encoding of the intended meaning with the
  figure removed. E.g. literal "the earth's sins became too heavy for the
  earth" becomes dynamic "the sins of earth's people prevent earth's people
  from doing the work that God wants them to do, just-like a heavy load
  prevents a person from moving".

When to produce pairs:
- Mostly poetry/prophecy (nearly all of Isaiah 24; also Job, Song of Songs,
  Lamentations, Amos, Zechariah, i.e. most current zero-coverage books) and
  any verse with metaphor, personification, or idiom.
- Plain narrative/prose verses need no tags. Don't invent a dynamic version
  when the literal text already is the intended meaning.

Notation (from the reviewer's own draft):
- Untagged sentences are shared by both readings.
- A tag **precedes** the sentence it applies to: `(literal) <sentence>`,
  `(dynamic) <sentence>`.
- Literal sentences are grouped, followed by the dynamic sentences that
  replace them. Pairing is by meaning, not strictly one-to-one (two literal
  sentences may be answered by two dynamic ones, or one).
- A literal sentence is still fully encoded Phase 1, not a gloss. Each
  reading must independently follow every `niv-to-phase1` rule.

Example (Isa 24:20, reviewer's HE1 draft, abridged):

```
The earth is like a man who is-D drunk _adj and who stumbles when-C
_implicitSituational he walks. ...
(literal) For _implicit _conj the earth's sins became too heavy for the earth.
(dynamic) For _conj _implicit the sins of earth's people prevent earth's
people from doing the work that God wants them to do just-like a heavy load
prevents a person from moving.
(literal) So the earth falls. (literal) And the earth will not rise again.
(dynamic) The plans of earth's people will fail when they work.
(dynamic) And those people's plans will never succeed.
```

### Similes: "is like" (house form)

**Standard form: `The earth is like a drunk _adj person.`** Use plain `is like`
with an attributive adjective. Do not add `-U` and do not use a relative
clause for the simile unless the sense requires it.

Tested live against `/check` (2026-10-02):

- `The earth is like a drunk _adj person.` -> **ok**, no messages. BT "The
  earth is like a drunk person."
- `The earth is like a person [who is drunk _adj].` -> ok, but the checker
  suggests the attributive adjective instead.
- `The earth is-U like a person ...` / `be-U like a person ...` -> ok, but the
  checker suggests removing the sense since it is selected by default. `be-U`
  also backtranslates as "be like", not "is like".
- `The earth is-U a person [who is drunk].` / `be-U a person ...` -> **error**
  ("be-U: missing state ('like X')"). The reviewer's tentative HE2 form was
  not valid. `is-U drunk _adj` also fails (be-U cannot take a predicate
  adjective).
- `just-like` clauses also pass, e.g. `The earth will move _future [just like
  a drunk _adj man moves].` Use them when the comparison needs a verb.

### Other points from the reviewed draft

- Mark implicit information where the source leaves it unstated. Both of the
  reviewer's spellings are accepted by `/check`, but they are not
  interchangeable. Tested behaviour:
  - Underscore tags (`_implicitSituational`, `_implicitActiveAgent`,
    `_implicit`) attach to the **word immediately before them** and that word
    is shown as `<<...>>` in the backtranslation. Placement matters:
    `[when _implicitSituational the wind blows]` marks "when", but
    `shakes _implicitSituational [when ...]` wrongly marks "shakes".
  - `(implicit-situational)` marks the **whole bracketed clause**:
    `[when (implicit-situational) the wind blows]` gives `<<when the wind
    blows>>`.
  - `_implicitActiveAgent` needs the agent written out before it, e.g. `is
    shaken by the wind _implicitActiveAgent`. Bare `is shaken
    _implicitActiveAgent` errors ("A passive verb must have an explicit
    agent").
  - For implicit conjunctions, `For _implicit _conj ...` marks "For"; the
    reverse order `For _conj _implicit` gives an empty `<<>>`. Prefer the
    first order.
  Check the `<<...>>` span in the backtranslation to confirm the tag landed on
  the intended word or clause.
- Sense choices the reviewer varied: "crimes/transgressions" for the sin sense
  (vs `bad-B things`) and `fall-E` for the fall sense. `fall-E` passes
  `/check`. Bare "sins" fails with "Word must be a level 0 or 1", which is why
  `bad-B things` is used; "crimes/transgressions" was not tested, so run it
  through `/check` before using it.
- Baseline of a good draft: main and subordinate clauses right, tense marked
  (`_future`), `_adj` marked, `bad-B` for "sin". The points above refine a
  good draft; they do not replace those basics.

### Validating and logging pairs

- Run `/check` on each reading **separately**: strip the `(literal)` /
  `(dynamic)` tags and validate shared + literal sentences as one text, then
  shared + dynamic sentences as another. Don't send the annotated string
  unless you've confirmed `/check` tolerates the tags.
- In the dashboard doc (Step 3), keep `encoding` as the full annotated text
  (it renders in the current tab) and add an optional `variants` array per
  verse: `[{"type":"literal|dynamic","encoding","status","back_translation","messages":[...]}]`.
  The existing tab does not render `variants` yet; until the page HTML is
  updated, mention the pair in the batch `note`.
- `/ai-assist/generate` output is a single reading (literal-style). Use it
  only as the comparison column; don't expect pairs from it.

## Step 3 — log the batch to the dashboard

The "New Verses" tab (added 2026-09-23) reads live from the artifact's
`new_verses` collection, keyed by date. **You do not need to touch the
dashboard's HTML for a routine batch** — only write a new doc:

```
ArtifactData(action="set", url="<dashboard artifact URL>",
 collection="new_verses", doc_id="<YYYY-MM-DD>",
 data={
 "date": "<YYYY-MM-DD>",
 "note": "<what this batch covered and any systemic pattern>",
 "verses": [
 {"ref": "...", "niv": "...", "encoding": "...", "status": "ok|warning|error", "variants": [optional, see Step 2a],
 "back_translation": "...", "messages": [{"token","label","message","rule_id"}, ...],
 "changes": [{"was","now","reason"}, ...],
 "ai_assist": {"phase_1","notes":[...],"check_status","back_translation","messages":[...],"collapsed_count"}}
 , ...]
 })
```

Use one doc per date/batch (matches the `suggestions` collection's pattern).
If you batch is large, keep `ai_assist.messages` to the first ~8 with a
`collapsed_count` for the rest, same convention as `suggestions`.

## Step 4 — log ontology gaps found along the way

If Step 2 turned up a word with no ontology entry (or missing the sense the
verse needs), append it to the `missing_ontology_words`/`pending` doc (same
collection the "Missing from Ontology" tab reads):

1. `ArtifactData(action="get", ..., collection="missing_ontology_words", doc_id="pending")` to get the current `items` array and its `version`.
2. Append `{word, kind, refs:[...], first_seen, note}` — `note` should say
 what's missing (no entry at all vs. missing a specific sense) and how you
 worked around it in the encoding (usually rule 0.24's `named X`).
3. `ArtifactData(action="update", ..., data={"items": <full array>}, if_version=<version>)`.

## Never needed for a routine batch

Republishing the dashboard artifact itself. That's only needed the one time
a new tab or rendering change is added to the page — not for adding another
batch of verses, which is a pure `ArtifactData` write the existing "New
Verses" tab already knows how to render.

## Handbook (source of truth)

Rule numbers, notation and background for Phase 1 are maintained once, in the
TBTA-experiments repo's `phase1-handbook/` folder — this skill links there
instead of restating them. If this file and the handbook disagree, the handbook
wins; flag the difference to the user.

- Start here (reading order): https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/README.md
- Rules index, numbered 0.1–0.53 / §1–§35: https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/03-rules-checklist.md
- Notation reference: https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/04-notation-reference.md
- Checker rule IDs ↔ rules, API: https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/06-checker-and-api.md
- Lessons learned and playbooks: https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/07-lessons-learned.md, https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/08-playbooks.md
- Open questions: https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/09-open-questions.md
