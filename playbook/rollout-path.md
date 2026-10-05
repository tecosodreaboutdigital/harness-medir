# Rollout path template, N0 to N3

Grounded in: [Part 1](../harness-p1.html)'s autonomy-tier table, which Part 1 only sketches as a
static table, not a progression. The rule that turns it into a path is stated once, directly: "you
only move up a band when the sensor of the previous band actually works." Part 2 supplies the
matching signal for when that is true: its firing-history table reads "firings drop over time" as
meaning "the guides are working," and names that specifically as the moment to "consider moving up
an autonomy tier."

This template is this project's own construction, not a quotation: Part 1 states the gating
principle and Part 2 states the signal, but neither part writes out the path as a table. It is
listed here as a playbook template rather than a "done" item elsewhere in this project's tracking,
because it is new material assembled from two parts' arguments, not reproduced from either one.

---

```
Task or agent: <name>
Current tier: <N0 / N1 / N2 / N3>

TIER          WHAT MUST EXIST BEFORE ENTERING IT           EVIDENCE THIS RUN HAS IT   DATE ENTERED
N0 Assisted   An instruction and a model, nothing else.     <n/a, this is the floor>   <date>
              A human reviews every output.

N1 Guided     Written guide, defined tools, a task          <link to task-contract.md  <date>
              contract (task-contract.md). Reversible,       instance>
              low-cost tasks only (risk-matrix-by-tier.md).

N2 Measured   Durable state, working sensors (Part 2's      <sensor firing history,    <date>
              own bar: "the sensor of the previous band      trending down over what
              actually works"), a retry ceiling and a cost   period, and the result of k
              ceiling. Evidence produced before delivery,    identical runs judged by
              not asserted after. Consistent success in k    final state>
              identical runs (start with k = 5).

N3 Governed   Permission outside the model (a policy the     <execution-receipt.md      <date>
              system cannot rewrite, risk-matrix-by-tier.md), instances covering an
              a full trace (execution-receipt.md), and a      irreversible action>
              working rollback path (the receipt's
              rollback_point / reversal_point fields).
```

## The gate between each row

Do not promote on a calendar. Promote only when the row above's evidence column is filled with real,
checked data, the same discipline Part 2's inspection-line analogy asks for: a sensor that never
fires is not proof of a clean process, it may be proof the sensor measures the wrong thing.

**N0 to N1** requires a completed `task-contract.md`, not a verbal understanding of scope. Part 1's
own N1 row names the task contract explicitly as what has to exist.

**N1 to N2** requires a firing history (Part 2), not a single clean run. One good run under
observation proves the harness can work once. A trending-down firing rate over multiple runs is what
proves the guide, not luck, is doing the work.

It also requires consistent success: the same task, run k times on identical input, succeeding every
time, with success judged by the final state against the contract's done criterion and not by what
the agent reports. Start with k = 5. The idea is pass^k from tau-bench (Yao et al., arXiv:2406.12045),
the chance that all k trials of a task succeed, which falls quickly with k for an agent that is right
most of the time but not always. A firing history can look clean while an agent still fails one run in
five; a repeat run is what shows it.

**N2 to N3** requires the machinery Part 3 introduces, not more confidence in the existing setup.
Check each of these; do not assume any of them:

1. The policy is applied by the runtime (a hook, a rule or a permission), not requested in a prompt.
2. It sits outside the agent's write reach: the agent cannot edit the file that defines its own
   permissions.
3. It fails closed: if the policy cannot be read or evaluated, the action is refused.
4. A floor survives bypass mode: switching approval prompts off does not switch the policy off.
5. Containment is declared: which folders, which network destinations and which credentials the agent
   can reach (the compact guide's containment entry).
6. Every action that is not safe to repeat carries an operation key (`risk-matrix-by-tier.md`,
   `execution-receipt.md`).

Plus a receipt schema that already produces a real audit trail at N2. Granting N3 without this is the exact failure mode Part 1's own opening case
describes: an automation at N0 operating as if it were N3, with external, financial, irreversible
effect and no guide, no sensor, no approval limit and no trace.

**Moving down is also removing.** When the model changes, review every component of the harness
and remove what no longer pays for itself. Each guide, tool and check is a hypothesis about a
limitation of the model you had; a newer model may not have that limitation, and the component then
costs tokens, latency and attention for nothing. Run the same task with and without it, as
`skill-template.md`'s evidence section asks, before keeping it.

**Moving down a tier is not a failure of this template, it is the template working.** Part 4's own
life cycle (see `agent-registry.md`) treats a return to a lower state, suspension pending review, as
a normal transition triggered by an indicator firing, never as something to hide from this log.
