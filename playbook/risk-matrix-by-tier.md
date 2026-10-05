# Risk matrix by tier template

Grounded in: [Part 3](../harness-p3.html#en-separation)'s general matrix of authority (class of
action, reversibility, authority required), crossed with [Part 1](../harness-p1.html)'s autonomy
tiers N0 to N3. Part 3 states the organising criterion directly: authority is set by
reversibility, not by how important an action looks. A reversible action costs the price of undoing
it. An irreversible one costs the price of the mistake, however reliable the system appears.

This is the table someone approves and the system cannot rewrite, the same phrase Part 2's
business-unit example uses. It is not an instruction living inside a conversation.

Part 3's own seven rows are reproduced as the starting point, with three rows and two columns added
on 5 October 2026 (marked below as this project's own, not Part 3's). Add rows for your own action
classes, keep the columns, and never remove the last row: the rule of two overrides class-based
authority whenever an action would answer yes to all three of its questions (see
`execution-receipt.md`), regardless of what this table alone would otherwise allow.

---

```
| Class of action                                                  | Reversibility                | Authority required                                          | Tier that may execute it | Safe to retry?            | Survives bypass mode?       |
|------------------------------------------------------------------|------------------------------|-------------------------------------------------------------|---------------------------|----------------------------|------------------------------|
| Read or query internal data                                      | Reversible                   | None                                                         | N0 and above              | Yes                        | Not applicable, no approval  |
| Draft a communication, not sent                                  | Reversible                   | None                                                         | N0 and above              | Yes                        | Not applicable, no approval  |
| Send a routine communication with no commitment                  | Reversible                   | Free, logged                                                 | N1 and above              | Only with an operation key | Not applicable, no approval  |
| Send a communication that commits money, terms or policy         | Irreversible once received   | Named human approval, every time                             | N2 and above, gated       | No                         | Yes                          |
| Modify a financial or contractual record                         | Partially reversible         | Named approval, logged                                       | N2 and above, gated       | Only with an operation key | Yes                          |
| Delete a record or release a payment                             | Irreversible                 | Two named approvals, one independent of the requester        | N3 only, gated            | No                         | Yes                          |
| Change its own instructions, skills, memory or permissions (*)  | Partially reversible         | A person reads the change before it takes effect             | N2 and above, gated       | Only with an operation key | Yes                          |
| Publish to a shared repository or to production (*)              | Irreversible in practice     | Named human approval, every time                             | N3 only, gated            | No                         | Yes                          |
| Read credentials, environment files or folders outside scope (*) | Reversible, the exposure is not | Approval request every time, declined by default          | N2 and above, gated       | Yes                        | Yes                          |
| Any action answering yes to all three rule-of-two questions     | Depends on the class above   | Human in the loop, regardless of class                       | Overrides every row above | Depends on the class       | Yes                          |
| <your own row>                                                   | <reversible / partial / irreversible> | <who approves, and how many>                        | <N0-N3, gated or not>     | <yes / only with an operation key / no> | <yes / not applicable> |

(*) Added on 5 October 2026 by this project, not part of Part 3's seven rows.
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
5. **Safe to retry?** answers what a timeout does to this row. Some operations have the same effect
   whether they run once or five times; paying an invoice, e-mailing a customer or creating an order
   do not. For the second kind, the answer is "only with an operation key": a unique key the
   receiving system recognises, sent with the action and recorded in the receipt's
   `idempotency_key`. Automatic retry is decided per row, never as a default. The distinction is the
   one in IETF RFC 9110, section 9.2.2.
6. **Survives bypass mode?** asks whether the rule still binds when the runtime's approval prompts
   are switched off. A row that needs approval has to answer yes: the rule must live in policy the
   runtime enforces, with a floor beneath any bypass mode, not in a prompt a person can click away.
   The 2026 source-code study of eleven coding-agent systems recommends exactly this (Barbaste et
   al., arXiv:2609.00006, Recommendation 11), and describes one tool whose policy floor survives its
   most permissive mode (section 10.7).

**Run both nets, not one.** Part 3's own warning: the rule of two and the reversibility matrix are
two independent checks. A well-built policy layer runs both, because either one alone misses cases
the other catches. The last rule row above exists specifically to keep that from being forgotten.

**Approval is not containment.** The three rows added on 5 October 2026 are the ones an approval
prompt alone protects worst: a person who is asked to approve often will, and Anthropic reported in
May 2026 that users approved roughly 93% of permission prompts. Pair these rows with a limit on what
the agent can reach at all (the compact guide's containment entry), not only with a question.
