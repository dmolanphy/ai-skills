# Shadcn Token Architecture & Naming

This is the **alternate foundation path** for shadcn/ui-based projects, used instead of `token-architecture.md` when the user picks "shadcn/ui" at the Step 0 foundation-type question. It mirrors the custom-foundation structure where that structure is just a convention (Typography, Spacing modes), and adapts to shadcn's real conventions where shadcn actually defines something (Semantic color pairs, Tailwind's type scale). Read this file *instead of* `token-architecture.md`, not in addition to it — the two paths share the Color-primitives shape, the cover recipe, and the specimen-page recipes, but diverge everywhere else.

## Table of contents
- Naming conventions
- Collection order
- Collection 1: Typography (Tailwind-aligned, Desktop/Mobile modes)
- Collection 2: Color (primitives — unchanged from the custom path)
- Collection 3: Spacing (unchanged from the custom path)
- Collection 4: Semantic (shadcn-shaped, conditional Light/Dark)
- Radius (trimmed, direct values)
- Opt-in extras: chart & sidebar tokens
- Variable scoping (summary table)
- Defaults to use when nothing is specified

---

## Naming conventions

- Same rule as the custom path: **lowercase, slash-grouped**, e.g. `color/primary/brand-primary`, `text-size/lg`.
- **Four collections, same order as the custom path:** `Typography` → `Color` (primitives) → `Spacing` → `Semantic`. Semantic still comes last since it aliases Color.
- **Semantic is single-mode by default.** It only gets `Light`/`Dark` modes if the user opts into dark mode during intake — this is asked per-project, never assumed. If they decline, build Semantic exactly like the custom path's Semantic collection: one mode, one value per token.
- Typography and Spacing keep the existing baseline's **Desktop/Mobile** mode pair — this is *not* how shadcn itself handles responsiveness (shadcn/Tailwind swaps utility classes per breakpoint rather than swapping a token's value), but it's a deliberate, confirmed choice to keep the Figma-side mode-switch convenience rather than match shadcn's literal behavior.

## Collection order

1. **Typography**
2. **Color** (primitives)
3. **Spacing**
4. **Semantic** (shadcn-shaped aliases; conditional modes)

---

## Collection 1: Typography (Desktop / Mobile modes, Tailwind-aligned)

Structurally identical to the custom path (`font-family/*`, `font-weight/*` same value both modes; `font-size` per-mode). The difference is **naming and default values**, aligned to Tailwind's real font-size scale so a developer can read a token name straight into a class name with no translation.

- `font-family/primary`, `/secondary`, `/mono` (STRING)
- `font-weight/light`, `/regular`, `/medium`, `/semibold`, `/bold` (STRING)
- **`font-size`** (FLOAT) — named after Tailwind's `text-*` utilities, Desktop value = Tailwind's real default for that step. Mobile value = the next Tailwind step down; the two smallest are unchanged, matching the custom path's "mobile = next step down" pattern:

| Token | Tailwind class | Desktop | Mobile |
|---|---|---|---|
| `font-size/text-7xl` | `text-7xl` | 72 | 60 |
| `font-size/text-5xl` | `text-5xl` | 48 | 36 |
| `font-size/text-4xl` | `text-4xl` | 36 | 30 |
| `font-size/text-2xl` | `text-2xl` | 24 | 20 |
| `font-size/text-xl` | `text-xl` | 20 | 18 |
| `font-size/text-base` | `text-base` | 16 | 16 |
| `font-size/text-sm` | `text-sm` | 14 | 14 |
| `font-size/text-xs` | `text-xs` | 12 | 12 |

> Inferred default, flagged: this is a subset of Tailwind's full 13-step scale (`xs` through `9xl`) chosen to keep the same 8-role shape as the custom path's Headline/Body/Utility styles. Tailwind's real values are used at Desktop; Mobile step-downs are my own convention (same pattern as Spacing), not a native shadcn/Tailwind behavior. Confirm/adjust during intake like any other value.

**Scoping:** unchanged from the custom path — `font-family/*` → `["FONT_FAMILY"]`, `font-weight/*` → `["FONT_STYLE"]`, `font-size/*` → `["FONT_SIZE","LINE_HEIGHT","PARAGRAPH_SPACING"]`.

---

## Collection 2: Color (primitives — unchanged from the custom path)

**This collection is intentionally identical to `token-architecture.md`'s Color collection.** shadcn's semantic pairs (`primary`/`primary-foreground`, etc.) need to point at *something* — that something is this primitive layer, so brand colors can be imported once (from guidelines or interactively) and referenced by both the custom path's Semantic collection and this path's Semantic collection.

- `color/primary/*` — `brand-primary`, `brand-secondary`, `accent`
- `color/secondary/*` — `secondary-1` … `secondary-5`
- `color/neutral/*` — 7-step ramp: `White`, `Grey-10`, `Grey-20`, `Grey-40`, `Grey-60`, `Grey-80`, `Black`
- `color/utility/*` — `success`, `warning`, `error`

Single mode (`Value`). Scoping: `["ALL_SCOPES"]`.

**Practical effect:** Step 4 of `SKILL.md` (extract from brand guidelines) works unchanged for the shadcn path — same PDF/image extraction, same neutral ramp, no shadcn-specific rewrite needed.

---

## Collection 3: Spacing (unchanged from the custom path)

Reused as-is — Desktop/Mobile modes, `spacing/*` differs per mode (Mobile = next step down), same 11-step scale as `token-architecture.md`. See that file for the full table; nothing shadcn-specific changes here except **Radius**, which moves to its own trimmed shape below (still lives in the Spacing collection, same as the custom path).

---

## Collection 4: Semantic (shadcn-shaped)

Aliases pointing at Color primitives. **Single mode by default** (`Value`); becomes **Light/Dark** only if the user opts into dark mode at intake. Groups mirror shadcn's real CSS-variable pairs, adapted into slash-grouped names, each with a `-foreground` counterpart where shadcn has one.

### Base
`base/background`, `base/foreground`

### Surface
`surface/card`, `surface/card-foreground`, `surface/popover`, `surface/popover-foreground`

### Brand
`brand/primary`, `brand/primary-foreground`, `brand/secondary`, `brand/secondary-foreground`, `brand/accent`, `brand/accent-foreground`

### Utility
`utility/muted`, `utility/muted-foreground`, `utility/destructive`, `utility/destructive-foreground`

### Border
`border/default`, `border/input`, `border/ring`

### Alias map (Light values; Dark column only built if dark mode is opted into)

| Semantic token | Light → | Dark → |
|---|---|---|
| `base/background` | `color/neutral/White` | `color/neutral/Black` |
| `base/foreground` | `color/neutral/Black` | `color/neutral/White` |
| `surface/card` | `color/neutral/White` | `color/neutral/Grey-80` |
| `surface/card-foreground` | `color/neutral/Black` | `color/neutral/White` |
| `surface/popover` | `color/neutral/White` | `color/neutral/Grey-80` |
| `surface/popover-foreground` | `color/neutral/Black` | `color/neutral/White` |
| `brand/primary` | `color/primary/brand-primary` | `color/primary/brand-primary` |
| `brand/primary-foreground` | `color/neutral/White` | `color/neutral/White` |
| `brand/secondary` | `color/primary/brand-secondary` | `color/primary/brand-secondary` |
| `brand/secondary-foreground` | `color/neutral/White` | `color/neutral/White` |
| `brand/accent` | `color/primary/accent` | `color/primary/accent` |
| `brand/accent-foreground` | `color/neutral/White` | `color/neutral/White` |
| `utility/muted` | `color/neutral/Grey-10` | `color/neutral/Grey-80` |
| `utility/muted-foreground` | `color/neutral/Grey-60` | `color/neutral/Grey-40` |
| `utility/destructive` | `color/utility/error` | `color/utility/error` |
| `utility/destructive-foreground` | `color/neutral/White` | `color/neutral/White` |
| `border/default` | `color/neutral/Grey-20` | `color/neutral/Grey-60` |
| `border/input` | `color/neutral/Grey-20` | `color/neutral/Grey-60` |
| `border/ring` | `color/primary/brand-primary` | `color/primary/brand-primary` |

> Inferred default, flagged: brand colors are shown holding constant across modes (common practice — a brand primary usually doesn't change color, just what surrounds it does) but every value here is a starting point to confirm or override during intake, same as the custom path's alias map.

**Scoping:**
- `base/foreground`, `*-foreground` (all of them), `base/background`'s text-adjacent uses → follow the same pattern as the custom path: any token ending in `-foreground` or used purely for text → `["TEXT_FILL"]`
- `base/background`, `surface/*` (non-foreground) → `["FRAME_FILL","SHAPE_FILL"]`
- `border/*` → `["STROKE_COLOR"]`
- `brand/*`, `utility/*` (non-foreground) → `["ALL_SCOPES"]` (used across fills, strokes, and icons in practice)

---

## Radius (trimmed, direct values — lives in the Spacing collection)

Per your direction: **not** derived from a single base via shadcn's multiplier math (that produces decimal pixel values, e.g. 4.8px, which don't work well in a Figma corner-radius field). Instead, four clean, direct values — same spirit as the custom path's `radius/*`, renamed toward shadcn's naming:

| Token | Default value |
|---|---|
| `radius/sm` | 4 |
| `radius/md` | 8 |
| `radius/lg` | 16 |
| `radius/full` | 999 |

Same in both modes (Desktop/Mobile) — radius doesn't change by viewport, matching the custom path's treatment. Scoping: `["CORNER_RADIUS"]`.

---

## Opt-in extras: chart & sidebar tokens

**Not built by default.** Only included if explicitly selected during the shadcn scoped intake (Step 3). This is the mechanism that keeps the skill from "importing everything shadcn has" per the original goal.

### Chart (if selected)
`color/chart/1`, `/2`, `/3`, `/4`, `/5` — five distinct hues, single mode, `["ALL_SCOPES"]`. Default to spaced-out hues from the secondary placeholder set unless the project specifies otherwise.

### Sidebar (if selected)
Semantic-style pairs, same Light/Dark conditionality as the rest of Semantic: `sidebar/background`, `/foreground`, `/primary`, `/primary-foreground`, `/accent`, `/accent-foreground`, `/border`, `/ring`. Scoped the same way as the equivalent Base/Brand/Border tokens above.

---

## Variable scoping (summary table)

| Tokens | scopes |
|---|---|
| `font-family/*` | `["FONT_FAMILY"]` |
| `font-weight/*` | `["FONT_STYLE"]` |
| `font-size/*` | `["FONT_SIZE","LINE_HEIGHT","PARAGRAPH_SPACING"]` |
| `color/*` (primitives, all) | `["ALL_SCOPES"]` |
| `spacing/*` | `["WIDTH_HEIGHT","GAP"]` |
| `radius/*` | `["CORNER_RADIUS"]` |
| `*-foreground` (semantic) | `["TEXT_FILL"]` |
| `base/background`, `surface/*` (non-foreground) | `["FRAME_FILL","SHAPE_FILL"]` |
| `border/*` | `["STROKE_COLOR"]` |
| `brand/*`, `utility/*` (non-foreground) | `["ALL_SCOPES"]` |
| `chart/*`, `sidebar/*` (if opted in) | `["ALL_SCOPES"]` / semantic pattern above |

---

## Defaults to use when nothing is specified

Only a starting point — label as defaults, prefer asking interactively over silently using them, same rule as the custom path.

- **Type scale (px):** see the Typography table above — Desktop 72/48/36/24/20/16/14/12, named `text-7xl` down to `text-xs`.
- **Spacing (px):** identical to the custom path's defaults — see `token-architecture.md`.
- **Radius (px):** `sm` 4, `md` 8, `lg` 16, `full` 999 (same in both modes).
- **Neutral ramp, Secondary placeholders, Utility colors:** identical to the custom path's defaults — see `token-architecture.md`. Reused deliberately so brand-guideline extraction doesn't need a shadcn-specific version.
- **Dark mode:** off by default; ask every project.
- **Chart / Sidebar tokens:** off by default; ask every project.
