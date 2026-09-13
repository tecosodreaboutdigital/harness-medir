# Skill template

Grounded in: [Part 2](../harness-p2.html#en-exemplos), the five-field skeleton every worked example
uses ("contract, guide, sensor, gatekeeper and receipt"), and the non-negotiable-rule-plus-red-flags
pattern Part 2 borrows from the most used skill collections and explains directly: the point is not
to teach the system the rule, it already knows it, the point is to stop it talking itself out of
following the rule under pressure.

This is the scaffold behind Part 2's two full worked examples (an individual contract-review skill,
a team weekly-report skill). Copy it, fill every section, delete none: a skill missing its `## Never`
section is a guide, not a skill, in this project's own terms.

---

```
---
name: <kebab-case-name>
description: <One or two sentences. State what it does and when to use it, the way
  every real example in Part 2 does. This is what a system reads to decide whether
  to reach for this skill at all.>
---

# <Human-readable title>

## Task contract
Delivers: <see task-contract.md, the "Delivers" field, copied here>
Never does: <see task-contract.md, the "Never does" field, copied here>
Done when: <see task-contract.md, the "Done when" field, copied here>

## How to do the work
1. <Step. Prefer an imperative, checkable instruction over a description of intent.>
2. <Step.>
3. <Step. If verification is a command, name the exact command here, the way Part
   2's team example names `python verify.py report.md`.>

## Never
NON-NEGOTIABLE RULE: <the one rule this skill cannot break, stated in one sentence,
short and unambiguous.>

Red flags, stop if you catch yourself thinking:
- "<the most plausible excuse for breaking the rule under time pressure>"
- "<a second plausible excuse, phrased the way the system would actually phrase it>"
- "<a third, if a real one exists. Do not pad this list with a generic entry: Part 2's
  own guidance is to write the actual excuse, not a placeholder>"
None of these is verification. Follow the rule anyway, and say so in the output.
```

## Notes before you fill this in

**The `## Never` section is not decoration.** Part 2's own case for it: the guide-writing failure
mode is not that the rule was badly written, it is that the system talks itself out of it under a
plausible-sounding justification. Writing the excuse down in advance is "getting ahead of the
negotiation instead of waiting for it to happen."

**If this skill produces anything with external effect, add a receipt.** See
`execution-receipt.md`. Part 2's own business-unit example is the one that introduces this: once a
skill's output leaves the company, or reaches someone who is not the person who ran it, the skill
needs a receipt, not just a done criterion.

**If the skill's output ever needs named human approval before acting, add a gatekeeper step
referencing `risk-matrix-by-tier.md`,** the same way Part 2's business-unit example gates on a table
someone approves that the system cannot rewrite.
