# Live Insight Pull

## Contents
- What it is and why it is not scored
- The two queries
- Leading with the finding
- Multiple engines (connected browser)
- Reporting

## What it is and why it is not scored

Ask a real, specific, client-relevant category question **cold** (no searching first) and report which named brands come up unprompted, in what order, and under what name. This simulates someone asking an AI chatbot for a recommendation, the moment GEO tries to influence.

It is shown separately from the 12 scored checks because those are deterministic (the same fetch gives the same result), while this is one model's single response to one phrasing of one question: real and useful, but not repeatable. Never present it with score-level confidence; label it illustrative.

## The two queries (always run both)

1. **Broad / brand-recall query** — a top-of-funnel question a category leader wins regardless of technical readiness (e.g. "who are the best [category] providers for [audience]"). This tests legacy and scale, not GEO. A technically blocked market leader can still dominate on brand equity, so a strong result here is not proof GEO readiness worked.
2. **Specific / retrieval-dependent query** — a bottom-funnel question that forces the engine to look something up (e.g. "what's included standard in [Brand A]'s [offering] vs. [Brand B]'s in [specific market]"). This is where GEO readiness shows. A blocked or poorly structured site cannot supply the answer, so the engine finds someone else's description (a listing aggregator, regional blog, review site) and cites that instead.

## Leading with the finding

State the conclusion in one sentence first, then show both queries as proof, broad first, specific second:

*GEO readiness determines who controls the message. A well-optimized site is cited as the source of truth on the specific questions that drive a buyer's decision. A blocked or poorly structured site doesn't disappear; someone else's description of it fills the gap, on the engine's terms.*

The broad query usually shows the finding absent or weak (legacy wins); the specific query shows it clearly (sourcing shifts to third parties). This is what makes the audit land as a finding rather than a report card: a client can shrug at "8/10," but not at hearing they are recommended under a different name, or not at all.

## Multiple engines (connected browser)

If browser automation is connected and the person is logged into ChatGPT and/or Gemini, ask the same two queries on every available engine by typing them into the chat interface a real prospect would use (not via API). Watch each engine's citations: a brand that supplies its own answer is cited directly; one that can't forces a substitute, visible in the citation. Report citations by name, e.g. "Engine X cited [client-domain] directly for the client; for the blocked competitor it cited a third-party blog instead."

## Reporting

Present it as its own clearly separated section, never folded into the score. Name the actual substitute source whenever a specific query could not be answered from a brand's own material. Report which mechanism is in play: a ToS restriction (legal signal) and a robots.txt block (technical) have different real-world effects, and a ToS restriction alone can leave a site cited directly. Test both and don't assume one implies the other.
