# Skills Roadmap — Design & Dev Orchestration Framework

A living inventory of skills that exist today, organized by discipline, with gaps flagged for `product-owner` to eventually call on. Update this as new skills are built.

---

## Product Management
*Where `product-owner` and `grill-me` will live.*

**Have:**
- `design:design-critique` — structured usability/hierarchy/consistency feedback. Closest existing thing to a "grill-me" for finished work, but reactive (reviews output) rather than proactive (stress-tests a plan before work starts).
- `grill-me` — devil's-advocate stress test, both brief-mode (is this the right problem) and solution-mode (does this actually solve it). Its Blocking Issues / Worth Considering / Direct Questions format is now reused by other skills in this library (e.g. `code-review`).

**Need to build:**
- `product-owner` — dispatcher, not a narrating SKILL.md: digests a brief, runs a pre-decomposition clarity check (separate from grill-me — checks the brief has enough to work with before attempting decomposition at all), decomposes into tasks, assigns a model per subagent based on task complexity, dispatches real subagents via the Agent/Task tool, runs grill-me brief-mode on the task list before dispatch and solution-mode on the synthesized output before presenting, and proposes the right doc format per brief rather than defaulting to one. Never fully autonomous — task decomposition always pauses for approval before subagents are dispatched. Built last, once the rest of the bench exists (see priority build order below).

---

## Strategy
*Market research, brand strategy, positioning.*

**Have:**
- `brand-guardian` — brand strategy foundations, positioning, voice/messaging architecture, consistency audits
- `design:user-research` — research planning (interview guides, usability tests, surveys)
- `design:research-synthesis` — synthesizes raw research into themes/insights/recommendations

**Need to build:**
- Competitive audit skill (explicitly called out as a `product-owner` use case — distinct from user research, focused on competitor positioning/feature/UX benchmarking)
- Go-to-market / launch strategy skill (partially adjacent to brand-guardian, but GTM sequencing is distinct)

---

## Content
*Content audit, mapping, strategy, copywriting, voice & tone, messaging.*

**Have:**
- `writing-style` — personal voice/style application across copywriting tasks
- `design:ux-copy` — microcopy, error states, CTAs, empty states
- `visual-storyteller` — narrative structure for decks, moodboards, storyboards
- `image-prompt-engineer` — AI image prompt crafting (content production adjacent)
- `buyer-journey-builder` — evidence-based buyer journey maps: phases, touchpoints, channels by demographic, validated vs. assumed claims

**Need to build:**
- Content audit skill (inventory + gap analysis of existing content)
- Content mapping skill (mapping content to funnel stages — narrower than buyer-journey-builder, which now covers the journey-mapping half)
- Content strategy skill (broader than voice & tone — pillars, cadence, channel strategy)
- Message framework skill (formal positioning statements, proof points, messaging hierarchy — brand-guardian touches this but a dedicated skill may be worth it)

---

## Design
*UX/UI, design systems, brand guidelines, documentation.*

**Have:**
- `ds-foundations` — design tokens/variables, grids, text styles at project kickoff
- `design:design-system` — audit/document/extend design systems
- `design-spec` / `design-md` — DESIGN.md generation from Figma
- `design:design-handoff` — developer handoff specs
- `design:accessibility-review` — WCAG 2.1 AA audits
- `figma:figma-generate-library` — full design system builds in Figma
- `figma:figma-generate-design`, `figma:figma-create-new-file`, `figma:figma-use`, `figma:figma-use-figjam`, `figma:figma-use-slides` — Figma manipulation tooling
- `figma:figma-generate-diagram` — flowcharts, ERDs, sequence diagrams
- `frontend-design` — visual design direction/aesthetic guidance for UI builds

**Need to build:**
- Nothing glaring — this is your most mature category. Possible gap: a dedicated wireframing/IA skill distinct from full design-system work.

---

## Develop
*Figma-to-code, front-end, back-end, micro-interactions, code review, SEO/GEO.*

**Have:**
- `figma:figma-design-to-code` — Figma → code implementation
- `figma:figma-code-connect` — maps Figma components to code components
- `figma:figma-implement-motion` / `figma:figma-use-motion` — Figma motion → production animation code
- `figma:figma-swiftui` — SwiftUI ↔ Figma
- `transitions-dev` — CSS transitions/micro-interactions
- `frontend-design` — also relevant here for build-time aesthetic decisions
- `code-review` — general-purpose correctness/readability/maintainability review, any code regardless of language or whether it's a diff or a snippet. Distinct from the installed `security-review` (vulnerability-focused) and `review` (GitHub PR workflow). Reuses `grill-me`'s Blocking Issues / Worth Considering / Direct Questions output format.

**Need to build:**
- Back-end architect skill (explicitly mentioned)
- SEO/GEO skill (explicitly mentioned — technical + content crossover, may need a foot in both Content and Develop)
- Front-end specialist skill distinct from `frontend-design` (that one's aesthetic-direction focused, not implementation-pattern focused)

---

## Content Production (Adobe tools)
*Not one of your five disciplines, but worth tracking separately since it's a distinct capability set.*

**Have:**
- `adobe-create-social-variations`, `adobe-batch-edit-photos`, `adobe-retouch-portraits`, `adobe-resize-photos-and-videos`, `adobe-edit-quick-cut`, `adobe-design-from-template`, `adobe-create-pdfs-from-data`

---

## Utility / Infrastructure
*Cross-cutting, not discipline-specific.*

- `docx`, `pdf`, `pptx`, `xlsx` — file format handling
- `file-reading`, `pdf-reading` — ingestion
- `skill-creator` — meta: builds/optimizes skills (what we're using right now)
- `product-self-knowledge` — Anthropic product facts

---

## Extensibility — open question for `product-owner`

For the orchestrator to actually discover and use new skills as they're built (rather than hardcoding a skill list that goes stale), it needs some kind of registry it checks at runtime — e.g., a `skills-registry.md` or JSON manifest, tagged by discipline and use case, that `product-owner` reads before dispatching. This doc could evolve into that manifest, or feed one.

**Priority build order (based on what's explicitly missing and most-cited):**
1. ~~`grill-me` (Product Management)~~ — done
2. ~~Code review (Develop)~~ — done
3. Competitive audit (Strategy) — **next**
4. SEO/GEO (Develop/Content crossover)
5. Content mapping (Content) — buyer-journey-builder shipped ahead of schedule, covers the journey-mapping half
6. `product-owner` (Product Management) — built last, references everything above
