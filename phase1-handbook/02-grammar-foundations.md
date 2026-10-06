# 02 — Grammar foundations (from "+01 Introduction to TBTA Grammar")

Almost every Phase 1 rule is a consequence of how TBTA models a sentence. Learn this model once and the checklist stops looking arbitrary.

*Items the original marks as less important for He1 are flagged **(He2-heavy)**.*

## 1. Words

The sentence is the basic unit; words are its building blocks. Every word you may use is an **ontology** entry (or a proper noun, or a pending addition).

Not every Phase 1 word becomes a word in Phase 2. Many become **features**:

| You write | Becomes in P2 |
|---|---|
| `John is very sad` | `very` → "intensified" feature on the adjective `sad` |
| `too big`, `extremely big` | "too" / "extremely intensified" features on `big` |
| `bigger than` | "comparative" feature |
| `John began talking` | `began` → "inceptive" aspect on `talk` (not a verb) |

## 2. Phrases

Words are always wrapped in a **phrase**: nouns in noun phrases (NP), verbs in verb phrases (VP), adjectives in adjective phrases (AdjP), adverbs in adverb phrases (AdvP). Exceptions: conjunctions, "phrasals" (like *Selah*) and particles (periods, parentheses, list numbers). You never build phrases by hand in Phase 1.

Curly-brace shorthand used in the source:

```
A big man was eating food
{NP {AdjP big} man} {VP eat} {NP food}
```

The tense and "a/was…ing" are features, not words in the structure.

## 3. Clauses

A **clause** (= proposition) is a statement about something. Every clause has a **verb phrase** and a **noun phrase for the agent** (the subject).

Consequence for implicit marking — the single most error-prone area:

* A verb can only be implicit via `_implicitNecessary` (He1: `<…>`). It will still appear in generated text, flagged as implicit.
* An active-voice agent can only be implicit via `_implicitNecessary`.
* A *passive* agent can be implicit via `_implicitActiveAgent` (He1: `<<by X>>`).
* Other phrases can be ordinary `_implicit` (He1: `<<…>>`).

Example *(source)*: `John eats` vs `John eats food _implicit`. If a language *requires* an object for "eats", TBTA will generate "food" anyway even if you marked it implicit and the translator switched implicit info off.

## 4. Adjective phrases

* **Attributive** — next to the noun: `big house`.
* **Predicative** — argument of `be-D`: `The house is big`.

You don't normally mark the difference; your wording decides it.

## 5. Noun phrases and their nine semantic roles

Every NP has one role. These replace English grammar terms like "direct object":

| Role | Roughly | Signal word you write | Example |
|---|---|---|---|
| Most Agent-like | the doer / subject | — | **John** went |
| Most Patient-like | the thing acted on | — | John saw **Mary** |
| State | the state (only with `be`/`have`) | — | John is **a man** |
| Source | where/what from | `from` | John came **from Bethlehem** |
| Destination | where to | `to` | John went **to Bethlehem** |
| Instrument | what is used | `with` | John filled the container **with water** |
| Beneficiary | who benefits | `for` | John did good things **for Mary** |
| Addressee | who is spoken to | (comma) | **Lord**, I am very sad! |
| Not applicable | NP with a relation, or inside an adjective phrase | relation word | John worked **during the day** |

### Signal (function) words

`to`, `from`, `with`, `for` (in these senses), `by` (passive agent), `do not`, `was` in "was helping" are **signal words**: they trigger a feature or select an argument, then *disappear* in Phase 2.

Worked example: `John filled the container with water.` — look up `fill` in the ontology: its theta grid has an Instrument argument signalled by `with`. So `water` becomes the Instrument. There is *no word "with"* in Phase 2.

Contrast — **relations that stay as words.** There is an ontology relation `with`, but it means *accompaniment or possession*, not instrument; there is a relation `from`, but only for *time*; `for-C` means "concerning/as for" (topic), not beneficiary. Example *(source)*: `For-C the animals John took 10 strong animals` = "As for the animals, John took 10 strong ones".

### Reading a theta grid

Hover over / open the verb in the ontology. Example *(source)*: `speak-A`'s patient is the thing spoken *about*, so you write `John spoke about X`, **not** `John spoke several words` — for that use `John said several words`. Optional arguments appear in parentheses in the grid: `(Source NP)` is optional. For `speak-A` only the Agent is required, so `John spoke` is complete.

If a verb lacks an argument you want (e.g. a Beneficiary — "almost always we can add a beneficiary argument to any verb"), ask the ontology maintainers rather than abusing a preposition.

### Relations: adverbial by default

A **relation** with a noun argument (`during the day`, `in the house`, `because of the storm`) or a clause argument (`[while Mary was in Bethlehem]`) **modifies the verb**, never a noun.

❌ `The mouse in the house was small` — means the mouse was small *when it was in the house* (implying it is bigger elsewhere).
✅ `The mouse [that was in the house] was small` — the relative clause modifies `mouse`.

Same with `John talked to the man inside the house later outside the house`: both phrases modify `talked`, so John is inside and outside the house at once. To attach to the man: `the man [who was inside the house]`.

## 6. Heads of structures

The **head** of a phrase is the word everything else in the phrase modifies. If a head is marked implicit, **everything inside its phrase is implicit too**. TBTA's structure is flat and linear:

```
A big man was eating food
{NP {AdjP big} man} {VP eat} {NP food}
```

So if `man` is implicit, `big` goes too. Therefore:

❌ `the man _implicit [who saw the soldier]` — if the translator turns implicit info off, the literal clause "who saw the soldier" vanishes with its head.
✅ Don't mark a head implicit when a modifier inside it is literal text.

This is the reason for the "reversed" notations `_explainName` / `_dynamicExpansion` / `_literalExpansion` (file 04): `Cana named a town _implicitExplainName` keeps the literal head `Cana` safe, and TBTA reverses it to `<<a town named>> Cana` on generation.

Worked example *(source, Proverbs 26:6)*: the author wanted "a person who sends a fool" to be implicit-ish. He first marked `A person _1implicitNecessary [who sends a foolish person …]` — then realised the relative clause is literal text inside that NP, so the head must **not** be implicit. Corrected: remove the `_implicitNecessary`.

## 7. The nine clause types

Seen in the analyzer's feature list for a clause boundary:

| Type | Example | Notes |
|---|---|---|
| **Independent** | `John saw Mary` | The main clause. **Never bracketed.** |
| Coordinate independent | (not used in analysis) | TBTA may *generate* it by joining two sentences |
| **Restrictive thing modifier** (relative clause) | `the man [who fell] died` | modifies a noun; narrows it down |
| **Descriptive thing modifier** | `David [who was the king of Israel] attacked…` | adds extra info |
| **Event modifier** (adverbial clause) | `John saw Mary [while Mary was in Mary's house]` | begins with a relation: `while`, `because-A`, `when`… modifies the outer verb |
| **Agent** (subject complement) | `[People do stupid things] is-V bad` → "It is bad that people do stupid things" | only with `be-V`, `seem-B`, `please-B` |
| **Patient** (object complement) | `John knew [Mary was in the town]` | the clause is the patient of the verb |
| **Attributive patient** (adjectival object complement) | `Mary is angry-B with John` ; `John is able [to go to Mary's house]` | the clause lives *inside* an adjective phrase |
| Closing quotation frame | (not used; may be removed) | |

Restrictive vs descriptive: by default relatives on a **common noun** are restrictive and relatives on a **proper noun (level 4)** are descriptive. Override with `_descriptive` / `_restrictive` (e.g. `that person [ _descriptive who lived in Bethlehem]`; `the God [ _restrictive who hears us(people)]`). Relative clauses with possessives (`whose`) are not allowed: `the man [who had a black cat]`.

**Because-A vs because-B:** `because-A` takes a clause (`[because Mary was in her house]`); `because-B` takes a noun (`because of that storm`).

### Why `able` inside `able-B [to see …]` matters (a worked example) *(source)*

> `But during the day _significantTime [while Mary was in Bethlehem] John was often able-B [to see [Mary was in Mary's big house]].`

Structure, flattened:

```
But
{NP during day}                      ← relation NP, role "not applicable"
[while {NP Mary} {VP be} {NP in Bethlehem}]
{NP John} {AdvP often} {VP be}
{AdjP able-B [ {NP John} {VP see-C [ {NP Mary} {VP be} {NP in big house of Mary} ]} ]}
```

Lessons embedded in that one sentence:

1. `able` takes a *clause* inside its adjective phrase, so you cannot mark `able` implicit without marking the whole clause implicit — you'd be left with "…John is often". Use `_implicitNecessary` on `able` if needed.
2. `-B` on `able` selects circumstantial ability. `able-A` = personal ability. Both have the same argument structure, so the analyzer cannot guess; the tag helps P2.
3. `see-C` ("see that…") takes a patient clause. The analyzer chose it automatically because a clause follows.
4. `_significantTime` fronts "during the day" in English output.
5. English generation reorders freely (the back translation put "often while she was in Bethlehem" at the end). That's fine: Phase 2 carries features, not word order.

## 8. Signal words in more depth

| You write | Triggers |
|---|---|
| `to` + noun (verb has a destination) | Destination argument |
| `from` | Source |
| `with` (instrumental) | Instrument |
| `for` (benefit) | Beneficiary |
| `by X` in a passive | X is the active agent |
| `do not go` (in an imperative) | negative polarity on `go` |
| `was helping` | background/imperfective feature on the clause. Default reading = *background information*; if you mean *imperfective* (extended over time), write `was helping _imperfective` |
| `began / started` + verb | inceptive aspect (**not** a separate verb) |
| `stopped` | cessative aspect |
| `finished` | completive aspect |
| `continually` | continuative aspect |
| `probably` / `certainly` / `might` / `might not` / `must` / `should` / `should not` / `must not` / `may` | mood/potential features |

There is also a *verb* `begin` (only an Agent argument): `That day began.` / `A war began.` — not "the action of X begins".

**Preposition retained:** for the locative `be-F` (and `have`), the preposition stays in Phase 2 because so many are possible: `John was in Cana`, `at that place`, `on the ground`.

## 9. Summary of the model (memorise this)

* The sentence is the basic unit. It has a **main clause** (verb + agent; never bracketed).
* Other clauses: relative, event (adverbial), patient (object complement), agent (subject complement), adjectival complement — all bracketed.
* Optional pieces: conjunctions, adverbial phrases, event clauses, relations with noun arguments.
* **Event clauses and noun-argument relations modify the verb.** To modify a noun, use a relative clause.
* Verb and adverb phrases never contain modifiers. Noun phrases can contain adjectives, other NPs with relations (`man named John`), and relative clauses.
* If a head is implicit, its whole structure is implicit.

## 10. Common mistakes — worked examples *(source)*

**A. A prepositional phrase meant for a noun**

❌ `John talked to the man inside the house later outside the house`
✅ `John talked to the man [who was inside the house] later outside the house`

**B. A relative clause bracketed as a patient clause**

❌ `John saw [the man that was in the house]` — the word `that` is the clue that this is a *relative*.
✅ `John saw the man [that was in the house]` (see-A, noun patient)
✅ `John saw [the man was in the house]` (see-C, "saw that the man was in the house"). Writing `John saw [that the man was in the house]` was the old style; discouraged because the analyzer reads `that` as a demonstrative.

**C. A patient clause that does nothing**

❌ `John saw the man [was leaving]`
✅ `John saw [the man was leaving]` → "John saw that the man was leaving".

**D. Gluing independent clauses**

❌ `John went to Mary [and talked to Mary]` / `John went to Mary [and John talked to Mary]`
✅ `John went to Mary. And John talked to Mary.`

**E. Implicit head with literal modifier** — see §6 (Proverbs 26:6).

**F. The Proverbs 26:6 literal/dynamic pair** — the full phase 1 given in the source:

```
(literal) A person _1implicitNecessary [who sends a stupid/foolish person _2 [so that a stupid/foolish person _2 would take a message to another person _3implicit]] is like a person _4 [who cut-off _present a person's _4 feet] [or who drinks violence].
```

and the generated English with the marking removed: "A person who sends a foolish person so that he would take a message <<to another person>> is like a person who cuts off his feet or drinks violence". Note the `_1 _2 _3 _4` noun-index notes (file 04), and that a dynamic alternate is needed because "drinks violence" would not be understood by all readers: "(dynamic) A person who sends a foolish person … causes himself to have trouble. (dynamic) He is like a person who cuts off his feet."
