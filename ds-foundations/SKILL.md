---
name: ds-foundations
description: >
  Stands up a foundational design-system Figma file at the start of a new design project —
  tokens/variables (typography, color, spacing, radius), semantic tokens, layout grids, and text
  styles, built directly into a Figma file. Supports two foundation types: the user's own custom
  system, or a shadcn/ui-aligned token structure (CSS-variable-style semantic tokens, Tailwind-aligned
  typography). Use whenever the user kicks off a new project needing baseline design foundations, or
  says things like "set up a foundations file," "create the design tokens," "start the DS foundations,"
  "build out type and color tokens," "make the grid and text styles," "set up shadcn tokens in Figma,"
  "build a shadcn foundation," or points to a Figma foundations file to populate — even without saying
  "tokens." Always use for any request to establish baseline design-system tokens, variables, grids, or
  text styles in Figma at kickoff, regardless of foundation type.
---

# Design System Foundations

Stand up the **foundational design-system Figma file** at the start of a new design project: cover, primitive tokens, semantic tokens, layout grids, text styles, and three specimen pages (Typography, Color, Grid). **Baselines only** — not components, full UI, or finished documentation. On the shadcn path this is a token-and-variable baseline, not the shadcn component library; if the user wants components, point them to an existing free Figma kit (e.g. Obra's shadcn/ui community edition, RAVN's shadcn/ui Ultimate Kit).

This skill is self-contained: take conventions, fonts, colors, and layout specs only from this file and its references, never from another skill. Read only the reference set for the chosen foundation type:

| Foundation type | Token structure | Figma build recipes |
|---|---|---|
| Custom (the user's own system) | `references/token-architecture.md` | `references/figma-build.md` |
| shadcn/ui | `references/shadcn-token-architecture.md` | `references/shadcn-figma-build.md` |

Both paths share `references/specimen-pages.md`.

## Golden rules

- **Never guess values silently.** Confirm or ask; each project is specific.
- **Wait for the file.** Ask which Figma file to work in and wait for the URL. Create a new file only if the user explicitly okays it.
- **Match existing conventions** (slash-grouped variable names, semantic text-style names) from the path's token-architecture reference. Do not invent a naming scheme. When a file the user points to differs from a default here, mirror the file.
- **Build real assets** (variables, text styles, grid styles in their panels) **and** the three specimen pages. Pages are standard output; tokens are the source of truth and the pages stay bound to them.
- **shadcn: never "import everything."** Build only the core baseline unless the user opts into more.

## Workflow

### 1. Intake (one round)

Ask everything below in a single turn, using AskUserQuestion for the structured choices, and request the Figma file URL in the same turn. Nothing is built until answers arrive.

1. **Source of truth**, in order of preference: an existing **DESIGN.md** (from `design-spec` or hand-authored; its YAML already holds colors, typography, spacing, radius, grid, so use it directly in step 4); else **brand guidelines as PDF or images only** (no Figma links, websites, or other formats); else collect values interactively.
2. **Foundation type:** custom system or shadcn/ui. Ask directly; never infer from mentions of React or Tailwind.
3. **Scope** (multiSelect, default all): typography tokens, color tokens, spacing + radius primitives, semantic tokens, layout grids, text styles. Specimen pages are always built; ask only if the user wants to skip one.
4. **If shadcn/ui:** **dark mode** (Light-only or Light + Dark; asked fresh every project, never assumed) and **chart and sidebar tokens** (off by default; build only on explicit opt-in).

If the user already supplied values (hex colors, fonts), acknowledge and confirm them instead of re-asking, and never present invented brand colors or fonts as real. Label anything beyond what they gave as a default.

### 2. File and cover

If the user has no file, offer to create one, and only on their explicit okay: call `Figma:whoami`, ask which team/org (prefer an enterprise seat; personal/starter plans hit rate limits), and create it there. Never hard-code an org key.

Tell the user to **open the file in the Figma desktop app** (`use_figma` runs against the open file). List its pages and check for a Cover (detection recipe in `references/figma-build.md`).

- **Cover exists:** leave it untouched; do not ask about it.
- **No cover:** ask for the **title** and whether to place a **logo**, then build it per `references/figma-build.md`: 1920×1080 black frame on a `📕 Cover` page, optional logo top-left (only if supplied), title large in the primary font, light weight, white, lower-left.

### 3. Remaining intake

Ask only what step 1 and the source of truth left open; confirm rather than re-ask.

- **Typography:** headline family, body family, mono (only if needed), weights, base body size, scale ratio.
- **Color:** two brand colors + accent (`color/primary/*`), up to 5 supporting colors (`color/secondary/*`), brand-specific neutrals. Utility colors default to success/warning/error.
- Custom path is **single color mode**; mention modes can be added later. (shadcn dark mode is decided in step 1.)

### 4. Extract and confirm

- **DESIGN.md:** read the YAML and map its keys onto the primitive structure (same shape on both paths; see the Color-primitives section of the path's token-architecture reference). Confirm the mapping with the user.
- **Guidelines (PDF/images):** read them, pull every concrete value (color hex + role; font families, weights, size scale or named styles; spacing/radius/grids only if specified), and show the user what you found. Ask: "Want me to create color tokens from these values?" and the same for type. Fill gaps from the path's defaults, **labeled as defaults**.

Then present the proposed token set (names, values, modes) as a compact plan and get a thumbs-up before writing to Figma.

### 5. Build in Figma

Load `figma:figma-use` (mandatory before `Figma:use_figma`) and skim `figma:figma-generate-library`. Follow the path's build reference. Create collections in this order (panel order follows creation order), setting each variable's `scopes` as you create it (scoping table in the token-architecture reference; not optional):

1. **Typography** — Desktop/Mobile modes. Custom: t-shirt names (`font-size/large`). shadcn: Tailwind-aligned names (`font-size/text-lg`).
2. **Color** — single mode, identical structure on both paths (`color/primary|secondary|neutral|utility/*`; neutral has 7 steps). Scopes left at all properties.
3. **Spacing** — Desktop/Mobile modes (`spacing/*`; Mobile = next step down). Radius: custom uses `radius/*` from `token-architecture.md`; shadcn uses direct-value `radius/sm|md|lg|full`.
4. **Semantic** — aliases to Color. Custom: single mode, `text/*`, `surface/*`, `border/*`. shadcn: `base/*`, `surface/*`, `brand/*`, `utility/*`, `border/*` with `-foreground` pairs; one mode unless dark mode was chosen, then Light/Dark. Chart/sidebar tokens only if opted in.
5. **Grid styles** — Desktop, Tablet, Mobile, values from the token-architecture reference or the guidelines.
6. **Text styles** — `Headline/*` (Jumbo, XL, LG, MD, SM), `Body/*` (LG, Base, MD, SM), `Utility/*` (Eyebrow, Caption), optional `Mono`; same names on both paths. Hanging punctuation ON; line-heights only 100/110/120/130; Eyebrow uppercase + 6% tracking. Bind family/size/weight to variables (fall back to literals with a note). Also create the private `.Docs/*` styles (Header, Spec Name, Spec Detail; recipe in `figma-build.md`).
7. **Specimen pages** — `→ Typography`, `→ Color`, `→ Grid` per `references/specimen-pages.md`. Run after tokens, styles, and grids exist. Screenshot each to verify.

Build incrementally and verify as you go. If a required font is not installed, build with the closest stand-in and leave an off-canvas note frame listing the intended font (recipe in `figma-build.md`).

### 6. Hand off

Brief, conversational summary: cover created (title, logo) or left alone; foundation type; collections with approximate variable counts; modes (including whether dark mode was built); grids; text styles; and anything defaulted or substituted for review (fonts, guessed neutrals).

## Conventions in one place

- Names are **lowercase and slash-grouped** so Figma nests them (`font-family/primary`, `color/primary/brand-primary`, `spacing/space-16`).
- Four collections, same order on both paths. Text styles are semantically named, not sized.
- shadcn semantic tokens follow shadcn's real CSS-variable pairs (`brand/primary`, `brand/primary-foreground`, `utility/muted`...); where shadcn defines nothing (typography, dual-mode spacing), the user's conventions apply. Prefer documented shadcn conventions (ui.shadcn.com/docs/theming) over invented defaults.
- Typography/Spacing keep Desktop/Mobile modes on both paths, a deliberate choice rather than a shadcn convention. Radius is a trimmed direct-value set, not shadcn's derived-multiplier math.
