# DESIGN.md Specification Reference

Source: https://stitch.withgoogle.com/docs/design-md/specification

---

## Overview

A DESIGN.md file has two layers:
- **YAML front matter** (between `---` delimiters): machine-readable design tokens
- **Markdown body**: human-readable rationale in `##` sections

The spec is a foundation, not a prescription. Extend it for domain-specific needs.

---

## YAML Front Matter Schema

```yaml
---
version: <string>        # optional, current version: "alpha"
name: <string>           # required, design system / file name
colors:
  <role>: <hex>          # e.g. primary: "#1A1C1E"
  # roles: primary, secondary, tertiary, surface, background, error, on-primary, etc.
  # shade variants: primary-60, primary-20, etc. (0–100 scale, 60 = 60% opacity/lightness)
typography:
  <level>:               # h1, h2, h3, h4, h5, h6, body, body-sm, caption, label, overline, etc.
    fontFamily: <string>
    fontSize: <Npx>
    fontWeight: <100|200|300|400|500|600|700|800|900>
    lineHeight: <ratio>  # e.g. 1.2 (unitless)
    letterSpacing: <em>  # e.g. -0.02em
rounded:
  <size>: <Npx>          # sm, md, lg, xl, full — border radius values
spacing:
  <size>: <Npx>          # xs, sm, md, lg, xl — spacing/gap values
components:
  <component-name>:
    <property>: <value>  # raw value or token reference
    # Token reference syntax: "{token.name}" e.g. "{colors.primary-60}"
    # Token reference with shade: "{colors.primary-20}"
---
```

### Token reference syntax

Within component values, reference other tokens with `{token.path}`:
- `{colors.primary}` → the primary color hex
- `{colors.primary-60}` → primary color at 60 shade
- `{rounded.md}` → medium border radius
- `{spacing.sm}` → small spacing value
- `{typography.body.fontSize}` → body font size

---

## Token Types

### Typography properties

Every typography level supports:
- `fontFamily` — font name string
- `fontSize` — pixel value string (e.g., "16px")
- `fontWeight` — numeric weight (100–900)
- `lineHeight` — unitless ratio (e.g., 1.5)
- `letterSpacing` — em value (e.g., "0.01em", "-0.02em")

### Color shades

Color roles can have shade variants appended as `-N` where N is 0–100.
A shade of 60 typically means 60% opacity or a mid-weight tint, depending on the system.
Common shades: -10, -20, -40, -60, -80, -90.

---

## Markdown Body Sections

### Required section order

1. `# Overview`
2. `# Colors`
3. `# Typography`
4. `# Layout`
5. `# Elevation & Depth`
6. `# Shapes`
7. `# Components`
8. `# Do's and Don'ts`

Additional custom sections may be added after the required ones.

### Overview
- What this design system is
- Who it's for / target platform/audience
- Key design principles or personality
- Relationship to a brand if relevant

### Colors
- What each color role communicates (brand, emotional intent)
- How the palette was chosen
- Usage guidance: primary actions vs. surfaces vs. accents
- Accessibility notes if relevant

### Typography
- Font family choice and rationale
- Type scale philosophy (e.g., modular scale, baseline grid)
- Usage guidelines per level: what each heading/body size is for
- When to use weight variants

### Layout
- Grid system (columns, gutters, margins)
- Spacing philosophy (the spatial rhythm)
- Key layout patterns (e.g., card-based, list-based)
- Breakpoints if applicable

### Elevation & Depth
- Shadow system (levels, use cases)
- When to use elevation (modals, cards, drawers)
- Z-index philosophy

### Shapes
- Border radius philosophy: rounded vs. sharp, and why
- When to use sm vs. md vs. lg radii
- Special cases (e.g., fully rounded pills for tags)

### Components
- Key component patterns and their intent
- Compositional rules (what can be nested in what)
- State handling (hover, active, disabled, error)
- Any component-specific constraints

### Do's and Don'ts
- Practical guidance formatted clearly
- Common mistakes to avoid
- Things that seem reasonable but break the system

---

## Consumer behavior for unknown content

Consumers of DESIGN.md should:
- **Skip** unknown top-level YAML keys (forward compatibility)
- **Skip** unknown section headers in the markdown body
- **Preserve** the section order when regenerating
- **Not fail** if optional sections are missing

---

## Recommended token names

**Colors**: `primary`, `secondary`, `tertiary`, `surface`, `background`, `error`, `warning`,
`success`, `on-primary`, `on-secondary`, `on-surface`, `outline`, `shadow`

**Typography levels**: `display`, `h1`, `h2`, `h3`, `h4`, `h5`, `h6`, `body`, `body-sm`,
`caption`, `label`, `overline`, `code`

**Spacing**: `xs` (4px), `sm` (8px), `md` (16px), `lg` (24px), `xl` (32px), `2xl` (48px),
`3xl` (64px)

**Rounded**: `none` (0), `sm` (4px), `md` (8px), `lg` (12px), `xl` (16px), `2xl` (24px),
`full` (9999px)
