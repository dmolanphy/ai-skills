---
name: seo-geo-audit-builder
description: Run a technical SEO/GEO Readiness Audit on a website — real, verifiable checks (not simulated AI-citation scores) covering SEO fundamentals and AI-crawler/GEO readiness, scored and compared against competitors on the same rubric. Use when users want to audit a site's search or AI-visibility, ask "run a GEO audit," "check our SEO," "how visible are we to AI," or want to compare technical readiness against named competitors. Trigger for "SEO audit," "GEO audit," "technical audit," "crawler accessibility," "is our site AI-ready," or requests to size up a site against competitors on search/AI fundamentals. Distinct from market-landscape-builder's competitive-artifact lens (qualitative) — this produces a scored, checklist-driven technical assessment. Honest about its limits — measures technical readiness, not live AI-citation share, which needs paid tools (Profound, Gumshoe, Semrush AI visibility); says so rather than simulating it.
---

# SEO/GEO Audit Builder

Run a real, verifiable technical audit — never a simulated citation score dressed up as a real one.

## Core Principle: Verified Over Simulated

Every finding is tagged by how it was established. A check that was actually fetched and parsed is 🔒 **Verified**. A check that required judgment or a tool that may not be available is 🔍 **Best-Effort**, with its confidence stated. Never present an inferred or estimated number with the same confidence as a directly measured one — that's the exact failure mode this skill exists to avoid.

**What this skill measures:** technical readiness — can AI engines and search crawlers actually access, parse, and extract this site's content.
**What this skill does NOT measure:** live AI-citation share — how often a brand actually gets mentioned in ChatGPT/Perplexity/Gemini answers. That requires paid tools with API access to those systems (Profound, Gumshoe, Semrush AI visibility) that query at scale over time. If asked to produce that number, say so directly and point to those tools rather than fabricate a plausible-looking substitute.

**Always fetch and verify — never assert a check result without a fetched source behind it.**

**Check thresholds stay current.** The specifics behind several checks — character-length ranges, which schema types are worth checking, which AI bot user-agents to name — shift over time. Before leaning on the threshold numbers below as settled fact, search for current guidance rather than assuming they're still right, and if a threshold hasn't been reconfirmed against a source from the last 3 years, flag it in the output rather than presenting it with unearned confidence.

## The 12 Checks

### 🔒 Verified (fetched and parsed directly)

1. **Title Tag** — present? Length 50–60 characters (too short wastes opportunity, too long gets truncated in results)
2. **Meta Description** — present? Length 150–160 characters
3. **Canonical Tag** — present, and does it correctly self-reference or point to the intended canonical URL
4. **Heading Structure** — single H1 present, logical H2/H3 nesting beneath it (not skipped levels, not multiple competing H1s)
5. **AI Crawler Accessibility** — fetch `/robots.txt`, check named AI bot user-agents explicitly: `GPTBot`, `ClaudeBot`, `Claude-User`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `anthropic-ai`, `cohere-ai`. Report each as Allowed / Disallowed / Not Mentioned (not mentioned usually defaults to allowed, but say which it is)
6. **llms.txt Presence** — fetch `/llms.txt`; present and well-formed, present but malformed, or not found. This is a young, still-forming, optional standard — absence is not a failure on par with a robots.txt block. Score presence-and-well-formed as full credit, absence as partial credit (not zero), and say plainly in the output that this is an emerging convention, not yet a baseline expectation.
7. **AI-Access Legal Posture** — check Terms of Service / Terms & Conditions for language restricting automated access, AI agents, or scraping. Distinct from robots.txt: a site can be technically crawlable but contractually hostile to it — both are real findings, worth reporting separately, not collapsed into one
8. **Image Alt Text** — from the same homepage fetch used for title/meta/canonical, check `<img>` tags for populated (non-empty) alt attributes. Same tooling caveat as Structured Data below: a plain fetch can miss JS-injected images. If the page is JS-rendered, mark this unassessed rather than scoring a false negative.
9. **URL Structure** — is the URL itself clean and human-readable (no excess query-string cruft, a sensible path, no auto-generated IDs where a slug would do)? No fetch required beyond having the URL — a direct read of the string.

### 🔍 Best-Effort (judgment-based or tool-dependent — state confidence)

10. **Structured Data / Schema.org Presence** — look for `application/ld+json` blocks (Organization, Service, FAQPage, Product). **Reliability depends on tooling**: a text-extraction fetch often strips `<script>` content, so this check may come back "not assessed" rather than a false negative — never report "no structured data found" unless a rendering-capable tool actually confirmed its absence. If no browser-rendering tool is available, say so and mark this check unassessed rather than guessing.
11. **Content Extractability** — does the page answer the implied question in its first sentence/paragraph, or bury it several paragraphs down? Apply this consistently across every page/competitor in the same audit — same rubric, same standard, every time (same discipline as buyer-journey-builder's validation tiers).
12. **Internal Linking Structure** — does the page link to other relevant, related in-domain content (not just nav/footer boilerplate)? Counting links present is objective; judging whether they're the *right* related links is a judgment call — apply it with the same consistency discipline as Content Extractability, across every site in the comparison.

## The Live Insight Pull (not scored, run and shown separately)

This is what makes the audit more than a scorecard, and it's the piece most worth showing a client directly.

**What it is:** ask a real, specific, client-relevant category question — cold, without searching or looking anything up first — and report which named brands come up unprompted, in what order, and under what name. This simulates the actual experience of someone asking an AI chatbot for a recommendation, which is exactly the moment GEO is trying to influence.

**Why it's separate from the scored checks:** the scored checks are deterministic — the same fetch produces the same result every time. This is a single model's single response to a single phrasing of a single question. It is real and it is useful, but it is not repeatable in the way a score should be, and presenting it with the same confidence as the scored checks would be exactly the kind of overclaiming this skill exists to avoid.

**How to run it — two queries, not one:**

A single query tests one thing at a time, and which thing it tests changes the entire result. Run both, always:

1. **Broad / Brand-Recall Query** — a top-of-funnel question a category leader would win regardless of technical readiness ("who are the best national homebuilders for X"). This tests *legacy and scale*, not GEO. Expect established, well-known brands to surface here almost no matter what — a technically blocked market leader can still dominate this query on brand equity alone. Don't mistake a strong result here for proof that GEO readiness worked.
2. **Specific / Retrieval-Dependent Query** — a bottom-funnel question that requires the engine to actually go look something up rather than recall a famous name ("what's currently included standard in a [Brand A] home vs. a [Brand B] home in [specific market]"). This is where GEO readiness actually shows up. A blocked or poorly-structured site can't supply the answer directly — watch what the engine does instead. It doesn't just fail; it goes and finds someone else's description of the brand (a listing aggregator, a regional realty blog, a review site) and cites that instead.

**Lead with the finding, prove it with both queries — don't just report two results side by side.** State the conclusion first, in one sentence, the same discipline as every other finding in this skill: *GEO readiness determines who controls the message. A well-optimized site gets cited as the source of truth on the specific questions that actually matter to a buyer's decision. A blocked or poorly-structured site doesn't disappear — someone else's description of it fills the gap instead, on the engine's terms, not the brand's.* Then show the broad query (where the finding is usually absent or weak — legacy wins) and the specific query (where the finding shows up clearly — sourcing shifts to third parties) as the evidence, in that order.

**Why this matters more than the score:** a client can look at "8/10, Adequate" and shrug. A client cannot easily shrug off reading, in plain language, that when someone asks a real question their category, they get recommended under a *different name* than the one on their building, or not recommended at all. This is the piece that makes the audit feel like a finding instead of a report card.

**Extending to multiple engines, when a connected browser is available:** if browser automation is connected and the person is already logged into ChatGPT and/or Gemini, the same two queries (broad and specific) can be asked directly on those products too — not through an API, just typed into the same chat interfaces a real prospect would use. Run both queries on every available engine. This is where the specific-query result becomes provable rather than asserted: watch each engine's citations. A brand that supplies its own answer gets cited directly. A brand that can't (blocked, poorly structured, or simply thin on the specific detail asked) forces the engine to a substitute — a listing aggregator, a regional blog, a review site — and that substitution is visible in the citation, not just inferred. Report each engine's citations by name (e.g., "Gemini cited lennar.com directly for Lennar; for the blocked competitor, it cited a third-party realty blog instead") — that specificity is what makes the finding land as evidence rather than assertion.

## Quick Start Process

### 1. Scope

- What's the client's URL, and which page(s) — homepage only, or specific service pages too?
- Which competitors (up to 3) for comparison?
- Is this SEO + GEO combined, or GEO only?

### 2. Fetch & Verify (search first, then fetch — web_fetch requires a URL to have appeared in a prior search result)

For each site being audited:
1. Search for the site to get its URL into fetchable context
2. Fetch the homepage (and any additional in-scope pages) — extract title, meta description, canonical, heading structure, image alt attributes, and note the URL structure directly from the returned page data
3. Search for `[domain]/robots.txt` specifically, then fetch it — parse for the named AI bot user-agents
4. Search for `[domain]/llms.txt` specifically, then fetch it — note presence and whether it's well-formed
5. Search for `[domain] terms of service` or `terms and conditions` — fetch and check for AI/scraping restriction language
6. If a browser-rendering tool (e.g., a connected browser control tool) is available, use it to check for JSON-LD structured data and JS-rendering dependency; if not, mark those sub-checks unassessed rather than guessing
7. Apply the Content Extractability and Internal Linking Structure rubrics by reading the fetched content directly — same consistency discipline for both, across every site in the comparison
8. Run the Live Insight Pull for the whole comparison set (not per-site) — a broad brand-recall query and a specific retrieval-dependent query, both asked cold with no search, reporting which brands surfaced under which name, and — critically — where a specific query's answer got sourced from when a brand couldn't supply it directly

### 3. Score

Each of the 12 checks scored 0–2:
- **0** — missing / fails / actively hostile (e.g., AI bots disallowed, no title tag)
- **1** — partial / present but weak (e.g., meta description present but wrong length, some but not all AI bots blocked, llms.txt absent)
- **2** — present and correct

Max score: 24 points. Unassessed checks (e.g., structured data or alt text with no rendering tool available) are excluded from both the numerator and denominator — never scored as 0, since that would misrepresent "couldn't check" as "failed."

**Bands:**
- 19–24: Strong
- 12–18: Adequate, real gaps
- 0–11: At Risk

### 4. Compare

Run the identical 12-check process against each named competitor, same rubric, same standard. Present side by side — this is what makes the score mean something; a single site's score in isolation is much less useful than knowing whether it's ahead of or behind the specific competitors the client actually cares about.

### 5. Assemble

Default to HTML output using `assets/audit-report-template.html` as the structural and visual reference — same visual system as market-landscape-builder and buyer-journey-builder (grid layout, sparing accent color, dark closing block), so this reads as part of the same family of tools when handed off alongside them. Score prominently at the top, all 12 checks shown with their Verified/Best-Effort tags intact, competitor comparison as its own section, the Live Insight Pull as its own clearly-separated section (not folded into the score), and a closing section stating plainly what this audit measured and what it didn't — including which threshold specifics were reconfirmed against current sources.

## Critical Pitfalls to Avoid

1. **Assuming a specific query's substitution finding applies uniformly.** A ToS restriction and a robots.txt block are different levers with different real-world effects — a site can restrict scraping in its Terms (legal signal) without being technically blocked, and still get cited directly by live engines. Test both, and don't assume a legal restriction alone produces the same substitution effect a technical block does. Report which mechanism is actually in play.
2. **Simulating an AI-citation score.** Never generate a plausible-looking "appears in X of 10 AI answers" statistic without genuine, repeated, multi-engine querying behind it. This skill does not have that capability — say so, don't fake it.
3. **Reporting "not assessed" as "failed."** If structured data can't be checked because no rendering tool is available, that's a gap in the audit's coverage, not a 0 score for the site.
4. **Skipping the ToS check because robots.txt looked fine.** They're different signals. A site can pass robots.txt and still have hostile ToS language — both are real findings.
5. **Applying the Content Extractability rubric inconsistently** across competitors — if the client's site gets a strict read and competitors get a generous one (or vice versa), the comparison is worthless.
6. **Presenting a Best-Effort finding with Verified-level confidence.** The tag exists specifically so this doesn't happen — don't drop it in the final output for the sake of a cleaner-looking report.
7. **Treating "robots.txt allows it" as proof of actual access.** CDN/WAF-level blocking (e.g., Cloudflare's AI Bot Management) can silently override robots.txt entirely — a bot can be blocked before the request ever reaches the server that hosts the robots.txt file. This skill's robots.txt check cannot detect that layer; say so in the output rather than implying a clean robots.txt result is the full picture.
8. **Assuming a failed robots.txt fetch means it doesn't exist.** In practice, robots.txt isn't always independently discoverable via search for a given domain even when the mechanism works fine in general. Report "unable to verify in this pass" rather than treating a failed lookup as a Disallow finding.
9. **Treating an absent llms.txt as a failure.** It's an emerging, optional standard, not yet a baseline expectation the way robots.txt is — score it as partial credit, not zero, and say so.
10. **Scoring Internal Linking Structure like a simple count.** The judgment is whether the links are actually relevant to the reader, not just whether links exist — nav and footer boilerplate don't count.

## Quality Checklist

Before delivery, verify:
- [ ] Every check result traces to an actual fetched source — no assertion without a fetch behind it
- [ ] Robots.txt was actually fetched and parsed, not assumed
- [ ] llms.txt was actually fetched and checked, not assumed absent
- [ ] ToS/Terms checked as a distinct signal from robots.txt
- [ ] Alt text checked against the same fetch as title/meta, or marked unassessed if the page is JS-rendered
- [ ] URL structure assessed for every site in the comparison
- [ ] Unassessed checks are marked unassessed, not scored as failures
- [ ] Content Extractability and Internal Linking Structure both applied with the same standard across every site in the comparison
- [ ] Output states clearly what this audit does and does not measure (technical readiness vs. live citation share)
- [ ] Competitor comparison uses the identical 12-check process, not a lighter pass
- [ ] Live Insight Pull run as two queries — one broad/brand-recall, one specific/retrieval-dependent — not just one
- [ ] The finding is stated first, in one sentence, before the two queries' results are shown as proof
- [ ] Where a specific query couldn't be answered from a brand's own material, the actual substitute source is named, not glossed over
- [ ] Live Insight Pull clearly labeled as illustrative, never presented with score-level confidence
- [ ] Threshold/best-practice specifics (character lengths, schema types, named AI bots) reconfirmed against current guidance, or flagged if not

## When User Challenges Your Work

**Good responses:**
- "You're right to ask — that structured-data check came back unassessed because I didn't have a rendering tool available, not because I confirmed it's missing. Want me to try with browser tooling connected?"
- "That's a fair catch — I should have flagged the ToS restriction separately from the robots.txt result. They're different signals."

**Bad responses:**
- Presenting an estimated AI-citation percentage as if it were measured
- Defending a "0" score on a check that was actually never verified
- Applying a stricter extractability read to a competitor than to the client's own site

## Relationship to Market Landscape Builder and Buyer Journey Builder

Three legs, not one trick. Market Sizing tells you whether the fight is worth having. Buyer Journey tells you how the audience actually decides. This skill tells you whether the client can even be found by the tools their buyers increasingly use to do that deciding. The first two sharpen strategic perspective; this one is closer to a deliverable in its own right — a scored, competitive, sellable diagnostic.

---

**Remember:** A defensible score that says "here's what we could verify, and here's what we couldn't" is worth more than an impressive-looking number nobody can trace back to a real check.
