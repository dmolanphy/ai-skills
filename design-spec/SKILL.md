---
name: design-spec
description: >
  Generates a DESIGN.md file from a Figma design file, following the Stitch DESIGN.md
  specification (https://stitch.withgoogle.com/docs/design-md/specification): YAML design
  tokens plus human-readable rationale. Use when the user wants to create a DESIGN.md, export
  a design spec from Figma, document design tokens, or produce a machine-readable design system
  file ("create a design.md from my Figma", "document my design system"). Also use whenever a
  Figma URL or file key appears and a design spec is the goal.
---

# DESIGN.md Generator

Extract design tokens from Figma and write a valid DESIGN.md: YAML front matter (normative
tokens) plus a markdown body (rationale for agents). Spec details: `references/spec.md`.
Read it before Step 5.

## Workflow

Copy this checklist and tick it off:

```
- [ ] 1. Validate the Figma file
- [ ] 2. Extract design data
- [ ] 3. Gap audit + rules validation
- [ ] 4. Present summary, get confirmation
- [ ] 5. Map to tokens
- [ ] 6. Write markdown body
- [ ] 7. Save and present
```

### 1. Validate the Figma file

Get a Figma URL or file key (ask if missing). Call `Figma:get_metadata`. If it fails, stop and
tell the user what went wrong, what you tried, and how to fix it (check URL, sharing,
re-authenticate). Do not extract from an inaccessible file.

### 2. Extract design data

Call in parallel: `Figma:get_variable_defs` (primary token source), `Figma:get_design_context`
(semantics, informs prose), `Figma:get_screenshot` (visual check).

- Run `get_design_context` on the **primary design/production page** (e.g. "Design",
  "Production"), not wireframe or spec pages. Only the live page shows which variables are bound.
- If `get_variable_defs` is sparse, try `Figma:get_libraries`, then `Figma:search_design_system`.
  Note the gap in Step 3.
- Typography missing from variables: read text nodes directly (`fontName`, `fontSize`,
  `lineHeight`, `letterSpacing`). Map non-English weight names to 100–900 and keep the original
  name as a YAML comment. Monospace companions are typically reserved for labels/eyebrows/code;
  state that constraint explicitly.
- Variable libraries, semantic vs. primitive tokens, grids: see `references/figma-binding.md`.

### 3. Gap audit and rules validation

Inventory every token group (`colors`, `typography`, `rounded`, `spacing`, `grid`,
`components`) and body section (Overview, Colors, Typography, Layout, Elevation & Depth,
Shapes, Components, Do's and Don'ts). Status: ✅ found / 🔍 inferred / ❌ not found / ❓ needs
user input / ⬜ not applicable.

Resolve each gap in this order:
1. **Infer from the visual** — mark `# inferred from visual`.
2. **Spec default** (from `references/spec.md`) — mark `# spec default — confirm this value`.
3. **Ask the user** — required for `colors` and typography you cannot infer confidently. Be specific.
4. **TBD** — optional or low-confidence only: `# TODO: add value`.

Then validate against the active standard (Tailwind CSS v3 unless the user names another).
Read `references/design-rules.md` for rules, the alternate-standard procedure, and the
violation format (🔴 must fix / 🟡 should fix / 🔵 consider). Check: type ramp on scale and
strictly descending headings, spacing multiples of 4px, rounded multiples of 2px, required
color roles (`primary`, `surface`/`background`, a legible on-primary), component values use
token references, every referenced token exists.

### 4. Present summary, get confirmation

Show the summary using the format in `references/output-template.md`. It includes the
standard being applied (default Tailwind; accept "not sure" as Tailwind and note it in the
output), gap statuses, violations, and targeted questions. Include the question: auto-correct
🔴 violations or preserve and flag? **Wait for the user's reply before Step 5.**

If the user names another standard (Material, Apple HIG, custom), derive its ruleset per
`references/design-rules.md` and re-validate.

### 5. Map to tokens

- **Color names:** normalize Figma names (`color/brand/primary`, `color-primary-500`) to flat
  keys (`primary`, `secondary`, `surface`, `error`) plus shade variants (`primary-60`).
- **Components:** use `{colors.primary-60}`-style references, never raw hex/px.
- **Typography:** `fontFamily`, `fontSize` (px), `fontWeight`, `lineHeight` (ratio),
  `letterSpacing` (em); use recommended level names from `references/spec.md`.
- **Two-layer variable systems:** bind to the semantic layer, not primitives.
- **Grid:** read `layoutGrids` on top-level production frames; check `boundVariables` first and
  record variable IDs rather than guessing token names. Raw px values that match no spacing
  token get a comment naming the variable. Emit `grid.mobile` only if a mobile grid exists.
- Keep the `figma-variables` block whenever real variable IDs are known.

### 6. Write the markdown body

Write for an AI agent: explain the *intent* behind the tokens, not just the values. Required
sections in this exact order: Overview, Colors, Typography, Layout, Elevation & Depth, Shapes,
Components, Do's and Don'ts. If Figma variable bindings are documented, add **Token Binding**
last, never before Overview. Mark drafts needing review with `<!-- TODO: review this section -->`.

### 7. Save and present

Assemble front matter + body (skeleton and YAML rules in `references/output-template.md`) into
`DESIGN.md` in the workspace folder. Show the YAML front matter and Overview inline, link the
file, and summarize what came from Figma vs. was inferred vs. defaulted so the user knows
what to verify.

## Generating or correcting Figma frames from DESIGN.md

Binding fills to variables and applying `layoutGrids` is a separate workflow. See
`references/figma-binding.md` (load `figma:figma-use` before any `use_figma` call).

## Principles

- Validate access before extracting; a bad URL wastes the user's time.
- Token names are not literal: resolve IDs to hex and verify against the visual (e.g.
  `surface-primary` is often the default white surface, not the brand color).
- Prefer a tight, well-named token set over dumping every variable.
- The gap audit is a conversation: ask targeted questions, not everything at once.
