---
type: llm
weight: 1
---

The response runs a scoped intake for a shadcn/ui foundation instead of importing everything. All of these must be true:

1. It asks whether to build Light-only or Light + Dark (dark mode) rather than assuming either.
2. It does not plan to build chart or sidebar tokens by default — it either asks whether they're needed or states they're off unless requested.
3. It asks for the Figma file (URL) to work in and does not create a new file or claim to have built anything yet.

Fail the response if any of the three is missing.
