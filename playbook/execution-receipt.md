# Execution receipt template

Grounded in: the base receipt [Part 2](../harness-p2.html#en-exemplos) introduces ("a compact record
of what produced a result: contract, sources, sensors, attempts, cost and approval"), extended in
[Part 3](../harness-p3.html#en-separation) with the rule-of-two answers and the reversal point. Both
versions are real, working JSON from the articles, reproduced here as a single template that carries
every field either one used, so a project can adopt whichever subset its own risk actually requires.

The point of a receipt, stated in both parts: it answers, with no investigation needed, what an
incident review always asks first. Part 2's version answers five questions (task, information used,
what was checked, attempts, who authorised). Part 3's extension adds what a real incident review
needs when the action had external effect: why it was flagged, what the decision was, how long the
record has to survive.

**The one rule that matters more than any field:** log the reversal point *before* the tool
executes, not after. Part 3 states this as the single most common mistake, because a reversal point
logged afterwards describes a world that no longer exists.

---

```json
{
  "run": "<ISO-8601 timestamp, when this run started>",
  "task": "<task or skill name>",
  "contract": "<task-contract identifier and version, e.g. tier-1-response@v3>",
  "action_class": "<from risk-matrix-by-tier.md, e.g. external-communication>",
  "reversible": "<true, false, or 'partial', from risk-matrix-by-tier.md>",
  "sources_consulted": ["<every source of record this run actually used>"],
  "sensors": {
    "<sensor name>": "<ok, or the exact gap it found>"
  },
  "rule_of_two": {
    "private_data": "<true/false>",
    "untrusted_content": "<true/false>",
    "external_communication": "<true/false>",
    "answers_yes": "<count of the three above that are true>"
  },
  "gate": "<'none' if answers_yes is 2 or fewer, otherwise 'human-in-the-loop'>",
  "reversal_point_logged_at": "<timestamp, logged BEFORE execution, not after>",
  "attempts": "<count>",
  "cost": "<real cost, not an estimate>",
  "approved_by": "<named approver, or null>",
  "declined_by": "<named decliner and timestamp, or null>",
  "decline_reason": "<if declined, why, in enough detail to reconstruct the decision>",
  "rollback_point": "<the identifier or state to roll back to, if reversible>",
  "retention_until": "<minimum six months for anything touching an external effect,
    see Part 3 section 8 for the legal grounding in Brazil and Europe>"
}
```

## Field notes

**`rule_of_two`** exists because of Part 3's own rule: without a human in the loop, an agent may
satisfy at most two of the three questions. The moment all three are true, `gate` must read
`human-in-the-loop`, no exception for urgency or inconvenience.

**`sensors`** is a map, not a list, because Part 2's own guidance on a good sensor applies here too:
record the exact gap, not just a pass or fail verdict, so the receipt itself teaches the next run
something a bare "ok" cannot.

**Not every run needs every field.** A low-risk, fully reversible task (Part 2's individual
contract-review example) needs contract, sources, sensors and attempts. It does not need
`rule_of_two` or `reversal_point_logged_at`, because nothing about it has external effect. Add the
extended fields once an action could answer yes to any rule-of-two question, not before: an unused
field nobody fills in correctly is worse than a shorter, honest receipt.

**Telemetry standard, if you export this at scale:** the OpenTelemetry semantic conventions for
generative AI, open and vendor-neutral, with growing adoption among agent runtimes (Part 3, section
on the record). This template's field names do not need to match OTel's attribute names one for one;
what matters is that the underlying data (model, tokens, tool calls, outcome) is exportable to it,
so an audit does not become captive to one vendor's proprietary log format.
