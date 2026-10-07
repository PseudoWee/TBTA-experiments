# 04 — Notation reference (from "+03 Summary of Specialized Notation")

Every special tag, bracket and marker in one place. Anything after an underscore `_` is ignored by the analyzer but read by the Phase 2 person (P2). **Always put a space before the underscore** — `things _implicit`, never `things_implicit` (the checker raises "Notes notation should have a space before the underscore").

> Spelling matters in two ways. Some tag families match by *prefix* (the `_implicit…` family: a typo such as `_implicitActveAgent` still works by luck). Others need an *exact* match (`_literalExpansion`) and are **silently ignored** when misspelled — no error, no effect. Proofread tags by eye. (Lessons file 07.)

## 1. Quick lookup table

| You want | Notation | He1 |
|---|---|---|
| Implicit word/phrase | `X _implicit` | `<<X>>` |
| Implicit but grammar needs it | `X _implicitNecessary` | `<X>` |
| Implicit passive agent | `by X _implicitActiveAgent` | `<<by X>>` |
| Implicit clause/sentence | `(implicit-situational)` etc. | `<<…>>` |
| Imperative | `You(John) (imp) go` | `Go` |
| Let's | `We(P) _incl go _suggestiveLets` | natural |
| Third-person command | `Peter (jussive) go` | natural |
| Prayer/hope | `I(John) pray-hope [Peter will go]` | `May Peter go` |
| Inclusive/exclusive we | `we(P) _incl` / `_excl` | |
| Rhetorical question | `(yesrhetorical)` / `(norhetorical)` / `(rhetorical)` + `(statement)` | |
| Literal / dynamic alternate | `(literal) …  (dynamic) …` | |
| Complex / simple alternate | `(complex) … (simple) …` | |
| Pairing | `simple/complex` | complex alone OK |
| `null/X` pairing | generate nothing if X is unavailable | |
| One-word literal/dynamic | `dynamic_word|literal_word` | |
| Sense | `word-B` | |
| Part of speech tag | `word _noun` / `_verb` / `_adj` / `_adv` / `_adp` / `_conj` / `_part` | |
| Title | `(title)` | |
| Paragraph | `_paragraph` (BT shows `(paragraph)`) | |
| Footnote | `(footnote)` | |
| Parenthetical comment | `(comment-begin) … (comment-end)` | `( … )` |
| Poetry | `(begin-poetry) … (end-poetry)`, `(blank-line)` | |
| Biblical units | `(literalunits)` / `(modernunits)` or `modern/biblical` pairing | |
| New noun index | `_1`, `_2`, `_3`… | |

## 2. Implicit information in depth

### 2.1 Phrase-level (underscore after the word)

* `_implicit` — regular (a word not grammatically required).
* `_implicitNecessary` — required by grammar (verbs, non-passive subjects) or sentence makes no sense without it. The generator always generates these, but flags them (`<…>`, italics).
* Applies to the *whole phrase headed by that word* → see head rule, file 02 §6.
* Noun/verb/adjective/adverb phrases only. An adjective phrase can be implicit with its noun left alone, and vice versa for adverbs.

Examples:

| ✅ | ❌ |
|---|---|
| `John eats food _implicit` | `the man _implicit [who loved God]` when the relative clause is literal |
| `Mary is angry _implicitNecessary with John` (the adjective phrase contains `John`, so `John` goes too; role "not applicable") | `John is able _implicit [to go …]` (`able` heads a phrase containing the clause) |
| `Those people were killed by enemies _implicitActiveAgent` | `The enemies were killed _implicit` with no `by`-agent in a passive |

### 2.2 Clause-level (parenthesised tags)

If the tag sits in a main clause or in front of the sentence, the whole sentence is implicit. If inside a subordinate clause, only that clause (and what it contains) is.

| Tag | Use |
|---|---|
| `(implicit)` / `(implicit-info)` | generic |
| `(implicit-cultural)` | ancient-culture background |
| `(implicit-situational)` | inferable from the situation — **the most common** |
| `(implicit-historical)` | an earlier **event** (Ruth 4:17 "And David became the king of Israel" tagged historical) |
| `(implicit-background)` | background **information**, not an event (Matt 1:16 "People call Jesus 'Christ' because God chose Jesus to save His people") |
| `(implicit-subaction)` | an unmentioned step that *must* have happened between the stated events |
| `(implicit-argument)` | an implicit patient proposition of a verb |

Don't over-think the category. Example in a subordinate clause:
`John talked to Mary [while John (implicit-situational) was in the town]`.

**Worked example — implicit expansion (corpus, 2 Samuel 6:6).** The NIV's one sentence ("…Uzzah reached out and took hold of the ark of God, because the oxen stumbled") became four, two tagged `(implicit-situational)` spelling out the unstated causal chain (oxen stumble → wagon tips → ark starts to fall → Uzzah grabs it). The back-translation wraps those in `<<…>>`. That is a legitimate convention, not fabrication.

### 2.3 Special implicit descriptions on nouns (the "reversed" notations)

All three are written **reversed** relative to how they generate, so the literal noun survives if the implicit one is removed.

**Explain a name — `_implicitExplainName` (older: `_explainName`).** Only with the `named` relation. Used the first time a place, nation or person is introduced *in a book*.

* Write: `Cana named the city _implicitExplainName`
* Generates (implicit included): `<<the city named>> Cana`
* Without implicit info: `Cana` — still there, because it is the head.
* Also for people: `Jeremiah named a man _implicitExplainName`.

**Dynamic expansion — `_dynamicExpansion` (older `_explainMetonymy`).** For metonymy (someone is named who did not literally act). Used if the translator wants the dynamic reading.

* Write: `Herod of the soldiers _dynamicExpansion searched for Jesus`
* Generates: `<<The soldiers of>> Herod searched for Jesus`
* Literal rendering: `Herod searched for Jesus`.

**Literal expansion — `_literalExpansion`.** The literal text includes an extra noun many languages would drop; the expansion is included only in a literal translation.

* Write: `Yahweh of the eyes _literalExpansion see all things-B`
* Literal reading: "The eyes of Yahweh see…"; dynamic: "Yahweh sees…". The literal word is *not* implicit — it *is* the text.
* Correct placement matters (checker rule 49): `X of Y _literalExpansion`, not `X Y of _literalExpansion`.

Why not `the soldiers _implicit of Herod`? Because `soldiers` would be the head; removing it would also remove the literal `of Herod`.

### 2.4 Necessary implicit

`_implicitNecessary` is for any syntactic category that is implicit but required. It is *not* for optional items. Verbs and non-passive subjects need this notation to be considered implicit.

## 3. Pronouns and referents — see file 03 §B1 and §12 below

Extra from +03: when "we" has several people (`Jesus, Peter, and John`), list one: `we(Jesus) _incl`. Third-person forms standing in for first/second person: `the Son-of-Man _1stAs3rd` → BT `<<I, who am the>> Son of Man`; `my(David's) Lord _2ndAs3rd` → `<<you,>> my Lord`.

## 4. Quotes, comments, titles, footnotes

Quotes — see file 03 §F2. Comment: `(comment-begin)…(comment-end)` for text that is literally in parentheses in the NIV (e.g. Genesis 13:10 "(This was before the LORD destroyed Sodom and Gomorrah.)").

Titles: `(title)` — if more than one sentence, put `(title)` on each. Present tense. Independent of the text.

Footnote: `(footnote)` precedes it; **everything after it is the footnote** until the verse ends or another `(footnote)` starts; only at the end of a verse; no closing tag. Example (Mark 9:29):

```
And Jesus said to those followers/disciples, ["This kind of spirit will only leave a person [if you(followers) pray]"]. (footnote) Some copies/manuscripts _copyinLDV of this part of the Scriptures say, ["This kind of spirit will only leave a person [if you(followers) pray] [and if you(followers) do not eat food [so that you(followers) could pray]]"].
```

**Parenthetical comment ≠ footnote.** Both appear as `(…)` in English but they are different tags. Ask: *is it literally in parentheses in the NIV, or is it a note I'm adding?* The checker cannot tell you; both pass.

Questionable texts: P1 person decides. Options: regular text (John 7:53–8:11), include but mark as "Questionable Text" (a clause feature, may be anywhere in the verse), footnote (Mark 9:29), or omit (KJV 1 John 5:7–8).

Bible references: write as is: `Isaiah 53:3`.

The word "X": `the word gods`; for language-specific words: `The word of Aramaic named Abba means "father".` (Don't add quotes around the meaning in `means`/`called` constructions' generated single quotes.)

## 5. Alternates

TBTA has several families of alternates. Use as few as possible — "zero is optimal".

### 5.1 Literal / dynamic

`(literal)` first, `(dynamic)` second. Either or both may be generated depending on the audience switches (e.g. churched adult vs unchurched children).

Example from Proverbs 26:6 (file 02): `(literal) … drinks violence` vs `(dynamic) … causes himself to have trouble.`

### 5.2 Complex / simple (vocabulary alternates)

For **level 3** words (and any level 2/3 word when a pairing/explication isn't suitable). The only alternate allowed to span multiple sentences — tag *each* sentence.

```
(complex) Mary had faith in God.
(simple)  Mary trusted in God.
```

If the level-3 word exists in the target language, the complex version is generated; otherwise the simple one. `glory` is the textbook level-3: a sentence with it is often paired with an alternate using `wonderful/glorious`.

⚠️ `(alt)` is **not** a tag. The checker rejects it ("This clause notation is not recognized") — use `(complex)/(simple)` or `(literal)/(dynamic)`.

### 5.3 Meaning alternates (oldest kind)

For disputed interpretation or hard wording: `(primary)`, `(alternate-1)`, `(alternate-2)` … up to five. Use only where the difference matters.

### 5.4 Rhetorical alternates — `(yesrhetorical)` / `(norhetorical)` / `(rhetorical)` + `(statement)`. See file 03 §G3. In the English back translation use the same tags and explain the expected answer to the consultant in a comment where it first appears.

### 5.5 Units alternates

When units have different structures (hours "the third hour/9AM"; "talents/bags of gold" in Matt 25) a pairing can't work:

```
(literalunits) The time was the third hour [when those soldiers crucified Jesus.]
(modernunits)  The time was 9AM [when those soldiers crucified Jesus].
```

If the structure is identical and arithmetic converts (km/stadia, kg/shekel), use a **pairing**: `Bethany was about 3/15 kilometers/stadia from Jerusalem` (modern/biblical).

### 5.6 Order of alternates — file 03 §H5.

## 6. Pairings, complex terms, `null`

* `X/Y` — X simple (level 0/1), Y complex (2/3). Y if available, else X. Currently the analyzer ignores `/Y`; P2 sets it by hand.
* `null/X` — if X is unavailable, nothing is generated (including modifiers). Use when substituting a simple word wouldn't be acceptable: `friends/brothers-D <<and null/sisters-D>>` — don't want "and sisters" if the first noun becomes "friends".
* Referent parentheses with a previously-used pairing → use the simple term (file 03 §B1).

## 7. Sense letters — `-B` etc.

Only when you know the correct sense and P2 might err. Examples: five senses of `then` (`then-A` temporal succession is by far most common; if you mean `then-D` consequence, say so). The analyzer does not yet automatically interpret `-B`; P2 sees it and adjusts.

## 8. Relations with specialised functions

| Relation | Write as |
|---|---|
| Begin scene | `One day` |
| Title | `(title)` |
| body part | `Mary's hand` |
| composed of | `lake of fire` |
| generic genitive | `Mary's friends` / `friends of Mary` |
| group | `group of sheep` |
| iteration | `X does something three times` |
| kind-of | `kinds of animals` |
| kinship | `Mary's sister` |
| made-of | `house of bricks` |
| named | `town named Bethlehem` |
| nationality | `Hebrew man` |
| owner | `John's house` |
| part-whole | `the front of the boat` |
| quantity | `10 kilograms of wheat` (currently the analyzer prefers `wheat -30 kilograms`) |
| realm of authority | `king of the Israelites` |
| region of authority | `ruler of Israel` |
| subgroup | `some of the apples` |
| title (noun) | `king Herod` |

Optionally add a note for P2, e.g. `_regionOfAuthority`. Most relations act **adverbially** (about…, iteration); a handful modify nouns (made-of, kinship…).

## 9. Other special notation

| Notation | Meaning |
|---|---|
| `all-B` or `all _hyperbolic` | hyperbolic "all" (means "many"). BT shows plain "all". Example: `All-B the people [who lived in Judea] came [in-order-to hear Jesus]` |
| `_unknownFuture` etc. | which future tense; default future is "immediate", often wrong. Applies to the *rhetorical future* — prophetic perfect for events considered certain. |
| `_significantTime`, `_significantLocation` | front a time/place phrase in English |
| `_emphasized` | emphasis on agent/patient: `John _emphasized is tall` |
| `_coordinate` | modifier covers all coordinate nouns |
| `_descriptive`, `_restrictive` | override relative clause type |
| `_dual` | `both men _dual` |
| `_plural` | features plural, esp. mass nouns: `money _plural` |
| `_imperfective` | `was helping _imperfective` |
| `_present`, `_past`, `_future` | tense on hyphenated verbs |
| `_verseBoundary` | marks that a quotation starts across the verse break |
| `_frameInferable` | `the king` inferable from context |
| `_incl` / `_excl` | first-person plural |
| `_inLDV` | proposed new LDV word |
| `_addArg`, `_addInstrumentArg`… | P2: add an argument to this verb (Mark 7:2 `eating food with … hands _addArg`) |
| `_addSense`… | P2: add a new sense (Mark 6:23 `promised/swear _addSense`) |
| `_Adj`, `_Adp`, `_Adv` | P2: choose that part of speech form |
| `_1`, `_2`, … (or `_newNounIndex`) | the previously used noun now refers to a new thing (Mark 13:22: `people _1 [who …] … people _2 …  Those people _3 will do signs-B … people _4`) |
| `_jussive` | third-person imperative (He1 clarification) |
| `_suggestiveLets` | "Let's" feature |
| `_analysisNoteSeeTNN` | interpretation follows the translator's notes |
| `_copyinLDV` | (used in the Mark 9:29 example for "copies/manuscripts") flag |

**P2 notes** may be left in the P1 text (preferred) or in a comment beneath it; whatever makes the intent clear to P2 is acceptable since everything after `_` is uninterpreted.

## 10. Relative time (grammar-level notes from +03)

* Relative clauses and patient clauses use *relative* time, set against the main verb (`John thought [John will go to the store on the next day]` — "tomorrow" relative to the thinking day). Adverbial clauses do not.
* In quotes, the main verb takes a time value **other than Discourse**; relative time still applies inside.

## 11. Metaphor, idiom, `be-X`

Metaphors are allowed if they would probably be understood; add an alternate if it might not be (often literal/dynamic). **Idioms** (understood only in one culture) are not used. For a speaker who says something *is* something metaphorically (Jesus: "I am the light"), use the new metaphorical `be` sense. In titles and footnotes, explaining the meaning, use `be-U` ("be like").

## 12. Analysis Conventions (from the "Analysis Conventions" document)

The document is titled *Analysis Conventions*; its introduction says these conventions exist "when editing Easy English text into **TBTAese**" (the TBTA-flavoured English of a Phase 1 encoding), to simplify both manual editing and the semi-automatic semantic analysis. It is a short, example-driven summary; the full rules are in file 03 (cross-referenced below). Where it adds detail the other documents lack, that detail is marked **new**.

| Topic | Convention | Example | File 03 |
|---|---|---|---|
| Direct quote, one sentence | Whole sentence inside `["…"]`; `?` and `!` stay inside the bracket | `John said, ["Mary read that book"].` `John asked, ["Did Mary read that book?"]` `John shouted, ["Mary read this book!"]` | §F2 |
| Direct quote, several sentences | Bracket closes after the first sentence; the closing `"` goes at the very end | `John said, ["Mary read that book]. Then Peter read this book."` | §F2 |
| Addressee comma | An addressee NP is followed by a comma | `John, Mary read this book.` | 0.42 |
| Coordinate NP commas | Commas between items, `and` before the last | `John saw Mary, Peter, Steve, and Susan.` | §D12 |
| Question marks | Yes/no questions and content questions both end in `?` | `Did John read that book?` `Why did John read that book?` | §G3 |
| Exclamation marks | May end a proposition | `John read this book!` | §F2 |
| Imperatives | Begin with a second-person pronoun (singular **or plural**) and carry `(imp)` somewhere in the proposition **(new: plural form and placement)** | `You(John) (imp) read this book.` `You(students) (imp) read these books.` | §G1 |
| Personal pronouns | First and second person always carry a referent in parentheses; third person never appears | `I(John) read this book.` `You(Mary) read this book.` `[After John read this book] John read that book.` (no `he` in the main clause) | §B1 |
| Possessive pronouns | First and second person carry a referent; third person (`his`, `their`) is not allowed — repeat the noun with `'s` | `My(John's) book is there.` `Your(students') books are there.` `John read John's book.` | §B1, 0.1 |
| Reciprocal pronouns | Carry a referent | `The women asked each-other(women), ["Is this woman Naomi?"]` `The people talked to each-other(people).` | §B1 |
| Reflexive pronouns | First and second person carry a referent; third person (`himself`, `themselves`) is not allowed — repeat the noun **(new)** | `We(students) saw ourselves(students).` `You(students) saw yourselves(students).` `John saw John.` `The people saw the people.` | §B1 |
| Subordinate clauses | Every subordinate clause (relative, object complement, attributive complement, adverbial) is bracketed | see below | §D1 |
| Relative clauses | Begin with a relativizer (`that`, or `than` for comparatives **if the adjective allows it — new**) or a relative pronoun (`who`, `whom`); `whom` and `who` are equivalent to `that`. Use `[that … at]` instead of `where`/`when` | `The man [that John saw] read this book.` `The people [who live in Dallas] read many books.` `The people [whom John saw] live in Dallas.` `the place [that John was at]` `the time [that Mary left at]` | §D5 |
| Object complements (patient clauses) | No complementizer `that` (the analyzer reads it as a demonstrative adjective); keep the clause's own agent when it differs; verb fully inflected when it has its own subject, non-finite (`to …`) when the subject is shared or is the main clause's patient | `John thinks [Mary might read this book].` `John told [Mary to read this book].` `John wants [to read this book].` | §D6 |
| Attributive complements | Clausal arguments of adjectives, bracketed **(new: now named explicitly)** | `John is afraid [to read that book].` `John is afraid [Mary will read that book].` | §D1, file 02 §9 |
| Adverbial clauses | Bracketed | `[Before John read this book] John read that book.` `[After Mary read this book] John read that book.` | §D3 |

Notes:

* Nothing in this document contradicts files 02–04; it restates their core mechanics in one place. The wording "relative clauses **always** begin with a relativizer or relative pronoun" is the same as rule 0.8–0.9.
* The comparative `than` relativizer is not demonstrated in the document and has not been tested against the checker — see file 09 §C.
