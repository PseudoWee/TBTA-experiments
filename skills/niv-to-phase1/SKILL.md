---
name: niv-to-phase1
description: "Converts raw NIV Bible verses into TBTA/TaBiThA \"Phase 1\" encoding — a controlled, unambiguous semantic representation used in Bible translation (with a lighter \"He1\" shorthand variant). Use this skill whenever the user pastes NIV verse text and asks for Phase 1 encoding, TBTA encoding, He1 encoding, or otherwise asks to \"encode\", \"convert\", or \"phase-1\" a verse — even if they just paste a verse reference plus \"Phase 1\" or \"He1\" with no further explanation. Also use it when checking whether an already-encoded verse follows the Phase 1 rules (bracket balance, pronoun rules, word complexity, etc.)."
---

# NIV → Phase 1 Encoding

Phase 1 encoding rewrites a natural NIV verse as an unambiguous, simplified
semantic representation: idioms and compressed predicates are unpacked into
their component simple clauses, third-person pronouns are eliminated in
favor of repeated full nouns, apposition is replaced by explicit relations,
and a large set of formatting/notation rules (brackets, tense marking,
implicit-info marking, etc.) apply. There are two output variants:

- **Full notation** — the default. Uses square brackets for subordinate
  clauses, explicit pronoun-referent parens, underscore tense/implicit
  notation.
- **He1** — a lighter shorthand. No brackets; uses `<<...>>` / `<...>` for
  implicit info; a few rules relax toward more natural wording (object
  complement clauses, imperatives, "and"-joined independent clauses).

If the user doesn't say which variant they want, default to full notation
and mention you did so — it's the stricter, more universally useful form,
and easy to loosen into He1-style prose afterward if they actually wanted
that.

## Sourcing the raw NIV text

When the user gives a reference (e.g. "1 Chronicles 10:2") rather than
pasting the verse text themselves, pull it from their own NIV source file
using `scripts/get_verse.py`:

```
python scripts/get_verse.py <path-to-their-NIV-docx> "<Book> <chapter>:<verse>"
```

The source file (`NIV1984_-_original.doc`, converted to `.docx`) is kept as
a project file for this project, not bundled with the skill itself — look
for it among the project's available files first. If it isn't there in a
given session (e.g. the skill has been exported/shared outside this
project), ask the user for its path, or ask them to paste the verse text
directly rather than reconstructing it from memory.

(Legacy `.doc` files need converting to `.docx` first — see the `docx`
skill.) This script reads only the one requested verse into memory/output;
it does not dump the surrounding text.

**Do not bundle a copy of the user's NIV file inside this skill's own
files, and do not print more of the source text than the verse(s) being
converted in any given turn.** The NIV translation is copyrighted; the
license here is to use it as a private reference for this conversion work,
not to reproduce or redistribute it. If the source file isn't available in
a given session, ask the user to paste the verse text directly instead of
reconstructing it from memory.

**When reviewing multiple verses in one sitting (a queue), print each raw
NIV verse at the top of your message alongside its encoding**, so the user
can compare source and output without looking it up separately.

## Workflow

1. **Read the verse for its actual meaning first**, not word-for-word.
   Idiomatic or compressed English predicates ("pressed hard after" =
   pursued + drew close) need to be decomposed into the separate simple
   events they represent, each becoming its own clause. Don't try to
   encode the English surface phrasing directly — encode what happened.

2. **Identify every noun referent and eliminate third-person pronouns.**
   Per rule 0.1, third-person pronouns (he/she/it/they/his/her/their/etc.)
   are never used — write out the full noun phrase every time instead, and
   keep that noun phrase worded identically at each occurrence (rule 0.36).
   Only first/second-person pronouns and "each-other" survive, each with a
   parenthetical referent: "I(John)", "you(Mary)". When choosing how to
   refer to a person or thing, prefer the most specific correct expression
   available — if the wider passage makes an unnamed figure's identity
   clear (e.g. "the Philistine" who is Goliath), use the known proper name
   rather than a generic description, even if that particular verse itself
   doesn't name them.

3. **Resolve apposition and "of"-meaning-"named" constructions.** A name
   directly following a noun ("his sons Jonathan, Abinadab...") is
   apposition, which is disallowed outside addressees (rule 0.40) — convert
   it to "named X" (rule 0.23), e.g. "Saul's sons named Jonathan, named
   Abinadab, and named Malki-Shua".

4. **Split into one-verb clauses.** Every clause has exactly one verb.
   Independent clauses from a single English sentence become separate
   Phase 1 sentences joined by "And ..." at the start of the next one
   (never a bracketed clause for an independent thought — see rule 0.22).
   Subordinate clauses get square brackets (omit brackets entirely if
   writing He1). Double check total left brackets = total right brackets,
   and no more than 4 levels of nesting (rule 0.4).

5. **Check word complexity before using any word — local lookup first, then
   the live ontology.**
   - **Check `references/complex-terms.md` first.** It's a 1,469-entry
     snapshot of the ontology's complex-term guidance (source: the project's
     "How to handle complex terms" spreadsheet), organized by status
     (in ontology / approved / suggested / not used) with the pairing or
     explication already recorded for most entries — using it skips a live
     API round-trip and sidesteps the stale-cache reliability caveat below.
     It also flags ~70 words known to be complex with no recorded guidance
     yet (the "Known-complex words with no how-to entry yet" section) —
     treat those as level 2/3 by default even before a live lookup confirms it.
   - If the word isn't in that file, or you need to confirm/refresh its
     status, call:
     `GET https://ontology.tabitha.bible/search?q={word}&scope=all`
   - Level 0/1 → usable directly.
   - Level 2/3 → cannot be used as a plain word (rule 0.2). Call
     `GET https://ontology.tabitha.bible/simplification_hints?complex_term={word}`
     to get a pairing, explication, or complex/simple alternate, and use
     that instead. Use `GET https://ontology.tabitha.bible/examples?concept={concept}&part_of_speech={pos}`
     if you need precedent for how a concept has been encoded before.
   - If the local table and a live lookup disagree, the live lookup wins —
     `complex-terms.md` is a snapshot, not a live mirror.
   - **Access note:** hitting these endpoints requires either the Chrome
     browser tool (connected and signed in) or a `web_fetch`-capable
     context where the URL is fetchable. If neither is available, say so
     plainly and flag which words you were unable to verify, rather than
     guessing a complexity level.
   - **Reliability caveat:** a `web_fetch` call built by editing the query
     string of a URL already fetched this session (e.g. changing `q=sling`
     to `q=rope`) has been observed to silently return the *previous*
     query's cached result instead of erroring — no warning, just wrong
     data. Never chain modified-query fetches back to back and trust them
     blindly; re-verify with a fresh Chrome browser-tool navigation, or ask
     the user to check, before relying on a second lookup in the same
     session.

6. **Apply the remaining notation/formatting rules** from
   `references/phase1-rules.md` — this is the full itemized ruleset (tense
   marking, implicit-info marking, imperatives, passives, quotations,
   numbers/units, poetry markers, punctuation, and everything else). Skim
   it for anything the verse touches; don't skip this step even for
   short-looking verses, since many rules are easy to trip on without
   noticing (double negatives, "can", "going to", stray third-person
   pronouns, apposition, isolated noun phrases).

7. **Reassemble and self-check** the final output against:
   - Bracket count balance (full notation only)
   - No disallowed third-person pronouns remaining
   - Every repeated noun phrase worded identically
   - Oxford commas in coordinate lists (rule 0.42)
   - Every level-2/3 word wrapped in a pairing/explication/complex-alternate
   - **The mechanical pass below** — quantifiers and notation hygiene. These
     are the cheapest errors to avoid and the most common ones to ship.

### The mechanical pass

Two classes of error fire constantly in the reviewed corpus and are fully
preventable at generation time. Run this pass over the finished string
before returning it; it is pure string inspection and needs no ontology
lookup.

**`all` before a specific noun must be `all of` (checker:35, P1 Checklist
0.17).** Bare `all` is only legal when the noun it modifies is *generic* —
an unbounded class, not a definite or demonstrative set. In practice every
`all the ...`, `all these ...`, `all those ...`, `all your(X's) ...` and
`all X's ...` needs `of`:

| Wrong | Right |
|---|---|
| `all the animals` | `all of the animals` |
| `all these animals` | `all of these animals` |
| `all the people [who lived previously]` | `all of the people [who lived previously]` |
| `all you(soldiers)` | `all of you(soldiers)` |

`all people are sinners` (generic class, no determiner) stays bare. When in
doubt, add `of` — the rule fires on the determiner, and a definite or
demonstrative determiner is the reliable tell. This is one of the densest
single-rule error sources in the corpus: in the 2026-09-10 calibration
sample it produced 15 errors across 5 verses, all of them a missing
two-letter token.

**Notation hygiene (`token:syntax`).** The checker tokenizes on whitespace
and punctuation, so a missing space is a hard error, not a cosmetic one —
and it cascades, because the malformed token poisons verb diagnostics in
the same clause the way an unrecognized word does. Verify each of these:

| Rule | Wrong | Right |
|---|---|---|
| Space **before** `[` | `David[who was ...]` | `David [who was ...]` |
| Space **after** `]` `.` `)` | `].../rape`, `.Why`, `(dynamic)John` | `] ...`, `. Why`, `(dynamic) John` |
| Space before `_` notes | `things_implicit`, `able_B` | `things _implicit`, `able-B` |
| Literal pairings use a pipe | `People\children` | `People\|children` (i.e. `dynamic\|literal`) |
| Only recognized clause notations | `(implicit-info)`, `(implicit)`, `(alt)` | `_implicit`, `_implicitNecessary`, or the notation named in `references/phase1-rules.md` |

Sense suffixes are hyphenated (`able-B`, `made-A`, `follows-B`), never
underscored — `able_B` is read as a notes tag and errors.

**`(alt)` specifically means you want a complex/simple alternate reading —
use `(complex) ... (simple) ...`, not `(alt)`.** There is no generic "here's
an alternate rendering" tag. The two real alternate-sentence pairs are
`(literal) ... (dynamic) ...` (a literal vs. dynamic translation pair) and
`(complex) ... (simple) ...` (rule 0.2's complex alternate — a level-2/3-word
sentence paired with its plain-language explication). 1 Kings 10:12 tried to
pair `The king also made harps and lyres...` with `The king also made
instruments [that had strings]...` under `(alt)`; because `(alt)` isn't a
real tag, the checker never registered the first sentence as a `(complex)`
context at all, so `harps` and `lyres` (both L2) were flagged exactly as if
written bare — retagging as `(complex) ... (simple) ...` cleared both errors
with no other change. Decide which pair you actually have before writing the
tag.

**Footnotes vs. parenthetical comments — different notations, easy to
conflate.** Both render as something in parentheses in English, but they are
not the same tag and the checker does not treat a bare literal `(` `)` pair
or an invented dash-prefixed token (`-Footnote`, `-CommentBegin`) as either
one — both fail as unrecognized syntax.

- A **parenthetical comment** — text that is literally inside parentheses in
  the NIV wording itself, e.g. Genesis 13:10's *"(This was before the LORD
  destroyed Sodom and Gomorrah.)"* — is marked `(comment-begin) ...
  (comment-end)` (`(begin-comment)` / `(end-comment)` are also accepted).
  This generates as `(...)` in English.
- A **footnote** — a translator-added note that is not itself part of the
  literal verse text (a unit-conversion aside, a textual-variant note) — is
  marked with `(footnote)` alone, with **no closing tag**. Everything after
  `(footnote)` is part of that footnote until the verse ends or a new
  `(footnote)` starts elsewhere; a footnote can only go at the end of a
  verse, never mid-verse.

Confirmed failure mode: Genesis 13:10's NIV parenthetical aside was twice
mis-tagged as a footnote (`-Footnote`, then later `(footnote)`) across two
review passes — both attempts cleared the checker (it validates the syntax,
not the linguistic choice), but the parenthetical-comment tag is the
correct one for content that is literally parenthesized in the source text.
Ask "is this literally in parentheses in the NIV, or is it a note I'm
adding" before choosing between the two.

**Numbers: use digits, not number words.** `two`, `three`, `forty`, etc. are
not recognized ontology entries — only the numeral form (`2`, `3`, `40`)
validates (`checker:built-in:7`, "not recognized"). This fires constantly
across the corpus (Genesis 13:10, Joshua 24:12, Ezra 8:32, Luke 9:13 among
others) and is a pure find-and-replace with no judgment call — spell out a
number in the English backtranslation if needed, but encode it as a digit.

**Tag an ambiguous part of speech rather than leaving it.** When a word can
be read as more than one part of speech, append the tag as a separate
space-preceded token: `living _verb`, `gold _noun`, `first _adv`. This is
not merely warning-suppression — an untagged ambiguous word cascades into
`does not match any sense in the Ontology` errors on the surrounding verb
and adpositions. In 1 Kings 10:16 a single `gold _noun` cleared errors on
both `make` and `with` that looked like genuine case-frame faults.

**If the semantically obvious tag makes things worse, try the word's other
listed sense instead of giving up.** A word can have more than one
plausible tag, and one sense's case frame can be pickier than another's
about what sits next to it. On 1 Kings 10:12, `more-than` has both an
Adposition sense (case frame demands a bracket immediately after it) and an
Adjective sense (no such demand). `more-than _adp` — the "obvious" tag,
since it governs a bracketed clause like a preposition — broke that
adjacency and turned the warning into a real error; `more-than _adj`
cleared it to zero messages with the same meaning. Check the `lookup_results`
in the `/check` response for every sense a word has before writing off a
POS warning as unfixable.

**Pairing order is always simple word first, complex word second**
(`animal/donkey`, not `donkey/animal`; `poles/beams`, not `beams/poles`
— confirmed on 1 Kings 10:12, where the ontology's own suggested pairing for
`beam` is `pole`). The backtranslation still shows the complex word
(`poles/beams` reads back as "beams"); the simple word on the left is what
makes the pairing valid, not what shows up in the output.

8. **If something depends on grammar or notation detail beyond what's in
   this skill's own reference files** (see the "Companion documents" note at
   the end of `references/phase1-rules.md` for what's available as a project
   file but not yet extracted into a dedicated reference), say so explicitly
   in your answer rather than silently guessing.

## Worked example

Raw NIV (1 Chronicles 10:2):
> The Philistines pressed hard after Saul and his sons, and they killed his
> sons Jonathan, Abinadab and Malki-Shua.

Phase 1 (full notation):
> The Philistines chased Saul and Saul's sons. And the Philistines came near
> Saul and Saul's sons. And the Philistines killed Saul's sons named
> Jonathan, named Abinadab, and named Malki-Shua.

What happened here, rule by rule:
- "pressed hard after" (one idiomatic English predicate) → decomposed into
  two real component events, "chased" and "came near", each its own
  sentence (step 1).
- "they" / "his" (third-person pronouns) → "the Philistines" / "Saul's"
  written out in full every time (rule 0.1, 0.36).
- "his sons Jonathan, Abinadab and Malki-Shua" (apposition) → "Saul's sons
  named Jonathan, named Abinadab, and named Malki-Shua" (rules 0.40, 0.23).
- One independent English sentence with two verb-phrases ("pressed hard
  after ... and killed") → three separate one-verb Phase 1 sentences joined
  by "And" (rule 0.3, 0.22).
- Oxford comma before "and Malki-Shua" (rule 0.42).

## Worked example 2 — decomposing a level-2/3 instrument noun

Raw NIV (1 Samuel 17:50):
> So David triumphed over the Philistine with a sling and a stone; without
> a sword in his hand he struck down the Philistine and killed him.

Phase 1 (full notation, per user correction):
> So David defeated Goliath with a rope and a stone. David threw/slung
> that stone at Goliath with the rope. And David killed Goliath without a
> sword.

What happened here:
- "sling" (noun) is L2 in the ontology, pairing → "rope"; "sling" (verb) is
  L2, pairing → "throw-A". Rather than swap in the pairing word-for-word,
  the sentence was decomposed into the general statement ("with a rope and
  a stone") plus a second clause spelling out the actual slinging action
  ("threw/slung that stone at Goliath with the rope") — don't just
  substitute a pairing in place; make sure the resulting sentence actually
  describes the event using it.
- Discourse-connective "So" at the start of the verse was kept, since it
  reflects a real logical link to the preceding verses, not dropped by
  default.
- "the Philistine" → "Goliath": confirmed general practice — prefer the
  most specific correct referring expression available, even if the raw
  verse itself doesn't name the person. If the wider passage makes the
  identity unambiguous, use the known proper name instead of a generic
  description like "that Philistine", since it's clearer for translators.

## Calibration against the verified corpus

`Sources_2026-07-27_tabitha.sqlite` (kept as a project file, not bundled in
this skill) contains ~18,830 professionally reviewed `phase_1_encoding`
rows keyed by book/chapter/verse, alongside a `Features` table of
grammatical feature codes for the deeper `semantic_encoding` stage. Aligning
all of them against the NIV docx (in memory only — never written back out
as a merged file) gives real expectations to calibrate against, not just
the handful of examples above:

- **~2.4 Phase 1 sentences per NIV sentence on average.** Aggressive
  decomposition (step 4) is the norm, not the exception.
- **Subordinate-clause brackets appear in ~92% of verses.** Don't default
  to flat, bracket-free sentences unless the verse is genuinely simple —
  most real verses need at least one relative or event clause.
- Implicit-info marking appears in ~36% of verses, imperatives in ~18%,
  apposition-to-"named" in ~12%, passive-with-implicit-agent in ~9%,
  rhetorical questions in ~3%.
- `scripts/analyze_corpus.py` reproduces these stats and can be re-run
  against an updated export of the sqlite file.

A few more real examples worth internalizing (raw NIV / Phase 1):

- **Imperative + verse-boundary subject supply** (1 Samuel 1:14): the raw
  verse is just *"and said to her, 'How long will you keep on getting
  drunk? Get rid of your wine.'"* — the subject ("Eli") is only recoverable
  from the previous verse. Phase 1 supplies it explicitly: *"Then Eli said
  to Hannah, [\"You(Hannah) (imp) do not become drunk! You(Hannah) (imp)
  throw-away your(Hannah's) wine!\"]"* — don't assume a verse is
  self-contained; check the surrounding verses for an implied subject
  before encoding.
- **Passive with implicit agent + imperative together** (1 Corinthians
  6:20): raw *"you were bought at a price. Therefore honor God with your
  body"* → *"For you(friends) were bought by God _implicitActiveAgent for a
  price. Therefore, you(friends) (imp) honor/glorify God through-B
  your(friends') body."* — the implicit passive agent ("by God") is
  supplied per rule 0.13, and "friends" is supplied as the addressee
  referent for "you" since it's the first mention in this stretch.
- **Rhetorical question + statement pair** (2 Corinthians 3:8): raw *"will
  not the ministry of the Spirit be even more glorious?"* →
  *"(yesrhetorical) Will the work of the Spirit be more great/glorious?
  (statement) The work of the Spirit will certainly be more
  great/glorious!"* per rule 0.14 — always follow a rhetorical question with
  its statement form, and note "ministry" was resolved to a pairing
  ("work") rather than used directly.

## Reference

`references/phase1-rules.md` — the full 54-point Phase 1 rule checklist,
verbatim, with the He1-specific carve-outs noted inline. Read this whenever
you need the exact wording of a rule or you're unsure whether a construction
is allowed. Note: this reference file does not yet include the footnote-vs-
parenthetical-comment distinction, the digit-numbers rule, the `(alt)`
notation fix, or the pairing-order rule added above — those live only in
this SKILL.md for now.

`references/complex-terms.md` — the 1,469-entry complex-term pairing/
explication lookup table (source: the project's "How to handle complex
terms" spreadsheet). Check this before any live `/simplification_hints`
call — see step 5.

`references/feature-codes.md` — the position-coded grammatical feature
table for the deeper `semantic_encoding` stage (source: the project's
`Sources_...tabitha.sqlite` file). Background reading, not needed for most
Phase 1 conversions.

`scripts/analyze_corpus.py` — re-run this against an updated export of the
project's sqlite file and the NIV docx to refresh the calibration stats
above, or to pull fresh real examples for a rule that needs one.