---
name: skill-improver
description: Meta-skill that watches how skills perform during real work, logs concrete improvement opportunities to a central log, and proposes changes in batch during a scheduled weekly review. Trigger this skill whenever the user gives feedback that a skill missed, misfired, or could have done better ("that didn't work", "you should have used X", "why didn't you...", "the docx skill kept doing Y"); when a skill is invoked but the result is poor; when a task pattern recurs that has no matching skill; when wrapping up a work session and there's anything worth remembering; or when a scheduled "weekly skill review" runs. Also use it when the user asks to "log an improvement", "remember this for next time", "improve my skills", "review my skills", or sets up the auto-improvement system for the first time. Improvements to the skill-improver itself go in the same log — it watches itself too.
---

# Skill Improver

A meta-skill that turns scattered "the skill should have done X" moments into a structured improvement pipeline. It has two clearly separated modes:

1. **Observation mode** — runs *during* normal work sessions. Cheap, fast, append-only. Just notices when something is worth remembering and logs it.
2. **Review mode** — runs *during* a scheduled weekly session (or on demand). Reads the accumulated log, groups by skill, and produces proposed changes for the user to approve.

These are separate on purpose: observation has to be lightweight enough to not derail the user's actual task, and review has to be thorough enough to produce changes worth applying.

## Where things live

- **Improvement log**: `~/claude-skills/improvement-log.md` (create the directory if it doesn't exist)
- **Weekly review outputs**: `~/claude-skills/reviews/YYYY-MM-DD/`
- **Proposed new skills**: `~/claude-skills/proposed-skills/`

On the first invocation, run `scripts/bootstrap.py` — it creates the folders, the empty log with a header, and offers to schedule the weekly review.

## Observation mode

Observation mode is the default. When this skill triggers during normal work, you're almost always in observation mode (the only exceptions are the weekly session and explicit user requests like "run the review now").

**What to log.** Read `references/observation-triggers.md` for the full taxonomy with examples. The short version: log a entry when one of these happens and the cause is *generalizable* (not a one-off fluke).

- The user pushes back on how a skill behaved ("you should have...", "that's not what I wanted", "why did you...").
- A skill was invoked but produced a result the user had to correct or redo.
- A task obviously needed a skill, but none triggered (or the wrong one did).
- A task pattern repeats and there's no skill for it — candidate for a new skill.
- The user explicitly says "remember this" or "log this".
- You're wrapping up a session and notice a pattern worth capturing.

**What NOT to log.** Don't log:

- Things specific to one file or one moment that won't recur.
- User preferences that are about *them* personally rather than how a skill should behave (those belong in memory, not here).
- Issues where the skill behaved correctly and the user just wanted something different this once.

When in doubt, lean toward logging — the weekly review can dismiss noise, but it can't recover insights that were never written down.

**How to log.** Append a new entry to `~/claude-skills/improvement-log.md` using the format in `references/log-format.md`. Use `scripts/append_entry.py` for this — it handles the timestamp, the entry separator, and validates the structure. Doing it by hand is fine too if the script can't run, but the script is safer because the format has to stay parseable for the weekly review.

**Be specific.** The single most common failure mode here is logging vague entries that the weekly review can't act on. "docx skill could be better" is useless. "docx skill doesn't explain how to insert images into headers — I had to look it up via web search and the user noticed the delay" is actionable. Include the evidence (a user quote, a description of what happened) so the weekly reviewer has something to ground proposals in.

**Don't interrupt the user's actual task.** Observation mode is a side effect. Log the entry, then continue with whatever the user actually asked for. Don't announce every log entry — a brief mention at session end is fine ("I logged 2 improvement opportunities for the docx skill"), but don't narrate each one as it happens.

**End-of-session reflection.** When a session is clearly winding down (user says "thanks", "that's all", "good for now", or the work is obviously done), take a moment to look back across the session for anything worth logging that you didn't catch in the moment. This is when patterns become visible that weren't obvious during the work.

## Review mode

Review mode runs when:

- A scheduled "weekly skill review" task fires.
- The user explicitly says "run the skill review", "review my skills", "process the improvement log".
- The log has accumulated a lot of entries and the user wants to clear it.

Read `references/weekly-session.md` for the full procedure. The shape of it:

1. Parse the log with `scripts/parse_log.py` — get all open entries, grouped by skill.
2. For each skill with open entries, read the current SKILL.md, then propose changes. Output two things per skill: a markdown review section (rationale + evidence + summary of the change) and a unified diff or before/after of the SKILL.md.
3. For new-skill candidates (entries categorized `new-skill-needed`), draft a starter SKILL.md in `~/claude-skills/proposed-skills/<name>/SKILL.md`.
4. Write the full review to `~/claude-skills/reviews/YYYY-MM-DD/review.md` and present it to the user.
5. Mark all reviewed entries as `proposed` (not yet applied). When the user approves changes, mark them `applied` and actually edit the skill files. Dismissed entries get marked `dismissed` with a one-line reason.

The review never auto-applies changes. The user is always the one who says "yes, apply that". This is by design — skills shape every future session, so a regression in a skill is more expensive than a regression in a one-off task.

## Self-improvement

The skill-improver is itself a skill. When the user gives feedback about *this* skill, log it the same way — `skill: skill-improver`. The weekly review will pick it up and propose changes to its own SKILL.md and reference files. This is the whole point: every skill, including this one, gets better over time from real usage.

If you ever find yourself thinking "this skill should have logged that earlier" or "the log format is awkward to write by hand", that's a self-improvement entry. Log it.

## Bootstrapping

The first time the user asks to set this up, or the first time the skill triggers and the log doesn't exist:

1. Run `scripts/bootstrap.py` — creates `~/claude-skills/`, `~/claude-skills/reviews/`, `~/claude-skills/proposed-skills/`, and an empty log with a header.
2. Offer to schedule the weekly review using the scheduled-tasks tool. A reasonable default cron is `0 9 * * 1` (every Monday 9am). The scheduled prompt should be something like: "Run the weekly skill review: read ~/claude-skills/improvement-log.md, process all open entries using the skill-improver skill in review mode, and write the proposed changes to ~/claude-skills/reviews/."
3. Tell the user where the log lives and how the system works, briefly.

If the user already has the directory set up but no schedule, just offer the schedule. If they have both, skip bootstrapping — go straight to whatever mode is needed.

## Quick reference

| Situation | Mode | What to do |
|---|---|---|
| User pushes back mid-task | Observation | Append entry, keep working |
| Skill produced poor output | Observation | Append entry, fix the output, continue |
| Task needed a skill that doesn't exist | Observation | Append entry with category `new-skill-needed` |
| Session wrapping up | Observation | Reflect, log anything missed |
| Weekly schedule fires | Review | Run full review procedure |
| User says "review my skills" | Review | Run full review procedure |
| First-ever use | Bootstrap | Run setup, then go to relevant mode |

## Reference files

- `references/observation-triggers.md` — Detailed taxonomy of what to log, with examples
- `references/log-format.md` — Exact format for log entries (and why)
- `references/weekly-session.md` — Step-by-step weekly review procedure
- `scripts/bootstrap.py` — First-time setup
- `scripts/append_entry.py` — Append a structured log entry
- `scripts/parse_log.py` — Read the log, group by skill, filter by status
