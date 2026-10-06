# 06 — The checker and the API: how to run and read it

Phase 1 text is validated by the **TaBiThA Editor** (<https://editor.tabitha.bible>, open source at `presciencelabs/tabitha-editor`). You can paste text into the web page or call it over HTTP. Use it constantly: it is the fastest feedback loop you have.

## 1. Endpoints

| Endpoint | Method | Purpose |
|---|---|---|
| `/check?text=…` | GET | Rule-check an encoding; returns status, nested per-word messages, and an **English back-translation** |
| `/analyze?text=…` | GET | Semantic analysis of text or an encoding: sentences, entities, features |
| `/ai-assist/generate` | POST | Fine-tuned model suggests a Phase 1 encoding of raw text |

No documented auth, SLA or rate limits. Be polite: ~4 concurrent workers, retry with backoff (≈0.6 s per verse, 200 verses ≈ 100 s).

### ⚠️ Two gotchas that cost hours

1. **Cloudflare blocks the default Python User-Agent** — you get HTTP 403, `error_code 1010 browser_signature_banned`. Send a browser-like `User-Agent` header, e.g. `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36`. A 403/1010 means *the header is missing*, not that the service is down. A DNS/connection error means your network blocks the domain.
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

## 3. The rule IDs you will meet most

| Rule ID | What it says | Typical fix |
|---|---|---|
| `checker:built-in:0` | Capitalise first word of a sentence/quote | Capitalise; and a comma before quotes (`checker:20`) |
| `checker:built-in:1` | **Verb argument structure / case frame** | Check theta grid; check for cascade causes first (file 07) |
| `checker:built-in:2` | Argument structure/case frame (non-verb, e.g. adposition) | Reorder; check missing `[` after e.g. `more-than` (adposition sense) |
| `checker:built-in:3` | Verb has **no theta grid information** | Acceptable warning (upstream gap), but check for side effects |
| `checker:built-in:4` | Level 2/3 word not inside a pairing/explication/`(complex)` alternate | File 05 |
| `checker:built-in:5` | Cannot have multiple verbs in the same clause | Add bracket / split sentence |
| `checker:built-in:6` | Ambiguous complexity (word has senses at different levels) | Prefer explication; else sense tag (`Lot-A`) |
| `checker:built-in:7` | Word not recognised in ontology | Typo? number word? unknown proper noun? |
| `checker:built-in:8` | Ambiguous part of speech | Tag it: `first _adv` |
| `checker:20` | Expect `,` before a quote | Add comma |
| `checker:23` | Don't inflect the verb (`took-away`) | Use base form |
| `checker:32` | Cannot use `where` as relativizer | `that … <preposition>` |
| `checker:35` | Use `all of` for non-generic nouns | Add `of` |
| `checker:38` | `could` only within `so that` | `be able [to …]` |
| `checker:48` | No negatives with purpose clauses | Judgement call (0.34) |
| `checker:49` | Write `X of Y _literalExpansion` | Reorder |
| `token:syntax` | Missing space before `[`, after `]`/`.`/`)`, malformed notation | Fix spacing/tag |
| `clause:nesting_depth` | More than the allowed bracket depth | Split sentences |

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
