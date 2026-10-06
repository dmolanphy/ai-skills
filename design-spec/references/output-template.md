# DESIGN.md Output Templates

## Contents
- Audit summary format (Step 4)
- YAML front matter guidelines
- Output format (full skeleton)

---

## Audit summary format (Step 4)

Show this before writing the file. Adapt the rows to what was actually found.

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
1. Standard: validating against Tailwind CSS v3 defaults. Right, or does this project follow another standard?
2. [Specific question about a gap, e.g., "What spacing base unit does this design use?"]
3. Should I auto-correct the 🔴 violations, or preserve the original values and flag them?

Or say "looks good, go ahead" if you're happy with the inferences and want auto-corrections applied.
```


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

