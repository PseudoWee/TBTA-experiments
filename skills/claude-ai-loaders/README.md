# claude.ai loader

One thin skill, `presciencelabs/`, replaces installing six separate skills on
claude.ai. It holds only the combined trigger description and a Step 0 that
fetches the router from this repo:

`https://raw.githubusercontent.com/PseudoWee/TBTA-experiments/main/skills/presciencelabs/SKILL.md`

The router (`skills/presciencelabs/SKILL.md`) picks the right sub-skill
(niv-to-phase1, phase1-encoding-review, phase1-new-verses, phase1-ai-assist,
tabitha-editor-api, presciencelabs-skill-maintenance) and fetches its real
`SKILL.md` and references from `skills/<name>/`.

## Install

Install only `skills/claude-ai-loaders/presciencelabs/` on claude.ai (card or
folder upload). Do not install the six folders under `skills/` separately.

## Updating

- Edit a sub-skill under `skills/<name>/` and push to `main`. Nothing else needed.
- Re-save the loader only when its description changes (new skill, new triggers).
- Procedure for Claude: `skills/presciencelabs-skill-maintenance/SKILL.md`.

## Requirements

The repo stays public; the session can reach `raw.githubusercontent.com`. If the
fetch fails, the loader stops and says so rather than guessing.
