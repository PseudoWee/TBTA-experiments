# 06 — The checker and the API: how to run and read it

Phase 1 text is validated by the **TaBiThA Editor** (<https://editor.tabitha.bible>, MIT-licensed, open source in the TaBiThA monorepo at <https://github.com/CanIL-CA/tabitha/tree/main/apps/editor>). You can paste text into the web page or call it over HTTP. Use it constantly: it is the fastest feedback loop you have.

## 1. Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/check?text=…` | GET | Rule-check an encoding; returns status, nested per-word messages, and an **English back-translation** |
| `/analyze?text=…` | GET | Semantic analysis of text or an encoding: sentences, entities, features |
| `/ai-assist/generate` | POST | LLM suggests a Phase 1 encoding of raw text, then the server checks it (and repairs once if errors) |

No auth or API key. **Production allows 60 requests per minute per IP** (Editor README); beyond that expect throttling. For batch work run a local editor (`bun run dev:editor`, port 1337 — see the TaBiThA repo's `CONTRIBUTING.md`) instead of hammering production. If you must use production: ~4 concurrent workers, retry with backoff (≈0.6 s per verse, 200 verses ≈ 100 s). The API has no versioning or compatibility guarantee — routes and shapes can change without notice.

### ⚠️ Two gotchas that cost hours

1. **Cloudflare blocks some default library User-Agents** (e.g. Python's `urllib`) — you get HTTP 403, `error code: 1010`. The Editor README recommends a descriptive `User-Agent` such as `my-project/0.1 (+https://github.com/me/my-project)`; a browser-like one also works in practice, e.g. `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36`. A 403/1010 means *the header is missing*, not that the service is down. A DNS/connection error means your network blocks the domain.
2. **AI-assist's request key is `"text"`, not `"message"`.** The older `references/api-reference.md` still shows `{"message": …}` and a `{finish_reason, message}` response; both are stale. Sending `message` returns `{"status":"error","message":"Enter some text to encode."}`.

A tested Python client is in `tools/tabitha_editor_client.py` (`check()`, `analyze()`, `ai_assist_generate()`, and `batch_*` versions with concurrency, retry and per-item error capture).

```bash
python3 - <<'PY'
import sys; sys.path.insert(0, "tools")
from tabitha_editor_client import check
r = check("John went to the town.")
print(r["status"], "|", r["back_translation"])
PY
```

## 2. Reading a `/check` response

```json
{
  "status": "ok" | "warning" | "error",
  "tokens": [ { "token": "...", "messages": [...], "sub_tokens": [ ... ] } ],
  "back_translation": "..."
}
```

**Messages are nested.** Each token has `messages[]` *and* `sub_tokens[]`, which nest further. A flat scan of top-level `tokens[].messages` misses most of them. Walk recursively:

```python
def walk(token):
    for m in token.get("messages") or []:
        yield token.get("token", ""), m
    for sub in token.get("sub_tokens") or []:
        yield from walk(sub)
```

Each message: `{label, severity, message, rule_id}`; `label` ∈ `error`, `warning`, `suggest`, `info`.

| Label | Treat as |
|---|---|
| `error` | must fix |
| `warning` | fix unless it is one of the (very short) acceptable-residual list in file 07 |
| `suggest` | advisory — **but read it**: the part-of-speech tag suggestion arrives here |
| `info` | mostly routine case-frame chatter (one line per argument-slot variant of a word). Collapse to a count. Its text can *reveal the exact structure a verb sense wants* (`prepare-A: missing same-participant patient clause ('[to Verb]')`). |

### Quirks to know

* **The `status` string can lie.** It can read `error` with *no* error/warning messages at all (e.g. `That man will put all his(man's) grain into those buildings.`). Judge by the message list, not just status. When counting a sample, "ok" runs slightly below "fully clean".
* **A recorded status isn't a fact.** A verse logged `warning` can really be `error` (2 Kings 18:11) or `ok` (Genesis 30:32). Re-run `/check` before trusting anything recorded.
* **The back-translation is your content check.** It exposes garbled constituent order and fabricated or dropped clauses that the rule checker passes silently. Read it against the NIV, sentence by sentence.
* **The checker's own caveat:** "because this word is not recognized, errors and warnings within the same clause may not be accurate." Cascades are covered in file 07.
* Implicit text appears as `<<…>>` (regular) or `<…>` (necessary) in the back-translation.
* The back-translator does not always render tense tags (`come-out _past` still prints "come out"). That's a display gap, not an encoding fault.

## 3. Rule IDs — the full table

Taken from the editor source, `apps/editor/src/lib/rules/checker_rules.ts` (see file 10 for the link). IDs are positions in that file: `checker:built-in:N` = the Nth hand-coded rule; `checker:N` = the Nth declarative JSON rule. **Adding or reordering rules in the source shifts the numbers**, so treat the *name* as authoritative and the ID as a handle that can change. "Handbook rule" refers to file 03's numbering (not the source PDF's).

### Hand-coded rules (`checker:built-in:N`)

| ID | What it checks | Typical fix / see |
|---|---|---|
| 0 | Capitalise first word of a sentence or quote | Capitalise |
| 1 | **Verb argument structure / case frame** | Check theta grid; look for cascade causes first (file 07) |
| 2 | Argument structure / case frame for non-verbs (e.g. adpositions) | Reorder; check for a missing `[` |
| 3 | Verb has **no theta grid information** | Usually an acceptable upstream gap |
| 4 | Level 2/3 word outside a pairing / explication / `(complex)` alternate | Handbook 0.2; file 05 |
| 5 | Word complexity level of complex pairings | File 05 |
| 6 | Ambiguous complexity (senses at different levels) | Prefer explication, else sense tag (`Lot-A`) |
| 7 | Word not recognised in the ontology | Typo? number word? unknown proper noun? |
| 8 | Ambiguous part of speech | Tag it: `first _adv` |
| 9 | Relative clause that may be meant as a complement clause | Handbook D5/D6 |
| 10 | `(complex)` clause with no following `(simple)` clause | Add the simple version |
| 11 | Expect an agent of a passive (stem verbs) | Handbook 0.14 |
| 12 | Adjective used as a noun after a determiner | Add a noun (`the poor people`) |

### Declarative rules (`checker:N`)

| ID | What it says | Handbook rule |
|---|---|---|
| 0 | "it" apart from an agent clause | 0.1 |
| 1 | Expect an agent of a passive | 0.14 |
| 2 | `each other` must be hyphenated | 0.1 |
| 3 / 4 | Suggest `at that place` for `there`, `at this place` for `here` | style |
| 5 | Two verbs in the same sentence | 0.4 |
| 6 / 7 | Imperative with no subject (sentence start / after a conjunction) | 0.19 |
| 8 | Imperative note in a non-quote subordinate clause | 0.19 |
| 9 / 10 / 11 | `Let's`, `Let X…`, `May X…` | use `(jussive)` / `_suggestiveLets` |
| 12 | Avoid `way` | §35 |
| 13 / 14 / 15 / 16 | Cannot use `even` / `any` / `really` / `X's own Y` | 0.17 |
| 17 | Suggest a comma after "One day/morning/evening…" | 0.43 |
| 18 | Expect `[` before a relative clause | 0.5 / D4 |
| 19 | Expect `[` before a quote | 0.13 |
| 20 | Expect `,` before a quote-begin clause | 0.43 |
| 21 | `so` in an adverbial clause should be followed by `that` | — |
| 22–28 | Unhyphenated phrasal verbs with `around`, `away`, `down`, `off`, `put on`, `out`, `up` | 0.3 |
| 29 | Some noun plurals aren't recognised | — |
| 30 / 31 / 32 / 33 / 34 | `what`, `where`, `when`, `whose` as relativizer; `what` vs `which thing` | 0.9 |
| 35 | `all of`, not bare `all`, for non-generic nouns | 0.18 |
| 36 | Aspect auxiliary (`start`) with no other verb | 0.20 |
| 37 | `X is able to`, not `X can` | 0.25 |
| 38 | `could` only inside a `so` adverbial clause | — |
| 39 | `is going to` as future marker | 0.29 |
| 40 / 41 | `is to {Verb}` / `have to {Verb}` as obligation | — |
| 42 / 43 | Two conjunctions starting a sentence; `now` as a conjunction | — |
| 44 | Prefer an attributive adjective to a predicative relative clause | — |
| 45 | Errant `that` in a complement clause | 0.8 |
| 46 / 47 | Passives in `in-order-to` / `by` adverbial clauses | — |
| 48 | Negative with a purpose clause | 0.34 (judgement call) |
| 49 | `of` in the wrong place before `_literalExpansion` / `_dynamicExpansion` | — |
| 50 | Negation on adjectives | — |
| 51 / 52 | Nested independent clauses with `and`/`but` (bare / after a relative clause) | 0.23 |

The handbook-rule column is the compiler's best match and is blank (—) where the checker enforces something the checklist doesn't spell out. Where no rule fits, trust the checker's message.

### Non-rule IDs

| ID | Meaning |
|---|---|
| `token:syntax` | Malformed notation or spacing (note/tag syntax) |
| `clause:syntax` | Missing period, or missing `[` / `]` |
| `clause:nesting_depth` | More than the allowed bracket depth |

## 4. `/ai-assist/generate`

```json
POST /ai-assist/generate
{"text": "<raw NIV verse>", "temperature": 0.7, "frequency_penalty": 0, "presence_penalty": 0}
```

Returns:

```json
{
  "status": "ok",
  "phase_1": "<AI-generated Phase 1 encoding>",
  "notes": ["Replaced 'confined' with 'kept-A'.", "…"],
  "check": {"status": "ok|warning|error", "tokens": [...], "back_translation": "..."}
}
```

* How it works (Editor source): the shared `@tabitha/ai` client, routed through the Cloudflare AI Gateway, is prompted with `system_instruction.md` (conventions + one worked example) and `phase1_rules.md` (itemised rules). The server then runs its own checker on the result and, **if errors are found, makes one automatic repair pass** whose prompt includes the checker's feedback and the ontology's pairing/explication hints for flagged words. Needs `AI_GATEWAY_TOKEN` on the server. ADR: `docs/decisions/0007-ai-consolidation.md`.
* `phase_1` — the suggestion. `notes` — the model's plain-English account of the swaps it made. `check` — the server already ran `/check` on it (same `walk()` applies).
* Treat it as a **first draft**, not an answer. In the project's own review passes the AI-assist drafts were sometimes *more* faithful than corpus entries (they kept clauses others had dropped) and sometimes less.

**Worked example (Genesis 39:20, 2026-09-10).** Raw NIV: *"Joseph's master took him and put him in prison, the place where the king's prisoners were confined. But while Joseph was there in the prison,"* AI-assist result (`status: ok`, check `warning`):

```
Joseph's master-A took-A Joseph. And Joseph's master-A put-A Joseph into prison-A [which was the place [that _implicitActiveAgent kept-A the king's prisoners-A in]]. But during the time [that Joseph stayed-A at that place in the prison-A].
```

Notes the AI gave: `was` → `stayed-A` (avoid `be-Y` grid issues); `where` → `the place [that … in]`; unrecognised `confined` → `kept-A`; `while-A` → `during the time [that …]`; final comma → period (verse-ending punctuation rule). One real warning remained: `in` doesn't match a sense for that argument structure (`checker:built-in:2`); 20 further `suggest`/`info` messages collapsed.

## 5. Batch and scheduled use

* Batch = loop client-side; results keep input order, each `{"input":…,"result":…}` or `{"input":…,"error":…}` so partial failures don't lose data.
* `tools/sample_and_check.py` samples N verses from a corpus slice and batch-checks them; `aggregate.py`, `build_run_doc.py`, `build_suggestions.py` convert results into the documents the dashboard stores.
* The scheduled task (every ≈3 h) samples **only not-yet-checked verses**, tracked by a per-slice ledger (`coverage` collection, `chunk_NN`), until a slice's ~471 verses are done, then resets. A `coverage_summary`/`totals` document shows corpus-wide progress (checked / 18,830).

## 6. Sizing what "good" looks like

Calibration run of 2026-09-10 (200 random corpus verses): 55 `ok`, 50 `warning`, 95 `error`; 57 fully clean; 282 errors and 287 warnings in total. So even *professionally reviewed corpus entries* mostly do not pass the current checker — which has two implications: (a) "the corpus says so" is not a reason to copy a construction; (b) the checker keeps getting stricter or the corpus pre-dates rules. Both mean you must **verify against `/check`, not against neighbours.**
