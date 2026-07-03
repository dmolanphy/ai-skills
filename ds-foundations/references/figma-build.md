# Figma Build Recipes

Plugin-API (`figma.*`) snippets to run through the `use_figma` tool. **Read the Figma plugin's `/figma-use` skill first** — it's mandatory before calling `use_figma` and explains how code is executed and returned.

Build in small batches and read back what you created so you can catch failures early, rather than firing one giant script.

## Table of contents
- Inspect the file & detect the Cover
- Create the Cover page (FEI/GEHC style)
- Helpers (hex→rgb)
- Create collections & modes
- Create primitive variables (FLOAT / STRING / COLOR)
- Create semantic variables (aliases, multi-mode)
- Create grid styles
- Create text styles (with variable binding)
- Fonts not installed locally

---

## Inspect the file & detect the Cover

Run this first. Never create or modify a Cover if one exists.

```js
const pages = figma.root.children.map(p => p.name);
const hasCover = figma.root.children.some(
  p => /cover/i.test(p.name) || p.name.includes("📕")
);
return { pages, hasCover };
```

If `hasCover` is true, leave it untouched and proceed to tokens. If false, ask the user for the cover **title**, then build one with the recipe below.

---

## Create the Cover page (FEI/GEHC style)

Only run this when there is **no** existing cover and you've gotten the title from the user. The look mirrors the FEI and GEHC files: a 1920×1080 black frame, the **Huge logo top-left**, and the title set very large in the primary font, light weight, white, anchored lower-left.

**The Huge logo is mandatory on every cover this skill creates.** It's bundled at `assets/huge-logo.png` (100×100, square corners, Huge pink `#ff0090`), with a ready-to-use base64 copy at `assets/huge-logo-base64.txt`. Before running this recipe, **read `assets/huge-logo-base64.txt` and substitute its contents** for `HUGE_LOGO_B64` in the code below. Do not resize the logo, round its corners, or swap it for a placeholder — place the PNG exactly as bundled at 100×100, top-left at x=53, y=42.

```js
async function buildCover(title, primaryFamily, logoB64) {
  const page = figma.createPage();
  page.name = "📕 Cover";

  const frame = figma.createFrame();
  frame.name = "Cover";
  frame.resize(1920, 1080);
  frame.x = 0; frame.y = 0;
  frame.fills = [{ type: "SOLID", color: { r: 0, g: 0, b: 0 } }]; // black
  page.appendChild(frame);

  // Huge logo — exact bundled PNG, 100×100, square corners, top-left. ALWAYS present.
  const bytes = figma.base64Decode(logoB64); // Figma plugin API decodes base64 → Uint8Array
  const image = figma.createImage(bytes);
  const logo = figma.createRectangle();
  logo.name = "Huge Logo";
  logo.resize(100, 100);
  logo.x = 53; logo.y = 42;
  logo.cornerRadius = 0; // square corners — do not round
  logo.fills = [{ type: "IMAGE", scaleMode: "FILL", imageHash: image.hash }];
  frame.appendChild(logo);

  // Title — large, light, white, lower-left. Fall back to Inter if the light weight isn't available.
  let family = primaryFamily, style = "Light";
  try { await figma.loadFontAsync({ family, style }); }
  catch (e) {
    try { await figma.loadFontAsync({ family, style: "Regular" }); style = "Regular"; }
    catch (_) { family = "Inter"; style = "Light"; await figma.loadFontAsync({ family, style }); }
  }
  const t = figma.createText();
  t.fontName = { family, style };
  t.characters = title;
  t.fontSize = 200;
  t.lineHeight = { value: 100, unit: "PERCENT" };
  t.letterSpacing = { value: -3, unit: "PERCENT" };
  t.fills = [{ type: "SOLID", color: { r: 1, g: 1, b: 1 } }]; // white
  t.textAutoResize = "HEIGHT";
  t.resize(1760, t.height);
  t.x = 40;
  t.y = 1008 - t.height; // sit ~72px above the bottom edge
  frame.appendChild(t);

  return { page: page.name, title };
}
// HUGE_LOGO_B64 below is the full contents of assets/huge-logo-base64.txt
// await buildCover("Design System: Foundations", "Inter", "HUGE_LOGO_B64");
```

Notes: if `figma.base64Decode` is unavailable on an older plugin version, decode manually into a `Uint8Array` before `createImage`. If the title is long enough to overflow at 200px, step the `fontSize` down (e.g. 160 / 120) until it fits the frame width. The logo itself never changes.

---

## Helpers

Figma colors are 0–1 RGB(A), not hex. Convert:

```js
function hexToRgb(hex) {
  const h = hex.replace('#', '');
  const n = h.length === 3 ? h.split('').map(c => c + c).join('') : h;
  return {
    r: parseInt(n.slice(0, 2), 16) / 255,
    g: parseInt(n.slice(2, 4), 16) / 255,
    b: parseInt(n.slice(4, 6), 16) / 255,
  };
}
```

---

## Create collections & modes

Four collections. **Create them in this order** — panel order follows creation order: Typography → Color → Spacing → Semantic. Typography and Spacing each have two modes (Desktop/Mobile); Color and Semantic are single mode. Semantic must come after Color since it aliases Color. Do not add Light/Dark color modes here.

```js
// 1. Typography — Desktop + Mobile modes
const typo = figma.variables.createVariableCollection("Typography");
const dMode = typo.modes[0].modeId; typo.renameMode(dMode, "Desktop");
const mMode = typo.addMode("Mobile");

// 2. Color — single mode
const color = figma.variables.createVariableCollection("Color");
color.renameMode(color.modes[0].modeId, "Value");
const colorMode = color.modes[0].modeId;

// 3. Spacing — Desktop + Mobile modes (spacing differs; radius identical)
const spacing = figma.variables.createVariableCollection("Spacing");
const sdMode = spacing.modes[0].modeId; spacing.renameMode(sdMode, "Desktop");
const smMode = spacing.addMode("Mobile");

// 4. Semantic — single mode (aliases → Color)
const sem = figma.variables.createVariableCollection("Semantic");
const semMode = sem.modes[0].modeId; // no addMode
```

(Color modes like Light/Dark are added later, once the system matures — not in this baseline.)

---

## Create primitive variables

The variable **name** carries the group via slashes. Resolved type is `"FLOAT"`, `"STRING"`, `"COLOR"`, or `"BOOLEAN"`.

### Typography variables (Desktop/Mobile)

`font-family` and `font-weight` get the **same value in both modes**; `font-size` differs per mode. **Set `scopes` on every variable** (see the scoping table in token-architecture.md) so each token only appears in the right property dropdowns.

```js
// STRING (family/weight) — same value in both modes, with scopes
function typoStr(name, value, scopes) {
  const v = figma.variables.createVariable(name, typo, "STRING");
  v.setValueForMode(dMode, value);
  v.setValueForMode(mMode, value);
  v.scopes = scopes;
  return v;
}
// FLOAT font-size — distinct Desktop/Mobile values
function fontSizeVar(name, desktop, mobile) {
  const v = figma.variables.createVariable(name, typo, "FLOAT");
  v.setValueForMode(dMode, desktop);
  v.setValueForMode(mMode, mobile);
  v.scopes = ["FONT_SIZE", "LINE_HEIGHT", "PARAGRAPH_SPACING"];
  return v;
}

typoStr("font-family/primary", "Inter", ["FONT_FAMILY"]);
typoStr("font-weight/light", "Light", ["FONT_STYLE"]);
fontSizeVar("font-size/jumbo",   72, 52);
fontSizeVar("font-size/xxlarge", 48, 32);
fontSizeVar("font-size/xlarge",  32, 24);
fontSizeVar("font-size/large",   24, 20);
fontSizeVar("font-size/medium",  20, 16);
fontSizeVar("font-size/base",    16, 16);
fontSizeVar("font-size/small",   14, 14);
fontSizeVar("font-size/xsmall",  12, 12);
```

### Spacing variables (Desktop/Mobile)

`spacing/*` differs per mode (Mobile = next step down) and is scoped to width/height + gap; `radius/*` is the same in both modes and scoped to corner radius.

```js
// spacing — distinct Desktop/Mobile values, scoped to sizing + gap
function spaceVar(name, desktop, mobile) {
  const v = figma.variables.createVariable(name, spacing, "FLOAT");
  v.setValueForMode(sdMode, desktop);
  v.setValueForMode(smMode, mobile);
  v.scopes = ["WIDTH_HEIGHT", "GAP"];
  return v;
}
// radius — identical in both modes, scoped to corner radius
function radiusVar(name, value) {
  const v = figma.variables.createVariable(name, spacing, "FLOAT");
  v.setValueForMode(sdMode, value);
  v.setValueForMode(smMode, value);
  v.scopes = ["CORNER_RADIUS"];
  return v;
}

spaceVar("spacing/space-120", 120, 80);
spaceVar("spacing/space-80",   80, 64);
spaceVar("spacing/space-64",   64, 48);
spaceVar("spacing/space-48",   48, 32);
spaceVar("spacing/space-32",   32, 24);
spaceVar("spacing/space-24",   24, 16);
spaceVar("spacing/space-16",   16, 12);
spaceVar("spacing/space-12",   12, 8);
spaceVar("spacing/space-8",     8, 8);
spaceVar("spacing/space-4",     4, 4);
spaceVar("spacing/space-none",  0, 0);

radiusVar("radius/none", 0);
radiusVar("radius/small", 4);
radiusVar("radius/base", 8);
radiusVar("radius/full", 999);
```

### Color variables (single mode)

```js
function colorVar(name, hex) {
  const v = figma.variables.createVariable(name, color, "COLOR");
  v.setValueForMode(colorMode, hexToRgb(hex));
  return v;
}

colorVar("color/primary/brand-primary", "#2D6CDF");
colorVar("color/secondary/secondary-1", "#1A73E8");
colorVar("color/neutral/White", "#FFFFFF");
colorVar("color/neutral/Black", "#000000");
```

Keep references to primitive variables you'll alias from semantics. If you build in separate `use_figma` calls, re-fetch them by name:

```js
const all = figma.variables.getLocalVariables();
const byName = Object.fromEntries(all.map(v => [v.name, v]));
const black = byName["color/neutral/Black"];
```

---

## Create semantic variables (aliases, single mode)

Semantic variables hold an **alias** to a color primitive. Single mode — one value each. Scope them by group: `text/*` → Text fill, `surface/*` → Frame + Shape fill, `border/*` → Stroke. Use the full alias map in token-architecture.md.

```js
// scope is derived from the group prefix
function scopeFor(name) {
  if (name.startsWith("text/"))    return ["TEXT_FILL"];
  if (name.startsWith("surface/")) return ["FRAME_FILL", "SHAPE_FILL"];
  if (name.startsWith("border/"))  return ["STROKE_COLOR"];
  return ["ALL_SCOPES"];
}
function semanticColor(name, primitiveName) {
  const v = figma.variables.createVariable(name, sem, "COLOR");
  v.setValueForMode(semMode, figma.variables.createVariableAlias(byName[primitiveName]));
  v.scopes = scopeFor(name);
  return v;
}

semanticColor("text/primary",    "color/neutral/Black");      // → Text fill
semanticColor("surface/primary", "color/neutral/White");      // → Frame + Shape fill
semanticColor("border/default",  "color/neutral/Grey-20");    // → Stroke
```

---

## Create grid styles

```js
function gridStyle(name, count, margin, gutter) {
  const g = figma.createGridStyle();
  g.name = name;
  g.layoutGrids = [{
    pattern: "COLUMNS",
    alignment: "STRETCH",
    gutterSize: gutter,
    count: count,
    offset: margin,       // side margins
  }];
  return g;
}
gridStyle("Grid/Desktop", 12, 64, 24);
gridStyle("Grid/Tablet",  8,  32, 24);
gridStyle("Grid/Mobile",  4,  16, 16);
```

---

## Create text styles (with variable binding)

Build from the text-style table in token-architecture.md. **Every style gets hanging punctuation ON; line heights are limited to 100/110/120/130; the Eyebrow style is uppercase + 6% tracking.** Bind family/size/weight to variables (headlines → `font-family/primary`; body & utility → `font-family/secondary`).

```js
for (const st of ["Light","Regular","Medium"]) await figma.loadFontAsync({ family: "Inter", style: st });
const byName = Object.fromEntries(figma.variables.getLocalVariables().map(v => [v.name, v]));
const weightTok = { Light:"font-weight/light", Regular:"font-weight/regular", Medium:"font-weight/medium" };
function bind(ts, field, varName){ const v = byName[varName]; if(!v) return; try{ ts.setBoundVariable(field, v);}catch(e){ try{ts.setBoundVariable(field, v.id);}catch(_){}}}

// [name, weight, sizePx, sizeToken, lineHeight, trackingPct, familyToken, upper]
const specs = [
  ["Headline/Jumbo","Light",72,"jumbo",100,-2,"primary",false],
  ["Headline/XL","Regular",48,"xxlarge",110,-2,"primary",false],
  ["Headline/LG","Regular",32,"xlarge",110,-1,"primary",false],
  ["Headline/MD","Regular",24,"large",120,-1,"primary",false],
  ["Headline/SM","Medium",20,"medium",120,0,"primary",false],
  ["Body/LG","Regular",20,"medium",130,0,"secondary",false],
  ["Body/Base","Regular",16,"base",130,0,"secondary",false],
  ["Body/MD","Regular",14,"small",130,0,"secondary",false],
  ["Body/SM","Regular",12,"xsmall",130,0,"secondary",false],
  ["Utility/Eyebrow","Medium",14,"small",130,6,"secondary",true],
  ["Utility/Caption","Regular",12,"xsmall",130,0,"secondary",false],
];
for (const [name, weight, size, sizeTok, lh, tr, fam, upper] of specs) {
  const ts = figma.createTextStyle();
  ts.name = name;
  ts.fontName = { family: "Inter", style: weight };
  ts.fontSize = size;
  ts.lineHeight = { value: lh, unit: "PERCENT" };
  ts.letterSpacing = { value: tr, unit: "PERCENT" };
  if (upper) ts.textCase = "UPPER";
  ts.hangingPunctuation = true;          // ON for every style
  bind(ts, "fontSize", "font-size/" + sizeTok);
  bind(ts, "fontFamily", "font-family/" + fam);
  bind(ts, "fontStyle", weightTok[weight]);
}
```

Bindable text-style fields: `fontFamily`, `fontStyle`, `fontSize`, `lineHeight`, `letterSpacing`, `paragraphSpacing`, `paragraphIndent`. `hangingPunctuation` and `textCase` are plain style properties (not variable-bindable). If binding throws on this Figma version, the literal values still produce a correct style — just tell the user the styles aren't variable-bound.

---

## Internal `.Docs/*` text styles (private chrome)

The specimen pages need their own text styles for **chrome** — page/column headers and the spec-table text — that are *not* part of the published design system. Create them once, **named with a leading period** (`.Docs/…`). The leading `.` is Figma's convention for private assets: they stay usable in the file but are excluded from the asset panel and library publishing. (`hiddenFromPublishing` is **not** settable on a TextStyle — it throws "object is not extensible" — so the period prefix is the reliable mechanism; set it in a `try/catch` only as a best-effort extra.)

Binding their `fontFamily` to the family variables means they still update globally if the brand font changes.

```js
const byName = Object.fromEntries(figma.variables.getLocalVariables().map(v => [v.name, v]));
const bindFam = (ts, fam) => { const v = byName["font-family/" + fam]; if(!v) return; try{ ts.setBoundVariable("fontFamily", v);}catch(e){ try{ts.setBoundVariable("fontFamily", v.id);}catch(_){}}};
for (const st of ["Regular","Medium"]) await figma.loadFontAsync({ family:"Inter", style:st });

// [name, weight, sizePx, lineHeight%, familyToken]
const docStyles = [
  [".Docs/Header",      "Medium", 32, 120, "primary"],    // page title + column headers
  [".Docs/Spec Name",   "Medium", 16, 130, "secondary"],  // each style's name in the spec block
  [".Docs/Spec Detail", "Regular",14, 130, "secondary"],  // spec labels + values, grid labels, color name/hex
];
for (const [name, weight, size, lh, fam] of docStyles) {
  const ts = figma.createTextStyle();
  ts.name = name; ts.fontName = { family:"Inter", style:weight }; ts.fontSize = size;
  ts.lineHeight = { value: lh, unit:"PERCENT" }; ts.letterSpacing = { value: 0, unit:"PERCENT" };
  try { ts.hangingPunctuation = true; } catch(e){}
  try { ts.hiddenFromPublishing = true; } catch(e){}   // best-effort; the "." prefix is what actually hides it
  bindFam(ts, fam);
}
```

The specimen pages apply these via their style names (see `specimen-pages.md`).

---

## Fonts not installed locally

Some brand or licensed fonts aren't installed locally and so aren't available to the plugin API. When that happens, substitute the closest available font, build everything with the stand-in, and drop an **off-canvas note frame** listing the intended font and the swap so the user sees it on open.

```js
const note = figma.createText();
await figma.loadFontAsync({ family: "Inter", style: "Regular" });
note.fontName = { family: "Inter", style: "Regular" };
note.characters =
  "FONT NOTE\n[Intended font] not available to the plugin — used [stand-in].\nSwap in Figma once the licensed font is installed.";
note.x = 2200; note.y = 0; // off to the side of any artboards
```

Confirm available families with `figma.listAvailableFontsAsync()` if unsure before loading.
