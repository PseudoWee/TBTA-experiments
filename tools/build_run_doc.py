#!/usr/bin/env python3
"""Assemble a "runs" collection document from aggregate.py's output — the
shape the dashboard artifact expects at write_db(collection="runs",
doc_id=<run timestamp>).

Usage:
    python3 build_run_doc.py <run-timestamp YYYY-MM-DDTHH:MM> <seed> \\
        <summary.json> <per_verse_results.json> [--out run.json]
"""
import argparse
import json
import os


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("run_timestamp", help="YYYY-MM-DDTHH:MM, also used as the doc_id")
    p.add_argument("seed", type=int)
    p.add_argument("summary_path")
    p.add_argument("per_verse_results_path")
    p.add_argument("--out", default="run.json")
    p.add_argument("--worst-n", type=int, default=12, help="How many verses to include in worst[] (default 12)")
    p.add_argument("--max-msgs", type=int, default=8, help="Cap on msgs[] per verse (default 8, keeps the doc under ~200KB)")
    args = p.parse_args()

    with open(args.summary_path) as f:
        summary = json.load(f)
    with open(args.per_verse_results_path) as f:
        per_verse = json.load(f)

    worst = [
        {
            "ref": v["ref"],
            "status": v["status"],
            "errors": v["errors"],
            "warnings": v["warnings"],
            "enc": v["enc"],
            "bt": v["bt"],
            "msgs": v["msgs"][: args.max_msgs],
        }
        for v in per_verse[: args.worst_n]
    ]

    doc = {
        "date": args.run_timestamp,
        "seed": args.seed,
        "n": summary["n"],
        "status_counts": {
            "ok": summary["status_counts"].get("ok", 0),
            "warning": summary["status_counts"].get("warning", 0),
            "error": summary["status_counts"].get("error", 0),
        },
        "clean": summary["clean"],
        "verses_with_errors": summary["verses_with_errors"],
        "verses_with_warnings": summary["verses_with_warnings"],
        "total_errors": summary["total_errors"],
        "total_warnings": summary["total_warnings"],
        "transport_errors": summary["transport_errors"],
        "top_rules": summary["top_rules"],
        "worst": worst,
    }

    with open(args.out, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"Wrote {args.out} ({os.path.getsize(args.out)} bytes)")


if __name__ == "__main__":
    main()
