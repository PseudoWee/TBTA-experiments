#!/usr/bin/env python3
"""Tests candidate fixes for 'tell' being used with a same-participant patient
clause (Mark 5:40): repeating the patient as the bracket's explicit subject
vs. a 'so that' rewrite vs. a _differentParticipant tag, to find which one the
checker actually accepts."""
import sys, json
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))
from tabitha_editor_client import check

tests = {
  "told_v2_repeat_participant": "Jesus told all of those people [those people to go-out from the house _implicit].",
  "told_v3_sothat": "Jesus told all of those people [so that those people would go-out from the house _implicit].",
  "told_v4_different_marker": "Jesus told all of those people [to go-out from the house _implicit] _differentParticipant.",
  "disciples_fix": "Jesus took the girl's father, the girl's mother, and Jesus's 3 man/disciples [who follow-B _routinely Jesus] into the place [that the girl was in].",
}

for k, v in tests.items():
    r = check(v)
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
