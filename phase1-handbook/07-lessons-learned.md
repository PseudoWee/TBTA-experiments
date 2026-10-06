# 07 — Lessons learned from running the pipeline

Everything here was **confirmed by running real verses through the checker** during review passes and scheduled calibration runs (Sept 2026), unless marked otherwise. Read it after you have attempted a few verses.

## How to use this file

When a verse errors, work down this order — it is ordered by "cheapest to check, most likely to be the real cause":

1. **Mechanical typos** — spacing, notation spelling, digits (§2).
2. **Cascade sources** — one malformed thing producing many fake errors (§3).
3. **Recurring rule patterns** — `all of`, level-2/3 words, POS tags (§4).
4. **Verb case frame** — theta grid, argument order, subordinator (§5).
5. **Content fidelity** — did you drop, invent, or paraphrase? (§6) — *the checker will not tell you.*
6. **Only then** decide a warning is unfixable (§7).

## 0. The meta-lessons (worth memorising)

1. **The checker validates syntax, not truth.** `status: ok` is compatible with a fabricated sentence, a dropped clause, or a changed speech act.
2. **A prior pass's claim is a claim.** "Unfixable", "known regression", "structural limit", "this sense was tried and failed" — each has been wrong repeatedly when re-tested (details below). *Re-run the exact thing.*
3. **Isolate to diagnose.** Copy the suspect clause into a one-sentence test string and re-check. If the error disappears, it was a cascade.
4. **The checker is a remote service that changes.** A note about its behaviour has a shelf life (a genuine outage on sense-letter tags existed at one timestamp and was later cited long after it ended).
5. **Prefer the literal wording first.** An expansive paraphrase is only justified if the literal one genuinely can't validate.
6. **Read the back-translation against the NIV, from the first word, every time.**

---

## 1. Root cause vs cascade

The checker says: *"because this word is not recognized, errors and warnings within the same clause may not be accurate."* An unrecognised or malformed element poisons diagnoses around it. If you "fix" the symptom you will make wrong changes.

**Method:** pull each suspect clause out, test it alone.

* Exodus 13:13 `buy-A` — error *survived* isolation → genuine word-order fault.
* Joshua 4:5 — two `go` errors vanished when `where` was fixed → pure cascade.

---

## 2. Mechanical fixes (do these first; zero judgement)

### 2.1 Spacing / `token:syntax`

| Wrong | Right |
|---|---|
| `David[who was …]` | `David [who was …]` |
| `].../rape`, `.Why`, `(dynamic)John` | `] ...`, `. Why`, `(dynamic) John` |
| `things_implicit`, `man-of-God_noun` | `things _implicit`, `man of God _noun` |
| `able_B` | `able-B` (sense suffix is hyphenated; underscore = notes tag) |
| `People\children` | `People|children` (`dynamic|literal`) |
| `(implicit-info)`, `(alt)` as invented | use real tags (file 04) |

A missing space before `[` can register as several separate messages: 1 Kings 20:13 — two glued brackets produced **5 spurious** `built-in:1` errors on `come` and `tell`; 7 messages cleared by adding two spaces. The back-translation shows the tell: `the person[ that who was the leader`.

### 2.2 `all` → `all of` (`checker:35`, rule 0.18)

| ❌ | ✅ |
|---|---|
| `all the animals` | `all of the animals` |
| `all these animals` | `all of these animals` |
| `all the people [who lived previously]` | `all of the people [who lived previously]` |
| `all you(soldiers)` | `all of you(soldiers)` |
| `all people are sinners` (generic) | unchanged |

Don't sweep blindly: **mass/generic nouns don't fire it.** Luke 12:18 — `all my(person's) grain` is right; `all the things` in the next clause is not. In the 2026-09-10 sample this rule produced 15 errors across 5 verses — all from a missing two-letter token.

### 2.3 Spelled-out numbers (`built-in:7`)

`two`→`2`, `three`→`3`, `forty`→`40`, **`one`→`1`** (always — confirmed 2026-09-21). Seen in Genesis 13:10, Joshua 24:12, Ezra 8:32, Luke 9:13.

### 2.4 Capitalisation and comma before quote

First word of sentence/quote capitalised (`built-in:0`); `that person said, ["I(person) will …]` (comma, `checker:20`).

### 2.5 Title-case common nouns mid-sentence

`the King of the Jews` read as an unrecognised proper noun. Lowercase: `the king of the Jews` → `ok`, zero messages (Luke 23:37). A prior pass had called this a "lexicon gap".

### 2.6 Hyphenated pseudo-nouns

`man-of-God`, `river-Habor`, `valley-Arnon` aren't ontology entries → unhyphenate: `man of God`, `a river named Habor`.

### 2.7 Uninflected hyphenated verbs

`took-away` ❌ → `take-away`; `came-out` ❌ (not an entry) → `come-out _past`. Inside a pairing the fault is silent as "unrecognised": `take-away/arrested` ✅, `took-away/arrested` ❌ (two `built-in:7` warnings).

### 2.8 Misspelled `_tags` can be silently ignored

* `_implicit…` tags match by **prefix** — `_implicitActveAgent` and even `_implicitXYZZY` behave like `_implicit…`.
* `_literalExpansion` needs an **exact** match; `_litearlExpansion` is silently dropped (no error, no effect).
* ⚠️ "Fixing" a typo isn't always safe: respelling `_litearlExpansion` correctly on Ezra 9:7 produced a real `checker:49` placement error, because the sentence had been validating *without* the tag. Check whether the sentence validates equally well with no tag at all before respelling. Proofread tags by eye.

---

## 3. Cascade sources that are *not* unrecognised words

All of these look like a **verb** fault — `This use of '<verb>' does not match any sense in the Ontology`, often with `cannot be used with a different-participant patient clause` — while the break is elsewhere. **Never start by re-picking a verb sense** if one of these is present.

### 3.1 `where` as relativizer (`checker:32`)

❌ `into the river near the place [where the priests are standing]`
✅ `into the river near the place [that the priests are standing in]`

❌ `to the house [where Jesus was teaching people about God]`
✅ `to the house [that Jesus was teaching people about God in]`

Joshua 4:5: four errors → zero. Luke 5:18: both `carry` errors vanished. Genesis 36:43: five errors → one. The tell: back-translation reads *"the house **that where** Jesus was teaching"*. **Not guaranteed:** Luke 12:18 (`my buildings [where I store things]`) — the `where` error stands alone. Confirm by isolation.

### 3.2 Glued bracket — see §2.1.

### 3.3 Distributive `each … one <noun>`

`Each of you(man) should carry one stone on your(man's) shoulder` — checker can't resolve POS of `one` and `stone`; cascades to `carry`. No tag or rewording of the subject helps. A plural rewrite validates: `You(men) should carry the stones-A on your(men's) shoulders.` ⚠️ **Meaning-narrowing** (distributive force lost) — flag it to the user.

### 3.4 `(alt)` — not a tag

1 Kings 10:12 used `(alt)` to pair `harps and lyres` with an explication. The checker never saw the first sentence as `(complex)`, so `harps`/`lyres` were flagged as bare L2. Retag `(complex) … (simple) …` → both errors cleared. Two `checker:5` "multiple verbs" errors (`have brought`, `have not seen`) in the same verse were *also* cascade — isolated, `People have brought gold to Judah.` checks clean. **Don't rewrite `have + participle` to simple past on sight.**

### 3.5 `let` (and `make`, `have`, causatives) without a bracket around the embedded action

`let those sick people touch the edge of Jesus's clothes/robe` → read as two main-clause verbs: `Incorrect usage of let-A`, `Unexpected patient for let-A`, `Cannot have multiple verbs in the same clause (let and touch)` — three messages from a missing bracket.
✅ `let [those sick people touch the edge of Jesus's clothes/robe]` — Matthew 14:36: 4 errors → 0.

### 3.6 Untagged ambiguous-POS word — cascades *far* from itself

* **Luke 9:13–14** — `We(representatives) have only 5 loaves of bread and 2 fish` errored on `have` (`have-X: missing state` on every sense) even though the object was right there. A review pass called it a "genuine case-frame gap". Real cause: untagged `only`. `only _adv` → `status: ok`.
* **1 Corinthians 13:4** — `Love is patient`, `Love is kind`, `Love does not want…` etc. had errors on `is`, `want`, `speak`. A prior pass declared a "structural limit": abstract nouns can't be Agent. Wrong. `Love _noun` at all five occurrences → **zero** messages.
* So: **a claim that a construction is a "structural limit" is exactly the claim to test with a POS tag first.** It was disproved at two scales (one clause; a whole verse).

### 3.7 Unrecognised proper noun right before a `be` verb breaks the verb

2 Kings 18:11 `A river named Habor is beside that town named Gozan.` → `is` fails every sense (`be-A`…`be-Y`, "missing agent"). Isolation: `A river named Habor is beside a town.` errors; `A river named John is beside a town.` is clean; `A river named Habor _noun is beside a town.` is clean except the expected "not recognized" warning. Tag only the one before `be`. The verse was recorded `warning` but was really `error`.

Same for **recurrences**: 1 Kings 20:4 had `Ben-Hadad` four times; a prior pass fixed the two inside `named` constructions and missed `You(Ben-Hadad) are the king` (breaks `are`). Fix: swap the bare referent for a recognised token (`you(king)`) and establish the name once via `named`. **Check every occurrence, not just the one already fixed.**

### 3.8 Unknown proper noun directly after an adposition

`in Halah` breaks `in` itself. → `in a town named Halah` (order matters; `Halah named a town` still fails).

---

## 4. Recurring patterns by rule

### 4.1 Level-2/3 word used bare (`built-in:4`) — #1 by volume

85 of 241 errors in the 2026-09-09 sample; same rank every sample since. Fix per word → file 05 table. Key reminders: simple word first; test an explication standalone; repeat per occurrence; referents count.

**`not used` words are different** — `The Adjective 'large' is not in the Ontology` → `ontology_status: not used`, explication `Use 'big'`. Swap the word.

### 4.2 Ambiguous part of speech (`built-in:8`) — tag it, don't dismiss it

When the editor says it "cannot determine which part of speech" and suggests `_noun/_verb/_adj/_adv/_adp/_conj/_part`: **take the suggestion.** `[that was born first _adv]` → `ok` (Exodus 13:13). Rules:

* Separate token with a leading space: `first _adv`. `man-of-God_noun` → "Notes notation should have a space before the underscore".
* **Per occurrence, not per word.** Genesis 35:2 used `clean` as verb *and* adjective; prior note said "no way to disambiguate" → `clean _verb yourselves` … `clean _adj clothes` → `ok`.
* **If the first tag worsens things, try the other listed sense.** 1 Kings 10:12 `more-than`: `_adp` (case frame demands an immediate bracket) made it an error; `more-than _adj` → zero messages.
* **Try every sense, including an odd-looking one.** Genesis 24:31 `stand outside`: `_adv` (no Adverb sense exists) and `_adp` (wants an object) both failed, so a prior pass left it. `/search` showed a Noun sense; `stand outside _noun` → `ok`, zero messages.
* **Partitive `one of the X`.** Judges 17:5 `Micah chose one of the sons of Micah [to be the priest of Micah]` — warning on `one`. Every sense tag and rewording failed. The fix touches two things at once: digit **and** re-bracket the whole partitive-plus-complement: `Micah chose [1 of the sons of Micah to be the priest of Micah]` → zero messages. Neither alone works.
* A POS warning is fixed by a **POS tag**, never a sense letter: 1 Kings 20:37 `please` — `please-A` didn't help; `please _part` → `ok`.

### 4.3 Ambiguous complexity (`built-in:6`) — also fixable

*"This word has multiple senses and ambiguous complexity. Consider including the sense (e.g. heal-A)."* Prefer **full explication** over a bare sense tag when one exists (clears the word entirely; no `suggest` noise): 1 Kings 10:12 `temple` → `the building [that people honor/worship Yahweh in]` → `ok`.

Otherwise tag the sense: `Lot-A` (Genesis 13:10 → `ok`). Choose by **meaning**, not by what clears first: `ark-A` is Noah's boat, `ark-B` is "another name for the ark of the covenant" → use `ark-B` (2 Samuel 6:6); `sign-B` "a thing or an event that has a specific meaning" for a supernatural token (Judges 6:33); `hang-C` ("hang something somewhere") not `hang-A` (no patient slot) nor `hang-B` (kill by hanging) (2 Samuel 21:6); `temple-C` (a place of worship for a false god) for Micah's household shrine (Judges 17:5).

**The "consider removing the sense" `suggest` message is unreliable.** Removing `temple-A` on its say-so brought the warning back (1 Kings 10:12). Test the untagged form yourself.

**Claims about sense tags regressing.** A genuine service outage on sense-letter tags was recorded at 2026-09-12T08:03 ("9 of 9 spot-checked tags failed"). Runs from 09:55 and 10:54 still cited it, and left warnings bare — but by then `Lot-A`, `sign-A` validated fine. 1 Kings 20:37 conflated a sense-tag claim with a POS warning. Treat any "known regression" claim as presumptively stale and re-test.

### 4.4 Possessive 's — warns only when the *base word* is out of the ontology

Corpus notes claimed "possessive 's isn't recognised" as a corpus-wide gap. Re-tested: **wrong three times** — Genesis 30:32 `your(Laban's) sheep` (zero messages), Ezra 9:7 `Ezra's`, `Israelites'` (only an unrelated `today _adv` fix needed), Mark 5:40 `the girl's` (common noun, zero messages). Only `Naboth's`, `Ben-Hadad's` still warn — because `Naboth`, `Ben-Hadad` aren't in the ontology. **Check the base word with `/search` before accepting any possessive claim.**

### 4.5 Footnote vs comment — see file 04. Passes the checker either way; read the NIV.

### 4.6 Verb used with a role outside its theta grid

`take-away` is `Agent, Patient, (Source)` — takes *from*, never *to*. "Deported X to Assyria" can't use it with a destination. Decompose: `…take-away … from Israel` then `forced [X to go to Assyria]`. (2 Kings 17:6 and 18:11 shared the identical fault — fix parallels together.)

### 4.7 Patient not immediately after the verb

✅ `buy a donkey from me(Yahweh)` / ❌ `buy from me(Yahweh) a donkey` (`Incorrect usage of buy-A`). `give` states it in its message. When a verb errors with `Incorrect usage` but arguments look right, check **order**.

### 4.8 Over-nested clause inside a patient clause

`live` rejects a different-participant patient clause; a `[_descriptive which …]` buried in `forced [… to live in …]` errors on the verb. Lift the descriptive out into its own sentence.

### 4.9 Object-gap relative clause needs its own bracket

`the bad-B action [that person did today]` — single bracket → `Incorrect usage of do-A … missing patient`. ✅ `[the bad-B action [that person did today]]` (1 Samuel 14:38 → zero messages). The corpus had dodged it by rewording the question — silent paraphrase drift. Try the bracket before rewording.

### 4.10 Verb-specific subordinator

`prepared [in-order-to fight Jephthah …]` errored (Judges 12:1) though `prepare` was fine. The `info` messages said `prepare-A: missing same-participant patient clause ('[to Verb]')`. `[to fight …]` → `ok`. A prior pass had called it a lexical gap. **Read the `info` messages for the exact structure.**

### 4.11 `could` outside a so-that clause → `be able [to …]` (`checker:38`).

### 4.12 Referent drift across a passage (0.36)

1 Kings 13:14 `the man` for the old prophet vs 13:16 `I(man)` for the man of God, two verses apart. Check neighbours; report conflicts rather than silently choosing.

### 4.13 Missing-grid verbs can still cascade

`'X' has no theta grid information to check with` (`bring-D`, `be-Y`, `promise-C`) is an acceptable warning — but it can spuriously break an embedded clause. Joshua 2:12: `promise Yahweh [that you(men) will be kind to my(Rahab) family]` → three extra `be` cascade messages (only `promise me(Rahab)` didn't cascade). Fix by restructuring: `promise/swear by Yahweh to me(Rahab) [that …]` (pairing per 0.2, instrument before destination) → back to the single acceptable warning.

---

## 5. When every sense of a verb fights you — check the source

Sometimes the verb doesn't belong there.

* **Genesis 47:30.** NIV: *"I will do as you say."* Encoded `I(Joseph) will do all of the things [that you(Jacob) commanded [me(Joseph) to do]]` — every sense of `command` rejected it. Literal wording: `I(Joseph) will do the thing [that you(Jacob) say]` → `ok`.
* **Luke 6:4** `temple` (with two ambiguous-complexity warnings) — NIV says *"the house of God"*, and the story predates the temple. Replacing with `house of God` → `ok` and fixes an anachronism. *A sense tag would have cleared the warning but kept a wrong word.*
* **Genesis 13:15.** `the places [that you(Abram) are able [to see]]` threw 4 messages (`'able' cannot be used attributively`, 24-sense cascade on `are`). NIV: *"the land that you see"*. Drop `able` → `[that you(Abram) see]` → zero messages. **A word that validates as a main predicate but walls only inside a relative clause is a second hint it's drifted content.**

---

## 6. Content fidelity — what the checker can't see

The deliverable must be **the verse**. Compare back-translation to NIV from the first word. Seven recurring flavours, each from a real corpus entry:

| # | Flavour | Real example | Fix |
|---|---|---|---|
| 1 | **Fabricated sentence** | Genesis 35:2 had an extra *"People/foreigners honor/worship those objects/idols!"* — nothing in *"Get rid of the foreign gods you have with you, and purify yourselves and change your clothes."* It had survived a correction pass because pairing `objects/idols` correctly and having a sentence that doesn't belong are orthogonal. | Delete it — that *is* the content fix. |
| 1b | **Filler to satisfy quote-bracket mechanics** | Matthew 8:4 opened the quote with invented `You(man) (imp) listen to me(Jesus) _implicit`; 1 Kings 20:18 inserted redundant restatements of each conditional. A `["…"]` bracket wraps **one sentence only** (several → "multiple verbs in the same clause"). | The one genuine first sentence — even a complex `if`-conditional — can be the bracketed sentence: `["[If those men are coming to us(army) [in-order-to make peace]], you(people) (imp) catch/capture those men.] And you(people) (imp) do not kill those men. Or [if …]…` validates (only the expected `Ben-Hadad` warning). |
| 2 | **Changed speech act / person / number** | Genesis 24:31: *"Why are you standing out here?"* → flat command `You(servant) (imp) do not stand outside`; invented `come into our(Laban) house`; *"I have prepared the house and a place for the camels"* → `We(Laban) have a room [that you(servant) may stay in]`. | Literal forms all validate: `Why are you(servant) standing outside _noun?` / `You(servant) (imp) come` / `I(Laban) prepared the house _noun and a place [for your(servant) animal/camels]`. |
| 3 | **Content pulled from another verse / one speech act split in two** | Joshua 2:12 made one oath (*"swear to me by the Lord that you will show kindness to my family"*) into two `promise` acts, and turned *"Give me a sure sign"* into `prove … protect me` (borrowed from 2:13). | Symptom-fix of a real cascade (§4.13). Literal `swear/promise by Yahweh to me(Rahab) [that …]` and `give a true sign-B to me(Rahab)` both validate. |
| 4 | **Swapped name/epithet** | 2 Samuel 6:6 used "ark of the covenant" where NIV has "the ark of God". Accurate but not what the verse says. | `ark of God` + `ark-B`; `ok`, zero messages. |
| 5 | **Silently dropped clause** | 2 Samuel 21:6 omitted the opening *"As for the man who destroyed us and plotted against us so that we have been decimated…"*. The corpus change-log lists edits made, not content never carried over. | Restore it — needed real work: `plan/plot` only validates with its own explication `Saul plan/plotted [to do bad-B things to us(people)]` (the case frame follows the **simple** word `plan`'s grid; even `plan/plot-A against us` fails). **Only reading the back-translation against the full NIV sentence catches this.** |
| 6 | **Unforced paraphrase** | 1 Samuel 14:38 reworded *"what sin has been committed today"* to *"which person did not obey God"* to dodge a bracket problem (§4.9). | Bracket correctly; literal wording validates. |
| 7 | **Dynamic swapped for literal** | — | Literal first; add dynamic as an alternate. |

### When expansion is *right*

* **Tagged implicit expansions** (`(implicit-situational)` shown as `<<…>>`) — documented convention, leave alone (2 Samuel 6:6).
* **Genuine case-frame wall** — Genesis 13:9: *"Let's part company"* + *"If you go to the left, I'll go to the right…"* became `You(Lot) and I(Abram) should not live in the same place… [if you go to the western place/region] I will go to the eastern place/region`. Testing the literal: `separate` takes Agent/Patient/Source, not a reciprocal; `go to the left` is `go` used with a predicate adjective (`built-in:1`, real). `western/eastern` isn't arbitrary (Genesis 13:11 says Lot went east). **A paraphrase is only drift if a more literal version also validates and wasn't used.**

---

## 7. What is genuinely acceptable to leave

**Only these two** (the list is short because every other candidate eventually proved fixable):

1. **Genuine Bible proper nouns absent from the ontology** (Halah, Gozan, Habor — logged upstream by the project owner 2026-09-18; don't re-diagnose). Where the name sits in a construction that accepts it, `_noun` clears the accompanying POS warning, though the corpus generally omits it.
2. **`'X' has no theta grid information to check with`** — but check for side-cascades (§4.13).

**Not acceptable-residual (each was once listed and later fixed):** ambiguous POS, ambiguous complexity, spelled-out numbers, partitive `one of the sons`, `more-than` adposition conflict.

### Judgment-call residuals (flag to the user *every* time)

Warnings that *could* be reworded away but at a cost the reviewer judged worse. Example — Judges 12:1 `"Why did you not call us [so that we could help …]]"` carries `checker:48` (negative + purpose clause). Rewriting to avoid it traded it for `checker:38` (`could` outside so-that), which is worse. Original is the right call, but the user should get to weigh in; don't bury it as "acceptable".

### When the fix narrows meaning

State it in the Was/Now/Reason row and let the user decide (the distributive rewrite §3.3 is the standard case).

---

## 8. Checklist of "claims to re-test before believing"

| Claim in an old note | What re-testing found |
|---|---|
| "Sense-letter tags are rejected (known regression)" | True once (2026-09-12 08:03); stale within hours. |
| "`ark-A`/`ark-B` not found in any POS" | Both validate. |
| "Every sense of `sign` returns 'No sense found' and tagging breaks `for`" | All three validate; nothing breaks. |
| "Possessive 's not recognised, corpus-wide" | False ×3. |
| "Abstract noun can't be Agent (structural limit)" | False — it was a missing `_noun`. |
| "Genuine case-frame gap in `have`" | Missing `only _adv`. |
| "`prepare` is a lexical gap" | Wrong subordinator. |
| "No way to disambiguate `clean`" | Tag each occurrence. |
| "Status: warning" | Re-run: can be `error` or `ok`. |
| "`outside` can't be tagged" | `_noun` works. |

## 9. Systemic observations worth knowing

* **Parallel passages share bugs** (2 Kings 17:6 and 18:11). Fix both; flag the systemic issue and offer to sweep.
* **Neighbouring corpus verses are not proof of validity**, even at "Final Review in Progress". Copy a convention only after it validates (Numbers 18:15 is the working model for firstborn-redemption verses).
* **`status` and recorded notes drift**; re-run before trusting.
