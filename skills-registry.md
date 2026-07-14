# Skills Registry

Machine-readable index for `product-owner` to match tasks to skills. Update this file every time a skill is added, renamed, or retired — this is the single source of truth `product-owner` reads at runtime, not the skill descriptions themselves.

**Columns:**
- `skill_id` — exact skill name as it appears in `available_skills` (must match frontmatter `name` exactly)
- `discipline` — Product Management / Strategy / Content / Design / Develop / Content Production / Utility
- `subcategory` — narrower classification within the discipline
- `trigger_summary` — short, task-oriented description of when to dispatch this skill (not the full SKILL.md description — just enough for `product-owner` to match against a decomposed task)
- `status` — `active` (built and usable today) or `planned` (identified gap, not yet built — `product-owner` should flag these as "no skill available yet, needs manual work or skill creation" rather than fail silently)

---

## Product Management

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| design:design-critique | Product Management | review | Structured feedback on usability, hierarchy, consistency of a finished design | active |
| grill-me | Product Management | stress-test | Devil's-advocate pressure-test of a brief or proposed solution before work starts/ships (two modes: brief-mode, solution-mode) | active |
| product-owner | Product Management | orchestration | Digest brief, decompose into tasks, assign models/skills, dispatch, synthesize | planned (in progress) |

## Strategy

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| brand-guardian | Strategy | brand strategy | Brand positioning, visual identity specs, voice/messaging architecture, brand consistency audits | active |
| design:user-research | Strategy | research planning | Design interview guides, usability tests, surveys, research questions | active |
| design:research-synthesis | Strategy | research synthesis | Synthesize interviews/surveys/tickets into themes, segments, prioritized recommendations | active |
| competitive-audit | Strategy | competitive analysis | Benchmark competitor positioning, features, UX against the brief | planned |
| gtm-strategy | Strategy | launch strategy | Go-to-market sequencing and launch planning | planned |

## Content

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| writing-style | Content | copywriting | Apply personal voice/style to headlines, copy, decks, briefs | active |
| design:ux-copy | Content | microcopy | Write/review buttons, error states, empty states, CTAs | active |
| visual-storyteller | Content | narrative structure | Structure decks, moodboards, storyboards, data stories around a narrative | active |
| image-prompt-engineer | Content | AI image prompting | Craft prompts for AI-generated reference imagery/moodboard visuals | active |
| content-audit | Content | audit | Inventory and gap-analyze existing content against goals | planned |
| content-mapping | Content | mapping | Map content assets to funnel stages / buyer journey | planned |
| content-strategy | Content | strategy | Content pillars, cadence, channel strategy | planned |
| message-framework | Content | messaging | Formal positioning statements, proof points, messaging hierarchy | planned |
| buyer-journey-builder | Content | journey mapping | Build evidence-based buyer journey maps: phases, touchpoints, channels by demographic, validated vs. assumed claims | active |

## Design

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| ds-foundations | Design | design system | Set up tokens/variables, grids, text styles at project kickoff | active |
| design:design-system | Design | design system | Audit, document, or extend an existing design system | active |
| design-md | Design | documentation | Generate DESIGN.md spec from a Figma file | active |
| design:design-handoff | Design | dev handoff | Generate developer handoff specs (layout, tokens, props, states, breakpoints) | active |
| design:accessibility-review | Design | accessibility | WCAG 2.1 AA audit of a design or page | active |
| figma:figma-generate-library | Design | design system | Build/update component libraries, variables, theming in Figma | active |
| figma:figma-generate-design | Design | screen assembly | Build/update full pages, modals, panels in Figma from code or description | active |
| figma:figma-create-new-file | Design | file setup | Create a new blank Figma/FigJam/Slides file | active |
| figma:figma-use | Design | Figma scripting | Write actions in Figma (create/edit nodes, variables, components) | active |
| figma:figma-use-figjam | Design | FigJam | FigJam-specific context for use_figma tool | active |
| figma:figma-use-slides | Design | Slides | Figma Slides-specific context for use_figma tool | active |
| figma:figma-generate-diagram | Design | diagramming | Flowcharts, ERDs, sequence diagrams, state diagrams, gantt charts | active |
| frontend-design | Design | aesthetic direction | Distinctive visual/typographic direction for new or reshaped UI | active |

## Develop

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| figma:figma-design-to-code | Develop | design-to-code | Implement a Figma design as production code | active |
| figma:figma-code-connect | Develop | design-to-code mapping | Map Figma components to code components via Code Connect | active |
| figma:figma-implement-motion | Develop | motion implementation | Translate Figma motion/animation into production code | active |
| figma:figma-use-motion | Develop | motion authoring | Add/edit/inspect animation on a Figma node | active |
| figma:figma-swiftui | Develop | SwiftUI | Translate between Figma and SwiftUI in either direction | active |
| transitions-dev | Develop | micro-interactions | CSS transitions/animations for UI states (modals, dropdowns, loaders, etc.) | active |
| code-review | Develop | code quality | Review code for correctness, quality, maintainability | planned |
| backend-architect | Develop | architecture | Design/review backend systems and architecture | planned |
| seo-geo | Develop | SEO/GEO | Technical + content SEO/GEO optimization | planned |
| frontend-specialist | Develop | implementation patterns | Frontend implementation patterns distinct from aesthetic direction | planned |

## Content Production

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| adobe-for-creativity:adobe-create-social-variations | Content Production | social assets | Resize/crop/export images or video for specific social platforms | active |
| adobe-for-creativity:adobe-batch-edit-photos | Content Production | photo editing | Apply consistent adjustments across a batch of photos | active |
| adobe-for-creativity:adobe-retouch-portraits | Content Production | portrait retouching | Bulk-retouch a folder of portrait photos | active |
| adobe-for-creativity:adobe-resize-photos-and-videos | Content Production | resizing | Resize photos/videos to exact dimensions or aspect ratios | active |
| adobe-for-creativity:adobe-edit-quick-cut | Content Production | video editing | Cut a video into a highlight/sizzle reel | active |
| adobe-for-creativity:adobe-design-from-template | Content Production | templated design | Create flyers, posters, social posts, business cards from templates | active |
| adobe-for-creativity:adobe-create-pdfs-from-data | Content Production | data merge | InDesign data merge from CSV/TSV + template | active |

## Utility / Infrastructure

| skill_id | discipline | subcategory | trigger_summary | status |
|---|---|---|---|---|
| docx | Utility | file format | Create/read/edit Word documents | active |
| pdf | Utility | file format | Create/read/edit/manipulate PDFs | active |
| pptx | Utility | file format | Create/read/edit presentation decks | active |
| xlsx | Utility | file format | Create/read/edit spreadsheets | active |
| file-reading | Utility | ingestion | Route uploaded files to the correct reading tool | active |
| pdf-reading | Utility | ingestion | Extract content/inspect PDFs prior to processing | active |
| skill-creator | Utility | meta | Create, edit, evaluate, and optimize skills | active |
| product-self-knowledge | Utility | product facts | Verify Anthropic product facts before stating them | active |

---

## Maintenance rule

Every time a skill moves from `planned` to `active` (or a new skill is created), add/update its row here in the same session. `product-owner` should treat this file as authoritative over its own assumptions — if a task doesn't match any `active` row closely, it should tell you rather than guess or invent a call to a skill that doesn't exist.
