# 08 — Playbooks (step-by-step procedures with worked examples)

Three procedures: **A. encode a new verse**, **B. review an existing encoding**, **C. use AI-assist as a first draft**. All three finish with the same gate: *`/check` clean, back-translation read against the NIV.*

---

## A. Encode a raw NIV verse into Phase 1

### Step 0 — decide the variant

Default to **full notation** (brackets, explicit referents). Say so; it is easy to relax to He1 later.

### Step 1 — get the raw text and read for meaning

Pull the verse from your *own* NIV source (not bundled in the repo — copyright); `skills/niv-to-phase1/scripts/get_verse.py <docx> "Book 1:2"` extracts one verse. Verses are rarely self-contained: **check the neighbours for an implied subject**.

Worked example — implied subject (1 Samuel 1:14): the verse alone is *"and said to her, 'How long will you keep on getting drunk? Get rid of your wine.'"* The speaker (Eli) and addressee (Hannah) come from verse 13. Phase 1:

> `Then Eli said to Hannah, ["You(Hannah) (imp) do not become drunk! You(Hannah) (imp) throw-away your(Hannah's) wine!"]`

Read for **meaning, not wording**. Idioms and compressed predicates are decomposed (*pressed hard after* → *chased* + *came near*).

### Step 2 — list referents; kill third-person pronouns

Write the full noun each time, **worded identically** (0.36). Prefer the most specific correct expression: if the wider passage makes an unnamed figure's identity clear ("the Philistine" = Goliath), use the name.

### Step 3 — apposition and "of"-meaning-"named"

`his sons Jonathan, Abinadab and Malki-Shua` → `Saul's sons named Jonathan, named Abinadab, and named Malki-Shua`.

### Step 4 — split into one-verb clauses

Independent actions → separate sentences joined by `And …` (no bracketed independent clauses). Subordinate clauses bracketed; count brackets; ≤4 levels.

### Step 5 — vocabulary check

For every content word: is it level 0/1? Use `complex-terms.md` first, then `/search`, then `/simplification_hints`. Level 2/3 → pairing / explication / complex alternate. Numbers → digits.

### Step 6 — notation and rules pass

Run through file 03. Typical misses: `can`, `going to`, stray `he`, double negatives, apposition, isolated noun phrases, `where`/`when` relativizers.

### Step 7 — mechanical pass (cheap, always)

* `all` + determined noun → `all of`.
* Space before every `[`; space after every `]`, `.`, `)`.
* Space before every `_`; sense suffixes hyphenated (`able-B`, not `able_B`).
* Pairings written `dynamic|literal` with a pipe when that's what you mean; complex/simple pairs use `(complex)/(simple)`.
* Digits for numbers.
* Footnote vs comment: *is it literally in parentheses in the NIV?* → `(comment-begin)…(comment-end)`; otherwise `(footnote)` (at the end).
* Tag ambiguous POS.

### Step 8 — run `/check`, then read the back-translation against the NIV

If any message remains, go to the diagnosis order at the top of file 07. Stop only when `status: ok` or you can name a residual from the short acceptable list.

### Worked example 1 — decomposition (1 Chronicles 10:2)

Covered in file 01. Notice: one NIV sentence → three Phase 1 sentences; no `he/they/his`; `named` ×3; Oxford comma.

### Worked example 2 — instrument noun that is level 2 (1 Samuel 17:50)

NIV: *"So David triumphed over the Philistine with a sling and a stone; without a sword in his hand he struck down the Philistine and killed him."*

> `So David defeated Goliath with a rope and a stone. David threw/slung that stone at Goliath with the rope. And David killed Goliath without a sword.`

* `sling` (noun) is L2, pairing `rope`; `sling` (verb) is L2, pairing `throw-A`. The sentence was **decomposed** rather than swapped word for word: the general statement, then a second clause spelling out the slinging action — "make sure the resulting sentence describes the event using it."
* Discourse-connective `So` kept (it reflects a real link to the previous verses).
* `the Philistine` → `Goliath` (use known identity).

### Worked example 3 — passive + imperative (1 Corinthians 6:20)

NIV: *"you were bought at a price. Therefore honor God with your body"*

> `For you(friends) were bought by God _implicitActiveAgent for a price. Therefore, you(friends) (imp) honor/glorify God through-B your(friends') body.`

Passive agent supplied (0.14); first-mention addressee `friends` supplied for `you`; `honor/glorify` is a pairing.

### Worked example 4 — rhetorical question (2 Corinthians 3:8)

NIV: *"will not the ministry of the Spirit be even more glorious?"*

> `(yesrhetorical) Will the work of the Spirit be more great/glorious? (statement) The work of the Spirit will certainly be more great/glorious!`

`ministry` → `work` (pairing/explication); positive verb in the question; statement follows.

### Worked example 5 — quote with comma and implicit speaker

NIV (Matthew 8:4, shape): *Then Jesus said to him, "See that you don't tell anyone…"*

> `Then Jesus said to the man, ["You(man) (imp) do not tell anyone [about that thing]…]` — one sentence inside the bracket; extra sentences continue outside it. Do not invent a filler first sentence to feed the bracket (file 07 §6, flavour 1b).

### Worked example 6 — relative instead of `where` (Joshua 4:5 shape)

NIV: *"into the river near the place where the priests are standing"*

> `into the river near the place [that the priests are standing in]`

### Worked example 7 — numbers and POS tag (Exodus 13:13 shape)

NIV: *"every firstborn donkey… "* — `donkey` L2, `firstborn` is not a word:

> `…every animal/donkey [that was born first _adv] …` — pairing + tag; verify by `/check`.

---

## B. Review an existing encoding (the `phase1-encoding-review` procedure)

**Deliverable:** a corrected encoding that `/check` accepts **plus** a Was / Now / Reason table naming a rule for every change. Never hand back a fix you haven't re-run.

1. **Get encoding + check result**; walk the *whole* message tree.
2. **Separate root causes from cascades.** Isolate each suspect clause. Clear cascade sources (§3 of file 07) before re-picking any verb sense.
3. **Look up every word you change or keep** (complex-terms table; `/search` for level + theta grid; `/simplification_hints`).
4. **Check the corpus**: neighbouring verses, parallels, other uses of the same proper nouns (SQL against `Sources`). Copy a convention only if it validates; fix both if it doesn't.
5. **Draft, re-check, iterate.** Test candidate phrasings individually. Aim for `status: ok`. Confirm bracket balance. **Read the back-translation against the NIV sentence by sentence** for added/dropped/substituted content (the seven flavours in file 07 §6).
6. **Present** in the format below.

### Output format

Lead with the corrected encoding as a blockquote, then:

```
| Was | Now | Reason |
|---|---|---|
| `the old prophet` | `the old man [who told God's messages to people]` | `prophet` is L2 — rule 0.2 allows level 2/3 words only in a pairing, explication, or complex alternate. Ontology explication; worded to match v11 (rule 0.36) |
```

Table rules:

* **Every Reason names the rule** (number and requirement) or the ontology fact (level, theta grid). "Reads better" isn't a reason; if a change is stylistic, **label it so the user can decline it**.
* One row per distinct change, not per error message (six identical L2 errors on one word = one row).
* Expand non-obvious fixes (cascade, theta grid, decomposition) in a short paragraph below.
* State which warnings remain and why; flag judgment-call residuals as open items.
* When the validating fix narrows meaning, **say so** in the row.
* Flag systemic issues (bug shared with the parallel verse; convention failing corpus-wide) and offer to sweep.

### Worked example — a two-row review

Illustrative rows (the two fixes are real corpus patterns — number words in Joshua 24:12, `all` in many verses — but this table is a shape, not a verified review):

| Was | Now | Reason |
|---|---|---|
| `the two Amorite kings` | `the 2 Amorite kings` | Number words aren't ontology entries (`checker:built-in:7`) — digits only; mechanical, no judgement call |
| `all the kings` | `all of the kings` | `checker:35` / rule 0.18 — `all` + determined noun needs `of` |

---

## C. Using AI-assist (`phase1-ai-assist`)

Purpose: a **first draft** from the editor's fine-tuned model, plus its notes and check status. Not a final answer.

1. Get the raw text (paste or look up in the NIV file; verify verse number — the NIV doc has no verse-level markers, so nearby verses can look similar).
2. `POST /ai-assist/generate` with `{"text": …}` and the browser User-Agent (file 06).
3. Report **in this order**: raw verse, suggested encoding, AI's notes (short bullets), check status, then — only if `warning`/`error` — the messages (collapse `info`/`suggest` noise to a count).
4. Don't dump raw JSON. For many verses, loop client-side with ~4 workers and retries.
5. **Then run Playbook B on the result.** The dashboard's "Suggested changes" tab stores both columns side by side — the reviewed fix and the unedited AI draft — which is how the pipeline measures where each is stronger.

Worked example: Genesis 39:20 in file 06 §4.

---

## D. Running the calibration loop (maintainers)

Weekly/auto: `tools/sample_and_check.py <chunk.json>` → `aggregate.py` → `build_run_doc.py`, `build_suggestions.py` → dashboard. The scheduled-task prompt (`docs/scheduled-task-prompt.md`) is the canonical description. Key conventions:

* Run/suggestion document ids = UTC start time truncated to the minute, `YYYY-MM-DDTHH:MM`.
* Slice selection = whole hours since anchor `2026-09-09T00:00 UTC` modulo 40; 40 shuffled slices of the 18,830 corpus.
* Per-slice `coverage` ledger prevents re-sampling checked verses; a round resets after a slice's ~471 are covered.
* The task does **not** call `propose_skills` itself; it appends a short note to a `skill_notes/pending` doc (cap 50) that you review in a normal chat and turn into a skill proposal on your schedule.
* The repo snapshot contains one run (`2026-09-10T12-18`) and one slice (`chunk_36`) as a worked example.
