---
name: phase1-encoding-review
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
   Assyria of>> the king`).

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
- State explicitly which warnings remain and why they are acceptable.
- **When the fix that validates also narrows the meaning, say so in the row**
  and let the user decide. The distributive rewrite below is the standard
  case: it reaches `status: ok` but loses "each … one".
- Flag anything systemic you noticed — a bug shared with the parallel verse,
  a convention that fails corpus-wide — and offer to sweep for it, rather
  than silently fixing only the verse asked about.

## Cascade sources that are not unrecognized words

All three of these present as a **verb** fault — `This use of '<verb>' does
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
paralyzed`).

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

### Missing comma before an opening quote (checker:20)

`Expect a , before a quote_begin clause.` A quoted speech clause must be
preceded by a comma: `that person said, ["I(person) will ...]`. Cheap and
mechanical, and it travels with the capitalization rule (`built-in:0`) at
the start of the quoted material.

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

### `could` outside a so-that clause

Use `be able [to ...]` (P1 Checklist 2.1). Inside a `so-that` clause `could`
is fine.

### Referent drift across a passage

Rule 0.36 — write a given noun the same way everywhere. Real corpus example:
1 Kings 13:14 uses `the man` for the old prophet while 13:16 uses `I(man)`
for the man of God, two verses apart. Check neighbours before settling on a
referent, and report the conflict rather than silently picking one.

## Acceptable residual warnings

Only these two. Everything else deserves one attempt at a fix before you
call it unavoidable — this list previously included the part-of-speech
warning, which turned out to be fixable with a `_adv` tag.

- Genuine Bible proper nouns absent from the ontology (Halah, Gozan, Habor).
  The name itself cannot be resolved; where one sits in a construction that
  accepts a tag, `_noun` does clear the accompanying part-of-speech warning,
  though the corpus generally omits it — match the surrounding verses.
- `'X' has no theta grid information to check with` (e.g. `bring-D`,
  `be-Y`) — nothing to fix, the grid is simply missing upstream.

Everything at `label: error` should be gone, and `status: ok` is the normal
end state. `suggest` and `info` are advisory — but read the `suggest` items
before dismissing them, since the part-of-speech tag arrives as one.

**One quirk to know about `status`**: the top-level `status` field can come
back `error` on a sentence that carries no error or warning messages at all
(`That man will put all his(man's) grain into those buildings.` does this).
Judge a fix by the message list, not by the status string alone — and when
counting a corpus sample, expect the "ok" count to run slightly below the
"fully clean" count for this reason.
