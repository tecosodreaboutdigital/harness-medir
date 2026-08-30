*Read this in [Português](README.pt.md) · [Español](README.es.md).*

# The Harness series and the MEDIR cycle

A content and tooling project about **harness engineering**: the discipline of building the environment around an AI model so it can operate reliably.

Author: Fernando Teco Sodré
Status: in progress, August 2026

---

## The thesis

> Everyone has access to the same model. The competitive advantage is not in the intelligence you hire, it is in the environment you build around it.

An agent equals a model plus a harness. The model is the reasoning engine, and it is the part the industry sells. The harness is everything else: what the system sees, what it can touch, what survives between sessions, what counts as evidence, and when execution needs to stop and call someone.

Harness engineering is not a new field. It is poka-yoke applied to a non-deterministic worker, and it belongs to the same lineage as Shewhart, Deming, PDCA and the Toyota Production System.

---

## The MEDIR cycle

This project's own method, in the PDCA and DMAIC family. It works without adaptation in Portuguese, English and Spanish.

| Step | PT | EN | ES | What it decides |
|---|---|---|---|---|
| M | Mapear | Map | Mapear | The task contract, the boundaries and the knowledge map |
| E | Equipar | Equip | Equipar | Tools, access and durable memory |
| D | Delegar | Delegate | Delegar | Isolated execution, autonomy calibrated to risk |
| I | Inspecionar | Inspect | Inspeccionar | Sensors that produce evidence, not opinion |
| R | Reforçar | Reinforce | Reforzar | The failure becomes a permanent change to the environment |

What separates MEDIR from a generic PDCA is the R step: you act on the environment, not on the response. A patch fixes one run, a change to the harness improves every run after it.

### Autonomy tiers

| Tier | What exists in the environment | Autonomy allowed |
|---|---|---|
| N0 · Assisted | Instruction and model | None, a human reviews every output |
| N1 · Guided | Written guide, tools, task contract | Reversible, low-cost tasks |
| N2 · Measured | Durable state, sensors, attempt ceiling | Long tasks, with evidence before delivery |
| N3 · Governed | Permission outside the model, a trail, reversal | Action with an external effect, under human approval |

Sizing rule: the harness must be smaller than the failure surface it controls.

---

## What is in this repository

```
.
├── README.md                          this file
├── STANDARDS.md                       writing and formatting rules, READ BEFORE EDITING
├── STATUS.md                          what is ready and what is missing, in detail
├── NEXT-STEPS.md                      the work queue, in order
├── TOOLS.md                           third-party skills installed and used, with a real-usage log
├── harness-p1.html                    Part 1, trilingual, ready
├── harness-p2.html                    Part 2, trilingual, ready
├── harness-toolkit.html               compact guide, organised by MEDIR, ready
├── sources/
│   └── inventory.md                   every source verified, with status
├── diagrams/                          SVG renderings for Parts 3 and 4's diagrams, ahead of the articles
├── docs/
│   ├── harness-p3-p4-briefing.pt.md   working dossier for Parts 3 and 4, internal, Portuguese only
│   ├── logbook.html                   trilingual, generated from git and the session's real usage
│   └── assets/logbook-metrics.json    the log's raw data, never edited by hand
└── build/                             text bodies and assembly scripts
```

The HTML files live at the root on purpose: they reference each other by simple relative path. Moving any of them into a subfolder breaks the cross-navigation.

---

## The series' architecture

Six pieces, with different review cadences, organised around a three-layer framework, and only three.

| Layer | Question it answers | Piece |
|---|---|---|
| Build | How you build a reliable agent | Part 2, MEDIR |
| Operation | What it can do, and who answers for it | Part 3, the separation of powers |
| Governance | How many agents exist, who owns each one, which ones still pay for themselves | Part 4, the agent office |

Autonomy tiers N0 to N3 cross all three layers as the one shared ruler, the only vocabulary common to all of them, which is what keeps the framework from becoming three unrelated pieces. A fourth layer was deliberately left out: every framework that has died, died from too much vocabulary.

| Piece | Nature | Review |
|---|---|---|
| Part 1, why | Argument. Why the environment is worth more than the model | Rare |
| Part 2, how | Method. Guides, sensors, skill format, examples | Rare |
| Part 3, operation | Permission outside the model, trail, accountability | Rare |
| Part 4, governance | Life cycle, roles, indicators, where the office sits | Rare |
| Compact guide | Market inventory, with names and repositories | Quarterly |
| Playbook | Consolidation, plus the operational templates | Annual, by version |

The compact guide lives apart precisely because it ages faster. The four parts talk about principles and do not depend on it.

Part 4 joined the series on 30 August 2026, once the research round for Part 3 exposed a second gap behind the first: MEDIR governs a task, not an agent, and nothing in the series before that point governed the set of agents an organisation ends up running. See `docs/harness-p3-p4-briefing.pt.md` for the working dossier this decision came from, internal, Portuguese only, the same exception `sources/inventory.md` already carries.

---

## The reader

An executive, board member, area director, successor running a family business. Not a technical or intermediate-level reader. Companies in the hundred-to-five-hundred-million-real range.

The series exists so that this person can diagnose what stage they are at, understand what they need to build, and talk as an equal with whoever builds it.

One character runs through the series: an operations director at a mid-size manufacturer who single-handedly builds an automation for reconciling freight invoices. She is composed from recurring patterns and does not describe a specific company. In Part 1 she is at N0 and suffers a structural accident. In Part 2 she reaches N1 and discovers that a guide without a sensor is just a well-written recommendation, ending at N2. In Part 3 she faces the first irreversible action. Part 4, not yet written, is where her arc as the agent's sole builder is meant to close.

---

## Languages

English is this project's primary production language for both public repositories, decided 30 August 2026. New content is authored in English first, with Portuguese and Spanish produced as full translations from it.

Three complete versions of every piece: English, Portuguese and Spanish. A single file per piece, with a selector at the top right, English as the default tab. A browser-language hint offers Portuguese or Spanish visitors a dismissible switch when it does not match the active tab.

Important technical detail: anchor identifiers and SVG markers are prefixed by language (`en-`, `pt-`, `es-`) to avoid collisions between the three versions in the same document. Any new content needs to pass through the assembly scripts' `scope()` function.

---

## How to continue

1. Read `STANDARDS.md`. It holds the writing and formatting rules that cannot be violated, including the absolute ban on em dashes.
2. Read `STATUS.md` to know exactly what is ready.
3. Follow `NEXT-STEPS.md` in order.
4. Before citing any tool, check `sources/inventory.md`. An unverified source does not enter a signed document.
5. Before installing any third-party skill to work on this project, follow the same checklist the project recommends to third parties, and log the result in `TOOLS.md`.

---

## Licence

Articles: all rights reserved, use by authorisation.

The project's own skill, `intake-briefing`, lives in a separate repository, [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing), MIT, in the same pattern as the other skills cited in the compact guide.
