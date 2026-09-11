*Read this in [Português](TOOLS.pt.md) · [Español](TOOLS.es.md).*

# Tools and skills used on this project

A record of what this project has actually installed and uses, not just what it cites. A project about harness engineering that did not instrument its own creation would just be a nice-sounding argument. This document is the instrumentation.

Updated 10 September 2026. It grows with every new skill that enters use, it is never rewritten wholesale.

---

## Third-party collections installed

Ten collections, thirty-seven skills, all MIT or Apache-2.0. Installed locally in `.claude/skills/`, outside version control (see `.gitignore`): they run in this environment, but the third-party code does not enter this repository's public history. The first six are cited as an entry in the [compact guide](harness-toolkit.html); the four most recent are not yet, see the note at the end of this section. Add `intake-briefing`, the project's own skill covered in the next section, and the environment has 38 active skills in total.

| Collection | Origin | Skills installed | Why it made the cut |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, the whole collection | It is the non-negotiable-rule-plus-red-flags pattern that `STANDARDS.md` already adopts as this project's skill-writing standard |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, curated selection | Writing, clarification and session-handoff skills. The collection's software-engineering set (TDD, code architecture, merge conflicts, TypeScript) was left out as not applicable to a content project, see the full list below |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, the whole collection | The C4 model and architecture decision records, relevant to the Part 3 research round |
| Karpathy-inspired guide | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | A behavioural guide against common LLM mistakes. Not actually by Karpathy, see the full caveat in `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | The real source of the five-rule cleanup matrix cited in Part 2's Reinforce section |
| impeccable | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1 | Design-QA reference for the project's own HTML pages: 61 deterministic detector rules for common AI-generated frontend tells, Apache-2.0, 30 contributors. Installed as documentation only, see the caveat below |
| humanizer | [github.com/blader/humanizer](https://github.com/blader/humanizer) | 1, the whole collection | Strips AI-sounding prose patterns from an English draft before it branches into Portuguese and Spanish. None of the other nine collections on this page reaches that level of detail, phrase and paragraph shape, not vocabulary. Added 10 September 2026 from a reader-submitted list of candidate skills |
| Agent Skills for Context Engineering | [github.com/muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 3, out of 17 | A reader flagged agent-harness architecture as a real gap in this page. `harness-engineering`, `multi-agent-patterns` and `tool-design` close it directly; the other 14 skills (context optimisation, memory systems, evaluation and more) address adjacent problems this project does not have, see the full list below |
| ai-act-skill | [github.com/morellid/ai-act-skill](https://github.com/morellid/ai-act-skill) | 1, the whole collection | A versioned, task-by-task checklist for EU AI Act obligations, already current with the Digital Omnibus (Regulation (EU) 2026/1744). Part 3 and 4 already cite Articles 12, 14 and 26 in prose; this is the first tool in this project's own toolkit that turns that citation into a runnable check |
| threat-modeling | [github.com/rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | 1, out of a larger personal collection | STRIDE-based threat modelling scoped to agent architecture and security review, not per-change diff review. Scoped install: only the one skill folder came in, not the rest of the repository |

---

## The thirty-seven skills, by collection

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (the origin folder calls this skill `c4designer`, but `SKILL.md`'s own internal header declares the name `c4-model`; we renamed the local folder to match the declared name).

**Karpathy-inspired guide:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

**impeccable:** impeccable. **Scoped install, stated honestly:** we copied `SKILL.md` and every file under `reference/`, nothing under `scripts/`. The upstream skill's own frontmatter lists `Bash(npx impeccable *)` and `Bash(node .../scripts/*)` as its allowed tools, wired to 61 deterministic detector rules that need those scripts to run without an LLM. Without them, `/impeccable audit` and its siblings still work as LLM-guided critique against the same written rules, just without the no-LLM deterministic pass. Every other skill in the first six collections is markdown-only by nature; impeccable is the first one where we chose to leave code behind on purpose, precisely because the compact guide's own "before installing anything" checklist (see below) treats an unreviewed script that shells out as a real cost, not a free upgrade.

**humanizer:** humanizer.

**Agent Skills for Context Engineering:** harness-engineering, multi-agent-patterns, tool-design. **Scoped install, stated honestly:** the upstream collection has 17 skills; we copied only these three folders (`SKILL.md` plus their own `references/` and `scripts/`), because the other 14 (context-fundamentals, memory-systems, evaluation, self-improvement-loops and more) solve problems this project does not have. `multi-agent-patterns` and `tool-design` each carry a small local Python helper (`coordination.py`, `description_generator.py`); both are standard-library only, audited below.

**ai-act-skill:** ai-act-skill. Full install: `SKILL.md`, the six task files under `tasks/`, and the reference extracts and worked examples that back them. The upstream repository's own `install.sh`, `uninstall.sh`, release scripts and cross-tool adapters were left out, they serve the author's packaging process, not this skill's function inside this environment.

**threat-modeling:** threat-modeling. **Scoped install, stated honestly:** this skill lives inside `rjmurillo/ai-agents`, a much larger personal collection; only the `threat-modeling` folder (`SKILL.md`, `references/`, `scripts/`, `templates/`) was copied. The three bundled scripts (`generate_threat_matrix.py`, `generate_mitigation_roadmap.py`, `validate_threat_model.py`) are standard-library only, audited below.

---

## The project's own skill

`intake-briefing` is not installed from a third party, it is created by this project. It lived as a subfolder in here until 30 August 2026, when it gained its own public, MIT repository the same day: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renamed from `levantando-briefing` later that same day, as part of the English-primary restructuring). harness-medir no longer holds its content, only points to it, the same pattern it uses to point at the other collections on this page.

It also was not active in this environment until this round: `.claude/skills/`, which is where this harness discovers project skills, only had the thirty third-party ones. Fixed: a copy of it lives at `.claude/skills/intake-briefing/`, outside version control, pulled from its own repository.

**Risk accepted, stated honestly:** this local copy can fall behind if the skill's repository is edited without updating the copy here. It is the same kind of risk we accept for the thirty-seven third-party skills, now also for our own. It already happened once: the repository gained `AGENTS.md`, `llms.txt`, `.claude-plugin/` and `briefings/`, plus a rewritten multi-tool `Installation` section, on 31 August 2026, while this local copy still held the 30 August snapshot. Resynced the same day; see `README.md`'s own `Installation` section for the multi-tool detail that came out of that round.

---

## Audit before installing

We applied the compact guide's own checklist, the "Before installing anything" section: read the content, look for an instruction telling the system to fetch something from an external network, check the licence before deciding.

A scan for network or execution patterns (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) across the five sources found no automatic external-fetch instruction. The only hits were a didactic code example (a mocked `fetch` in a mattpocock/skills test skill) and legitimate local execution (superpowers' `execFileSync`, to render a Mermaid diagram to SVG, no network involved). None of the five sources required an undeclared external dependency to function as a standalone skill.

impeccable was audited separately, because its full repository is a different shape: an npm CLI plus browser-injected detector scripts, not a plain markdown skill. We read the `scripts/` tree before deciding, rather than running `npx impeccable install` first and reading afterward. It shells out to Node and, for the visual detector, a headless browser, both declared openly in `SKILL.md`'s own `allowed-tools`, not hidden. We chose not to install any of it: the copy in `.claude/skills/impeccable/` is `SKILL.md` and `reference/` only, see the caveat in the collection table above.

**Second audit round, 10 September 2026.** A reader sent a list of eight candidate skill repositories and asked for a comparison against this page, plus a search for anything this project was missing on software architecture, data privacy and information security. Five background agents read each candidate directly (raw file content, not marketing README) and cross-checked it against what was already installed here. Two of the eight turned out to already be covered: the karpathy-inspired guide was already this exact source, and a UI-design skill in the list matched something already active globally on the operator's machine but out of scope for this project. Four were read and set aside as citation-only or a poor fit, including one, Understand-Anything, that installs itself with a `curl | bash` one-liner and ships a hook whose own instructions tell the agent not to ask the user for confirmation before acting, exactly the pattern this checklist exists to catch. The remaining four, humanizer, three skills out of Agent Skills for Context Engineering, ai-act-skill and threat-modeling, passed the same scan run on the first round (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`, plus `requests`, `urllib`, `subprocess` and `os.system` for the three sources that ship Python). The scan found one match: `sandbox.exec()` inside a case-study code sample in `tool-design`'s `references/architectural_reduction.md`, quoting a third party's own sandboxed benchmark, not an instruction this skill executes. No source in this round required an undeclared network call to function.

**Citation in the compact guide is pending for these four.** The first six collections were installed and cited in `harness-toolkit.html` in the same sitting; this round deliberately separated the two steps so the operator could decide on installation first. Writing the six-field entries, in three languages, and syncing the `build/` mirror is tracked as its own next step, not silently assumed done.

---

## A note on the environment

Two of these collections, superpowers and the Karpathy-inspired guide, were already globally available in this environment before this installation, likely via a plugin already configured on the machine. We installed the project's local copy anyway, on purpose: the goal is for this project's work to stay reproducible on any machine that clones the repository and installs the same skills, without depending on what is configured globally on one specific machine.

---

## Real usage log

This section is what separates "installed" from "used", and it is the one that will grow the most. Every entry names the skill, the artefact it helped produce, and the date.

*No usage logged for the first day beyond the installation itself, done on 30 August 2026. All of this project's work up to that point (the repository, the compact guide rewrite, Part 2's translation, the English-primary restructuring across both repositories) was done with the harness's native tools, without any of these thirty skills.*

**`research`, 31 August 2026.** Used directly, repeatedly, at real scale, across the day's two rounds of citation correction and the later adversarial research pass on Parts 3 and 4: researching a claim against real primary sources and saving the findings as a markdown file, rather than a chat summary that disappears when the session ends. It held up well every time, consistently well-sourced output, saved to a sensible location. One real inefficiency logged rather than hidden: its own instruction to spin up a background agent adds one redundant layer of delegation when it is invoked from a call that is already a background agent. Now cited on its own in the compact guide's Inspect section, closing the gap `NEXT-STEPS.md`'s item 4 named: installed and audited at the collection level is not the same claim as individually verified and cited.

---

## Where this shows up

Footer of `harness-p1.html`, `harness-p2.html` and `harness-toolkit.html`, in all three languages where the piece is trilingual. And in the [project log](docs/logbook.html), trilingual, with the per-milestone detail, generated from git and the session's real usage log, never edited by hand.
