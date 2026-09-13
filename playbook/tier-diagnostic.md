# Tier diagnostic template

Grounded in: [Part 1](../harness-p1.html#en-checklist)'s twelve-question checklist, "use this before
letting any agent touch real work." Part 1 states the finding this template turns into an
instrument: "if several answers are no, a stronger model will not fix it: it will only make the
failure more expensive." The checklist was written to be read once. This is the same twelve
questions, organised so a team can run it as a standing instrument, on a real task, not as a thought
experiment.

Run this before assigning a tier in `agent-registry.md`, and again at every revalidation (see
`rollout-path.md`): a task that answered yes across the board six months ago can drift, and Part 2's
own firing-history table treats a rising rate of the same failure as the signal that a guide, not
the model, needs attention.

---

```
Task or agent being diagnosed: <name>
Diagnosed by: <named person>
Date: <date>

MAP
[ ] Is the definition of done written before execution begins?
[ ] Can the system find the right knowledge without loading everything?
[ ] Are the task limits explicit, including what it must not do?
Map score: <count of yes> / 3

EQUIP
[ ] Does every tool have a clear purpose and a predictable failure state?
[ ] Are decisions stored outside the conversation?
[ ] Is execution isolated from production systems?
Equip score: <count of yes> / 3

DELEGATE
[ ] Is the autonomy granted proportional to the cost of the error?
Delegate score: <count of yes> / 1

INSPECT
[ ] Does every risky transition produce evidence rather than an opinion?
[ ] Is the evaluator different from the executor?
Inspect score: <count of yes> / 2

REINFORCE
[ ] Does every loop have a retry ceiling, a cost ceiling and an escalation path?
[ ] Does every failure update a guide, a test, a tool or a permission?
[ ] Can you reconstruct what happened and reverse what was done?
Reinforce score: <count of yes> / 3
```

## How to read the result

**This is a gate, not a scorecard.** Part 1 does not offer a numeric threshold, and this template
does not invent one: a project with eleven yeses and one no is not "92% ready," it has one specific,
named gap, and that gap is exactly where the next incident will originate. Read each "no" as an open
item with a named owner, not as a number to average away.

**A "no" names the MEDIR step to fix, not the whole harness.** A gap in Map (no definition of done)
is a different problem, with a different fix, from a gap in Reinforce (no retry ceiling). Fix the
step where the "no" actually lives; do not add unrelated controls elsewhere to compensate.

**Tier assignment, read against `risk-matrix-by-tier.md` and the autonomy-tier table in
`README.md`:**

- Any "no" in Map or Equip: the task is not ready to leave N0. A human reviews every output until
  those gaps close.
- All of Map and Equip are "yes," but Inspect or Reinforce has a "no": N1 is defensible for
  reversible, low-cost tasks (see `risk-matrix-by-tier.md`). Do not grant N2 or above: Part 1's own
  N2 row requires durable state, sensors and a retry ceiling, exactly what an Inspect or Reinforce
  "no" means is missing.
- All twelve are "yes": N2 is defensible. N3 additionally requires the permission-outside-the-model
  and rollback machinery `rollout-path.md` describes, which this checklist does not itself verify.

**Re-run this at revalidation, not only at intake.** A tier granted once and never rechecked is
exactly the governance debt Part 4 documents for non-human identity generally. This instrument is
cheap enough to repeat on a calendar.
