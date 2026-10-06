# claude.ai loader stubs

Thin skills installed on claude.ai. Each stub only holds the skill's name, its
trigger description and a Step 0 that fetches the real `SKILL.md` from this
repo at run time:

`https://raw.githubusercontent.com/PseudoWee/TBTA-experiments/main/skills/<name>/SKILL.md`

So the repo is the single source of truth: pushing to `main` updates every
claude.ai session, scheduled tasks included, with no re-upload.

## Folders

One folder per skill, each containing only `SKILL.md`: niv-to-phase1,
phase1-encoding-review, phase1-new-verses, phase1-ai-assist, tabitha-editor-api,
presciencelabs-skill-maintenance.

## Updating

- Edit the real skill under `skills/<name>/` and push. Nothing else needed.
- Re-save a stub on claude.ai (card or folder upload) only when a skill's name or
  trigger description changes, or when a new skill is added (add its stub here).
- Procedure for Claude: `skills/presciencelabs-skill-maintenance/SKILL.md`.

## Requirements

The repo stays public; the session can reach `raw.githubusercontent.com`. If the
fetch fails, the stub stops and says so rather than guessing.
