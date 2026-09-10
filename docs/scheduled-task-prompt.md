# Scheduled task prompt — Phase 1 encoding calibration run

This is the exact prompt sent to a fresh Claude session every ~3 hours by
the "Phase 1 encoding — 3-hourly 200-verse check" scheduled task. Each
firing has no memory of the previous one — everything the run needs is
either in this prompt, in the skills under [`skills/`](../skills), or in
the dashboard artifact's own database.

Reproduced here for reference/versioning; the live copy of record is the
scheduled task's own configuration.

---

Calibration run for the TBTA/TaBiThA Phase 1 encoding work. This runs
roughly once every 3 hours — work through this end to end and report in the
conversation. There is no prior context — everything you need is below.

## 1. Pick this run's slice

The verse corpus (18,830 rows with a `phase_1_encoding`, from
`Sources_2026-07-27.tabitha.sqlite`, shuffled once and cut into 40 slices)
lives in the database of the dashboard artifact (see the top-level README
for the link). Slice index = (whole hours between 2026-09-09T00:00 UTC and
the start of this run, in UTC) mod 40, zero-padded to two digits (e.g. 38
whole hours since that anchor is `chunk_38`). Read it with the Artifact
tool: `action: "read_db"`, `db_op: "get"`, `collection: "corpus"`,
`doc_id: "chunk_NN"`, passing `out_dir` so the ~170 KB document is written
to a file instead of returned inline. The document is
`{index, count, verses: [{ref, enc, status}]}`, ~471 verses.

## 2. Sample and check

Take a random 200 verses from that slice. Run each verse's `enc` through
the TaBiThA editor rule checker — use the `tabitha-editor-api` skill, which
carries the client, the browser User-Agent Cloudflare requires, and the
message-walking helper. 4 workers, roughly 2 minutes for 200. Messages nest
inside each token's `sub_tokens`, so recurse; count only messages whose
`label` is `"error"` or `"warning"` (ignore `"info"` and `"suggest"`).

## 3. Aggregate

Status split (ok / warning / error), verses fully clean, verses with
errors, verses with warnings, total error messages, total warning
messages, transport errors, the top ~12 `rule_id`s by message count split
by severity, and the verses ranked by error count then warning count.

## 4. Report in the conversation

- Key insights first: which rules dominate, what looks systematic rather
  than a per-verse slip, and how it compares with the previous run (read
  the most recent doc in the `runs` collection, or the 2026-09-09 baseline
  if none exists yet).
- The verses carrying the most errors, with their counts.
- Correction suggestions for 3 verses. Pick ones whose errors are
  genuinely fixable in the encoding (relativizer misuse, 'all' vs 'all of',
  case-frame mismatches, missing sense tags) rather than ontology gaps that
  no encoding change can fix. Use the `phase1-encoding-review` skill and
  present them as a Was / Now / Reason table, each reason naming the
  specific rule behind the change. Re-run every proposed fix through
  `/check` and confirm the named error actually clears before including
  it. If a verse's original errors were partly cascade, say so explicitly
  and name which errors were cascade vs. independent.

## 5. Save the run so the dashboard picks it up

Naming convention: every run needs its own unique, sortable identifier
instead of a calendar date — the run's start time in UTC, truncated to the
minute, formatted `YYYY-MM-DDTHH:MM`. Use that exact string for both the
`date` field inside the JSON and the `doc_id` it's stored under. Write a
JSON file shaped `{date, seed, n, status_counts, clean, verses_with_errors,
verses_with_warnings, total_errors, total_warnings, transport_errors,
top_rules, worst}` and store it via the Artifact tool
(`write_db` / `set` / collection `"runs"` / that `doc_id`). Keep it under
200 KB (cap `msgs` at 8 per verse). The dashboard's Overview tab aggregates
every stored run into corpus-wide totals automatically.

## 6. Save the suggestions to the "Suggested changes" tab

Every run's corrections from step 4 accumulate into a running, per-verse
detail view, matching the depth of the Sample runs tab. Each verse shows
two side-by-side columns: a reviewed fix (`phase1-encoding-review`) and an
unedited AI-assisted first draft of the same verse (`phase1-ai-assist`,
generated in step 6b) — see [`data/runs/`](../data/runs) for the exact JSON
shape and a worked example. Store via the Artifact tool (`write_db` / `set`
/ collection `"suggestions"` / the same `doc_id` as step 5).

## 6b. Generate the AI-assisted draft for each suggested verse

For each of the same verses picked in step 4, also run the raw NIV text
through the `phase1-ai-assist` skill to get the AI-assist model's own
first-draft encoding — independent of, and not informed by, the
hand-reviewed `suggested` encoding from step 4. This is reporting what the
AI-assist function proposes on its own, not another review pass.

## 7. Skill notes — do NOT call propose_skills from this run

This task fires every few hours from a fresh session each time, with no
memory of the previous firing, so a proposal card posted inside one run's
own session is easy to miss before the next run replaces it. Instead:
decide whether anything in this run warrants a change to `niv-to-phase1`
or `phase1-encoding-review` — typically a rule firing so consistently that
the skill should pre-empt it — and if so, append a note to the
accumulating `skill_notes` / `"pending"` doc rather than editing the skill
directly. The dashboard's "Skill notes" tab shows the accumulated list;
review it on your own schedule and ask Claude, in an ordinary chat, to fold
any of them into the actual skill file.

## 8. Keeping the "Ontology & structure" changelog in sync — not part of this scheduled run either

The dashboard's Changelog tab has a third sub-tab, "Ontology & structure",
which lays out the original P1 Checklist (0.1–0.54) as an unhighlighted
baseline followed by three color-coded groups of accumulated learning:
cascade sources, recurring failure patterns & notation mechanics, and
corrected understanding — each pulled from the `niv-to-phase1` and
`phase1-encoding-review` skill files. This is a curated, hand-designed page
that a scripted run every 3 hours shouldn't touch unsupervised. Instead:
whenever accumulated skill notes get folded into the actual skill files
(the same moment referenced in step 7), that same session should also
check whether the folded-in change adds a genuinely new pattern to the
ontology/structure understanding, and if so add one new highlighted entry
to the matching color group (or start a new group if the pattern doesn't
fit) — read the live artifact fresh, read it in full, then republish to
the same URL.
