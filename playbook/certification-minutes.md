# Certification meeting minutes template

Grounded in: [Part 4](../harness-p4.html#en-lifecycle)'s certified state and the certifier role.
Part 4's own sizing rule names the format directly: "certification is a meeting with minutes." This
formalises the certifier's act, the moment an agent moves from briefing to certified in
`agent-registry.md`, into a record that survives the meeting.

An agent certified with no minutes is a verbal decision nobody can reconstruct later. Part 3's own
argument for a receipt applies here on the organisational plane: the whole exchange, proposal,
review, decision and reason, should take minutes to reconstruct, not a week, because it was written
down as it happened.

---

```
CERTIFICATION MEETING MINUTES

Agent ID: <see agent-registry.md>
Briefing version reviewed: <version>
Date: <date>

Attendees and roles:
  Requester:      <named person>
  Reviewer:       <named person>
  Certifier:      <named person, cannot also be the agent owner below>
  Agent owner:    <named person, cannot also be the certifier above>
  Area sponsor:   <named person, if the briefing's promised return is being confirmed here>

Reviewed against:
  [ ] Task contract complete (task-contract.md)
  [ ] Tier diagnostic run, gaps named (tier-diagnostic.md)
  [ ] Risk matrix by tier reviewed for this agent's action classes (risk-matrix-by-tier.md)
  [ ] Rule-of-two exposure assessed for this agent's likely actions (execution-receipt.md)
  [ ] Rollback and reversal-point mechanism confirmed working, if tier is N2 or above
      (rollout-path.md)

Tier granted: <N0 / N1 / N2 / N3>
Rationale: <one or two sentences, tied to the diagnostic and risk matrix above, not to
  confidence in the model>

Revalidation:
  Date: <date, the floor>
  Event triggers (if any, see agent-registry.md): <owner change, scope change,
    credential expiry, or 'calendar only'>

Decision: <CERTIFIED / NOT CERTIFIED / CERTIFIED WITH CONDITIONS>
Conditions, if any: <named, checkable, with an owner and a date>

Signed:
  Certifier: <name, date>
  Agent owner: <name, date, acknowledging the conditions above>
```

## Notes before you run one of these

**Do not skip a "not certified" outcome.** Part 4's own opening case (the automation at N0 operating
as if it were N3) happened because no meeting like this one ever occurred. A short, honest "not
certified, here is what is missing" minute is the artefact that would have caught it.

**File this alongside the agent's row in `agent-registry.md`,** not in a separate system nobody
checks at revalidation. The registry's "Certified date" and "Revalidation date" columns should point
back to the specific minutes that set them.

**Recertification uses the same template.** Part 4's own critique of one-time certification: nobody
asks the agent to prove, months later, that the reasons it was approved still hold. Run this again
at the revalidation date, not a lighter version of it.
