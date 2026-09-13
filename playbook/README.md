# The harness-medir playbook

Seven operational templates, each one traceable to the part and section that already introduced its
underlying concept. None of these is invented fresh: this directory reuses the four parts and the
compact guide, it does not add a fifth idea to the series. See `harness-playbook.html` for the
human-facing explanation of each one, and `NEXT-STEPS.md` item 3 for why this was deliberately
parked from 31 August 2026 until 13 September 2026: building it right after finishing the article
series would have blurred the line between the argument and the toolkit derived from it.

**Opens with D10** (`../diagrams/part4/d10-quarterly-loop.svg`), the office's own quarterly loop from
[Part 4](../harness-p4.html), section 6: briefing, certification, operation, receipts, indicators,
revalidation, and back to briefing. It organises this whole playbook the same way it closes Part 4's
eight-indicators section, a second, legitimate appearance rather than a competing one.

| Template | File | Grounded in |
|---|---|---|
| Task contract | `task-contract.md` | Part 1, the Map step |
| Skill | `skill-template.md` | Part 2, the five-field skeleton and the two worked examples |
| Execution receipt | `execution-receipt.md` | Part 2's base receipt, extended in Part 3 with the rule-of-two answers and the reversal point |
| Risk matrix by tier | `risk-matrix-by-tier.md` | Part 3's matrix of authority, crossed with Part 1's N0 to N3 tiers |
| Tier diagnostic | `tier-diagnostic.md` | Part 1's twelve-question checklist, expanded into a standing instrument |
| Rollout path, N0 to N3 | `rollout-path.md` | The progression Part 1 states as a rule and Part 2 states as a signal, assembled here for the first time as a path |
| Agent registry | `agent-registry.md` | Part 4's life cycle (six states) and four roles |
| Certification meeting minutes | `certification-minutes.md` | Part 4's certified state, formalising the certifier's act |

The last row of the table above (agent registry and certification minutes) is one bullet in
`NEXT-STEPS.md` item 3 but two separate files here, since a registry and a set of meeting minutes
are used differently and by different people in the room.

## How these connect to each other

`task-contract.md` feeds `skill-template.md` (a skill's own `## Task contract` section is the same
fields). `risk-matrix-by-tier.md` and `execution-receipt.md`'s `rule_of_two` block are the two
independent nets Part 3 insists both run together. `tier-diagnostic.md` feeds the tier decision in
`rollout-path.md`, which in turn feeds the tier column in `agent-registry.md`. `certification-minutes.md`
is the record that sets an `agent-registry.md` row's certified date and revalidation date; run it
again, not a lighter version of it, at every revalidation.

## Machine-readable form

Each template is registered in `../toolkit.json` as `"kind": "template"`, with the same fields the
installed skills carry (role, the MEDIR step or part it grounds, and its path in this repository),
so an agent enumerating what this project offers sees these seven artefacts alongside the 38
installed skills, not as a separate, undiscoverable category.

## Honest limits

These are working templates, not software. Nothing here validates that you filled a field in
correctly, the way `execution-receipt.md`'s JSON shape does not enforce that a `cost` field holds a
real number rather than a guess. Adapt every field to your own context before using one of these on
real work; a template copied verbatim, unread, recreates the exact failure mode this whole project
argues against, an artefact mistaken for the judgement it is supposed to support.
