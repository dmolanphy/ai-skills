---
name: seo-geo
description: >
  Audits or plans SEO (traditional search) and GEO (visibility/citation in AI answer
  engines like ChatGPT, Perplexity, Google AI Overviews) with equal weight given to
  both. Auto-detects mode: point it at a live page/site/repo and it audits; give it a
  content brief or topic before anything's written and it plans. Does its own
  keyword/topic research and current best-practice research rather than waiting for
  targets to be supplied. Can implement technical fixes directly in code, but always
  proposes changes and gets explicit go-ahead before editing anything. Use when the
  user says "SEO audit," "is this optimized for search," "will AI engines cite this,"
  "GEO," "keyword research," "technical SEO," "why aren't we ranking," or wants search
  or AI-answer-engine visibility evaluated or planned for.
---

# SEO / GEO

Evaluates and improves visibility in two channels with equal billing: traditional search engines (SEO) and AI answer engines like ChatGPT, Perplexity, and Google AI Overviews (GEO — generative engine optimization). Works on existing sites/pages or on content that hasn't been written yet.

## Core Principle: Evidence Over Assumptions

Same three-tier system used across this library, for consistency:

✅ **Validated** — Research-backed + current best practice (cite source, year — anything over 3 years old is dated, especially for GEO, which is a fast-moving field)
⚠️ **Validation Needed** — Logical but untested for this specific site/content
📱 **Table Stakes** — Already handled correctly, or an expected baseline not worth prioritizing further

**Always search first** — for target keywords/topics, for current SEO ranking-factor guidance, and for current GEO/AI-citation guidance. Don't rely on general knowledge for either; both shift often enough that stale guidance produces bad recommendations.

## Step 1: Detect mode

- **Audit mode** — user points to a live URL, an existing site, or a codebase/repo. Evaluate what's there.
- **Planning mode** — user provides a content brief, topic, or describes something not yet written. Shape SEO/GEO strategy before a word is drafted.
- If it's ambiguous which applies, ask rather than guess — the research and output differ meaningfully between the two.

## Step 2: Research (before evaluating anything)

**Keyword/topic research** — do this yourself, don't wait for the user to hand over targets:
```
1. "[topic/product] keyword search volume [current year]"
2. "[topic] related searches / people also ask"
3. "[topic] search intent [current year]"
4. "[topic] competitor rankings [current year]"
```

**Current SEO best practice** — search for current guidance rather than relying on training knowledge (ranking factors shift):
```
"Google ranking factors [current year]"
"Core Web Vitals requirements [current year]"
"technical SEO checklist [current year]"
```
Prioritize Google Search Central's own documentation, then established industry sources (Ahrefs, Moz, Search Engine Land, Search Engine Journal) — note when a claim comes from a single vendor source rather than confirmed guidance.

**Current GEO best practice** — this field moves fast and most authoritative material is recent by default; still cite year and source:
```
"how to get cited by ChatGPT / Perplexity / AI Overviews [current year]"
"generative engine optimization best practices [current year]"
"llms.txt standard [current year]"
```

## Step 3: Technical SEO (audit mode, or as constraints for planning mode)

- Core Web Vitals / page speed
- Crawlability & indexability — robots.txt, sitemap.xml, canonical tags
- Meta titles & descriptions — presence, length, quality
- Heading hierarchy (H1–H6) — logical structure, not just keyword stuffing
- Structured data / schema markup — presence and correctness
- Image alt text
- Internal linking structure
- Mobile responsiveness
- URL structure

## Step 4: GEO — equal weight to Step 3

- **Citability** — are there clear, quotable, factual statements an AI engine could lift directly as an answer?
- **Entity clarity** — is the subject (brand, product, person) named and described consistently enough for an AI system to resolve it unambiguously?
- **Structured data AI crawlers use** — schema.org, FAQ schema, HowTo schema, author/organization markup
- **Source authority signals** — author attribution, publish/update dates, citations to other authoritative sources
- **Extraction-friendly structure** — direct answers positioned early, scannable lists, headers phrased the way a question would actually be asked
- **Crawl access for AI systems** — robots.txt directives affecting AI crawlers specifically, llms.txt if relevant

## Step 5: On-page content (both modes)

- Keyword/topic alignment across headers, body copy, and meta — natural, not stuffed
- Content depth relative to what's currently ranking and what's currently getting cited by AI engines (these aren't always the same pages — check both)
- Readability and structure for human readers and AI parsers simultaneously
- Internal linking opportunities to and from related content

In planning mode, this step becomes recommendations for the brief (target structure, headers, questions to answer directly) rather than an audit of existing copy. Content voice/writing itself stays with `writing-style` or `design:ux-copy` — this skill defines the SEO/GEO requirements, not the prose.

## Step 6: Structure findings

```
## Fix Now (High Impact)
[Issues with clear, evidenced impact on search or AI-citation visibility — cite the specific page/element and the source behind the recommendation]

## Worth Doing (Medium Impact)
[Real improvements, not urgent — flag them, don't force priority they don't have]

## Already Table Stakes
[Things already handled correctly — confirm rather than re-flag, so effort doesn't get wasted re-fixing what's fine]
```

Tag each finding with an evidence tier (✅⚠️📱) and whether it's SEO, GEO, or both.

## Step 7: Propose implementation — then stop and ask

If working in a codebase and a fix is a direct code change (meta tags, schema markup, alt text, heading structure, sitemap/robots.txt), list the exact proposed change per file. **Do not make the edit yet.** Present the list and explicitly ask for go-ahead before touching anything. Once approved, implement directly rather than re-describing what to do.

## Critical Pitfalls to Avoid

1. **Treating SEO and GEO as the same checklist** — they overlap but aren't identical; a page can rank well and still never get cited by an AI engine, or vice versa.
2. **Stale ranking/citation guidance** — both fields shift; flag anything sourced from material older than 3 years as potentially outdated rather than presenting it as current.
3. **Keyword stuffing disguised as optimization** — alignment should read naturally; forced repetition hurts both channels.
4. **Auditing only the obvious top-ranking pages** — check who's actually getting cited by AI answer engines too; it's frequently a different set of pages than top organic results.
5. **Editing code before approval** — always propose and wait for go-ahead first, even for small fixes.
6. **Ignoring planning-mode constraints** — in planning mode, technical recommendations (Step 3) still apply as constraints for whoever builds the page, even though there's nothing to audit yet.

## Quality Checklist

Before delivery, verify:
- [ ] Mode (audit vs. planning) correctly detected or confirmed
- [ ] Keyword/topic research conducted, not assumed
- [ ] Current-year search conducted for both SEO and GEO best practices
- [ ] SEO and GEO each got genuinely equal treatment, not GEO as an afterthought
- [ ] Findings prioritized (Fix Now / Worth Doing / Table Stakes), not a flat list
- [ ] Every claim has a source and year, or is explicitly labeled a judgment call
- [ ] If code changes are proposed, they're listed and awaiting approval — not already made
- [ ] Sources current (≤3 years) or explicitly flagged as dated

## When User Challenges Your Work

**Good responses:**
- "Let me check current guidance on that rather than assume it's still true."
- "That recommendation was based on older material — here's what's current."
- "Good catch — let me verify whether that page is actually what's getting cited, not just what's ranking."

**Bad responses:**
- Defending a recommendation sourced from outdated guidance
- Presenting a GEO claim with the same confidence as an established SEO ranking factor when the evidence tier is actually ⚠️, not ✅
- Making a code change without having asked first

---

**Remember:** SEO and GEO are two channels to the same goal — being found — and neither one is the safe default to lean on. The output should make clear what's confirmed, what's a reasonable bet, and what's just expected baseline, and it should never touch code without asking first.
