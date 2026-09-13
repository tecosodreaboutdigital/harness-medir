# Risk matrix by tier template

Grounded in: [Part 3](../harness-p3.html#en-separation)'s general matrix of authority (class of
action, reversibility, authority required), crossed with [Part 1](../harness-p1.html)'s autonomy
tiers N0 to N3. Part 3 states the organising criterion directly: authority is set by
reversibility, not by how important an action looks. A reversible action costs the price of undoing
it. An irreversible one costs the price of the mistake, however reliable the system appears.

This is the table someone approves and the system cannot rewrite, the same phrase Part 2's
business-unit example uses. It is not an instruction living inside a conversation.

Part 3's own seven rows, reproduced as the starting point. Add rows for your own action classes,
keep the three columns, and never remove the last row: the rule of two overrides class-based
authority whenever an action would answer yes to all three of its questions (see
`execution-receipt.md`), regardless of what this table alone would otherwise allow.

---

```
| Class of action                                                | Reversibility            | Authority required                                        | Tier that may execute it |
|-----------------------------------------------------------------|--------------------------|------------------------------------------------------------|---------------------------|
| Read or query internal data                                     | Reversible               | None                                                         | N0 and above              |
| Draft a communication, not sent                                 | Reversible               | None                                                         | N0 and above              |
| Send a routine communication with no commitment                 | Reversible               | Free, logged                                                 | N1 and above              |
| Send a communication that commits money, terms or policy         | Irreversible once received | Named human approval, every time                            | N2 and above, gated       |
| Modify a financial or contractual record                        | Partially reversible     | Named approval, logged                                       | N2 and above, gated       |
| Delete a record or release a payment                             | Irreversible             | Two named approvals, one independent of the requester        | N3 only, gated            |
| Any action answering yes to all three rule-of-two questions      | Depends on the class above | Human in the loop, regardless of class                       | Overrides every row above |
| <your own row>                                                   | <reversible / partial / irreversible> | <who approves, and how many> | <N0-N3, gated or not>    |
```

## How to fill your own rows

1. Name the action class the way a person would describe it to a colleague, not the way a system
   logs it. "Grant a discount or credit" reads better than "POST /discounts".
2. Reversibility first, before authority. Part 3's own finding: a mis-classified action class is
   sometimes still caught correctly if reversibility is judged honestly, so get this column right
   even when the class name is ambiguous.
3. Authority required states who, named, not a role that could be anyone on a given day. "Named
   approval" means a specific person is identified in the receipt (`execution-receipt.md`'s
   `approved_by` field), not that a category of person exists somewhere in the org chart.
4. The tier column is this project's own addition, not lifted verbatim from either part: it answers
   the practical question a rollout actually asks, which tier is allowed to attempt this action class
   at all, gated or not. See `rollout-path.md` for what "gated" requires before granting it.

**Run both nets, not one.** Part 3's own warning: the rule of two and the reversibility matrix are
two independent checks. A well-built policy layer runs both, because either one alone misses cases
the other catches. The last row above exists specifically to keep that from being forgotten.
