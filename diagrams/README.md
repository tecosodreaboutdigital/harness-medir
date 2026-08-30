*Working directory, not reader-facing.*

# Diagram renderings for Parts 3 and 4

Nine standalone SVG files, one per diagram specified in `docs/harness-p3-p4-briefing.pt.md` (block C), rendered ahead of the articles that will carry them.

**Source of truth.** The Mermaid specification for each diagram lives in the dossier, not here. Per `STANDARDS.md`'s `Diagrams` rule, if a diagram's structure or a label needs to change, edit the Mermaid in the dossier first, then regenerate the matching file below.

**Visual validation, 30 August 2026.** The nine SVGs were rendered for the first time (headless Chrome, `viewBox` dimensions at 2x scale) and checked by eye, closing the caveat the previous session had logged: coordinates computed by hand, never seen rendered. Five files had real overlap bugs, all fixed in the SVG source directly: `d3` had connector lines starting from a box's centre rather than its edge, cutting straight through the label text of boxes stacked below it (fixed by starting each line from the box edge nearest the destination); `d4` carried a duplicate connector into its first diamond, one copy the right length but missing its arrowhead, the other with an arrowhead but overshooting deep into the diamond's interior (merged into one correct line); `d5` had a caption running 82px past the 700-wide canvas, invisible past the edge (right-aligned it inward); `d7`'s heavier "validity expired without renewal" line cut straight through the `IN OPERATION` box, and its "certifier's decision" curve clipped the bottom of `UNDER REVIEW` (both rerouted, the canvas gained 24px of height to give the relabelled curve room); `d9`'s third and fourth platform columns overlapped by 40px, doubling their dashed borders visibly (all four columns recomputed to equal, non-overlapping widths). `d1`, `d2`, `d6` and `d8` had no layout bugs. The Mermaid specs in the dossier were not touched, since none of these were structural or label changes, only coordinate corrections within the existing shapes.

**PNG renders, for Medium.** Each SVG has a matching `.png` alongside it, same basename, rendered at 2x the SVG's `viewBox` dimensions on an opaque white background (headless Chrome screenshot, not a library), because Medium's editor does not render pasted inline SVG or arbitrary HTML — only uploaded image files. These are what get uploaded to Medium; the GitHub repository stays the source both the inline SVG (once Parts 3 and 4 are written) and the PNG derive from. Regenerate a PNG after any edit to its SVG; a PNG that has drifted from its SVG source is worse than none.

**Why English.** Part 3 and Part 4 do not exist yet. Per `STANDARDS.md`'s `Languages` rule, new content is authored in English first, so these are English-only for now. When each article is actually written, its diagram is copied inline into the HTML, re-IDed through the build scripts' `scope()` function, and translated alongside the surrounding prose, the same path Parts 1 and 2 already went through.

**Visual system.** Inline SVG, 0.7 stroke, no fill, no colour, `#1b1b19` ink and `#8a887f` faint ink on a transparent background, labels in spaced small caps (`svg-lbl`), captions in italic 9-point (`svg-cap`), exactly as declared in `STANDARDS.md`. Each file is self-contained with its own `<style>` block so it can be opened and checked on its own.

**Terminology introduced here, first use.** Part 4 coins governance vocabulary that did not exist in the series before this round. Keep these exact terms when Part 4 is written, so the diagrams and the prose do not drift apart: **Agent owner** (dono do agente), **Certifier** (homologador) and **Certified** (homologado) for the state and the role, **Auditor** (auditor), **Area sponsor** (patrocinador da área), **Receipt** (recibo, the per-execution artefact) kept distinct from **Record** (registro, the append-only log itself).

| File | Diagram | Piece | Where it enters |
|---|---|---|---|
| `part3/d1-separation-of-powers.svg` | D1 · The separation of powers | Part 3 | Section 2, right after the Air Canada opening |
| `part3/d2-concentration.svg` | D2 · The failure mode: concentration | Part 3 | Immediately after D1, same page |
| `part3/d3-order-inside-the-data.svg` | D3 · Where the order enters inside the data | Part 3 | Section on malicious instructions arriving inside content |
| `part3/d4-rule-of-two.svg` | D4 · The rule of two | Part 3 | Section on authority, right after D3 |
| `part3/d5-life-of-an-action.svg` | D5 · The life of an action with an external effect | Part 3 | Section on what needs to be logged, or on reversal |
| `part4/d6-three-layers.svg` | D6 · The three layers of the framework | Part 4 | Opening of Part 4, and likely the playbook's own opening |
| `part4/d7-agent-lifecycle.svg` | D7 · The agent life cycle | Part 4 | Life-cycle section |
| `part4/d8-four-roles.svg` | D8 · The four roles and the non-accumulation rule | Part 4 | Roles section |
| `part4/d9-platforms-govern-inward.svg` | D9 · Every platform governs inward | Part 4 | Section on the record's independence |

D10, the office's own loop, is a candidate not yet decided, see the dossier. It has no file here.

**Rendering notes honoured, one line each, full notes in the dossier.**

- D1: the record is a cylinder, the only shape among the four functions that does not decide or act.
- D2: deliberately sparse next to D1, fewer boxes, a dotted line, empty space as the argument.
- D3: the two zones stay visually separate until the funnel, the caption states the boundary is the diagram's, not the model's.
- D4: both outcomes of the count converge into the same receipt, approved or not.
- D5: the reversal point is logged before execution, that line carries a heavier stroke and its own annotation, because logging it after is the most common mistake.
- D6: the N0 to N3 ruler is drawn touching all three layers, it is the only vocabulary shared across them.
- D7: the two transitions nobody implements, expired certification and no execution in the period, both leading to decommissioning, carry a heavier stroke.
- D8: the four groups reuse D1's exact verbs, proposes, authorizes, executes, witnesses, to keep the technical and organisational separation of powers visibly the same idea.
- D9: each platform is drawn inside its own dashed wall, the master record sits above and outside every wall.
