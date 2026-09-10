#!/usr/bin/env python3
"""Turn sample_and_check.py's output into the summary/per-verse shapes used
by the dashboard's "runs" and "suggestions" collections.

Usage:
    python3 aggregate.py <sampled_verses.json> <check_results.json> [--out-dir DIR]

Writes <out-dir>/summary.json and <out-dir>/per_verse_results.json.
"""
import argparse
import collections
import json
import os


def walk(token):
    """Messages nest inside sub_tokens, so recurse rather than scanning
    only the top-level tokens[]."""
    for m in token.get("messages") or []:
        yield token.get("token", ""), m
    for sub in token.get("sub_tokens") or []:
        yield from walk(sub)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("sampled_verses_path")
    p.add_argument("check_results_path")
    p.add_argument("--out-dir", default=".")
    args = p.parse_args()

    with open(args.sampled_verses_path) as f:
        sample = json.load(f)
    with open(args.check_results_path) as f:
        results = json.load(f)

    status_counts = collections.Counter()
    clean = 0
    verses_with_errors = 0
    verses_with_warnings = 0
    total_errors = 0
    total_warnings = 0
    transport_errors = 0
    rule_counts = collections.Counter()  # (rule_id, label) -> count
    per_verse = []

    for v, r in zip(sample, results):
        ref, enc = v["ref"], v["enc"]
        if "error" in r:
            transport_errors += 1
            continue
        res = r["result"]
        status = res.get("status", "unknown")
        status_counts[status] += 1

        msgs = []
        for tok in res.get("tokens", []):
            for token_str, m in walk(tok):
                if m.get("label") in ("error", "warning"):  # ignore info/suggest
                    msgs.append({
                        "token": token_str,
                        "label": m.get("label"),
                        "severity": m.get("severity"),
                        "message": m.get("message"),
                        "rule_id": m.get("rule_id"),
                    })

        n_err = sum(1 for m in msgs if m["label"] == "error")
        n_warn = sum(1 for m in msgs if m["label"] == "warning")
        total_errors += n_err
        total_warnings += n_warn
        if n_err == 0 and n_warn == 0:
            clean += 1
        if n_err > 0:
            verses_with_errors += 1
        if n_warn > 0:
            verses_with_warnings += 1
        for m in msgs:
            rule_counts[(m["rule_id"], m["label"])] += 1

        per_verse.append({
            "ref": ref,
            "enc": enc,
            "bt": res.get("back_translation", ""),
            "status": status,
            "errors": n_err,
            "warnings": n_warn,
            "msgs": msgs,
        })

    rule_totals = collections.Counter()
    rule_by_label = collections.defaultdict(lambda: {"error": 0, "warning": 0})
    for (rule_id, label), cnt in rule_counts.items():
        rule_totals[rule_id] += cnt
        rule_by_label[rule_id][label] += cnt

    top_rules = [
        {"rule": rule_id, "count": cnt, "by_label": rule_by_label[rule_id]}
        for rule_id, cnt in rule_totals.most_common(12)
    ]

    worst_sorted = sorted(per_verse, key=lambda x: (-x["errors"], -x["warnings"]))

    summary = {
        "n": len(sample),
        "status_counts": dict(status_counts),
        "clean": clean,
        "verses_with_errors": verses_with_errors,
        "verses_with_warnings": verses_with_warnings,
        "total_errors": total_errors,
        "total_warnings": total_warnings,
        "transport_errors": transport_errors,
        "top_rules": top_rules,
    }

    os.makedirs(args.out_dir, exist_ok=True)
    with open(os.path.join(args.out_dir, "summary.json"), "w") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)
    with open(os.path.join(args.out_dir, "per_verse_results.json"), "w") as f:
        json.dump(worst_sorted, f, indent=2, ensure_ascii=False)

    print(json.dumps(summary, indent=2))
    print("\nTop 15 worst verses:")
    for v in worst_sorted[:15]:
        print(f"  {v['ref']}: errors={v['errors']} warnings={v['warnings']} status={v['status']}")


if __name__ == "__main__":
    main()
