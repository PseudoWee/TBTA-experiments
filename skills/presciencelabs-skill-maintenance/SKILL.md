---
name: "presciencelabs-skill-maintenance"
description: "Use whenever a Presciencelabs / TBTA / TaBiThA Phase 1 skill (niv-to-phase1, phase1-encoding-review, phase1-new-verses, phase1-ai-assist, tabitha-editor-api, or a new one) or the phase1-handbook needs to be created, updated, fixed or synced. Checks the GitHub repo first and updates the repo skills before anything on claude.ai."
---

# Presciencelabs skill maintenance

GitHub (https://github.com/PseudoWee/TBTA-experiments, branch `main`) is the
reference for every Presciencelabs skill. The claude.ai copies are thin loaders
that fetch the repo version at run time (see `skills/claude-ai-loaders/README.md`).
So a skill is "updated" only when the repo is updated.

Covered skills: niv-to-phase1, phase1-encoding-review, phase1-new-verses,
phase1-ai-assist, tabitha-editor-api, and this one. Rules and notation live in
`phase1-handbook/`; skills link there instead of restating.

## Procedure — follow every time a skill change is requested

1. **Check the repo first.** Fetch the current `skills/<name>/SKILL.md` (and any
   `references/`, `scripts/` involved) from
   `https://raw.githubusercontent.com/PseudoWee/TBTA-experiments/main/skills/<name>/...`.
   Check recent changes: `https://api.github.com/repos/PseudoWee/TBTA-experiments/commits?path=skills/<name>&per_page=5`.
   Never start from the claude.ai installed copy or from memory: it is a loader.
2. **Decide where the change belongs.** A rule, notation or numbering change goes
   in `phase1-handbook/` first (03 rules, 04 notation, 06 checker/API, 07 lessons,
   08 playbooks, 09 open questions); the skill then links or references it. A
   workflow or skill-specific lesson goes in that skill's `SKILL.md` or `references/`.
3. **Edit the repo version.** Build the full updated file(s) from the fetched
   current version, keeping the "Handbook (source of truth)" section and the
   current rule numbering (0.1–0.53 / §1–§35). Deliver them to the user
   (connected repo folder if linked, otherwise as files) for commit and push; if
   you have git access with push rights, commit and push. State the exact files.
4. **Loaders.** `skills/claude-ai-loaders/<name>/SKILL.md` only changes if the
   skill's name or trigger description changes, or a new skill is added. In that
   case update the loader in the repo and propose the claude.ai card with
   `propose_skills` (full description, at most 1024 chars). Otherwise no card is needed.
5. **Tell the user** that changes go live only after the push to `main`, and
   re-verify by fetching the raw URL once pushed.
6. If the repo cannot be reached, say so and stop. Do not edit from memory.
