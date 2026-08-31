# Research: four uncited or under-cited claims in Parts 1 and 2

Gathered 31 August 2026, against primary sources only: the actual benchmark's own blog post, the actual arXiv paper, the actual tweet, the actual essay — never a summary, a secondary aggregator, or a consultancy's paraphrase.

**Scope.** Four specific claims flagged in `harness-p1.html` and `harness-p2.html` as either already hedged ("without a single locatable primary source") or asserted without a link to a primary source for half of the sentence. This file is a working dossier, not the article. Verified content that survives should migrate into `sources/inventory.md` and `harness-sources.html` in the usual flow.

**Language.** This file stays in English only. Like `sources/inventory.md`, it is an internal verification tool for whoever writes the articles, not reader-facing content, so it sits outside the project's English/Portuguese/Spanish translation policy (see `STANDARDS.md`'s `Languages` section).

**Legend.** **FOUND** — a primary source directly confirms the claim, read or fetched directly, with URL. **PARTIALLY FOUND** — a primary source confirms part of the claim, or confirms an adjacent/looser version of it. **NOT FOUND** — no primary source located after a genuine search effort; the gap should be stated, not papered over.

**Method note on X/Twitter.** This session's fetch tool returned `HTTP 402 Payment Required` on every `x.com` URL tried (the platform blocks unauthenticated scraping). Tweet content and dates below are therefore confirmed the way `sources/inventory.md`'s own legend allows for **V**: "a search result with a confirmed URL" — the search engine's indexed snippet reproduces the tweet's exact text under its exact permalink. This is short of opening the page directly, and is flagged as such in claim 4.

---

## Claim 1: LangChain benchmark climb (30th to 5th, +13.7 points, harness-only)

**Claim text.**

> PT: "A LangChain melhorou apenas o harness do próprio agente e subiu do trigésimo para o quinto lugar em um benchmark público, com ganho de 13,7 pontos, sem trocar o modelo."
>
> EN (live): "LangChain improved only its own agent's harness and rose from thirtieth to fifth place on a public benchmark, a gain of 13.7 points, without changing the model."

**Search process.** Started with a targeted web search combining the exact numbers ("30th to 5th", "13.7"). This surfaced the primary source on the first attempt: LangChain's own engineering blog. Confirmed by fetching that post directly and asking it to quote its own numbers verbatim. Cross-checked the benchmark's identity and the leaderboard's existence via a second search, then attempted to fetch the live leaderboard directly to see if the same rank/score pair was still visible.

**What was found.** LangChain published this as its own blog post: **Vivek Trivedy, "Improving Deep Agents with harness engineering," 17 February 2026**, `https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering`. Fetched directly. Exact quotes pulled from the page:

- Headline claim: "Our coding agent went from Top 30 to Top 5 on Terminal Bench 2.0. We only changed the harness."
- Exact score: "We used a simple recipe to iteratively improve deepagents-cli (our coding agent) 13.7 points from 52.8 to 66.5 on Terminal Bench 2.0."
- Model held constant, stated explicitly: "We only tweaked the harness and kept the model fixed, `gpt-5.2-codex`."
- Benchmark identity: "We used Terminal Bench 2.0, a now standard benchmark to evaluate agentic coding. It has 89 tasks across domains like machine learning, debugging, and biology," with a link to `https://www.tbench.ai/leaderboard/terminal-bench/2.0`.

Every element of the claim — the rank range, the point delta, the before/after scores, the named benchmark, and the harness-only framing — comes from LangChain's own account of its own work, dated and named to an individual author.

Attempted to independently reproduce the Feb 2026 snapshot on the live leaderboard at `tbench.ai/leaderboard/terminal-bench/2.0`. The page is JavaScript-rendered and returned no scraped rows; separately, other August 2026 search results describe the benchmark as having since moved to a "2.1" revision that "fixes 28 of 89 tasks" and even references a "Terminal-Bench 4.0" resolution-rate metric on the live site. The original rank snapshot is not independently reproducible from today's leaderboard — which is expected and normal for a fast-moving leaderboard, and is exactly why the dated blog post, not the live leaderboard, is the citable source.

Secondary corroboration only (not needed for the verdict, but consistent): tech-press coverage of the same event under a slightly different framing, e.g. "LangChain Jumps 25 Spots on AI Benchmark Without Changing the Model" (MEXC News, blockchain.news) — 25 spots is arithmetically consistent with a 30th-to-5th move.

**Verdict: FOUND.** High confidence.

**Best candidate URL and exactly what it supports.** `https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering` (Vivek Trivedy, LangChain, 17 February 2026) confirms, in LangChain's own words: the benchmark (Terminal Bench 2.0), the rank range ("Top 30 to Top 5"), the exact point delta (13.7 points, 52.8 → 66.5), and the harness-only framing (model fixed at `gpt-5.2-codex`). One precision nuance worth carrying into the text: LangChain's own headline says "Top 30 to Top 5," which most plausibly means the two rank positions the article already states, but is not phrased as literally "30th place" and "5th place" the way the article renders it. This is a minor wording gap, not a substance gap — the number pair and the harness-only claim are both confirmed at the source.

**Recommendation.** Add a new `harness-sources.html` entry and cite it directly, replacing "via a secondary source" in `sources/inventory.md`'s numbers table. Suggested exact citation text (matching the house format, `Author. <em>Title</em>, date. <a href="URL">domain</a>`):

> `Vivek Trivedy, LangChain. <em>Improving Deep Agents with harness engineering</em>, 17 February 2026. <a href="https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering">langchain.com</a>`

The live sentence in `harness-p1.html`/EN can drop "without a single locatable primary source" for this half — a primary source exists and is now locatable. If the article wants to preserve exact rank-language rigor, consider softening "thirtieth" and "fifth" to LangChain's own "Top 30" / "Top 5" framing, though this is optional given how closely the two already match.

---

## Claim 2: unnamed academic harness-evolution paper (14 of 15 configs, +14.5% avg)

**Claim text.**

> PT: "E um trabalho acadêmico que automatizou a evolução do harness registrou melhora em quatorze de quinze configurações, com ganho médio de 14,5%."
>
> EN (live): "And an academic effort that automated harness evolution recorded improvement in fourteen of fifteen configurations, averaging 14.5%."

**Search process.** Searched arXiv-flavored terms combining the exact numbers: `"automated harness evolution" agent benchmark "14 of 15"`. This surfaced several 2026 arXiv papers about agent harness search/evolution (HarnessX, Harness-Bench, HarnessForge, Adaptive Auto-Harness, "Harness Updating Is Not Harness Benefit," "Agentic Harness Engineering"). The search engine's own summary of the top result already contained an exact match to both numbers, attributed to a system called AEGIS inside a paper called HarnessX. Confirmed by fetching the paper directly, twice: once via the HTML full-text mirror (`arxiv.org/html/...`) to find the results-table language, once via the abstract page (`arxiv.org/abs/...`) to get the submission date and author count.

**What was found.** **arXiv:2606.14249, "HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry,"** submitted 12 June 2026 (v1), 14 authors (Tingyang Chen et al.), subject `cs.AI`. No author affiliation is shown on the arXiv abstract page itself. Fetched full text directly. Exact quote, pulled from the results section:

> "AEGIS improves 14 of 15 model–benchmark configurations, with an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest."

The paper explains the "15" as 5 benchmarks × 3 model/task-agent families = 15 configurations, evolved over up to 15 rounds each via AEGIS, described as a "trace-driven multi-agent evolution engine" — i.e., exactly "an academic effort that automated harness evolution." The single non-improving configuration is named explicitly: GAIA with GPT-5.4 (Δ = 0.0%), attributed by the authors to "a fundamental limitation of single-harness evolution on heterogeneous task sets." A results table (Table 4, "Main results (pass@2 success rate, %)") backs the number.

This is as close to a word-for-word match as this kind of claim gets: both "14 of 15" and "14.5%" appear verbatim, together, in the same sentence of the primary source.

**Verdict: FOUND.** High confidence.

**Best candidate URL and exactly what it supports.** `https://arxiv.org/abs/2606.14249` (abstract, submission metadata) and `https://arxiv.org/html/2606.14249` (full text with the results-table language) jointly confirm: the exact "14 of 15" configuration count, the exact "+14.5%" average gain figure, the identity of the one non-improving configuration, and that the mechanism (AEGIS) is precisely an automated harness-evolution system, run by an academic team and published on arXiv. Nothing in the claim exceeds what the paper states.

**Recommendation.** Add a new `harness-sources.html` entry and cite it directly, replacing "Academic work on automatic harness evolution" (unlinked) in `sources/inventory.md`'s numbers table. Suggested exact citation text (matching the house format used for the project's other arXiv entries, e.g. `pt-src-arxiv-audit`):

> `arXiv 2606.14249. <em>HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry</em>. AEGIS module: "improves 14 of 15 model–benchmark configurations, with an average gain of +14.5%." <a href="https://arxiv.org/abs/2606.14249">arxiv.org</a>`

The live sentence's hedge ("without a single locatable primary source") no longer applies to this half either. Between claims 1 and 2, the article's entire hedged sentence can now be rewritten as a fully sourced one, or the two new source links can simply be attached to the existing sentence without changing its wording.

---

## Claim 3: "an entire category of tools" for skill/guide cleanup, five rules

**Claim text.**

> PT: "Existe hoje uma categoria inteira de ferramentas para essa limpeza. Elas convergem em cinco regras, e as regras valem mais que qualquer produto específico" — followed by the five-rule table: (1) lock behavior before touching, (2) prefer removal over addition, (3) write the plan before editing, (4) auto-revert anything that breaks the lock, (5) separate who cleans from who reviews.
>
> (No EN wording was quoted in the task brief verbatim; the EN page mirrors the PT structure and table one-for-one in the same section, "Cleanup as cadence, not as a marathon.")

**Search process.** First checked this project's own `sources/inventory.md`, which already lists `ai-slop-cleaner` (`https://github.com/yeachan-heo/oh-my-claudecode`, actually hosted under the mixed-case handle `Yeachan-Heo`) as **V**, with the note "The real source of the cleanup skill cited in Part 2." Checked `harness-sources.html` and the `harness-p2.html` body text directly for any existing citation of this tool near the five-rule table: **none exists**. The claim is currently unsourced in both the visible text and the citation apparatus, even though the project's own internal ledger already names a specific tool as standing behind it. Fetched the tool's actual `SKILL.md` directly from GitHub to check the five rules against its documented workflow word for word, then searched separately for (a) a distinct category of tools that clean up agent guide/instruction files specifically (as opposed to code), and (b) whether any curated list (e.g. this project's own cited `awesome-harness-engineering`) names a cleanup/hygiene section.

**What was found.**

*ai-slop-cleaner itself.* Fetched `https://raw.githubusercontent.com/Yeachan-Heo/oh-my-claudecode/main/skills/ai-slop-cleaner/SKILL.md` directly. Its frontmatter description: "Clean AI-generated code slop with a regression-safe, deletion-first workflow and optional reviewer-only mode." Checking each of the article's five rules against this text:

| Article's rule | Match in ai-slop-cleaner's SKILL.md |
|---|---|
| Lock behavior before touching | Close match: "Add or run the narrowest regression tests needed before editing"; "Keep regression tests green" |
| Prefer removal over addition | Near-verbatim match: "Prefer deletion over addition" |
| Write the plan before editing | Close match: "Write a cleanup plan before code" |
| Auto-revert anything that breaks the lock | **Not found.** Searched the full document specifically for "revert," "rollback," and "undo" — none of these words appear anywhere in the file. The closest idea present is "keep regression tests green" as an ongoing discipline, not a stated auto-revert mechanism. |
| Separate who cleans from who reviews | Close match: `--review` mode instructs the reviewer to "not start by editing files" and to "hand needed changes back to a separate writer pass instead of fixing and approving in one step" |

So four of the five rules are documented in this one real, named, MIT-adjacent, already-cited tool, in close-to-verbatim language. The fifth (auto-revert) is not present in this tool's own documentation as fetched.

*Whether a broader "category" exists for guide/skill cleanup specifically (as opposed to code cleanup).* This is where the claim overreaches. Two adjacent but distinct things exist, and neither one is the thing the article describes:

1. **Code-cleanup tools resembling ai-slop-cleaner.** Search terms like `"deletion-first" cleanup tool code agent 2026` return ai-slop-cleaner itself as the dominant, most-indexed result, not a wider field of comparably-documented competitors. This looks like one well-documented tool inside one project (`oh-my-claudecode`), not an established multi-vendor category yet.
2. **Agent guide/instruction-file linters (a real, different, nameable category).** Search turned up several concretely named, real tools built specifically to detect staleness in `AGENTS.md`/`CLAUDE.md`/skill-guide files: `AgentLint` (`agentlint.com`, "Freshness Check" for stale file-path references and dead npm scripts), `agents-lint` (GitHub, "detect stale paths, dead npm scripts, outdated framework patterns"), `ctxlint` (supports `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `.cursorrules`, flags stale command/file references). This category is real and directly on-topic for "guias e sensores acumulam entulho." But none of the fetched descriptions shows these tools implementing the article's rules 1, 3, 4, or 5 (lock-with-tests, plan-before-editing, auto-revert, separate reviewer) — they are read-only auditors/scorers that flag staleness, not autonomous cleanup agents that lock behavior, delete, and revert. They converge on detection, not on the article's five-rule cleanup discipline.

Also checked whether this project's own already-cited curation, `awesome-harness-engineering` (`https://github.com/ai-boost/awesome-harness-engineering`), names a cleanup/hygiene section that could anchor "an entire category." It does not: fetched directly, its closest material is a mention of Böckeler's "entropy management" and periodic drift-repair agents under a general foundations section, not a dedicated tools list for skill/guide cleanup.

**Verdict: PARTIALLY FOUND.** The claim conflates two true things into an overstated third: a real tool exists (ai-slop-cleaner) that documents 4 of the 5 rules almost verbatim, and a real, differently-scoped category exists (AGENTS.md/CLAUDE.md staleness linters) that is on-topic but doesn't implement the five-rule discipline. No single external source, and no curated list already cited by this project, proposes these five rules as a converged, named category for either code cleanup or guide/skill cleanup specifically.

**Best candidate URL(s) and exactly what each supports.**
- `https://github.com/Yeachan-Heo/oh-my-claudecode/blob/main/skills/ai-slop-cleaner/SKILL.md` — confirms 4 of the article's 5 rules in close-to-verbatim language, for **code** cleanup, as one specific tool. Does not confirm an auto-revert mechanism, and does not describe skill/guide-file cleanup specifically (it targets code slop: dead code, duplication, weak tests).
- `https://agentlint.com/` and the GitHub `agents-lint` and `ctxlint` projects — confirm a real, nameable category of tools that specifically targets stale `AGENTS.md`/`CLAUDE.md`/skill-guide content (matching the article's "guias e sensores" framing much more precisely than ai-slop-cleaner does), but do not confirm the five-rule cleanup discipline (lock-with-tests, deletion-first destructive action, auto-revert, separate reviewer) — these tools detect and score, they do not autonomously clean up under that discipline as documented.

**Recommendation.** Two changes, not one:
1. Cite `ai-slop-cleaner` directly where the five-rule table appears in `harness-p2.html`, since this project's own inventory already treats it as the real source and it currently has no link at all in the body text or in `harness-sources.html`. Suggested exact citation text (matching the house GitHub-tool format, e.g. `en-src-superpowers`):
   > `Yeachan Heo. <em>ai-slop-cleaner</em>, oh-my-claudecode. Regression-safe, deletion-first cleanup skill with an optional reviewer-only mode. <a href="https://github.com/Yeachan-Heo/oh-my-claudecode/blob/main/skills/ai-slop-cleaner/SKILL.md">github.com/Yeachan-Heo/oh-my-claudecode</a>`
2. Soften "an entire category of tools" to something that doesn't overclaim a converged multi-vendor field, e.g.: "This kind of cleanup already has a documented discipline in code-cleanup tooling, and ai-slop-cleaner states it almost rule for rule" — then keep the five-rule table, but drop or rephrase rule 4 ("auto-revert") to match what is actually documented, e.g. "revert immediately if the lock breaks" as a stated discipline rather than an implied automated feature, since the one concrete source behind the claim does not describe automatic reverting.

---

## Claim 4: Karpathy did not coin "harness engineering"

**Claim text.**

> PT: "Vale registrar, porque circula errado: não foi Andrej Karpathy. Ele cunhou 'vibe coding' e popularizou 'context engineering', mas o termo harness já circulava antes, em contextos técnicos, e quem o transformou em disciplina foi Hashimoto."

**Search process.** Four separate sub-checks, run in this order: (a) Karpathy's original "vibe coding" post — searched directly for the term plus "February 2025"; (b) Karpathy's "context engineering" post — searched directly for the term plus "2025"; (c) any instance of Karpathy using or being credited with "harness engineering" — searched the bare term, then the term with a negative filter to catch tangential mentions; (d) sanity-check on Hashimoto's own post — fetched `mitchellh.com/writing/my-ai-adoption-journey` directly.

**What was found.**

*(a) Vibe coding.* Karpathy's post, dated **2 February 2025**, at `https://x.com/karpathy/status/1886192184808149383`. Exact text, as reproduced in the search engine's indexed page title (the fetch tool could not open `x.com` directly — every attempt returned `HTTP 402 Payment Required`, so this is confirmed the way the project's own **V** legend allows, "a search result with a confirmed URL," not by opening the page): "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper." Multiple independent secondary sources (coderabbit.ai, vibecodinghistory.com, and others) converge on the same date and the same being the originating post, with no competing claimant.

*(b) Context engineering.* Karpathy's post, dated **25 June 2025**, at `https://x.com/karpathy/status/1937902205765607626`. Same access limitation and same confirmation method. Exact text per the indexed snippet: "+1 for 'context engineering' over 'prompt engineering'. People associate prompts with short task descriptions you'd give an LLM in your day-to-day use. When in every industrial-strength LLM app, context engineering is the delicate art and science of filling the context window." Multiple sources agree Shopify CEO Tobi Lütke used a closely related formulation six days earlier (19 June 2025) and that Karpathy's post is what made the label go mainstream — which is exactly why the article's own wording, "popularizou" ("popularized"), not "cunhou" ("coined"), is the more defensible verb here, and it already uses that more careful verb only for this term. The article gets this distinction right as currently written.

*(c) Harness engineering — confirming absence.* No search turned up any Karpathy post, tweet, or interview using the term "harness engineering," in either a coining or a credited-with sense. Every source discussing the term's origin (Hashimoto's own post, OpenAI's amplification, multiple 2026 blog retrospectives on the term's history) places its naming with Hashimoto in February 2026, explicitly distinct from Karpathy's own vocabulary of "vibe coding," "context engineering," and, per some 2026 retrospectives, a later "agentic engineering." No contradicting source was found.

*(d) Hashimoto sanity check.* Fetched `https://mitchellh.com/writing/my-ai-adoption-journey` directly. Confirmed: the term appears prominently, in Step 5, with a defining quote pulled directly from the page: "I don't know if there is a broad industry-accepted term for this yet, but I've grown to calling this 'harness engineering.'" The post does not credit anyone else with the term, and it does not mention Andrej Karpathy anywhere. This matches and reinforces the project's own already-**V**-rated `sources/inventory.md`/`harness-sources.html` entry for Hashimoto; no correction is needed there.

**Verdict: FOUND**, for all four parts, with one access caveat carried forward.

**Best candidate URLs and exactly what each supports.**
- `https://x.com/karpathy/status/1886192184808149383` — the "vibe coding" post, 2 February 2025. Confirmed via indexed search snippet only, not by direct fetch (platform blocks this session's fetch tool). Supports "he coined 'vibe coding'."
- `https://x.com/karpathy/status/1937902205765607626` — the "context engineering" post, 25 June 2025. Same access caveat. Supports "he popularized 'context engineering'" — and specifically supports the article's choice of "popularized" over "coined," since a near-identical formulation predates his post by six days.
- `https://mitchellh.com/writing/my-ai-adoption-journey` — fetched directly and in full. Confirms Hashimoto's post is where "harness engineering" gets its name, confirms the exact defining sentence, and confirms the post credits no one else and never mentions Karpathy.
- No URL exists to cite for "Karpathy did not say harness engineering," because a negative cannot be linked — this is stated here as a search-effort record, not as a citable fact.

**Recommendation.** No change to the substance of the live claim — it is accurate as written, and more careful than most of the secondary commentary that conflates Karpathy with the term. Two mechanical improvements only:
1. The Karpathy half of the sentence currently links "vibe coding" and "context engineering" only to the internal glossary (`harness-glossary.html`), not to any primary source. Given the `x.com` fetch limitation, this project should decide deliberately, the same way it already has for other tricky sources (see the Bölük entry's reverification note), whether to: (i) link directly to the two `x.com` URLs above despite not having opened them directly in this session — acceptable per the project's own **V** bar, which allows "a search result with a confirmed URL" — or (ii) leave them as plain text with the gap stated, per `STANDARDS.md`'s rule that an unverified address appears in plain text with the gap named. Given the strength and consistency of the secondary confirmation (multiple independent sources, same date, same exact quote, no competing claimant), option (i) is defensible; a future session with authenticated `x.com` access should still try to open both directly and upgrade the note.
2. If option (i) above is taken, suggested exact citation text for two new `harness-sources.html` entries:
   > `Andrej Karpathy. <em>"There's a new kind of coding I call 'vibe coding'..."</em>, 2 February 2025. Confirmed via indexed search snippet, not opened directly; this project's fetch tooling returns HTTP 402 on x.com. <a href="https://x.com/karpathy/status/1886192184808149383">x.com</a>`
   > `Andrej Karpathy. <em>"+1 for 'context engineering' over 'prompt engineering'..."</em>, 25 June 2025. Same access caveat as above. <a href="https://x.com/karpathy/status/1937902205765607626">x.com</a>`

No change needed to the Hashimoto citation already in place; this round's fetch reconfirms it independently.

---

## Summary table

| Claim | Verdict | Recommended action |
|---|---|---|
| 1. LangChain, 30th→5th, +13.7 points, harness-only | FOUND | Add `harness-sources.html` entry citing LangChain's own blog post (Vivek Trivedy, 17 Feb 2026); drop "without a single locatable primary source" for this half of the sentence |
| 2. Academic harness-evolution paper, 14 of 15 configs, +14.5% avg | FOUND | Add `harness-sources.html` entry citing arXiv:2606.14249 (HarnessX/AEGIS, 12 Jun 2026); drop the hedge for this half too |
| 3. "Entire category of tools" for skill/guide cleanup, five rules | PARTIALLY FOUND | Cite `ai-slop-cleaner` directly (already **V** in `sources/inventory.md` but unlinked anywhere in the live text); soften "an entire category" to avoid overclaiming a converged multi-vendor field, and adjust or drop the "auto-revert" rule to match what the one concrete source actually documents |
| 4. Karpathy did not coin "harness engineering" | FOUND | No substance change; decide whether to link the two Karpathy `x.com` posts directly (search-confirmed but not directly fetchable this session) or leave them as stated plain-text gaps per house style |
