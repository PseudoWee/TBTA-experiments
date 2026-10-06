<!-- Copy of phase1-handbook/03-rules-checklist.md. Rule numbers here (0.1-0.53, §1-§35) are the HANDBOOK numbering, not the original +02 PDF's; see the crosswalk below. Cross-references to "file 02/05/07" mean the other files in phase1-handbook/. Keep this copy in sync with the handbook. -->

# 03 — The Phase 1 rules checklist, grouped and explained

Source: "+02 Phase 1 Checklist of Essential Information", with the repo's `phase1-rules.md` for exact wording. Numbers (0.x and §n) are shown in bold; they are renumbered into a running sequence — see the crosswalk below.

**How to use this file.** Skim it once end to end. Then use it as a lookup: each theme lists the rules, a correct/incorrect pair, and the *reason* (almost always a consequence of the grammar model in file 02). Where He1 differs it is noted as **He1:**.

> Reminder of the He1 relaxation: no brackets; first/second-person pronoun referents only on the first occurrence in a verse; `<<…>>` / `<…>` for implicit; complex words may be left bare; object-complement clauses and imperatives can be worded naturally. Everything else still applies.

> **Numbering note (read this if you compare with the source PDF or the repo skills).** The source checklist has two items numbered 0.3, skips 0.35 and 0.46, and has no §27. This handbook **renumbers everything into one running sequence: 0.1–0.53 and §1–§35**. Crosswalk (old source number → handbook number):
>
> | Source (+02) | Handbook |
> |---|---|
> | 0.1 – 0.3 (first 0.3 = hyphenated words / default tense) | 0.1 – 0.3 (unchanged) |
> | 0.3 (second: one verb per clause) | **0.4** |
> | 0.4 – 0.34 | **0.5 – 0.35** (+1) |
> | 0.36 – 0.45 | unchanged |
> | 0.47 – 0.54 | **0.46 – 0.53** (−1) |
> | §1 – §26 | unchanged |
> | §28 – §36 | **§27 – §35** (−1) |
> | −1.x, 2.1, 3.1, 13.1 | unchanged |
>
> The repo's `phase1-rules.md`, skill files, and checker rule messages still use the **source** numbering (e.g. `checker:35` "all of" is source 0.17 = handbook **0.18**).

---

## A. Before you write: the meaning checklist (−1.x)

| # | Rule | Example / note |
|---|---|---|
| **−1.1** | Every bit of the literal text must be represented somehow. | Don't drop the opening clause of a verse — see lessons file 07 (2 Samuel 21:6). |
| **−1.2** | Add implicit information if it clarifies, sparingly. | `(implicit-situational)` sentences supplying a causal chain. |
| **−1.3** | Mark as implicit everything that is *not* literal text — but never mark literal text (or its representation) implicit. | See the head-of-phrase trap, file 02 §6. |
| **−1.4** | Check meaning in NIV, NASB, ESV (sometimes RSV/NRSV). Disagreement → prefer the SIL Translator's Notes (TNN); if none, the UBS Handbook. If translations agree with each other and the Handbook but not the TNN, follow translations + Handbook. If translations agree but both references disagree → judgment; add a note like `_analysisNoteSeeTNN`. Use meaning alternates only if the difference matters. | |
| **−1.5** | Greek *aner* / Hebrew *'ish* = male person. Greek *anthropos* / Hebrew *'adam* = often "person". Use `man` only if context says male, otherwise `person`. | `anthropos` in a generic proverb → `person`. |

---

## B. Pronouns, determiners, reference

### B1. No third-person pronouns — **0.1, §3**

* ❌ `John talked to Mary. He loved her.`
* ✅ `John talked to Mary. John loved Mary.`
* First and second person pronouns and `each-other` **must** carry a referent in parentheses: ✅ `I(John) talked to Mary`; ✅ `You(followers) are my(Jesus) followers`.
* Referent when several people: list **one** — ✅ `The Pharisees said to Peter and John, ["You(Peter) are foolish"]`; ❌ `you(Peter and John)`.
* Pairing as referent is now allowed: ✅ `you(followers/disciples)`. But if the complex pairing was used earlier in the verse, use the simple term in the parentheses (§3): `Jesus said to Jesus's followers/disciples, ["You(followers) are my(Jesus's) followers/disciples"]`.
* Do not put a sense letter in the parentheses: ✅ `you(son)`, not `you(son-C)` (if needed: `you(son) _C`).
* First-person plural: `_incl` (including the hearer, **default — never required**) or `_excl`: `Peter replied to the Pharisees, ["We(Peter) _excl are not stupid/foolish"]`.
* **The pronoun-generation rule.** TBTA decides when to turn nouns into pronouns; you never do.
* **He1:** write the first pronoun in the verse the full way so the AI knows the referent; afterwards pronouns are fine.

### B2. "a / the / that / this" — **0.11, §3.1**

| Word | Use |
|---|---|
| `a` (`some` plural) | first mention: `Then a man came to Bethlehem from Jerusalem` |
| `that` | later mention (preferred over `the`, because many languages lack a definite article): `Then that man went to the house…` |
| `the` | frame-inferable referents (`the king`, `the land`, `the town` in context), or after several `that`s. Optionally note `_frameInferable` on the first one. |
| `this` | newly referred to / special emphasis / in sight / the current book: `A man came. That man was tall. Then another man came. This man was short.` |
| no article | generic: `People like [to eat]`; singular generic: `bad-B action = sin` |

* ❌ `And John saw that man [that Mary was with]` — don't put `this/that` before a noun with a restrictive relative clause; `that` already defines it.
* In P2, `a` → "First Mention" tracking; `that` → "Routine" + "Contextually Near"; `this` → "Routine" + "Near with Focus".

### B3. Same noun, same wording — **0.36, §3.1**

❌ `Paul gave letters to those men [so that those men would read THOSE LETTERS]`
✅ `Paul gave letters to those men [so that those men would read LETTERS]`

Reason: target-language word order is unknown. If the subordinate clause comes first in the output, "those letters" would appear before the letters are introduced. (Second and later *coordinate* noun phrases and *subordinate clauses* may be assumed to come after the first because same-type structures keep their order.) He1: pronouns are acceptable.

### B4. Genitives — **§13.1, §27**

The "generic genitive" means "some relation between two nouns": `John's house`, `town of Judah`, `army leader`. English output picks Saxon/Norman/pre-posed form. You may write `of`.

But Bible-English genitives often mean something TBTA's genitive doesn't: `faith of Christ` could be "Christ's faith" or "faith in Christ"; `knowledge of the Son of God` (Eph 4:13) means knowledge **about** him. ❌ don't write these as genitives; ✅ expand: `[people know the Son of God]`-style wording.

### B5. "named" — **0.24**

❌ `the nation of Israel` ✅ `the nation named Israel`. Same for cities, rivers, etc.

---

## C. Words and vocabulary

### C1. Simple words only; complex words via pairing/explication/alternate — **0.2, §1, 0.31**

See file 05. Short version:

* ✅ `son/descendant` (pairing — simple first) · ✅ `hard hat` (explication for *helmet*) · ✅ `(complex) Mary had faith in God. (simple) Mary trusted in God.`
* ❌ bare `helmet`, `prophet`, `donkey`.
* **0.31:** whichever reading the target language uses, the sentence must make sense. Both `friends/brothers-D` and `friends` must fit.
* **Look the word up before using it.** If unsure of the level: ontology search.

### C2. Hyphenated ontology words stay hyphenated and uninflected — **0.3, 0.27, §1**

* ✅ `John stand-up` ❌ `John stood-up`
* ✅ `John take-away _future Mary's food` (tense via note)
* Default tense is `discourse` (English past, but may be present etc. in other languages). To get present: `stand-up _present`. Writing `went` instead of `go` already signals discourse; `John and Mary go` signals present.
* Exceptions exist (e.g. `in order to` may be written with or without hyphens).
* Capitalise only sentence/quote starts and proper nouns: ✅ `king`, ❌ `King` mid-sentence (the checker may read it as an unknown proper noun).

### C3. Adding a word — **§1**

* Any LDV word is allowed in principle — flag a missing one with `_inLDV` (e.g. `the measure _inLDV`).
* Not used even though common: `really` → use `actually` or `truly`.
* Proper nouns are always allowed (some kinds of people go as "people of X"; some nouns need a type: `tree-*`, `mount-*`).
* Complex words may be added if they significantly improve translation **and** have a pairing or explication, typically 20+ occurrences in the Bible (exceptions exist). New words get an entry in the complex-terms table.

### C4. Sense letters — **§2**

TBTA picks the lowest-lettered sense whose argument structure fits. Only add a letter when you know the right one and P2 might get it wrong.

* `John knows the law` → `know-A` (be familiar with). ⚠️ If you mean "know the content", write `John knows-C the law`.
* `John knows about the law` → automatically `know-D`.
* `Yahweh sees all things` — to mean *events* not *objects*: `things-B`.
* ❌ Don't add letters the computer can infer; reviewers must then verify them.

### C5. Banned or restricted words

| Word | Rule | Fix |
|---|---|---|
| `can` | **0.25, §2.1** | `is able [to …]`. `able-A` = ability, `able-B` = circumstance: `John is able-B [to eat with Mary] [because Mary is in the town]` |
| `could` | §2.1 | OK only inside `so that … could`: `X did a thing [so that X could …]`. Otherwise `be able [to …]`. |
| `going to` (future) | **0.29** | `will`: `John will see Mary` |
| `even`, `any`, `own` | **0.17, §17** | Omit. `John did not eat any apples` → `John did not eat an apple`. For emphasis: `_emphasized`. `even-if` and `even-though` *do* exist as relations. |
| `all` | **0.18, §19** | `all of` unless generic: `all of those people`, `All of Jesus's followers were at that place`; but ✅ `God loves all people` (generic). |
| `only` (adverb) | **0.33** | Allowed now as `only-A` (exclusivity): `John only prayed in the temple`. Low-esteem "only" still needs the adjective: `helped only-B a few people`. |
| `now` | §23 | Only the adverb "at the present time" (`Let's look at the function of verbs now`). Not the discourse marker "Now, let's…". |
| `way` | §35 | Avoid. In relatives it fails (`the way [that the lilies grow]` has no grammatical function for `way` inside). |
| `obey` vs `follow-B` | **0.48** | `obey` / `obey/submit` for laws and instructions; `follow-B` for following people. |
| `give` vs `offer` | **0.49** | `give` for sacrifices; `offer` means "ask someone if they want something". |
| `make` + adjective | **0.45** | ❌ `X made Y good` ✅ `X caused [Y to be good]` (He1: `X caused Y to be good`) |
| `answer` | §12 | Only when someone answers a question; otherwise `reply`. |
| colon `:` | §20 | Use a period. |
| `both A and B` | **0.46** | Not supported. `both` only with a dual noun: `both men _dual`. |
| participles/gerunds as nouns | **0.32** | ❌ `Teaching is fun` ✅ `[A person teaches people _implicit] is-V fun` (He1: `It is fun that a person teaches <<people>>.`) |
| English-only idioms | **0.38** | ❌ `in prison` ✅ `in a//the//that prison`. Idioms (only understood by one culture) aren't used; metaphors are OK if likely understood, with an alternate if they might not be. |
| `X-ed` forms of hyphenated verbs | **0.27** | see C2 |
| `listen`, `look-A` with no patient | §34 | Give them a (possibly implicit) patient. Exception: `listen/behold`, `look/behold`. |

---

## D. Clause structure and brackets

### D1. One verb per clause; bracket every subordinate clause — **0.4, §4**

* Count verbs; each verb is a clause. Auxiliaries (`do` in `do not go`, `will`) are not verbs.
* Main clause: **never** bracketed. Everything else: bracketed.
* Brackets must balance: add 1 per `[`, subtract 1 per `]`; total 0.
* Exceptions: answers to questions (may be a word or phrase). Quote openings — see §F.

Example of counting levels *(source)*: `John saw [Mary was eating with the man [who went with Mary [in order to see Paul]]]` has **three** levels of embedding. `The man [who saw Mary] knew [Mary went with Paul]` has only **one** — the two subordinate clauses are siblings.

### D2. Maximum four levels of embedding — **0.5**

Four is allowed but "strongly discouraged"; at four, break the sentence into several. **He1:** keep sentences from getting complicated even though you can't see the brackets.

### D3. Place event clauses and adverbial phrases correctly — **0.6, §5**

❌ `We(people) know [Jesus died] because of our(people's) _incl bad-B actions` — this says we know *because of our sins*.
✅ `We(people) know [Jesus died because of our(people's) _incl bad-B actions]`.

### D4. Noun-modifying phrases go in a relative clause — **0.7, §5**

❌ `John talked to the man previously in Bethlehem` (while in Bethlehem, John talked to the man)
✅ `John talked to the man [who previously was in Bethlehem]`. He1: same wording, no brackets.

### D5. Relative clauses — **0.8, 0.9, §6**

* Start with a relativizer (`who`, `whom`, `that`): ✅ `the man [who was in the house]`, ❌ `man in the house`.
* **Never** `when` or `where` as a relativizer: ❌ `The time [when John saw Mary] was late` ✅ `The time [that John saw Mary at] was late`; ❌ `the place [where I(Paul) lived]` ✅ `the place [that I(Paul) lived at]`.
* Keep the stranded preposition: ✅ `reason [that John left FOR]`, `time [that John left AT]`.
* `when` is fine for **adverbial** clauses (`I(Paul) was happy [when I(Paul) was with you(Timothy)]`) and as a question word. `where` is *only* a question word.
* Often you can drop the `place`/`time` noun: `the camp [that I(Yahweh) live in]`.
* ❌ possessive relatives: `the man [whose cat was black]` → ✅ `the man [who had a black cat]`.
* Restrictive vs descriptive: see file 02 §7.
* **Object-gap relatives** (the head noun is the missing patient inside the clause) sometimes need their own bracket nested inside the head noun's — see lessons file 07.

### D6. Patient (object-complement) clauses — **0.8, 0.10, §7**

Omit the complementizer `that`; open the bracket right after the main verb; do not repeat a noun that is understood to be shared.

| Situation | Write |
|---|---|
| subject of the clause = subject of main clause | ✅ `John wanted [to eat food]` ❌ `John wanted [John to eat food]` |
| subject of the clause = patient of main clause | ✅ `John wanted [Paul to eat food]` ❌ `John wanted Paul [Paul to eat food]` |
| unrelated | ✅ `John knew [Paul was eating food]`; ❌ `John knew [that Paul …]` |
| the sense of the verb allows an arbitrary patient | ✅ `John told Paul [John will go to the town]`, `Mary showed John [John was wrong]` |

Reason for omitting `that`: the analyzer reads it as a demonstrative.
**He1:** write it naturally: `John knew that Paul was eating food.`

### D7. "and" before a subordinate clause — **0.23, §25, §31**

`and` may start a subordinate clause **only** if it is the last of a *series of the same type*:
✅ `The man [who was in the house] [and who knew Mary] left` (two relatives)
❌ `The army came to Jerusalem [and defeated the Jews]` (that's an independent clause)
✅ `The army came to Jerusalem. And the army defeated the Jews.`

Also (§25): don't start a restating sentence with "And". `Paul did some things. Paul cooked a meal. And Paul served that meal to John.` — the second sentence *explains* "some things", so it must not begin with "And".

### D8. Begin/start/stop/finish/continue — **0.20, §21**

✅ `John started talking to Mary` ❌ `John started [talking to Mary]`. They trigger features (inceptive/cessative/completive/continuative) on the next verb.

### D9. No isolated noun phrases — **0.22**

❌ `The next day [rest]`, ❌ sentence-initial `The next day …`
✅ `On the next day, …`. Every noun must be a verb argument or follow a relation.

### D10. "to" — **0.26, §8**

* Not at the start of an event/adverbial clause. ❌ `John went to Mary's house [to talk to Mary]` ✅ `John went to Mary's house [in order to talk to Mary]`. (He1: bare `to` tolerated, `in order to` preferred.)
* ✅ allowed at the start of a patient clause when the verb takes a same-agent clause: `John wants [to meet Mary]`.
* No generic `to` relation: only use `to` + noun if the verb has a Destination argument.

### D11. One direct object — **0.28**

✅ `John gave a gift to Mary` ❌ `John gave Mary a gift`.

### D12. Coordinates — **0.21, §22, §28, §29**

* Commas after all but the last item, `and`/`or` before the last: ✅ `an apple, a pear, and a peach`.
* A modifier meant for several coordinated nouns needs `_coordinate` or repetition:
  * adjective: `black _coordinate dogs and cats` — but for first mentions write `black _coordinate a dog and a cat` (not `a black _coordinate dog and cat`).
  * noun modifier: `the soldiers and the horses of _coordinate the king` (Norman genitive, modifier at the end).
  * relative clause: `boys and girls [ _coordinate _descriptive that God loves]`.
* Coordinate verbs are experimental and strict: no patient or source argument; every oblique argument applies to all. ✅ `Jesus was born and grew`, `The man died and fell`. ❌ `Peter cooked and ate the food`; ❌ `John ran from Paul and fell`; ❌ `John died and fell on the ground`.
* Coordinate relative clauses/subordinates: last one gets `and`, `or`, or (sometimes) `but`: `a man [who was very big] [but who was not very strong]`.

### D13. Referents of passives and "same agent" verbs — **0.37, §24**

Many languages have no passive and TBTA converts it to active, so the passive must be convertible.

❌ `John went to Bethlehem [in order to be seen by the Pharisees]` → active `…[in order to the Pharisees see John]`, where the subordinate agent isn't John, which `in-order-to` forbids.
❌ `John tries [to be seen by Mary]` (same-agent verb).
✅ `John tries [to see Mary]`.
✅ `John knew the man [who was hit by Paul]` (relative clauses can be agent or patient).
✅ `John know-how _present [houses are built by people _implicitActiveAgent]` — `know-how-B` doesn't require same agent.
Same-agent senses include `know-how-A`, `want-B`, `like-B`.

### D14. Only a patient-taking verb passivises — **0.47**.

---

## E. Tense, mood, aspect, modality

### E1. Perfect tense — **0.16, §18**

Allowed only if both "recently" and "previously" would be adequate paraphrases: ✅ `John has gone to Mary's house`, ✅ `you have believed in Christ` (Paul to new believers). ❌ `God has chosen [us to be God's people]` — may be the eternal past; use `God chose …` or expand: `We(people) are God's people [because God chose [us(people) to be God's people]]`. Past perfect: only if the simple past with or without "already" works. TBTA encodes the perfect as the "flashback" feature.

### E2. "would" — **§16**

Only in specific constructions:
* `[If-A John will go to Bethlehem] John will see Mary` (future conditions)
* `John went to the town [so-C that John would see Mary]`
* `[If-B _hypothetical John were to read that book] Mary would read that book`
* `[If-C _counterfactual John had read that book] Mary would have read that book`
You cannot write a stand-alone `John would go to Bethlehem`. `if-A` is not used for past events (yet).

### E3. Negation and causes — **0.34**

Avoid `not` + `because` / `so-A` / `so-C`. `The office did not hire Jane because Jane is the boss's daughter` has two opposite readings: (1) the reason it hired her was *not* that; (2) because she is the daughter, they did *not* hire her. Allowed if context decides (`even though that friend won't get up to give something to you because you are his friend` — obviously "not because") or if avoiding it is too awkward. The checker raises `checker:48` as a *warning*; treat as a judgement call (file 07 / 09).

### E4. Causality words — **§8**

| Word | Meaning |
|---|---|
| `cause`, `make`, `force` | verbs |
| `so`, `then-D`, `therefore`, `for` | conjunctions |
| `because-A` (clause) / `because-B` (noun) | relation |
| `in-order-to` | **intent; same agent** in subordinate and main clause |
| `so that … would` (`so-C`) | intent, different agent OK |
| `so that … could` (`so-A`) | ability |
| `so-B` | consequence **without** intent (unintended) |

English `to` often means `in order to` — spell it out.

### E5. Mood signal words — see file 02 §8 (`must`, `should`, `might`, `probably`, `certainly`…).

### E6. "when" ↔ "after" — **0.39**

`[After John saw Jesus] John was happy` — use `after` when the main action clearly follows.

### E7. Rhetorical future (prophetic perfect) — file 04: use `_unknownFuture` etc. when you know which future.

---

## F. Quotations, speech and discourse

### F1. Introduce every quotation — **0.13, §10**

`John said, ["…"]`. If the speaker and verb are implicit: `X _implicitNecessary said _implicitNecessary, ["…`. A quote may open a sentence if earlier wording signalled it: `X said the following words. _verseBoundary "quotation"` / `X spoke to Y. _verseBoundary "quotation"`.

### F2. Bracket the first sentence of a quote — **§10**

The first sentence is the *patient clause* of `said`:

* single: `Richard said, ["I(Richard) love you(Mary)"].`
* multi-sentence: `Richard said, ["I(Richard) love you(Mary)]. So I(Richard) want [to hold your(Mary's) hand]."`
* One opening quote mark at the very start and one closing mark at the very end of a multi-paragraph quote; always double quotes, even when nested; no single quotes (TBTA adds them for `called`, `means`).
* Place the period at the end of the whole sentence (outside the `"`); `?` and `!` go inside.
* Indented text in the NIV that is really a quotation must be written as a quotation.
* Quote openings need a comma before: `that person said, ["I(person) will …`.

### F3. `answer` vs `reply` — **§12**: `John said, ["I think [you(Paul) are bad"]]. Paul replied, ["I(Paul) am not bad!"]`.

### F4. Titles and paragraphs — **§11**

`(title)` at the start of a title (present tense; independent of the text; ideally one sentence; a noun phrase is acceptable). Paragraph break: `_paragraph` in P1 (`(paragraph)` in the back translation). `(title)` is always followed by `(paragraph)`, even in poetry where the NIV doesn't show one.

### F5. Poetry — **0.52**

`(begin-poetry)` … `(end-poetry)` (also accepted: `(poetry-begin)`/`(poetry-end)`), `(blank-line)` between sections where the NIV has a blank line. Non-poetry block quotations are *not* poetry — use quote marks. `(poetry-begin/end)` are internal to a sentence and repeated across alternates; `(paragraph)` and `(blank-line)` are external and are not.

### F6. Conjunctions — **§31** (guidelines, not rules)

* A second sentence restating the first: **no** `And`.
* Joining: put `And` at the start of the sentence that should combine with the previous *of the same type*. For A, B, C where B and C should combine, put `And` on C only (otherwise A+B may combine).
* Contrast → `But` (regardless of what the NIV says); no `But` if not contrastive.
* Break runs of `And` with `Then`/`Then-C` (immediate succession) or `Then-D` (consequence), and bare sentences.
* A second rhetorical question starting `Or` normally pairs with a statement starting `And`: `Should you steal things? OR should you kill people?` → `You should not steal things. AND you should not kill people.`
* After finishing a passage, read it aloud for flow.

---

## G. Imperatives, jussives, prayers, questions

### G1. Imperatives — **0.19, §15, 0.50**

`You(John) (imp) go to that town` → "Go to that town". To address by name: `John, you(John) (imp) go to the town` (name twice). He1: write as the English output.
Imperatives with epistemic verbs (know, understand, realize) and emotions (`You(people) (imp) be happy`) are now allowed.

### G2. "Let's", jussive, prayer — **§15**

| Meaning | Write |
|---|---|
| Let's go | `We(Peter) _incl go _suggestiveLets to the town` |
| Let Peter go (command to a third person) | `Peter (jussive) go to the town` |
| Let Peter go (permission) | `You(people) (imp) let [Peter go to the town]` |
| May Peter go (prayer/hope) | `I(John) pray-hope [Peter will go to the town]` |

### G3. Rhetorical questions — **0.15, §13, §32**

Always followed by a statement version:

```
(yesrhetorical) Did you(John) speak to Mary? (statement) You(John) spoke to Mary.
```

* `(yesrhetorical)`: expected answer yes (Greek *ouch*); write the verb **positive** even though English often negates it.
* `(norhetorical)`: expected answer no (Greek *me*).
* `(rhetorical)`: debatable.
* Optional sub-type note after `(yesrhetorical)`: `_persuasive` (Matt 7:22 "Lord, Lord, didn't we prophesy…"), `_accusatory` (Gen 3:11), `_assertive` (Luke 22:49), `_reflective` (Gen 18:17), `_emphatic` (1 Sam 1:8), `_instructional` (Matt 6:25). Context decides; skip if unsure.

### G4. "which" — **0.41**: `What` → `which thing-A`; prefer `which thing` with the intended sense. `which` is now also permitted in non-questions: `John did not know [which house Mary was living in]`.

---

## H. Implicit information and notes

### H1. Implicit marking — **0.12, §9**

| Target | Notation |
|---|---|
| word/phrase (not grammar-required) | `word _implicit` |
| word grammar needs (subject, verb, anything the sentence needs to make sense) | `word _implicitNecessary` |
| passive agent | `by X _implicitActiveAgent` |
| whole clause/sentence | `(implicit-situational)` etc. (file 04) |
| He1 | `<<…>>` regular, `<…>` necessary, `<<by X>>` for passive agent |

* Mark implicit sparingly; "anything helpful for interpretation and most likely to be true".
* The mark applies to the **phrase** containing the word before the underscore — it removes modifiers too (file 02 §6).
* An adjective phrase or adverb phrase can be implicit without making the noun/verb implicit.
* Put a clause's implicit marker *after* a few words in a subordinate clause (`while John (implicit-situational) was in the town`) — easier for P2. Whole-sentence implicit: put it in front.
* Implicit clauses make **everything inside** implicit (nested clauses included).

### H2. Passives need agents — **0.14, §13**

`John was hit by a soldier`; if the agent is not in the text: `John was hit by a soldier _implicitActiveAgent`. Passives are encouraged when the literal text is passive, especially to avoid saying God is the agent: `Those people will be destroyed by Yahweh _implicitActiveAgent`. Change to active when passive makes a complex construction hard to read.

### H3. `let`/`allow` with God as agent — **0.43**

❌ `You(Moses) (imp) do not allow [the people to be destroyed by Yahweh _implicitActiveAgent]` — converted to active it says "Do not allow Yahweh to destroy the people", which is inappropriate.

### H4. Names and expansions — **§14** (see file 04 for full detail)

`_explainName` / `_implicitExplainName`, `_dynamicExpansion`, `_literalExpansion` — written *reversed* so the literal word survives when the implicit one is removed.

### H5. Alternate order — **§26, §30**

Order, most literal first: literal rhetorical complex → literal rhetorical simple → literal statement complex → literal statement simple → dynamic rhetorical complex → … → dynamic statement simple. Simple immediately follows complex. At most four alternates per sentence; fewer is better. One-word differences: `dynamic_word|literal_word` — e.g. `destroy|swallow` — all features of both must agree.

---

## I. Apposition and misc

| Rule | Detail |
|---|---|
| **0.40** Apposition banned except for addressees | ✅ `Lord, my(David) God, you(God) are great`. ❌ `The Lord, my(David) God, is great`. Distinguish from a noun-noun relation (`army hat`). |
| **0.35** Avoid vague back-references | ❌ `did that action//thing` — say what happened. |
| **0.30** No double negatives | ❌ `No person does not love his mother` ✅ `All people love their mothers`. |
| **0.44** Use only the senses we have | |
| **0.51** `faith in X`, `relationship with X` | Prefer the noun-argument construction to a relative clause. |
| **0.53** Short/long time | `for a time-short-<unit>` / `for a time-long-<unit>` e.g. `for a time-long-years` (may generate "for many years"). |
| **0.42** Commas | Needed after an addressee, after `X said` + quote, in coordinate noun phrases. Elsewhere optional/no effect. |
| **0.21** | see D12 |
| **§33** Emphasis | `John _emphasized is tall` → "It is John who is tall". Time/place fronting: `In the past _significantTime John lived in Bethlehem`, `At Bethlehem _significantLocation John met Mary`. |
| **§35** `way` | avoid. |

### Bible references

Write `Isaiah 53:3` as is; P2 will fix it (not automatically analyzed). Special-relation phrasing: file 04.

---

## J. One-glance "most-often-broken" list (from real corpus statistics)

From the 2026-09-10 calibration of 200 random verses (282 errors, 287 warnings; 57 verses fully clean) the rules firing most were:

1. Verb argument structure / case frame (`checker:built-in:1`) — 154 messages.
2. Ambiguous part of speech (`built-in:8`) — 93, nearly all warnings: **tag the word** (`first _adv`).
3. Word not recognised in the ontology (`built-in:7`) — 84: typos, number words (`two` → `2`), proper nouns.
4. Level 2/3 word outside a pairing/explication/`(complex)` (`built-in:4`) — 83 errors. *This was the #1 error in the very first sample (85 of 241).*
5. Token syntax (`token:syntax`) — 23: missing spaces, malformed notation.
6. `all` → `all of` (`checker:35`) — 15 errors, a purely mechanical fix.
7. Nesting depth, ambiguous complexity, capitalisation, negative+purpose clause.

Details and fixes for each are in file 07.

---

## Companion documents (now in the TBTA-experiments repo)

The three documents this checklist refers to are on hand. Read the matching file instead of guessing:

| The checklist refers to | Read this in <https://github.com/PseudoWee/TBTA-experiments> | Use it for |
|---|---|---|
| "How to handle complex terms" (detail for rule 0.2) | [`skills/niv-to-phase1/references/complex-terms.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/skills/niv-to-phase1/references/complex-terms.md) (the 1,469-row lookup) and [`phase1-handbook/05-vocabulary-and-complexity.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/05-vocabulary-and-complexity.md) | Pairings, explications and `(complex)` alternates. Check the table first, then the ontology's `/simplification_hints` for anything it doesn't list (the live lookup wins on disagreement) |
| "Intro to TBTA grammar" (background for the bracket/clause rules) | [`phase1-handbook/02-grammar-foundations.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/02-grammar-foundations.md) | Words → phrases → clauses, semantic roles, why clauses are bracketed |
| "Summary of specialized notation" (underscore/implicit notation) | [`phase1-handbook/04-notation-reference.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/04-notation-reference.md) | Every tag, bracket and alternate notation |

Also useful: [`phase1-handbook/README.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/README.md) (reading order), [`07-lessons-learned.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/07-lessons-learned.md) (confirmed failure patterns) and [`06-checker-and-api.md`](https://github.com/PseudoWee/TBTA-experiments/blob/main/phase1-handbook/06-checker-and-api.md) (checker rule IDs). The original PDFs/spreadsheet live in the Claude Project "Presciencelabs".

If a case still depends on detail none of these resolve, flag it to the user rather than guess.
