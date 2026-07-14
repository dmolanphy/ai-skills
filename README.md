# AI-Skills

Central, version-controlled home for my agent skills — one folder per skill, following the open SKILL.md standard. Lives in DM-OS so my skills travel with me; platforms get symlinks or copies, never ownership.

## Structure

```
AI-Skills/
├── writing-style/           # my voice: headlines, copy, decks, briefs
├── design-spec/             # generate DESIGN.md specs from Figma files
├── ds-foundations/          # design-system foundations in Figma
├── visual-storyteller/      # narrative structure for decks, moodboards, data stories
├── image-prompt-engineer/   # layered prompts for AI image generation
├── brand-guardian/          # brand strategy foundations, identity systems, audits
├── grill-me/                # devil's-advocate stress-test for a brief or a finished deliverable
├── buyer-journey-builder/   # evidence-based buyer journey maps, validated vs. assumed
├── code-review/             # general-purpose correctness/readability/maintainability review
├── competitive-audit/       # market landscape + how competitors frame and describe their solutions
├── transitions-dev/         # 21 production-ready CSS transitions + motion tokens (vendored)
├── skills-registry.md       # machine-readable skill index for the in-progress product-owner orchestrator
└── skills-roadmap.md        # discipline-by-discipline inventory of built vs. planned skills
```

`skills-registry.md` and `skills-roadmap.md` aren't skills themselves — they're planning docs for a `product-owner` orchestrator (not yet built) that will decompose briefs and dispatch them to the right skill. Keep the registry in sync whenever a skill here goes from planned to active.

`visual-storyteller`, `image-prompt-engineer`, and `brand-guardian` are adapted from [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) (MIT) — converted from agent-persona format to SKILL.md and distilled to fit my workflow. Provenance is noted at the bottom of each SKILL.md.

`transitions-dev` is vendored **verbatim** from [Jakubantalik/transitions.dev](https://github.com/Jakubantalik/transitions.dev) (`skills/transitions-dev/`, captured 2026-07-09). It's auto-generated from the upstream site, so don't hand-edit it — to update, re-copy that folder from a fresh clone. One local patch: the frontmatter description is compressed to fit the 1024-char install limit (upstream's is 1193) — re-apply that trim after any upstream refresh. Deploy when building components or prototypes. For personal use; not for redistribution (upstream repo has no explicit license).

Each skill folder: `SKILL.md` required, plus optional `assets/` and `references/`. Future skills go here the same way — a new top-level kebab-case folder per skill.

## How to actually use a skill from here

Skills reach Claude differently depending on which surface you're using — there's no single "sync" that covers both. See the note in each product's docs for specifics; the short version:

### Claude Code
Skills are read live from a folder on disk — personal skills at `~/.claude/skills/`, project skills at `.claude/skills/` inside a repo. Since that's just a directory, this repo can be cloned or symlinked straight in:

```bash
git clone <this-repo-url> ~/.claude/skills/design-skills
# or, if you already have other personal skills:
git clone <this-repo-url> /tmp/design-skills && cp -r /tmp/design-skills/ds-foundations ~/.claude/skills/
```

Pulling updates (`git pull`) picks up edits on the next Claude Code session — no re-upload needed.

### claude.ai (web / desktop / Cowork)
Custom skills are uploaded as a **ZIP file** through **Settings > Customize > Skills** — claude.ai doesn't read live from a git folder. Workflow:

1. `git pull` this repo to get the latest version of the skill.
2. Zip the individual skill folder (not the whole repo) — e.g. `cd design-skills && zip -r ds-foundations.zip ds-foundations`.
3. Upload that zip in Settings > Customize > Skills. If a version already exists there, delete it first, then re-upload.

This repo is the source of truth; the claude.ai copy is a manual snapshot that needs re-uploading after edits made here.

## Making edits

Edit the `SKILL.md` / `references/*.md` files directly (by hand, or by asking Claude to make the edit and copying the result back here), then:

```bash
git add .
git commit -m "describe what changed"
git push
```
