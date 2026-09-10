# TaBiThA Editor API Reference

Source project: https://github.com/presciencelabs/tabitha-editor
Live app: https://editor.tabitha.bible
Base URL for API calls: `https://editor.tabitha.bible`

This is a small open-source service (no published SLA, no documented auth,
no documented rate limits). Be conservative with concurrency and add
retries — see `scripts/tabitha_editor_client.py`.

## 1. Grammar & Rule Checker API

`GET /check?text={text}`

Parses input encoding text, checks rule validations, performs
backtranslation, and returns overall status.

- **Query params**: `text` (string, required) — raw encoding text to check.
- **Example**: `/check?text=Paul+write-01`
- **Response shape** (documented fields): overall status (`ok` | `warning` |
  `error`), tokens with associated messages, and a backtranslation string.

## 2. Text Analysis API

`GET /analyze?text={text}`

Parses input text into sentences and performs semantic analysis to extract
source entities and features.

- **Query params**: `text` (string, required) — raw text or encoding.
- **Example**: `/analyze?text=Paul+write-01`

## 3. AI Assist Generation API

`POST /ai-assist/generate`

Generates AI completions for semantic encoding assistance using fine-tuned
models.

- **Request body** (JSON):
  ```json
  {
    "message": "User prompt or encoding context",
    "temperature": 0.7,
    "frequency_penalty": 0,
    "presence_penalty": 0
  }
  ```
- **Response**: `{ "finish_reason": "stop", "message": "Generated response..." }`

## Batching (client-side — no native batch endpoint)

None of the three endpoints has a documented batch mode. "Batch" support in
this skill means: loop over a list of inputs, call the relevant endpoint for
each, and collect results in original order — with limited concurrency
(default 4 workers) and retry-with-backoff on transient failures, so one bad
input or hiccup doesn't take down the whole run.

Each batch result is one of:
```json
{"input": "<original input>", "result": {...}}
{"input": "<original input>", "error": "<error message>"}
```
so a run with partial failures still returns everything, and you can filter
for `"error"` afterward to see what needs a retry or manual look.
