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

**Diagrams D1 to D9 validated by rendering, and a unified series architecture.** The nine standalone SVGs were rendered for the first time (headless Chrome) and checked visually, closing the previous round's caveat. Five carried real coordinate bugs (connector lines cutting through box text in D3, a duplicate connector in D4, a caption overflowing the canvas in D5, a line crossing a box and a curve clipping another in D7, two overlapping columns in D9), all fixed in the SVG source; D1, D2, D6 and D8 had none. Each SVG gained a matching `.png` (2x, opaque white background) for Medium publication, since Medium's editor does not render pasted inline SVG. Separately, the series gained the top navigation the reader was missing: a single shared `.topbar` component, centred, sticky, reactive to the language selector (`SERIES` object plus `setSeries()` inside every page's `set()`), replacing the inconsistent, Portuguese-only, non-sticky bar that previously existed only on `harness-p1.html`. The per-article glossary and sources sections were retired in favour of two new shared, trilingual pages, `harness-glossary.html` and `harness-sources.html`, consolidating and deduplicating every term and citation from parts 1 and 2; every in-body glossary link and citation across the whole series now points there. `harness-p1.html`, `harness-p2.html` and `harness-toolkit.html` were retrofitted (and `build_p2.py` / `build_toolkit.py` updated to reproduce the same bar on the next regeneration, so the fix does not silently revert). Part 3's English body was drafted in full against this new pattern (see the next section) and wired into `harness-p3.html`; its Portuguese and Spanish tabs are an honest "translation in progress" stub, not fabricated text, pending the next session.

---

## Completed on 31 August 2026

**AGENTS.md and llms.txt created, the repository made operable by an AI agent, not only readable by one.** `AGENTS.md`, English only, at the repository root: the operating protocol for any AI agent or assistant acting on this repository, written in `STANDARDS.md`'s own skill-writing pattern (non-negotiable rule, red flags, verification steps, an explicit exit path when no network access exists, a Never section, honest limits). Its core rule: before installing, recommending or fetching any third-party skill this project curates, check the origin URL for whether it is still current, never present `sources/inventory.md`'s dated snapshot as a live state. `llms.txt` added at the root, publishing a discovery index for an agent that only fetched the site's URL. `README.md` gained a visible section, "This repository is also built to be operated", right after The thesis, plus a line at the top pointing to `AGENTS.md`, without touching the rest of the document, in all three languages. `harness-toolkit.html` section 11 and the top of `sources/inventory.md` each gained one sentence pointing an agent at the same protocol, in every language the page carries. Every insertion is additive: no existing paragraph of the README, the compact guide or the ledger was rewritten.

**The project log made visible in the README, with its own two charts.** `docs/logbook.html` used to appear as a single line in the file tree and nowhere else in `README.md`. A new section, "This project also inspects itself", placed right after the MEDIR cycle table so it reads as Inspect applied reflexively, embeds the log's own two real charts (words published and tokens consumed, cumulative by milestone, same X axis) as `docs/assets/logbook-words-published.png` and `docs/assets/logbook-tokens-consumed.png`, exported at 2x from the current `docs/logbook.html` markup via the same headless-Chrome screenshot method the D1 to D10 diagrams already use. Each caption states plainly that the embed is a snapshot as of the logbook's last regeneration, not a live view, and points to `docs/logbook.html` for the current numbers. Regenerate both PNGs whenever the logbook itself regenerates, or the README's snapshot drifts from the page it summarises.

**GitHub Pages checked for the first time, one broken link found and fixed.** The bare Pages URL, `tecosodreaboutdigital.github.io/harness-medir`, cited from `README.md`, `STATUS.md` and this file since it went live on 30 August, had never actually been opened, exactly the check this file's own `Publication` item had left pending. It 404s: `gh api repos/tecosodreaboutdigital/harness-medir/pages` confirms the site serves from the repository root, and no `index.html` existed there to answer a request for the bare directory. Fixed at the source rather than in each citation: a minimal `index.html` now sits at the root and redirects to `harness-p1.html`, the series' natural entry point, which already carries the full navigation bar and the browser-language hint. Every reference to the bare Pages URL across the repository resolves correctly now, with no text changed in any of them.

**Multi-tool installation for `intake-briefing` documented directly in this repository, not only in the skill's own.** `README.md` gained a full `Installation` section, all three languages, deliberately duplicating the skill repository's own already-verified instructions rather than only linking out: personal skill clone, `.agents/skills/` for Cursor, Codex CLI and Google Antigravity, Google AI Studio's Playground by mounting the repository or pasting the files, and a Claude Code plugin from its own marketplace. Each of the four vendor claims, plus the open Agent Skills format itself, was checked independently against that vendor's own documentation before writing it here, not only inherited from the skill repository's 31 August verification note. `harness-toolkit.html`'s compact-guide card for `intake-briefing` gained the same multi-tool detail inside its `How to start in 15 minutes` field, all three languages, the other five fields of the six-field format untouched. The `intake-briefing` repository itself had, separately, already been packaged with `AGENTS.md`, `llms.txt`, `.claude-plugin/` and `briefings/`; the stale local copy at `.claude/skills/intake-briefing/`, the risk `TOOLS.md` had already named, was resynced to match. The duplication is deliberate, not an oversight of the project's usual single-shared-page rule: the goal is a repeatable installation pattern for any future repository on this account about an agent, an automation or a skill, each one self-sufficient even while pointing at the others.

---

## 1. Write Part 3, done

**Status: written and live at `harness-p3.html`, all three languages.** The nine sections below are all in the body (`build/body_p3_en.html`, `_pt.html`, `_es.html`), with the five diagrams inline and fully translated (including every SVG label, checked by rendering each diagram standalone in all three languages, no overflow, no overlap), the matrix-of-authority and receipt-schema artefacts in the text, both honesty obligations honoured, and the Air Canada character arc closing in section 9. Word counts run close across the three (EN 5,131, PT 5,468, ES 5,676), consistent with a real translation rather than a summary. Kept as tracking record below.

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

**Done when:** all three versions are ready, the character's arc closes, the piece works alone for a reader who has not read the previous ones, and the matrix-of-authority and receipt-schema artefacts it leaves behind are in the text. **Met, 30 August 2026.**

---

## 2. Write Part 4, done

**Status: fully trilingual and live at `harness-p4.html`, since 31 August 2026.** Nine sections, five diagrams inline (D6 to D10, D10 newly rendered for this piece, then translated and visually re-validated in all three languages before merging), the six-state life cycle table, the four-role table with the non-accumulation rule, the eight-indicator table with the honesty admission that the panel is synthesis, the SCHUFA-grounded gate-rejection-rate argument tying part 4 to part 3's legal ground, the CISO-reporting-line precedent for where the office sits, the seven-agents-and-a-spreadsheet constraint held through the warning section, and the closing table matching part 3's pattern. Word counts run close across all three (English 6,889, Portuguese 7,051, Spanish 7,377), consistent with a real translation rather than a summary. Ten new glossary terms added across all three languages; `harness-sources.html` gained a Part 4 section, 32 sources.

Research is complete, see `sources/inventory.md`'s Part 4 section and `docs/research-part4.pt.md`. Central thesis realised: the agent life cycle, states and not steps, distinguished from MEDIR with enough clarity that a reader cannot confuse the two.

Structure covered, in the order actually drafted:

1. Opens with the 20,225-account Instagram takeover, part 3's concentration failure mode at population scale
2. The director re-enters running six systems nobody has counted, unable to answer a board member's simplest question
3. The life cycle itself, six states from a versioned briefing to decommissioning, with the two transitions almost nobody implements, expired certification and no execution in the period, both leading to decommissioning
4. The four roles and the non-accumulation rule, the same separation of powers as Part 3, now on the organisational plane, sourced to the IIA's Three Lines Model
5. The eight indicators, two of which measure the governance's own quality rather than the agent's: the exception rate, and the gate's own refusal rate, closed by D10, the office's quarterly loop
6. Where the office sits, and why not in IT, presenting the realistic options with the cost of each
7. The warning: the antidote to reading as a vendor brochure is an explicit constraint running through the text, everything it proposes has to work in a company with seven agents and a spreadsheet
8. The closing argument: every platform governs inward, which is why the office has to be a function of the company, not a product it buys
9. Who answers, and where you stand: the director's arc closes across all four parts

**Done when:** all three versions are ready, the character's arc closes the series, the eight indicators are defined with a formula, and the text holds to the seven-agents-and-a-spreadsheet constraint throughout. **Met in full, 31 August 2026.**

---

## 3. Consolidate the playbook

Not started, and not scoped for the next content session either, decided 31 August 2026: the four parts are the argument, the playbook is the toolkit derived from them, and building it now, right after finishing the article series, would blur that boundary. This entry stays as the explicit, deliberately parked record of what the playbook will contain, so the next session that does pick it up does not have to re-derive the plan from scratch.

Reuses the four parts and the guide, and adds seven operational templates that do not exist yet, each one traceable to the piece that already introduced its underlying concept, not invented fresh:

- Task-contract template, from the task contract in Part 1's Map step
- Skill template, derived from Part 2's three worked examples of the skill format
- Execution-receipt template, from Part 2's original receipt, extended in Part 3 with the rule-of-two answers and the reversal point
- Risk matrix by tier, from Part 3's matrix of authority (class of action, reversibility, authority required) crossed with Part 1's N0 to N3 tiers
- Tier diagnostic, questionnaire version, expanding Part 1's twelve-question checklist into a standalone instrument
- Rollout path from N0 to N3, the progression Part 1 only sketched
- Agent-registry template and certification-meeting-minutes template, from Part 4's life cycle states and four roles, the registry answering "how many exist" and the minutes formalising the certifier's act

D10, the office's own quarterly loop, is no longer a playbook candidate: it shipped inside Part 4 itself, closing the eight-indicators section. It can still open the playbook as a second appearance, legitimately, since it organises the whole document there rather than competing with itself.

**Done when it is actually picked up:** all seven templates exist, each cross-referenced back to the part and section that grounds it, and the playbook opens with D10 as its own organising diagram.

---

## Minor pending items, to decide at any point

**Real opening case.** The scene is composite. If a real anonymised case from the author's ecosystem comes up, replacing it would raise the text considerably.

**Table-of-contents box border.** It is the only box border left in the documents. Decide whether it goes, to stay consistent with the removal of the others.

**Pull-quote background in print.** Depends on whether the browser is set to print background graphics. A dependency-free alternative: a thin rule above and below the block.

**English spelling.** Currently British, now the project's default reading. If the target audience shifts toward the United States, convert it.

**Locate the rule of two's primary source.** Two independent secondary sources attribute it to Meta with the same wording, sufficient to cite the content in Part 3, not to link it. Search again before that piece is signed off, see `sources/inventory.md`.
