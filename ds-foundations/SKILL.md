---
name: ds-foundations
description: >
  Stand up a foundational design-system Figma file at the start of a new design project —
  tokens/variables (typography, color, spacing, radius), semantic tokens, layout grids, and
  text styles, built directly into a Figma file the user points to. Supports two foundation
  types: the user's own custom system, or a shadcn/ui-aligned token structure (CSS-variable-style
  semantic tokens, Tailwind-aligned typography). Use this skill whenever the user kicks off a
  new project and needs baseline design foundations, or says things like "set up a foundations
  file," "create the design tokens," "start the DS foundations," "build out our type and color
  tokens," "make the grid and text styles," "set up shadcn tokens in Figma," "build a shadcn
  foundation," or points to a Figma foundations file and asks to populate it — even if they
  don't say the word "tokens." Always use this skill for any request about establishing baseline
  design-system tokens, variables, grids, or text styles in Figma at project kickoff, regardless
  of which foundation type is named.
---

# Design System Foundations

You are helping the user stand up the **foundational design-system Figma file** that gets created at the start of nearly every new design project. This is a highly repeatable setup with project-specific values. Your job is to (1) get the right Figma file to work in, (2) make sure it has a cover, (3) find out whether this project is building its own foundation or starting from shadcn/ui, (4) gather the project's specifics — extracting from brand guidelines where possible — and (5) build the foundations directly into that file: variables, grids, and text styles, using the right conventions for the path chosen.

This skill is for **baselines only.** It gets the cover, primitive tokens, semantic tokens, grids, and text styles in place so design work can start. It is not for building components, full UI, or finished documentation pages. On the shadcn path specifically, this is a **token-and-variable baseline, not a shadcn component library** — it does not build the ~50 shadcn components. If the user wants those, point them at an existing free Figma kit (e.g. the Obra shadcn/ui community edition, or the RAVN shadcn/ui Ultimate Kit) rather than building components here.

This skill is self-contained. Everything you need is in this file and the references below — do not pull conventions, fonts, colors, or layout specs from any other skill. There are **two parallel sets of references** depending on the foundation type chosen in Step 3 — read only the set for the path you're on:
- **Custom foundation:** `references/token-architecture.md` (token structure, naming, defaults, distilled from the user's FEI/GEHC files) and `references/figma-build.md` (plugin-API recipes for variables, styles, grids).
- **Shadcn/ui foundation:** `references/shadcn-token-architecture.md` and `references/shadcn-figma-build.md` — same shape, adapted to shadcn's real CSS-variable conventions where shadcn defines something, and layered with the user's own conventions where it doesn't (typography, dual-mode spacing).

Both paths share `references/specimen-pages.md` (the Typography/Color/Grid documentation-page builders) unchanged — it's data-driven off live variable/style names, not hardcoded to either path.

---

## Golden rules

- **Never guess values silently.** Confirm or ask. The whole point of the intake is that each project is specific.
- **Wait for the file.** Always ask which Figma file to work in and wait for the URL before doing anything. Never create a new file unless the user explicitly says it's okay.
- **Match the user's conventions** (slash-grouped variable names, semantic text-style names). They're in `references/token-architecture.md` (custom path) or `references/shadcn-token-architecture.md` (shadcn path). Don't invent a new naming scheme.
- **Cover logic:** If the file already has a Cover page, leave it exactly as-is and move on. If it has none, create one in the FEI/GEHC style — but ask the user for the title first.
- **Build the real Figma assets** (variables, text styles, grid styles in their panels) **and** the three specimen pages that document them (Typography, Color, Grid), modeled on the user's FEI file. The pages are standard output now, not optional — the tokens are the source of truth, the pages visualize them and stay bound to them.
- **On the shadcn path, never default to "import everything."** shadcn is large and comprehensive; ask what's actually needed (Step 4's scoped intake) rather than building chart tokens, sidebar tokens, or anything beyond the core baseline unless the user opts in.

---

## Workflow

### Step 1 — Get the Figma file (ask, then wait)

Ask the user which Figma file to work in and **wait for them to give you the URL.** Do not proceed without it.

If the user doesn't have a file yet, offer to create one — but **only create a new file if they explicitly say it's okay.** When they okay it, call `whoami` to list their teams/orgs and ask which one to use (prefer an enterprise seat — personal/starter plans hit Figma rate limits quickly), then create the file there. Never silently spin up a file, and never hard-code an org key.

Once you have the file, tell the user to **open it in the Figma desktop app** — the `use_figma` plugin runs against the open file. Then inspect it: list its pages and check for an existing Cover (cover-detection recipe in `references/figma-build.md`). Report what's there.

### Step 2 — Cover page

- **If a Cover already exists:** leave it completely untouched and move on to Step 3.
- **If there is no Cover:** ask the user what **title** the cover should use (e.g. "Design System: Foundations," or a project/brand name). Wait for their answer, then build a cover in the FEI/GEHC style using the cover recipe in `references/figma-build.md` — a 1920×1080 black frame on a `📕 Cover` page, the **bundled Huge logo top-left** (always present — read `assets/huge-logo-base64.txt` and inject it into the recipe; never resize, round, or replace it), and the title set large in the primary font, light weight, white, lower-left.

Only ask about the title when you're actually going to create the cover. If one exists, don't ask.

### Step 3 — Foundation type

Ask which foundation this project needs, before running the intake — the answer determines which reference files and which intake questions apply:

- **Your own system** — the existing custom foundation (`token-architecture.md` / `figma-build.md`).
- **shadcn/ui** — adapted token structure that mirrors shadcn's real CSS-variable conventions (`shadcn-token-architecture.md` / `shadcn-figma-build.md`).

Don't guess this from context (e.g. don't assume shadcn just because the user mentioned React or Tailwind) — ask directly and wait for the answer, same as the file URL and cover title.

### Step 4 — Intake interview

Run a short, focused intake. Use the AskUserQuestion tool where it helps. Cover these, in roughly this order:

1. **Brand guidelines.** Ask: *"Do you have existing brand guidelines I should pull from? If so, share them as a PDF or image files."* Accept **PDF or images only** — do not offer or accept Figma links, websites, or other formats. If the user provides them, extract color and typography (see Step 4). If not, you'll collect values interactively.
2. **Scope.** Which to build this run (default: all): typography tokens, color tokens, spacing + radius primitives, semantic tokens, layout grids, text styles. Let them drop any.
3. **Typography specifics** (if not coming cleanly from guidelines): headline font family, body font family, mono (only if needed), the weights in use, base body size, and scale ratio.
4. **Color specifics** (if not from guidelines): the two brand colors + accent (`color/primary/*`), up to 5 supporting base colors (`color/secondary/*`), and any brand-specific neutrals. Utility colors default to success/warning/error.
5. **Specimen pages** are built by default (Typography, Color, Grid) — you don't need to ask. Only ask if the user wants to *skip* any of them.

**If the shadcn/ui path was chosen in Step 3, also ask:**

6. **Dark mode.** Build Light-only, or Light + Dark? This is asked fresh every project — never assumed from a previous run or from context. Determines whether the Semantic collection gets one mode or two (see `shadcn-token-architecture.md`).
7. **Chart & sidebar tokens.** Off by default. Ask explicitly whether the project needs either — don't build them unasked. This is the main lever for not importing "everything shadcn has."

This baseline is **single color mode on the custom path** — don't build Light/Dark there. Mention that modes can be added later once the system matures. (The shadcn path's dark-mode question above is the one exception — it's asked, not defaulted either way.)

Don't over-interview. If guidelines answer a question, confirm rather than ask from scratch.

### Step 5 — Extract from brand guidelines (when provided as PDF/images)

Read the PDF or image files and pull every concrete value you can, then **show the user what you found before building** so they can correct it:

- **Color:** hex values with their intended roles (primary, secondary, accent, neutrals, utility). Map them onto the primitive structure — this is the same on both paths; see `references/token-architecture.md` (custom path) or `references/shadcn-token-architecture.md`'s Color-primitives section (shadcn path, structurally identical).
- **Typography:** font families (headline / body / mono), the weights, and any documented size scale or named styles.
- **Spacing / radius / grids:** only if the guidelines specify them; otherwise use the defaults from the appropriate token-architecture reference for the chosen path, and tell the user they're defaults they can tune.

Ask explicitly: *"Want me to create color tokens from these guideline values?"* and the same for type. Anything the guidelines don't cover, fill from defaults and **label it as a default**, or collect interactively — the user prefers to be asked when there's nothing to extract from.

Present the proposed token set (names + values + modes) as a compact plan and get a thumbs-up before writing to Figma. This is the last cheap moment to fix naming or values.

### Step 6 — Build in Figma

Before calling `use_figma`, read the Figma plugin's `/figma-use` skill (mandatory per the Figma MCP server) and skim `/figma-generate-library` for design-system patterns. Then build, following `references/figma-build.md` (custom path) **or** `references/shadcn-figma-build.md` (shadcn path — chosen in Step 3):

Create the collections in this exact order on both paths (panel order follows creation order): **Typography → Color → Spacing → Semantic.** Set each variable's `scopes` as you create it (full scoping table in `references/token-architecture.md` or `references/shadcn-token-architecture.md`) — this is a key step, not optional. On the shadcn path, Semantic's mode count (one vs. Light/Dark) depends on the Step 4 dark-mode answer — never build both modes without having asked.

1. **Typography collection** — two modes (**Desktop**/**Mobile**) on both paths. Custom path: t-shirt names (`font-size/large`, etc.), full table in `references/token-architecture.md`. Shadcn path: Tailwind-aligned names (`font-size/text-lg`, etc.), full table in `references/shadcn-token-architecture.md`. Scopes are the same on both: Font family / Font style / Font size + Line height + Paragraph spacing.
2. **Color collection** — single mode, **structurally identical on both paths**: `color/primary/*`, `color/secondary/*`, `color/neutral/*` (7 steps), `color/utility/*`. Scopes left as all properties. This is deliberate — it lets brand-guideline extraction (Step 5) work the same regardless of foundation type.
3. **Spacing collection** — two modes (**Desktop**/**Mobile**) on both paths: `spacing/*` (scope Width/height + Gap; per-mode, Mobile = next step down). **Radius differs by path:** custom path uses `references/token-architecture.md`'s `radius/*`; shadcn path uses the trimmed, direct-value `radius/sm`/`/md`/`/lg`/`/full` in `references/shadcn-token-architecture.md` (no derived multiplier math — flagged there as a deliberate simplification, not shadcn's literal formula).
4. **Semantic collection** — aliases pointing at Color. Custom path: single-mode, `text/*`/`surface/*`/`border/*`, alias map in `references/token-architecture.md`. Shadcn path: single mode **unless** the Step 4 dark-mode question was answered yes, in which case Light/Dark modes; groups are `base/*`, `surface/*`, `brand/*`, `utility/*`, `border/*` with `-foreground` pairs, alias map and conditional-mode build logic in `references/shadcn-token-architecture.md` / `references/shadcn-figma-build.md`. If chart/sidebar tokens were opted into during Step 4, build those here too (recipe in `references/shadcn-figma-build.md`) — otherwise skip them entirely.
5. **Grid styles** — Desktop, Tablet, Mobile, with the column counts / margins / gutters from the appropriate token-architecture reference (or guideline-specified). Same on both paths.
6. **Text styles** — three groups on both paths: `Headline/*` (Jumbo, XL, LG, MD, SM), `Body/*` (LG, Base, MD, SM), `Utility/*` (Eyebrow, Caption), plus optional `Mono`. Style *names* are identical on both paths — only the underlying size-token references differ (t-shirt vs. Tailwind-aligned). Every style has hanging punctuation ON; line-heights are limited to 100/110/120/130; Eyebrow is uppercase + 6% tracking. Bind family/size/weight to variables; fall back to literal values with a note if binding fails. Also create the private **`.Docs/*` chrome styles** (period-prefixed so they don't publish: Header, Spec Name, Spec Detail) the spec pages use — recipe in `references/figma-build.md` (shared, unchanged on both paths).
7. **Specimen pages** — after the tokens/styles/grids exist, build the `→ Typography`, `→ Color`, and `→ Grid` documentation pages following `references/specimen-pages.md`, **unchanged on both paths** — it reads live variable/style names and groupings rather than hardcoding either path's conventions. The Typography page is a column/spec-table layout (one column per group; each style shows its live spec values beside a specimen; 4px rule above each column header, 1px between entries). Color swatches bind fills to color variables (name + hex labels); grid frames bind to grid styles. All page chrome (titles, headers, spec text, labels) binds to the `.Docs/*` styles. Screenshot each to verify before finishing.

Build incrementally and verify as you go (the recipes file explains how to re-read what you created). If a required font isn't installed locally, substitute the closest available font, build with the stand-in, and leave an off-canvas note frame listing the intended font and the swap so the user can fix it later (recipe in `references/figma-build.md`).

### Step 7 — Hand off

Give the user a brief, conversational summary: whether you created a cover (and its title) or left an existing one alone, which foundation type was built, which collections and roughly how many variables per group, the modes (including whether dark mode was built, on the shadcn path), the grids, and the text styles you created — plus anything you defaulted or substituted that they should review (fonts, guessed neutrals, etc.). Keep it short; they can open the panels for detail.

---

## What "match my system" means

the user's conventions, confirmed from the FEI and GEHC foundations files and detailed in `references/token-architecture.md`:

- Variable names are **lowercase, slash-grouped** so Figma nests them: `font-family/primary`, `font-weight/light`, `color/primary/brand-primary`, `spacing/space-16`, `radius/base`.
- Four collections, created in order: **Typography** (Desktop/Mobile modes), **Color** (single mode), **Spacing** (Desktop/Mobile modes), **Semantic** (single-mode aliases → Color). No Light/Dark color modes in the baseline.
- Variables are **scoped** so each only appears where it belongs (full table in `references/token-architecture.md`).
- Text styles are **semantically named** under `Headline/*`, `Body/*`, `Utility/*` — not sized names.
- Tokens live in the **Variables/Styles panels**; the canvas documents them on dedicated pages — a `📕 Cover` page (black, large light-weight title, Huge logo top-left) plus `→ Typography`, `→ Color`, and `→ Grid` specimen pages.

When in doubt, mirror what's already in the file the user points you to over any default here.

---

## What "shadcn/ui foundation" means

The alternate path, used when Step 3's answer is shadcn/ui. Detailed in `references/shadcn-token-architecture.md` and `references/shadcn-figma-build.md`:

- Same **lowercase, slash-grouped** naming rule, same **four collections in the same order** (Typography → Color → Spacing → Semantic).
- **Color (primitives) is intentionally identical to the custom path** — same `color/primary/*`, `/secondary/*`, `/neutral/*`, `/utility/*` shape — so a brand's palette can be imported once, then referenced by shadcn's semantic pairs.
- **Semantic is shaped after shadcn's real CSS-variable pairs** (`primary`/`primary-foreground`, `muted`/`muted-foreground`, etc.), adapted into slash-grouped names (`brand/primary`, `brand/primary-foreground`, `utility/muted`, `utility/muted-foreground`...). It's **single-mode unless dark mode is opted into that project** — never built with two modes by default.
- **Typography and Spacing keep the Desktop/Mobile mode convenience** even though shadcn/Tailwind itself doesn't work that way (it swaps utility classes per breakpoint, not token values) — this was a deliberate choice to keep, not a shadcn convention.
- **Typography naming and default values are Tailwind-aligned** (`text-sm`, `text-base`, `text-lg`...) rather than the custom path's t-shirt names, since shadcn ships no typography tokens of its own — matching Tailwind's real scale lets a developer read a Figma spec straight into a class name.
- **Radius is a trimmed 4-value set with direct values** (`sm`/`md`/`lg`/`full`), not shadcn's literal derived-multiplier math — chosen deliberately to avoid decimal pixel values in Figma's corner-radius field.
- **Chart and sidebar tokens are opt-in only** — never built unless explicitly requested in the Step 4 intake. This is the main guardrail against importing more of shadcn than the project needs.
- This path is **tokens and variables only** — it does not build shadcn's component library. Point users at an existing free Figma kit for components (see the note at the top of this file).

When in doubt on this path, prefer shadcn's real documented conventions (ui.shadcn.com/docs/theming) over an invented default — the custom path's conventions only apply where noted above.
