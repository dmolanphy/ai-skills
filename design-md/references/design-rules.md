# Design Rules Reference

This file defines the default validation rules used when generating and auditing a DESIGN.md file.
The default standard is **Tailwind CSS v3 defaults**. Project-specific overrides may replace or
extend these rules when the user specifies a different standard.

---

## How to use this file

During the rules validation step:
1. Load the active standard (Tailwind by default, or the user-specified one)
2. Check each extracted token against the rules below
3. Flag deviations — don't silently accept out-of-spec values
4. For each deviation, suggest the nearest valid value and explain why

---

## Tailwind CSS v3 Defaults

### Type ramp

Tailwind's font size scale uses a roughly 1.125–1.25× ratio per step. All `fontSize` values in
`typography` should snap to this scale (±1px tolerance). Values not on the scale should be flagged.

**Valid font sizes (px):**
```
12, 14, 16, 18, 20, 24, 30, 36, 48, 60, 72, 96, 128
```

**Font weight rules:**
- Use only defined Tailwind weights: 100, 200, 300, 400, 500, 600, 700, 800, 900
- Display/h1: typically 700–900
- Headings (h2–h4): typically 600–700
- Body: typically 400–500
- Caption/label: typically 400–500
- Flag weights like 350, 450, 550 — these are non-standard and may not render correctly cross-platform

**Line height rules:**
- Use named ratios: 1 (none), 1.25 (tight), 1.375 (snug), 1.5 (normal), 1.625 (relaxed), 2 (loose)
- Body text: 1.5–1.625 recommended
- Display/headings: 1–1.25 recommended
- Flag values outside 1–2 range as unusual

**Letter spacing rules (em):**
- Valid range: -0.05em to 0.1em
- Tight tracking (display): -0.05em to -0.01em
- Normal body: 0 to 0.025em
- Wide (overline/caps): 0.05em to 0.1em
- Flag values outside this range

**Heading hierarchy rule:**
- Each heading level must be strictly smaller than the level above it
- e.g., h2.fontSize < h1.fontSize, h3.fontSize < h2.fontSize, etc.
- Gaps between levels should be at least one step on the scale

---

### Grid & spacing

Tailwind uses a **4px base unit**. All spacing values must be multiples of 4px.

**Valid spacing values (px):**
```
4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 56, 64, 72, 80, 96, 112, 128
```

**Rules:**
- All `spacing` token values must be multiples of 4
- All `rounded` token values must be multiples of 2 (Tailwind uses 2px steps for border radius)
- Flag any value that is not a multiple of its base unit
- Spacing scale should have at least xs/sm/md/lg defined
- Spacing values should increase monotonically (sm < md < lg)

**Valid rounded values (px):**
```
0, 2, 4, 6, 8, 12, 16, 24, 9999 (full)
```

---

### Color system

**Required color roles:**
Every design system must define at minimum:
- `primary` — main brand/action color
- `surface` or `background` — page/card background
- `on-primary` or a legible text-on-primary color

**Recommended additional roles:**
- `secondary` — supporting brand color
- `tertiary` — accent color
- `error` — destructive/error state
- `outline` — border/divider color

**Contrast rules (WCAG AA):**
- Normal text on background: contrast ratio ≥ 4.5:1
- Large text (18px+ regular, 14px+ bold) on background: ≥ 3:1
- UI components and graphical elements: ≥ 3:1
- Flag any primary text color on its background that falls below these thresholds
- Note: full contrast calculation requires both foreground and background colors to be defined

**Color completeness rules:**
- If `primary` is defined, `on-primary` (or equivalent) should also be defined
- Shade variants (e.g., `primary-60`) must be derivable from the base color
- Flag orphaned shade variants (e.g., `primary-60` defined but no `primary`)

---

### Component tokens

**Token reference rules:**
- All component color values must use token references (`{colors.primary}`) — not raw hex values
- All component sizing values (padding, radius) must use token references (`{rounded.md}`, `{spacing.sm}`)
- Exception: pixel values for padding/gap that are intentionally component-specific (not in spacing scale) may be raw, but should be flagged for review
- Every token referenced in a component (`{colors.primary-60}`) must exist as a defined token in the YAML — flag broken references

**Component completeness:**
- Each component entry should have at minimum: a background/surface color and a text/content color
- Interactive components (buttons, inputs) should define both default and at least one state variant

---

## Asking about alternate standards

At the start of each run, ask:

> "This will validate your design tokens against **Tailwind CSS v3 defaults**. Is that right,
> or does this project follow a different standard?" 

If the user says yes to a different standard, ask them to describe it (or paste a reference).
Common alternatives to handle:
- **Material Design 3**: uses a 4px grid, specific type roles (Display, Headline, Title, Body, Label),
  tonal color system with 6 roles + on-variants + container variants
- **Apple HIG / SF**: different type scale, system font, specific semantic color tokens
- **Custom**: user provides their own rules inline — capture them and apply them instead

When a custom standard is provided, derive rules from it using the same structure as above
(valid values, hierarchy rules, required roles) and apply them in place of Tailwind defaults.

---

## Validation output format

When reporting rule violations, use this format:

```
⚠️  [Token path] — [Rule violated]
    Found: [actual value]
    Expected: [valid value or range]
    Suggestion: [nearest valid value or fix]
```

Example:
```
⚠️  typography.h3.fontSize — not on Tailwind type scale
    Found: 22px
    Expected: one of 20px, 24px
    Suggestion: use 24px (h3 typically sits between h4=20px and h2=30px)

⚠️  spacing.md — not a multiple of 4px
    Found: 15px
    Expected: multiple of 4
    Suggestion: use 16px

⚠️  components.button-primary.backgroundColor — raw hex value, should be a token reference
    Found: "#1A1C1E"
    Expected: "{colors.primary}" or similar
    Suggestion: replace with "{colors.primary}"
```

Group violations by severity:
- 🔴 **Must fix**: broken token references, missing required color roles, heading hierarchy violations
- 🟡 **Should fix**: values off the standard scale, missing on-color variants
- 🔵 **Consider**: non-standard but functional values, optional roles missing
