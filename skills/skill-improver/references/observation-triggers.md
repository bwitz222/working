# Observation triggers

This is the detailed taxonomy of when to log an improvement entry. SKILL.md has the short version; this file has examples and judgment calls.

## The core question

Before logging, ask: "If a future Claude session were running with an improved version of this skill, would this issue go away?"

- **Yes** → log it. That's exactly what this system is for.
- **No, it was a one-off** → don't log. Noise in the log makes the weekly review worse.
- **Unsure** → log it with severity `low`. The weekly reviewer can dismiss it cheaply.

## Categories

Each entry has a `category` field. Use the closest match.

### `missing-instruction`

The skill exists and is roughly right, but it lacks specific guidance that would have prevented the problem.

**Example.** User asked for a Word doc with a company logo in the header. The docx skill produced the doc but used the wrong python-docx API for header images and the logo didn't render. The skill should include a "headers and footers" section with a working code snippet.

### `wrong-trigger`

The skill either fired when it shouldn't have, or didn't fire when it should have. This is usually a description-field problem.

**Example.** User asked to "process the spreadsheet from accounting and flag anomalies". The xlsx skill should have triggered but didn't, because the description emphasizes file creation/editing and undersells data analysis.

**Example.** The docx skill triggered for "summarize this PDF", which it shouldn't have — pdf should have won.

### `poor-output`

The skill triggered and followed its instructions, but the output was bad for reasons traceable to the skill itself (not the user's prompt or external constraints).

**Example.** The pptx skill always produces 16:9 slides even when the user pastes content that's clearly portrait-oriented (a long form, a tall infographic). The skill should at least consider aspect ratio.

### `inefficient-workflow`

The skill worked, but took a roundabout path. Often means a bundled script would help, or an early step in the skill is sending Claude down the wrong path.

**Example.** Every time the analyze skill runs on a CSV, the subagent writes its own profile_csv.py helper. That should be a bundled script.

### `new-skill-needed`

The user did something that didn't match any existing skill, and the pattern looks like it'll recur.

**Example.** The user asked Claude to compare two contracts side-by-side and generate a redline. No existing skill covers contract comparison specifically. If this is a recurring task for the user, it's a new-skill candidate.

For this category, the entry should describe the *pattern*, not just the one task. "User compared two contracts" is weak. "User regularly needs to redline contracts against a master template — this happens monthly during vendor reviews" is strong.

### `self-improvement`

The skill-improver itself could have done better — logged something it missed, used a clearer format, etc. Use `skill: skill-improver` for these.

## Severity

- **low** — minor polish, edge case, nice-to-have
- **medium** — affects normal usage, user noticed but worked around
- **high** — actively misleads or wastes significant time

Don't over-think this. The reviewer can recalibrate during the weekly pass.

## What NOT to log

These are common mistakes — entries that look reasonable but pollute the log.

**One-off corrections that don't generalize.** The user wanted the doc title to be "Q4 Review" not "Q4 Report". That's a prompt-specific fix, not a skill issue.

**User preferences about themselves.** "The user prefers concise summaries." That belongs in memory or CLAUDE.md, not in a skill log. (Unless every skill is producing verbose output, which would be a skill-level issue.)

**Frustration without a concrete cause.** "User seemed annoyed at the docx output." Don't log unless you can articulate what specifically should change.

**Speculation about hypothetical users.** "Other users might want X." We're improving skills based on this user's actual usage. Speculative entries crowd out real ones.

**Things you fixed mid-task and the user never noticed.** If Claude routed around a skill quirk silently and the output was fine, no log entry needed. The skill is working.

## Evidence

Every entry includes an evidence block. Strong evidence makes the difference between a proposal the user accepts and one they dismiss.

**Strong evidence.** A direct user quote, a description of what the skill did vs. what the user wanted, a count of how many times this came up in the session.

**Weak evidence.** "I think the user would prefer...", "It seemed like...", "Generally..."

If you don't have concrete evidence, the entry probably shouldn't exist yet. Wait until you do.

## End-of-session reflection

When the user signals the session is done, spend a brief moment looking back. Questions to ask yourself:

- Were there moments where a skill almost-but-not-quite did the right thing?
- Did the user have to redirect Claude multiple times around the same issue?
- Were there tasks I had to figure out from scratch that felt like they should have had a skill?
- Did any skill produce output the user asked me to redo?
- Was there friction I worked around silently that's worth surfacing?

If any of those produce a concrete answer, log it. If not, don't force entries — empty reflection is fine.
