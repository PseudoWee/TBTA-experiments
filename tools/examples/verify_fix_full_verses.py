#!/usr/bin/env python3
"""Final verification: the 'robes' pairing on its own, then the 3 full
corrected verses (Mark 5:40, 1 Kings 22:10, Matthew 14:36) assembled from
all their individual fixes together, confirming each reaches status: ok
with zero error/warning messages before being reported as a suggestion."""
import sys, json
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))
from tabitha_editor_client import check

tests = {
  "robes_test1": "The king of Israel was wearing the king's royal clothes/robes.",
  "robes_test2": "The king of Israel was wearing the king's royal clothes/robe.",
  "mark540_full": "But those people laughed at Jesus. (paragraph) Then Jesus told all of those people [those people to go-out from the house _implicit]. Jesus took the girl's father, the girl's mother, and Jesus's 3 man/disciples [who follow-B _routinely Jesus] into the place [that the girl was in].",
  "k22_10_full": "The king of Israel was wearing the king's royal clothes/robes. And Jehoshaphat [who was the king of Judah] was wearing Jehoshaphat's royal clothes/robes also. Those kings were sitting on the kings' chairs at the place [that people separate grain from plants in] [which was near the entrance of the gate of Samaria]. All of the people [who told God's messages to people] were speaking in-front-of those kings.",
  "mt1436_full": "And those people asked/beg Jesus [Jesus to let [those sick people touch the edge of Jesus's clothes/robe]]. And all of the sick people [who touched Jesus's clothes/robe] were healed-A by Jesus _implicitActiveAgent.",
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
