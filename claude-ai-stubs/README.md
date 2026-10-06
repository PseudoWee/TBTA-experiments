# claude.ai skill loaders

Thin stubs for the claude.ai-installed copies of the TBTA skills. Each stub keeps
the skill's name and trigger description and, at run time, downloads the real
`SKILL.md` (and any reference it needs) from this repo's `main` branch. Edit the
skills under `skills/`, push, and every claude.ai session (including scheduled
tasks) picks up the change; the stubs themselves rarely need re-uploading.

Re-upload a stub only when a skill's name or trigger description changes
(copy the new `description:` line from the real `SKILL.md`).

Requires: network access to raw.githubusercontent.com, and the repo staying
public. Changes are visible only after they are pushed to `main`.
