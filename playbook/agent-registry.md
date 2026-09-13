# Agent registry template

Grounded in: [Part 4](../harness-p4.html#en-lifecycle)'s life cycle (six states, not steps: briefing,
certified, in operation, under review, suspended, decommissioned) and the four roles (agent owner,
certifier, auditor, area sponsor). Part 4 states the sizing rule this template exists to honour
directly: "everything this part proposes has to work in a company with seven agents and a
spreadsheet. A registry is a table."

This answers the question Part 4 opens with: how many agents actually exist. Not how many were
approved, how many are actually running, with a name attached to each one. Part 4's own finding is
that almost nobody can answer this today: the market's own numbers on non-human identity generally
(824,000 orphaned accounts in one 2026 study, no HR-system owner but live entitlements) are what
happens when nobody keeps this table.

---

```
| Agent ID | Name | Briefing version | State        | Tier   | Agent owner | Certifier | Area sponsor | Certified date | Revalidation date | Last transition           | Next review trigger                     |
|----------|------|-------------------|--------------|--------|-------------|-----------|---------------|-----------------|---------------------|----------------------------|-------------------------------------------|
| <id>     | <name> | <version, see task-contract.md> | <see states below> | <N0-N3> | <named person, never a department> | <named person, cannot be the agent owner> | <named person> | <date> | <date, or 'event-triggered', see note> | <date + one-line reason> | <date, an event, or 'indicator firing'> |
```

## The six states (fill the "State" column with one of these, verbatim)

| State | Who decides | Has a validity date |
|---|---|---|
| Briefing | Requester and reviewer | Versioned |
| Certified | Certifier | Yes, with a revalidation date |
| In operation | Agent owner | Continuous |
| Under review | Auditor | Yes, a fixed window |
| Suspended | Certifier or auditor | Until decided |
| Decommissioned | Agent owner and certifier | Terminal |

## Rules this table exists to enforce

**The non-accumulation rule.** Agent owner and certifier can never be the same named person for the
same row. Auditor can never be the agent owner either. If two columns in one row ever name the same
person, that row is out of compliance with Part 4's own argument, not a formatting choice.

**The two transitions to decommissioned that almost nobody builds.** Part 4 names both explicitly,
and marks them as requiring a joint decision, never an automatic trigger:

1. **Certification expires without renewal.** The revalidation date passes with no recorded
   recertification. This is a signal to review, not a delete trigger on its own.
2. **No execution recorded for the whole review period.** An agent that has not run in the observed
   window. Part 4's own warning: finding a stale entry is the easy part, judging whether something
   still quietly depends on it is the hard part. Decommissioning requires the agent owner and
   certifier together, never a scheduled job acting alone.

**Prefer event-triggered revalidation over calendar-only, once volume justifies it.** Part 4's own
2026 finding: organisations relying only on quarterly certification keep discovering stale access
after the fact. Calendar-based revalidation (a fixed date) is the floor. Event-triggered
revalidation, an owner leaving, a scope changing, a credential expiring, is the target. Note which
one applies per row rather than assuming the calendar date is the only trigger that matters.

**This table is the answer to "how many agents actually exist."** If a row cannot be filled in
completely for an agent already running in production, that is itself the finding: an agent
operating without a named owner, a set tier, or a revalidation date is exactly the "dark matter of
identity" Part 4 describes, invisible to governance while active in the infrastructure.
