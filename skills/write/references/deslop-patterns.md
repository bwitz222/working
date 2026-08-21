# Deep-pass pattern catalog

The deep-tier catalog: 24 patterns, loaded only on a deep pass.

## Contents
- How to use this catalog
- The 24 patterns
- Soul, beyond pattern removal
- Worked deep-pass example
- Before and after pairs
- When three is not a rule of three

## How to use this catalog

Scan the draft once per pattern family, not once per row. The table is a lookup list, not a checklist to narrate. Patterns already handled by the 7 quick-tier rules or by the tables in deslop-lists.md are not repeated here: filler openers, negative parallelism, rule of three, em dashes, hedging.

Two constraints on every fix. Never alter a figure, a date, a quotation, or a proper noun while cleaning. When a fix requires a fact you do not have, for example a real source to replace a vague attribution, leave a visible [TK: source for adoption figure] placeholder. Never invent the fact.

## Patterns 1 to 24

| # | Pattern | Triggers | Fix |
|---|---------|----------|-----|
| 1 | Significance inflation | stands/serves as, testament, pivotal, evolving landscape, underscores, reflects broader, indelible mark | Cut or replace with specific facts |
| 2 | Notability name-dropping | cited in [outlet list], active social media presence | Add context or remove |
| 3 | Superficial -ing phrases | showcasing..., reflecting..., highlighting..., fostering..., cultivating... | Cut or expand with real source |
| 4 | Promotional language | nestled, vibrant, boasts, breathtaking, renowned, in the heart of, groundbreaking, must-visit | Replace with neutral description |
| 5 | Vague attributions | Experts believe, Industry reports, Observers have cited, Some critics argue | Cite real source or delete claim entirely |
| 6 | Formulaic challenges | Despite challenges... continues to thrive, Future Outlook, Challenges and Legacy | Replace with specific facts |
| 7 | AI vocabulary | additionally, crucial, delve, enhance, foster, garner, interplay, intricate, landscape (abstract), pivotal, showcase, tapestry, testament, underscore, vibrant | Replace with simpler words or restructure |
| 8 | Copula avoidance | serves as, stands as, features [a], boasts [a] | Replace with is / are / has |
| 9 | Synonym cycling | protagonist... main character... central figure... hero (rotating synonyms) | Repeat the clearest word |
| 10 | False ranges | from X to Y, from A to B (non-scale pairings) | List topics directly |
| 11 | Boldface overuse | **OKRs**, **KPIs** in running prose | Remove bold |
| 12 | Inline-header lists | **Speed:** Speed improved... (bold label restating itself) | Convert to prose |
| 13 | Title Case headings | ## Strategic Negotiations And Partnerships | Sentence case |
| 14 | Emojis | rockets, lightbulbs, checkmarks in headings or bullets | Remove |
| 15 | Curly quotes | "smart quotes" | Replace with straight quotes |
| 16 | Chatbot artifacts | I hope this helps!, Let me know if..., Here is a... | Remove entirely |
| 17 | Cutoff disclaimers | As of my last training..., While details are limited... | Remove or replace with real source |
| 18 | Sycophancy | Great question!, You're absolutely right!, That's an excellent point | Remove entirely |
| 19 | Generic conclusions | The future looks bright, Exciting times lie ahead, a major step in the right direction | Replace with specific plans or cut |
| 20 | Editorializing asides | it's important to note, it is worth noting that, no discussion would be complete without, it should be emphasized | Cut, state the point |
| 21 | Section-summary restatement | a closing sentence or paragraph restating the section just read; in summary, overall, to summarize mid-document | Cut; the reader just read it |
| 22 | Formulaic transitions | Moreover, Furthermore, In addition, Additionally used as paragraph openers; Consequently | Use but / so / because / which means, or no transition at all |
| 23 | Letter-style phrasing out of context | I hope this message finds you well, Thank you for reaching out, Please do not hesitate to (in non-letter copy) | Remove |
| 24 | Heritage puffery | rich cultural heritage, enduring legacy, storied history, time-honored, deeply rooted tradition | Replace with a specific fact or cut |

## Soul (beyond pattern removal)

Pattern-clean text can still fail if it's lifeless. Vary sentence length. React to information rather than just reporting it. Let uncertainty show when real. Use first person where the register allows.

**Lifeless (technically clean):** "The agents generated 3 million lines of code. Some developers were impressed while others were skeptical."

**Has a pulse:** "3 million lines of code, generated overnight. Half the community thinks it counts, half are explaining why it doesn't. I keep thinking about those agents working through the night."

Only inject voice when register permits. Academic, legal, medical, and financial documents stay neutral.

## Worked deep-pass example

**Input:**
> AI-assisted coding serves as an enduring testament to the transformative potential of large language models, marking a pivotal moment in the evolution of software development. It's not just about autocomplete; it's about unlocking creativity at scale. Industry observers have noted adoption has accelerated from hobbyist experiments to enterprise-wide rollouts. Additionally, the ability to generate documentation showcases how AI contributes to better outcomes, highlighting the intricate interplay between automation and human judgment.
> - **Speed:** Code generation is significantly faster, reducing friction.
> - **Quality:** Output quality has been enhanced through improved training.
>
> In conclusion, the future looks bright. Let me know if you'd like me to expand!

**Output:**
> AI coding assistants speed up the boring parts: config files, test scaffolding, repetitive refactors. They're also good at sounding right while being wrong. I've accepted suggestions that compiled, passed lint, and still missed the point because I stopped paying attention.
>
> The productivity claims are hard to verify. GitHub says Copilot users accept 30% of suggestions, but acceptance isn't correctness. If you don't have tests, you're guessing.

*Changes: cut significance inflation, chatbot opener/closer, boldface bullets, -ing phrases, vague attribution ("Industry observers"), negative parallelism, false range, AI vocab, formulaic transition ("Additionally"), generic conclusion. Restructured bullets as prose. Varied rhythm.*

# Before and after pairs

## 1. Throat-Clearing + Binary Contrast

**Before:** "Here's the thing: building products is hard. Not because the technology is complex. Because people are complex. Let that sink in."

**After:** "Building products is hard, and the hard part is people rather than technology."

---

## 2. Filler + Permission-Granting

**Before:** "It turns out that most teams struggle with alignment. The uncomfortable truth is that nobody wants to admit they're confused. And that's okay."

**After:** "Teams struggle with alignment. Nobody admits confusion."

---

## 3. Jargon Stack

**Before:** "In today's fast-paced landscape, we need to lean into discomfort and navigate uncertainty with clarity. This matters because your competition isn't waiting."

**After:** "Move faster. Your competition is."

---

## 4. Dramatic Fragmentation

**Before:** "Speed. Quality. Cost. You can only pick two. That's it. That's the tradeoff."

**After:** "Speed, quality, cost: pick two."

---

## 5. Rhetorical Setup

**Before:** "What if I told you that the best teams don't optimize for productivity? Here's what I mean: they optimize for learning. Think about it."

**After:** "The best teams optimize for learning."

---

## When three is not a rule of three

Example 4's "After" keeps three items on purpose. The carve-out is stated in full in rule 6 in
deslop-rules.md and applies at every tier, not only here. Speed, quality, and cost are three
because the tradeoff has three terms; cutting one would make the sentence false. Bull, base,
and bear behave the same way, as do three named risk drivers and the three legs of a return
attribution. Meaning changes, keep three. Only cadence changes, cut to two.
