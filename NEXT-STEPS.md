*Read this in [Português](NEXT-STEPS.pt.md) · [Español](NEXT-STEPS.es.md).*

# Next steps

In order. Every item carries its done criterion.

---

## Completed on 30 August 2026

**Public GitHub repository created**, at `github.com/tecosodreaboutdigital/harness-medir`. Initial commit with the 23 files that existed at the time, no sensitive data. LICENSE (MIT) added inside what was then `skills/levantando-briefing/`, consistent with what the skill's README already declared. No licence at the root, because the articles remain all rights reserved.

**Compact guide completely rewritten.** See the matching entry in `STATUS.md` for detail. Done criterion met: seventeen six-field entries, every tool verified in `sources/inventory.md` (three new sources verified in that round: Semgrep, LangGraph, GitHub Spec Kit with a direct link), and every MEDIR step carrying a recorded critique.

**Part 2 translated into English and Spanish**, in the same file, with the selector. `build/build_p2.py` rewritten for trilingual assembly, in the same pattern `build/build_all.py` once used: extracts the PT body from the live file (which is the source of truth, not `build/body_p2_pt.html`, which had drifted out of date), assembles EN and ES from `build/body_p2_en.html` and `build/body_p2_es.html`, prefixes everything by language via `scope()`. All three buttons work and there is no broken anchor. As a side effect, the language-switching JavaScript in `harness-p1.html` and `harness-p2.html` gained anchor-based routing (`#en-opening` selects the right tab before scrolling), so a cross-link between the pieces in English or Spanish would not always land on the Portuguese tab.

**Thirty third-party skills installed for use on this project**, five collections (superpowers in full, a curated selection of twelve from mattpocock/skills, c4-skills in full, the Karpathy-inspired guide, ai-slop-cleaner), all MIT, all audited against the compact guide's own checklist before installing. They live in `.claude/skills/`, outside version control. Full documentation, with a real-usage log growing per session, in `TOOLS.md`. Credit visible in the footer of `harness-p1.html`, `harness-p2.html` (three languages) and `harness-toolkit.html`.

**The skill separated into its own repository**, at what was then `github.com/tecosodreaboutdigital/levantando-briefing`, public, MIT, in the same pattern as the other skills cited in the compact guide. Removed from `skills/` inside harness-medir, which now only points to it.

**Project log created**, `docs/logbook.html`, trilingual, generated in two steps: `build/generate_logbook_metrics.py` reconstructs the real series (words published per `git show` on each commit, lines in `build/` and the governance documents, tokens summed from the real `usage` of every message in the session's `.jsonl` transcript, attributed to the chronologically next commit) and writes `docs/assets/logbook-metrics.json`; `build/build_logbook.py` assembles the page from that JSON, never written by hand. Two stacked SVG charts, same X axis, no dual Y axis. Six real milestones recorded (the repository's full history so far, not a sample), plus whatever had not closed a milestone yet.

**GitHub Pages enabled**, publishing the repository at `tecosodreaboutdigital.github.io/harness-medir`. `.nojekyll` added to serve the HTML files as they are, with no Jekyll processing. Without it, no article was actually readable as a web page there, only as source code in GitHub's viewer.

**English-primary restructuring across both public repositories.** English became the primary production language, decided partway through this session. Every governance document renamed and rewritten English-first (`PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`), each with a Portuguese and Spanish translation alongside it. `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, matching `build/` scripts renamed and, for the toolkit, rewritten into a trilingual build with English as the default tab. `harness-p1.html`, `harness-p2.html` and `docs/logbook.html` had their default tab flipped from Portuguese to English, in both the built files and the scripts that regenerate them. A browser-language hint banner was added to all four trilingual pages (Portuguese or Spanish browsers get a dismissible offer to switch, anything else falls back to English silently). The skill repository was renamed `levantando-briefing` → `intake-briefing` and every one of its four files rewritten English-first with `.pt.md`/`.es.md` translations, plus a static language-navigation line at the top of each, since GitHub does not execute JavaScript inside rendered Markdown. See `STATUS.md` for the full detail and `STANDARDS.md`'s `Languages` section for the rule itself.

**Four externally recommended skills checked, one adopted.** `ponytail`, `no-ai-slop`, `taste-skill` and `impeccable` were compared on relevance, maintenance signal, contributor count and licence before any of them touched this repository. `ponytail` (117,000 stars, benchmarked, actively maintained) would have resolved `karpathy-guidelines`' own misattribution caveat but was set aside for now rather than adopted. `no-ai-slop` is a genuinely useful prose-cleanup skill whose banned-word list happens to include this project's own core term, "harness", and was also set aside pending a decision on how to except it. `taste-skill` was declined outright: its ten sub-skills read in exactly the hype register a project about evidence over opinion should not cite, and six contributors against 82,000 stars is a thin base. `impeccable` was adopted: Apache-2.0, 30 contributors, versioned (v4.1.2), derives from Anthropic's own frontend-design skill, and its 61 deterministic detector rules fit Inspect's own definition, evidence instead of opinion, applied to frontend design specifically. Installed as documentation only, `SKILL.md` and `reference/`, deliberately leaving out the `scripts/` tree its CLI needs, see `TOOLS.md`. Added as the compact guide's eighteenth entry, in Inspect, across all three languages, see `sources/inventory.md` for the verification record.

**Parts 3 and 4 preparation, the first three items of the working dossier's queue.** `docs/harness-p3-p4-briefing.pt.md` set the queue in its block D, and this round closed items 1 through 3. `README.md`, `STATUS.md`, `NEXT-STEPS.md` and `STANDARDS.md`, in all three languages, now describe four parts organised around a three-layer framework, build, operation, governance, crossed by the N0 to N3 tiers, instead of three parts plus two companions, and `STANDARDS.md` gained the `Diagrams` rule the dossier proposed: Mermaid first, the SVG derives and never replaces it. `sources/inventory.md` gained a new section carrying the dossier's 32 sources across seven research axes plus the Air Canada finding, original V or P status preserved, with an explicit note on the two that mark a real gap rather than a missing link: the rule of two's primary source, and the fact that no Brazilian precedent exists yet. Nine standalone SVG files, D1 to D9, were rendered into the new `diagrams/` directory from the dossier's Mermaid specifications, in English since this is new content, with Part 4's governance vocabulary (agent owner, certifier, auditor, area sponsor, receipt kept distinct from record) fixed at this stage so the diagrams and the eventual prose do not drift. See `STATUS.md` for the full detail and `diagrams/README.md` for the index.

---

## 1. Write Part 3

Research is complete, see `sources/inventory.md`. The dossier's own closing section, block B's "What the research changes in the planned structure", revises the original ten-section sketch down to nine. Reconstructed here for tracking, confirm against the dossier before drafting:

1. Air Canada opens the piece: a real company argued in a real tribunal that its assistant was a separate legal person, answerable on its own, and lost
2. The director re-enters here, at N2, facing the first irreversible action, the contrast against Air Canada's argument is the point
3. The separation of powers, with the rule of two as its operational tool, the equivalent of Part 2's guides-and-sensors matrix
4. Identity and a named owner: who deployed it, what it is authorized to do, on whose behalf it is acting right now
5. When the order arrives inside the data
6. What needs to be logged, and what reversal actually means
7. A third-party skill is third-party code, closing the hook Part 2 left open
8. Legal obligations in two columns, Brazil and Europe, what already applies before what is still pending
9. Who answers for it, and where you are, the series' closing

Two honesty obligations the dossier flags explicitly: state that the Air Canada precedent is foreign, or a legal reader will discount the whole piece, and date the claim that Brazil's specific regulation for LGPD article 20 has not been published yet, because that sentence can age within months.

**Done when:** all three versions are ready, the character's arc closes, the piece works alone for a reader who has not read the previous ones, and the matrix-of-authority and receipt-schema artefacts it leaves behind are in the text.

---

## 2. Write Part 4

Research not started, scope defined in the dossier's block A. Central thesis: the agent life cycle, states and not steps, distinguished from MEDIR with enough clarity that a reader cannot confuse the two.

Structure to cover, per the dossier, order subject to drafting:

1. The life cycle itself, six states from a versioned briefing to decommissioning, with the two transitions almost nobody implements, expired certification and no execution in the period, both leading to decommissioning
2. The four roles and the non-accumulation rule, the same separation of powers as Part 3, now on the organisational plane
3. The eight indicators, two of which measure the governance's own quality rather than the agent's: the exception rate, and the gate's own refusal rate
4. Where the office sits, and why not in IT, presenting the realistic options with the cost of each
5. The warning: this is the piece most likely to read as a vendor brochure, and the antidote is an explicit constraint running through the text, everything it proposes has to work in a company with seven agents and a spreadsheet
6. The closing argument: every platform governs inward, which is why the office has to be a function of the company, not a product it buys

**Done when:** all three versions are ready, the character's arc closes the series, the eight indicators are defined with a formula, and the text holds to the seven-agents-and-a-spreadsheet constraint throughout.

---

## 3. Consolidate the playbook

Reuses the four parts and the guide, and adds what does not exist yet:

- Task-contract template
- Skill template, derived from Part 2's three examples
- Execution-receipt template
- Risk matrix by tier
- Tier diagnostic, questionnaire version
- Rollout path from N0 to N3
- Agent-registry template and certification-meeting-minutes template

D10, the office's own quarterly loop, not decided for Part 4, is a strong candidate to open the playbook if it stays out of Part 4.

---

## Minor pending items, to decide at any point

**Real opening case.** The scene is composite. If a real anonymised case from the author's ecosystem comes up, replacing it would raise the text considerably.

**Table-of-contents box border.** It is the only box border left in the documents. Decide whether it goes, to stay consistent with the removal of the others.

**Pull-quote background in print.** Depends on whether the browser is set to print background graphics. A dependency-free alternative: a thin rule above and below the block.

**English spelling.** Currently British, now the project's default reading. If the target audience shifts toward the United States, convert it.

**Publication.** Resolved on 30 August 2026: GitHub Pages live at `tecosodreaboutdigital.github.io/harness-medir`. Check after the first automatic build that the documents render correctly there (the link most likely to need adjustment is some relative path between them).

**Locate the rule of two's primary source.** Two independent secondary sources attribute it to Meta with the same wording, sufficient to cite the content in Part 3, not to link it. Search again before that piece is signed off, see `sources/inventory.md`.
