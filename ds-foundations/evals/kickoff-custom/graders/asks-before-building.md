---
type: llm
weight: 1
---

The response treats this as the start of an intake conversation rather than a finished build. All of these must be true:

1. It asks the user which Figma file to work in (or asks for a Figma file URL) and makes clear it will wait for that before building.
2. It does NOT create a new Figma file, and does not claim to have created one or to have built variables, styles, or pages.
3. It asks which foundation type to build — the user's own/custom system versus a shadcn/ui-aligned structure — instead of picking one silently.

Fail the response if any of the three is missing.
