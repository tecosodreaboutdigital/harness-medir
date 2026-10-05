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

## Five more questions, added on 5 October 2026

Part 1's twelve questions stay as they are. These five come from running agents in production, not
from the checklist, and they sit here so the instrument can grow without changing the article. Answer
them in the same way, yes or no, with the same owner named for each "no".

```
OPERATION
[ ] Which actions are safe to retry, and does the system know that for each one?
[ ] After an interruption, is it defined whether the agent resumes, retries, rolls back or restarts?
[ ] Can text the agent reads (web pages, e-mail, files, memory, skills, other agents) carry
    instructions it would follow?   (the answer you want is "no, or it is contained")
[ ] Can the agent change the file that defines its own permissions?   (the answer you want is "no")
[ ] Do you know which model and harness version produced the last result?
```

How they change the tier decision:

- **A "yes" to "can the agent change the file that defines its own permissions"** blocks N3, whatever
  else the checklist says. A policy the agent can edit is a request, not a policy.
- **A "no" to "do you know which model and harness version produced the last result"** blocks N2.
  Without it, a change in behaviour cannot be attributed, and a firing history means nothing across
  versions.
- The other three feed the receipt: `idempotency_key` and `action_stage` (retry and interruption),
  and `sources_consulted[].trust` (what the agent reads).

## The thirteen failure classes

The `failure_class` field of `execution-receipt.md` takes one of these. The list is a taxonomy that
a 2026 handbook on harness engineering proposes (Tech with Mak, self-published, 4 October 2026; used
here for orientation only, and not a standard). It is useful because a failure that can be named can
be counted, and a count is what the indicators of Part 4 are built from.

| Class | One line |
|---|---|
| Tool selection | The agent picked the wrong tool, or one that sounds like the right one |
| Tool contract | The tool's inputs, outputs or errors did not mean what the agent assumed |
| Observation | The agent misread or ignored what a tool returned |
| Context | The right information was not in front of the model when it decided |
| State | What the agent remembered or stored was stale, lost or wrong |
| Environment | The place the agent runs in, not the agent, failed (network, disk, a changed dependency) |
| Verification | A check was missing, wrong or satisfied by a claim instead of evidence |
| Authorisation | An action ran without the approval it needed, or was blocked when it should not have been |
| Recovery | The agent could not resume, retry safely or roll back after an interruption |
| Coordination | Several agents or steps conflicted, duplicated work or lost a handoff |
| Budget | A limit (steps, tokens, time, cost) was hit, or was missing |
| Provenance and injection | Untrusted text was treated as an instruction, or its source was not recorded |
| Skill-induced | A loaded skill made the work wrong or slower |

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
