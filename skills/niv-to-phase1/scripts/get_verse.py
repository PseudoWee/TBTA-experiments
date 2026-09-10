#!/usr/bin/env python3
"""
Pull ONE verse (or a small verse range) out of the user's own NIV docx file,
by reference, without ever writing the full Bible text to disk or printing
more than what was asked for.

Usage:
    python get_verse.py <path-to-docx> "<Book> <chapter>:<verse>[-<verse2>]"

Example:
    python get_verse.py NIV1984_-_original.docx "1 Chronicles 10:2"
    python get_verse.py NIV1984_-_original.docx "1 Chronicles 10:2-4"

Notes on the source formatting (NIV1984_-_original.doc, converted to docx):
- Book headings are bold paragraphs like "1st Chronicles".
- The first verse of each chapter is marked by a BOLD run containing just
  the chapter number (e.g. bold "1"), immediately followed by that verse's
  text in the same paragraph -- there is no separate "1" verse marker.
- Every other verse is its own paragraph starting with a plain (non-bold)
  verse number directly against the first word, e.g. "2Kenan, Mahalalel,".
- Occasional inline section subheadings (e.g. "The Japhethites") got merged
  into the end of the preceding verse's paragraph by text extraction. If a
  requested verse's text ends with what looks like a short Title Case
  phrase with no verb, that's almost certainly one of these -- drop it, or
  flag it for the user to double check against a print copy.

This script only ever holds one book's paragraphs in memory long enough to
find the requested reference, and only prints the verse(s) asked for.
"""
import sys
import re
from docx import Document

# Normalize a few common ways people write book names to how they appear
# as headings in this particular file ("1st Chronicles", not "1 Chronicles").
ORDINAL_PREFIX = re.compile(r"^(\d)\s+")
ORDINAL_MAP = {"1": "1st", "2": "2nd", "3": "3rd"}


def normalize_book(name: str) -> str:
    name = name.strip()
    m = ORDINAL_PREFIX.match(name)
    if m:
        name = ORDINAL_MAP.get(m.group(1), m.group(1)) + " " + name[m.end():]
    return name


def parse_reference(ref: str):
    m = re.match(r"^(.*?)\s+(\d+):(\d+)(?:-(\d+))?$", ref.strip())
    if not m:
        raise ValueError(f"Couldn't parse reference: {ref!r}. Expected 'Book chapter:verse'.")
    book, chapter, v1, v2 = m.groups()
    chapter = int(chapter)
    v1 = int(v1)
    v2 = int(v2) if v2 else v1
    return normalize_book(book), chapter, v1, v2


def get_verses(docx_path: str, book: str, chapter: int, v1: int, v2: int):
    doc = Document(docx_path)
    in_book = False
    current_chapter = None
    results = {}

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue

        is_bold_heading = all(run.bold for run in para.runs if run.text.strip()) and para.runs

        if is_bold_heading:
            # Could be a book heading ("1st Chronicles") or a chapter-number
            # run glued to verse-1 text (handled below via mixed runs).
            if text == book:
                in_book = True
                current_chapter = None
                continue
            elif in_book and re.match(r"^[A-Za-z].{0,40}$", text) and text != book:
                # Hit the next book's heading -- stop.
                break

        if not in_book:
            continue

        # Chapter-start paragraph: first run is bold and numeric, rest is verse 1 text.
        if para.runs and para.runs[0].bold and para.runs[0].text.strip().isdigit():
            current_chapter = int(para.runs[0].text.strip())
            verse_text = "".join(r.text for r in para.runs[1:]).strip()
            if current_chapter == chapter and v1 <= 1 <= v2:
                results[1] = verse_text
            continue

        if current_chapter != chapter:
            continue

        m = re.match(r"^(\d+)(\D.*)$", text)
        if not m:
            continue
        vnum = int(m.group(1))
        vtext = m.group(2).strip()
        if v1 <= vnum <= v2:
            results[vnum] = vtext
        if vnum > v2:
            break

    return results


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(__doc__)
        sys.exit(1)
    docx_path, ref = sys.argv[1], sys.argv[2]
    book, chapter, v1, v2 = parse_reference(ref)
    verses = get_verses(docx_path, book, chapter, v1, v2)
    if not verses:
        print(f"No verses found for {ref} (looked for book heading {book!r}, chapter {chapter}).")
        sys.exit(1)
    for vnum in range(v1, v2 + 1):
        if vnum in verses:
            print(f"{vnum} {verses[vnum]}")
        else:
            print(f"{vnum} [not found]")
