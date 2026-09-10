#!/usr/bin/env python3
"""
Align every phase_1_encoding row in the Sources sqlite db with its raw NIV
verse (parsed once, in memory, from the project's NIV docx) and report
aggregate patterns -- never writes the merged corpus back out to disk.

Usage:
    python analyze_corpus.py <niv.docx> <sources.sqlite>
"""
import sys
import re
import sqlite3
from collections import Counter
from docx import Document

ORDINAL_PREFIX = re.compile(r"^(\d)\s+")
ORDINAL_MAP = {"1": "1st", "2": "2nd", "3": "3rd"}


def normalize_book(name: str) -> str:
    m = ORDINAL_PREFIX.match(name)
    if m:
        return ORDINAL_MAP.get(m.group(1), m.group(1)) + " " + name[m.end():]
    return name


def parse_bible(docx_path):
    """One pass over the whole docx -> {book: {chapter: {verse: text}}}."""
    doc = Document(docx_path)
    bible = {}
    current_book = None
    current_chapter = None

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text or not para.runs:
            continue

        is_bold_heading = all(r.bold for r in para.runs if r.text.strip())

        if is_bold_heading and re.match(r"^[A-Za-z0-9].{0,40}$", text) and not text.isdigit():
            current_book = text
            bible[current_book] = {}
            current_chapter = None
            continue

        if current_book is None:
            continue

        if para.runs[0].bold and para.runs[0].text.strip().isdigit():
            current_chapter = int(para.runs[0].text.strip())
            verse_text = "".join(r.text for r in para.runs[1:]).strip()
            bible.setdefault(current_book, {}).setdefault(current_chapter, {})[1] = verse_text
            continue

        if current_chapter is None:
            continue

        m = re.match(r"^(\d+)(\D.*)$", text)
        if not m:
            continue
        vnum, vtext = int(m.group(1)), m.group(2).strip()
        bible[current_book].setdefault(current_chapter, {})[vnum] = vtext

    return bible


def main():
    docx_path, sqlite_path = sys.argv[1], sys.argv[2]
    bible = parse_bible(docx_path)

    conn = sqlite3.connect(sqlite_path)
    cur = conn.cursor()
    cur.execute(
        "SELECT id_primary, id_secondary, id_tertiary, phase_1_encoding "
        "FROM Sources WHERE phase_1_encoding IS NOT NULL AND phase_1_encoding != ''"
    )
    rows = cur.fetchall()

    matched, unmatched = 0, 0
    token_counts = Counter()
    sentence_ratio_sum, sentence_ratio_n = 0.0, 0
    unmatched_books = Counter()

    # Patterns worth tracking frequency of, keyed by rule number for reference.
    patterns = {
        "0.1/0.36 named-X (apposition->named)": re.compile(r"\bnamed \w"),
        "0.11 implicit info (<<...>> / (...)/(implicit)": re.compile(r"_implicit|\(implicit"),
        "0.13 passive implicit agent": re.compile(r"_implicitActiveAgent"),
        "0.14 rhetorical question": re.compile(r"\((?:yes|no)?rhetorical\)"),
        "0.18 imperative (imp)": re.compile(r"\(imp\)"),
        "0.3 hyphenated tense underscore": re.compile(r"_(?:past|future|present)\b"),
        "0.41 which-interrogative": re.compile(r"\bwhich \w"),
        "0.53 poetry markers": re.compile(r"\(begin-poetry\)|\(end-poetry\)"),
        "brackets present (subordinate clause)": re.compile(r"\["),
    }

    for book, chap, verse, phase1 in rows:
        docx_book = normalize_book(book)
        try:
            chap_i, verse_i = int(chap), int(verse)
        except ValueError:
            unmatched += 1
            unmatched_books[book] += 1
            continue
        niv_text = bible.get(docx_book, {}).get(chap_i, {}).get(verse_i)
        if niv_text is None:
            unmatched += 1
            unmatched_books[book] += 1
            continue
        matched += 1

        for label, pat in patterns.items():
            if pat.search(phase1):
                token_counts[label] += 1

        niv_sentences = len(re.findall(r"[.!?]+(?:\s|$)", niv_text)) or 1
        phase1_sentences = len(re.findall(r"[.!?]+(?:\s|$)", phase1)) or 1
        sentence_ratio_sum += phase1_sentences / niv_sentences
        sentence_ratio_n += 1

    print(f"Total phase_1_encoding rows: {len(rows)}")
    print(f"Matched to NIV text: {matched}")
    print(f"Unmatched: {unmatched}")
    if unmatched_books:
        print("Top unmatched books (likely book-name mismatch):")
        for b, c in unmatched_books.most_common(10):
            print(f"  {b}: {c}")
    print()
    print(f"Avg phase1-sentences / niv-sentences ratio: {sentence_ratio_sum / sentence_ratio_n:.2f}"
          f"  (n={sentence_ratio_n})")
    print()
    print("Pattern frequency across matched verses:")
    for label in patterns:
        n = token_counts[label]
        pct = 100 * n / matched if matched else 0
        print(f"  {label}: {n} verses ({pct:.1f}%)")


if __name__ == "__main__":
    main()
