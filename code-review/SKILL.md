---
name: code-review
description: >
  Reviews code for correctness, readability, and maintainability. Use when the user says
  "review this code," "code review," "is this well-structured," "check this for quality,"
  "does this look right," or shares a file, function, snippet, or diff and wants feedback
  before merging or shipping. General-purpose quality lens only: use security-review for
  vulnerabilities and review for GitHub PR workflow. Also used by product-owner as the
  Develop-discipline review step.
---

# Code Review

A structured quality pass on any code (snippet, file, module, or diff): is it correct,
readable, and maintainable?

## 1. Scope

Infer from context what is being reviewed, the language/stack, and existing conventions
(CLAUDE.md, style guide, lint config, patterns elsewhere in the codebase). Ask only if scope is
genuinely ambiguous. Prefer matching existing conventions over generic best practice. For a
fragment with no surrounding context, say so rather than assuming conventions.

## 2. Review

Apply only the dimensions that are present:

- **Correctness:** logic bugs, off-by-one, bad assumptions, unhandled edge cases (empty input, null, concurrency, scale).
- **Readability:** naming, function/file length, nesting, intent clear without heavy comments.
- **Duplication and structure:** logic to extract, misplaced responsibilities, coupling that makes change hard.
- **Error handling:** explicit, swallowed, or left to crash; is the failure mode right for where this runs?
- **Consistency:** matches the codebase's established patterns, or introduces a new one without reason.
- **Tests:** are risky paths (edge cases, error branches) covered, not just the happy path? Note gaps; don't demand 100%.
- **Performance:** flag only real concerns (O(n²) on unbounded n, N+1 queries, needless re-renders), not micro-optimizations.

## 3. Output

```
## Blocking Issues
[Bugs, correctness problems, or maintainability risks to fix before merging; cite file/line/function]

## Worth Considering
[Real, non-blocking improvements; flag, don't force]

## Direct Questions For You
[2–5 pointed questions where intent is genuinely unclear and guessing would be wrong]
```

Be honest: if the code is solid, say so rather than inventing findings. Cite the specific line
or function for every point, and make each actionable (what to change and why). Tone is direct and specific,
neither performative about severity nor hedging on real problems.

## Under product-owner

Works identically when dispatched by `product-owner`. Surface the output to the user as
usual; blocking issues pause the flow for a decision and are never auto-fixed by guessing at intent.
