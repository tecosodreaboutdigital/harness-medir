*Read this in [Português](STANDARDS.pt.md) · [Español](STANDARDS.es.md).*

# Standards

Non-negotiable rules for this project. Read before editing any file.

---

## Writing

**Em dash is forbidden under any circumstance.** Do not use it in any language. Replace it with a comma, colon, parentheses or full stop. This is the most-violated and most important rule.

**Hyphen is allowed**, including automatic hyphenation in justified text.

**Register of the prose:** narrative and argued, in the line of Adam Grant, Brené Brown, Simon Sinek and Malcolm Gladwell. No bullet dumps. The text argues, it does not list.

**Tone:** direct. No long introduction, no empty transition, no redundant conclusion, no positive reinforcement.

**Factual correction outranks smoothing.** Wrong attributions are corrected in the text. A tool without a verified source is not cited.

**Avoid:** filler words such as "genuinely", "honestly", "simply" (and their Portuguese/Spanish equivalents). Avoid overusing the "it's not X, it's Y" construction. Avoid scare quotes around invented terms.

---

## Document formatting

| Element | Specification |
|---|---|
| Page | A4, 2 cm margins top and bottom, 1.5 cm on the sides |
| Body | Aptos or Aptos Light, 10.5, justified |
| Level-1 title | 14, bold |
| Level-2 title | 12 |
| Section numbering | Number on the title's own line. No small label above it. No sub-item numbering |
| Tables | Full width, header centred at 8, body at 9, no shading, no alternating colours |
| Figure and footnote captions | No border, italic, size 9 |
| Pull quote | No border at all, light blue-grey background, size 9, protected against page breaks |
| Code blocks | Same background as pull quotes, no border, 8.5 in print |
| Output | HTML only. No DOCX, no Markdown for articles |

Exception to the last line: skills and operational templates are born in Markdown, because they are repository artefacts.

---

## Visual system

Inline SVG diagrams, 0.7 stroke, no fill, no colour. Labels in spaced small caps. Captions in italic 9, no border.

One deliberate exception: the tier diagram uses increasing box height to represent autonomy.

Do not use charting libraries. Do not use raster images.

---

## Diagrams

Every diagram is born as a Mermaid sketch, inside the corresponding markdown file. There is no rendering pipeline: nothing in this project turns Mermaid into the inline SVG mechanically. The sketch is a plain-text structural plan, readable as a diff and rendered natively by GitHub when the file is viewed there, nothing more.

The inline SVG in the HTML is drawn by hand, in the project's own visual system, matching the sketch's structure. This is deliberate, not a shortcut skipped for lack of tooling: a generic Mermaid renderer outputs its own theme and its own automatic layout, neither of which matches this project's thin-stroke, no-fill, no-colour system, so hand-drawing is the direct path, not a workaround.

When structure or a label changes, change the Mermaid sketch first, then redraw the SVG by hand to match it. Changing only the SVG leaves the sketch out of date, and the next session works from the wrong map.

Each diagram carries, in the markdown, its purpose and a rendering note, including what needs to jump out at the reader and the sentence the caption carries.

---

## Glossary

Book style. Alphabetical order ignoring accents. No rule between entries. Term in bold, colon, definition on the same line, origin at the end in italic with a link. Hanging indent.

In body text, the term appears with a dotted underline, with a tooltip on hover and a link to the entry.

Proper names are alphabetised by surname: "Deming, W. Edwards".

---

## References

**Link only where the URL has been verified.** When the source is known but the address has not been checked, the source appears in plain text with no link.

References point to the primary source, never to a consultancy blog or a skill showcase with no visible origin repository.

An inventory that only recommends is not an inventory, it is a vendor catalogue. Every entry also states when not to use it.

---

## Cross-navigation

Four layers, all implemented:

1. Series bar at the top of every document, next to the language selector.
2. In-body links: mentions of a tier or of MEDIR lead to the corresponding section of Part 1. Mentions of a tool lead to its entry in the compact guide.
3. A "Where you are" block at the end of every piece.
4. A glossary with a single wording per entry, replicated across documents.

---

## Languages

English is this project's primary production language for both public repositories, decided 30 August 2026. New content is authored in English first; Portuguese and Spanish are full translations produced from it, not the other way round. This does not require redoing content that was already complete in all three languages before that date.

Three complete versions per piece, in the same file, with a selector. English is the default tab.

**Spanish:** "tú" register, not "usted".
**English:** British spelling.
**MEDIR** stays as the method's proper noun in all three languages.

Anchor identifiers and SVG markers are prefixed by language. Never generate new content without passing it through the `scope()` function.

A browser-language hint applies on the four trilingual HTML pages: if the visitor's browser language is Portuguese or Spanish and does not match the active tab, and no language-prefixed hash is already routing the page, a dismissible banner in that language offers to switch. Any other browser language falls back to English silently. GitHub renders the skill repository's Markdown files without executing JavaScript, so the equivalent there is a static language-navigation line at the top of every file, not an adaptive one.

---

## Tool entry in the compact guide

Six fields, always in this order, in prose rather than a loose list:

1. What problem this solves
2. What you gain in practice
3. Who it is for, by tier N0 to N3
4. Minimum tier
5. When not to use it
6. How to start in fifteen minutes

---

## Skill-writing pattern

Inherited from the best public collections and adopted as this project's standard:

**Non-negotiable rule at the top,** short and unambiguous.

**Red flags right below it:** the rationalisations the system will likely use to justify not following the rule. The target is not teaching the rule, which it already knows, it is stopping it from talking itself out of following it.

**A verifiable done criterion,** preferably the output of a command rather than an opinion.

**An attempt ceiling** with an explicit exit path.

**A Never section** at the end.

**Honest limits** stated: what has been exercised, what is inference, what the skill does not do.
