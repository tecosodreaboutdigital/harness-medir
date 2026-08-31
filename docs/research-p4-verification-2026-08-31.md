# Part 4 follow-up verification: three unresolved claims

Verification pass. Raised 31 August 2026, against `harness-p4.html` as it stood that day. Follows the method in `.claude/skills/research`: trace every claim to the source that owns it. Kept in English, matching `sources/inventory.md`'s own rule that internal verification ledgers sit outside the project's PT/ES/EN translation policy (they are working tools for whoever writes the articles, not reader-facing).

**Legend.** **V** verified by direct reading (WebFetch/curl against the live page or a search result with a confirmed URL). **P** partial, existence confirmed but not read directly. **N** not found / does not support the claim.

---

## Summary of verdicts

| # | Claim | Verdict |
|---|---|---|
| 1 | Veza 824,000 orphaned identities / ~8% / 17:1 ratio, cited via CloudEagle | **FOUND** — exact match, but at a different source. CloudEagle mis-citation confirmed wrong |
| 2 | Deloitte, "89% of agent pilots never reach production" | **PARTIALLY FOUND** — real Deloitte number exists (11% in production), but "89%" and "pilots... never reach production" is not Deloitte's own phrasing |
| 3 | 2025 ransomware breach via a "ghost vendor" account never deactivated | **FOUND** — real, specific, dated incident. The article already cites the source elsewhere in the same paragraph, just not on this sentence |

---

## 1. Veza's non-human-identity survey figures

**Claim in `harness-p4.html`.** Via a CloudEagle blog citation, attributed to "Veza's 2026 identity survey": 824,000 orphaned active identities, about 8% of a typical identity provider's total users, all still holding live access rights; a machine-to-human identity ratio near 17 to 1; dormant accounts nearly doubled in a year; orphaned identities up about 40%.

### What was wrong with the current citation

The current link, `https://www.cloudeagle.ai/blogs/why-every-team-is-quietly-building-up-non-human-identity-debt`, does **not** contain these numbers.

- Fetched and read in full (via WebFetch, then independently via raw `curl` + `grep` on the HTML source, to rule out a JS-rendering gap). Neither pass found 824,000, 8%, 17:1, or any doubling/40% figure anywhere on the page.
- The only string "Veza" anywhere in the page's HTML is a site-footer nav link, "CloudEagle.ai vs Veza" — a competitor-comparison page link that appears site-wide, unrelated to the blog's content. The page's own concrete number is a single CloudEagle customer case study (Armorcode: non-human-identity visibility 40% → 95%, 480 unmanaged accounts remediated, 220 over-permissioned ones scoped down) — a product testimonial, not an industry survey stat.
- **Wayback Machine check** (requested explicitly, since `sources/inventory.md` records this URL as verified "V" on 30 August 2026 with these exact numbers quoted): queried both the Wayback `availability` API and the full CDX index directly via `curl` (WebFetch itself refuses `web.archive.org` as a host). Result: **zero snapshots exist for this URL, at any date.** `archived_snapshots: {}`; CDX search returns `[]`. This rules out "the page was edited in the last day" as a provable explanation — there is no archived version, past or present, to compare against. The more likely explanation is that the 30 August verification conflated this CloudEagle page with the real Veza report (which was fresh, widely covered news at the time) rather than reading the CloudEagle page itself closely enough. Worth flagging in `sources/inventory.md` as a correction, in the spirit of this project's transparency standard, rather than silently fixing it.

### The real source

Veza published its own first-party research: the **2026 State of Identity & Access Report** (Veza's proprietary analysis of identity/entitlement data — millions of identities, 230+ billion permissions — across large global enterprises), announced via Veza's own press release on **11 December 2025**.

Primary (Veza's own domain):
- Press release: `https://veza.com/company/press-room/veza-identity-access-research-report-reveals-identity-permissions-sprawl-has-reached-critical-levels-amid-explosion-of-machine-and-ai-agent-identities-across-the-enterprise/` — **V**, read directly. Quotes: "824,000 orphaned accounts (8% of all accounts)" with no owner in HR systems but retaining live entitlements; "Machine identities now outnumber human users 17:1"; "roughly 3.8 million dormant accounts... representing 38% of all identity provider users."
- Report landing page: `https://veza.com/resources/the-state-of-identity-access-2026/` — **V**, read directly, corroborates the 8% orphaned figure and the 17:1 ratio (the gated full report itself was not accessed; the landing page and press release together are enough to confirm the figures).

Secondary, correctly attributing to Veza, and the source that fills in the two growth-rate figures the landing page/press release don't spell out on their surface:
- Help Net Security, "Non-human identities push identity security into uncharted territory," 30 December 2025: `https://www.helpnetsecurity.com/2025/12/30/identity-security-permissions-sprawl/` — **V**, read directly. States explicitly: orphaned identities "increased by approximately 40% year-over-year," and dormant accounts "nearly doubled year over year" — matching the remaining two figures in the `harness-p4.html` claim exactly, correctly attributed to Veza's report throughout.

### Exact-match check

All five sub-figures in the `harness-p4.html` claim match the real Veza report precisely:

| Figure in the article | Veza's real number |
|---|---|
| 824,000 orphaned active identities | 824,000 orphaned accounts — exact match |
| ~8% of a provider's total users | 8% of all accounts — exact match |
| Machine-to-human ratio near 17:1 | "outnumber human users 17:1" — exact match |
| Dormant accounts nearly doubled in a year | "nearly doubled year over year" — exact match |
| Orphaned identities up ~40% | "increased by approximately 40% year-over-year" — exact match |

No discrepancy to note — this is a rare case where every number in the article is exactly right, just attributed to the wrong (and non-supporting) URL.

### Recommendation

Replace the CloudEagle citation in `harness-sources.html` (all three languages) with a genuine Veza citation: the press release as primary, Help Net Security as secondary corroboration for the two growth-rate figures. Update `sources/inventory.md`'s Part 4 axis 1 row accordingly, and add a one-line correction note there (the CloudEagle URL was recorded "V" on 30 August in error; it does not and, per an empty Wayback history, apparently never did contain these figures). Drop the CloudEagle URL from the citation entirely — it does not support the claim.

---

## 2. Deloitte's "89% of agent pilots never reach production"

**Claim in `harness-p4.html`.** A table row: "89% of agent pilots never reach production," cited to "Deloitte, 2026" with no link, already flagged in the document itself as "(unverified at the primary source)."

### The 89% figure is unstable across secondary sources

A wide search turned up the "89%" figure (and close variants — 78%, 86%, 88%) repeated across a cluster of near-identical SEO/content-marketing articles about "the AI agent pilot-to-production gap," e.g.:

- `digitalapplied.com` (two of its own posts disagree with each other: one titled around "88% of AI agents never reach production," another citing "89% failures traced to 5 root causes" from **its own** March 2026 survey of 650 leaders — not Deloitte at all)
- `beri.net`, headlined "89% of AI Agent Pilots Never Scale: Gartner's 2026 Data" — fetched directly, and the 89% figure **does not appear anywhere in the article body**; the only figure actually attributed to Gartner there is "40% of agentic AI projects will be canceled by 2027"
- `mywrittenword.com` ("86%"), `zenvanriel.com` ("78%")

This spread of different numbers across nearly-identical articles, several of which cite each other or cite nothing at all, is a strong signal of an unverifiable statistic circulating through content farms rather than a single stable, citable figure. One source, `luizneto.ai`, does explicitly attribute "89%" to "Deloitte's 2026 Tech Trends report" and links to a real Deloitte URL — this lead was followed to the primary source.

### What Deloitte's own report actually says

Fetched directly: `https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html` — Deloitte Insights, "Agentic AI strategy," a chapter of **Tech Trends 2026**, dated **10 December 2025**, citing "Deloitte's 2025 Emerging Technology Trends study" (footnoted in the piece as "publication in process," so respondent count and survey window are not disclosed on the page itself). **V**, read directly.

The exact sentence on Deloitte's own page:

> "...while 30% of surveyed organizations are exploring agentic options and 38% are piloting solutions, only 14% have solutions that are ready to be deployed and a mere 11% are actively using these systems in production."

The literal string "89%" does not appear on this page, and neither does the phrase "never reach production." Also checked Deloitte's companion page, "The State of AI in the Enterprise" (`https://www.deloitte.com/us/en/what-we-do/capabilities/applied-artificial-intelligence/content/state-of-ai-in-the-enterprise.html`) — no matching pilot-failure statistic there either; its closest content is a different point about production-scale growth doubling in six months.

### The likely origin, and why "89%" overstates it

100 − 11 = 89. The circulating "89%" figure is evidently the arithmetic complement of Deloitte's real, directly quotable number — 11% of surveyed organizations actively using agentic AI in production — recast by secondary sites as "89% of pilots never reach production." That recasting is imprecise in two ways: (a) Deloitte's own pipeline (30% exploring / 38% piloting / 14% ready-to-deploy / 11% in production) is not framed as "pilots that failed" — it lumps together organizations that never started piloting at all with those that piloted and stalled; (b) Deloitte never states an aggregate "pilots that don't reach production" rate as its own headline figure.

### Recommendation

The in-document flag ("unverified at the primary source") was the right call — do not resolve it by inventing a firmer attribution than the evidence supports. Two ways to close it out:

- **Preferred:** replace the sentence with Deloitte's own, directly quotable number and framing — e.g. "only 11% of surveyed organizations are actively running agentic AI in production" — and cite `https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html` directly. This finally gives Part 4 a working Deloitte link (today's only Deloitte source in the bibliography is the unrelated Three Lines of Defense piece), and the real pipeline breakdown (30/38/14/11) is, if anything, a more concrete and citable number than a bare "89%."
- **Alternative**, if the rhetorical shape of "89%" is wanted for the table: keep it but reframe honestly, e.g. "roughly nine in ten surveyed organizations have not moved agentic AI into production, by Deloitte's own numbers (Tech Trends 2026)" — explicit that this is a derived reading of Deloitte's pipeline stages, not a stat Deloitte itself published as "89%."

---

## 3. The 2025 ransomware "ghost vendor" incident

**Claim in `harness-p4.html`.** Sitting between two cited sentences (Colonial Pipeline 2021, and the 2026 GitHub dormant-accounts case) in the same paragraph, with no citation at all: "A 2025 ransomware victim was entered through a ghost vendor account that had never been formally deactivated."

### The incident exists, is specific, and is dated

Primary source: Barracuda Networks' own MDR blog, first-party account of an incident their team detected and contained.

> **The SOC case files: XDR catches Akira ransomware exploiting 'ghost' account and unprotected server**, published **5 February 2025**. `https://blog.barracuda.com/2025/02/05/soc-case-files-akira-ransomware-ghost-account` — **V**, read directly.

Details confirmed from the source: an unnamed manufacturing company (company name withheld, standard for an MDR vendor's own case-study writeups) was breached via an account "created for a third-party vendor" that "was not deactivated when they left" — Barracuda's own words, and the origin of the term "ghost account" in its title. Attackers used the account over an open VPN channel, attempted lateral movement and endpoint-security tampering (both blocked), pivoted to an unprotected server, and deployed **Akira** ransomware. Barracuda's Managed XDR detected and isolated all affected endpoints within about four minutes of the ransomware launching; the SOC restored from snapshots and the post-incident review flagged the VPN/MFA gap.

### It is already inside this article's own bibliography — just not linked on this sentence

The Hacker News, "The Hidden Risk of Orphan Accounts," January 2026 — already cited elsewhere in this exact paragraph of `harness-p4.html` (`harness-sources.html#pt-src-thn-orphan` / `#en-src-thn-orphan`, used today only for the neighboring Colonial Pipeline sentence) — retells this same incident, citing Barracuda's analysis: "breach came through a 'ghost' third-party vendor account that wasn't deactivated." `https://thehackernews.com/2026/01/the-hidden-risk-of-orphan-accounts.html` — **V**, read directly, confirms this is the same case as the Barracuda write-up (same "ghost" framing, same vendor-account mechanism, same 2025 dating).

### Recommendation

This is not a case of an illustrative composite that needs softening — it is a real, specific, dated incident, already inside the article's own source list. **Fix by citation, not by rewriting the claim.** Two options, not mutually exclusive:

- **Minimum fix:** add the existing `harness-sources.html#...-thn-orphan` anchor to the currently-uncited sentence — the source is already doing this job for its neighbor in the very same paragraph, and it explicitly covers the 2025 case too.
- **Stronger fix:** add a new `harness-sources.html` entry citing Barracuda's original blog post directly (`https://blog.barracuda.com/2025/02/05/soc-case-files-akira-ransomware-ghost-account`) as the primary source for this sentence specifically, since The Hacker News is itself a secondary retelling of Barracuda's own case file. Update `sources/inventory.md`'s Part 4 axis 6 (narrative cases) table to add this row.

---

## Files touched by this research

- Read for context: `harness-p4.html`, `harness-sources.html` (not modified), `sources/inventory.md`, `docs/research-part4.pt.md`
- New: this file, `docs/research-p4-verification-2026-08-31.md`
