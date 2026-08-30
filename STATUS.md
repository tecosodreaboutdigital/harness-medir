*Read this in [Português](STATUS.pt.md) · [Español](STATUS.es.md).*

# Status

Situation as of 30 August 2026.

Published at `github.com/tecosodreaboutdigital/harness-medir` (repository) and `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, the HTML files render as pages, not just as source code).

---

## Ready

### English-primary restructuring

English became this project's primary production language for both public repositories on 30 August 2026, decided partway through what had been a Portuguese-first project. Every governance document, the compact guide and the briefing skill were renamed and rewritten English-first, with Portuguese and Spanish as full translations rather than the other way round. See the `Languages` section of `STANDARDS.md` for the rule itself.

Mechanically: `PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`, `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, plus the corresponding `build/` scripts and data files. Every cross-reference across both repositories was swept and fixed, including the absolute GitHub blob URLs pointing at the old governance filenames and the language-prefixed anchors linking Part 2 into the compact guide. Historical commit descriptions inside the project log were deliberately left naming the old filenames where that is what was literally true at the time of that commit, with a note added where the later rename needed acknowledging, so the log stays a faithful record rather than a retroactively tidied one.

The already-complete trilingual pieces (`harness-p1.html`, `harness-p2.html`, `docs/logbook.html`) had their default tab flipped from Portuguese to English: the `<html lang>` attribute, the active langbar button and which `<main>` is hidden all moved, both in the built files and in the build scripts that regenerate them, so a rebuild does not silently revert to the Portuguese default.

A browser-language hint was added to all four trilingual HTML pages: if the visitor's browser language is Portuguese or Spanish and does not already match the active tab, and no explicit language-prefixed link is routing the page, a small dismissible banner offers to switch, worded in that language. Any other browser language falls back to English with no banner. GitHub does not execute JavaScript inside rendered Markdown, so the skill repository's twelve files instead carry a static language-navigation line at the top of each.

### Project log

`docs/logbook.html`, trilingual. Documents the project's own evolution: words published and tokens consumed per milestone, generated from git and the real session transcript, never written by hand. See `build/generate_logbook_metrics.py` and `build/build_logbook.py`. Six milestones recorded so far from the repository's full history, plus whatever is still in the open session.

### Part 1 · The best model in the world inside a company with no process

`harness-p1.html`

Fully trilingual, thirteen sections plus the navigation block, three diagrams, 26 glossary entries. About 4,700 words in Portuguese, 4,500 in English, 4,700 in Spanish.

Content: an opening scene with the director, what a harness is, the delegation analogy, the historical lineage with a correction to the term's attribution, four case studies with numbers, the MEDIR cycle, the equivalence table against quality vocabulary, tiers N0 to N3, board-level risks, a twelve-question checklist.

Series bar and "Where you are" block already implemented.

### Part 2 · Guides and sensors: how an agent learns to correct itself

`harness-p2.html`

Fully trilingual since 30 August 2026. Seventeen sections, three diagrams, 26 glossary entries per language. About 6,200 words in Portuguese, 6,350 in English, 6,450 in Spanish.

Completely rewritten after a discarded first version. The discarded version failed by dropping the character, not carrying Part 1's history forward, and organising by concept instead of by the cycle.

Content: opens in week four with the director having written the whole guide and the system releasing an invoice from a de-accredited supplier. Sections anchored on Equip, Delegate and Inspect, with Reinforce at the end. Includes the guides-and-sensors matrix, the comparison between an error message that teaches and an alarm, the threshold trick, the durability unit, three full examples with a real SKILL.md, environment classes crossed with tiers, and cleanup as cadence.

English translation in British spelling, Spanish by "tú". MEDIR and harness kept as proper nouns in all three languages, per `STANDARDS.md`. The skill examples (file names, fields, values) were translated too, not just the surrounding prose.

The language-switching JavaScript in Part 1 and Part 2 gained anchor-based routing: a link like `harness-p1.html#en-opening` now selects the correct tab before scrolling, instead of always opening on the default tab. Without that fix, a reader in English clicking any cross-reference into Part 1 always landed in Portuguese.

### Skill intake-briefing

`github.com/tecosodreaboutdigital/intake-briefing`, its own repository since 30 August 2026, renamed from `levantando-briefing` that same day as part of the English-primary restructuring ("levantando" was a plain Portuguese verb, not an established proper noun the way MEDIR and harness are). The project's original artefact, complete, published, MIT. Four files, each with a Portuguese and Spanish translation alongside it: `SKILL.md`, `interview-script.md`, `briefing-template.md`, `README.md`.

Decides whether the automation should exist, before discussing how it works. Eight blocks, a deterministic tier-derivation table, a verdict with three options including do not do it, and versioning with block-by-block comparison.

Fills a verified gap: there is plenty of material on how to specify well, almost none on how to decide whether it is worth it.

Separated from the harness-medir monorepo for independent installation, in the same pattern as the other skills cited in the compact guide. Active in this environment via a local copy at `.claude/skills/intake-briefing/`, outside version control, see `TOOLS.md`.

### Compact guide to tools and skills

`harness-toolkit.html`

Completely rewritten on 30 August 2026, then translated into English and Spanish the same day as part of the language restructuring, with English as the default tab. Organised by the five steps of MEDIR, not by product category. Eighteen six-field entries, plus a tier-diagnosis section at the start for readers arriving from Part 1. Every MEDIR step carries a recorded critique, not just a recommendation. The eighteenth, `impeccable`, was added to Inspect afterwards, once this project started curating design-QA tools too, see `TOOLS.md`.

Distribution: Map with four entries (intake-briefing, a Karpathy-inspired guide, c4-skills, spec-before-code with Böckeler and Pocock's critique), Equip with three (superpowers, mattpocock/skills, planning-with-files), Delegate with three (holdfast, environment classes, scheduled orchestration with LangGraph), Inspect with four (dependency-cruiser, Stryker, Semgrep, sensors-cli), Reinforce with three (ai-slop-cleaner, cleanup as cadence, garbage collection).

Every tool cited is verified in `sources/inventory.md`, including three sources added in this rewrite: Semgrep, LangGraph and GitHub Spec Kit with a direct link.

Published, public repository at `github.com/tecosodreaboutdigital/harness-medir`.

---

## Not started

### Part 3 · Agent governance

Scope defined, research base weak. It is the piece with the greatest commercial value and the shallowest foundation.

Scope: permission enforced outside the model, malicious instructions arriving inside a piece of data or a third-party skill, an auditable log, reversal, legal obligations, and who answers for what the agent did.

What still needs researching, and it is a dedicated round, not an add-on: agent security literature, documented real incidents, the Brazilian data-protection authority's position on automated decisions, European regulatory obligations for systems classified as high-risk, and what already exists as agent audit standards.

Writing it now would produce well-written opinion, not a reference.

### Translation status

| Piece | PT | EN | ES |
|---|---|---|---|
| Part 1 | ready | ready | ready |
| Part 2 | ready | ready | ready |
| Compact guide | ready | ready | ready |
| Part 3 | missing | missing | missing |
| Briefing skill | ready | ready | ready |
| Governance docs | ready | ready | ready |

### Playbook

Consolidation of the three parts plus the guide, adding what does not exist yet: a task-contract template, a skill template, an execution-receipt template, a risk matrix, a tier diagnostic and a rollout path.

The briefing skill is already its first operational artefact.

---

## Decisions made that should not be reverted without reason

**English is this project's primary production language, decided 30 August 2026,** for both public repositories, even though the working conversation with the author stays in Portuguese. See the `Languages` section of `STANDARDS.md`.

**The term harness is not translated.** Kept in English for the same reason nobody translated kaizen, kanban or poka-yoke. The alternatives arnês, arreio, cabresto and sela (rough Portuguese equivalents evoking a restraint) were discarded: a containment metaphor sells the wrong idea to a reader who already fears losing control.

**The term's correct attribution is Mitchell Hashimoto, February 2026,** not Andrej Karpathy. Karpathy coined vibe coding and popularised context engineering, and his name appears correctly in those contexts.

**Inspect, not Instrument, for the I step.** Instrument is technically more precise and consistent with the argument that quality is not inspected at the end of the line, but Inspect is the term from the author's own repertoire and the acronym depends on it.

**Examples on the individual, team, area ladder.** Do not use "company" or a level above area.

**The opening scene is composite,** not real, and that is stated in the footer of every piece. If a real anonymised case from the author's ecosystem comes up, replacing it would improve the text considerably.

**The compact guide lives apart from the articles,** with a visible revision date, because it ages faster.

**The skill repository is renamed intake-briefing, not kept as levantando-briefing.** Unlike harness and MEDIR, "levantando" was never established as a proper noun the reader needed to learn, it was simply the Portuguese verb for the skill's function, so it translates rather than staying fixed.
