# Wealth management domain rules

Loads whenever a piece is written for, about, or on behalf of a private client household: a
client email, quarterly review, IPS, allocation change note, market-event note, onboarding
document, meeting recap, fee conversation, estate or tax-adjacent explanation, or anything a
prospect might read.

`domain-finance.md` governs research about securities. This file governs communication with the
people whose money is in them. When a piece does both, load both; where they differ, this file
wins, because the reader is a client rather than an analyst.

## Contents
- Part 1: the client-facing compliance gate
- Part 2: performance and reporting conventions
- Part 3: asset-class-specific traps
- Part 4: client communication craft

---

## Part 1: the client-facing compliance gate

Blocking. The piece does not ship until every rule is satisfied or the violation is written into
the open-items block. A silent pass is a failure. This gate fires on drafts too, including ones
that "will get reviewed later," because the review is what this block exists to inform.

**Suitability language is the human's call, never yours.** Second person plus a specific action
is the trigger: "you should shift to short duration," "given your situation, sell the
concentrated position," "this is the right allocation for you." Quote the exact line in open
items and flag it for review. Do not quietly soften it into generic language. Softening hides a
decision the advisor is required to make and destroys the record of what the draft actually
said.

**Never state or imply a recommendation is suitable for a reader whose circumstances are not in
the document.** If the piece is going to more than one household, every recommendation is
general by construction. Say so in the text, not only in a footer.

**No performance promises, guarantees, or protection language.** "Will return," "should compound
at," "protects your downside," "locks in," "guaranteed income," "safe." Rewrite to a conditional
tied to a stated assumption, or cut the sentence. "Protects your downside" is the single most
common violation in reassurance notes written during a drawdown, which is exactly when they get
written.

**Past performance framing must not imply future results, and the bridge is usually implicit.**
A performance sentence followed by a forward-looking sentence reads as a forecast whether or not
the word "forecast" appears. Separate them, state the period explicitly, and attach the
limitation in plain words rather than boilerplate the client will skip.

**Every figure carries an as-of date and a named source.** Prices, yields, rates, balances,
returns, allocations, drift percentages, fee figures, tax rates. Figures from memory are
prohibited. If live data was not pulled, say so in the text and label the number an estimate.
An undated performance number in a client document is the defect that ends careers.

**Fees are stated in dollars and basis points, never in basis points alone.** A household reading
"42bps" does not know what it costs them. Give both, name what is included, and name what is
not (fund-level expense ratios, custody, trading, third-party manager fees). If the total cost
is not knowable from what you have, mark it `[TK: all-in cost]` rather than quoting the advisory
fee as though it were the whole number.

**Tax and legal statements stop at the general.** Describe how a mechanism works. Do not tell a
specific household what their treatment will be, do not compute their liability, and do not
recommend a filing position. Route to their CPA or attorney by name where one is known, and
flag any sentence that crosses from mechanism into their specific situation.

**No projections without the method and the range beside them.** A single-point retirement or
funding number implies precision the model does not have. Show the assumption set, show at least
a downside case, and label Monte Carlo output as probability rather than outcome. "You will have
$4.2M at 65" is prohibited regardless of what the software printed.

**Balanced risk language sits in the same passage as any action.** Not in an appendix, not in a
disclosure block at the end. If the note says trim, the adjacent lines say what would make that
wrong and what the client gives up if it is.

**Math that reaches a client deliverable is verified programmatically.** Weights to 100, drift
calculations, blended benchmark returns, contribution and attribution figures, after-fee
arithmetic, tax-lot math. Run it; do not eyeball it. Report that it was verified, and label any
figure that could not be run as unverified.

---

## Part 2: performance and reporting conventions

Getting these wrong is not a style problem. It is a misstatement.

| Convention | The rule |
|---|---|
| Net vs gross | State which, every time, in the same sentence as the number. A return with no net/gross label is unusable. Default to net for client copy. |
| Time-weighted vs money-weighted | TWR measures the manager, MWR measures the client's experience. A household that made a large contribution mid-period will see a different number than the composite. Name which one you quoted and why. |
| Benchmark | Named, with its weights if blended, and the same period and net/gross basis as the portfolio. A blended benchmark whose components are unstated is not a benchmark. |
| Period | Explicit start and end dates. "Year to date" without the as-of date is undated. Annualize only for periods over one year, and say "annualized" when you do. |
| Inception | Give the inception date whenever an inception-to-date figure appears. Short track records must state their length in the same breath. |
| Contribution vs attribution | Contribution is what a sleeve added to total return. Attribution decomposes it into allocation and selection. They are different numbers; do not use the words interchangeably. |
| Risk statistics | A return without vol, drawdown, or a risk-adjusted measure invites the reader to assume it was free. Give at least one. |
| Rounding | Match the precision of the source. Two decimals on a return sourced to the tenth is false precision. |

---

## Part 3: asset-class-specific traps

**Fixed income.** Name which yield: current yield, yield to maturity, yield to worst, SEC yield,
distribution rate. They are different numbers and the difference is the whole point in a callable
or premium bond. Distribution rate is not yield and must never be presented as income the client
can expect to persist. State duration when you make a rate argument, and state it as a
sensitivity ("roughly 4% for a 100bp move") rather than a bare number. Credit quality gets the
agency and the date. Municipal yields compared to taxable yields require the tax-equivalent
calculation shown, with the assumed rate stated, and that assumption is a general illustration
rather than the client's rate.

**Alternatives and private markets.** Marks are stale by construction; give the valuation date
and say plainly that it lags. Never compare a private mark's volatility to a public index without
saying the smoothing makes the comparison invalid. IRR is not a time-weighted return and is not
comparable to one. Name the J-curve when a young fund shows a negative number. Capital calls,
lockups, gates, and secondary-market discounts get named in any piece recommending an allocation,
not only in the subscription documents. K-1 timing gets stated whenever a tax-sensitive household
is the reader.

**Concentrated and legacy positions.** These are the emotionally loaded ones. Never write about
selling a founder or inherited position without acknowledging the basis, the tax cost, and the
non-financial attachment. A note that treats a concentrated position as a pure risk problem reads
as tone-deaf and gets ignored.

**Structured products, annuities, and insurance.** State the counterparty, the surrender terms,
the cap or participation rate, and the all-in cost including rider fees. "Principal protection"
is a credit exposure to the issuer and must be described as such.

**Cash and equivalents.** Yields move; date them. Distinguish FDIC coverage from SIPC coverage
from neither, and state which applies.

---

## Part 4: client communication craft

The reader is intelligent, not trained. They are also anxious more often than they say. Write for
someone who will read this once, on a phone, possibly while upset.

**Answer the question they actually have in the first two sentences.** In a drawdown the question
is never "what is your macro view." It is "am I going to be fine" and "did you see this coming."
Address both, honestly, before anything else. A market note that opens with macro context has
already lost.

**One idea per message.** A client email carrying a performance update, a rebalancing
recommendation, and a paperwork request will produce a response to the paperwork request only.
Split them.

**Jargon gets a one-line plain translation on first use, then use the term.** Not a glossary, not
a parenthetical every time. "Duration, which is roughly how much the bond moves for a given
change in rates, sits at 4.2 years." Then say duration.

**Numbers get context or they get cut.** "Down 8%" means nothing alone. Against what, over what
period, versus what plan, and what does it mean for the thing the client actually cares about.

**Do not perform certainty you do not have.** "I do not know how long this lasts" is stronger
than a confident forecast that ages badly, and clients remember which one you gave them. State
what you do know, what you are watching, and what would change the plan.

**Never imply the client is wrong to be worried.** "There is no reason for concern" is both
condescending and, in compliance terms, close to a guarantee. Acknowledge, then give the reason
the plan already accounted for it.

**Every recommendation names what happens if you are wrong.** This is the compliance rule and it
is also the trust rule. Advisors who state their failure case keep clients through the failure.

**Close with the specific next step, its owner, and its date.** "I will call Thursday," "sign the
attached by the 30th," "nothing needed from you." A client note with no next step generates a
phone call asking what the next step is.

**Anti-patterns.** Reassurance built on adjectives rather than the plan · "as you know" in front
of something the client does not know · a market narrative substituting for a portfolio answer ·
hedging so heavy the recommendation disappears · the quarterly letter that reports what happened
and never says what it means for this household · disclosure language dropped mid-paragraph where
it reads as an admission rather than a standard.
