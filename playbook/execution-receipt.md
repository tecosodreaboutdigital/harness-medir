# Execution receipt template

Grounded in: the base receipt [Part 2](../harness-p2.html#en-exemplos) introduces ("a compact record
of what produced a result: contract, sources, sensors, attempts, cost and approval"), extended in
[Part 3](../harness-p3.html#en-separation) with the rule-of-two answers and the reversal point. Both
versions are real, working JSON from the articles, reproduced here as a single template that carries
every field either one used, so a project can adopt whichever subset its own risk actually requires.
Revised on 5 October 2026 with thirteen fields the 2026 reading added; they are marked in the table
below and sorted by tier in the field notes.

The point of a receipt, stated in both parts: it answers, with no investigation needed, what an
incident review always asks first. Part 2's version answers five questions (task, information used,
what was checked, attempts, who authorised). Part 3's extension adds what a real incident review
needs when the action had external effect: why it was flagged, what the decision was, how long the
record has to survive. The 2026 fields add three more: which model and harness produced the result,
how the run ended, and whether an action that could not be repeated safely was repeated.

**The one rule that matters more than any field:** log the reversal point *before* the tool
executes, not after. Part 3 states this as the single most common mistake, because a reversal point
logged afterwards describes a world that no longer exists.

---

```json
{
  "run": "<ISO-8601 timestamp, when this run started>",
  "task": "<task or skill name>",
  "contract": "<task-contract identifier and version, e.g. tier-1-response@v3>",
  "model": "<model identifier and version>",
  "harness": "<harness name and version>",
  "config_hash": "<hash of the instructions, skills and policy in force for this run>",
  "policy_version": "<version of the authority matrix that applied, from risk-matrix-by-tier.md>",
  "action_class": "<from risk-matrix-by-tier.md, e.g. external-communication>",
  "reversible": "<true, false, or 'partial', from risk-matrix-by-tier.md>",
  "sources_consulted": [
    {
      "source": "<every source of record this run actually used>",
      "trust": "<system, internal or external_untrusted>"
    }
  ],
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
  "idempotency_key": "<unique key sent with any action that is not safe to repeat, or null>",
  "action_stage": "<requested, executed, observed or committed: the last moment this record reached>",
  "reversal_point_logged_at": "<timestamp, logged BEFORE execution, not after>",
  "reversal_scope": "<files, conversation or none_external: what a rewind can and cannot undo>",
  "attempts": "<count>",
  "exit_reason": "<completed, policy_block, timeout, budget_exhausted, failed or handed_to_human>",
  "failure_class": "<one of the classes in tier-diagnostic.md, or null when the run completed>",
  "budget": {
    "limits": "<steps, tokens, time, cost, tool calls and workers allowed for this run>",
    "used": "<the same six, as actually spent>"
  },
  "tokens": {
    "input": "<count>",
    "output": "<count>",
    "cache_read": "<count>",
    "cache_write": "<count>",
    "subagents": {"count": "<how many were started>", "tokens": "<total they used>"}
  },
  "cost": "<real cost, not an estimate>",
  "approved_by": "<named approver, or null>",
  "declined_by": "<named decliner and timestamp, or null>",
  "decline_reason": "<if declined, why, in enough detail to reconstruct the decision>",
  "rollback_point": "<the identifier or state to roll back to, if reversible>",
  "redactions": ["<what was left out of this record as secret or personal data>"],
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

**`sources_consulted` changed shape on 5 October 2026**, from a list of strings to a list of objects
that carry a `trust` level. Text the agent reads can carry instructions it will follow; the receipt
has to say which of its sources could have. Receipts written to the earlier shape stay valid: read a
bare string as `{"source": <the string>, "trust": "unknown"}`.

**`exit_reason` is not a success flag.** A run can end because the work is done, because a policy
blocked it, because time or budget ran out, because it failed, or because it was handed to a person.
Collapsing the six into one word, done, is how a dashboard ends up green while the work is not.
Reaching the step limit is not finishing the task.

**Which fields at which tier.** Not every run needs every field, and an unused field nobody fills in
correctly is worse than a shorter, honest receipt.

| Tier | Required | Add at this tier |
|---|---|---|
| N1 | `run`, `task`, `contract`, `sources_consulted`, `sensors`, `attempts`, `cost` | `model`, `exit_reason` |
| N2 | all of N1 | `harness`, `config_hash`, `budget`, `tokens`, `failure_class` |
| N3 | all of N2 | `action_class`, `reversible`, `rule_of_two`, `gate`, `policy_version`, `idempotency_key`, `action_stage`, `reversal_point_logged_at`, `reversal_scope`, `rollback_point`, `trust` on every source, `redactions`, `retention_until`, `approved_by` or `declined_by` |

A low-risk, fully reversible task (Part 2's individual contract-review example) needs the N1 row and
nothing more, because nothing about it has external effect. Move a field up a tier only when an
action could answer yes to a rule-of-two question, not before.

## Why the 2026 fields exist

| Field | Why | Source |
|---|---|---|
| `model`, `harness`, `config_hash` | A change in behaviour cannot be attributed without them. In April 2026 Anthropic traced weeks of degraded quality in its own coding agent to three product changes while stating the API was not impacted | Anthropic, "An update on recent Claude Code quality reports", 23 April 2026 |
| `policy_version` | Which rule authorised the action. Safety rules kept as data or policy files, with a floor beneath any bypass mode, are what the 2026 source-code study recommends for every tier | Barbaste et al., arXiv:2609.00006, Recommendation 11 |
| `exit_reason` | Ending is not finishing. One tool in the study enumerates eleven turn-exit reasons | Same study, section 6.2 |
| `budget`, `tokens` | The six limits of Part 2, and the cache split that cost per completed task needs | The project's own price ledger (`docs/assets/prices.json`) prices cache reads and 5-minute and 1-hour writes separately |
| `idempotency_key`, `action_stage` | An action that is not safe to repeat needs a unique key the receiving system recognises, and the record has to say which of the four moments (requested, executed, observed, committed) it reached, so a retry after a timeout does not pay twice | IETF RFC 9110, section 9.2.2, Idempotent Methods |
| `reversal_scope` | What a rewind can and cannot undo. One tool in the study checkpoints per message and can restore files, which does not undo anything outside them | Same study, Mistral Vibe's rewind manager |
| `sources_consulted[].trust` | Provenance: tool results can carry hostile instructions | Debenedetti et al., AgentDojo, 629 security test cases |
| `failure_class` | Failures become countable | The 13 classes in `tier-diagnostic.md` |
| `redactions` | Auditable and compatible with data-protection law at the same time | Part 3, section 8, on the legal grounding in Brazil and Europe |

**Telemetry standard, if you export this at scale:** the OpenTelemetry semantic conventions for
generative AI, open and vendor-neutral, with growing adoption among agent runtimes (Part 3, section
on the record). This template's field names do not need to match OTel's attribute names one for one;
what matters is that the underlying data (model, tokens, tool calls, outcome) is exportable to it,
so an audit does not become captive to one vendor's proprietary log format.
