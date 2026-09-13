# Task contract template

Grounded in: [Part 1](../harness-p1.html#en-medir), the Map step, and the N1 row of the autonomy-tier
table ("written guide, defined tools, task contract"). The Map questions from the twelve-question
checklist this contract answers: is the definition of done written before execution begins, can the
system find the right knowledge without loading everything, are the task limits explicit including
what it must not do.

No harness has one of these without it. It is the artefact that makes correction possible: Part 2
states plainly that "correction is out of reach of any sensor if the human did not clearly say,
beforehand, what they wanted." A missing or vague field here is not a formatting problem, it is the
exact gap no sensor downstream can close.

Copy the block below, delete this preamble, fill every field. Leave no field blank: write "not
applicable" rather than deleting one you have not thought through.

---

```
# Task contract: <name of the task or skill>

## Delivers
<What a finished, correct run actually produces. One or two sentences, concrete
enough that two different people would recognise the same output as correct.>

## Never does
<Everything explicitly out of scope. This is not a nice-to-have. Part 2's own worked
examples make this the field that keeps a reviewer skill from ever declaring a
contract approved, and a report skill from ever opining on commercial merit.>

## Done when
<The literal, checkable condition. Prefer a command's output, a file's existence, or
a specific state over a description of effort. "Every item in checklist.md is marked
present, absent or not verifiable" is a done criterion. "The review is thorough" is not.>

## Boundaries
<What the task must not touch: systems, records, people, budgets. If an action would
answer yes to all three of the rule-of-two questions (private data, untrusted content,
external communication, see execution-receipt.md), name that here explicitly, do not
leave it to be discovered at runtime.>

## Knowledge required
<Where the task finds what it needs, and what it should NOT have to load to do its
job. The Map question this answers: can the system find the right knowledge without
loading everything.>

## Autonomy tier
<N0, N1, N2 or N3, see rollout-path.md. State it, do not leave it implicit. A task
with no tier stated defaults to N0: a human reviews every output.>

## Owner
<The named person who answers for this task's contract, not a department. See
agent-registry.md if this contract belongs to a standing agent rather than a
one-off task.>
```
