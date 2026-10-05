*Read this in [Português](README.pt.md) · [Español](README.es.md).*

# build

Text bodies and assembly scripts that generate the HTML pages at the repository root, plus the checks that keep them honest.

## How it works

Each page is assembled from two parts: an HTML body per language, and a Python script that prefixes every identifier by language (`scope()`), finishes each language block (`common.py`) and pastes it all into the shared CSS shell.

The shell is extracted from the finished page that already exists, so every page stays identical in formatting. Change the CSS in one page and regenerate the others, and the change propagates.

Pages built here: `harness-p1.html` to `harness-p4.html`, `harness-toolkit.html`, `harness-playbook.html`, `harness-glossary.html`, `harness-sources.html` and `docs/logbook.html`.

## Files

| File | Role |
|---|---|
| `body_p1_{pt,en,es}.html` | Part 1 bodies, extracted from the published `harness-p1.html` on 5 October 2026. The PT body is rewritten on every build; EN and ES are editable |
| `body_p2_{pt,en,es}.html` | Part 2 bodies. The PT body is rewritten on every build; EN and ES are editable |
| `body_p3_*`, `body_p4_*`, `body_playbook_*`, `body_toolkit_*`, `body_glossary_*`, `body_sources_*` | Bodies of the other pages, one per language, all editable. These are the source of truth |
| `build_p1.py`, `build_p2.py` | Assemble Part 1 and Part 2. Self-referential: the shell and the PT body are read back from the page as published |
| `build_p3.py`, `build_p4.py`, `build_playbook.py`, `build_toolkit.py`, `build_glossary.py`, `build_sources.py` | Assemble the other pages from the three `body_*` files of each. Never read the published page back |
| `build_logbook.py` | Assembles `docs/logbook.html` in three languages from `docs/assets/logbook-metrics.json`, including the cost chart |
| `common.py` | Rules shared by every assembly script: the top anchor and the language fragment on cross-page links, the `lang` attribute on each `<main>` |
| `generate_logbook_metrics.py` | Rebuilds `docs/assets/logbook-metrics.json` from git, from the real session transcripts and from `docs/assets/prices.json`, never edited by hand. Modes: normal, `--recount`, `--reprice`, `--enrich [--dry-run]`, see below |
| `docs/assets/prices.json` | Dated, append-only price ledger (source data, not a script). A milestone reads the entry in force on its own date and the computed cost is frozen afterwards |
| `generate_toolkit_manifest.py` | Rebuilds `toolkit.json` from `TOOLS.md`, `sources/inventory.md` and `playbook/README.md`, never edited by hand. `--check` only reports whether it is stale |
| `check_all.py` | The single verifier, see "Checks" below |
| `check_glossary_order.py`, `check_readme_snapshot.py` | Two checks that `check_all.py` runs, also usable on their own |
| `check_known.json` | Findings that existed before `check_all.py` did. A ratchet: it may only shrink |
| `stop_hook.py` | Claude Code stop hook, wired in `.claude/settings.json`: runs `check_all.py` when a session changed published files and keeps the session from ending on a new finding |
| `legacy/` | `build_all.py`, `build_en.py` and `patch_p2.py`, historical, moved here on 5 October 2026 so that no agent runs them by mistake. The first two use fixed sandbox paths and do not run in this repository; `build_p1.py` replaced them |

## Checks

`python build/check_all.py` runs ten checks in one pass: dashes, glossary order, the README chart alt text, `toolkit.json`, links and anchors, consistency between parts, facts repeated between the glossary and the parts, missing accents in Portuguese and Spanish, American spelling in English, and parity of sections, tables, SVG and tooltips across the three languages. Every finding names the file, the line, the passage and the expected fix.

Findings that existed before the script are recorded in `build/check_known.json` and do not fail the run. Any finding outside that list does. When one is fixed, the script says so, and `python build/check_all.py --write-baseline` drops it from the list. The list may only shrink. `--only NAME` runs one check, `--strict` ignores the list, `-v` prints the known findings too.

Two things run it without being asked: the stop hook (`stop_hook.py`), which protects a working session, and `.github/workflows/check.yml`, which protects the published site on every push and pull request, hand edits included. The hook's configuration and script are the part of the setup that should change only with a person reading the diff.

## Critical rules

`scope()` prefixes anchor identifiers and SVG markers by language. All new content has to go through it, or the three versions of the same document collide and anchors point at the wrong language. Write the EN and ES bodies without a language prefix in ids and anchors (`id="opening"`, not `id="en-opening"`), because `scope()` adds it at build time.

`build_p1.py` and `build_p2.py` extract the PT body straight from the published page, which is the source of truth, and rewrite `body_p1_pt.html` and `body_p2_pt.html` on every run. Edit the PT text of Part 1 or Part 2 in the published page, then rebuild. Before 5 October 2026 Part 1 had no build script at all: its PT and ES bodies existed only inside the assembled page, and `body_en.html` had drifted a whole revision behind it.

The other six scripts do **not** read the published page back. They read the three languages from `build/body_*`. Editing a published page by hand without mirroring the change in its body is invisible until the next regeneration, which reverts it without warning. That happened on 31 August 2026, when `build/body_sources_*.html` ended up two rounds of citation fixes behind `harness-sources.html`. Run the script after any direct edit, or edit only the body and let the script assemble the final file.

Cross-page links in a body are written without a fragment (`href="harness-p2.html"`). `common.py` rewrites them to `harness-p2.html#pt-top`, `#en-top` or `#es-top`, depending on the language block they sit in, because the language switch reads the prefix of the URL to choose the tab before scrolling. A link with no prefix, or with the wrong language's prefix, opens the other page on the English tab. Links with an explicit anchor need the target language's prefix (`#en-opening`, `#es-apertura`, `#pt-abertura`). Each language block also starts with an element whose id is `<lang>-top`, carries a `lang` attribute (`pt-BR`, `en-GB`, `es`), and the tab title follows the language switch, taken from the block's `<h1>`.

Renaming a glossary term changes the letter that decides its position but does not move the row: run `python build/check_glossary_order.py` after any terminology change, before rebuilding. Found on 11 September 2026, when two Portuguese entries stood out of order for eleven days without anyone noticing, see `NEXT-STEPS.md`.

Editing `TOOLS.md` (the table of installed collections, or the list of skills per collection) or the "Tools and skills" table of `sources/inventory.md` without running `python build/generate_toolkit_manifest.py` afterwards leaves `toolkit.json` stale, the same way editing `harness-sources.html` without mirroring it in `build/` lets the next build revert the edit. `--check` reports the divergence (a hash of the source sections) and writes nothing.

## Money cost, ported back from `milestone-loc-tokens-ai-ledger`

On 14 September 2026 `generate_logbook_metrics.py` gained the same dated, append-only price logic that the skill this project produced (`milestone-loc-tokens-ai-ledger`, see `NEXT-STEPS.md` item 5) had already built: `load_price_ledger`, `find_price_series`, `price_at` and `compute_cost`, reading `docs/assets/prices.json`. The cost of a milestone is computed once, at the price in force on that milestone's date, and never recalculated afterwards, even if the ledger gains a new entry. `load_previous` guarantees this by reading the previous run's `logbook-metrics.json` before overwriting it.

**A wrong price, corrected on 20 September 2026.** The 13 September entry recorded Sonnet 5 at US$3/15, but the price charged is US$2/10 (the increase planned for 1 September was cancelled, according to Anthropic's pricing page read on the day, together with the model overview). The wrong entry stays in the ledger, and a second one, with `corrects` and the reason, replaces it: on a date tie, `price_at` picks the entry written later. Since a recorded cost is never recalculated by a normal run, `python build/generate_logbook_metrics.py --reprice` is the explicit, audited way to handle such a case, ported from `milestone-loc-tokens-ai-ledger`: it recalculates only the cost of milestones already recorded, from the tokens already recorded in them, without reading git or any transcript, and keeps the previous cost in `repricings` inside the milestone. Running it again with no new ledger entry changes nothing. Do not use `--reprice` for an ordinary price change: an entry with a later `effective_date` already leaves each old milestone at the price in force on its date.

**The limit of the reprice, closed on 20 September 2026.** `tokens_bucket` holds only the four original counters, because that is how `build_logbook.py` sums them (`sum(m['tokens_bucket'].values())`). The port used to price every cache write at `cache_creation_price`, and in this project's transcripts every cache write read is a 1-hour one, at a higher price. The split by model and by cache TTL now lives in a sibling key, `tokens_split`, and `price_milestone` prices each model with its own series and 1-hour writes at the 1-hour price. A 1-hour write under an entry with no `cache_creation_1h_price` is left unpriced, never priced at the 5-minute rate. The 79 milestones that already existed were migrated with `--enrich`, and the recorded cost of the 14 that had one went from US$77.7944 to US$83.1673 (+US$5.3729), measured milestone by milestone.

**An honest limit, not hidden.** `docs/assets/prices.json` has three series, all from 13 September 2026: Sonnet 5, Opus 5 and Haiku 4.5. The last two entered on 20 September 2026 under an assumption recorded in each entry (the price read that day holds since 13 September, with no source dating the change), see `NEXT-STEPS.md` item 6. Every earlier milestone shows `cost_recorded: null` in the output and "unpriced" in the published log, never an invented cost. That is expected, not a bug: this script does not state a price it did not verify. Unlike the token engine itself (one continuous session covering the whole project), an LLM price changes by the vendor's commercial decision, not by this project's use, so it cannot be rebuilt retroactively without a real source for each date.

## Freezing, `--enrich` and `--recount`, ported from `milestone-loc-tokens-ai-ledger` on 20 September 2026

The rule: freeze the finest-grained fact and derive the price later. A recorded cost is a derived number; the tokens, by model and by cache TTL, are the fact.

- **Normal run.** Never reopens the tokens of a milestone already recorded (`tokens_bucket`, `tokens_split`): they come from the file, not from the transcript, because Claude Code deletes transcripts after `cleanupPeriodDays` (30 days by default). Only a new commit derives tokens. Words and lines are also reused per commit hash, as long as `count_rules_hash` (a fingerprint of `CONTENT_HTML`, `CODE_GLOBS_PREFIXES`, `GOV_DOCS` and `COUNT_ALGORITHM_VERSION`) is the same as in the run that recorded them. Without the mark, or with a different one, the script recounts everything and says why; the first full recount took about eight minutes, a normal run takes about a second. **Raise `COUNT_ALGORITHM_VERSION` whenever `word_count_html` or `line_count` changes behaviour**, or the frozen counts keep applying under a rule that is no longer the same.
- **`--recount`.** Forces a recount of words and lines for every milestone and prints every difference against what was recorded. It is the proof that a refactor moved no published number.
- **`--reprice`.** As before, now with pricing by model and by TTL: recalculates only the cost, from the recorded tokens, without reading git or transcripts.
- **`--enrich [--dry-run]`.** The one-off migration of a milestone recorded before the split by model and TTL. It enriches a milestone only if its four original counters, re-derived from the transcripts, are exactly equal to the recorded ones; otherwise it refuses and leaves it untouched, and the exit code is 3. A milestone with a recorded cost has the cost recalculated and gains a `repricings` entry with `"reason": "enrich"`; one with no cost only gains the token split. **Read the `--dry-run` report before running for real, and commit `logbook-metrics.json` first**, so the previous state is in git. It has a deadline: once the transcript expires, the milestone can no longer be enriched.
- **Subagents.** Claude Code files subagent transcripts under `<session>/subagents/*.jsonl`, not beside the parent session, and this script never read them until 20 September 2026 (about 257 million tokens that day, a fifth more than the total counted). Since then they **count**, by the author's decision: they are captured per milestone in `subagent_tokens` (a frozen fact, by model and TTL), and what the totals, the charts and the cost read is `tokens_total`, the sum of `tokens_bucket` (parent sessions) and `subagent_tokens`, derived on every run, never frozen. `tokens_bucket` and `tokens_split` remain parent sessions only, because they are the fact the `--enrich` guard checks against the transcript. A subagent token is attributed to the next commit of this repository, wherever the work happened, and 43 of the 114 transcripts also name another repository's path (41 of them `milestone-loc-tokens-ai-ledger`, whose own log counts those 41 by its path): the two logs must not be added together. `--reprice --note TEXT` records the reason in each `repricings` entry.
- **`unpriced`.** The list of unpriced tokens is only recorded on a partial cost. A milestone with no cost at all already says everything with `cost_recorded: null`.

## When regenerating the project log, in order

The log describes earlier commits, so regeneration comes after them. The commit of the regeneration itself is always the only milestone with no narrative, and the next regeneration describes it.

1. `python build/generate_logbook_metrics.py` (about a second; recount everything only with `--recount` or if the counting rules change).
2. Write the narrative of the new milestones in `COMMIT_TXT`, in `build_logbook.py`, in three languages. The build stops with a `KeyError` on the missing hash, on purpose.
3. `python build/build_logbook.py`.
4. Re-export the README's three charts from `docs/logbook.html` into `docs/assets/logbook-*.png`, with an exact crop of 616 by 230 at 2x, which gives 1232 by 460 (without the crop it comes out 462).
5. Update, in the three READMEs, the alt text of the words chart (words and number of milestones) and check with `python build/check_readme_snapshot.py`.
6. `python build/generate_toolkit_manifest.py --check`, then `python build/check_all.py`.

## If `generate_logbook_metrics.py` is reused in another repository

Found by direct reuse in a smaller external project, recorded in `NEXT-STEPS.md`: the script works well here, but it carries three implicit decisions that need manual adjustment before it runs anywhere else, none of them exposed as a command-line parameter.

1. **The session directory suffix** (`target_suffix` in `_project_dir()`, used by `find_session_jsonl()` and `find_subagent_jsonl()`) is specific to this clone, on this machine. There is no safe way to discover it algorithmically, since Claude Code's path sanitisation is an undocumented internal detail. List `~/.claude/projects/` once and confirm the real name before changing the suffix.
2. **`CONTENT_HTML`, `CODE_GLOBS_PREFIXES` and `GOV_DOCS`** are hardcoded for this repository's file structure. Rewrite all three in full for any other project.
3. **Usage deduplication by `message.id`**, inside `load_usage_events()`, has to be in any new copy of this script from the start. Without it the token count doubles (a real finding here, fixed in September 2026, see `NEXT-STEPS.md`), because a single assistant message produces more than one line in the transcript, each carrying the whole message's running total, repeated.
