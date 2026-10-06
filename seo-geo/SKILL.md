---
name: seo-geo
description: >
  Audits or plans SEO (traditional search) and GEO (visibility and citation in AI answer
  engines like ChatGPT, Perplexity, Google AI Overviews) with equal weight to both. Auto-detects
  mode: point it at a live page, site, or repo to audit; give it a brief or topic before
  anything is written to plan. Does its own keyword and best-practice research. Use for "SEO
  audit," "is this optimized for search," "will AI engines cite this," "GEO," "keyword
  research," "technical SEO," "why aren't we ranking," or any request to evaluate or plan
  search or AI-answer-engine visibility. For a scored, competitor-benchmarked deliverable
  ("SEO scorecard," "benchmark us against competitors"), use seo-geo-scorecard.
---

# SEO / GEO

Evaluates and improves visibility in two channels with equal billing: traditional search (SEO) and AI answer engines (GEO, generative engine optimization). Works on existing pages or on content not yet written. This is the open-ended, build-phase skill (research, audit or plan, fix). For a repeatable competitor-benchmarked score, use `seo-geo-scorecard`; if a scorecard has already run, use this skill to act on its findings.

## Evidence rules

Tag each finding ✅ **Validated** (research-backed, current best practice; cite source and year), ⚠️ **Validation needed** (logical but untested for this site), or 📱 **Table stakes** (already correct, or baseline not worth prioritizing), and mark it SEO, GEO, or both. Guidance older than 3 years is dated, especially for GEO. Don't present a ⚠️ GEO claim with the confidence of an established SEO factor.

## 1. Detect mode

- **Audit:** the user points to a live URL, site, or repo. Evaluate what's there.
- **Planning:** the user gives a brief, topic, or something not yet written. Shape SEO/GEO strategy before drafting.
- If ambiguous, ask; research and output differ meaningfully.

## 2. Research

Search rather than relying on training knowledge; both fields shift. **Run the searches in parallel in one turn**, scoped to the request (for a narrow fix like one page's meta tags, skip the generic best-practice searches).

- **Keywords/topics** (do it yourself; don't wait for targets): `"[topic] keyword search volume [current year]"`, `"[topic] related searches / people also ask"`, `"[topic] search intent [current year]"`, `"[topic] competitor rankings [current year]"`.
- **SEO guidance:** `"Google ranking factors [current year]"`, `"Core Web Vitals requirements [current year]"`. Prefer Google Search Central, then established industry sources (Ahrefs, Moz, Search Engine Land, Search Engine Journal); note when a claim rests on one vendor.
- **GEO guidance:** `"how to get cited by ChatGPT / Perplexity / AI Overviews [current year]"`, `"generative engine optimization best practices [current year]"`, `"llms.txt standard [current year]"`. Cite year and source.

## 3. Technical SEO

Audit mode, or constraints for planning mode: Core Web Vitals, crawlability and indexability (robots.txt, sitemap.xml, canonicals), meta titles and descriptions, heading hierarchy (logical, not keyword-stuffed), structured data, image alt text, internal linking, mobile responsiveness, URL structure.

## 4. GEO (equal weight to step 3)

- **Citability:** clear, quotable, factual statements an engine could lift as an answer.
- **Entity clarity:** brand, product, or person named and described consistently enough to resolve unambiguously.
- **Structured data AI crawlers use:** schema.org, FAQ, HowTo, author/organization markup.
- **Authority signals:** author attribution, publish/update dates, citations to authoritative sources.
- **Extraction-friendly structure:** direct answers early, scannable lists, headers phrased as real questions.
- **Crawl access:** robots.txt rules affecting AI crawlers specifically; llms.txt if relevant.

SEO and GEO are not the same checklist: a page can rank and never get cited, or the reverse. Check who is actually getting cited by AI engines, not just who ranks; it is frequently a different set of pages.

## 5. On-page content

Natural keyword/topic alignment across headers, body, and meta (forced repetition hurts both channels); depth relative to what ranks and what gets cited; readability for humans and AI parsers; internal linking opportunities. In planning mode this becomes recommendations for the brief (structure, headers, questions to answer directly). Prose itself stays with `writing-style` or `design:ux-copy`; this skill defines the requirements, and technical constraints from step 3 still apply to whoever builds the page.

## 6. Structure findings

```
## Fix Now (High Impact)
[Clear, evidenced impact on search or AI-citation visibility; cite the page/element and the source]

## Worth Doing (Medium Impact)
[Real improvements, not urgent]

## Already Table Stakes
[Handled correctly; confirm rather than re-flag]
```

## 7. Propose, then stop and ask

For direct code fixes (meta tags, schema, alt text, headings, sitemap/robots.txt), list the exact proposed change per file. **Do not edit yet.** Ask for explicit go-ahead, even for small fixes. Once approved, implement directly rather than re-describing.

## Before delivery

- [ ] Mode detected or confirmed; keyword research done, not assumed
- [ ] Current-year searches done for both SEO and GEO
- [ ] SEO and GEO got equal treatment
- [ ] Findings prioritized and tagged; every claim has a source and year or is labeled a judgment call
- [ ] Sources ≤3 years or flagged as dated
- [ ] Proposed code changes are listed and awaiting approval, not already made
