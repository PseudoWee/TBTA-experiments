# 05 — Vocabulary and complexity (+04 Longman, +05 Complex Terms, ontology levels)

## 1. The core idea

Every word in Phase 1 should be one that nearly any target language can express. "Simple" is defined by the **Longman Defining Vocabulary (LDV)** — the ~2,000 words Longman dictionary writers restrict themselves to — plus a few exceptions. "Complex" words aren't banned; they are *offered alongside* a simple fallback so the translator's language can use whichever it has.

## 2. Complexity levels (ontology colour → level)

| Level | Colour in TBTA ontology | Meaning | In Phase 1 |
|---|---|---|---|
| **0** | Blue | Semantic primitives — "supposed to be available in every language" (⚠️ blue can also mean "nobody set a level; defaulted to 0") | ✅ free |
| **1** | Cream (same as background) | Simple; mostly LDV | ✅ free |
| **2** | Magenta | Complex | ❌ bare. ✅ only in a **pairing** (`son/descendant`), an **explication** (`hard hat`), or a **complex alternate** |
| **3** | Dark green | Very complex/abstract; often expressed a different way (`glory`, `faith`) | pairing, rarely an explication, or **vocabulary alternate** `(complex)…(simple)…` |
| **4** | Brown | Proper names and "key terms" (`God-Almighty`) | ✅ free; never explicated |

Online ontology app: the level appears as `L#` in a coloured box. In the desktop program: the colour of the "Senses" column, or right-click → *Edit this concept's semantic complexity level*.

Tod's stated intent: eventually level 3 words are used *only* in complex alternates; for now levels 2 and 3 are treated the same.

**He1:** you may use a level-2 word without a pairing; indicate how to handle it in a "complex concepts" section, e.g. `CC: helmet = hard hat | ask/beg` (explication for *helmet*, pairing for *beg*). Complex alternates are used in He1 exactly as in He2. A level-3 word where pairing/explication isn't appropriate → complex alternate.

## 3. Choosing between pairing, explication, alternate

| Method | When | Form | Example |
|---|---|---|---|
| **Pairing** | A simple word carries the sense well enough | `simple/complex` | `say/proclaim`, `animal/donkey`, `good-B/righteous` |
| **Explication** | No good pairing; a phrase of simple words works | simple phrase in place of the word | `hard hat` for helmet; `young sheep` for lamb |
| **Complex alternate** | Abstract level-3 idea; neither of the above is adequate | `(complex)… (simple)…` | `(complex) Mary had faith in God. (simple) Mary trusted in God.` |
| **`null/X`** | Substituting a simple word would be wrong | `null/X` | `friends/brothers-D <<and null/sisters-D>>` |

Hard rules:

* **Simple word first, complex second.** `animal/donkey` ✅; `donkey/animal` ❌ (the pairing's *case frame* is checked against the simple word's grid, too).
* **Rule 0.31:** the sentence must make sense with either side.
* **A hyphenated particle verb on the simple side stays uninflected**: `take-away/arrested` ✅, `took-away/arrested` ❌ (comes back as "not recognized"). Tense goes on the complex side.
* **Referents in parentheses** count too: `I(prophet)` errors exactly like bare `prophet`. Use a level-0/1 referent (`person`, `man`).
* **Don't paste an explication blindly** — test it standalone first. `astrologer` → `person [who searches signs-B [that are in the sky-B]]`: the bare verb `search` raises "Incorrect usage of search-A"; `searches for signs-B` validates.
* **Repeat the explication in full at each occurrence.** `neighbor's` ×6 in Exodus 20:17 means six full explications — verbose by design.

### Worked examples (corpus-verified fixes)

| Word | ❌ bare | ✅ fix |
|---|---|---|
| prophet | `the old prophet` | `the old man [who told God's messages to people]` |
| donkey | `a donkey` | `animal/donkey` (also `horse/donkey`) |
| lamb | `a lamb` | `young sheep` |
| firstborn | `the firstborn son` | `the son [that was born first _adv]` |
| angel | `an angel` | `servant/messenger [who comes from God]` |
| holy | `holy` | `special/holy`, `good-B/holy`, `perfect/holy`, `pure/holy` (only for substances) |
| kingdom | `kingdom` | `country/kingdom`, `land/kingdom`, `area/kingdom` |
| neighbor | `neighbor` | `person [who lives near X]` (no pairing exists) |
| redeem | `redeem` | `buy/redeem` (also save, protect, defend) |
| arrest | `arrest` | `take-away/arrest` |
| chariot | `chariot` | `vehicle/wagon of war` |
| sacrifice (noun) | `a sacrifice` | `animal/sacrifice`, `gift/sacrifice`, or `animal [that a person gives to God//Yahweh [so that the priest would kill that animal]]` |
| scripture | `scripture` | `God's book` (singular) |
| apostle (L3) | `apostle` | `man [that Jesus sent to people _genericOptional [so that that man would be Jesus's representative]]`, then pair with `representative`/`leader` |
| temple | `temple` (ambiguous) | `the building [that people honor/worship Yahweh in]` (clean, zero messages) |
| sling/rope | `sling` (L2) | `rope` (noun), `throw-A` (verb) — and decompose, don't just swap (1 Samuel 17:50) |

The **full 1,469-entry table** (status in ontology / approved / suggested / not used; pairing; explication; argument structure; notes) is at `skills/niv-to-phase1/references/complex-terms.md`. It's a snapshot; `https://ontology.tabitha.bible/simplification_hints?complex_term={word}` is authoritative when they disagree. Note some words have structure-specific entries: e.g. `prophet-A` has five entries (bare, `prophet of X`, `be-Prophet`, `False prophet`, `be a false prophet`).

### Statuses you will meet in `/simplification_hints`

| `ontology_status` | Meaning |
|---|---|
| in ontology | real entry at the stated level |
| approved | pairing/explication ratified and implemented/going to be |
| suggested | proposed, not ratified |
| not used | **not an entry at all** (`level: -1`); the "explication" is just the replacement word. Example: `large` → *"Use 'big'"*. Swap the word; nothing to pair. |

A note in +02 §1: any word in the how-to table with **"Yes"** in the right-hand column may be used as a complex word, **even if not yet in the ontology** — the table records what *will* be implemented.

### Policy summary (from +00)

* Full Phase 1: **always** write in simple terms — `say/proclaim`, `hard hat`.
* He1: complex terms may be written without a pairing/explication.
* A complex word needs a pairing or simple explication, and typically **20+ occurrences** in the Bible (exceptions where no pairing/explication represents it well).
* Proper nouns can always be added. New arguments (e.g. optional beneficiary) and new words are sometimes introduced — ask the maintainers.

## 4. The Longman Defining Vocabulary

* Source: *Longman American Dictionary* "Table of words used in definitions". Letters A–Z, ~2,000 headwords; labels like `n.`, `adj.` restrict part of speech (e.g. `anger n.` — noun only).
* Allowed derivations: the listed prefixes/suffixes (`-able -al -ance -ation dis- -ed -ence -er -ful -ic -ical im- in- -ing -ion ir- -ish -ity -ive -less -ly -ment -ness non re- self- -th un- -y`) provided the meaning is completely clear.
* Compound words made from LDV words are OK if the meaning is clear (`businessman`).
* Phrasal verbs: Longman avoids them; in TBTA, hyphenated ontology phrasal verbs (`take-away`, `stand-up`) are separate entries.
* No proper nouns in the LDV; they are always allowed in TBTA.
* **Using the LDV for a new word:** if the sense you want is the **first or second** sense in the Longman online dictionary, assume it can be added. If the sense is far down a long list, think twice. Mark a candidate with `_inLDV` after the word; a reviewer decides.
* Not everything in the LDV is in the ontology; **not everything in the ontology is in the LDV**. The ontology is the final authority for what's *recognized* — the LDV tells you what's *likely acceptable to add*.
* Words that the project deliberately does not use even if common: `really` (use `actually`/`truly`), `large` (use `big`), spelled-out numbers (`two` → `2`).

Checking examples:

| Candidate | Check | Verdict |
|---|---|---|
| `ability` | in LDV | likely addable, tag `_inLDV` |
| `consider` | complex but appears many times in epistles | add with pairing `think/consider` |
| `really` | LDV word but not used | `actually` or `truly` |
| `helmet` | not in LDV; level 2 | explicate: `hard hat` |

## 5. Numbers

Only digits are ontology entries: `two` → `2`, `forty` → `40`, and **`one` → `1` always** (confirmed by the project owner 2026-09-21; `one` otherwise exists only as an attributive adjective). Fires `checker:built-in:7` ("not recognized") if you spell it out. See also the partitive `1 of the sons` trick in file 07.

## 6. Proper nouns missing from the ontology

Allowed; the checker warns "not recognized" and that warning is acceptable. Known upstream gap logged by the project owner: **Halah, Gozan, Habor** should be recognized as locations and aren't. (Naboth, Ben-Hadad also remain unrecognized.) But a missing proper noun sitting directly before a `be` verb or directly after an adposition *breaks the neighbouring grammar* — tag it `_noun`, or use the rule 0.24 form: `in a town named Halah`. Details in file 07.

## 7. Looking things up (endpoints)

| Need | Call |
|---|---|
| Level, senses, theta grid | `GET https://ontology.tabitha.bible/search?q={word}&scope=all` |
| Pairing/explication for L2/3 | `GET https://ontology.tabitha.bible/simplification_hints?complex_term={word}` |
| Precedent for how a concept was encoded | `GET https://ontology.tabitha.bible/examples?concept={concept}&part_of_speech={pos}` |

Reliability caveat observed in practice: a fetch tool that "edits the query string of a URL already fetched" has silently returned the *previous* query's cached result. Don't chain modified-query fetches blindly; verify with a fresh request.
