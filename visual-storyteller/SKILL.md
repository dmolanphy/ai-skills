---
name: visual-storyteller
description: >
  Structure visual narratives for decks, moodboards, storyboards, data stories, and
  campaign concepts. Use this skill whenever the work involves telling a story visually —
  building a presentation narrative, sequencing a deck, art-directing a moodboard,
  planning a storyboard or video concept, turning data or complex information into a
  visual story, or mapping an emotional journey. Trigger on requests like "help me
  structure this deck", "build a moodboard for", "storyboard this", "make this data
  tell a story", or any concept/campaign work that needs narrative shape — even if the
  user never says "story."
---

# Visual Storyteller

Give visual work narrative shape. A deck, a moodboard, a campaign — each one is a story
with a beginning, a tension, and a resolution. Flat sequences of nice images don't move
anyone; structured ones do.

Pair this skill with `writing-style` — it governs the words (headers, copy, framing);
this skill governs the narrative and visual structure underneath them.

## Narrative spine (use for any visual sequence)

Build every visual narrative on this arc before touching layout or imagery:

1. **Setup** — the world as the audience knows it. Establish context fast.
2. **Tension** — the gap, problem, or misalignment. This is the engine; without a
   tension the story is a brochure. (Mirrors the writing-style rule: frame ideas as
   tensions, not solutions.)
3. **Resolution** — how the idea, brand, or product closes the gap.

Then map the **emotional journey**: where should the audience feel recognition,
discomfort, curiosity, relief? Place visual peaks (bold image, stark stat, white space)
at those moments. Pacing is rhythm — vary density, don't let every slide shout.

## Deck structure

- Idea before deliverable, problem before tactics. Open high-level.
- Every section ladders to a strategic takeaway; cut sections that don't.
- One idea per slide. If a slide needs a paragraph, it's two slides or none.
- Sequence check: read only the headers start to finish — they should tell the whole
  story on their own. If they don't, restructure before polishing.

## Moodboards & art direction

- Anchor every board to a written **mood statement** first (2–3 sentences: feeling,
  era, energy, texture). Images serve the statement, not the reverse.
- Organize by: palette / typography energy / photography style / texture & materials /
  in-the-wild references. Label groupings.
- Deliver 2–3 distinct directions with names and a one-line POV each — not one big
  board of everything. (David works options-first.)
- For AI-generated reference imagery, hand off to the `image-prompt-engineer` skill.

## Storyboards & motion

For video, animation, or interactive concepts: frame-by-frame beats, each beat noting
(a) what's on screen, (b) what it makes the viewer feel, (c) duration/pacing. Identify
the single held moment — every good piece has one frame it's willing to slow down for.

## Data storytelling

- Find the story in the data before choosing a chart: what changed, what's surprising,
  what's the tension? The headline is the finding, not the metric name.
- Progressive disclosure: lead with the one-number takeaway, reveal supporting layers
  on demand. Never open with the full spreadsheet view.
- Choose chart types by comparison job (change over time → line; composition → stacked;
  distribution → histogram; relationship → scatter). Strip everything that isn't the
  point — gridlines, legends, decoration.

## Standards

- Accessibility isn't optional: contrast-check palettes, never encode meaning in color
  alone, alt-text anything that ships digitally.
- Keep brand consistency across the sequence — one visual voice per story.
- Check cultural read on imagery and metaphors before client presentation.

---
*Adapted from `design-visual-storyteller` in [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT), distilled and fitted to David's workflow 2026-07-08.*
