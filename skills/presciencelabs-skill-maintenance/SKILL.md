---
name: "presciencelabs-skill-maintenance"
description: "Use whenever a Presciencelabs / TBTA / TaBiThA Phase 1 skill (niv-to-phase1, phase1-encoding-review, phase1-new-verses, phase1-ai-assist, tabitha-editor-api, or a new one) or the phase1-handbook needs to be created, updated, fixed or synced. Checks the GitHub repo first and updates the repo skills before anything on claude.ai."
---

# Presciencelabs skill maintenance

GitHub (https://github.com/PseudoWee/TBTA-experiments, branch `main`) is the
reference for every Presciencelabs skill. On claude.ai only one thin loader is
installed (`presciencelabs`, see `skills/claude-ai-loaders/README.md`); it routes
to the skills in `skills/` and fetches them at run time. So a skill is "updated"
only when the repo is updated.

Sub-skills: niv-to-phase1, phase1-encoding-review, phase1-new-verses,
phase1-ai-assist, tabitha-editor-api, and this one. Rules and notation live in
`phase1-handbook/`; skills link there instead of restating.

## Procedure — follow every time a skill change is requested

1. **Check the repo first.** Fetch the current `skills/<name>/SKILL.md` (and any
   `references/`, `scripts/` involved) from
   `https://raw.githubusercontent.com/PseudoWee/TBTA-experiments/main/skills/<name>/...`.
   If you have GitHub access, also check recent commits for that path. Never
   start from a claude.ai installed copy or from memory.
2. **Decide where the change belongs.** A rule, notation or numbering change goes
   in `phase1-handbook/` first (03 rules, 04 notation, 06 checker/API, 07 lessons,
   08 playbooks, 09 open questions); the skill then links or references it. A
   workflow or skill-specific lesson goes in that skill's `SKILL.md` or `references/`.
3. **Edit the repo version.** Build the full updated file(s) from the fetched
   current version, keeping the "Handbook (source of truth)" section and the
   current rule numbering (0.1–0.53 / §1–§35). Deliver them to the user
   (connected repo folder if linked, otherwise as files) for commit and push; if
   you have git access with push rights, commit and push. State the exact files.
4. **Router and loader.** Adding or renaming a skill, or changing its triggers:
   update the table in `skills/presciencelabs/SKILL.md` and the description in
   both that file and `skills/claude-ai-loaders/presciencelabs/SKILL.md`, then
   propose the claude.ai card for `presciencelabs` with `propose_skills` (full
   description, at most 1024 chars). Otherwise no card is needed.
5. **Tell the user** that changes go live only after the push to `main`, and
   re-verify by fetching the raw URL once pushed.
6. If the repo cannot be reached, say so and stop. Do not edit from memory.
