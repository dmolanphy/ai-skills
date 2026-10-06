---
name: market-landscape-builder
description: Builds evidence-backed market/category landscape briefings: why a market matters now, what's broken about how it's served, the opportunity size, and where the underserved gap sits. Leads with findings before evidence and sizes and visualizes the opportunity. Use to understand a market or category, size an audience or opportunity, or build the evidence case for a business direction ("tell me about the market," "market landscape," "category analysis," "size the opportunity," "where's the opportunity," "why does this matter"). For competitor positioning and adjacent-industry discovery use competitive-audit; for the customer's path to purchase use buyer-journey-builder. Pairs well with both.
---

# Market Landscape Builder

Build evidence-backed market landscapes that triangulate proof rather than pile up citations. A finding backed by four *different kinds* of evidence is far more durable than one backed by ten citations of the same kind.

**Search before asserting** any market size, sentiment, or competitive position.

## The five evidence lenses

Tag every finding with the lens(es) that support it:

- 💭 **Attitudinal** — how people feel or perceive (surveys, sentiment, stated preferences)
- 🖱️ **Behavioral** — what people actually do (channel usage, research habits, purchases, AI-assisted discovery/GEO behavior)
- 📊 **Market sizing** — size of the audience, category, or addressable opportunity
- 💰 **Economic** — dollar value, cost, value-at-stake, willingness to pay
- 🔍 **Competitive artifact** — a specific, describable, falsifiable observation of what a competitor shows, says, or does (a screenshot, stated policy, quote; never an impression)

## Workflow

### 1. Scope and start researching together

Ask in one AskUserQuestion round while starting category searches in the same turn: market/category and the decision this serves; target audience (segment, geography); known competitors or discovery needed; output (category briefing, competitive teardown, full landscape deck, raw evidence table).

### 2. Research

Run these literally, filling brackets: `"[category] market size [current year]"`, `"[audience] attitudes toward [category]"`, `"[category] customer satisfaction benchmark"`, `"[competitor] [category] experience"`, `"[category] willingness to pay [current year]"`, `"[audience] [category] research behavior"` (add AI-chatbot/GEO variants when discovery behavior is in scope).

Sources: Tier 1 academic, industry association, government; Tier 2 consulting and syndicated research (McKinsey, Deloitte, Forrester, Gartner); Tier 3 vendor white papers, single-source claims, aggregators (flag; avoid when better exists). Nothing older than 3 years without a stated reason. When data is thin, triangulate from adjacent categories, label it ("Estimated based on [adjacent category]"), and recommend validation.

### 3. Show the math on every derived number

State the formula and cite each input separately.
❌ "This represents a $X opportunity." ✅ "[Population] × [average annual value] = ~$X (population: [source, year]; value: [source, year])."

### 4. Ground every competitive claim in an artifact

❌ "Competitor X has a confusing checkout." ✅ "Competitor X's quote flow requires 14 fields before showing an estimate, with no explanation at any step (observed [date])."

### 5. Apply the validation gate

- **✅ Market-validated:** 3+ of the 5 lenses represented, and no single lens supplies more than half of the citations for that finding.
- **⚠️ Validation needed:** fewer than 3 lenses, extrapolated from an adjacent category, or logical but unproven. State the evidence gap and recommend a specific validation (survey, interview, pilot).

### 6. Lead with the finding, not the evidence

State each major finding in one sentence before the lenses that support it.
❌ "[Source A]: [stat]. [Source B]: [stat]. [Source C]: [stat]..." ✅ "[Conclusion in one sentence.] Two independent sources agree: [then the evidence]."

Placement depends on output shape. **Briefings, evidence tables, anything skimmed:** finding first, every time. **Decks experienced in sequence:** the finding may land at the climax of a narrative arc (context → tension → stakes → payoff); check whether the project already has an arc, and ask which mode you're building for if unclear.

### 7. Carve out the opportunity

- **Underserved segment:** identify who the market currently fails, from the lenses already gathered, not asserted fresh.
- **Size it** with Step 3's discipline (population × value, each input cited).
- **Frame dual advantage:** value capturable now plus future pipeline value, not one static number.
- **Visualize derived dollar figures by default** (chart, sized comparison, segment breakdown). Use the `dataviz` skill when available.

### 8. Assemble

- **Category briefing** (1–2 pages): the case for why the market matters, top findings by lens, sources. **Default to HTML using `assets/category-briefing-template.html`** (lens cards, boxed headline finding, dark opportunity block at close, one sparing accent color). Reuse its CSS; swap in current findings, sources, numbers.
- **Competitive teardown:** artifact-by-artifact review of how competitors serve the category, gaps identified. Can reuse the template's artifact-grid section standalone.
- **Full landscape deck:** all five lenses in a narrative arc (why this is critical → the challenge → the stakes → the opportunity → the imperative).
- **Raw evidence table:** findings tagged by lens and validation status.

## Pitfalls

1. Piling up one evidence type (ten attitudinal stats is repetition, not triangulation).
2. Treating recycled aggregator stats as primary; if a number appears on many "statistics roundup" pages with no traceable original, it's unusable.
3. Presenting single-source claims as settled fact.
4. Asserting derived numbers without the formula.
5. Competitive claims without a specific artifact.
6. Stale data presented as current.
7. Ignoring segment differences; market-wide numbers can hide the split that matters.

## Before delivery

- [ ] 3–5+ searches across multiple lenses
- [ ] Every major finding tagged by lens, and states its conclusion before the evidence
- [ ] Validated findings meet the gate (3+ lenses; none over 50% of citations)
- [ ] Every derived number shows its formula and cites each input
- [ ] Every competitive claim cites a specific artifact
- [ ] Sources meet the tier bar; nothing past 3 years without a stated reason
- [ ] Underserved segment identified, opportunity sized and visualized
- [ ] Output shape matches the user's goal
