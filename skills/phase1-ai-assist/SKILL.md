---
name: phase1-ai-assist
description: "Generate an AI-suggested Phase 1 (TBTA/TaBiThA) encoding for a raw NIV verse via the TaBiThA editor's AI-assist function, and report the suggested encoding plus the AI's own comments and any check warnings."
---

# Phase 1 AI-Assist

Runs a raw NIV verse through the TaBiThA Editor's AI-assist function
(`POST /ai-assist/generate` on https://editor.tabitha.bible) to get an
AI-generated Phase 1 encoding suggestion, then reports the suggested
encoding, the AI's own comments on what it changed, and the rule-check
result the server already ran against that suggestion.

This is different from the other TBTA skills in this workspace:
- `niv-to-phase1` hand-builds an encoding by applying the Phase 1 ruleset.
- `phase1-encoding-review` reviews an *existing* encoding and proposes a
  Was/Now/Reason table of fixes.
- This skill asks the AI-assist model itself for a first-draft encoding of
  raw text, and just reports what it returns.

## Step 1 -- get the raw verse text

If the user pastes verse text directly, use that. If they give only a
reference (e.g. "Genesis 39:20"), look it up in the "NIV1984 - original.doc"
project file with `project_search` (search on a distinctive phrase, or the
book/chapter) or `project_read`, and confirm the verse number matches before
using it -- the doc has no verse-level markers, so nearby verses can look
similar.

## Step 2 -- call the AI-assist endpoint

Write this client to a scratch directory. The Cloudflare-blocking
User-Agent requirement from the `tabitha-editor-api` skill applies here too
-- a default Python User-Agent gets HTTP 403 `error_code 1010`:

```bash
WORK=/tmp/tabitha && mkdir -p $WORK
cat > $WORK/ai_assist.py <<'PY'
#!/usr/bin/env python3
import json, sys, urllib.error, urllib.request

BASE_URL = "https://editor.tabitha.bible"
USER_AGENT = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36")

def ai_assist_generate(text, temperature=0.7, frequency_penalty=0, presence_penalty=0):
    """POST /ai-assist/generate. IMPORTANT: the request body key is "text",
    not "message" -- sending "message" (as the tabitha-editor-api skill's
    bundled reference doc previously showed) returns {"status":"error", ...,
    "message":"Enter some text to encode."} because the server never sees
    the input."""
    body = {"text": text, "temperature": temperature,
            "frequency_penalty": frequency_penalty, "presence_penalty": presence_penalty}
    data = json.dumps(body).encode("utf-8")
    req = urllib.request.Request(
        BASE_URL + "/ai-assist/generate", data=data, method="POST",
        headers={"Accept": "application/json", "Content-Type": "application/json",
                 "User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))

if __name__ == "__main__":
    print(json.dumps(ai_assist_generate(sys.argv[1]), indent=2, ensure_ascii=False))
PY
```

Run it with the raw verse text as the single argument:

```bash
python3 $WORK/ai_assist.py "Joseph's master took him and put him in prison, the place where the king's prisoners were confined. But while Joseph was there in the prison,"
```

## Step 3 -- read the response

Actual response shape (confirmed by a live call 2026-09-10; use this over
what `tabitha-editor-api`'s bundled `references/api-reference.md` may still
show for this endpoint if that file hasn't been regenerated):

On success:
```json
{
  "status": "ok",
  "phase_1": "<AI-generated Phase 1 encoding>",
  "notes": ["<comment on one change the AI made>", "..."],
  "check": {
    "status": "ok" | "warning" | "error",
    "tokens": [...],
    "back_translation": "<back-translation of phase_1>"
  }
}
```
On failure (e.g. empty input, or the model errors out):
```json
{"status": "error", "phase_1": "", "notes": [], "check": {...}, "message": "<reason>"}
```

Fields, and what to do with each:
- **`phase_1`** -- the suggested encoding. This is the main result.
- **`notes`** -- the AI's own plain-English comments on specific
  substitutions it made (e.g. "Replaced 'confined' with 'kept-A'"). Report
  these as-is; they are the "comments" the AI-assist function produces.
- **`check`** -- the server already ran `/check` on the generated `phase_1`.
  `check.status` is the overall verdict; `check.back_translation` is a
  sanity-check paraphrase. `check.tokens` nests messages inside
  `sub_tokens` recursively (reuse the `walk()` pattern from
  `tabitha-editor-api`), each `{label, severity, message, rule_id}` --
  surface `error` and `warning` items; treat `suggest`/`info` as optional
  detail (`info` is usually routine case-frame noise, e.g. one line per
  argument-slot variant of a preposition -- worth collapsing to a count
  rather than listing each one).

## Output format

Report, in this order: the raw verse text (with reference if known), the
suggested Phase 1 encoding, the AI's notes as a short bullet list, the check
status, and -- only if status is `warning` or `error` -- the warning/error
messages from `check.tokens` (collapse repetitive `info`/`suggest` clutter to
a count, e.g. "12 routine `info` messages about the missing head noun for
'in' collapsed"). Do not dump the raw JSON unless asked.

## Worked example -- Genesis 39:20

Raw NIV text (NIV1984):
> Joseph's master took him and put him in prison, the place where the king's
> prisoners were confined. But while Joseph was there in the prison,

AI-assist result (`status: ok`):

**Suggested encoding:**
```
Joseph's master-A took-A Joseph. And Joseph's master-A put-A Joseph into
prison-A [which was the place [that _implicitActiveAgent kept-A the king's
prisoners-A in]]. But during the time [that Joseph stayed-A at that place in
the prison-A].
```

**AI's comments (`notes`):**
- Replaced 'was' with 'stayed-A' to avoid 'be-Y' theta grid issues.
- Replaced 'where' relativizer with 'the place [that... in]'.
- Replaced unrecognized 'confined' with 'kept-A'.
- Replaced 'while-A' with 'during the time [that...]' to resolve the while-A error.
- Changed the final comma to a period to satisfy the verse-ending punctuation rule.

**Check result:** `warning` -- back-translation: "Joseph's master took
Joseph. And Joseph's master put Joseph into prison which was the place that
<<>> kept the king's prisoners in. But during the time that Joseph stayed at
that place in the prison."

One warning: `in` does not match any sense in the Ontology for that argument
structure (rule `checker:built-in:2`). The remaining 20 messages are routine
`suggest` (8x -- drop redundant senses that would be selected by default)
and `info` (12x -- per-sense "missing head noun" detail for `in`) noise,
safely collapsed.

## Batching multiple verses

For more than a couple of verses, loop client-side (there's no native batch
endpoint) with the same modest concurrency (~4 workers) and retry-with-
backoff approach as `tabitha-editor-api`'s batch functions -- reuse that
skill's `_run_batch` helper, just route each call through the corrected
`ai_assist_generate` above (the `text` key, not `message`).