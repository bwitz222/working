# ATS Compatibility Rules

## Why ATS Matters

Most companies with 50+ employees use an Applicant Tracking System (ATS) to parse resumes before a human ever sees them. The parser converts your PDF or Word doc into structured data — name, contact, experience entries, skills. If the parser fails, your resume goes into a black hole. This document covers the rules that keep that from happening.

The big ATS platforms in enterprise: Workday, Greenhouse, Lever, iCIMS, Taleo, ADP, BambooHR. Each has quirks, but core parsing rules apply across all of them.

---

## CRITICAL FAILURES — Instant Rejection Risk

These will cause partial or total parse failure on most systems:

| Issue | Why It Breaks | Fix |
|---|---|---|
| Multi-column layout | Parsers read left-to-right, top-to-bottom. Two columns produce jumbled data | Single column only |
| Text boxes | Content in text boxes is often invisible to parsers | Delete text boxes; use normal paragraphs |
| Tables for layout | Same parsing issue as columns | Use plain text with consistent spacing |
| Headers/footers with contact info | Many parsers skip header/footer regions | Move all contact info into the main body |
| Images, logos, icons | Cannot be parsed | Remove entirely |
| Non-standard section headings | Parser can't categorize the data | Use standard labels (see Section Headings below) |
| Skills section missing | ATS cannot score keyword match without a dedicated skills section | Always include |
| Image-based PDF | Scanned or image PDF has no selectable text | Export from source as text-based PDF |
| Decorative dividers or shapes | Some parsers choke on symbols used as visual separators | Use a plain line or no divider |

---

## Section Headings — Safe vs. Unsafe

Parsers are trained to recognize standard headings. Non-standard headings may be skipped or miscategorized.

**Safe (use these):**
- Experience / Work Experience / Professional Experience
- Education
- Skills / Technical Skills / Core Skills
- Summary / Professional Summary / Profile
- Certifications / Licenses
- Projects
- Publications
- Volunteer / Volunteer Experience

**Risky (avoid unless testing):**
- "My Story" / "Career Journey" / "About Me" (parsers don't know what to do with these)
- "Where I've Been" / "What I've Built" (creative but ATS-hostile)
- "Core Competencies" mixed with "Skills" in the same resume (creates duplicate fields, confuses scoring)

---

## File Format Rules

| Format | ATS Safety | Notes |
|---|---|---|
| .docx | Safest | Best parser compatibility across all major ATS |
| .pdf (text-based) | Generally safe | Most modern ATS parse well; avoid if applying via email to old systems |
| .pdf (image/scanned) | Will fail | No selectable text — never submit this |
| .txt | Parses cleanly | Loses all formatting; acceptable for some systems, not ideal |
| .odt, .pages, .wps | Risky | Many ATS reject or error on these |

**Default recommendation:** .docx for application uploads. Keep a text-safe version for pasting into web forms.

---

## Date Format Rules

ATS uses dates to calculate tenure and sort experience. Inconsistency creates parse errors.

**Use consistently throughout:**
- `Month Year` format: `Jan 2020 – Mar 2023` (preferred)
- Or `MM/YYYY`: `01/2020 – 03/2023`
- Or year-only for education: `2018 – 2022`

**Never mix formats in the same document.** Mixing `January 2020` with `01/20` will confuse tenure calculation.

**Current role:** Use `Present` not `Now`, `Ongoing`, or `Current`.

---

## Contact Block Requirements

The contact block is parsed first and must be in the main body (not a header/footer).

**Required:**
- Full name (first line, largest text)
- City, State (or Country if international — do not include full address for privacy)
- Phone number
- Professional email address
- LinkedIn URL (optional but strongly recommended)

**Optional:**
- GitHub / Portfolio URL (for technical roles)
- Personal website

**Do not include:** Photo, date of birth, nationality, marital status (illegal to request in US hiring; including it can create bias risk and signal unfamiliarity with norms).

---

## Keyword Density Guidelines

ATS systems score resumes by keyword match against the job description. More match = higher rank.

**Where keywords matter most (in order):**
1. Skills section — highest weight in most ATS
2. Job titles — must match or closely mirror the JD title
3. Experience bullets — contextual keyword presence
4. Summary — secondary weight
5. Education section — degree/field keywords

**Keyword stuffing warning:** Hiding keywords in white text (same color as background) used to work in 2015. Modern ATS detect it and flag the resume as fraudulent. Don't do it.

**Natural density target:** Core skills should appear 2–3 times naturally across the document. No need to stuff.

---

## Skills Section Rules

The skills section is the primary keyword matching target for most ATS.

**Format:** Simple comma-separated list or short bullet list. Do NOT use columns, meters, icons, or proficiency bars — these either parse incorrectly or create bias questions (what does "4/5 stars in Python" actually mean?).

**Organize by category if list is long:**
```
Languages: Python, SQL, R
Frameworks: Django, FastAPI, dbt
Tools: Snowflake, Airflow, Tableau
Certifications: AWS Solutions Architect (Associate)
```

**Avoid self-assessments:** "Advanced Python" vs. "Python" — the adjective doesn't help ATS and invites skepticism from humans.

**Include the exact string from the JD where possible:** If the JD says "Microsoft Excel" don't just write "Excel." If it says "React.js" not just "React."

---

## Job Title Optimization

ATS matches your title against the JD title. Exact or near-exact match scores highest.

**Rule:** Use your official job title exactly as it appears on your records (background checks verify this). But you can add a clarifying descriptor in parentheses if your internal title is obscure:
- `Software Engineer II (Backend, Growth Team)` — adds context without fabricating a different title
- Do NOT change "Software Engineer II" to "Senior Software Engineer" if that wasn't your actual title

**For freelance / consulting:** Use `Freelance [Role] / [Your Name] Consulting` — ATS needs an employer name in that field.

---

## Senior Executive Resume Notes (VP+, C-Suite)

Executive resume conventions differ from individual contributor rules:

- **Length:** 2–3 pages is acceptable and often expected at VP+
- **ATS relevance:** Executive roles are often filled via recruiting firms or referrals, not cold ATS submissions — optimize for human readers first, ATS second
- **Metrics focus:** Board-level outcomes, P&L ownership, headcount led, budget managed — these are the signals executives are scored on
- **Summary is mandatory:** At executive level, a strong 3–5 line summary is standard. It should position their leadership philosophy and scope, not just list job functions
- **Skills section:** May be replaced by "Core Competencies" — a list of 6–12 leadership-level capabilities. This is acceptable at executive level; not recommended for IC roles
- **Education placement:** Goes last at this level, even for Ivy credentials — experience dominates

---

## Common ATS Parser Behaviors by Platform

### Workday
- Aggressively parses contact info — if phone number format is unusual (country codes without +), it may parse incorrectly
- Tables will break; confirmed reports of column layouts creating output like "RoleSoftware at Engineer Google"
- Date parsing is strict — use `Month YYYY` format

### Greenhouse
- Generally more lenient parser
- Handles PDFs well
- Skills section parsed well; keyword matching is strong

### Lever
- Strong PDF support
- More modern parser; handles some layout variation
- Still fails on image-based PDFs

### Taleo (Oracle)
- Oldest major ATS; strictest parser
- Plain .docx is strongly recommended
- Known to fail on any table use
- Often used in large enterprises and government contractors

### iCIMS
- Mid-tier parsing ability
- Handles most standard .docx files well
- Text boxes will fail consistently

---

## ATS Score Thresholds (Approximate)

Most ATS rank candidates by score. Typical gating thresholds:

- **70%+ match:** Recruiter sees resume
- **50–70%:** May appear in search but may be filtered in competitive roles
- **Below 50%:** Typically auto-filtered in high-volume roles

These are approximations — every company sets their own thresholds. The goal is above 70% on required keywords.
