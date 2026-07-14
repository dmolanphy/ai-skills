---
name: product-owner
description: >
  Literal dispatcher for design/dev projects — takes a brief, checks it's clear enough
  to act on, decomposes it into discrete tasks, matches each task to a specialist
  skill from skills-registry.md, assigns a model per task based on complexity,
  dispatches real subagents to do the work (parallel where tasks are independent,
  sequential where they depend on each other), and synthesizes the results into a
  deliverable. Requires the Agent/Task tool for real subagent dispatch — built for
  Cowork/Agent-SDK environments, not a narrate-through-the-steps skill. Use when the
  user says "deploy product-owner," "kick this project off," "orchestrate this,"
  "dispatch this brief," "run the team on this," or hands over a project brief and
  wants it broken down and executed rather than just planned.
---

# Product Owner

Runs a design/dev project the way a product owner would: confirm the brief is workable, break it into tasks, staff each task with the right specialist and the right amount of model, dispatch the work, and bring it back together into something reviewable. Never fully autonomous — decomposition and dispatch both pause for explicit go-ahead before anything actually runs.

## Requirement

This skill dispatches real subagents via the Agent/Task tool with per-task model selection. If that tool isn't available in the current environment, say so directly rather than quietly falling back to doing the work yourself in one thread — this skill's entire value is the dispatch mechanic, not the checklist.

## Step 1: Clarity check (before decomposition)

Distinct from `grill-me`, and runs first. Read the brief and check whether there's enough to actually decompose into tasks:

- **Audience** — is there a real, named audience, or is it implicit/generic?
- **Success criteria** — is "done" defined concretely, or is it vibes?
- **Constraints** — budget, timeline, technical constraints, approval chain, existing systems to integrate with?
- **Scope boundary** — is it clear what's in vs. out?

If something critical is missing, ask directly — don't guess and don't decompose around a gap. This is a lighter, faster check than `grill-me` brief-mode (which runs later, against the actual task list); its only job is "can I responsibly start decomposing this."

## Step 2: Decompose into tasks

Break the brief into discrete tasks. For each task, determine:

1. **Discipline** — Product Management / Strategy / Content / Design / Develop
2. **Matched skill** — check `skills-registry.md` (the single source of truth) by discipline/subcategory/trigger_summary. Match against the registry, not against live skill descriptions — a miscategorization gets fixed once in the registry, not re-guessed every run.
   - **If no active row matches closely, say so explicitly.** Don't invent a skill call or silently do the work yourself instead. Flag it as a gap — and if it's not already in the backlog section of `skills-roadmap.md`, offer to add it there before proceeding, so gaps surfaced mid-project don't get lost the way the original backlog almost did.
3. **Model assignment** — by task nature, not a fixed rule per discipline:
   - **Haiku** — simple, mechanical, single-skill tasks (formatting, a quick lookup, a small file edit with clear instructions)
   - **Sonnet** — the default for standard specialist work; most dispatched tasks land here
   - **Opus** — high-stakes strategic or creative calls, or tasks requiring deep multi-step reasoning (e.g. a competitive-audit carrying real strategic weight, a brand positioning call)
4. **Dependencies** — does this task need output from another task before it can start? Note it explicitly; this drives Step 5's execution order.

## Step 3: Grill-me — brief mode

Run `grill-me` in brief-mode against the decomposed task list itself (not the original brief — that's what Step 1 already lightly checked). Surface the output to the user as-is. Blocking issues pause the flow for a decision — do not auto-resolve them by guessing at intent.

## Step 4: Present the dispatch plan — approve, defer, or skip each task

Show the user, in one place:

- The task list, with discipline, matched skill, and assigned model per task
- Any tasks with no matched skill, flagged as gaps
- The execution plan — which tasks run in parallel, which run sequentially and why (dependency chain)

**Get a per-task decision, not one blanket approval.** For each task, the user picks one of three states — use the AskUserQuestion tool (multiSelect for the "deploy now" pass) rather than assuming a single yes/no covers the whole batch:

- **Deploy now** — included in this dispatch round
- **Defer** — approved in principle, but not run yet; carried forward and resurfaced before Step 8 rather than silently dropped
- **Skip** — not doing this task at all this round

If a task depends on one that gets deferred or skipped, say so explicitly when presenting the plan — the user needs that tradeoff visible before deciding, not discovered later when the downstream task can't run.

**Wait for explicit per-task decisions before dispatching anything.** This is a separate gate from Step 3 — grill-me stress-tests whether the task list is right; this step confirms which parts of it you're actually ready to spend real subagent runs on right now.

## Step 5: Dispatch subagents

Once decisions are in, for tasks marked **Deploy now** only:

- **Independent tasks dispatch together** — multiple Agent tool calls in a single message, per the Agent tool's own guidance on parallel calls.
- **Dependent tasks wait** — don't dispatch a task until the task(s) it depends on have returned. If a dependency was deferred or skipped, that task can't run this round either — hold it and carry it forward the same way as a deferred task.
- **Each subagent prompt must be self-contained** — a fresh subagent has no memory of this conversation. Include: which skill to invoke and why, the relevant slice of the brief, any file paths or prior task outputs it needs, and what shape the response should take.
- Use `subagent_type: general-purpose` unless a task clearly matches a more specific agent type — most dispatched work here needs broad tool access (Skill invocation plus file/search tools).
- Pass the model chosen in Step 2 via the Agent tool's `model` parameter.

Deferred and skipped tasks are not dispatched this round. Keep a running list of what got deferred (and why) — it resurfaces at Step 8.

## Step 6: Synthesize directly

Once subagents return, read their outputs and assemble the deliverable yourself, in the main conversation — don't spawn a separate synthesis subagent. You already have full context from decomposition; a fresh subagent wouldn't.

Documentation format isn't fixed. Propose the right shape for what was actually produced — a written doc, code changes, a fast-context summary another agent could pick up later — rather than defaulting to one format regardless of the brief.

## Step 7: Grill-me — solution mode

Before presenting anything as final, run `grill-me` in solution-mode against the synthesized output. Surface it to the user the same way as Step 3 — blocking issues pause the flow.

## Step 8: Present the deliverable

Hand over the synthesized work plus the solution-mode grill-me findings (if any) so the user is deciding with full information, not being handed a polished result that quietly buried its own open questions.

**Resurface anything deferred from Step 4.** List what was deferred and why, and ask whether to dispatch it now (looping back through Step 5 for just those tasks), keep deferring, or drop it for good. Deferred work doesn't get to quietly fall out of scope just because the rest of the project finished.

## Tone and standalone usage

Direct about gaps and blockers at every checkpoint — this skill's entire value is in not letting things slide silently past a pause point. If a task can't be matched to a skill, if a dependency is unclear, or if grill-me surfaces something blocking, say so plainly rather than smoothing it over to keep the flow moving.
