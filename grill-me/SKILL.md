---
name: grill-me
description: >
  Pressure-tests a project brief or a proposed solution before work starts or ships.
  Use this whenever the user says "grill me on this," "stress-test this," "poke holes
  in this," "what am I missing," "play devil's advocate," or asks for critical feedback
  before committing to a direction. Also use proactively when a brief seems to be
  accepted without scrutiny, or when a finished deliverable (design, code, doc, plan)
  is about to be presented or shipped without having been challenged first. Also called
  internally by product-owner at two checkpoints — right after a brief is decomposed
  into tasks, and right before subagent outputs are synthesized into a final
  deliverable. Covers two distinct modes: brief-grilling (is this the right problem)
  and solution-grilling (does this actually solve it) — do not conflate them.
---

# Grill Me

A structured stress-test for two different moments in a project: before you start (is this the right problem?) and before you ship (does this actually solve it?). The goal isn't to be difficult for its own sake — it's to surface the gaps that would otherwise show up three weeks later, expensively.

## Step 1: Detect which mode applies

- **Brief mode** — the input is a problem statement, project brief, task description, or plan that hasn't been executed yet. Trigger phrases: "grill me on this brief," "before we start," "is this the right approach," or product-owner calling immediately after task decomposition.
- **Solution mode** — the input is a finished or near-finished deliverable: a design, a piece of code, a document, a strategy doc, a plan someone's about to present. Trigger phrases: "grill me on this," "poke holes in this," "before I ship this," or product-owner calling right before final synthesis.

If it's ambiguous which mode applies (e.g., the user just pastes something with no context), ask — don't guess. Getting this wrong means asking the wrong questions entirely.

If asked to grill something that touches both (e.g., "here's the brief and my draft response"), run both modes and clearly separate the two sets of output.

## Step 2: Run the relevant question set

### Brief mode — is this the right problem?

Work through these, adapting to the specific brief rather than reciting them generically:

1. **Root cause vs. symptom** — Is this brief solving the actual problem, or a downstream symptom of something else? What would happen if you asked "why" one more time than the brief did?
2. **Audience clarity** — Who is this actually for? Does the brief name a real audience with real constraints, or an assumed/generic one?
3. **Success criteria** — What does "done" or "working" mean here, concretely? Is it measurable, or is it vibes ("looks better," "feels modern")?
4. **Missing context** — What's the brief silent on that would normally cause a mid-project derailment — budget, timeline, technical constraints, stakeholder approval chain, existing systems it has to integrate with?
5. **Scope creep risk** — Where does the brief's language quietly imply more work than what's explicitly scoped?
6. **Alternative framings** — Is there a fundamentally different way to frame this problem that the brief didn't consider?

### Solution mode — does this actually solve it?

1. **Traceback to the brief** — Does this deliverable actually address what the original brief asked for, or does it solve an adjacent, easier problem?
2. **Edge cases** — What breaks at the edges: error states, empty states, scale, unusual input, accessibility, different devices/contexts?
3. **Roads not taken** — What alternative approach existed and wasn't chosen — and is the reason it wasn't chosen actually good, or just the path of least resistance?
4. **Hidden cost** — What technical debt, maintenance burden, or future constraint does this quietly introduce?
5. **Stakeholder stress test** — What would the most skeptical person in the room ask about this that isn't already answered?
6. **Evidence vs. assertion** — Where does this deliverable claim something works without showing why (e.g., "this will improve conversion" with no reasoning or data behind it)?

## Step 3: Structure the output

Always end in questions, not a monologue — the point is to prompt a response, not deliver a verdict.

```
## Blocking Issues
[Things that should be resolved before proceeding — genuine gaps or risks, not nitpicks]

## Worth Considering
[Real concerns that aren't fatal — flag them, don't force a stop]

## Direct Questions For You
[2-5 pointed questions the person actually needs to answer]
```

Keep "Blocking Issues" honest and short — if there's nothing genuinely blocking, say so rather than manufacturing severity to seem thorough. Padding this section erodes trust in it over time.

## Tone

Direct and specific, not performative or theatrical about being "harsh." Every point should be something the person can act on, not just an observation that something feels off. Cite the specific line, assumption, or gap in the input being grilled rather than making generic observations that could apply to any brief or any solution.

## Standalone vs. product-owner usage

This skill works identically whether invoked directly by the user or called by `product-owner`. When called by `product-owner`:
- After task decomposition → run in **brief mode** against the decomposed task list, before subagents are dispatched
- Before final synthesis → run in **solution mode** against subagent outputs, before they're written up and presented

In both cases, product-owner should surface the grill-me output to the user rather than resolving it silently — blocking issues in particular should pause the flow for a decision, not get auto-resolved by an agent guessing at intent.
