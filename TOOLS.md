*Read this in [Português](TOOLS.pt.md) · [Español](TOOLS.es.md).*

# Tools and skills used on this project

A record of what this project has actually installed and uses, not just what it cites. A project about harness engineering that did not instrument its own creation would just be a nice-sounding argument. This document is the instrumentation.

Updated 30 August 2026. It grows with every new skill that enters use, it is never rewritten wholesale.

---

## Third-party collections installed

Five collections, thirty skills, all MIT-licensed. Installed locally in `.claude/skills/`, outside version control (see `.gitignore`): they run in this environment, but the third-party code does not enter this repository's public history. Each is cited as an entry in the [compact guide](harness-toolkit.html). Add `intake-briefing`, the project's own skill covered in the next section, and the environment has 31 active skills in total.

| Collection | Origin | Skills installed | Why it made the cut |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, the whole collection | It is the non-negotiable-rule-plus-red-flags pattern that `STANDARDS.md` already adopts as this project's skill-writing standard |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, curated selection | Writing, clarification and session-handoff skills. The collection's software-engineering set (TDD, code architecture, merge conflicts, TypeScript) was left out as not applicable to a content project, see the full list below |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, the whole collection | The C4 model and architecture decision records, relevant to the Part 3 research round |
| Karpathy-inspired guide | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | A behavioural guide against common LLM mistakes. Not actually by Karpathy, see the full caveat in `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | The real source of the five-rule cleanup matrix cited in Part 2's Reinforce section |

---

## The thirty skills, by collection

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (the origin folder calls this skill `c4designer`, but `SKILL.md`'s own internal header declares the name `c4-model`; we renamed the local folder to match the declared name).

**Karpathy-inspired guide:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

---

## The project's own skill

`intake-briefing` is not installed from a third party, it is created by this project. It lived as a subfolder in here until 30 August 2026, when it gained its own public, MIT repository the same day: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renamed from `levantando-briefing` later that same day, as part of the English-primary restructuring). harness-medir no longer holds its content, only points to it, the same pattern it uses to point at the other five collections on this page.

It also was not active in this environment until this round: `.claude/skills/`, which is where this harness discovers project skills, only had the thirty third-party ones. Fixed: a copy of it lives at `.claude/skills/intake-briefing/`, outside version control, pulled from its own repository.

**Risk accepted, stated honestly:** this local copy can fall behind if the skill's repository is edited without updating the copy here. It is the same kind of risk we accept for the thirty third-party skills, now also for our own.

---

## Audit before installing

We applied the compact guide's own checklist, the "Before installing anything" section: read the content, look for an instruction telling the system to fetch something from an external network, check the licence before deciding.

A scan for network or execution patterns (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) across the five sources found no automatic external-fetch instruction. The only hits were a didactic code example (a mocked `fetch` in a mattpocock/skills test skill) and legitimate local execution (superpowers' `execFileSync`, to render a Mermaid diagram to SVG, no network involved). None of the five sources required an undeclared external dependency to function as a standalone skill.

---

## A note on the environment

Two of these collections, superpowers and the Karpathy-inspired guide, were already globally available in this environment before this installation, likely via a plugin already configured on the machine. We installed the project's local copy anyway, on purpose: the goal is for this project's work to stay reproducible on any machine that clones the repository and installs the same thirty skills, without depending on what is configured globally on one specific machine.

---

## Real usage log

This section is what separates "installed" from "used", and it is the one that will grow the most. Every entry names the skill, the artefact it helped produce, and the date.

*No usage logged yet beyond the installation itself, done on 30 August 2026. All of this project's work up to that point (the repository, the compact guide rewrite, Part 2's translation, the English-primary restructuring across both repositories) was done with the harness's native tools, without any of these thirty skills. From here on, every real use enters this log before being claimed in any article.*

---

## Where this shows up

Footer of `harness-p1.html`, `harness-p2.html` and `harness-toolkit.html`, in all three languages where the piece is trilingual. And in the [project log](docs/logbook.html), trilingual, with the per-milestone detail, generated from git and the session's real usage log, never edited by hand.
