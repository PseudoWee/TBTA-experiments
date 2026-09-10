#!/usr/bin/env python3
"""Isolation checks for the Mark 5:40 and 1 Kings 22:10 fixes (2026-09-10T12:18
run): confirms the 'where' relativizer clauses validate clean once rewritten,
and separately that clearing them also clears the cascade errors on the
neighboring verb ('took', in Mark 5:40) without touching that verb at all."""
import sys, json
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))
from tabitha_editor_client import check

tests = {
  "mark540_s1_orig": "Jesus told all of those people [to go-out from the house _implicit].",
  "mark540_s2_fixed_where": "Jesus took the girl's father, the girl's mother, and Jesus's 3 disciples into the place [that the girl was in].",
  "k22_10_where_fixed": "Those kings were sitting on the kings' chairs at the place [that people separate grain from plants in] [which was near the entrance of the gate of Samaria].",
  "k22_10_allof_fixed": "All of the people [who told God's messages to people] were speaking in-front-of those kings.",
  "mt1436_let_fixed": "And those people asked/beg Jesus [Jesus to let [those sick people touch the edge of Jesus's clothes/robe]].",
  "mt1436_allof_healed_fixed": "And all of the sick people [who touched Jesus's clothes/robe] were healed-A by Jesus _implicitActiveAgent.",
}

results = {}
for k, v in tests.items():
    r = check(v)
    results[k] = r
    print("="*70)
    print(k, "->", v)
    print("status:", r.get("status"))
    print("bt:", r.get("back_translation"))
    def walk(token):
        for m in token.get("messages") or []:
            yield token.get("token",""), m
        for sub in token.get("sub_tokens") or []:
            yield from walk(sub)
    for tok in r.get("tokens", []):
        for t, m in walk(tok):
            if m.get("label") in ("error","warning"):
                print(" -", m["label"], m["rule_id"], "|", t, "|", m["message"])

with open("test1_results.json","w") as f:
    json.dump(results, f, indent=2)
