---
name: market-landscape-builder
description: Build evidence-backed market/category landscape briefings — why a market matters now, what's broken about how it's served, the opportunity size, and where the underserved gap sits. Leads with findings before evidence; sizes and visualizes the opportunity rather than just describing the landscape. Use when users want to understand a market or category, ask "tell me about the market," need competitive landscape analysis, want audience/opportunity sizing, or need to justify why a business problem is worth solving. Trigger for "tell me about the market," "market landscape," "competitive landscape," "category analysis," "why does this matter," "size the opportunity," "where's the opportunity," or requests to build the evidence case for a business direction. Complements buyer-journey-builder — that skill maps the path a customer takes; this skill establishes why the market is worth entering and where the gap is. Running both together produces a fuller strategic picture.
---

# Market Landscape Builder

Build evidence-backed market landscapes that triangulate proof rather than pile up citations.

## Core Principle: Triangulate Evidence Types, Not Just Sources

A finding backed by four *different kinds* of evidence pointing the same direction is far more durable than one backed by ten citations of the same kind. One weak source shouldn't be able to sink the whole case — and it won't, if the case never depended on a single evidence type to begin with.

**Always search first.** Never assert market size, sentiment, or competitive positioning without data behind it.

## The Five Evidence Lenses

Every finding gets tagged with which lens(es) support it:

💭 **Attitudinal** — how people feel or perceive (surveys, sentiment studies, stated preferences)
🖱️ **Behavioral** — what people actually do (channel usage, research habits, purchase patterns, AI-assisted discovery/GEO behavior)
📊 **Market Sizing** — how big is the audience, category, or addressable opportunity
💰 **Economic** — dollar value, cost, value-at-stake, willingness to pay
🔍 **Competitive Artifact** — a specific, describable, falsifiable observation about what a competitor actually shows, says, or does (a screenshot, a stated policy, a quote — never a vibe or general impression)

## Quick Start Process

### 1. Scope (ask upfront)

- What market/category, and what decision is this research in service of?
- Target audience — demographics, segment, geography?
- Are competitors known, or does the field need discovery first?
- Output goal: category briefing, competitive teardown, full landscape deck, or raw evidence table?

### 2. Research (search before asserting anything)

**Essential searches — fill the brackets, run literally:**
```
1. "[category] market size [current year]"
2. "[audience] attitudes toward [category]"
3. "[category] customer satisfaction benchmark"
4. "[competitor] [category] experience"
5. "[category] willingness to pay [current year]"
6. "[audience] [category] research behavior" (how they discover/evaluate — include AI chatbot/GEO-specific variants like "[category] AI chatbot research" when the audience's discovery behavior is in scope)
```

**Prioritize these sources (same tiering as buyer-journey-builder):**
- Tier 1: Academic studies, industry association reports, government data
- Tier 2: Consulting firms (McKinsey, Deloitte, Forrester, Gartner), reputable platform/syndicated research
- Tier 3: Vendor white papers (note bias), single-source claims, aggregator content (flag and avoid where a better source exists)

**When data is limited:**
- Triangulate from adjacent categories
- Label as assumption: "Estimated based on [adjacent category]..."
- Recommend validation: "Test via [interviews/survey]"

### 3. Show the Math on Every Derived Number

Never assert a calculated figure without stating the formula and citing each input separately.

- ❌ "This represents a $16B opportunity."
- ✅ "11.6M category seekers × $1,400 average annual policy value = ~$16B opportunity (population: [source, year]; value: [source, year])."

Two independently sourced inputs multiplied together is far more defensible than one asserted total.

### 4. Ground Every Competitive Claim in an Artifact

A claim about a competitor needs a specific, describable thing behind it — not an opinion.

- ❌ "Competitor X has a confusing checkout flow."
- ✅ "Competitor X's quote flow requires 14 fields before showing an estimate, with no coverage explanation at any step (observed [date])."

### 5. Apply the Validation Gate

**✅ Market-Validated requires:**
- 3+ of the 5 evidence lenses represented, AND
- No single lens carrying more than 2 of the total citations for that finding

**⚠️ Validation Needed when:**
- Fewer than 3 lenses represented
- Extrapolated from an adjacent category
- Logical but unproven

**Action required for ⚠️ findings:**
- State the evidence gap explicitly
- Recommend specific validation (survey, interview, pilot)

### 6. Lead With the Finding, Not the Evidence

State each major finding in one sentence before presenting the lenses that support it. The evidence explains the finding; it doesn't replace it. A reader should understand what you concluded before they see why — never make them assemble the conclusion themselves from a pile of stats.

- ❌ "IBISWorld: $169.8B, -0.1% YoY. NAHB: 940,000 starts, +1%. NAHB HMI: 37-39, below breakeven since April 2024. Fannie Mae: ~25% think it's a good time to buy..."
- ✅ "This market isn't growing — builders are competing for a fixed pool of buyers, not riding category expansion. Two independent sources agree: [then the evidence]."

**Placement depends on the output shape, not a fixed rule:**
- **Briefings, evidence tables, anything meant to be skimmed or read partially** — lead with the finding, every time. The reader may not reach the end.
- **Presentation decks meant to be experienced in sequence** — the finding can land at the climax instead of the top, the way a narrative arc builds context → tension → stakes → payoff (this mirrors how a locked pitch narrative might structure its own emotional arc — check whether the project already has one before deciding placement). Front-loading the conclusion can undercut a deck's built momentum even though it strengthens a quick-reference document. Ask which mode you're building for if it isn't obvious from the stated output goal in Step 1.

Never make the reader do the synthesis work themselves — the only question is whether they get it in sentence one or at the arc's peak.

### 7. Carve Out the Opportunity, Not Just the Landscape

A landscape describes what's true. This step identifies where the gap is that nobody's currently serving well, and sizes it.

- **Identify the underserved segment** — based on the attitudinal, behavioral, and competitive findings already gathered, who is the market currently failing to serve well? This should fall out of the lenses already triangulated, not be asserted fresh.
- **Size it with the same math-showing discipline as Step 3** — population × value, each input cited separately. Never assert a dollar opportunity without showing the formula.
- **Frame it as dual advantage where possible** — immediate value capture (revenue/share available now) + future pipeline value (why this segment compounds over time), not just a single static number. This mirrors how the strongest version of this argument shows both the now and the later.
- **Visualize derived dollar figures by default.** Any time this step produces a calculated opportunity size, treat a visual (chart, sized comparison, segment breakdown) as the default output, not an optional add-on — a stated number is easy to skim past; a sized visual is what makes an opportunity register. Use whatever visualization tooling is available in the current environment.

### 8. Assemble

Pick the shape based on what the research is for:

- **Category Briefing** (1-2 pages): the case for why this market/audience matters, top findings by lens, source list. **Default to HTML output using `assets/category-briefing-template.html` as the structural and visual reference** — grid-based lens cards, a boxed headline finding, a dark opportunity block at the close, sparing color (one accent used only for emphasis, not decoration). Reuse its CSS approach rather than inventing new styling each time; swap in the current findings, sources, and numbers. This is what makes output consistent run to run, the same way a fixed taxonomy makes findings consistent.
- **Competitive Teardown**: artifact-by-artifact review of how competitors currently serve the category, gaps identified. Can reuse the template's artifact-grid section standalone.
- **Full Market Landscape Deck**: attitudinal + behavioral + market sizing + economic + competitive, assembled into a narrative arc (mirrors the "why this is critical → the challenge → the stakes → the opportunity → the imperative" structure)
- **Raw Evidence Table**: findings tagged by lens and validation status, for someone else to build from

## Critical Pitfalls to Avoid

1. **Piling up one evidence type** — ten attitudinal stats isn't triangulation, it's repetition
2. **Recycled/aggregator stats treated as primary** — if a number appears on ten SEO-farm "statistics roundup" pages with no traceable original source, it's not usable
3. **Single-source claims presented as settled fact** — one survey is a data point, not a conclusion
4. **Derived numbers asserted without showing the formula** — always show the multiplication, always cite each input
5. **Competitive claims made without a specific artifact** — "their site feels dated" is an opinion; "their homepage hasn't added a mobile checkout option as of [date]" is a finding
6. **Stale data presented as current** — flag anything past the 3-year soft cutoff with a stated reason for the exception
7. **Ignoring segment differences** — market-wide numbers can hide the exact split that matters for the audience in scope

## Quality Checklist

Before delivery, verify:
- [ ] 3-5+ web searches conducted across multiple evidence lenses
- [ ] Every major finding tagged with its supporting lens(es)
- [ ] Market-Validated findings meet the 3-lens / no-lens-over-50% gate
- [ ] Every derived/calculated number shows its formula and cites each input separately
- [ ] Every competitive claim is grounded in a specific artifact, not an impression
- [ ] Sources meet the tiering bar (Tier 1/2 preferred; Tier 3 flagged if used)
- [ ] Nothing older than 3 years without a stated reason for the exception
- [ ] Every major finding states its conclusion in one sentence before the supporting evidence — placement (top vs. arc's climax) matches the output shape
- [ ] Underserved segment identified and the opportunity sized with the same math-shown discipline as other derived numbers
- [ ] Derived opportunity figures are visualized by default, not left as a bare stated number
- [ ] Output shape matches the user's stated goal

## When User Challenges Your Work

**Good responses:**
- "You're right to push back — let me check what lenses that finding is actually resting on."
- "That was asserted without showing the math. Here's the formula and both sources."
- "Fair catch — that's a Tier 3 source. Let me find something stronger."

**Bad responses:**
- Defending a finding that only has one evidence lens behind it
- Citing "industry knowledge" without a source
- Treating a competitor observation as fact without a specific artifact behind it

## Relationship to Buyer Journey Builder

These two skills answer different questions and are meant to run together:

- **buyer-journey-builder** — *how* does this audience decide, and *where* along the path do they act?
- **market-landscape-builder** — *why* does this market/audience matter right now, and *what* is everyone currently getting wrong?

Journey tells you where to intervene. Landscape tells you why it's worth intervening at all, and what the field currently misses. Used together, they produce a case with both a rationale and a path — not just one or the other.

---

**Remember:** The goal is a landscape that survives scrutiny — every major finding resting on multiple independent evidence types, every calculated number showing its work, every competitive claim grounded in something a skeptic could go look at themselves.
