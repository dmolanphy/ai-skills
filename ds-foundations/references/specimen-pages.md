# Specimen Pages (Typography, Color, Grid)

After the variables, text styles, and grid styles exist, build three specimen pages that document them — modeled on the user's FEI foundations file. Run each recipe through `use_figma`. **Run these only after the tokens/styles are created**, since they reference local variables and styles by name.

Pages are named `→ Typography`, `→ Color`, `→ Grid`. Everything that can be bound is bound: page titles use a text style + the on-brand color token, type specimens use the local text styles, section labels use the Eyebrow style, color swatches bind their fill to the color variable, grid frames bind to the grid styles, and divider/border lines bind to border tokens.

## Shared layout constants (from FEI)
- Spec frame width **2827**, white fill. Left/right margin **120** (content spans 120 → 2707).
- **Header bar:** full-width rect `0,0,2827,181`, fill bound to `color/primary/brand-secondary`; page title at `x=120, y=70`, **bound to the `.Docs/Header` text style** (the private chrome style — see below), fill bound to **`text/on-brand`** (white on the brand bar).

> **Prereq:** create the private `.Docs/*` text styles first (see `figma-build.md` → "Internal `.Docs/*` text styles"). All spec-page chrome — page titles, column headers, spec name, spec details, grid labels, color name/hex — binds to those, so updating one `.Docs` style restyles every page. They're period-prefixed so they never publish to the shared library.
- **Section title:** a **real 1px line** (`figma.createLine()`, not a filled rectangle) at `x=120`, length `2587`, stroke bound to **`border/strong`**; plus an uppercase label bound to the **`Utility/Eyebrow`** text style at `x=120, y+12`, fill `text/tertiary`.

Shared helpers (define once per recipe):
```js
async function loadInter(){ for (const s of ["Light","Regular","Medium"]) await figma.loadFontAsync({ family:"Inter", style:s }); }
const byVar = Object.fromEntries(figma.variables.getLocalVariables().map(v => [v.name, v]));
const styleByName = Object.fromEntries(figma.getLocalTextStyles().map(s => [s.name, s]));
function paintVar(varName, fallback){ let p={type:"SOLID",color:fallback||{r:0,g:0,b:0}}; const v=byVar[varName]; if(v){ try{p=figma.variables.setBoundVariableForPaint(p,"color",v);}catch(e){} } return p; }
async function applyStyle(t, name){ const s=styleByName[name]; if(!s) return; try{ await t.setTextStyleIdAsync(s.id);}catch(e){ try{t.textStyleId=s.id;}catch(_){}}}
function rgbToHex(c){ const f=x=>Math.round(x*255).toString(16).padStart(2,"0"); return "#"+f(c.r)+f(c.g)+f(c.b); }
function freshPage(name){ for (const p of [...figma.root.children]){ if(p.name===name && figma.currentPage!==p){ try{p.remove();}catch(e){} } } const pg=figma.createPage(); pg.name=name; return pg; }

async function header(frame, label){
  const bar=figma.createRectangle(); bar.resize(2827,181); bar.fills=[paintVar("color/primary/brand-secondary",{r:0.1,g:0.23,b:0.42})]; frame.appendChild(bar);
  const t=figma.createText(); t.fontName={family:"Inter",style:"Regular"}; t.characters=label; await applyStyle(t,".Docs/Header"); t.fills=[paintVar("text/on-brand",{r:1,g:1,b:1})]; t.x=120; t.y=70; frame.appendChild(t);
}
async function section(frame, label, y){
  const line=figma.createLine(); line.resize(2587,0); line.x=120; line.y=y; line.strokes=[paintVar("border/strong",{r:0.65,g:0.66,b:0.69})]; line.strokeWeight=1; frame.appendChild(line);
  const lab=figma.createText(); lab.fontName={family:"Inter",style:"Medium"}; lab.characters=label; await applyStyle(lab,"Utility/Eyebrow"); lab.fills=[paintVar("text/tertiary",{r:0.36,g:0.38,b:0.42})]; lab.x=120; lab.y=y+12; frame.appendChild(lab);
}
```
Note: a line node carries the divider via **strokes** (not fills) — that's the "real line, not a rectangle" requirement. Load fonts before applying styles (`setTextStyleIdAsync` needs the style's font available).

---

## Typography page

**Column / spec-table layout** (modeled on the Penske design-system spec page). One **column per text-style group** (`Headline`, `Body`, `Utility`), laid side by side in a horizontal auto-layout. Each column has a top-rule header with the group name, then one **entry per style**. Each entry is a horizontal auto-layout row with a **top-border divider** (`border/strong`), containing:
- a fixed **325px spec block**: the style's leaf **name** on top, then a two-column attribute table (labels `text/secondary` + values `text/primary`) reading **font-family, font-weight, font-size, line-height, letter-spacing, paragraph-spacing, text-transform** straight off the live text style;
- a flexible **specimen** ("Lorem ipsum…") set in the actual text style (`layoutGrow=1`).

The page is wider than the others (3700) to fit the columns. The navy header bar is kept for cross-page consistency (no logo). Chrome binds to the `.Docs/*` styles. Each **column header has a 4px top rule**; each **entry has a 1px top divider**. Auto-layout means heights are automatic. Data-driven off `getLocalTextStyles()`, so it always reflects the real styles.

```js
await loadInter();
const W = 3700;
const styles = figma.getLocalTextStyles().filter(s => !s.name.startsWith(".Docs/"));  // DS styles only in the columns
function topBorder(f, wt){ f.strokes=[paintVar("border/strong",{r:0.65,g:0.66,b:0.69})]; f.strokeAlign="INSIDE"; f.strokeTopWeight=wt; f.strokeBottomWeight=0; f.strokeLeftWeight=0; f.strokeRightWeight=0; }
async function styledTxt(styleName, fill, chars){ const t=figma.createText(); t.fontName={family:"Inter",style:"Regular"}; t.characters=chars; await applyStyle(t, styleName); t.fills=[fill]; return t; }
const fmtLH=lh=> lh.unit==="PERCENT"?Math.round(lh.value)+"%":(lh.unit==="AUTO"?"auto":Math.round(lh.value)+"px");
const fmtLS=ls=> (Math.round(ls.value*10)/10)+(ls.unit==="PERCENT"?"%":"px");
const SAMPLE="Lorem ipsum dolor sit amet consectetur adipiscing elit";
// Body specimens use a longer multi-sentence sample with a paragraph break (\n\n) so line-height + paragraph rhythm are legible.
const BODY_SAMPLE="Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.";
const LABELS=["font-family","font-weight","font-size","line-height","letter-spacing","paragraph-spacing","text-transform"];

const page = freshPage("→ Typography");
const frame = figma.createFrame(); frame.name="Typography"; frame.resize(W,1200); frame.fills=[{type:"SOLID",color:{r:1,g:1,b:1}}]; page.appendChild(frame);
await header(frame, "Typography");  // page title → .Docs/Header

const rowF=figma.createFrame(); rowF.name="Columns"; rowF.x=120; rowF.y=300; rowF.fills=[]; rowF.layoutMode="HORIZONTAL"; rowF.itemSpacing=80; rowF.primaryAxisSizingMode="AUTO"; rowF.counterAxisSizingMode="AUTO"; rowF.counterAxisAlignItems="MIN"; frame.appendChild(rowF);

const groups={}; for(const s of styles){ const g=s.name.split("/")[0]; (groups[g]=groups[g]||[]).push(s); }
const colOrder=["Headline","Body","Utility"].filter(g=>groups[g]);  // skips "Mono" if present unless you add it

for(const colName of colOrder){
  const col=figma.createFrame(); col.name=colName; col.fills=[]; col.layoutMode="VERTICAL"; col.itemSpacing=0; col.primaryAxisSizingMode="AUTO"; col.counterAxisSizingMode="FIXED"; rowF.appendChild(col); col.resize(1100,100);
  const hdr=figma.createFrame(); hdr.name="header"; hdr.fills=[]; hdr.layoutMode="VERTICAL"; hdr.primaryAxisSizingMode="AUTO"; hdr.counterAxisSizingMode="FIXED"; hdr.paddingTop=40; hdr.paddingBottom=40; col.appendChild(hdr); hdr.resize(1100,80); topBorder(hdr, 4);   // 4px header rule
  hdr.appendChild(await styledTxt(".Docs/Header", paintVar("text/primary",{r:0,g:0,b:0}), colName));
  for(const s of groups[colName]){
    const leaf=s.name.split("/").pop();
    const vals=[s.fontName.family, s.fontName.style, Math.round(s.fontSize)+"px", fmtLH(s.lineHeight), fmtLS(s.letterSpacing), (s.paragraphSpacing||0)+"px", (s.textCase==="UPPER"?"uppercase":"none")];
    const entry=figma.createFrame(); entry.name=leaf; entry.fills=[]; entry.layoutMode="HORIZONTAL"; entry.itemSpacing=40; entry.primaryAxisSizingMode="FIXED"; entry.counterAxisSizingMode="AUTO"; entry.paddingTop=40; entry.paddingBottom=40; col.appendChild(entry); entry.resize(1100,100); topBorder(entry, 1);   // 1px entry divider
    const specs=figma.createFrame(); specs.name="specs"; specs.fills=[]; specs.layoutMode="VERTICAL"; specs.itemSpacing=24; specs.primaryAxisSizingMode="AUTO"; specs.counterAxisSizingMode="FIXED"; entry.appendChild(specs); specs.resize(325,100); specs.layoutGrow=0;
    specs.appendChild(await styledTxt(".Docs/Spec Name", paintVar("text/primary",{r:0,g:0,b:0}), leaf));
    const attrs=figma.createFrame(); attrs.fills=[]; attrs.layoutMode="HORIZONTAL"; attrs.itemSpacing=40; attrs.primaryAxisSizingMode="AUTO"; attrs.counterAxisSizingMode="AUTO"; specs.appendChild(attrs);
    const labs=figma.createFrame(); labs.fills=[]; labs.layoutMode="VERTICAL"; labs.itemSpacing=8; labs.primaryAxisSizingMode="AUTO"; labs.counterAxisSizingMode="AUTO"; attrs.appendChild(labs);
    const valsF=figma.createFrame(); valsF.fills=[]; valsF.layoutMode="VERTICAL"; valsF.itemSpacing=8; valsF.primaryAxisSizingMode="AUTO"; valsF.counterAxisSizingMode="AUTO"; attrs.appendChild(valsF);
    for(let i=0;i<LABELS.length;i++){ labs.appendChild(await styledTxt(".Docs/Spec Detail", paintVar("text/secondary",{r:0.4,g:0.42,b:0.46}), LABELS[i])); valsF.appendChild(await styledTxt(".Docs/Spec Detail", paintVar("text/primary",{r:0,g:0,b:0}), vals[i])); }
    const sampleText = (colName==="Body") ? BODY_SAMPLE : SAMPLE;   // Body gets the longer, multi-paragraph copy
    const sample=figma.createText(); sample.fontName={family:"Inter",style:"Regular"}; sample.characters=sampleText; await applyStyle(sample,s.name); sample.fills=[paintVar("text/primary",{r:0,g:0,b:0})]; sample.textAutoResize="HEIGHT"; entry.appendChild(sample); sample.layoutGrow=1;
  }
}
frame.resize(W, Math.round(rowF.y + rowF.height + 120));
```

---

## Color page

Swatches **331×331, square corners (cornerRadius 0)**, in a 7-column grid (`x = 120 + col*365`). Each swatch fill is **bound** to its color variable; below it, the **name** (leaf variable name, bound to `.Docs/Spec Name`) and the **hex** (read from the variable's own value, bound to `.Docs/Spec Detail`). Very light swatches get a `Grey-20` stroke. One section per color group.

```js
await loadInter();
const page = freshPage("→ Color");
const frame = figma.createFrame(); frame.name="Color"; frame.resize(2827,2950); frame.fills=[{type:"SOLID",color:{r:1,g:1,b:1}}]; page.appendChild(frame);
await header(frame, "Color");

async function swatch(col, sy, varName){
  const v=byVar[varName]; if(!v) return;
  const val=v.valuesByMode[Object.keys(v.valuesByMode)[0]]; const leaf=varName.split("/").pop(); const x=120+col*365;
  const r=figma.createRectangle(); r.resize(331,331); r.x=x; r.y=sy; r.cornerRadius=0; r.fills=[paintVar(varName)];
  if((val.r+val.g+val.b)/3>0.92){ r.strokes=[paintVar("color/neutral/Grey-20",{r:0.89,g:0.89,b:0.9})]; r.strokeWeight=1; }
  frame.appendChild(r);
  const nm=figma.createText(); nm.fontName={family:"Inter",style:"Regular"}; nm.characters=leaf; await applyStyle(nm,".Docs/Spec Name"); nm.fills=[paintVar("text/primary",{r:0,g:0,b:0})]; nm.x=x; nm.y=sy+349; frame.appendChild(nm);
  const hx=figma.createText(); hx.fontName={family:"Inter",style:"Regular"}; hx.characters=rgbToHex(val).toUpperCase(); await applyStyle(hx,".Docs/Spec Detail"); hx.fills=[paintVar("text/tertiary",{r:0.36,g:0.38,b:0.42})]; hx.x=x; hx.y=sy+375; frame.appendChild(hx);
}
const groups=[
  ["PRIMARY",315,410,["color/primary/brand-primary","color/primary/brand-secondary","color/primary/accent"]],
  ["SECONDARY",970,1065,["color/secondary/secondary-1","color/secondary/secondary-2","color/secondary/secondary-3","color/secondary/secondary-4","color/secondary/secondary-5"]],
  ["NEUTRAL",1625,1720,["color/neutral/White","color/neutral/Grey-10","color/neutral/Grey-20","color/neutral/Grey-40","color/neutral/Grey-60","color/neutral/Grey-80","color/neutral/Black"]],
  ["UTILITY",2280,2375,["color/utility/success","color/utility/warning","color/utility/error"]],
];
for (const [label,secY,swY,names] of groups){ await section(frame,label,secY); for(let i=0;i<names.length;i++) await swatch(i,swY,names[i]); }
```

---

## Grid page

Three device frames side by side, each white, **bound to the matching grid style** (`Grid/Desktop`, `Grid/Tablet`, `Grid/Mobile`). The label is bound to `.Docs/Spec Detail`. The light-blue column overlays live inside an **auto-layout frame** (horizontal, `itemSpacing = gutter`) with a **1px border** (`border/default`) around it — mirroring FEI's bordered column container. Columns stretch to fill the container height via `layoutAlign = "STRETCH"`.

```js
for (const s of ["Regular","Medium"]) await figma.loadFontAsync({family:"Inter",style:s});
const gridByName = Object.fromEntries(figma.getLocalGridStyles().map(s => [s.name, s]));
const page = freshPage("→ Grid");
const COL = {r:0.862,g:0.894,b:1};

async function device(label, gridStyleName, x, W, H, count, margin, gutter){
  const f=figma.createFrame(); f.name=label; f.resize(W,H); f.x=x; f.y=0; f.fills=[{type:"SOLID",color:{r:1,g:1,b:1}}]; f.clipsContent=true; page.appendChild(f);
  const gs=gridByName[gridStyleName]; if(gs){ try{await f.setGridStyleIdAsync(gs.id);}catch(e){ try{f.gridStyleId=gs.id;}catch(_){}} }
  const t=figma.createText(); t.fontName={family:"Inter",style:"Regular"}; t.characters=label; await applyStyle(t,".Docs/Spec Detail"); t.fills=[paintVar("text/tertiary",{r:0.36,g:0.38,b:0.42})]; t.x=margin; t.y=40; f.appendChild(t);
  const top=99, bottom=64, inner=W-2*margin, h=H-top-bottom, colW=(inner-(count-1)*gutter)/count;
  const cont=figma.createFrame(); cont.name="Columns"; cont.x=margin; cont.y=top;
  cont.layoutMode="HORIZONTAL"; cont.itemSpacing=gutter; cont.paddingLeft=0; cont.paddingRight=0; cont.paddingTop=0; cont.paddingBottom=0;
  cont.primaryAxisSizingMode="FIXED"; cont.counterAxisSizingMode="FIXED";
  cont.fills=[]; cont.strokes=[paintVar("border/default",{r:0.89,g:0.89,b:0.9})]; cont.strokeWeight=1; cont.strokeAlign="INSIDE";
  f.appendChild(cont); cont.resize(inner,h);
  for (let i=0;i<count;i++){ const r=figma.createRectangle(); r.resize(colW,h); r.fills=[{type:"SOLID",color:COL}]; cont.appendChild(r); r.layoutAlign="STRETCH"; r.layoutGrow=0; }
}
await device("Desktop · 1440 · 12 col","Grid/Desktop",0,    1440,1024,12,64,24);
await device("Tablet · 1024 · 8 col",  "Grid/Tablet", 1495, 1024,1024, 8,32,24);
await device("Mobile · 440 · 4 col",   "Grid/Mobile", 2574, 440, 956,  4,16,16);
```

Match the device frames and margins/gutters to whatever the project's grid styles actually are. If the project defines a 1920 desktop too, add a fourth frame (FEI includes a `DesktopXL-1920`).
