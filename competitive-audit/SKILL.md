---
name: competitive-audit
description: >
  Builds an evidence-based competitive and market landscape audit — how competitors
  frame the problem, how they position and describe their solutions, and what the
  broader market looks like. Discovers competitors and adjacent industries when the
  user doesn't already know who they are, and pauses for approval on that list before
  researching. Strategic/market focus, not a UX or visual-design critique (use
  design:design-critique for screen-level usability feedback, brand-guardian for deep
  brand identity/voice work). Use when users want to "audit the competition," "who
  are our competitors," "what does the market look like," "how are others solving
  this," "competitive landscape," or "benchmark us against the market."
---

# Competitive Audit

An evidence-based read on the competitive and market landscape: how competitors approach the problem, how they describe their solutions, and where the whitespace is. Strategic and market-level — not a screen-by-screen UX critique (that's `design:design-critique`) and not deep brand voice/identity work (that's `brand-guardian`).

## Core Principle: Evidence Over Assumptions

Same three-tier system as `buyer-journey-builder`, for consistency across the library:

✅ **Validated** — Research-backed + market proven (cite source, sample size or scale, year)
⚠️ **Validation Needed** — Logical but untested (state the gap, recommend validation)
📱 **Table Stakes** — Expected baseline across the category (absence = dealbreaker, not a differentiator)

**Always search first.** Never guess who the competitors are, what the market size is, or how a competitor positions itself without checking. Sources must be current — prioritize anything published in the last 3 years, and flag anything older as dated context rather than current fact.

## Step 1: Scope (ask upfront)

- What's the product/service, and what problem does it solve?
- Do you already have specific competitors in mind, or should this start from a blank slate?
- Industry/category and geography (local, national, global)?
- Output goal — exec summary, interactive map, strategic playbook, or slides? (see Step 7)

## Step 2: Discover competitors and adjacent industries — then pause

This is the step that's different from `buyer-journey-builder`: don't wait for the user to hand you a competitor list.

**Search for direct competitors:**
```
1. "[category] companies/brands [current year]"
2. "[category] alternatives to [known player, if any]"
3. "best [category] tools/services [current year]"
4. "[category] market leaders [current year]"
```

**Reason toward adjacent industries** — not just superficially similar categories, but industries solving the same underlying problem through a different mechanism or channel. State the logic for each one explicitly (e.g., for a meal-kit brand: grocery delivery solves the same "what's for dinner" problem via a different mechanism; ready-meal brands solve it with less prep; subscription boxes overlap on the commitment/logistics model even though the product differs).

Search pattern:
```
"how [adjacent problem] is solved outside of [category]"
"[underlying problem] alternative solutions"
```

**Compile a candidate list** — direct competitors and adjacent industries, each with a one-line rationale for why it's included.

**Pause here.** Present the candidate list to the user and get confirmation (add/remove/swap) before doing any deep research. Don't spend research effort on the wrong companies — this mirrors the same never-fully-autonomous principle the rest of this skills library follows.

## Step 3: Research the market as a whole

- Market size and growth trend (search: `"[category] market size [current year]"`, `"[category] industry trends [current year]"`)
- Market structure — segments, price tiers, business models, how the category is typically divided
- Prioritize sources the same way `buyer-journey-builder` does:
  - Tier 1: academic studies, industry association reports, government data
  - Tier 2: consulting firms (McKinsey, Deloitte, etc.), platform/market-research statistics
  - Tier 3: vendor white papers (note bias), single-source claims — use only when nothing better exists, and label as such

## Step 4: Research each approved competitor

For each competitor on the confirmed list, capture:

- **Problem framing** — how do they define or frame the problem they solve? Is it the same problem the user is solving, or a related-but-different one?
- **Solution approach** — what's their core mechanism or strategic approach, at a level above individual features or screens?
- **Positioning & messaging** — how do they describe the solution publicly (tagline, stated value prop, named target audience)? This is market intelligence on their stated position, not a brand-voice deconstruction.
- **Strategic moves** — recent funding, pivots, expansions, or shifts in direction (search recent news, not just the homepage)
- **Strengths / weaknesses** — at a strategic level: what's working for them in the market, where are they exposed
- Evidence tier (✅/⚠️/📱) on each substantive claim

## Step 5: Adjacent industries — what's transferable

For each adjacent industry on the confirmed list: what do they do differently that's genuinely transferable, and what's a false analogy (looks relevant, isn't actually applicable because the underlying constraints differ)? Be explicit about which is which — a bad adjacent-industry read is worse than not including one.

## Step 6: Strategic recommendations

Structure as:

**✅ Differentiate Here (Whitespace)**
Gaps the market isn't addressing, evidenced across multiple competitors — where there's real room to stand apart.

**⚠️ Compete on Parity (Table Stakes)**
What the category expects as baseline — not differentiating, but its absence would be a dealbreaker.

**❌ Avoid / Low Priority**
Approaches competitors tried and abandoned, or where evidence points to low differentiation value or market rejection.

## Step 7: Create the output

**Required elements regardless of format:**
- Market landscape summary (size, trend, structure — sourced)
- Competitor profiles (problem framing, positioning, strategic moves, evidence tiers)
- Adjacent industries section, with transferable-vs-false-analogy called out
- Strategic recommendations (Differentiate / Parity / Avoid)
- Methodology note — what was searched, what the candidate list was, what got confirmed
- Validation indicators (✅⚠️📱) on major claims

**Format options** (match user's stated goal from Step 1):
- **Executive Summary** (1 page) — market snapshot, top competitors at a glance, 3 key insights, top recommendation
- **Interactive Map** (HTML) — full landscape with expandable competitor detail and sourcing
- **Strategic Playbook** (multi-page) — landscape + full competitor profiles + adjacent industries + prioritized recommendations
- **Presentation** (slides) — visual landscape, key differentiators, recommended positioning, next steps

## Critical Pitfalls to Avoid

1. **Treating stated positioning as actual strategy** — a competitor's marketing copy isn't necessarily their real strategic bet; note where these seem to diverge.
2. **Confusing funding/popularity with product-market fit** — a well-funded competitor isn't automatically winning the actual problem.
3. **Ignoring category-definition differences** — a competitor may define "the market" differently than the user does; call this out rather than flattening it.
4. **Missing indirect competition** — don't stop at the obvious direct competitors; this is the entire point of the adjacent-industries step.
5. **Presenting dated data as current** — anything older than 3 years gets flagged as historical context, not current fact.
6. **False-analogy adjacent industries** — including an adjacent industry because it superficially resembles the category, without checking whether the underlying constraints actually transfer.
7. **Not distinguishing table stakes from differentiators** — expected baseline features aren't a competitive advantage even if they took real work to build.

## Quality Checklist

Before delivery, verify:
- [ ] Candidate competitor + adjacent-industry list was presented and confirmed before deep research began
- [ ] 3-5+ searches conducted for market landscape data, plus per-competitor searches
- [ ] Every market-size/trend claim has a source and year, or is explicitly labeled an estimate
- [ ] Evidence tiers (✅⚠️📱) marked on major claims
- [ ] At least one adjacent industry included, with transferability explicitly assessed
- [ ] Strategic recommendations are prioritized (Differentiate / Parity / Avoid), not just a flat list
- [ ] Sources are current (≤3 years) or explicitly flagged as dated
- [ ] Methodology/sources documented

## When User Challenges Your Work

**Good responses:**
- "You're right to push back — let me search for current data on that."
- "That was reasoning without a source. Here's what I can actually find..."
- "Fair catch — let me check whether that adjacent industry actually transfers, or if I forced the analogy."

**Bad responses:**
- Defending an unsupported claim
- Citing "obviously" or "common sense" without a source
- Assuming you know the market better than the user, who lives in it

---

**Remember:** the goal is an honest, sourced read on the competitive landscape that surfaces what's actually known vs. assumed, includes competition the user hadn't thought of, and ends in prioritized, actionable recommendations — not a flattering summary of who the competitors claim to be.
