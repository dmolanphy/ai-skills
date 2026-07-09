---
name: design-spec
description: >
  Generate a DESIGN.md file from a Figma design file, following the Stitch DESIGN.md specification
  (https://stitch.withgoogle.com/docs/design-md/specification). Use this skill any time the user
  wants to create a DESIGN.md, export a design spec from Figma, document design tokens, or produce
  a machine-readable + human-readable design system file. Trigger even if the user just says things
  like "create a design.md from my Figma", "document my design system", "generate a design spec
  from this file", or "I want a DESIGN.md for this". If a Figma URL or file key is present anywhere
  in the conversation, use this skill to produce the DESIGN.md automatically.
---

# DESIGN.md Generator

Generate a valid DESIGN.md file from a Figma design by extracting design tokens and writing
human-readable rationale — following the Stitch DESIGN.md specification exactly.

Read `references/spec.md` for the full spec before generating the file.

---

## What is DESIGN.md?

A DESIGN.md file has two layers:

- **YAML front matter** (`---` delimiters): machine-readable design tokens — the precise values
  agents use to enforce consistency across the design system.
- **Markdown body**: human-readable design rationale organized into `##` sections. Prose may
  use descriptive color names (e.g., "Midnight Forest Green") that correspond to token names
  (e.g., `primary`). Tokens are the normative values; the prose provides context for how to
  apply them.

The spec is a **foundation, not a prescription** — it provides common ground agents and tools
can rely on while preserving freedom to extend it for domain-specific needs.

---

## Step-by-step workflow

### Step 0 — Confirm the design standard

Before doing anything else, ask:

> "This will validate your design tokens against **Tailwind CSS v3 defaults** (4px grid,
> Tailwind type scale, standard weights and line heights). Is that right, or does this
> project follow a different standard?"

If they confirm Tailwind, proceed with `references/design-rules.md`.

If they name a different standard (Material Design, Apple HIG, custom), ask them to describe
it or paste a reference. Derive the equivalent ruleset and apply it in place of the defaults.
See `references/design-rules.md` → "Asking about alternate standards" for guidance.

If they say "not sure" or "doesn't matter", default to Tailwind and note it in the output.

### Step 1 — Get and validate the Figma file reference

If the user hasn't provided a Figma URL or file key, ask for one before proceeding.

Once you have a URL, call `get_metadata` to validate access. If the call fails or returns
an error, stop and tell the user clearly: what went wrong, what you tried, and what they
can do to fix it (e.g., check the URL, ensure the file is shared, re-authenticate).

Do not proceed to extraction if the file isn't accessible.

### Step 2 — Extract design data from Figma

Once the file is confirmed accessible, call these tools in parallel:

- **`get_variable_defs`** — primary source for YAML tokens (colors, spacing, radii, type)
- **`get_design_context`** — semantic understanding of the design; informs markdown sections
- **`get_screenshot`** — visual reference; use to verify extracted tokens and fill visual gaps

If `get_variable_defs` returns little or nothing:
- Try `get_libraries` to check if tokens live in a connected library
- Try `search_design_system` for specific token categories
- Note in your gap audit (Step 3) that variables weren't explicitly defined

**Important: scan the primary design/production page — not just wireframe or spec pages —
to discover which variables are actually in use.** Variable definitions may exist in the
library but only the live design page will show which ones are bound to real elements.
Use `get_design_context` on the page named something like "File 2", "Design", or "Production"
rather than pages named "Wireframes" or "Specs."

### Step 3 — Gap audit: identify what's present, missing, or inferrable

This is the most important step. Before writing anything, build an explicit inventory.

**For the YAML front matter**, check each required token group:

| Token group | Status options |
|---|---|
| `colors` | ✅ found in variables / 🔍 inferred from visual / ❌ not found |
| `typography` | ✅ found in variables / 🔍 inferred from visual / ❌ not found |
| `rounded` | ✅ found in variables / 🔍 inferred from visual / ❌ not found |
| `spacing` | ✅ found in variables / 🔍 inferred from visual / ❌ not found |
| `grid` | ✅ found in layoutGrids / 🔍 inferred from visual / ❌ not found / ⬜ optional |
| `components` | ✅ found / 🔍 inferred / ❌ not found / ⬜ optional |

**For the markdown body**, check each required section:

| Section | Status options |
|---|---|
| Overview | ✅ enough context / 🔍 can infer from file name + visual / ❓ needs user input |
| Colors | ✅ / 🔍 / ❓ |
| Typography | ✅ / 🔍 / ❓ |
| Layout | ✅ / 🔍 / ❓ |
| Elevation & Depth | ✅ / 🔍 / ❓ needs user input / ⬜ not applicable |
| Shapes | ✅ / 🔍 / ❓ |
| Components | ✅ / 🔍 / ❓ |
| Do's and Don'ts | ✅ / 🔍 / ❓ |

**Gap resolution strategy** (apply in this order for each gap):

1. **Infer from visual**: If the value is clearly visible in the screenshot (e.g., a consistent
   8px grid, a shadow on cards, a specific border radius), infer it and mark it as inferred
   with a YAML comment: `# inferred from visual`.
2. **Use spec defaults**: If the token type has a recommended default in `references/spec.md`
   and a reasonable default exists for the design style you can see, use it — but mark it:
   `# spec default — confirm this value`.
3. **Ask the user**: If you can't confidently infer a required token (especially for `colors`
   and typography), ask the user to provide it rather than guessing. Be specific — show them
   exactly what's missing and why.
4. **Mark as TBD**: For optional or low-confidence values, insert a placeholder:
   `# TODO: add value` so the file is still valid but clearly incomplete.

### Step 3b — Rules validation

After the gap audit, validate all extracted token values against the active design standard.
Read `references/design-rules.md` for the full ruleset. Check:

**Type ramp:**
- All `fontSize` values snap to the standard scale (±1px tolerance)
- `fontWeight` values are on the valid set (100–900 in 100-steps)
- `lineHeight` falls within normal range (1–2)
- `letterSpacing` is within the valid em range
- Heading hierarchy is strictly descending (h1 > h2 > h3...)

**Grid & spacing:**
- All `spacing` values are multiples of 4px
- All `rounded` values are multiples of 2px
- Spacing scale increases monotonically

**Color system:**
- Required roles are present (`primary`, `surface` or `background` at minimum)
- If `primary` is defined, a legible on-primary color exists
- No orphaned shade variants

**Component tokens:**
- All component values use token references, not raw hex/px values
- All referenced tokens (`{colors.primary-60}`) actually exist in the token set

For each violation, record it using the format in `references/design-rules.md`:
- 🔴 Must fix / 🟡 Should fix / 🔵 Consider

### Step 4 — Present the audit summary to the user

Before writing the file, show the user a structured summary. This is critical — it sets
expectations, catches mistakes early, and gives the user a chance to fill gaps.

Format the summary like this:

```
## What I found in your Figma file
**Standard:** Tailwind CSS v3 defaults

### Tokens
✅ Colors — 4 roles extracted (primary, secondary, surface, error)
✅ Typography — h1, h2, body, caption found
🔍 Rounded — no variables found; inferred sm=4px, md=8px from visual
❌ Spacing — not found; using spec defaults (xs=4px, sm=8px, md=16px, lg=24px)
⬜ Components — no component tokens defined

### Sections
✅ Overview, Colors, Typography — enough context to write these
🔍 Layout — will infer from spacing values and visual grid
❓ Elevation & Depth — couldn't find shadow styles; do you use elevation in this design?
🔍 Shapes — will use inferred rounded values
❓ Do's and Don'ts — I'll draft these from what I can see; you may want to review

### Rules violations
🔴 typography.h3.fontSize = 22px — not on Tailwind scale; suggest 24px
🟡 typography.body.lineHeight = 1.4 — slightly off; Tailwind "normal" is 1.5
🔵 No on-primary color defined — recommended for accessibility

**Before I write the file, I need you to confirm:**
1. [Specific question about a gap, e.g., "What spacing base unit does this design use?"]
2. Should I auto-correct the 🔴 violations, or preserve the original values and flag them?

Or say "looks good, go ahead" if you're happy with the inferences and want auto-corrections applied.
```

Wait for the user's response before proceeding to Step 5.

### Step 5 — Map Figma data to DESIGN.md tokens

Apply user-confirmed values and your inferences. See `references/spec.md` for the full schema.

**Color naming**: Normalize Figma variable names (e.g., `color/brand/primary`, `color-primary-500`)
to flat keys (`primary`, `secondary`, `tertiary`, `surface`, `error`). Add shade variants where
present (e.g., `primary-60`, `primary-20`).

**Token references in components**: Always use `{token.name}` syntax rather than raw values.
For example: `backgroundColor: "{colors.primary-60}"`.

**Typography**: Extract fontFamily, fontSize (px), fontWeight, lineHeight (ratio), letterSpacing
(em) for each text role. Use `references/spec.md` recommended level names.

**Semantic token hierarchy**: When a Figma file uses a two-layer variable system (semantic +
primitive), always prefer the semantic layer for DESIGN.md bindings. See the "Figma Variable
Binding" section below for the full procedure.

**Grid extraction**: For each top-level frame, check the `layoutGrids` property. Each entry
will contain `pattern`, `alignment`, `count`, `gutterSize`, `offset`, and optionally
`boundVariables`. Check `boundVariables` first — grid values are often bound to a dedicated
layout variable collection (separate from the color/spacing semantic tokens), and you should
record those variable IDs in the YAML rather than guessing at token names. If the gutter or
margin value doesn't match any spacing token exactly, record it as a raw px value with a
comment identifying the variable name. If `layoutGrids` is absent on production frames, infer
from the visual — look for alignment patterns in repeated content columns. Note: not all
breakpoints have a defined grid; only emit `grid.mobile` if a mobile grid actually exists in
the file.

### Step 6 — Write the markdown body

Write each section based on `get_design_context`, the visual, and user-provided context.
The goal is to communicate the *intent* behind the tokens, not just repeat the values.
Write for an AI agent as the primary reader — the prose helps agents understand *why* choices
were made so they can make consistent decisions in new contexts.

Required sections (in this exact order): Overview, Colors, Typography, Layout, Elevation &
Depth, Shapes, Components, Do's and Don'ts.

If the design uses explicit Figma variable bindings, add a **Token Binding** section after
Do's and Don'ts — never before Overview.

For any section marked TBD or needing user input, write the best draft you can with a
note like `<!-- TODO: review this section -->` so the user knows to revisit it.

### Step 7 — Write and present the file

Assemble YAML front matter + markdown body into `DESIGN.md` and save to the workspace folder.

Show the user the YAML front matter and Overview inline in the conversation so they can
immediately spot any issues, then link to the full file. Briefly summarize what was confirmed
from Figma vs. inferred vs. defaulted, so they know exactly what to verify.

---

## Figma Variable Binding

When the Figma file uses a variable library (especially a two-collection semantic/primitive
system), follow this procedure to discover and bind tokens correctly.

### Discovering semantic tokens in use

Before writing the DESIGN.md, identify which variables are actually being used in the live
design — not just what's defined in the library. The most reliable method:

1. Call `get_design_context` on the **primary design page** (not wireframes or specs).
2. Examine each major section frame for its fill's `boundVariables.color` to identify
   the variable ID that's live on the node.
3. Call `get_variable_defs` to get the full library — then cross-reference IDs to names.

This matters because libraries often contain legacy/deprecated tokens alongside the current
semantic ones. Only bind to variables that are actively used in the current design.

### Token hierarchy: which collection to use

Many Figma files have two or more variable collections:

- **Semantic collection** (e.g., `Vision Variables ONLY`, `Semantics`, `Alias`) — the
  normative layer. Token names carry intent: `surface-inverse`, `text-inverse`, etc. These
  are the tokens DESIGN.md should reference.
- **Primitive collection** (e.g., `Primitives`, `Core`, `Global`) — raw values, no intent.
  Use these only when no semantic equivalent exists.

Always prefer the semantic collection. If you find primitive tokens being used directly for
surfaces or text (e.g., a raw color name like `Primitives/navy` rather than a semantic role
like `surface-inverse`), treat them as candidates for replacement — they are often older tokens
that predate the semantic system. Surface, text, and border roles should all have semantic
equivalents in a mature library.

### Naming conventions to watch for

Semantic surface token names can be **counterintuitive** — don't assume a token name maps
literally to the brand color you'd expect. For example, in many systems `surface-primary`
means the default light/white surface, not the primary brand color, while the brand's darkest
surface might be named `surface-inverse`. Always resolve token IDs to their hex values and
verify against the visual before committing them to DESIGN.md.

### Binding fills in Figma (plugin context)

When a plugin is generating or correcting a Figma design programmatically, bind fills to
variables rather than setting flat hex values. This ensures the design respects the token
system and can be re-themed:

```js
// ✅ correct — bind to semantic variable
const variable = figma.variables.getVariableById(variableId);
const newFill = { type: 'SOLID', color: { r, g, b } };
const boundFill = figma.variables.setBoundVariableForPaint(newFill, 'color', variable);
node.fills = [boundFill];

// ❌ wrong — flat hex, no variable binding
node.fills = [{ type: 'SOLID', color: { r: 0.024, g: 0.051, b: 0.141 } }];
```

After binding, verify success by checking `node.fills[0].boundVariables?.color` — it should
contain a `{ type: 'VARIABLE_ALIAS', id: '...' }` object.

---

## Font identification

When `get_variable_defs` does not return typography tokens, extract font information directly
from text nodes using `get_design_context`. Read node styles directly: `fontName`, `fontSize`,
`lineHeight`, `letterSpacing`. Some typefaces use non-English weight names (e.g., German or
French naming conventions) — when you encounter them, map to the standard numeric weight
scale (100–900) and note the original name as a comment in the YAML for reference. If the
design uses a monospaced companion font, check how it's applied — monospaced fonts in
design systems are typically reserved for structural labels (overlines, code, eyebrows) rather
than body or heading roles, and the DESIGN.md should reflect that constraint explicitly.

---

## YAML front matter guidelines

- Do not use large block comment banners (`# ──────────────`) as section headers within
  the YAML. Use minimal inline comments only where they add clear annotation value (e.g.,
  a weight name or an "inferred from visual" note).
- Do not duplicate information: if a pairing rule is in the markdown Colors section, it does
  not need to be repeated as a YAML comment block in `colors:`.
- Component tokens must use `{token.path}` references, never raw hex or px values. Every
  reference must point to a token that actually exists in the YAML.
- Keep the `figma-variables` block whenever real variable IDs are known — it is the
  authoritative binding map for any Figma-based agent working with this system.

---

## Output format

```
---
version: alpha
name: <design system name from Figma file>

token-policy:
  enforcement: strict
  colors: "bind to figma-variables map; always prefer Semantics/ variables over Primitives/"
  spacing: "use spacing token names; no arbitrary px"
  generated-code: "emit CSS custom properties not hex literals"
  known-exceptions:
    - token: "<token-name>"
      hex: "#RRGGBB"
      reason: "<why this exception exists>"

figma-variables:              # include if variable IDs are known
  semantic-collection: "<collection name>"
  primitive-collection: "<collection name>"
  bindings:
    <role>:
      figma-name: "<Semantics/path/token-name>"
      figma-id: "<VariableID:...>"
      resolved: "#RRGGBB"

colors:
  primary: "#RRGGBB"
  secondary: "#RRGGBB"
  # ... all semantic color roles

typography:
  h1:
    fontFamily: <font name>
    fontSize: <Npx>
    fontWeight: <100–900>     # include weight name as comment if non-obvious
    lineHeight: <ratio>
    letterSpacing: <em>
  # ... continue for all roles

rounded:
  sm: <px>
  md: <px>
  full: "9999px"              # if pill shapes are used

spacing:
  xs: <px>
  sm: <px>
  md: <px>
  lg: <px>
  xl: <px>
  2xl: <px>
  3xl: <px>
  4xl: <px>

grid:                           # include if layout grid values are known
  desktop:
    columns: <N>
    gutter: "<px>"              # use token ref only if value maps exactly to a spacing token
    margin: "<px>"              # grid values often live in a separate layout variable collection
    base-width: "<px>"
    figma-pattern: "COLUMNS"
    figma-alignment: "STRETCH"
    figma-color: "rgba(...)"    # guide overlay color — note from the file, don't guess
    figma-variable-gutter: "<VariableID:...>"   # include if bound to a variable
    figma-variable-margin: "<VariableID:...>"   # include if bound to a variable
  mobile:
    columns: ~                  # set to ~ if no mobile grid is defined in the design system

components:
  <component-name>:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface}"
    rounded: "{rounded.none}"
    paddingX: "{spacing.lg}"
    paddingY: "{spacing.sm}"
---

# Overview
...

# Colors
...

# Typography
...

# Layout
...

# Elevation & Depth
...

# Shapes
...

# Components
...

# Do's and Don'ts
...

# Token Binding          ← include only if Figma variable bindings are documented
...
```

---

## Applying layout grids in Figma

When generating or correcting Figma frames programmatically, always apply `layoutGrids` —
not doing so makes designs harder to audit and maintain.

Always read the `grid:` block in DESIGN.md and apply those exact values — do not use generic defaults. Grid values come from a layout variable collection that is separate from the color/spacing tokens, so they will not match the spacing scale.

```js
// Read grid spec from DESIGN.md — example using Penske Vision values
// Desktop: 12-col, 20px gutter (height/h-5), 40px margin (width/w-10), red guide
const desktopGrid = [{
  pattern: 'COLUMNS',
  alignment: 'STRETCH',
  count: 12,
  gutterSize: 20,   // from grid.desktop.gutter in DESIGN.md
  offset: 40,       // from grid.desktop.margin in DESIGN.md
  visible: true,
  color: { r: 1, g: 0, b: 0, a: 0.1 },  // from grid.desktop.figma-color
  // Bind to layout variables if IDs are in DESIGN.md
  boundVariables: {
    offset: { type: 'VARIABLE_ALIAS', id: '<figma-variable-margin>' },
    gutterSize: { type: 'VARIABLE_ALIAS', id: '<figma-variable-gutter>' }
  }
}];

// Apply to desktop frames
desktopFrame.layoutGrids = desktopGrid;

// Mobile: only apply if grid.mobile is defined (not ~) in DESIGN.md
// If grid.mobile is ~ or absent, set layoutGrids = [] on mobile frames
if (hasMobileGrid) {
  mobileFrame.layoutGrids = [mobileGrid];
} else {
  mobileFrame.layoutGrids = [];
}
```

**Rules:**
- Always read grid values from DESIGN.md — never hardcode gutter/margin values.
- Always apply grids to outermost FRAME nodes only (not groups or child containers).
- Bind to layout variables when IDs are available in the DESIGN.md `figma-variable-*` fields.
- If DESIGN.md has no mobile grid (`mobile: ~`), clear `layoutGrids` on mobile frames.

---

## Tips

- **Validate before you extract**: a bad URL or inaccessible file wastes the user's time.
  Always confirm access first.
- **Scan the production page, not wireframes**: the live design page shows which variables
  are actually bound; wireframes may use different or unbound tokens.
- **Token names aren't always literal**: semantic naming is often counterintuitive. Always
  resolve variable IDs to hex and verify against the visual before committing a token to
  DESIGN.md — don't assume a name like `surface-primary` means the primary brand color.
- **Prefer semantic tokens over primitives**: if the file has both a semantic collection
  and a primitives collection, every binding in DESIGN.md should reference the semantic layer.
  Flag any primitive tokens found in direct use as candidates to migrate.
- **The gap audit is a conversation, not a blocker**: present what you found and what you
  inferred, then ask targeted questions — don't ask about everything at once.
- **Prefer specificity over completeness**: a tight set of well-named tokens is better than
  a sprawling dump of every Figma variable.
- **Token references over raw values in components**: always use `{colors.primary}` not
  `#1A1C1E`.
- **Mark what you inferred**: YAML comments (`# inferred from visual`) help the user know
  what to verify vs. what came directly from the file.
- **Ask before auto-correcting**: for 🔴 violations, always confirm with the user whether
  they want the value corrected to spec or preserved as-is with a flag.
- **Token Binding section goes last**: place it after Do's and Don'ts, never before Overview.
- **Always document and apply grids**: extract `layoutGrids` from production frames and emit
  a `grid:` block in the YAML. When generating frames in Figma, always apply `layoutGrids`
  so designs are immediately auditable against the grid spec.
- **Grid values are often not spacing tokens**: grid gutters and margins frequently live in a
  separate layout variable collection with their own naming scheme. Always check
  `boundVariables` on production frames — record the actual variable IDs in the YAML rather
  than assuming they match spacing tokens.
- **Only emit mobile grid if it exists**: if no mobile grid is defined in the design system,
  set `grid.mobile: ~` in the YAML and clear `layoutGrids` on mobile frames in Figma.
