---
name: code-review
description: >
  Reviews code for correctness, readability, and maintainability — general-purpose
  quality review, not security auditing and not GitHub-PR-diff mechanics. Use this
  whenever the user says "review this code," "code review," "is this well-structured,"
  "check this for quality," "does this look right," or shares a file, function, or
  snippet and wants feedback before merging or shipping. Distinct from security-review
  (vulnerability-focused) and review (GitHub PR review workflow) — this skill works on
  any code regardless of whether it's a diff, a whole file, or a pasted snippet, and
  its lens is quality/maintainability rather than security or PR mechanics. Also called
  internally by product-owner as the Develop-discipline review step before subagent
  output is synthesized.
---

# Code Review

A structured quality pass on code — correctness, readability, and maintainability. Not a security audit (use `security-review` for that) and not a GitHub PR workflow (use `review` for that). This is the skill for "is this good code," asked of any snippet, file, or module regardless of where it lives.

## Step 1: Establish scope

Before reviewing, confirm (from context or by asking if genuinely unclear):

- **What's being reviewed** — a single function, a file, a module, a whole diff?
- **Language/stack** — review criteria differ (e.g. error handling idioms in Go vs. JS).
- **Existing conventions** — is there a CLAUDE.md, style guide, lint config, or established pattern elsewhere in the codebase this should be checked against? Prefer matching what's already there over imposing generic best practice.

If reviewing a fragment with no surrounding codebase context, say so explicitly rather than assuming conventions that may not hold.

## Step 2: Work through the quality dimensions

Adapt to what's actually present — don't recite a checklist that doesn't apply.

1. **Correctness** — Logic bugs, off-by-one errors, incorrect assumptions, unhandled edge cases (empty input, null/undefined, concurrent access, scale).
2. **Readability** — Naming, function/file length, nesting depth, whether a new reader could follow the intent without extensive comments.
3. **Duplication & structure** — Repeated logic that should be extracted, misplaced responsibilities, coupling that will make future changes harder.
4. **Error handling** — Are failures handled explicitly, silently swallowed, or left to crash? Is the failure mode appropriate for where this code runs?
5. **Consistency** — Does this match the conventions already established elsewhere in the codebase (naming, structure, error handling style), or does it introduce a new pattern without reason?
6. **Test coverage** — Are the risky paths (edge cases, error branches) covered, or only the happy path? Note gaps rather than requiring 100% coverage as a rule.
7. **Performance** — Only flag if there's a real concern (e.g. O(n²) where n is unbounded, unnecessary re-renders, N+1 queries) — not micro-optimization for its own sake.

## Step 3: Structure the output

Reuse the `grill-me` format so output is consistent across the skills library:

```
## Blocking Issues
[Bugs, correctness problems, or maintainability risks serious enough to fix before merging — cite the specific file/line/function]

## Worth Considering
[Real improvements that aren't blocking — flag them, don't force a fix]

## Direct Questions For You
[2-5 pointed questions where intent is genuinely unclear and guessing would be wrong — e.g. "is this edge case actually reachable in production?"]
```

Keep "Blocking Issues" honest — if the code is solid, say so rather than manufacturing findings to seem thorough. Cite the specific line or function for every point; generic observations that could apply to any code aren't useful.

## Tone

Direct and specific, matching `grill-me`'s tone — not performative about severity, not hedging on real problems. Every point should be actionable: what to change and why, not just "this feels off."

## Standalone vs. product-owner usage

Works identically whether invoked directly ("review this code") or dispatched by `product-owner` as the Develop-discipline quality-review step. When `product-owner` calls it, surface the output to the user the same way `grill-me` does — blocking issues should pause the flow for a decision, not get silently auto-fixed by an agent guessing at intent.
