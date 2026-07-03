# Shadcn Figma Build Recipes

Plugin-API recipes for the shadcn/ui foundation path. Read alongside `shadcn-token-architecture.md` for the values/naming these recipes implement. **Shared with the custom path, reused unchanged — do not duplicate:** the Cover recipe, the Inspect/detect-Cover recipe, the `hexToRgb` helper, and all of `specimen-pages.md` (it's data-driven off `getLocalTextStyles()` / `getLocalVariables()` by group prefix, not hardcoded token names, so it works against either path's output as-is). Read `figma-build.md` for those.

## Table of contents
- Create collections & modes (conditional Semantic modes)
- Create Color primitives (reuse from figma-build.md)
- Create Typography variables (Tailwind-aligned)
- Create Radius variables (direct values)
- Create Semantic variables (shadcn-shaped, conditional dark mode)
- Create text styles (Tailwind-named)
- Opt-in: chart & sidebar tokens

---

## Create collections & modes

Same four-collection order as the custom path. The difference: **Semantic's mode count depends on the dark-mode intake answer**, decided once, before this runs.

```js
// darkModeEnabled comes from the Step 3 intake answer — never assumed.
const darkModeEnabled = true; // or false — set from the user's answer

// 1. Typography — Desktop + Mobile modes (same as custom path)
const typo = figma.variables.createVariableCollection("Typography");
const dMode = typo.modes[0].modeId; typo.renameMode(dMode, "Desktop");
const mMode = typo.addMode("Mobile");

// 2. Color (primitives) — single mode, identical shape to the custom path
const color = figma.variables.createVariableCollection("Color");
color.renameMode(color.modes[0].modeId, "Value");
const colorMode = color.modes[0].modeId;

// 3. Spacing — Desktop + Mobile modes (same as custom path; radius lives here too)
const spacing = figma.variables.createVariableCollection("Spacing");
const sdMode = spacing.modes[0].modeId; spacing.renameMode(sdMode, "Desktop");
const smMode = spacing.addMode("Mobile");

// 4. Semantic — single mode by default; Light/Dark only if opted in
const sem = figma.variables.createVariableCollection("Semantic");
let lightMode, darkModeId;
if (darkModeEnabled) {
  lightMode = sem.modes[0].modeId; sem.renameMode(lightMode, "Light");
  darkModeId = sem.addMode("Dark");
} else {
  lightMode = sem.modes[0].modeId; sem.renameMode(lightMode, "Value");
  darkModeId = null;
}
```

---

## Create Color primitives (reuse from figma-build.md)

Identical helper and identical calls to the custom path's "Create primitive variables → Color variables (single mode)" section — same `colorVar(name, hex)` function, same `color/primary/*`, `color/secondary/*`, `color/neutral/*`, `color/utility/*` names. Do not redefine this; copy the function and calls straight from `figma-build.md`.

---

## Create Typography variables (Tailwind-aligned)

Same pattern as the custom path's `typoStr` / `fontSizeVar` helpers, renamed to the Tailwind-aligned token names from `shadcn-token-architecture.md`.

```js
function typoStr(name, value, scopes) {
  const v = figma.variables.createVariable(name, typo, "STRING");
  v.setValueForMode(dMode, value);
  v.setValueForMode(mMode, value);
  v.scopes = scopes;
  return v;
}
function fontSizeVar(name, desktop, mobile) {
  const v = figma.variables.createVariable(name, typo, "FLOAT");
  v.setValueForMode(dMode, desktop);
  v.setValueForMode(mMode, mobile);
  v.scopes = ["FONT_SIZE", "LINE_HEIGHT", "PARAGRAPH_SPACING"];
  return v;
}

typoStr("font-family/primary", "Inter", ["FONT_FAMILY"]);
typoStr("font-weight/regular", "Regular", ["FONT_STYLE"]);
typoStr("font-weight/medium", "Medium", ["FONT_STYLE"]);
typoStr("font-weight/semibold", "Semi Bold", ["FONT_STYLE"]);

fontSizeVar("font-size/text-7xl", 72, 60);
fontSizeVar("font-size/text-5xl", 48, 36);
fontSizeVar("font-size/text-4xl", 36, 30);
fontSizeVar("font-size/text-2xl", 24, 20);
fontSizeVar("font-size/text-xl",  20, 18);
fontSizeVar("font-size/text-base", 16, 16);
fontSizeVar("font-size/text-sm", 14, 14);
fontSizeVar("font-size/text-xs", 12, 12);
```

---

## Create Radius variables (direct values, no derived math)

Deliberately **not** computed from a single base — direct values only, per your direction. Same mode-handling as the custom path's radius (identical in Desktop/Mobile).

```js
function radiusVar(name, value) {
  const v = figma.variables.createVariable(name, spacing, "FLOAT");
  v.setValueForMode(sdMode, value);
  v.setValueForMode(smMode, value);
  v.scopes = ["CORNER_RADIUS"];
  return v;
}
radiusVar("radius/sm", 4);
radiusVar("radius/md", 8);
radiusVar("radius/lg", 16);
radiusVar("radius/full", 999);
```

Spacing variables themselves (`spacing/*`) are unchanged from the custom path — copy `spaceVar()` and its calls straight from `figma-build.md`.

---

## Create Semantic variables (shadcn-shaped, conditional dark mode)

Aliases pointing at Color primitives. **Sets a dark-mode value only if the Semantic collection has a Dark mode** — checked at runtime via `darkModeId`, so this one function works for both cases without branching per-call.

```js
const byName = Object.fromEntries(figma.variables.getLocalVariables().map(v => [v.name, v]));

function scopeFor(name) {
  if (name.endsWith("-foreground")) return ["TEXT_FILL"];
  if (name.startsWith("border/"))   return ["STROKE_COLOR"];
  if (name.startsWith("base/background") || name.startsWith("surface/")) return ["FRAME_FILL", "SHAPE_FILL"];
  return ["ALL_SCOPES"]; // brand/*, utility/* (non-foreground)
}

function semanticColor(name, lightPrimitiveName, darkPrimitiveName) {
  const v = figma.variables.createVariable(name, sem, "COLOR");
  v.setValueForMode(lightMode, figma.variables.createVariableAlias(byName[lightPrimitiveName]));
  if (darkModeId) {
    // darkPrimitiveName falls back to the light one if a project keeps a token constant across modes
    const darkTarget = darkPrimitiveName || lightPrimitiveName;
    v.setValueForMode(darkModeId, figma.variables.createVariableAlias(byName[darkTarget]));
  }
  v.scopes = scopeFor(name);
  return v;
}

// [token, light primitive, dark primitive] — dark primitive omitted where the alias map holds it constant
semanticColor("base/background", "color/neutral/White", "color/neutral/Black");
semanticColor("base/foreground", "color/neutral/Black", "color/neutral/White");
semanticColor("surface/card", "color/neutral/White", "color/neutral/Grey-80");
semanticColor("surface/card-foreground", "color/neutral/Black", "color/neutral/White");
semanticColor("surface/popover", "color/neutral/White", "color/neutral/Grey-80");
semanticColor("surface/popover-foreground", "color/neutral/Black", "color/neutral/White");
semanticColor("brand/primary", "color/primary/brand-primary");
semanticColor("brand/primary-foreground", "color/neutral/White");
semanticColor("brand/secondary", "color/primary/brand-secondary");
semanticColor("brand/secondary-foreground", "color/neutral/White");
semanticColor("brand/accent", "color/primary/accent");
semanticColor("brand/accent-foreground", "color/neutral/White");
semanticColor("utility/muted", "color/neutral/Grey-10", "color/neutral/Grey-80");
semanticColor("utility/muted-foreground", "color/neutral/Grey-60", "color/neutral/Grey-40");
semanticColor("utility/destructive", "color/utility/error");
semanticColor("utility/destructive-foreground", "color/neutral/White");
semanticColor("border/default", "color/neutral/Grey-20", "color/neutral/Grey-60");
semanticColor("border/input", "color/neutral/Grey-20", "color/neutral/Grey-60");
semanticColor("border/ring", "color/primary/brand-primary");
```

---

## Create text styles (Tailwind-named)

Same structure and rules as the custom path (hanging punctuation ON, line-heights restricted to 100/110/120/130, Eyebrow uppercase + 6% tracking) — only the size-token names change to match the Tailwind-aligned Typography collection above. Style *names* (`Headline/Jumbo`, `Body/Base`, etc.) stay the same so `specimen-pages.md` needs no changes — it groups by the `Headline`/`Body`/`Utility` prefix, not by size-token name.

```js
for (const st of ["Regular","Medium","Semi Bold"]) await figma.loadFontAsync({ family: "Inter", style: st });
const byName2 = Object.fromEntries(figma.variables.getLocalVariables().map(v => [v.name, v]));
function bind(ts, field, varName){ const v = byName2[varName]; if(!v) return; try{ ts.setBoundVariable(field, v);}catch(e){ try{ts.setBoundVariable(field, v.id);}catch(_){}}}

// [name, weight, sizePx, sizeToken, lineHeight, trackingPct, upper]
const specs = [
  ["Headline/Jumbo","Regular",72,"text-7xl",100,-2,false],
  ["Headline/XL","Regular",48,"text-5xl",110,-2,false],
  ["Headline/LG","Regular",36,"text-4xl",110,-1,false],
  ["Headline/MD","Regular",24,"text-2xl",120,-1,false],
  ["Headline/SM","Medium",20,"text-xl",120,0,false],
  ["Body/LG","Regular",20,"text-xl",130,0,false],
  ["Body/Base","Regular",16,"text-base",130,0,false],
  ["Body/MD","Regular",14,"text-sm",130,0,false],
  ["Body/SM","Regular",12,"text-xs",130,0,false],
  ["Utility/Eyebrow","Medium",14,"text-sm",130,6,true],
  ["Utility/Caption","Regular",12,"text-xs",130,0,false],
];
for (const [name, weight, size, sizeTok, lh, tr, upper] of specs) {
  const ts = figma.createTextStyle();
  ts.name = name;
  ts.fontName = { family: "Inter", style: weight };
  ts.fontSize = size;
  ts.lineHeight = { value: lh, unit: "PERCENT" };
  ts.letterSpacing = { value: tr, unit: "PERCENT" };
  if (upper) ts.textCase = "UPPER";
  ts.hangingPunctuation = true;
  bind(ts, "fontSize", "font-size/" + sizeTok);
  bind(ts, "fontFamily", "font-family/primary");
  bind(ts, "fontStyle", "font-weight/" + weight.toLowerCase().replace(" ", ""));
}
```

The private `.Docs/*` chrome styles used by the specimen pages are unchanged — copy that recipe straight from `figma-build.md`.

---

## Opt-in: chart & sidebar tokens

Only run if selected in the Step 3 scoped intake.

```js
// Chart — single mode, five hues
function colorVar(name, hex, collection, mode) { // reuse from figma-build.md if already defined
  const v = figma.variables.createVariable(name, collection, "COLOR");
  v.setValueForMode(mode, hexToRgb(hex));
  return v;
}
colorVar("color/chart/1", "#1A73E8", color, colorMode);
colorVar("color/chart/2", "#1E8E3E", color, colorMode);
colorVar("color/chart/3", "#F9AB00", color, colorMode);
colorVar("color/chart/4", "#9334E6", color, colorMode);
colorVar("color/chart/5", "#FF5C39", color, colorMode);

// Sidebar — same conditional-dark-mode pattern as the rest of Semantic
semanticColor("sidebar/background", "color/neutral/White", "color/neutral/Grey-80");
semanticColor("sidebar/foreground", "color/neutral/Black", "color/neutral/White");
semanticColor("sidebar/primary", "color/primary/brand-primary");
semanticColor("sidebar/primary-foreground", "color/neutral/White");
semanticColor("sidebar/accent", "color/primary/accent");
semanticColor("sidebar/accent-foreground", "color/neutral/White");
semanticColor("sidebar/border", "color/neutral/Grey-20", "color/neutral/Grey-60");
semanticColor("sidebar/ring", "color/primary/brand-primary");
```
