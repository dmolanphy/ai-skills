---
name: seo-geo-scorecard
description: Produces a scored SEO/GEO Readiness Scorecard for a website, benchmarked against named competitors on the same 12-check rubric: real, verifiable checks covering SEO fundamentals and AI-crawler/GEO readiness, plus a live cross-engine citation test. A client-facing strategy deliverable, not a fix list. Use when the user wants a SCORE or COMPETITOR COMPARISON ("SEO scorecard," "GEO scorecard," "readiness audit," "benchmark us against competitors on SEO/GEO," "is our site AI-ready compared to X"). For a general SEO audit, keyword research, content planning, or fixing code, use seo-geo. Measures technical readiness, not live AI-citation share (that needs paid tools like Profound, Gumshoe, Semrush AI visibility) and says so rather than simulating it.
---

# SEO/GEO Scorecard

Scored, competitor-benchmarked deliverable. For open-ended audits, keyword research, content planning, or code fixes, use `seo-geo`; hand off there if this scorecard surfaces fixes, and hand off here if a `seo-geo` audit needs a competitor comparison.

## Core principle: verified over simulated

Tag every finding by how it was established: 🔒 **Verified** (actually fetched and parsed) or 🔍 **Best-effort** (judgment or tool-dependent; state confidence). Never present an inferred number with the confidence of a measured one, and never drop the tag from the final output for a cleaner look.

- **Measures:** technical readiness: can AI engines and search crawlers access, parse, and extract this site's content?
- **Does not measure:** live AI-citation share (how often a brand is mentioned in ChatGPT/Perplexity/Gemini answers). That needs paid tools querying at scale over time. If asked for that number, say so and point to those tools; never fabricate an "appears in X of 10 AI answers" statistic.

**Never assert a check result without a fetched source behind it.** Thresholds (title/meta lengths, schema types, AI bot names) shift: reconfirm against a source from the last 3 years, or flag in the output that you did not.

## The 12 checks

### 🔒 Verified

1. **Title tag** — present; 50–60 characters.
2. **Meta description** — present; 150–160 characters.
3. **Canonical tag** — present and correctly self-referencing or pointing to the intended URL.
4. **Heading structure** — a single H1, logical H2/H3 nesting, no skipped levels or competing H1s.
5. **AI crawler accessibility** — fetch `/robots.txt` and report each as Allowed / Disallowed / Not mentioned (usually defaults to allowed; say which): `GPTBot`, `ClaudeBot`, `Claude-User`, `PerplexityBot`, `Google-Extended`, `Applebot-Extended`, `CCBot`, `anthropic-ai`, `cohere-ai`.
6. **llms.txt** — fetch `/llms.txt`: well-formed, malformed, or not found. This is an emerging, optional standard: well-formed = full credit, absent = partial credit (not zero), and say plainly in the output it is not yet a baseline expectation.
7. **AI-access legal posture** — check Terms of Service for language restricting automated access, AI agents, or scraping. Distinct from robots.txt (a site can be crawlable but contractually hostile); report separately.
8. **Image alt text** — from the homepage fetch, check `<img>` alt attributes are populated. A plain fetch can miss JS-injected images; if the page is JS-rendered, mark unassessed rather than scoring a false negative.
9. **URL structure** — clean, human-readable URL (sensible path, slug rather than auto-generated ID, no query-string cruft). Read directly from the string.

### 🔍 Best-effort

10. **Structured data** — `application/ld+json` (Organization, Service, FAQPage, Product). Text-extraction fetches often strip `<script>`, so never report "no structured data found" unless a rendering-capable tool confirmed absence; otherwise mark unassessed.
11. **Content extractability** — does the page answer the implied question in its first sentence or paragraph, or bury it?
12. **Internal linking** — links to relevant related in-domain content (not nav/footer boilerplate). Counting is objective; judging relevance is judgment.

Apply 11 and 12 with the **same standard to every site** in the comparison; a strict read of the client and a generous read of competitors (or vice versa) makes the comparison worthless.

## Workflow

### 1. Scope

Ask in one AskUserQuestion round: client URL and in-scope pages (homepage only, or service pages too); up to 3 named competitors; SEO + GEO or GEO only.

### 2. Fetch and verify

For each site: fetch the homepage and extract title, meta description, canonical, headings, image alts, and URL structure; fetch `/robots.txt`, `/llms.txt`, and the Terms page. **Fetch directly first**; if a fetch is refused because the URL has not appeared in search results, search for it, then retry. If robots.txt cannot be fetched, report "unable to verify in this pass," never a Disallow finding. If a rendering tool (e.g. a connected browser) is available, use it for JSON-LD and JS-rendering checks; otherwise mark those unassessed. Read the fetched content directly for checks 11 and 12.

Then run the Live Insight Pull once for the whole comparison set, per `references/live-insight-pull.md`.

### 3. Score

Score each check **0** (missing, failing, or actively hostile), **1** (partial or weak), or **2** (present and correct). Unassessed checks are excluded from both points and maximum, never scored 0 (that misrepresents "couldn't check" as "failed"). Calculate with `python scripts/score.py results.json` (input format in the script's docstring): it returns points, maximum, percent, and band per site.

Bands (percent of assessed maximum): **≥79% Strong**, **50–78% Adequate, real gaps**, **<50% At Risk**.

### 4. Compare

Run the identical process on every named competitor and present side by side; a single score in isolation means far less than knowing where the client stands against the competitors it cares about.

### 5. Assemble

Default to HTML using `assets/audit-report-template.html` (fill its [bracketed] placeholders; same visual family as `market-landscape-builder` and `buyer-journey-builder`: grid layout, sparing accent, dark closing block). Include: the score prominently at the top; all 12 checks with Verified/Best-effort tags; the competitor comparison as its own section; the Live Insight Pull as its own clearly separated, unscored section; and a closing section stating what the audit measured and did not, including which thresholds were reconfirmed.

## Pitfalls

1. **Simulating a citation score.** Not a capability of this skill.
2. **Scoring "not assessed" as failed.**
3. **Skipping the ToS check** because robots.txt looked fine; they are different signals.
4. **Treating "robots.txt allows it" as proof of access.** CDN/WAF-level blocking (e.g. Cloudflare AI bot management) can override robots.txt before the request reaches the server; this check cannot detect that layer, so say so.
5. **Treating a failed robots.txt lookup as absence.**
6. **Treating an absent llms.txt as a failure.**
7. **Counting internal links** instead of judging their relevance.

## Before delivery

- [ ] Every result traces to a fetched source; robots.txt, llms.txt, and ToS actually fetched
- [ ] Unassessed checks marked unassessed; checks 11 and 12 use one standard across all sites
- [ ] Competitors got the identical 12-check process
- [ ] Output states what the audit does and does not measure
- [ ] Live Insight Pull run with both queries, finding stated first, substitute sources named, labeled illustrative
- [ ] Thresholds reconfirmed against current guidance, or flagged
