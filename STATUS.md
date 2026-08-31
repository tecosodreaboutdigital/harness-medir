*Read this in [Português](STATUS.pt.md) · [Español](STATUS.es.md).*

# Status

Situation as of 30 August 2026.

Published at `github.com/tecosodreaboutdigital/harness-medir` (repository) and `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, the HTML files render as pages, not just as source code).

**Branch protection on `main`, configured 30 August 2026.** Set directly via the GitHub API: a pull request is required to merge, at least one approval is required, an approval is dismissed if a new commit lands before merge, force pushes and branch deletion are both blocked. `enforce_admins` was deliberately left off, so the repository owner's existing direct-push workflow to `main` keeps working unchanged. The rule's real effect is on any future contribution arriving from a fork: it must be reviewed and merged by hand, never automatically, which was already true in practice (`allow_auto_merge` was already `false`, and no collaborator besides the owner has write access), but is now enforced by GitHub itself rather than by convention alone.

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

### Part 3 · The separation of powers: what it can do, and who answers for it

`harness-p3.html`

Fully trilingual since 30 August 2026. Nine sections, five diagrams, all inline and fully translated including every SVG label. About 5,131 words in English, 5,468 in Portuguese, 5,676 in Spanish, the word counts running close across all three, as expected of a real translation rather than a summary.

Opens with Moffatt v Air Canada, 2024 BCCRT 149: a real company argued in a real tribunal that its chatbot was a separate legal person answerable on its own, and lost, stated explicitly as a foreign precedent, not a Brazilian one. The director re-enters at N2, one small feature extension away from an unauthorised reply that would have bound the company, the direct echo of Air Canada's own mistake. Central thesis: the model proposes, the policy authorises, the tool executes, the record witnesses, four functions that cannot live in the same place, with the failure mode named, concentration. The rule of two (private data, untrusted content, external communication, at most two without a human in the loop) serves as the piece's operational tool, the equivalent of Part 2's guides-and-sensors matrix, alongside a general reversibility-based matrix of authority. Identity gets a named owner and the on-behalf-of versus autonomous delegation distinction; injection is treated as architecture, not configuration; a reversal point logged before execution, not after, anchors what must be on the record; a third-party skill's supply-chain risk closes the hook Part 2 left open; legal obligations run in two columns, Brazil (LGPD article 20, dated as not yet specifically regulated) and Europe (EU AI Act articles 12, 14 and 26). Both honesty obligations the research flagged are honoured in the text: the Air Canada precedent's foreign origin, and the dated claim about Brazilian regulation.

Series bar and glossary and sources links already implemented, per the shared architecture above.

### Part 4 · The agent office: how many exist, who owns them, and which ones still pay for themselves

`harness-p4.html`

English complete since 30 August 2026, about 6,900 words, nine sections, five diagrams (D6 to D10, D10 newly rendered for this piece, see `diagrams/README.md`). Portuguese and Spanish are an honest "translation in progress" stub for now, the same state Part 3 passed through earlier the same day before its own full translation landed; `harness-p4.html` reads correctly in all three tabs, English is simply the only complete one so far.

Opens with the 20,225 Instagram accounts taken over between 17 April and 31 May 2026 through a single AI-mediated interaction that combined identity management and credential recovery, Part 3's concentration failure mode at population scale rather than in one action. The director re-enters running six systems everyone calls agents and cannot answer a board member's simplest question: how many, and who owns each one. Central thesis: the agent life cycle, six states rather than steps, distinguished from MEDIR explicitly, with the two transitions almost nobody implements, expired certification and no execution in the period, both leading to decommissioning and both requiring a human decision, never an automation. Four roles under a non-accumulation rule mirror Part 3's separation of powers on the organisational plane, sourced this round to the Institute of Internal Auditors' Three Lines Model, adopted 2013. Eight indicators are declared explicitly as synthesis, not market standard, with the gate-rejection-rate indicator grounded in the SCHUFA holding (CJEU, case C-634/21, December 2023) exactly the way Part 3's legal ground works, the thread tying the two pieces together. Where the office sits draws the CISO reporting-line precedent, sourced to a 2026 benchmark and the fire-marshal-and-sprinklers quote. The explicit constraint runs through the whole piece: everything proposed has to work in a company with seven agents and a spreadsheet, illustrated by an unattributed, generic description of what today's agent dashboards already do and the five gaps past that floor. Closes with the director's arc across all four parts and the series' own closing table.

Ten glossary terms added this round (agent office, agent owner, certifier, area sponsor, non-accumulation rule, life cycle, dark matter of identity, Heinrich, cost per completed task, Three Lines Model), all three languages, alphabetised; fixing them also corrected five pre-existing alphabetisation bugs in the Portuguese glossary and one in the Spanish glossary, left over from an earlier round that translated terms without re-sorting. `harness-sources.html` gained a Part 4 section, 32 sources including the still-unlocated CJEU primary decision, same V/P discipline as Part 3.

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

### Parts 3 and 4 preparation

`sources/inventory.md`, `diagrams/`, `STANDARDS.md`, `README.md`, `STATUS.md`, `NEXT-STEPS.md`.

Follows the working dossier `docs/harness-p3-p4-briefing.pt.md`, added 30 August 2026 with a structural diagnosis, seven research axes and a nine-diagram visual specification, and completes the first three items of its work queue, block D.

The governance documents now describe four parts organised around a three-layer framework, build, operation, governance, crossed by the N0 to N3 tiers as the one shared ruler, instead of three parts plus two companions. `STANDARDS.md` gained a `Diagrams` section: every diagram is born as a Mermaid specification, the inline SVG derives from it and never replaces it, matching the rule the dossier itself proposed.

`sources/inventory.md` gained a new section, 32 sources across the dossier's seven research axes plus the finding that reframes Part 3's opening, all carried over with the original V or P status. Two are flagged with an explicit note, not just a status letter, because the gap they mark changes what Part 3 is allowed to claim: the rule of two's original Meta publication was never read at the primary source, and the Air Canada precedent used to open the piece is Canadian, not Brazilian.

`diagrams/` gained nine standalone SVG files, D1 to D9, rendered from the dossier's Mermaid specifications in the project's visual system, English because this is new content and English is authored first. Governance vocabulary that Part 4 needed, agent owner, certifier, auditor, area sponsor, and receipt kept distinct from record, was fixed at this stage precisely so the diagrams and the eventual prose did not drift apart. A tenth, D10, the office's own quarterly loop, was added once Part 4's drafting confirmed it earned its place, closing the indicators section rather than opening the piece. See `diagrams/README.md` for the full index and which rendering note each file honours.

What remains from the dossier's queue: Part 4's Portuguese and Spanish translation, and consolidating the playbook. Parts 3 and 4 are both written in English, see below.

### Diagrams D1 to D9 validated by rendering, and a shared series architecture

Closes the caveat the previous round had logged: the nine standalone SVGs (`diagrams/part3/`, `diagrams/part4/`) were never actually rendered, only checked as well-formed XML. They now have been, via headless Chrome, and checked visually. Five carried real coordinate bugs, all fixed in the SVG source, none in the underlying Mermaid specification, since none of the five were structural: `D3` had connector lines starting at a box's centre and cutting through the label text of boxes stacked below, fixed by starting each line at the box edge nearest its destination; `D4` carried two overlapping connectors into its first diamond, one the right length with no arrowhead, the other with an arrowhead overshooting into the diamond's interior, merged into one; `D5`'s closing caption ran 82 pixels past the 700-wide canvas; `D7`'s heaviest line cut straight through the `IN OPERATION` box, and a curve clipped `UNDER REVIEW`, both rerouted, the canvas gaining 24 pixels of height; `D9`'s third and fourth columns overlapped by 40 pixels, doubling a dashed border visibly. `D1`, `D2`, `D6` and `D8` had no bugs. Each SVG gained a matching `.png` (2x scale, opaque white background) for Medium publication, since Medium's editor renders neither pasted inline SVG nor arbitrary HTML.

Separately, the series gained the top navigation it had been missing since the four-part restructuring: a single shared `.topbar` component, one line, centred, sticky while scrolling, reactive to the language selector (`PART 1 · PART 2 · PART 3 · PART 4 | COMPACT GUIDE · GLOSSARY · SOURCES { PT EN ES }`, the current page rendered as plain text and a part not yet written rendered dim and unlinked). It replaces a bar that previously existed only on `harness-p1.html`, hardcoded in Portuguese regardless of the active tab, left-aligned, not sticky. The per-article glossary and sources sections that Parts 1 and 2 each carried were retired in favour of two new shared, trilingual companion pages, `harness-glossary.html` (56 consolidated, deduplicated entries) and `harness-sources.html` (46 consolidated sources, grouped foundational and Part 3), and every in-body glossary link and citation across the whole series now points there instead. `harness-p1.html`, `harness-p2.html` and `harness-toolkit.html` were retrofitted; `build_p2.py` and `build_toolkit.py` were updated to reproduce the same bar on their next regeneration, closing the gap where a rebuild would have silently reverted the fix. See `STANDARDS.md`'s `Cross-navigation` and `Glossary` sections for the rule this now follows.

---

## Not started

### Translation status

| Piece | PT | EN | ES |
|---|---|---|---|
| Part 1 | ready | ready | ready |
| Part 2 | ready | ready | ready |
| Compact guide | ready | ready | ready |
| Part 3 | ready | ready | ready |
| Part 4 | missing | ready | missing |
| Briefing skill | ready | ready | ready |
| Governance docs | ready | ready | ready |

### Playbook

Consolidation of the four parts plus the guide, adding what does not exist yet: a task-contract template, a skill template, an execution-receipt template, a risk matrix, a tier diagnostic, a rollout path, and an agent-registry and certification-minutes template.

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

**The series has four parts, not three, organised around three layers, build, operation, governance, crossed by the N0 to N3 ruler, decided 30 August 2026.** A fourth layer was considered, to hold the ruler itself, and rejected: N0 to N3 already plays that role, and a second axis would duplicate vocabulary with no gain. See `docs/harness-p3-p4-briefing.pt.md`.

**Part 4's governance vocabulary is fixed ahead of the prose:** agent owner, certifier (the state is certified), auditor, area sponsor, and receipt kept distinct from record. Set at diagram-rendering stage so the nine SVG files in `diagrams/` and the eventual article text do not drift apart.
