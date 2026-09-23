---
name: "phase1-encoding-review"
description: "Review an existing TBTA/TaBiThA Phase 1 encoding against the editor API and suggest corrections as a Was/Now/Reason table that names the specific rule behind each change. Use when asked to fix, correct, improve, or suggest changes to an already-encoded verse."
---

# Phase 1 Encoding Review

For **correcting an encoding that already exists** — in the corpus, or pasted
by the user. For converting raw NIV text into a new encoding, use
`niv-to-phase1` instead; this skill assumes an encoding is already in hand
and the job is to find what the checker rejects and propose the fix.

The deliverable is always: a corrected encoding that the API accepts, plus a
table justifying every change against a named rule. Never hand back a fix
you have not re-run through `/check`.

**When reviewing multiple verses in one sitting (a queue), print each raw
NIV verse at the top of your message alongside its review**, so the user
can compare source and output without looking it up separately.

## Workflow

1. **Get the current encoding and its check result.** Use the
   `tabitha-editor-api` skill (apply its User-Agent patch first, or every
   call 403s). Walk the message tree recursively — `messages[]` nest inside
   `sub_tokens[]`, and a flat scan misses most of them.

2. **Separate root causes from cascades before fixing anything.** The
   checker says so itself: *"because this word is not recognized, errors and
   warnings within the same clause may not be accurate."* An unrecognized
   word poisons every diagnosis in its clause. Isolate each suspect error in
   a one-clause test string and re-check — if it disappears, it was a
   cascade, and fixing the unrecognized word fixes it for free. If it
   survives isolation it is real: `buy-A` in Exodus 13:13 stayed under
   isolation and proved to be a genuine word-order fault. Skipping this step
   produces "fixes" for errors that were never real, and misses ones that
   were. **A malformed clause cascades exactly like an unrecognized word** —
   see "Cascade sources that are not unrecognized words" below, and clear
   those before re-picking any verb sense.

3. **Look up every word you intend to change or keep.**
   - **Check `../niv-to-phase1/references/complex-terms.md` first** for any
     word that looks level 2/3 — it's a 1,469-entry snapshot of the
     ontology's complex-term guidance (source: the project's "How to handle
     complex terms" spreadsheet), organized by status (in ontology /
     approved / suggested / not used) with the pairing or explication
     already recorded for most entries, plus ~70 known-complex words with no
     recorded guidance yet. It skips a live round-trip for the common case,
     but several entries have structure-specific variants (see note below
     the repeat-offenders table) — confirm anything non-obvious live.
   - `GET https://ontology.tabitha.bible/search?q={word}&scope=all` — level
     and, for verbs, the **categories list, which is the theta grid**
     (Agent-like / Patient-like / Source / Destination / Instrument /
     Beneficiary). A verb used with a role its grid does not list can never
     validate.
   - `GET https://ontology.tabitha.bible/simplification_hints?complex_term={word}`
     for any level-2/3 word — gives the pairing or explication to use. Read
     `ontology_status` alongside `level`: a word can come back **`not used`**
     with `level: -1` rather than level 2/3, and then the explication is
     simply its replacement (`large` → *"Use 'big'"*) — nothing to pair or
     explicate.
   - If the local table and a live lookup disagree, the live lookup wins —
     `complex-terms.md` is a snapshot, not a live mirror.

4. **Check the corpus for how this has been encoded before.** Query the
   project sqlite for the surrounding verses, the parallel passage, and
   other uses of the same proper nouns:

   ```sql
   SELECT id_tertiary, phase_1_encoding, status FROM Sources
    WHERE id_primary=? AND id_secondary=? ORDER BY CAST(id_tertiary AS INT);
   SELECT id_primary,id_secondary,id_tertiary,phase_1_encoding FROM Sources
    WHERE phase_1_encoding LIKE '%Gozan%';
   ```

   Match established conventions where they validate. **But verify them — a
   neighbouring verse being in the corpus, even at "Final Review in
   Progress", does not mean it passes `/check`.** Parallel passages tend to
   share the same bug: 2 Kings 17:6 carries the identical `take-away ... to
   Assyria` fault as 18:11. When the convention itself is broken, say so and
   fix both rather than propagating it. When it validates, copy it exactly —
   Numbers 18:15 is the working model for the firstborn-redemption verses.

5. **Draft, re-check, iterate to clean.** Test candidate phrasings
   individually before assembling. **Target `status: ok`.** Treat a residual
   `warning` as unfinished work and try to clear it — only the short list at
   the end of this file is genuinely unfixable, and that list has already
   been wrong once. Confirm bracket balance and read the backtranslation —
   it exposes garbled constituent order that the rule checker passes
   silently (2 Kings 18:11's mangled subject surfaced only as `<<The army of
   Assyria of>> the king`). **Also read the backtranslation against the raw
   NIV sentence-by-sentence for content that was added, dropped, or
   substituted — the rule checker has nothing to say about this, so a
   fabricated clause can sail through as `status: ok`/`warning` and survive
   any number of correction passes untouched, since none of those passes
   ever had a reason to look at it.** Genesis 35:2's corpus-recorded
   `suggested` text included a whole extra sentence, *"People/foreigners
   honor/worship those objects/idols!"*, with nothing in the NIV verse
   ("Get rid of the foreign gods you have with you, and purify yourselves
   and change your clothes") behind it — not even the same verse's own
   `ai_assist` attempt on file included it. It had already been through at
   least one correction pass (the `objects/idols` pairing fix in that
   sentence is listed in the corpus's own `changes` log) without being
   removed, because pairing a level-2/3 word correctly and having a
   sentence not belong in the verse at all are orthogonal problems — fixing
   the first never surfaces the second. Deleting the fabricated sentence
   is not optional cleanup; it is the actual content fix, on top of
   whatever syntax work the verse also needs.

   **A fabricated sentence can be a symptom of quote-bracket mechanics
   rather than pure invention — and the fix is not always "restructure to
   wrap the genuine content," sometimes it's "delete the filler outright."**
   A `["..."]`-style quote-begin bracket can wrap only ONE sentence before
   it has to close; anything genuinely part of the same quoted speech after
   that has to continue as separate, unbracketed top-level sentences (still
   understood as part of the quote by convention — wrapping several
   sentences inside one such bracket instead makes the checker parse them
   as a single clause and throws "cannot have multiple verbs in the same
   clause"). Two different corpus passes hit this constraint and "solved"
   it by inventing a sentence with no basis in the NIV, purely to give the
   bracket a single clause to close on. Matthew 8:4's suggested encoding
   opened the quote with a fabricated command, "You(man) (imp) listen to
   me(Jesus) _implicit" — nothing in the NIV text behind it — apparently
   inserted only so the bracket had something to close on before the
   genuine first command ("do not tell anyone...") continued outside it.
   1 Kings 20:18's suggested encoding did the same thing twice, with a
   subtler fabrication: instead of an invented command, it inserted a
   redundant declarative restating each conditional before stating it
   again as the real "if" clause — `Those men might coming to us
   [in-order-to make peace]]. [If those men are coming to us [in-order-to
   make peace]], you(people) (imp) catch/capture those men...` — adding no
   information (and using broken grammar, "might coming") beyond what the
   following "if" sentence already says. **Test whether the genuine first
   sentence — even a complex one, like an `if`-conditional — can itself be
   the single sentence the bracket closes on, before assuming a filler
   sentence is required.** It can: `["[If those men are coming to us(army)
   [in-order-to make peace]], you(people) (imp) catch/capture those
   men.] And you(people) (imp) do not kill those men. Or [if those men are
   coming to us(army) [in-order-to make war]], you(people) (imp)
   catch/capture those men. And you(people) (imp) do not kill those men.`
   validates at `status: warning` (only the expected `Ben-Hadad` residual)
   with the two filler sentences gone entirely and the "might coming" typo
   with them. The constraint the bracket enforces is "exactly one sentence
   inside," not "only a simple sentence inside" — a complex clause works
   fine there too, so reach for that before inventing filler content.

   **This isn't limited to outright fabrication — the same check catches
   unforced paraphrase drift, including a changed speech act.** Genesis
   24:31's suggested encoding turned the NIV's actual question *"Why are
   you standing out here?"* into a flat negative command, `You(servant)
   (imp) do not stand outside` — a real change from asking why to telling
   not to, not just a wording simplification. It also invented a
   destination for `come` (`come into our(Laban) house`, nothing in the
   NIV's `"Come, you who are blessed by the Lord,"` at that point in the
   verse) and loosened `"I have prepared the house and a place for the
   camels"` — a specific, already-completed act, first person singular —
   into `We(Laban) have a room [that you(servant) may stay in]`, generic
   present-tense possession, first person plural, with "that you may stay
   in" added and not in the source. None of this was needed for anything
   to validate: the literal question (`Why are you(servant) standing
   outside _noun?`), bare `You(servant) (imp) come`, and `I(Laban)
   prepared the house _noun and a place [for your(servant)
   animal/camels]` all check `ok` on their own. **When the backtranslation
   reads as a looser paraphrase of the NIV rather than the same sentence
   in Phase 1 words — a question became a command, a person or number
   changed, a detail appears early or not at all — test the literal
   wording before keeping the paraphrase; it usually validates too, and
   when it does it's the correct fix, not just a stylistic option.**

   **A third flavor: content pulled forward from a later verse, or one
   speech act split into two.** Joshua 2:12's suggested encoding split the
   NIV's single oath — *"swear to me by the Lord that you will show
   kindness to my family"* — into two separate `promise` acts, one to
   Rahab and a second one directly to Yahweh, which isn't what the verse
   says (`swear ... by the Lord` invokes the Lord's name as the oath's
   witness/guarantee, it doesn't address a second promise to him). It also
   turned *"Give me a sure sign"* into `You(men) (imp) prove to me(Rahab)
   [that you(men) will protect me(Rahab)]` — dropping the concrete `sign`
   entirely and substituting `protect`, a concept from a later verse (2:13)
   that this verse never mentions. Both were checker-driven workarounds for
   a real cascade (see "Acceptable residual warnings" below for the
   `promise-C` fix) rather than necessary simplifications — once the
   cascade was fixed at its actual source, the literal oath (`swear/promise
   by Yahweh to me(Rahab) [that ...]`) and a literal `give a true sign-B to
   me(Rahab)` both validated. **A paraphrase that reaches for content from
   a different verse, or turns one speech act into two, is a sign the fix
   was applied to work around a symptom rather than the actual cause —
   look for the real fix before accepting the content change.**

   **A fourth flavor: swapping the source's literal name or epithet for a
   different, factually-equivalent one.** 2 Samuel 6:6's suggested encoding
   referred to the object Uzzah reached for as "the ark of the
   agreement/covenant of God" throughout, but the NIV verse itself says "the
   ark of God" — not "the ark of the covenant." Both names refer to the same
   real-world object (this specific ark *was* the Ark of the Covenant), so
   the substitution isn't factually wrong, but it isn't what the verse says
   either, and nothing forced it — restoring the literal "ark of God"
   wording (paired with the ontology's proper-name sense `ark-B`, "another
   name for the ark of the covenant") validated at `status: ok` with zero
   messages, same as the covenant-framed version did. **A real-world-accurate
   rename is still a content change if the source verse used different
   words — check names and epithets against the literal NIV wording the same
   way as clauses.**

   **A fifth flavor: an entire clause can be silently dropped, not just
   paraphrased or expanded — and the corpus's own change log won't catch it,
   because a change log records edits made, not content omitted from the
   start.** 2 Samuel 21:6's suggested encoding opens directly with the
   Gibeonites' request (`(imp) You(David) bring 7 of the male
   sons/descendants of Saul to us(people)...`) with no trace of the NIV's
   preceding clause — *"As for the man who destroyed us and plotted against
   us so that we have been decimated and have no place anywhere in
   Israel,"* the Gibeonites' entire stated grievance against Saul. The
   corpus's own `changes` log for this verse lists five edits
   (capitalization, a `where`-relativizer fix, a `choose`-clause fix, three
   `Saul's` possessives, four `descendants` pairings) and the note flags one
   deliberately-left residual warning — nothing in either place mentions
   this whole clause being missing, because a diff-style change log only
   ever describes edits actually made to what's there; it has no way to
   surface content that was never carried over from the source in the first
   place. The same verse's own `ai_assist` draft on file, by contrast, does
   attempt this content (*"Concerning the man who is Saul who destroyed
   us... and who plotted against us so that Saul destroyed us and so that we
   do not have a place in Israel..."*), confirming it belongs in the verse
   and was dropped by the suggested encoding, not omitted from the NIV
   itself. Restoring it took real construction work, not just re-adding
   words: the paired `plan/plot` verb only validates when `plot`'s complex
   sense is spelled out as its own explication (`Saul plan/plotted [to do
   bad-B things to us(people)]`) — the plain "plotted against us" shape
   errors (`This use of 'plan' does not match any sense`), because the case
   frame the checker enforces on a pairing follows the *simple* word's
   argument structure (`plan`), and none of `plan`'s senses take a bare
   "against Y" argument the way `plot-A` alone would; even explicitly tagging
   the complex side (`plan/plot-A against us`) doesn't help, because it's
   still `plan`'s grid being checked. **A dropped opening clause is a
   different failure mode from every other content-fidelity check in this
   file — it won't show up in a change log, a `suggest` message, or even a
   close read of just the suggested text, because there's nothing there to
   flag; the only way to catch it is reading the backtranslation against the
   full raw NIV sentence, from the very first word, every time — not just
   checking that the wording that IS there matches.**

   **Distinguishing legitimate expansion from drift: the
   `(implicit-situational)` tag and its `<<...>>` backtranslation marker.**
   Not every multi-sentence expansion from a single NIV sentence is drift.
   2 Samuel 6:6's suggestion turns the NIV's one sentence ("...Uzzah reached
   out and took hold of the ark of God, because the oxen stumbled") into
   four, two of them tagged `(implicit-situational)` and spelling out the
   causal chain the NIV leaves implicit (oxen stumble → wagon tips → ark
   starts to fall → Uzzah grabs it to stop it). This is a documented,
   corpus-verified TBTA convention for making implicit causation explicit,
   not fabrication — and the backtranslation itself marks which sentences
   are the implicit ones by wrapping them in `<<...>>`. Before flattening an
   expanded verse back to bare literal wording, check whether the extra
   sentences are `(implicit-situational)`-tagged and `<<...>>`-marked; if so,
   the expansion is doing its job and should be left alone. The
   content-fidelity check in this step is for content that wasn't earned by
   an explicit convention — not for every deviation from a one-clause
   rendering.

   **Not every expansive paraphrase is drift, either — some are the only
   way past a genuine case-frame wall.** Genesis 13:9's suggested encoding
   turns the NIV's idiom *"Let's part company"* plus *"If you go to the
   left, I'll go to the right; if you go to the right, I'll go to the
   left"* into `You(Lot) and I(Abram) should not live in the same place...
   choose the place that you want to live in... [if you go to the western
   place/region] I will go to the eastern place/region` — a real expansion,
   and a literal-to-figurative swap (`left`/`right` → `western`/`eastern`).
   Before assuming this needed to be reined back in the way Genesis 24:31
   did: testing the literal wording directly shows why it can't be.
   `separate` (the closest ontology match for "part company") takes an
   Agent/Patient/Source frame, not a bare reciprocal, and errors on a
   predicate-adjective/reciprocal construction; `go` "can never be used with
   a predicate adjective" (`go to the left` as a literal directional
   predicate), confirmed as a real `checker:built-in:1`-family error, not a
   cascade. `western`/`eastern` also isn't an arbitrary substitution —
   Genesis 13:11 confirms Lot went east, so the direction is drawn from the
   passage itself, not invented. **A paraphrase that looks expansive is only
   drift if a more literal version also validates and wasn't used — test the
   literal wording before objecting to the paraphrase; here it genuinely
   doesn't validate, so the paraphrase is the correct fix, not a content
   problem.**

6. **Present as the table format below.**

## Output format

Lead with the corrected encoding as a blockquote. Then:

```
| Was | Now | Reason |
|---|---|---|
| `the old prophet` | `the old man [who told God's messages to people]` | `prophet` is L2 — rule 0.2 allows level 2/3 words only in a pairing, explication, or complex alternate. Ontology explication; worded to match v11 (rule 0.36) |
```

Rules for the table:

- **Every Reason names the rule** — its number and what it requires, or the
  ontology fact (level, theta grid) that forces the change. "Reads better"
  is not a reason. If a change is stylistic rather than rule-driven, label
  it as such so the user can decline it.
- One row per distinct change, not per error message — six identical
  level-2 errors on the same word are one row.
- Below the table, expand any fix whose reasoning is non-obvious (a cascade,
  a theta-grid mismatch, a decomposition) in a short paragraph each.
- State explicitly which warnings remain and why they are acceptable —
  and if a residual warning is a judgment call rather than a genuinely
  unfixable one (see "Judgment-call residual warnings" below), flag it as
  an open item to revisit, not a closed one.
- **When the fix that validates also narrows the meaning, say so in the row**
  and let the user decide. The distributive rewrite below is the standard
  case: it reaches `status: ok` but loses "each … one".
- Flag anything systemic you noticed — a bug shared with the parallel verse,
  a convention that fails corpus-wide — and offer to sweep for it, rather
  than silently fixing only the verse asked about.

## Cascade sources that are not unrecognized words

All of these present as a **verb** fault — `This use of '<verb>' does
not match any sense in the Ontology`, usually with `'<verb>' cannot be used
with a different-participant patient clause` — while the actual break is
elsewhere in the clause. Fix the structure and the verb errors disappear
untouched. Never start by re-picking a verb sense when any of them is
present.

### `where` as a relativizer (checker:32)

`Cannot use 'where' as a relativizer. Use 'the place [that...]' instead.`
The malformed relative is read as a patient clause on the preceding verb, so
a single `where` yields three or four errors. Rewrite it as `that …
<adposition>`, with the preposition at the end of the clause:

| Was | Now |
|---|---|
| `into the river near the place [where the priests are standing]` | `into the river near the place [that the priests are standing in]` |
| `to the house [where Jesus was teaching people about God]` | `to the house [that Jesus was teaching people about God in]` |

Joshua 4:5 went from four errors to zero on that one change — both `go`
errors were pure cascade. Luke 5:18 lost both its `carry` errors the same
way. Genesis 36:43 lost three `have` errors the same way, going from five
errors to one. The backtranslation is the tell: an unfixed `where` reads as
*"the house **that where** Jesus was teaching"*.

The cascade is not guaranteed, though — it depends on what governs the head
noun. In Luke 12:18 (`my buildings [where I store things]`) the head sits
under `destroy` rather than a have/be verb, and the `where` error stands
alone with nothing behind it. Always confirm by isolation rather than
assuming three free fixes.

### Glued bracket — `Missing a space before [` (token:syntax)

An opening bracket written flush against the preceding word (`person[who
...`) is read as part of that token, so the whole relative clause attaches
wrongly and the verbs around it collapse into false case-frame errors. In
1 Kings 20:13 two glued brackets (`person[who...`, `Ahab[who...`) generated
five spurious `checker:built-in:1` errors on `come` and `tell`; restoring
the two spaces cleared all seven messages at once.

The backtranslation is again the tell — `the person[ that who was the
leader` — and the token in the error message carries the bracket with it
(`'person['`). **Fix every glued bracket before re-picking any verb sense**;
it is a pure typo and never needs a semantic decision.

### Distributive `each … one <noun>`

`Each of you(man) should carry one stone on your(man's) shoulder` leaves the
checker unable to resolve the part of speech of both `one` and `stone`, and
that cascades into `This use of 'carry' does not match any sense`. Adding
the sense (`stone-A`) clears the complexity warning but not the part-of-
speech one, and no rewording of the subject (`Each man`, `Each man of
you(men)`) helps either. A plural rewrite validates clean:
`You(men) should carry the stones-A on your(men's) shoulders.` Offer it
flagged as meaning-narrowing — the distributive force is lost.

### Unrecognized clause-alternate notation — `(alt)` (token:syntax)

`This clause notation is not recognized.` Only two alternate-sentence tag
pairs exist: `(literal) ... (dynamic) ...` and `(complex) ... (simple) ...`
(rule 0.2's complex alternate). `(alt)` is neither, and its failure cascades
hard on both sides. 1 Kings 10:12's encoding paired `The king also made
harps and lyres...` with `The king also made instruments [that had
strings]...` under `(alt)`, meaning the first sentence as the complex
reading and the second as its explication — but since `(alt)` doesn't
register as a real clause tag, the checker never saw `harps`/`lyres` as
"within a (complex) alternate," so it flagged both under checker:built-in:4
exactly as if used bare. Retagging as `(complex) ... (simple) ...` cleared
both word-level errors with no other change.

The same run also carried two `checker:5` "multiple verbs" errors — `have
brought`, `have not seen` — elsewhere in the same verse. Both were pure
cascade from the `(alt)` fault and nearby glued brackets, not a real problem
with perfect tense: isolated, `People have brought gold to Judah.` and
`John has gone.` (rule 0.15's own example) both check clean. Don't rewrite a
`have + past-participle` clause to simple past on sight — clear the other
errors in the sentence first and re-check whether it was ever broken.

### `let` without a bracket around its embedded action

`let those sick people touch the edge of Jesus's clothes/robe` (no brackets)
gets read as two main-clause verbs, not as `let` governing a patient clause.
The checker reports it as a `let` problem — `Incorrect usage of let-A` and
`Unexpected patient for let-A` — plus `Cannot have multiple verbs in the same
clause (let and touch)`, all three pointing at word choice when the actual
fault is a missing bracket. Wrap the embedded action:
`let [those sick people touch the edge of Jesus's clothes/robe]`. Confirmed
on Matthew 14:36 (2026-09-10 calibration run): bracketing the clause alone
cleared all three messages, taking that verse from 4 errors to 0 with no
change to `let` itself. Check for this before re-picking a verb sense any
time `let`, `make`, `have`, or another causative-type verb is followed
directly by an unbracketed clause.

## Recurring failure patterns

Confirmed against the API. Check for these first — they account for most
errors in practice.

### `all` before a non-generic Noun (checker:35, P1 Checklist 0.17)

`Use 'all of', unless the modified Noun is generic.` A top-10 error rule in
every calibration sample so far (12–14 errors per 200 verses) and the most
mechanical fix in the corpus — run it first, before any judgement calls.

Substitute `all of` before any **determined or possessed** noun:

| Was | Now |
|---|---|
| `all the women` | `all of the women` |
| `all these buildings` | `all of these buildings` |
| `all my(person's) tools` | `all of my(person's) tools` |

**The exception is real and worth knowing**: generic and mass nouns do not
fire the rule, so both forms can be correct in the same verse. In Luke 12:18
`all my(person's) grain` is right as written while `all the things` in the
next clause is not — `grain` is a mass noun, `things` is determined.
Verified directly against the API: `all his(man's) grain` returns no
checker:35 message, `all the tools` returns one. Do not sweep blindly;
check the noun.

### Level-2/3 word used bare (rule 0.2)

By far the most common error in the corpus — **85 of 241 errors** in the
200-verse sample of 2026-09-09, and the same rank in every sample since.
Replace with the ontology's pairing or explication.

The repeat offenders, with the fix each takes:

| Word | Fix | Corpus rows |
|---|---|---|
| `prophet` | `man [who tells God's messages to people]` | — |
| `donkey` | `animal/donkey` (or `horse/donkey`) | 110 |
| `lamb` | `young sheep` | 27 |
| `firstborn X` | `X [who//that was born first _adv]` | 21 |
| `angel` | `servant/messenger [who comes from God]` | — |
| `region` | `area/region` or `place/region` | — |
| `kingdom` | `country/kingdom`, `land/kingdom`, `area/kingdom` | — |
| `holy` | `special/holy`, `good-B/holy`, `perfect/holy`, `pure/holy` (`pure` only for substances) | — |
| `bull` | `male cow`, or pair with `cow` | — |
| `ox` | `cow/ox` — the hint says prefer the pairing to the explication | — |
| `mat` | `bed/mat` | — |
| `righteous` | `good-B/righteous` | — |
| `neighbor` | `person [who lives near X]` — no pairing exists | — |
| `paralyzed X` | `X [that is not able [to move X's legs]]` | — |
| `statue` | `model/statue`, or `object [that has the shape of X]` | — |
| `disciple` | `man [who follows-B _routinely Jesus]` | — |
| `teacher` | `master/teacher`, or `person [who teaches-A things _generic to people _generic]` | — |
| `redeem` | `buy/redeem` (also `save`, `protect`, `defend`) | — |
| `ancestor` | `father/ancestor`, `person/ancestor` or `parent/ancestor` | — |
| `descendant` | `person/descendant`, `son/descendant` or `child/descendant` — but use `Son-of-David` for that case | — |
| `vision` | `dream/vision` or `picture/vision`; some cases need a full rewrite instead | — |
| `apostle` (L3) | explicate as `man [that Jesus sent to people _genericOptional [so that that man would be Jesus's representative]]`, then pair with `representative` or `leader` | — |
| `scripture` | `God's book` (singular; a theta grid rule handles the plural) | — |
| `chariot` | `vehicle/wagon of war` (note the order — adjusted from `war vehicle/wagon` for the P2) | — |
| `sacrifice` (Noun) | `animal/sacrifice`, `gift/sacrifice`, or explicate as `animal [that a person gives to God//Yahweh [so that the priest would kill that animal]]` | — |
| `arrest` | `take-away/arrest` — see the inflection note below | — |

Always confirm against `/simplification_hints` rather than trusting this
table alone — several of these have structure-specific variants (`prophet of
X` differs from bare `prophet`; `paralyzed X` differs from `X is
paralyzed`). `../niv-to-phase1/references/complex-terms.md` has the full
per-structure breakdown for every term above (e.g. `prophet-A` alone carries
five separate entries — bare, `prophet of X`, `be-Prophet`, `False prophet`,
`be a false prophet` — each with its own pairing/explication) and is the
faster way to check which variant applies before falling back to a live
`/simplification_hints` call.

**Do not paste an ontology explication in verbatim — check it on its own
first.** Several explications fail the verb case frame inside the clause
they create. `astrologer` returns `person [who searches signs-B [that are in
the sky-B]]`, but bare `search` there raises `Incorrect usage of search-A`
(`built-in:1`); `searches for signs-B` validates clean. Run every fresh
explication through `/check` as a standalone sentence before dropping it
into the verse, and treat a case-frame error inside a brand-new explication
as a bug in the explication, not in the verse you are reviewing.

Three mechanics that trip people up:

- **Pairing order is `simple/complex`.** `animal/donkey` validates;
  `donkey/animal` still errors. The level-0/1 word goes first.
- **A hyphenated particle verb on the simple side stays UNINFLECTED.**
  `arrest` pairs with `take-away`, and the tense goes on the complex side
  only: `take-away/arrested` validates at `ok` and still backtranslates as
  *"arrested"*, while `took-away/arrested` comes back as two
  `checker:built-in:7` "not recognized" warnings. checker:23 states the rule
  (*DO NOT inflect the Verb, e.g. NOT took-away*) but only fires on the
  unhyphenated form, so inside a pairing the fault is silent — it surfaces
  as an unrecognized word, which then cascades into the surrounding clause.
  Both forms verified against the API.
- **The rule applies inside pronoun-referent parens too.** `I(prophet)`
  errors exactly as bare `prophet` does. Pick a referent token that is
  itself level 0/1 and that distinguishes the participants — e.g. `person`
  for one man and `man` for another in the same dialogue.
- **And it applies to a standalone hyphenated particle verb, not just one
  side of a pairing.** Luke 15:28's prior pass wrote `came-out`, which isn't
  an ontology entry — only the base stem `come-out` is (verified against
  `/search`: sense A, "to come out from some place"). Swapping to
  `come-out` alone reached `status: ok`, but the backtranslation then read
  *"the father come out of the house"* — present tense, wrong. Appending
  `_past` (`come-out _past`, matching the tense-tag convention already used
  on 2 Kings 18:11's `take-away _past`) still checks `ok` with zero
  messages and is the right encoding, but **the backtranslator does not
  render `_past` on this verb** — it still prints "come out," not "came
  out." That's a backtranslator display gap, not a fault in the encoding;
  don't re-encode around it, and don't be misled into thinking the tag
  didn't take effect.

When one L2 word repeats across a verse — `neighbor's` fires six times in
Exodus 20:17 — the explication has to be written out in full at every
occurrence. That is one table row, and the verbosity is by design; do not
collapse it back to the bare word.

### Adjective that is `not used` rather than level 2/3

`The Adjective 'large' is not in the Ontology` is a different failure from
the level rule. `/simplification_hints` returns `ontology_status: not used`,
`level: -1`, and an explication that is just the replacement word (*"Use
'big'"*). Swap the word — there is nothing to pair or explicate.

### Ambiguous part of speech — tag it, don't dismiss it

When the checker says *"The editor cannot determine which part of speech
this word is"* or suggests adding `_noun` / `_verb` / `_adj` / `_adv` /
`_adp` / `_conj`, **take the suggestion.** It is a real fix, not noise.
`[that was born first]` warns on `first`; `[that was born first _adv]`
validates clean, taking Exodus 13:13 to `status: ok`. Try the tag on any
such warning — including `named` in the rule 0.23 construction — before
concluding it is unavoidable. The one known exception is the distributive
above, where no tag helps and the clause has to be restructured.

Note the spacing: the tag is a separate token preceded by a space
(`first _adv`). Attaching it directly to the word (`man-of-God_noun`)
raises `Notes notation should have a space before the underscore`.

**If the first tag you try turns the warning into an error, try the other
listed sense before giving up on tagging.** A word with more than one
lookup entry can have more than one plausible tag, and they are not
interchangeable — one sense's case frame can be strict about what sits next
to it while another sense has no such constraint. On 1 Kings 10:12,
`more-than` has two ontology senses: Adposition (case frame requires a
subordinate-clause bracket *immediately* after it) and Adjective (no such
requirement). Tagging the semantically obvious one, `more-than _adp`, broke
the bracket adjacency and turned the warning into a real
`checker:built-in:2` error (`Incorrect usage of more-than-A`,
`missing opening '[' bracket`). Tagging the *other* sense, `more-than _adj`,
cleared it to zero messages — same construction, same intended meaning,
different sense selected. There was no genuinely unfixable case here; the
first attempt just picked the wrong of two available tags. Check every
listed sense for the word (the `lookup_results` array in the raw `/check`
response) before concluding a POS warning can't be tagged away.

**The missed sense can also be one whose part of speech looks wrong for
the role the word is playing.** Genesis 24:31's `stand outside` carried an
ambiguous-part-of-speech warning on `outside`, and a prior pass's note said
both suggested tags were tried and rejected — `_adv` still left it
unrecognized, `_adp` introduced a new case-frame error — and left it
untagged as "a genuine residual." `/search` shows why both failed: `outside`
has no Adverb sense at all, and its Adposition sense is `always used in
Adjunct Phrases`, meaning it wants an explicit object (`outside the house`),
which a bare `stand outside` doesn't supply. But `/search` also lists a
third sense the prior pass never tried: `outside`, Noun, *"the outside of
something like a cup."* `stand outside _noun` clears the warning completely
— `status: ok`, zero messages — because `_noun` fits how the word is
actually functioning here (a bare locative, not the head of an Adjunct
Phrase with its own complement) even though "outside" doesn't read like a
noun. **Don't stop at the tag whose part of speech matches the word's
semantic role — pull the full `/search` sense list and try every one,
including a part of speech that looks like an odd fit.**

**An untagged ambiguous word can cascade into a case-frame error on a verb
that doesn't even touch it.** The cascade isn't limited to the word directly
governing the ambiguous one — it can break parsing further out in the same
clause. Real corpus example: Luke 9:13-14's `We(representatives) have only
5 loaves of bread and 2 fish` errored on `have` — `This use of 'have' does
not match any sense in the Ontology`, with every sense's `info` message
reading `have-X: missing state` even though the object (`5 loaves of bread
and 2 fish`) is right there in the sentence. A prior review pass concluded
this was "a genuine case-frame/lexical gap... left as-is," matching the same
wrong-diagnosis pattern as Judges 12:1's `prepare` error. The real cause:
`only` (untagged, ambiguous part of speech) was preventing the checker from
attaching the coordinated noun phrase after it as `have`'s required `state`
argument at all — tagging `only _adv` cleared `have`'s error completely with
no other change, taking the sentence from `status: error` to `status: ok`.
**Before accepting a verb's case-frame error as genuine, check the rest of
the clause for an untagged ambiguous-POS word — even one that isn't
adjacent to the failing verb — and try tagging it first.**

**The cascade can span an entire multi-sentence verse, not just one clause,
when the same untagged word repeats.** 1 Corinthians 13:4's `(literal)`
paraphrase sentences — `Love is patient`, `Love is kind`, `Love does not
want the things [that other people have]`, `Love does not proudly speak`,
`Love is not proud/arrogant` — had every `is`, `want`, and `speak` erroring
(`This use of '<verb>' does not match any sense in the Ontology`, `missing
agent` on every sense). A prior review pass diagnosed `want` and `speak` as
a genuine "structural limit" — its claim was that an abstract noun like
`Love` cannot fill a verb's Agent role in the ontology, "not fixable by
rewording" — and left `Love`'s ambiguous-part-of-speech warning as an
unrelated residual. Both halves of that diagnosis were wrong: tagging
`Love _noun` at all five occurrences (nothing else changed) took the whole
verse from `status: error` with errors on four different verbs to
`status: ok` with **zero** messages. There was no structural limit — an
abstract-noun subject fills the Agent role fine once the checker knows what
part of speech the subject is. **A claim that a construction is a
"structural limit" of the ontology is exactly the kind of claim to verify
by testing the ambiguous-POS tag first** — it has now disproved that
diagnosis twice (see the `have`/`only` case above) at two different scales:
once within a clause, once across a whole verse of repeated occurrences.

**An unrecognized proper noun sitting right before a `be` verb breaks that
verb's case frame too — tag it `_noun` even though it stays unrecognized.**
This is the same cascade shape as the two cases above, but the trigger is an
unrecognized-word warning rather than an ambiguous-POS one, and the tag does
not clear the residual warning — it only clears the cascade. Real corpus
example: 2 Kings 18:11's `A river named Habor is beside that town named
Gozan.` The prior pass recorded this whole verse as
`suggested_status: "warning"`, but re-checking the literal suggested text
showed the true status was `error` — `is` failed every sense (`be-A` through
`be-Y`, all "missing agent") because `Habor`, an unrecognized Bible proper
noun, sat inside the subject NP right before `is` with no POS tag. Isolating
confirmed it: `A river named Habor is beside a town.` errors on `is`; `A
river named John is beside a town.` (a recognized name in the same slot) is
clean; `A river named Habor _noun is beside a town.` is clean except for the
expected `'Habor' is not recognized` warning. Tagging only `Habor _noun` —
leaving `Halah` and the two other `Gozan` occurrences elsewhere in the verse
untagged, since they don't sit before a `be` verb and were never part of
this cascade — took the full verse from `error` back down to `warning` with
exactly the four genuine "not recognized" residuals (Halah, Gozan ×2,
Habor), the acceptable-residual class this skill already documents. **A
verse a prior pass logged as `warning` is not guaranteed to still check as
`warning` — re-run `/check` on the literal suggested text before trusting a
recorded status, the same way a prior pass's "unfixable" note needs
re-verification.**

**A prior pass can fix this cascade in one clause and leave it untouched in
another clause of the same verse, for the same recurring word.** Real corpus
example: 1 Kings 20:4's suggested encoding uses the unrecognized name
`Ben-Hadad` four times — twice as a bare referent (`you(Ben-Hadad) say`,
`You(Ben-Hadad) are the king`) and twice already wrapped in the rule-0.23
`named` construction (`you(king) [who is named Ben-Hadad]`). The prior
pass's note described fixing exactly one cascade — a `belong`/`belongs`
theta-grid gap on the two `named`-construction occurrences — and called the
verse's status settled at `warning` with only the expected "Ben-Hadad not
recognized" residual left. It missed that the other two, untouched
occurrences carry the identical cascade on different verbs: re-checking the
literal suggested text showed `status: error`, with `You(Ben-Hadad) are the
king...` breaking `are` exactly like 2 Kings 18:11's `Habor` breaks `is` —
confirmed in isolation (`You(Ben-Hadad) are the king` errors on `are`;
`You(David) are the king` in the same slot is clean). The fix followed the
same shape as the rest of this section — swap the bare referent for a
recognized token (`you(king)`) and establish the name once via the `named`
construction rather than repeating it — but the lesson is about coverage,
not mechanics: **when an unrecognized or ambiguous word recurs across a
verse, check every occurrence for the cascade, not just the one where a
prior pass already found and fixed it.** A verse can be "half-fixed" and
still validate a residual-warning claim on a spot check, the same way it can
be mis-recorded as `warning` when it's really `error` (see the `Habor` note
above) — re-run `/check` on the whole verse, not just the clause the prior
pass's note talks about.

**When a verse genuinely uses the same word as two different parts of
speech at two different occurrences, tag each occurrence separately —
"the verse legitimately mixes both senses, so it can't be disambiguated" is
not a valid reason to leave the warning as residual.** The tag attaches per
token, not per word, so nothing stops each occurrence getting its own tag.
Genesis 35:2's suggested encoding used `clean` twice — once as a verb
(`clean yourselves`) and once as an adjective (`clean clothes`) — and a
prior pass's note read *"no encoding change available to disambiguate it
further,"* leaving the ambiguous-part-of-speech warning as the verse's one
residual. That diagnosis was wrong: tagging `clean _verb yourselves` at the
first occurrence and `clean _adj clothes` at the second, with nothing else
changed, took the verse from `status: warning` to `status: ok` with zero
error/warning messages. Don't accept "the verse uses it both ways nearby"
as a reason a POS warning can't be tagged away — tag both occurrences by
their own actual part of speech and re-check.

**A partitive `one of the X` warning on `one` is not a lexical dead end —
the fix is to stop spelling the number as a word at all, and to bracket the
whole partitive-plus-complement as one clause.** Judges 17:5's `Micah chose
one of the sons of Micah [to be the priest of Micah]` carries an
ambiguous-part-of-speech warning on `one`. A first pass at this (this
skill's own, in an earlier draft of this entry) tried every ontology sense
of the word `one` (`one _adj`, `one-B`, `one-B _adj`) and every rewording
that dropped the partitive (`chose a son of Micah`, `chose one son of
Micah`) — all either left the warning standing or broke `choose`'s case
frame outright — and concluded, wrongly, that this was a genuine unfixable
bind and shipped it as an "acceptable residual warning." It wasn't
exhaustive: it never tried the fix that actually works, which touches two
things at once and doesn't work with either alone. First, spell the number
as the digit `1`, not the word `one` — `one` only exists in the ontology as
an Adjective, "always used attributively," which is why no tag ever fit
its partitive use here; `1` sidesteps the ontology lookup for the word
entirely. Second, bracket the *entire* partitive-plus-complement as
`choose`'s patient clause: `Micah chose [1 of the sons of Micah to be the
priest of Micah]`, not `Micah chose 1 of the sons of Micah [to be the
priest of Micah]` with the destination clause bracketed separately. Neither
change alone clears it — digit alone with the old bracket placement still
errors on `choose` (`This use of 'choose' does not match any sense`);
word `one` with the full bracket restructure still carries the original
part-of-speech warning. Only the combination reaches `status: ok` with
**zero** messages (confirmed against the API; `chose-B` and `sons-A` tags
are unnecessary and only draw harmless `suggest`-level "consider removing
the sense" noise, per the same-named quirk already documented under
"Ambiguous complexity" below). **Before writing off a partitive `one of the
X` warning as a lexical dead end, try the digit substitution together with
re-bracketing the whole complement as a unit — testing every tag on the
word itself, and every reworded object, is not the same as testing every
available fix, and "I checked every sense of this word" can still miss the
fix that doesn't touch the word's sense at all.**

### Ambiguous complexity — also tag it, don't dismiss it (checker:built-in:6)

A different warning from the part-of-speech one above: *"This word has
multiple senses and ambiguous complexity. Consider including the sense
(e.g. heal-A)."* This fires when a word has more than one ontology entry at
different complexity levels and the checker can't pick one on its own.

This is genuinely fixable, not an ontology gap, and there are two ways to
fix it — **prefer full explication over a bare sense tag when the ontology
offers one**, since it clears the word entirely rather than picking one of
its senses:

- **Bare sense tag** (`Lot-A`, `heal-A`) — the quick fix, and the only
  option when no explication exists (Genesis 13:10's `Lot`: reviewed twice,
  the first pass left the warning as an unconfirmed residual at
  `status: warning`, the second pass tagged `Lot-A` and reached
  `status: ok`). One quirk: the checker can follow a tag with a
  `suggest`-level *"Consider removing the sense, as it would be selected by
  default"* — don't trust it. Tagging `temple-A` on 1 Kings 10:12 first
  cleared the warning, but removing the tag on the strength of that
  `suggest` message brought the warning straight back on a re-check. The
  default-selection message describes what the checker picks when forced to
  guess, not what it reliably picks; verify by testing the untagged form
  yourself.
- **Full explication**, when the ontology's own `how_to_entries.explication`
  gives one — replaces the ambiguous word outright, so there's no sense
  left to be ambiguous about and no `suggest` noise either. 1 Kings 10:12's
  `temple` (sense A explication: *"building {of Jerusalem}_optional [that
  Jews//Israelites//people//Jesus honor//worship God//Yahweh in]"*)
  simplified to `the building [that people honor/worship Yahweh in]` and
  checked at `status: ok` with zero messages — cleaner than the `temple-A`
  tag, which still needed the tag kept against the misleading `suggest`.
  Prefer this when a usable explication exists; fall back to the sense tag
  only when it doesn't.

Try the fix — and confirm it in isolation — before writing off a complexity
warning as unavoidable.

**A prior pass's specific technical claim — "this sense tag was tried and
came back not found in any part-of-speech" — is exactly the kind of claim
worth re-testing, not just the vaguer "unfixable" framing.** 2 Samuel 6:6's
corpus note claimed both `ark-A` and `ark-B` had been tried and neither was
found in any part-of-speech; re-running both directly against `/check`
showed both validate cleanly (`status: ok`, zero messages) and produce an
identical backtranslation. When more than one sense clears the warning, pick
by meaning, not by whichever the checker happens to prefer: `ark-A`'s gloss
is Noah's boat (wrong here), `ark-B`'s is "another name for the ark of the
covenant" (right) — use `ark-B`.

**A compound technical claim — "every sense failed, and tagging even broke
something else" — needs both halves re-tested, not just the headline
conclusion.** Judges 6:33's corpus note said every ontology sense of `sign`
(`sign-A/B/C`) came back "No sense X found" when tried, and that tagging it
even broke an unrelated case-frame check on `for`, concluding this was a gap
between the ontology's public sense list and the checker's own word data
rather than a fixable fault. Both claims were false: `/search` confirms all
three senses exist, and running each one directly against `/check` (`sign-A`,
`sign-B`, `sign-C`) returned `status: ok` with **zero** messages every time —
no "not found" error, and nothing broken on `for` either. (`sign-A` also
draws the familiar `suggest`-level "consider removing the sense" noise, which
by itself is not a reason to distrust the tag — see the `suggest`-message
quirk under "Ambiguous complexity" above.) Picking by meaning rather than
whichever cleared first: this occurrence is a section title anticipating the
fleece episode (Judges 6:36-40), a supernatural proof/token — `sign-B`,
*"a thing or an event that has a specific meaning,"* fits; `sign-A` (a mark
made by a king's ring) and `sign-C` (a piece of wood with a message on it, a
signpost) don't. **A prior pass's claim about what happened when a fix was
tried can itself be simply wrong, not just its conclusion — re-run the exact
sense tags it says it tried before accepting either half of a "tried X, it
failed, and it even broke Y" report.**

**A claimed "known upstream regression" is still just a claim — check
whether this skill's own notes already contradict it before accepting it.**
Genesis 13:9's corpus note asserted that tagging `Lot-A` had been tried and
made things worse because "the API currently rejects essentially all
explicit sense-letter tags as 'not recognized' — a known upstream
regression." That's a much bigger claim than usual (not just this word, but
sense tags in general), and this skill's own record for the very same name
one verse over — Genesis 13:10's `Lot-A`, in the table above — already
disproves it: that tag validates fine. Re-running `Lot-A` at all six
occurrences in 13:9 confirmed it: `status: ok`, nothing but the usual
`suggest`-level "consider removing the sense" noise (already known to be
safe to ignore, and confirmed again here — removing the tag brings the
warning straight back). **The bigger and more sweeping a prior pass's
"known regression" or "known limitation" claim reads, the more it's worth
checking against a fix this skill has already confirmed works elsewhere —
a real regression wouldn't have worked one verse over.**

Tracing this one down further changes the lesson slightly: the regression
was real, but time-boxed, and later passes kept citing it past its expiry.
A corpus-wide `systemic_note` timestamped 2026-09-12T08:03 documents it
directly — "9 of 9 spot-checked tags failed identically" that run, a
genuine service-side outage on sense-letter tags specifically. (A separate
"possessive 's not recognized" note some corpus records cite is a different
claim, and per-name, not corpus-wide — see "Possessive 's" below; don't
conflate the two.) Genesis 13:9 (from a 09:55 run) and Daniel 2:12 (from a
10:54 run) both cite it and both leave their own ambiguous-complexity
warning bare as a result — but by the time those runs happened, the
regression had evidently already been fixed service-side: `Lot-A` and
`sign-A`/`signs-A` both validate cleanly today, and there's no reason to
think they didn't validate cleanly an hour or two after 08:03 either. **A
systemic note about the checker's own behavior has a shelf life, because
the checker is a remote service that can change under you mid-corpus — cite
it for what happened at that timestamp, but re-test before relying on it in
a run from an hour later, the same way a per-verse "unfixable" claim needs
re-testing.** Daniel 2:12 also shows the other side of this: the underlying
warning doesn't need the tag at all here — the suggested encoding had
decomposed the NIV's plain "wise men" into "the people that watch signs in
the sky and the men that use magic" (content pulled from Daniel 2:2's fuller
list of court specialists, not this verse — the third flavor above), and
`wise men` on its own, in the ontology at level 1 for both `wise` and `man`,
validates at `status: ok` with **zero** messages, sidestepping the `signs`
warning entirely rather than tagging around it.

Judges 17:5 makes it three for three: its corpus note cited the same
regression to justify leaving `temple`'s ambiguous-complexity warning bare.
`temple-C` — "a place of worship for a false god," the semantically correct
sense for Micah's household idol-shrine, as opposed to `temple-A`'s
Jerusalem temple — tagged clean on the first try, taking the verse from two
warnings down to one (a separate `one`-of-the-sons partitive warning,
covered under "Ambiguous part of speech" above — it turned out fixable too,
not residual). At this point treat any "known regression on sense tags"
claim as presumptively stale by default and re-test before citing it
yourself, rather than treating each new instance as a fresh question.

**A "sense-letter tag regression" claim doesn't mean a part-of-speech tag is
broken too — they're different notations, and a corpus note can conflate
them.** 1 Kings 20:37's `please` carried an ambiguous-*part-of-speech*
warning (`checker:built-in:8`, ordinary `_noun`/`_verb`/`_adj`/`_part`
territory — see "Ambiguous part of speech" above), not an
ambiguous-*complexity* one. The corpus note tried `please-A` (a sense-letter
tag) got the same warning back, and filed it as another instance of the
sense-tag regression, left unfixed. But `please-A` was never going to help:
the warning was about part of speech, and a sense letter doesn't disambiguate
that. The actual fix is the POS tag the warning suggests: `please _part`
reaches `status: ok` with zero messages, confirmed directly against the API.
**When a warning says "cannot determine which part of speech," the fix is a
POS tag (`_noun`/`_verb`/`_adj`/`_adv`/`_adp`/`_conj`/`_part`), never a sense
letter — don't let a "sense tags are regressed" note stop you from trying
the POS tag the warning itself suggests.**

2 Samuel 21:6 confirms the underlying "sense tags are regressed" claim wrong
yet again, and shows a specific way it can arise honestly: only one sense out
of several was ever actually tried. Its corpus note left `hang`'s
ambiguous-complexity warning bare, citing the same corpus-wide sense-tag
regression cited elsewhere in this run. `hang` has three ontology senses —
`hang-A` (intransitive, "something hangs on something," Agent-like +
optional Source only), `hang-B` (complex, "to kill someone by hanging
them"), `hang-C` ("to hang something somewhere," Agent-like + Patient-like +
optional Destination). `hang-A` genuinely does error when tried on this
verse's transitive use (`hang the bodies... on poles`) — `Incorrect usage of
hang-A`, `Unexpected patient for hang-A` — because its grid has no Patient
slot at all, not because sense tags are broken. But `hang-B` and `hang-C`
both validate at `status: ok` with zero messages the moment they're tried,
confirming sense-letter tags are working fine here too. Picking by meaning:
`hang-B` ("kill by hanging") is wrong for this verse — the men were already
ordered killed in the previous sentence, and this clause is about displaying
the corpses on poles afterward, not the method of execution; `hang-C`
("to hang something somewhere") matches exactly. **A "sense tags don't work"
claim can come from having tried only the one sense that happens to be
semantically closest but grammatically wrong for the sentence — pull the
full sense list and try each one, the same as for an ambiguous-POS warning,
before concluding the tag mechanism itself is broken.**

### Spelled-out numbers (checker:built-in:7)

`'two' is not recognized. Consult the How-To document or consider using a
different word.` Number words are not ontology entries; only the digit form
validates. `two` → `2`, `three` → `3`, `forty` → `40`. Confirmed across
multiple corpus verses (Genesis 13:10, Joshua 24:12, Ezra 8:32) and flagged
as corpus-wide in more than one run's systemic note. Pure mechanical
substitution, no judgment call — and it was the other fixable warning left
as "residual" in Genesis 13:10's first review pass.

**`one` follows the same rule as every other number word — always render it
as the digit `1`.** Confirmed by the user (2026-09-21): this isn't a
case-by-case judgment call the way some other fixes in this file are: `one`
is a number, and every number in this file's convention is spelled as a
digit, full stop. Do this on sight, the same way `two` → `2` is done on
sight, rather than waiting for a warning to justify it. This is also the
mechanism behind the partitive fix documented under "Ambiguous part of
speech" above (Judges 17:5's `one of the sons` → `1 of the sons`) — that
entry frames it as clearing an ambiguous-part-of-speech warning because
that's the symptom that showed up, but the underlying rule is simpler and
more general than "try the digit when `one` warns": `one` is always `1`,
warning or not.

### Footnote vs. parenthetical comment — different notations

Both surface as something-in-parentheses in the English output, but they
are two different tags, and neither is a bare literal `(...)` or an
invented dash-prefixed token (`-Footnote`, `-CommentBegin`) — both of those
fail as unrecognized syntax (`token:syntax`, missing open/close
parenthesis).

- Content that is **literally in parentheses in the NIV wording itself**
  (e.g. Genesis 13:10's *"(This was before the LORD destroyed Sodom and
  Gomorrah.)"*) is a **parenthetical comment**: `(comment-begin) ...
  (comment-end)` (`(begin-comment)` / `(end-comment)` also accepted).
- A **translator-added note that is not part of the literal verse text** (a
  unit-conversion aside, a textual-variant flag) is a **footnote**:
  `(footnote)` alone, no closing tag — everything after it is part of the
  footnote until the verse ends or a new `(footnote)` starts, and it can
  only sit at the end of a verse.

Genesis 13:10 was mis-tagged as a footnote in both review passes
(`-Footnote`, then `(footnote)`) when the content is actually the NIV's own
parenthetical aside and should be `(comment-begin) ... (comment-end)`. Both
wrong attempts still passed `/check` — the checker validates syntax, not
which of the two tags is linguistically correct — so this one has to be
caught by reading the source text, not by the checker result.

### Missing comma before an opening quote (checker:20)

`Expect a , before a quote_begin clause.` A quoted speech clause must be
preceded by a comma: `that person said, ["I(person) will ...]`. Cheap and
mechanical, and it travels with the capitalization rule (`built-in:0`) at
the start of the quoted material.

### Title-case common noun mid-sentence — reads as unrecognized proper noun

A capitalized common noun that is really a title, not a proper name (`King`
in `the King of the Jews`), gets looked up as if it were an unrecognized
proper noun rather than matched to its lowercase ontology entry — even
though the lowercase form is very much in the ontology (`king`, Noun sense
A). Real corpus example: Luke 23:37's `the King of the Jews` carried a
residual warning a prior pass diagnosed as *"'King' is not a recognized
ontology entry in this form... a lexicon gap... left alone."* That was
wrong: lowercasing to `the king of the Jews` reached `status: ok` with zero
messages, backtranslation unchanged in meaning. Before accepting a
capitalized common noun's "not recognized" warning as a lexicon gap, try
lowercasing it — NIV capitalizes titles (`King`, `Messiah`-as-title, etc.)
that the ontology only holds as lowercase common nouns, distinct from a
genuine proper noun that is unrecognized in every case (Halah, Gozan,
Habor — see "Acceptable residual warnings" below).

### Possessive 's — warns only if the base word is out of the ontology, not because of the 's itself

A corpus note can claim a possessive-form warning (*"X's is not recognized"*)
is a systemic, corpus-wide gap affecting every possessive noun — but the
possessive marking itself isn't what triggers it. A word that **is** in the
ontology takes 's cleanly, no warning at all: `Laban's sheep are black.`,
`David's son is here.`, `Paul's letter arrived.`, `Micah's sons are here.`,
`girl's` (below) — all `status: ok`, zero messages. Only a word that is
**not** in the ontology at all shows the warning on its possessive form:
`Naboth's vineyard...` and `Ben-Hadad's army...` both still warn — but for
the same reason bare `Naboth` and bare `Ben-Hadad` do everywhere else in
this corpus, because the base word has no ontology entry (the
acceptable-residual class documented above), not because it's wearing an
's. This isn't limited to proper names — see the Mark 5:40 case below,
where the same pattern holds for a common noun.

Real corpus example: Genesis 30:32's suggested encoding used
`your(Laban's) sheep` inside a pronoun-referent parenthetical, and the
corpus note claimed this produces 3 residual "Laban's not recognized"
warnings, calling it an unfixable systemic gap and citing an identical
pattern on Naboth's/Hezekiah's/David's/Paul's. Re-running the literal
suggested text returned `status: ok` with **zero** messages — the claim was
simply wrong for this verse. `Laban`, `Hezekiah`, `David`, and `Paul` are all
in the ontology; only `Naboth` genuinely isn't (matching the gap this skill
already documents). **Before accepting a "possessive form not recognized,
corpus-wide gap" claim, check whether the underlying name is in the ontology
at all (`/search`) — if it is, the possessive almost certainly validates
fine and the claim doesn't apply to this name.** This is the same
"recorded status needs re-verification" lesson as the Habor/Ben-Hadad cases
above, but running the other direction: those were recorded `warning` and
turned out to really be `error`; this one was recorded `warning` and turned
out to really be `ok`. A prior pass's status, in either direction, is a
claim to verify, not a fact to inherit.

Ezra 9:7 confirms it a second time, with a wider cast: the corpus note
claimed 7 residual "not recognized" warnings on possessives — `Ezra's` (×5)
and `Israelites'` (×2, a demonym/collective possessive, not an individual's
name) — as part of the same systemic gap. Re-running the literal suggested
text returned exactly one residual warning, and it had nothing to do with
possessives (an ambiguous-part-of-speech warning on `today`, cleared with
the standard `_adv` tag — see "Ambiguous part of speech" above). Both
`Ezra` and `Israelites` are in the ontology, so both possessive forms
validate cleanly, same as Laban/Hezekiah/David/Paul.

Mark 5:40 confirms it a third time, and extends it past proper names
entirely: the corpus note claimed `the girl's` (×2, `girl` a common noun,
not a person's name) carries "the same possessive-'s gap," describing it
as unfixable "since 'of the girl' just relocates the same information
without adding anything the checker can resolve differently for a common
noun" — as if common nouns were categorically worse off than proper names
here. Re-running the literal suggested text returned `status: ok` with
**zero** messages, no warning on `girl's` at all. `girl` is a level-1 noun,
plainly in the ontology (`/search` confirms it), so its possessive is no
different from Laban's or David's — the rule was never about proper names
specifically, it's about ontology membership of whatever word carries the
's, common or proper. Three verses in, treat any "possessive not
recognized, corpus-wide" claim as needing this same per-word ontology
check before accepting it — it has now been wrong all three times it was
tested, on three different kinds of "systemic" framing (an individual's
name, a demonym/collective, and a common noun).

### A misspelled `_tag` can be silently ignored rather than flagged — `status: ok` doesn't prove every tag in the text is doing something

Not all underscore-prefixed notation tags fail the same way when misspelled.
Some (the `_implicit*` family: `_implicit`, `_implicitActiveAgent`,
`_implicitNecessary`, etc.) appear to match by **prefix** — `Priests were
killed by enemies _implicitActveAgent.` (missing the second `i` in
`Active`) produces the exact same backtranslation, `<<by enemies>>`, as the
correctly-spelled tag, and even a nonsense suffix (`_implicitXYZZY`) still
triggers the same marking. Others (`_literalExpansion`, and presumably its
sibling `_dynamicExpansion`) require an **exact** match — a misspelling
(`_litearlExpansion`) is silently dropped, parsed as if no tag were present
at all: no error, no `Notes notation` complaint, and no effect on the
backtranslation. Confirmed against the API on both directions with Ezra
9:7's actual typo'd text.

This matters because it can go either way for what looks like a clean
result. Ezra 9:7's suggested encoding carried both typos (`_implictActveAgent`
and `_litearlExpansion`) and still checked at `status: warning` with the one
expected `today` residual — the `_implicit` typo happened to still work by
luck of prefix-matching, but the `_literalExpansion` typo was doing
**nothing at all**, silently. **Don't assume a tag is functioning just
because the encoding validates clean** — proofread tag spelling separately,
by eye, the same way you'd check a word choice; the checker will not
always catch it for you.

It also means "fixing" a typo isn't automatically safe. Correcting
`_litearlExpansion` to the real `_literalExpansion` on Ezra 9:7 turned a
clean, tag-free-in-effect phrase into a genuine `checker:49` placement
error (*"For literal/dynamic expansions, write 'X of Y _literalExpansion'
instead of 'X Y of _literalExpansion'"*) — the typo'd tag had been
silently inert, so the phrase was really validating on its own merits the
whole time, and the correctly-spelled tag turned out to be in the wrong
position for its own rule. Since the untagged phrase (`the hand of
other/foreign kings`) already validates at `status: ok`, the tag wasn't
doing any real work here and the right fix is to drop it, not to
respell it in place. **Before fixing a tag's spelling, check whether the
sentence validates just as well without the tag at all** — a typo that
was silently ignored may mean the tag was never load-bearing in the first
place.

### Hyphenated pseudo-ontology nouns

A hyphen makes the checker look the whole string up as one ontology entry
(rule 0.3 is for genuinely hyphenated ontology words). `man-of-God`,
`river-Habor`, `valley-Arnon` are not entries, so they come back
unrecognized and cascade into false errors on the verbs around them.
Unhyphenate: `man of God`, `a river named Habor`.

### Verb used with a role outside its theta grid

Check the categories list before assuming a verb works. `take-away` is
`Agent, Patient, (Source)` — it takes *from*, never *to*, so "deported X to
Assyria" cannot be encoded with it and must decompose into two events: taken
*from* the source, then `forced [X to go to <destination>]`.

### Patient not immediately after the verb

Several verbs require the Patient to follow the verb directly, with Source /
Destination / Instrument phrases after it. `buy a donkey from me(Yahweh)`
validates; `buy from me(Yahweh) a donkey` raises `Incorrect usage of buy-A`.
`give` states the same constraint explicitly in its message text. When a
verb errors with `Incorrect usage of <verb>` and the arguments all look
right, check the order before changing any words.

### Unknown proper noun directly after an adposition

`in Halah` breaks `in` itself. Use the rule 0.23 `named` form with a generic
head noun: `in a town named Halah`. Order matters — `Halah named a town`
still fails.

### Over-nested clause inside a patient clause

`live` rejects a different-participant patient clause, so a `[_descriptive
which ...]` relative buried inside `forced [... to live in ...]` errors on
the verb. Lift the descriptive out into its own sentence.

### An object-gap relative clause needs its own bracket, nested inside the head noun's bracket

`the bad-B action [that person did today]` — a single flat bracket — leaves
`did` without a patient: `Incorrect usage of do-A`, `do-A: missing patient`,
even though the missing patient is plainly the head noun the clause modifies
(`action`) and the relativizer `that` is present. Adding `that` is not
enough by itself; the relative clause needs its **own** bracket nested
inside the head noun's bracket: `[the bad-B action [that person did
today]]`, not `[the bad-B action that person did today]`. Confirmed on
1 Samuel 14:38: the NIV's *"what sin has been committed today"* is an
object-gap relative (the missing thing is what was committed) — the flat
form errors on `did` every time regardless of `that`; double-bracketing it
reaches `status: ok` with zero messages, same wording otherwise. The
corpus's suggested encoding never tested this: instead of "what sin was
committed," it reworded the whole question to "which person did not obey
God" — a subject-gap relative (`person` is directly the subject of
`obey`, no gap to fill), which needs neither `that` nor the extra bracket,
and sidesteps the construction rather than fixing it. That rewording wasn't
flagged as a forced fix for a case-frame wall (unlike the wall in Genesis
13:9); it was folded silently into an unrelated syntax fix (the `Let X...`
to jussive rewrite), so treat it as another instance of unforced paraphrase
drift the same way Genesis 24:31's is — the more literal wording, once
bracketed correctly, validates just as cleanly. **When an object-gap
relative clause's verb complains about a missing patient, try nesting the
clause in its own bracket inside the head noun's bracket before rewording
the sentence to dodge the construction.**

### `could` outside a so-that clause

Use `be able [to ...]` (P1 Checklist 2.1). Inside a `so-that` clause `could`
is fine.

### Referent drift across a passage

Rule 0.36 — write a given noun the same way everywhere. Real corpus example:
1 Kings 13:14 uses `the man` for the old prophet while 13:16 uses `I(man)`
for the man of God, two verses apart. Check neighbours before settling on a
referent, and report the conflict rather than silently picking one.

### Verb-specific subordinator requirements

`"<verb> does not match any sense in the Ontology"` on an otherwise-correct
verb can mean the same-participant patient clause is using the wrong
subordinator, not that the verb is missing from the ontology. Real corpus
example: Judges 12:1's `prepared [in-order-to fight Jephthah ...]` errored
even though `prepare` and the clause content were both fine — a prior review
pass concluded this was "a genuine case-frame/lexical gap... not fixable by
re-encoding" and left it as an open error. That diagnosis was wrong. The raw
`/check` response's `info`-level messages spell out the exact required
structure per sense, e.g. `prepare-A: missing same-participant patient
clause ('[to Verb]')` — `prepare` wants `[to Verb]`, not `[in-order-to
Verb]`, even though the two subordinators are near-synonyms in meaning.
Swapping to `[to fight ...]` checked `ok`. **Before writing off a
"does not match any sense" error as a lexical gap, read the `info` messages
for the verb's required argument structure and try matching it exactly** —
the fix is often a subordinator swap, not a decomposition or a dead end.

### When every sense of a verb fights the structure, check whether the verb strayed from the source text

Sometimes no case-frame variant works because the verb itself doesn't belong
there — a prior pass embellished past what the NIV actually says, and the
embellishment is what won't validate. Real corpus example: Genesis 47:30's
Joseph's reply — NIV just says *"I will do as you say"* — had been encoded
as `I(Joseph) will do all of the things [that you(Jacob) commanded [me(Joseph)
to do]]]`, introducing "commanded" where the source has no such word. Every
sense of `command` rejected this structure (`command-A: unexpected extra
patient`, `command-B: missing open-quote patient clause`, `command-C:
unexpected different-participant patient clause` — none of `command`'s
senses take a same/different-participant `to Verb` clause with a separate
object at all; only a direct quote or a `that`-clause proposition). Rather
than force `command` into a shape it doesn't have, matching the literal NIV
wording instead — `I(Joseph) will do the thing [that you(Jacob) say]` (`say`
sense B, "non-direct speech", fills the relative-clause gap cleanly) —
reached `status: ok` with zero messages. **When a verb resists every
case-frame variant you try, re-read the raw NIV text before decomposing
further: the verb may have drifted from the source in an earlier pass, and
the literal word is often both simpler and the one that actually validates.**

**The same drift happens with nouns, and it can masquerade as an
ambiguous-complexity warning rather than a case-frame error.** Real corpus
example: Luke 6:4's suggested encoding used `temple` for the place David
entered — but the NIV literally says *"He entered the house of God"*, and
the story (1 Samuel 21) predates the Jerusalem temple's construction by
generations, so `temple` is both a source-text drift and an anachronism. It
carried two `checker:built-in:6` "ambiguous complexity" warnings, and a
prior pass's note suggested the standard fix, a sense tag (`temple-A`).
Tagging would have "worked" in the sense of clearing the warning, but the
word itself didn't belong in the verse. Replacing `temple` with the literal
`house of God` throughout reached `status: ok` with zero messages — better
than tagging, because it fixes the content problem too, not just the
checker complaint. **A word carrying an ambiguous-complexity or level-2/3
warning is always worth checking against the raw NIV text before reaching
for a sense tag or explication — the fix might be that the word shouldn't
be there at all.**

**The same drift also happens with a predicate adjective embedded inside a
relative clause, and it can masquerade as a genuine case-frame gap because
the same word validates fine outside that relative clause.** Real corpus
example: Genesis 13:15's suggested encoding rendered the NIV's *"the land
that you see"* as `the places [that you(Abram) are able [to see]]`, adding
"able to" where the NIV just says "see." `able` (both senses, level 1) is
only ever used predicatively with a same-participant clause — `You(Abram)
are able [to see the places].` checks `status: ok` — but the identical
`are able [to see]` inside a relative clause modifying the noun it belongs
to (`The places [that you(Abram) are able [to see]] are big.`) throws 4
messages, including `'able' cannot be used attributively` on both `able`
and a `GAP_REL` token, plus a 24-sense cascade on `are` (matching the
`be`-cascade shape already documented above). The corpus note treated this
as "a genuine theta-grid gap in the relative clause... left unresolved," as
if `able` simply couldn't be used this way — but the real problem was that
`able` didn't belong in the sentence at all: the NIV says only "that you
see," and this same verse's own `ai_assist` attempt on file backtranslates
as *"the land that you see"* with no "able" in it either, the same tell
Genesis 35:2 showed for a fabricated sentence. Dropping `able` and using
bare `[that you(Abram) see]` reached `status: ok` with **zero** messages.
**A word that validates fine as a sentence's main predicate but throws a
case-frame wall only when embedded in a relative clause is a second signal
(alongside "every sense of the verb fails") that it may be drifted content,
not a real construction limit — check it against the raw NIV and the
verse's own `ai_assist` backtranslation before accepting "theta-grid gap,
left unresolved."**

### Judgment-call residual warnings are not "acceptable residual warnings"

Some warnings only clear by changing the sentence's structure or meaning in
a way that trades one problem for another — e.g. rule 0.33 / `checker:48`
("Don't allow negatives with 'purpose' adverbial clauses") allows an
exception when *"context makes the meaning clear regardless"* or *"avoiding
the construction would be too awkward otherwise."* Real corpus example:
Judges 12:1's `"Why did you not call us [so that we could help ...]]"`
carries this warning; rewriting it to avoid the negative-plus-purpose-clause
construction traded it for a new `checker:38` error (`could` outside a
so-that clause), which is worse. The original construction is the right
call here — but this is a judgment call, not a settled fix, and it must be
**flagged to the user explicitly, every time it recurs, as an open item to
revisit** — do not fold it into "Acceptable residual warnings" below as
though it were closed. The two lists are different in kind: "Acceptable
residual warnings" are warnings with no possible fix (the information
genuinely isn't there to resolve); judgment-call warnings like this one
*could* be reworded away, just at a cost the reviewer judged not worth
paying — so the user should get the chance to weigh in each time, not have
that judgment silently made for them.

## Acceptable residual warnings

Only these two. Everything else deserves one attempt at a fix before you
call it unavoidable — this list previously included the part-of-speech
warning (fixable with a tag, see above), and Genesis 13:10's first review
pass separately shipped an ambiguous-complexity warning and a spelled-out
number as "residual" that both turned out fixable on the second pass (see
"Ambiguous complexity" and "Spelled-out numbers" above). 1 Kings 10:12
briefly added a third item here — an ambiguous-POS adposition whose case
frame seemed to conflict with any disambiguating tag — but that turned out
fixable too: the conflict was with one of the word's two senses, not
inherent to tagging (see "Ambiguous part of speech" above). Try every
listed sense before shipping a POS warning as residual. Judges 17:5's
partitive `one of the sons` warning briefly sat here too, on the strength
of having tried every sense tag and every rewording of the object — but the
real fix touched neither: spelling the number as the digit `1` and
re-bracketing the whole partitive-plus-complement as one clause (see
"Ambiguous part of speech" above). **A warning surviving every tag you tried
on the word itself is not the same as surviving every fix** — check whether
restructuring around the word, not just relabeling it, clears it before
shipping it here.

- Genuine Bible proper nouns absent from the ontology (Halah, Gozan, Habor).
  The name itself cannot be resolved; where one sits in a construction that
  accepts a tag, `_noun` does clear the accompanying part-of-speech warning,
  though the corpus generally omits it — match the surrounding verses.
  Confirmed by the user (2026-09-18): Halah, Gozan, and Habor specifically
  have been logged as an upstream ontology bug — they should be recognized
  as location proper nouns and aren't. Nothing to do per-verse beyond the
  `_noun` tag above; don't keep re-diagnosing these three as if the gap
  might be something else, and don't treat the residual warning as this
  skill's problem to solve — it's tracked upstream.
- `'X' has no theta grid information to check with` (e.g. `bring-D`,
  `be-Y`) — nothing to fix, the grid is simply missing upstream. **But the
  warning itself is only the acceptable part — a missing-grid verb can also
  spuriously break an unrelated embedded clause, and that part IS fixable.**
  Real corpus example: Joshua 2:12's `promise-C` (empty `categorization`,
  no theta grid) took `You(men) (imp) promise Yahweh [that you(men) will be
  kind to my(Rahab) family]` from the lone acceptable warning to three extra
  `be`-cascade messages (`This use of 'be' does not match any sense`,
  `Unexpected destination for 'be'` ×2) — with nothing wrong with `be kind
  to X`, which checks clean on its own. Isolating patient by patient showed
  the cascade fires for every patient except the literal pronoun `me`
  (`promise the man`, `promise God`, `promise him(Yahweh)`, `promise
  her(Rahab)` all cascade; `promise me(Rahab)` doesn't) — a parser quirk
  tied to the missing grid, not a real constraint on who can be promised.
  Restructuring around it (here, pairing `swear` with `promise` per rule
  0.2 — `promise/swear`, simple word first — and moving the Instrument
  phrase before the Destination: `promise/swear by Yahweh to me(Rahab)
  [that ...]`, matching the verse's actual "swear ... by the Lord" idiom
  more literally than a bare `promise` to begin with) dropped the cascade
  back to just the one acceptable `promise-C` warning. **Don't stop at
  confirming the missing-grid warning is unfixable — check whether it's
  also cascading into a nearby clause, and try a different argument or
  argument order (or the word's own rule-0.2 pairing) before accepting
  every message in the group as residual.**

Everything at `label: error` should be gone, and `status: ok` is the normal
end state. `suggest` and `info` are advisory — but read the `suggest` items
before dismissing them, since the part-of-speech tag arrives as one.

**One quirk to know about `status`**: the top-level `status` field can come
back `error` on a sentence that carries no error or warning messages at all
(`That man will put all his(man's) grain into those buildings.` does this).
Judge a fix by the message list, not by the status string alone — and when
counting a corpus sample, expect the "ok" count to run slightly below the
"fully clean" count for this reason.