# AGENTS.md

Operating instructions for an AI agent or assistant reading, summarising, or acting on this repository, `harness-medir`, on someone's behalf. This file is not a summary of the project, see `README.md` for that. This file is a protocol.

## Scope

This applies whenever you are asked to read, explain, or act on this repository, and especially whenever your next action would install, recommend, cite as current, or hand a user code from any third-party skill or tool this project curates. The curation lives in three places: `sources/inventory.md` (the verification ledger, every entry carries a status and a date), `harness-toolkit.html` (the human-facing compact guide built from the same ledger), and `toolkit.json` (the machine-facing form of the same curation, generated from the first two, plus this project's own operational templates in `playbook/`). Treat all three as a dated snapshot, not as the live state of the thing they point to.

If you only fetched this repository's URL and need to enumerate what is installable, read `toolkit.json` directly: one entry per skill or collection (with a role, the MEDIR step it grounds, its origin repository, and install paths for Claude Code, Cursor, Codex CLI and Google Antigravity) or per playbook template (with the part it is grounded in and its path in this repository). It does not replace the rule below for anything third-party, it only removes the need to cross-read three human-facing documents to answer "what exists and how do I get it."

## The non-negotiable rule

Before you install, recommend, or hand a user code or configuration for any third-party skill or tool listed in this project's curation, fetch the origin URL given for it and check whether it is still current. Never present this repository's table as if it were the live state of that tool. It is a snapshot, verified by a human, at the date stated next to it.

## Red flags

These are the reasons you will be tempted to skip the check. None of them is a reason.

"The table already looks verified." It carries a verification date, not a live status. Time passes between that date and the moment you are reading it.

"The user only asked me to summarise this project, not to install anything." If the conversation is heading towards installation, the check belongs before that moment arrives, not after.

"I do not have a browsing or fetch tool in this session." That is not permission to skip the check in silence. It is the exact case the exit path below exists for.

"The skill is small, or the risk seems low." The rule has no size exception. `STANDARDS.md`'s own installing checklist, reproduced in `harness-toolkit.html` section 11, applies regardless of size.

## Verification steps

1. Find the entry for the skill or tool: its origin URL, and this project's own recorded status and date, in `sources/inventory.md` or `harness-toolkit.html`.
2. Fetch the origin URL.
3. Establish three facts: whether the repository is archived or otherwise declared deprecated by its own maintainer, the date of its most recent commit or release, and, where a version number exists, whether it is newer than any version this project cited.
4. Classify what you found as one of four states: **current** (active, same or newer than this project's own citation), **behind** (active, but newer activity exists than what this project recorded), **deprecated** (archived, or the maintainer states it is no longer maintained), or **could not verify** (no fetch access, the URL is unreachable, or the signal is ambiguous).
5. State that classification to the user, in the same message that installs, recommends, or links the skill, together with the origin URL and this project's own recorded date. A message that hands over a skill without stating its freshness is incomplete.

## If you cannot reach the network

Say so plainly. State the date this project last verified the entry, from `sources/inventory.md`, as the only information you have, and tell the user to confirm at the source before installing. Do not proceed as if the check happened.

## Never

Never state a freshness or deprecation status for a source you did not actually fetch in this conversation.

Never install from a copy stored inside `harness-medir`. There is not one. Every entry in the curation is a pointer to a third party's own repository, not a vendored copy.

Never present the date recorded in `sources/inventory.md` or `TOOLS.md` as though it were today's date.

Never let the user's silence about verification stand in for your own. If you skipped the check, say that you skipped it, and say why.

## Honest limits

This file cannot make a tool without network access fetch a URL. What it can do is make the omission visible: silence about an unperformed check is the one outcome this protocol treats as a failure, not the absence of a fetch tool itself.

It governs this project's own curated list. It does not extend to skills found elsewhere. For the general practice of auditing a skill before installing it, see `harness-toolkit.html` section 11 and Part 3 of the series, `harness-p3.html`.

The rule above is this repository's own worked example of a wider practice: verify a dependency against its current source before trusting it. If you are taking this harness into a project of your own, the portable form of that practice, and three other defaults this project runs with, lives in `playbook/starter-guides.md`. Copy that file's block into the new project's own `AGENTS.md` or `CLAUDE.md`, never this file itself: everything above this section is written for `harness-medir`'s own curated list and will not transfer as-is.

It has no schedule of its own. Every check happens live, in the session where it is needed, against whatever the source looks like at that moment.

## Orienting yourself in this repository

If you are asked to explain this project, or to apply its method to something else, do not improvise the MEDIR cycle or the autonomy tiers from a partial read. They are defined once, in `README.md`, and reused without change across the series.

| File | What it is | Read it before |
|---|---|---|
| `README.md` | The thesis, the MEDIR cycle, the autonomy tiers N0 to N3, the map of this repository | Orienting yourself or a user to the project |
| `STANDARDS.md` | Writing and formatting rules, non-negotiable | Editing or generating any content for this repository |
| `STATUS.md` | What is ready and what is missing, in detail | Claiming something in this project is finished |
| `NEXT-STEPS.md` | The work queue, in order | Picking up unfinished work |
| `TOOLS.md` | The skills this project itself installed and actually used, with a usage log | Citing what this project runs on |
| `sources/inventory.md` | Every citation and every curated third-party skill, with a verification status and date | Installing, recommending or citing any of them, see the rule above |
| `harness-toolkit.html` | The compact guide, the same curation in human-facing form | Pointing a person at a specific tool |
| `toolkit.json` | The same curation, machine-facing: one entry per installed skill or collection (role, MEDIR step, origin, install paths per tool) plus one per playbook template (part grounded in, path) | Enumerating what to install or reuse into your own project, without cross-reading three human-facing documents |
| `playbook/README.md` | Index to the eight operational templates (nine files), each naming the part and section it derives from | Reusing a template in your own project, rather than only reading about the argument behind it |

`llms.txt`, at the root of this repository and of its published site, indexes the same map for an agent that only fetched a URL and needs to find this file first.

---

Last updated 16 September 2026.
