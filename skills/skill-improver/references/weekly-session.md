# Weekly review session procedure

This runs once a week (or on demand) and turns accumulated log entries into proposed changes for the user to approve. The session is read-heavy and write-careful — nothing actually changes a skill file without the user signing off.

## Inputs

- `~/claude-skills/improvement-log.md` — the accumulated entries
- The skill files for any skill mentioned in the log
- Optionally, the previous review at `~/claude-skills/reviews/<prev-date>/review.md` for continuity

## Outputs

In `~/claude-skills/reviews/YYYY-MM-DD/`:

- `review.md` — the human-readable review document, grouped by skill, with rationale and evidence
- `<skill-name>.diff` — a unified diff per skill showing the proposed SKILL.md changes
- `<skill-name>.before.md` / `<skill-name>.after.md` — full before/after if a diff is too noisy (e.g., big restructures)
- `proposed-skills/<name>/SKILL.md` — draft SKILL.md for each new-skill candidate (also copied to `~/claude-skills/proposed-skills/`)

## Procedure

### Step 1 — Parse the log

Run `scripts/parse_log.py --status open --json` to get all open entries as JSON, grouped by skill. If there are no open entries, write a short review.md that says "No open entries to review" and stop. Don't manufacture proposals from nothing.

### Step 2 — Read the affected skill files

For each skill that has open entries, read its SKILL.md (and the references it points to, if the entries touch on them). Note: you have to know where each skill lives. Common locations:

- Plugin skills: under the plugin's skills directory
- User skills: typically under the skills-plugin directory

If a skill's location can't be determined, note it in review.md as "could not locate skill file — please point me at it" and move on. Don't guess and edit the wrong file.

### Step 3 — Group and synthesize

For each skill, look at all its open entries together. Common patterns:

- **Multiple entries on the same root cause** — collapse into one proposed change with all evidence cited.
- **Conflicting entries** — surface both in the review and ask the user to decide.
- **One entry, clear fix** — propose the change directly.
- **Vague entries** — flag in review as "needs more evidence" rather than fabricating a fix.

### Step 4 — Write the proposed changes

For each skill, draft the updated SKILL.md (and any reference file changes). Save:

- The diff: `diff -u old.md new.md > <skill>.diff` (or use Python's difflib if shell diff is unavailable)
- Or, for substantial rewrites where a diff is hard to read, full before/after copies

Don't actually overwrite the skill file. The user does that during approval.

### Step 5 — Handle new-skill candidates

For each `new-skill-needed` entry, draft a starter SKILL.md following the skill-creator guidance and save to `~/claude-skills/proposed-skills/<proposed-name>/SKILL.md`. Include:

- A description field that captures the trigger context from the log entries
- An outline of the procedure based on what the user actually did during the sessions that logged the entry
- A note in the review saying "this is a starter draft — recommend running the skill-creator skill to flesh it out and test it"

### Step 6 — Write review.md

Structure:

```markdown
# Skill Review — YYYY-MM-DD

## Summary

- N open entries across M skills
- K proposed changes
- L new-skill candidates
- (any conflicts or missing-info items)

## anthropic-skills:docx

**Entries (3, all open)**: 2 missing-instruction, 1 poor-output

**Proposed change**: <one-paragraph summary>

**Rationale**: <why this change addresses the entries>

**Evidence**:
- 2026-05-23 — User: "where's the logo? I thought I told you to include it"
- 2026-05-20 — (description)
- 2026-05-18 — (description)

**Diff**: see `docx.diff`

---

## (next skill)
...

## New-skill candidates

### contract-redline (3 entries over 6 weeks)

Draft at `proposed-skills/contract-redline/SKILL.md`.

Pattern: <description of recurring task>

Recommendation: run skill-creator to flesh out and test before installing.

---

## Items needing your input

- (vague entry — needs more evidence)
- (conflicting entries on X)
- (couldn't locate skill file for Y)
```

### Step 7 — Update statuses

Once review.md is written, update entries in the log:

- Proposed entries → status `proposed`
- Entries flagged "needs your input" → leave as `open` with a note in the entry body

Use `scripts/append_entry.py --update <heading>` or edit the log directly. The point is the next review doesn't re-process entries that are already in flight.

### Step 8 — Present to the user

Tell the user the review is ready and give them the path: `~/claude-skills/reviews/YYYY-MM-DD/review.md`. Offer to walk through the proposals one by one in the chat if they want, or wait for them to read on their own.

When the user approves a change, apply it (edit the actual skill file) and update the relevant log entries to `applied`. When they dismiss one, update to `dismissed` and add a one-line note in the entry explaining why (so future reviews don't re-propose the same thing).

## Style of the review

The user is choosing whether to ship changes to skills that affect every future session, so the review should be honest about uncertainty:

- If an entry is weak evidence, say so. Don't dress it up.
- If a proposed change is a judgment call between two options, surface both.
- If a skill seems fine and entries about it look like noise, recommend dismissal.

The review is not a marketing document for changes — it's a decision aid.

## When the log is huge

If there are 50+ open entries, don't try to process every one in a single review. Prioritize:

1. All `high` severity entries
2. New-skill candidates with multiple entries (suggests a real pattern)
3. Skills with the most entries (suggests a real problem)

Note in review.md that the long tail was deferred to the next review.
