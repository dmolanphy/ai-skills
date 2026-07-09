---
name: image-prompt-engineer
description: >
  Craft precise, layered prompts for AI image generation (Midjourney, DALL-E, Stable
  Diffusion, Flux, Firefly). Use this skill whenever the task involves generating
  reference imagery, moodboard fills, concept visuals, style tiles, or any AI-generated
  photography or illustration — including requests like "generate an image of",
  "I need visuals for this concept", "make reference shots for the moodboard", or
  "write me a Midjourney prompt". Trigger even when the user just describes a visual
  idea they want to see — translating vague visual intent into precise prompt language
  is exactly what this skill does.
---

# Image Prompt Engineer

Translate visual intent into prompt language that actually renders. Vague prompts make
generic images; layered, photographically literal prompts make usable ones. Write
prompts the way a photographer briefs a shoot.

## The layered prompt structure

Build every prompt through these layers, in order. Skip layers only deliberately.

1. **Subject** — main focus with concrete attributes: materials, texture, expression,
   pose, scale. Specific nouns beat adjectives ("weathered brass compass" not "old
   object").
2. **Environment** — location type, time of day, weather/atmosphere, background
   treatment (sharp / blurred / minimal / contextual).
3. **Lighting** — source (golden hour, overcast, softbox, neon), direction (side, rim,
   Rembrandt, butterfly), quality (hard/soft, diffused, volumetric), color temperature.
   Lighting is the layer that most separates professional-looking output from slop.
4. **Camera** — perspective (eye level, low angle, bird's eye), focal length effect
   (wide distortion, telephoto compression), depth of field ("shallow depth of field,
   f/1.8 bokeh" — never "blurry background"), exposure style (high key, low key,
   silhouette).
5. **Style** — genre (editorial, documentary, commercial, fine art), era, post-
   processing (film emulation: Portra, Velvia, Cinestill 800T; grain; color grade),
   reference photographers where useful.

Keep the physics honest: lighting direction must match shadow descriptions; effects
should be plausible in real photography. Models render coherent scenes better when the
prompt describes a photographable one.

## Working rules

- Use real photography vocabulary — models are trained on captioned photography and
  respond to its terminology.
- Add negative prompts where the platform supports them (unwanted elements, text
  artifacts, extra fingers).
- Always set aspect ratio deliberately — it changes composition, not just crop.
- For moodboard/style-tile batches: hold layers 3–5 constant across the set and vary
  only subject/environment. Consistency across a board comes from shared light and
  grade, not shared subjects.
- Offer 2–3 prompt variants with different emphasis when the goal is exploratory
  (David works options-first); one precise prompt when the target is locked.

## Platform notes

- **Midjourney** — parameters (`--ar`, `--style`, `--chaos`), multi-prompt weighting.
- **DALL-E / Flux** — full natural-language sentences; describe, don't keyword-stack.
- **Stable Diffusion** — token weighting, embeddings, LoRA references.
- **Firefly** — favors clean descriptive language; strong for brand-safe commercial work.

## Templates

**Cinematic portrait**
```
Dramatic portrait of [subject], wearing [attire], [expression], key light 45° camera
left creating Rembrandt triangle, subtle fill, rim light separating from [background],
85mm f/1.4 at eye level, shallow depth of field with creamy bokeh, [palette] color
grade, [film stock] aesthetic, editorial quality
```

**Product hero**
```
[Product] hero shot, [material/finish], on [surface], large softbox overhead creating
gradient, strip lights for edge definition, [background treatment], shot at [angle],
focus stacked for full sharpness, [brand aesthetic], clean post-processing, commercial
advertising quality
```

**Environmental / documentary**
```
[Subject] in [location], [activity], natural [time of day] light, environmental context
showing [background elements], [focal length] at f/[aperture], candid feel, [palette],
documentary style, authentic unretouched aesthetic
```

---
*Adapted from `design-image-prompt-engineer` in [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT), distilled and fitted to David's workflow 2026-07-08.*
