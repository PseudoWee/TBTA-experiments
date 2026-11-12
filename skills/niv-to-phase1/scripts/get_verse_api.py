#!/usr/bin/env python3
"""
Fetch ONE verse (or a short range) of NIV or NASB from API.Bible by reference.
Alternative to get_verse.py (which reads the user's local NIV1984 docx).

Usage:
    export API_BIBLE_KEY=<key>          # never commit or paste the key into files
    python get_verse_api.py NIV  "1 Chronicles 10:2"
    python get_verse_api.py NASB "Song of Songs 2:1-3"
    python get_verse_api.py --list-bibles [--lang eng]   # find/verify Bible ids

Reference docs: https://api.bible/api-reference (GET /v1/bibles/{bibleId}/passages/{passageId})

Notes:
- Requires only the `requests` package.
- Prints only the verse(s) asked for (copyright: private reference use, no bulk dumps).
- API.Bible's NIV (78a9f6124f344018-01) is most likely the 2011 NIV text, NOT the NIV 1984
  used by the project's local docx. Wording can differ -- the script prints the Bible's
  own name/abbreviation so the difference is visible. When the 1984 text is required,
  use get_verse.py with the docx instead.
- A 401/403 means the key lacks access to that Bible (licensed versions such as NIV and
  NASB must be enabled for the key in the API.Bible dashboard).
"""
import os
import re
import sys

import requests

BASE = "https://rest.api.bible/v1"  # legacy host: https://api.scripture.api.bible/v1
BIBLE_IDS = {
    "NIV": "78a9f6124f344018-01",
    "NASB": "a761ca71e0b3ddcf-01",
}

# USFM book ids; keys are lowercase, alphanumerics only
_BOOKS = """GEN Genesis|EXO Exodus|LEV Leviticus|NUM Numbers|DEU Deuteronomy|JOS Joshua|JDG Judges|RUT Ruth|
1SA 1 Samuel,1st Samuel|2SA 2 Samuel,2nd Samuel|1KI 1 Kings,1st Kings|2KI 2 Kings,2nd Kings|
1CH 1 Chronicles,1st Chronicles|2CH 2 Chronicles,2nd Chronicles|EZR Ezra|NEH Nehemiah|EST Esther|JOB Job|
PSA Psalms,Psalm|PRO Proverbs|ECC Ecclesiastes|SNG Song of Songs,Song of Solomon,Songs of Songs,Canticles|
ISA Isaiah|JER Jeremiah|LAM Lamentations|EZK Ezekiel|DAN Daniel|HOS Hosea|JOL Joel|AMO Amos|OBA Obadiah|
JON Jonah|MIC Micah|NAM Nahum|HAB Habakkuk|ZEP Zephaniah|HAG Haggai|ZEC Zechariah|MAL Malachi|
MAT Matthew|MRK Mark|LUK Luke|JHN John|ACT Acts|ROM Romans|1CO 1 Corinthians,1st Corinthians|
2CO 2 Corinthians,2nd Corinthians|GAL Galatians|EPH Ephesians|PHP Philippians|COL Colossians|
1TH 1 Thessalonians,1st Thessalonians|2TH 2 Thessalonians,2nd Thessalonians|1TI 1 Timothy,1st Timothy|
2TI 2 Timothy,2nd Timothy|TIT Titus|PHM Philemon|HEB Hebrews|JAS James|1PE 1 Peter,1st Peter|
2PE 2 Peter,2nd Peter|1JN 1 John,1st John|2JN 2 John,2nd John|3JN 3 John,3rd John|JUD Jude|REV Revelation"""


def _key(s):
    s = s.lower().strip()
    s = re.sub(r"^(\d)(st|nd|rd)\b", r"\1", s)
    return re.sub(r"[^a-z0-9]", "", s)


BOOK_MAP = {}
for _entry in _BOOKS.replace("\n", "").split("|"):
    _code, _names = _entry.strip().split(" ", 1)
    BOOK_MAP[_code.lower()] = _code
    for _n in _names.split(","):
        BOOK_MAP[_key(_n)] = _code


def parse_reference(ref):
    m = re.match(r"^(.*?)\s+(\d+):(\d+)(?:-(\d+))?$", ref.strip())
    if not m:
        sys.exit(f"Can't parse reference {ref!r}. Expected 'Book chapter:verse[-verse2]'.")
    book, ch, v1, v2 = m.groups()
    code = BOOK_MAP.get(_key(book))
    if not code:
        sys.exit(f"Unknown book {book!r}.")
    start = f"{code}.{ch}.{v1}"
    return start if not v2 or v2 == v1 else f"{start}-{code}.{ch}.{v2}"


def api_get(path, **params):
    key = os.environ.get("API_BIBLE_KEY")
    if not key:
        sys.exit("Set the API_BIBLE_KEY environment variable (do not hard-code the key).")
    try:
        r = requests.get(f"{BASE}{path}", headers={"api-key": key}, timeout=30,
                         params={k: v for k, v in params.items() if v is not None})
    except requests.RequestException as e:
        sys.exit(f"Could not reach API.Bible ({e}). If this is a sandbox, allow rest.api.bible.")
    if r.status_code in (401, 403):
        sys.exit(f"HTTP {r.status_code}: key invalid or not licensed for this Bible id.")
    if r.status_code == 404:
        sys.exit("HTTP 404: Bible id or passage id not found.")
    r.raise_for_status()
    return r.json()["data"]


def main(argv):
    if argv[:1] == ["--list-bibles"]:
        lang = argv[argv.index("--lang") + 1] if "--lang" in argv else None
        for b in api_get("/bibles", language=lang):
            print(b["id"], b.get("abbreviation", ""), b.get("name", ""), sep="\t")
        return
    if len(argv) != 2 or argv[0].upper() not in BIBLE_IDS:
        sys.exit(__doc__)
    version, ref = argv[0].upper(), argv[1]
    bible_id = BIBLE_IDS[version]
    d = api_get(f"/bibles/{bible_id}/passages/{parse_reference(ref)}", **{
        "content-type": "text", "include-notes": "false", "include-titles": "false",
        "include-chapter-numbers": "false", "include-verse-numbers": "false",
        "include-verse-spans": "false"})
    print(f"[{version} via API.Bible, id {bible_id}] {d.get('reference', ref)}")
    print(re.sub(r"\s+", " ", d["content"]).strip())


if __name__ == "__main__":
    main(sys.argv[1:])
