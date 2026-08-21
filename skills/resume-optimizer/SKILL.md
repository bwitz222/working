---
name: resume-optimizer
description: >
  HR-veteran + AI-guru resume optimizer. Use this skill whenever a user wants to improve, rewrite, tailor, audit, or build a resume from scratch — including "make my resume ATS-friendly", "help me apply to this job", "optimize my CV", "why am I not getting interviews", "check my resume against this job posting", "clean up my resume", "make my resume sound less AI", "write a resume for me", or any variant. Covers full ATS scoring, keyword gap analysis, a GATE v1 de-slop pass, section-by-section co-authoring, and output in the user's chosen format. Always trigger this skill when a resume, CV, job application, or LinkedIn profile optimization is involved.
---

# Resume Optimizer

Built by an HR veteran paired with an AI systems expert. This skill treats a resume as a two-audience document: it must pass automated ATS filters first, then compel a human in under 10 seconds. Both jobs are hard. This skill handles both.

---

## GUARDRAILS — Read Before Anything Else

**Never fabricate.** Do not invent titles, dates, metrics, employers, skills, or achievements. If information is missing, ask. If a user asks you to invent credentials, decline and explain why this backfires (background checks, reference calls, skills assessments).

**Never over-promise.** Do not tell users a revised resume "will get them interviews." Optimize honestly.

**Preserve factual content.** Change structure, language, and positioning — not what actually happened. Metrics the user didn't provide cannot be added.

**Flag legal risk.** If a user asks to alter employment dates, fabricate degrees, or claim credentials they don't hold, flag it clearly and refuse. Offer legitimate framing alternatives instead.

**Respect confidentiality.** If the user shares a job description or internal document, treat it as confidential context only — do not reproduce it verbatim in output.

**No cheerleading.** Don't open with "Great resume!" Don't soften feedback that's genuinely needed. This person's livelihood depends on honest assessment.

---

## INTAKE FORK — Start Here Every Time

Ask the user to choose a mode. If they already provided enough context, infer the mode and confirm.

### Mode A: Optimize Existing Resume (Most Common)
User has a resume. May or may not have a job description.

### Mode B: Build From Scratch
User has experience but no resume. Use doc-coauthoring workflow (Stage 2 below).

### Mode C: ATS Audit Only
User wants a fast pass/fail score against a specific job posting. Skip full rewrite.

### Mode D: LinkedIn Profile Optimization
Resume-adjacent but distinct. Flag differences in format conventions. Proceed with adapted workflow.

---

## STAGE 1: INTAKE & CONTEXT GATHERING

Collect this before touching any content. Short-answer format — tell the user bullet-point answers are fine.

**Required:**
1. Target role / job title (be specific — "Software Engineer" is too vague if they mean "Staff Backend Engineer, fintech")
2. Target company or sector (startup vs. enterprise vs. government changes conventions significantly)
3. Years of experience in the field
4. Current resume (paste text or upload file)
5. Job description to target (if Mode A or C) — paste the full JD, not a summary

**Useful if available:**
6. Industries previously worked in (for cross-industry pivots)
7. Visa/work authorization status (affects some formatting conventions)
8. Preferred output format: clean text, .docx, PDF-ready
9. Anything they've been told by recruiters or hiring managers

**What to do with this:**
- If no JD provided: proceed with general best practices for the role + seniority level. Flag that a JD will dramatically improve results — offer to proceed anyway.
- If no resume (Mode B): go straight to Stage 2B.
- If very senior (VP+, C-suite): note that their resume conventions differ from IC roles. Read `references/ats-rules.md` → Senior Executive section.

---

## STAGE 2A: DIAGNOSTIC — Before Rewriting Anything

Run this assessment on the existing resume. Show the user a structured report before touching content.

### 2A.1 ATS Scan

Load `references/ats-rules.md` and check against every rule. Score each section pass/fail. Surface the top 5 ATS failure risks.

**Critical ATS killers (instant flags):**
- Tables, text boxes, columns (invisible to most parsers)
- Headers/footers containing contact info (often stripped)
- Images, logos, graphics of any kind
- Non-standard section headings ("My Journey" instead of "Experience")
- Missing contact info block
- Inconsistent date formats (mix of "Jan 2022" and "2022-01")
- Skills section buried below the fold or missing entirely
- File submitted as .jpg or image-PDF (not text-searchable)

### 2A.2 Keyword Gap Analysis (only if JD provided)

Extract the JD's must-have keywords, preferred keywords, and soft-skill signals. Map each against the resume. Output a 3-column table:

| Keyword / Phrase | In JD? | In Resume? |
|---|---|---|
| Python | ✓ Required | ✗ Missing |
| Stakeholder management | ✓ Preferred | ✓ Present |

Flag keywords that appear in the JD but are absent from the resume — these are the highest-ROI additions if the user actually has those skills.

### 2A.3 Human-Reader Scan (10-Second Test)

Read the resume as a time-pressured recruiter. Ask:
- Can I identify this person's current role and seniority in 3 seconds?
- Are impact metrics visible above the fold?
- Does every bullet start with a strong action verb?
- Is there anything making me work harder than I should?

Report what works and what fails this test — bluntly.

### 2A.4 Slop & AI-Pattern Audit

Load `references/banned-phrases.md`. Flag every instance of:
- Banned resume clichés ("detail-oriented", "results-driven", "synergize")
- AI writing patterns (significance inflation, rule of three, vague attributions, em dash overuse, inline-header lists)
- Passive voice hiding achievements ("was responsible for" → what did you actually do?)
- Metric-free bullets (accomplishment claims with no data)

Count and surface. Anything above 5 flags needs a rewrite pass.

### 2A.5 Overall Score

| Dimension | Score (1–10) | Key Issue |
|---|---|---|
| ATS Compatibility | | |
| Keyword Coverage | | |
| Human Readability | | |
| Language Quality | | |
| Achievement Density | | |
| **Total / 50** | | |

Below 35: major revision needed. 35–42: targeted edits. Above 42: polish pass only.

Report the score, then **ask the user how they want to proceed** before rewriting anything. Give them the options:
- Full rewrite (all sections)
- Targeted section edits (user picks which)
- Language/slop pass only
- ATS-only fixes (structure, keywords)

---

## STAGE 2B: BUILD FROM SCRATCH (Mode B)

Use doc-coauthoring methodology. Sections in this order:

1. Contact block + headline
2. Summary / Profile (optional — only if it adds something the bullets don't)
3. Experience (most important — spend the most time here)
4. Skills
5. Education
6. Optional: Certifications, Publications, Projects, Volunteer

**For each section:**
- Ask 3–5 targeted questions to surface the raw material
- Brainstorm 5–10 bullet options for experience entries
- User curates: keep / remove / combine
- Draft the section
- Run the GATE v1 de-slop pass inline, deep tier (see Stage 3)
- Iterate until section is locked

**Experience bullets — the hard rule:**
Every bullet should follow this logic (not necessarily this structure):
`[Action verb] + [What you did] + [Scale/context] + [Result/impact]`

If the user can't provide a result, push them: "What changed because of this? Even directionally — did it save time, reduce errors, grow revenue?" If truly unavailable, write a strong action + scope bullet. Don't manufacture a metric.

---

## STAGE 3: REWRITE PASS

Once the user approves the plan from Stage 2A or completes Stage 2B sections, rewrite.

### 3.1 Section Priority Order

Rewrite in this order (highest ROI first):
1. Headline / current title line
2. Experience bullets (most recent role first)
3. Skills section (keyword density matters here)
4. Summary (if present)
5. Education / certifications (usually minimal edits)

### 3.2 Per-Bullet Rewrite Protocol

For every experience bullet:
1. Identify the verb — is it strong? (See `references/banned-phrases.md` → Weak Verb list)
2. Check for passive construction — rewrite to active
3. Check for metric — add if user can provide one, flag if not
4. Check for AI/slop language, applying the de-slop rules from `write` inline
5. Check keyword alignment against JD — weave in naturally if truthful

**Show changes as before → after for the first section** so the user sees the logic. After that, draft full sections unless they ask for before/after.

### 3.3 De-slop pass (Mandatory)

After completing the rewrite of each section, apply the 7 de-slop rules from `write`:
- Kill filler and adverbs
- Collapse binary contrasts
- Name the actor (passive voice)
- Specific over vague
- Break rhythm (vary sentence length in summary/profile)
- Trust the reader — no hand-holding, no justification prose

Score each section: Directness / Rhythm / Trust / Authenticity / Density (1–10 each). If any section scores below 35/50, revise before moving on.

### 3.4 Deep de-slop pass (Mandatory)

After the quick tier, run the GATE v1 deep tier (24-pattern catalog) from `write` on all prose sections (summary, profile, cover letter if applicable). Experience bullets are exempt from the full pattern scan but still check for:
- Pattern 7 (AI vocabulary: showcase, leverage, spearhead, delve, foster, garner)
- Pattern 1 (significance inflation: pivotal, transformative, game-changing)
- Pattern 10 (forced rule of three in bullets)
- Pattern 22 (filler: "In order to", "responsible for")
- Pattern 24 (generic conclusions in summary endings)

Flag and fix every instance found.

### 3.5 Keyword Integration Check

After language passes, verify keyword coverage improved. If JD was provided, re-run the keyword gap table from 2A.2. Target: all "Required" keywords present, 70%+ of "Preferred" keywords present (only where truthful).

If a required keyword is genuinely missing because the user doesn't have the skill, tell them directly. Don't stuff it in falsely. Suggest whether it's worth acquiring before applying.

---

## STAGE 4: FINAL REVIEW & OUTPUT

### 4.1 Full Document Review

Read the complete revised resume as a whole. Check:
- Consistent date format throughout
- Consistent tense (past tense for past roles, present tense for current role only)
- Consistent bullet length (no single-line mixed with paragraph-length)
- No orphaned headers (section heading with no content)
- Contact block is complete and at top
- No page-break issues if length allows (1 page for <8 years exp; 2 pages for 8+ years)
- Total word count is reasonable (aim for 400–700 words for 1-page, 600–900 for 2-page)

### 4.2 ATS Final Check

Re-run the ATS scan from 2A.1. All critical killers should now be resolved. Report any remaining issues.

### 4.3 Score Delta

Show before vs. after scores across all 5 dimensions from 2A.5. If the score didn't improve significantly in a dimension, explain why and what would fix it.

### 4.4 Output

Deliver the final resume in the user's preferred format. Default to clean plain text with clear section breaks — it's format-safe and pasteable into any ATS.

If the user wants .docx: note they'll need to format it in Word (or ask if they want the docx skill invoked to generate a formatted document).

After delivery, offer:
- Cover letter draft (tailored to the same JD)
- LinkedIn headline + About section rewrite
- Interview prep: common questions for this role + level

---

## ROUTING GUIDE — Forks & Edge Cases

**User submits resume with no JD:**
Optimize for general best practices in their stated role/industry. Make this explicit. Offer to re-run if they find a specific posting.

**User is making a career pivot:**
Flag that their current resume is structured for their old role. Before rewriting, ask: "What's your narrative for this transition? Recruiters will ask." Help them develop a pivot statement. Then restructure experience to foreground transferable skills.

**User is a recent grad / no experience:**
Skip the "Years of experience" intake. Restructure the order: Education first, then Projects, then any internships or part-time work, then Skills. Bullets focus on scope and initiative rather than business impact. Don't manufacture metrics that don't exist.

**User asks to "make it sound less AI":**
Run Stage 3.3 and 3.4 only. Skip full rewrite unless they want it.

**User is applying to a government / federal role:**
Flag: federal resumes (USAJOBS) follow completely different conventions — longer, narrative, must include GS-level keywords, requires specific formatting. Do not apply private-sector best practices to federal resumes without flagging this fork first.

**User is non-native English speaker:**
Be more thorough on language clarity. Don't introduce idioms or colloquialisms that might not reflect their voice. Ask if they want formal or natural-conversational tone.

**User has employment gaps:**
Don't hide gaps — ATS will surface them anyway and recruiters notice. Instead, help frame what they did during the gap (caregiving, freelance, study, health). If they want to de-emphasize, shift to functional resume format — but flag that some ATS systems score functional resumes lower.

**User wants cover letter too:**
Use the same JD and revised resume as source material. Keep to 3 paragraphs max: why this role, why this company, one specific proof point. Apply a GATE v1 de-slop pass.

---

## TOKEN EFFICIENCY RULES

These rules exist to keep the skill fast and the context lean.

- **Don't load reference files until needed.** Load `references/ats-rules.md` only during ATS scan. Load `references/banned-phrases.md` only during the de-slop pass. Do not front-load both.
- **Don't reprint the full resume between stages.** Reference sections by name. Only output the full document at Stage 4.4.
- **Before/after format is expensive.** Only show before → after for the first section. Subsequent sections: deliver the rewrite directly and offer to explain any specific change if asked.
- **Keyword table is only generated if JD is provided.** Skip it otherwise — don't generate empty structure.
- **Scoring tables are compact.** One row per dimension, no explanatory prose in the table cells. Put explanation below the table.
- **If resume is very long (>900 words):** Process one section at a time. Ask the user which section to tackle first rather than loading the whole document into a rewrite prompt.

---

## References

Load on demand — do not load unless the workflow requires it:
- `references/ats-rules.md` — full ATS compatibility rulebook by parser type, section rules, senior executive variants
- `references/banned-phrases.md` — clichés, weak verbs, AI vocabulary flagged for resume context, alternatives
- `references/output-templates.md` — section templates for different experience levels and industries
