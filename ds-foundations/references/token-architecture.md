# Token Architecture & Naming

This is the baseline structure for the user's DS Foundations files, distilled from the FEI and GEHC files and refined to current preferences. Treat the **names, structure, and scopes** as fixed conventions; treat the **values** as project-specific defaults to confirm or replace.

## Table of contents
- Naming conventions
- Collection order
- Collection 1: Typography (Desktop / Mobile modes)
- Collection 2: Color
- Collection 3: Spacing (Desktop / Mobile modes)
- Collection 4: Semantic
- Variable scoping (summary table)
- Grids
- Text styles
- Defaults to use when nothing is specified

---

## Naming conventions

- **Lowercase, slash-grouped.** Slashes make Figma nest the variables into groups in the panel. Example: `color/primary/brand-primary`, `font-family/primary`, `spacing/space-16`.
- Observed directly in the user's files: `font-family/primary`, `font-weight/light`. Follow that exact style.
- **Four collections:** `Typography` (font tokens; **Desktop/Mobile** modes), `Color` (color tokens; single mode), `Spacing` (spacing + radius; **Desktop/Mobile** modes), and `Semantic` (aliases that reference Color; single mode).
- **No color modes in the baseline.** Don't create Light/Dark color modes here. The only modes in the baseline are the Desktop/Mobile pairs on Typography and Spacing. In Typography only `font-size` differs between modes; in Spacing only `spacing/*` differs (radius is identical across modes).
- **Text styles use semantic, human names** ("Headline XL", "Body LG") — never size-based names like "48px-bold".

## Collection order

Create the collections in **this exact order** so they appear correctly in the Variables panel (panel order follows creation order):

1. **Typography**
2. **Color**
3. **Spacing**
4. **Semantic** (must come after Color, since it aliases Color)

---

## Collection 1: Typography (Desktop / Mobile modes)

Two modes: `Desktop` and `Mobile`. `font-family` and `font-weight` hold the **same value in both modes**; only `font-size` differs.

- `font-family/primary`, `/secondary`, `/mono` (STRING) — `/mono` only if needed
- `font-weight/light`, `/regular`, `/medium`, `/semibold`, `/bold` (STRING — Figma **style name**, e.g. "Light", "Semi Bold")
- **`font-size`** (FLOAT) — t-shirt names, per-mode values:

| Token | Desktop | Mobile |
|---|---|---|
| `font-size/jumbo` | 72 | 52 |
| `font-size/xxlarge` | 48 | 32 |
| `font-size/xlarge` | 32 | 24 |
| `font-size/large` | 24 | 20 |
| `font-size/medium` | 20 | 16 |
| `font-size/base` | 16 | 16 |
| `font-size/small` | 14 | 14 |
| `font-size/xsmall` | 12 | 12 |

**Scoping:**
- `font-family/*` → **Font family** only (`["FONT_FAMILY"]`)
- `font-weight/*` → **Font weight / style** only (`["FONT_STYLE"]`)
- `font-size/*` → **Font size, Line height, Paragraph spacing** (`["FONT_SIZE","LINE_HEIGHT","PARAGRAPH_SPACING"]`)

---

## Collection 2: Color

Color tokens only, single mode (`Value`). Four groups: `primary`, `secondary`, `neutral`, `utility`.

- **`color/primary/*`** — `brand-primary`, `brand-secondary`, `accent`
- **`color/secondary/*`** — `secondary-1` … `secondary-5` (placeholder hues to replace per project)
- **`color/neutral/*`** — 7-step ramp, exact names: `White`, `Grey-10`, `Grey-20`, `Grey-40`, `Grey-60`, `Grey-80`, `Black`
- **`color/utility/*`** — `success`, `warning`, `error` (no `info`)

**Scoping:** all color variables stay visible in **all supported properties** (`["ALL_SCOPES"]` — the default).

---

## Collection 3: Spacing (Desktop / Mobile modes)

Two modes: `Desktop` and `Mobile`. Holds `spacing/*` and `radius/*`.

- **`spacing/*`** (FLOAT) — per-mode; Mobile takes the next step **down** the scale; `space-8`, `space-4`, `space-none` are identical across modes:

| Token | Desktop | Mobile |
|---|---|---|
| `spacing/space-120` | 120 | 80 |
| `spacing/space-80` | 80 | 64 |
| `spacing/space-64` | 64 | 48 |
| `spacing/space-48` | 48 | 32 |
| `spacing/space-32` | 32 | 24 |
| `spacing/space-24` | 24 | 16 |
| `spacing/space-16` | 16 | 12 |
| `spacing/space-12` | 12 | 8 |
| `spacing/space-8` | 8 | 8 |
| `spacing/space-4` | 4 | 4 |
| `spacing/space-none` | 0 | 0 |

- **`radius/*`** (FLOAT) — **identical in both modes**: `none` (0), `small` (4), `base` (8), `full` (999)

**Scoping:**
- `spacing/*` → **Width & height, Gap (auto layout)** (`["WIDTH_HEIGHT","GAP"]`)
- `radius/*` → **Corner radius** only (`["CORNER_RADIUS"]`)

---

## Collection 4: Semantic

Aliases pointing at the `Color` collection, single mode. Each value is a `VariableAlias` to a color primitive.

### Text (COLOR)
`text/primary`, `text/secondary`, `text/tertiary`, `text/disabled`, `text/brand`, `text/on-brand`, `text/error`

### Surface (COLOR) — four for now
`surface/primary`, `surface/secondary`, `surface/tertiary`, `surface/brand`

### Border (COLOR)
`border/default`, `border/subtle`, `border/strong`, `border/brand`, `border/focus`

### Alias mapping (single mode)
- `text/primary` → `color/neutral/Black`
- `text/secondary` → `color/neutral/Grey-80`
- `text/tertiary` → `color/neutral/Grey-60`
- `text/disabled` → `color/neutral/Grey-40`
- `text/brand` → `color/primary/brand-primary`
- `text/on-brand` → `color/neutral/White`
- `text/error` → `color/utility/error`
- `surface/primary` → `color/neutral/White`
- `surface/secondary` → `color/neutral/Grey-10`
- `surface/tertiary` → `color/neutral/Grey-20`
- `surface/brand` → `color/primary/brand-primary`
- `border/default` → `color/neutral/Grey-20`
- `border/subtle` → `color/neutral/Grey-10`
- `border/strong` → `color/neutral/Grey-40`
- `border/brand` → `color/primary/brand-primary`
- `border/focus` → `color/primary/brand-primary`

**Scoping:**
- `text/*` → **Text fill** only (`["TEXT_FILL"]`)
- `surface/*` → **Frame fill + Shape fill** (`["FRAME_FILL","SHAPE_FILL"]`)
- `border/*` → **Stroke** only (`["STROKE_COLOR"]`)

---

## Variable scoping (summary table)

Scoping controls which property dropdowns a variable shows up in. Set each variable's `scopes` array. Figma `VariableScope` values used here:

| Tokens | scopes |
|---|---|
| `font-family/*` | `["FONT_FAMILY"]` |
| `font-weight/*` | `["FONT_STYLE"]` |
| `font-size/*` | `["FONT_SIZE","LINE_HEIGHT","PARAGRAPH_SPACING"]` |
| `color/*` (all) | `["ALL_SCOPES"]` |
| `spacing/*` | `["WIDTH_HEIGHT","GAP"]` |
| `radius/*` | `["CORNER_RADIUS"]` |
| `text/*` (semantic) | `["TEXT_FILL"]` |
| `surface/*` (semantic) | `["FRAME_FILL","SHAPE_FILL"]` |
| `border/*` (semantic) | `["STROKE_COLOR"]` |

---

## Grids (grid styles)

Three responsive layout grids. Defaults (override with guideline specs):

| Style name | Columns | Margin | Gutter | Typical frame |
|---|---|---|---|---|
| `Grid/Desktop` | 12 | 64 | 24 | 1440 |
| `Grid/Tablet`  | 8  | 32 | 24 | 768 |
| `Grid/Mobile`  | 4  | 16 | 16 | 375 |

Use `COLUMNS` pattern, `STRETCH` alignment, with `offset` = margin and `gutterSize` = gutter.

---

## Text styles

Semantic names, built from the type tokens. Default ramp (tune to the project's scale):

Three subcategories — `Headline/*`, `Body/*`, and `Utility/*`:

| Style | Family token | Weight | Size token | Line height | Tracking | Case |
|---|---|---|---|---|---|---|
| `Headline/Jumbo` | primary | light | `font-size/jumbo` (72) | 100% | -2% | — |
| `Headline/XL` | primary | regular | `font-size/xxlarge` (48) | 110% | -2% | — |
| `Headline/LG` | primary | regular | `font-size/xlarge` (32) | 110% | -1% | — |
| `Headline/MD` | primary | regular | `font-size/large` (24) | 120% | -1% | — |
| `Headline/SM` | primary | medium | `font-size/medium` (20) | 120% | 0 | — |
| `Body/LG` | secondary | regular | `font-size/medium` (20) | 130% | 0 | — |
| `Body/Base` | secondary | regular | `font-size/base` (16) | 130% | 0 | — |
| `Body/MD` | secondary | regular | `font-size/small` (14) | 130% | 0 | — |
| `Body/SM` | secondary | regular | `font-size/xsmall` (12) | 130% | 0 | — |
| `Utility/Eyebrow` | secondary | medium | `font-size/small` (14) | 130% | **6%** | **ALL CAPS** |
| `Utility/Caption` | secondary | regular | `font-size/xsmall` (12) | 130% | 0 | — |
| `Mono` (optional) | mono | regular | `font-size/small` (14) | 130% | 0 | — |

**Rules for every text style:**
- **Line heights are restricted to 100% / 110% / 120% / 130%** (130% is the max). Never use 105/115/140/150 — round to the nearest allowed value.
- **Hanging punctuation is ON** for every style (`textStyle.hangingPunctuation = true`).
- **Eyebrow** is uppercase (`textCase = "UPPER"`) with **6%** letter-spacing.

Bind each style's family/size/weight to the matching variable where the API allows (headlines → `font-family/primary`; body & utility → `font-family/secondary`); otherwise set literal values and leave a note. Drop `Mono` if the project has no mono family.

---

## Defaults to use when nothing is specified

Only a starting point — label these as defaults the user can change, and prefer asking interactively over silently using them.

- **Type scale (px):** see the Typography per-mode table. Desktop: xsmall 12, small 14, base 16, medium 20, large 24, xlarge 32, xxlarge 48, jumbo 72.
- **Spacing (px):** see the Spacing per-mode table. Desktop: none 0, 4, 8, 12, 16, 24, 32, 48, 64, 80, 120. Mobile = next step down (8/4/none unchanged).
- **Radius (px):** none 0, small 4, base 8, full 999 (same in both modes)
- **Neutral ramp (7 steps):** White #FFFFFF, Grey-10 #F2F2F3, Grey-20 #E3E4E6, Grey-40 #A6A9AF, Grey-60 #5C606A, Grey-80 #2A2D34, Black #000000
- **Secondary (5 placeholder base colors):** distinct hues to replace per project, e.g. #1A73E8, #1E8E3E, #F9AB00, #9334E6, #FF5C39
- **Utility:** success #1E8E3E, warning #F9AB00, error #D93025
- **Weights:** Light, Regular, Medium, Semi Bold, Bold (only those actually in the chosen family)
