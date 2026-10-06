#!/usr/bin/env python3
"""Client for the TaBiThA Editor API (https://editor.tabitha.bible).

Source of the API: https://github.com/CanIL-CA/tabitha/tree/main/apps/editor
Endpoint reference: skills/tabitha-editor-api/references/api-reference.md

  GET  /check?text=...        -> check(text) / batch_check(texts)
  GET  /analyze?text=...      -> analyze(text) / batch_analyze(texts)
  POST /ai-assist/generate    -> ai_assist_generate(text) / batch_ai_assist_generate(texts)

There is no native batch endpoint: "batch" loops client-side with limited
concurrency (default 4 workers; production allows ~60 requests/min/IP) and
returns results in input order, each {"input", "result"} or {"input", "error"}.

Cloudflare rejects the default Python User-Agent (HTTP 403, error 1010), so
USER_AGENT below must be kept.
"""
import argparse, concurrent.futures, json, sys, time, urllib.error, urllib.parse, urllib.request

BASE_URL = "https://editor.tabitha.bible"
DEFAULT_TIMEOUT = 30
DEFAULT_MAX_WORKERS = 4
DEFAULT_RETRY = 2
DEFAULT_RETRY_DELAY = 1.5

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"
)

def _request(method, path, params=None, json_body=None, timeout=DEFAULT_TIMEOUT):
    url = BASE_URL + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    data = None
    headers = {"Accept": "application/json", "User-Agent": USER_AGENT}
    if json_body is not None:
        data = json.dumps(json_body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read().decode("utf-8")
            return json.loads(body) if body else {}
    except urllib.error.HTTPError as e:
        detail = e.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"HTTP {e.code} calling {url}: {detail}") from e
    except urllib.error.URLError as e:
        raise RuntimeError(f"Network error calling {url}: {e.reason}") from e

def _with_retry(fn, *, retries=DEFAULT_RETRY, delay=DEFAULT_RETRY_DELAY):
    last_err = None
    for attempt in range(retries + 1):
        try:
            return fn()
        except RuntimeError as e:
            last_err = e
            if attempt < retries:
                time.sleep(delay * (2 ** attempt))
    raise last_err

def check(text: str) -> dict:
    return _with_retry(lambda: _request("GET", "/check", params={"text": text}))

def batch_check(texts, max_workers=DEFAULT_MAX_WORKERS):
    return _run_batch(check, texts, max_workers=max_workers)

def analyze(text: str) -> dict:
    return _with_retry(lambda: _request("GET", "/analyze", params={"text": text}))

def batch_analyze(texts, max_workers=DEFAULT_MAX_WORKERS):
    return _run_batch(analyze, texts, max_workers=max_workers)

def ai_assist_generate(text: str, temperature: float = 0.7,
                        frequency_penalty: float = 0, presence_penalty: float = 0) -> dict:
    """POST /ai-assist/generate: AI-suggested Phase 1 encoding for raw text.

    The JSON body key is "text" (NOT "message"). The server reads only "text";
    temperature / frequency_penalty / presence_penalty are sent for
    compatibility but are ignored by the current endpoint.

    Success: {"status": "ok", "phase_1": "<encoding>", "notes": ["<comment>", ...],
              "check": {"status": "ok|warning|error", "tokens": [...], "back_translation": "..."}}
    Failure: {"status": "error", "phase_1": "", "notes": [], "check": {...}, "message": "<reason>"}
    "check" is the /check result the server already ran on "phase_1".
    """
    body = {
        "text": text,
        "temperature": temperature,
        "frequency_penalty": frequency_penalty,
        "presence_penalty": presence_penalty,
    }
    return _with_retry(lambda: _request("POST", "/ai-assist/generate", json_body=body))

def batch_ai_assist_generate(texts, temperature: float = 0.7,
                              frequency_penalty: float = 0, presence_penalty: float = 0,
                              max_workers=DEFAULT_MAX_WORKERS):
    def _call(item):
        if isinstance(item, dict):
            return ai_assist_generate(
                item["text"],
                temperature=item.get("temperature", temperature),
                frequency_penalty=item.get("frequency_penalty", frequency_penalty),
                presence_penalty=item.get("presence_penalty", presence_penalty),
            )
        return ai_assist_generate(item, temperature, frequency_penalty, presence_penalty)
    return _run_batch(_call, texts, max_workers=max_workers,
                       label=lambda item: item.get("text") if isinstance(item, dict) else item)

def _run_batch(fn, items, max_workers=DEFAULT_MAX_WORKERS, label=None):
    results = [None] * len(items)
    def _task(i, item):
        input_label = label(item) if label else item
        try:
            return i, {"input": input_label, "result": fn(item)}
        except Exception as e:
            return i, {"input": input_label, "error": str(e)}
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_task, i, item) for i, item in enumerate(items)]
        for future in concurrent.futures.as_completed(futures):
            i, result = future.result()
            results[i] = result
    return results
