#!/usr/bin/env python3
"""Sample N verses from a corpus slice and batch-check them against the
TaBiThA editor API.

Usage:
    python3 sample_and_check.py <chunk.json> [--seed N] [--n N] [--out-dir DIR]

<chunk.json> is one slice as pulled from the dashboard artifact's
"corpus" collection: {index, count, verses: [{ref, enc, status}, ...]}.
Writes <out-dir>/sampled_verses.json and <out-dir>/check_results.json.
"""
import argparse
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tabitha_editor_client import batch_check


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("chunk_path", help="Path to a corpus slice JSON file")
    p.add_argument("--seed", type=int, default=None, help="Random seed (defaults to current UTC time, matching the scheduled task's convention)")
    p.add_argument("--n", type=int, default=200, help="Sample size (default 200)")
    p.add_argument("--workers", type=int, default=4, help="Concurrent check() calls (default 4)")
    p.add_argument("--out-dir", default=".", help="Where to write sampled_verses.json / check_results.json")
    args = p.parse_args()

    with open(args.chunk_path) as f:
        chunk = json.load(f)

    verses = chunk["verses"]
    seed = args.seed if args.seed is not None else int(__import__("datetime").datetime.utcnow().strftime("%Y%m%d%H%M"))
    rng = random.Random(seed)
    sample = rng.sample(verses, min(args.n, len(verses)))

    os.makedirs(args.out_dir, exist_ok=True)
    with open(os.path.join(args.out_dir, "sampled_verses.json"), "w") as f:
        json.dump(sample, f, indent=2, ensure_ascii=False)

    texts = [v["enc"] for v in sample]
    print(f"Running batch_check on {len(texts)} verses (seed={seed})...", file=sys.stderr)
    results = batch_check(texts, max_workers=args.workers)

    with open(os.path.join(args.out_dir, "check_results.json"), "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    n_ok = sum(1 for r in results if "result" in r)
    n_err = sum(1 for r in results if "error" in r)
    print(f"Done: {n_ok} ok, {n_err} transport errors (seed={seed})", file=sys.stderr)


if __name__ == "__main__":
    main()
