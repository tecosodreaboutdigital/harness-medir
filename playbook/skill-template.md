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
version: <version of this skill>
author: <named author>
licence: <licence of the skill, e.g. MIT>
# Optional, and support varies by tool; check yours before relying on either:
# activation: <a path pattern or an environment requirement that must hold>
# allowed-tools: <the tools this skill may use, if the tool supports a list>
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

## Evidence it helps
Task: <one task the skill is meant to improve>
Same input, without the skill: <result and cost>
Same input, with the skill: <result and cost>
Keep it only if the second beats the first. A skill that looks relevant can still make the work
wrong or slower.
```

## Notes before you fill this in

**The `## Never` section is not decoration.** Part 2's own case for it: the guide-writing failure
mode is not that the rule was badly written, it is that the system talks itself out of it under a
plausible-sounding justification. Writing the excuse down in advance is "getting ahead of the
negotiation instead of waiting for it to happen."

**Measure before you keep it.** The `## Evidence it helps` section is the cheapest guard against
loading a skill because it sounds right. A 2026 study of two benchmark suites reported 307 failures
induced by skills that looked relevant, 125 functional and 182 efficiency regressions (Dong et al.,
arXiv:2608.11888). The study does not say how often this happens in general; it says it happens,
which is enough to measure the task with and without the skill once.

**A skill the agent wrote for itself is a draft.** It counts only after a person has read it, the
same rule that applies to any change to the agent's own instructions (`risk-matrix-by-tier.md`).

**If the skill's steps have side effects that must not repeat on a retry, such as sending an e-mail or
charging a payment, consider a coded workflow instead of a skill.** Microsoft's own guidance for its
agent framework says to prefer workflows when steps produce side effects that should not be repeated
(Agent Skills documentation, revised 2 October 2026).

**If this skill produces anything with external effect, add a receipt.** See
`execution-receipt.md`. Part 2's own business-unit example is the one that introduces this: once a
skill's output leaves the company, or reaches someone who is not the person who ran it, the skill
needs a receipt, not just a done criterion.

**If the skill's output ever needs named human approval before acting, add a gatekeeper step
referencing `risk-matrix-by-tier.md`,** the same way Part 2's business-unit example gates on a table
someone approves that the system cannot rewrite.
