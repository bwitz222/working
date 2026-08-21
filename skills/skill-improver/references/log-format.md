# Log format

The improvement log is a single markdown file at `~/claude-skills/improvement-log.md`. New entries go at the **top** (newest first) so the weekly review sees the most recent context first.

## File header

The file starts with this header (created by `bootstrap.py`):

```markdown
# Skill Improvement Log

Entries newest at the top. Each entry begins with `## ` and ends at the next `## ` or end of file.

Statuses: open · proposed · applied · dismissed

---
```

Do not delete the header — `parse_log.py` uses the first `---` after the header as the boundary between header and entries.

## Entry format

Each entry is a level-2 heading with structured fields, followed by free-form sections. Example:

```markdown
## 2026-05-23 14:32 — anthropic-skills:docx — missing-instruction

- **skill**: anthropic-skills:docx
- **category**: missing-instruction
- **severity**: medium
- **status**: open

**What happened**: User asked for a Word doc with a company logo in the header. The docx skill produced the doc but used the wrong python-docx API for header images — the logo didn't render and the user had to point out the missing image.

**Proposed improvement**: Add a "Headers and footers" section to docx references with a working python-docx snippet for inserting images into header sections, including the gotcha that the section's header.is_linked_to_previous must be False.

**Evidence**:
> User: "where's the logo? I thought I told you to include it"

Claude initially used `paragraph.add_run().add_picture()` inside a header, which fails silently on Word headers. Took ~3 tool calls to discover the right pattern.

---
```

## Field rules

- **Heading**: `## <ISO date and time> — <skill name> — <category>`. The exact format matters — `parse_log.py` splits on these.
- **skill**: Full identifier including plugin prefix if applicable (e.g., `anthropic-skills:docx`, `data:analyze`, or just `skill-improver` for unprefixed user skills).
- **category**: One of `missing-instruction`, `wrong-trigger`, `poor-output`, `inefficient-workflow`, `new-skill-needed`, `self-improvement`.
- **severity**: One of `low`, `medium`, `high`.
- **status**: One of `open`, `proposed`, `applied`, `dismissed`. New entries are always `open`.
- **What happened**: 1-3 sentences describing the situation.
- **Proposed improvement**: Concrete change you'd make. If you don't have a specific proposal yet, write "TBD — needs reviewer judgment".
- **Evidence**: User quote (with `>`), or description of observed behavior. Strong evidence makes the weekly review's job easier.
- **Separator**: `---` after each entry.

## Why this format

A few things were considered and rejected:

- **Pure JSON/JSONL.** More parseable but harder for the user to read or edit by hand. They might want to dismiss or edit entries directly in their editor.
- **Per-skill files.** Scatters context — the weekly review wants to see everything in one place.
- **YAML frontmatter per entry.** Looks cleaner but adds parsing complexity and the bullet-list of fields is more familiar.

The bullet-list format gives us readability for humans and a regex-parseable structure for `parse_log.py`. The status field is the one that gets edited often — the weekly review flips entries from `open` to `proposed` and (after approval) to `applied`.

## Editing existing entries

It's fine to edit entries by hand — especially status. The weekly review will read whatever's current in the file. If you change the heading line, make sure it still matches the format `## <date> — <skill> — <category>`.

If multiple entries about the same thing accumulate before a review, that's signal not noise — leave them separate. The weekly reviewer will see the cluster and weight the proposal accordingly.
