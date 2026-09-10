#!/usr/bin/env python3
"""Worked example: how the 2026-09-10T12:18 run's "suggestions" document
was assembled, after hand-reviewing 3 verses with the phase1-encoding-review
skill and re-checking each fix through /check.

Unlike aggregate.py or build_run_doc.py, this isn't a generic tool — the
`corrections` list below is specific, human-reviewed content for this run.
Kept as a concrete example of the suggestions.json shape the dashboard
expects (see data/runs/2026-09-10T12-18/suggestions.json for the output).

Run with: python3 build_suggestions.py [--out suggestions.json]
"""
import argparse
import json
import os

RUN_TS = "2026-09-10T12:18"

corrections = [
    {
        "ref": "Mark 5:40",
        "original_errors": 8,
        "suggested_status": "ok",
        "suggested": "But those people laughed at Jesus. (paragraph) Then Jesus told all of those people [those people to go-out from the house _implicit]. Jesus took the girl's father, the girl's mother, and Jesus's 3 man/disciples [who follow-B _routinely Jesus] into the place [that the girl was in].",
        "changes": [
            {
                "was": "the place [where the girl was]",
                "now": "the place [that the girl was in]",
                "reason": "checker:32 - 'where' cannot be used as a relativizer; rewrite as 'that ... <preposition>'. This single fix also cleared 3 cascade error messages on 'took' (checker:built-in:1, both 'does not match any sense' and 'different-participant patient clause') — the malformed relative was being read as a patient clause attaching to 'took', not a genuine problem with the verb 'take'."
            },
            {
                "was": "told all of those people [to go-out from the house _implicit]",
                "now": "told all of those people [those people to go-out from the house _implicit]",
                "reason": "checker:built-in:1 - 'tell' cannot be used with a same-participant patient clause. The subject of 'go-out' is the people told, not Jesus, so the clause is different-participant and needs its subject spelled out inside the brackets (matching the convention seen elsewhere in the corpus, e.g. Matthew 14:36's 'asked Jesus [Jesus to let ...]'). This was independent of the 'where' cascade — it did not clear on its own."
            },
            {
                "was": "Jesus's 3 disciples",
                "now": "Jesus's 3 man/disciples [who follow-B _routinely Jesus]",
                "reason": "checker:built-in:4 - 'disciples' is a level 2/3 word and rule 0.2 only allows it inside a pairing, explication, or complex alternate; paired with 'man' and explicated per the standard corpus convention for this word."
            }
        ],
        "note": "3 of the 8 original error messages (all on 'took') were pure cascade from the 'where' relativizer fault, not independent problems with 'take'. The 'told' same-participant-clause fault (3 messages) and the 'disciples' level-2/3 fault (1 message) were both independent and needed separate fixes. Re-checked: status ok, 0 errors, 0 warnings."
    },
    {
        "ref": "1 Kings 22:10",
        "original_errors": 4,
        "original_warnings": 1,
        "suggested_status": "ok",
        "suggested": "The king of Israel was wearing the king's royal clothes/robes. And Jehoshaphat [who was the king of Judah] was wearing Jehoshaphat's royal clothes/robes also. Those kings were sitting on the kings' chairs at the place [that people separate grain from plants in] [which was near the entrance of the gate of Samaria]. All of the people [who told God's messages to people] were speaking in-front-of those kings.",
        "changes": [
            {
                "was": "royal robes (both occurrences)",
                "now": "royal clothes/robes",
                "reason": "checker:built-in:4 - 'robes' is a level 2/3 word (rule 0.2); paired with the level-0 word 'clothes' in simple/complex order, which is the pairing already used elsewhere in this corpus (e.g. Matthew 14:36's 'clothes/robe')."
            },
            {
                "was": "the place [where people separate grain from plants]",
                "now": "the place [that people separate grain from plants in]",
                "reason": "checker:32 - 'where' cannot be used as a relativizer; rewritten as 'that ... in'. The adjacent '[which was near the entrance...]' clause was already valid and needed no change."
            },
            {
                "was": "All the people [who told...]",
                "now": "All of the people [who told...]",
                "reason": "checker:35 (P1 Checklist 0.17) - 'all' must be 'all of' before a non-generic (determined) noun; 'the people who told God's messages to people' is restricted by its relative clause, so it is not generic."
            }
        ],
        "note": "All 3 changes were independent, mechanical fixes (no cascade between them). A pre-existing warning on 'was' ('be-Y' has no theta grid information — an acceptable-residual class of warning per the review guidance) no longer appeared after re-checking the restructured verse; not chased further since that class of warning has nothing to fix upstream. Re-checked: status ok, 0 errors, 0 warnings."
    },
    {
        "ref": "Matthew 14:36",
        "original_errors": 4,
        "original_warnings": 1,
        "suggested_status": "ok",
        "suggested": "And those people asked/beg Jesus [Jesus to let [those sick people touch the edge of Jesus's clothes/robe]]. And all of the sick people [who touched Jesus's clothes/robe] were healed-A by Jesus _implicitActiveAgent.",
        "changes": [
            {
                "was": "let those sick people touch the edge of Jesus's clothes/robe",
                "now": "let [those sick people touch the edge of Jesus's clothes/robe]",
                "reason": "checker:built-in:1 / checker:5 - 'let' requires its embedded action as a bracketed patient clause. Without the bracket the checker reads 'touch' as a second main-clause verb ('Cannot have multiple verbs in the same clause'), and that same missing bracket is what produced the 'Incorrect usage of let-A' and 'Unexpected patient for let-A' errors too — all 3 original error messages were one fault, not three separate word-choice problems."
            },
            {
                "was": "all the sick people",
                "now": "all of the sick people",
                "reason": "checker:35 (P1 Checklist 0.17) - 'all' must be 'all of' before the non-generic (determined) noun 'sick people [who touched...]'."
            },
            {
                "was": "healed",
                "now": "healed-A",
                "reason": "checker:built-in:6 - 'heal' has multiple ontology senses with ambiguous complexity; tagging the specific sense (heal-A) removes the warning."
            }
        ],
        "note": "All 3 original error messages were cascade from the single missing bracket around 'let''s embedded clause — confirmed by isolating that clause alone, which validated clean once bracketed. The ambiguous-complexity warning on 'healed' was independent and fixed separately with a sense tag. Re-checked: status ok, 0 errors, 0 warnings."
    }
]

doc = {
    "date": RUN_TS,
    "systemic_note": "'where' misused as a relativizer (checker:32) keeps showing up as a false-positive multiplier, not just a single error: in this sample it cascaded into 3-4 extra 'take'/'go' case-frame errors per occurrence by being misread as a patient clause on the preceding verb. A blanket find-and-flag for '[where ...]' inside an encoding (there is no legitimate use of 'where' as a relativizer in Phase 1) would let reviewers fix the root cause first and avoid chasing cascade errors that clear for free. The 'all' -> 'all of' rule (checker:35) remains the single most mechanical, highest-volume fix in every sample and could similarly be flagged automatically before manual review.",
    "corrections": corrections
}

if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--out", default="suggestions.json")
    args = p.parse_args()

    with open(args.out, "w") as f:
        json.dump(doc, f, indent=2, ensure_ascii=False)
    print(f"Wrote {args.out} ({os.path.getsize(args.out)} bytes)")
