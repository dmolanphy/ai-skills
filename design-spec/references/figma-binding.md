# Figma Variable Binding and Grid Application

## Contents
- Discovering semantic tokens in use
- Token hierarchy: which collection to use
- Naming conventions to watch for
- Binding fills in Figma (plugin context)
- Applying layout grids in Figma

Load `figma:figma-use` before any `Figma:use_figma` call in this file's plugin sections.

---

### Discovering semantic tokens in use

Before writing the DESIGN.md, identify which variables are actually being used in the live
design — not just what's defined in the library. The most reliable method:

1. Call `Figma:get_design_context` on the **primary design page** (not wireframes or specs).
2. Examine each major section frame for its fill's `boundVariables.color` to identify
   the variable ID that's live on the node.
3. Call `Figma:get_variable_defs` to get the full library — then cross-reference IDs to names.

This matters because libraries often contain legacy/deprecated tokens alongside the current
semantic ones. Only bind to variables that are actively used in the current design.

### Token hierarchy: which collection to use

Many Figma files have two or more variable collections:

- **Semantic collection** (e.g., `Variables ONLY`, `Semantics`, `Alias`) — the
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

## Applying layout grids in Figma

When generating or correcting Figma frames programmatically, always apply `layoutGrids` —
not doing so makes designs harder to audit and maintain.

Always read the `grid:` block in DESIGN.md and apply those exact values — do not use generic defaults. Grid values come from a layout variable collection that is separate from the color/spacing tokens, so they will not match the spacing scale.

```js
// Read grid spec from DESIGN.md — example using sample values
// Desktop: 12-col, 20px gutter (height/h-5), 40px margin (width/w-10), guide color
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
