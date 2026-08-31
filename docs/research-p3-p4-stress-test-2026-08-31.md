---
title: Adversarial research dossier — Part 3 and Part 4 concept stress-test
date: 31 August 2026
status: draft, awaiting cross-review by additional AI reviewers before any edit lands in harness-p3.html / harness-p4.html
---

# Adversarial research dossier: stress-testing the strong concepts in Part 3 and Part 4

## Why this document exists

Parts 3 and 4 of the harness-medir series carry the project's densest concentration of concepts from outside its own domain: information security, cryptography and identity, GDPR, the EU AI Act, LGPD, agent monitoring, and organisational governance. Each of those six axes cites real sources and real cases — but citing a source once, at drafting time, is not the same claim as that source still holding true months later, in a fast-moving field, at the article's own stated "present" of 31 August 2026.

This dossier does not ask "is there a source for X." It asks the harder question: **for each strong claim already published, what would the most skeptical domain expert say is wrong, dated, oversimplified, or missing — and did we go find that critique ourselves, before a reader does.**

Method: six independent research passes, one per axis, each using live web search and direct source fetches (not training-data memory alone, since almost every claim concerns 2025–2026 events at or past the assistant's knowledge cutoff). Each pass re-read the actual published English text first, then tried to break every specific claim in its axis: verify it still holds, find the strongest update or contradiction, and flag citation gaps or misattributions. Findings are marked **(V)** where the researcher opened the source directly, **(P)** where it was confirmed only through a secondary reference or a search snippet that could not be independently opened.

This is a **research artifact, not an edit**. Nothing in `harness-p3.html`, `harness-p4.html`, or the `build/` bodies that generate them has been touched. Every recommendation below is a candidate for the author's decision, cross-checked here by additional AI reviewers before anything is acted on.

The full English source text of both articles is reproduced in the appendices at the end of this file, exactly as currently published in `build/body_p3_en.html` and `build/body_p4_en.html`, so a reviewer has complete context without needing to open the repository separately.

---

## Executive summary — findings ranked by how much they matter

### 🔴 Critical — the claim is now false as of the article's own present date

| # | Location | Finding |
|---|---|---|
| 1 | Part 3, §8, Europe | The text says the November 2025 EU AI Act delay proposal "has not become law. Plan for August 2026." **This is now false.** The proposal became **Regulation (EU) 2026/1744**, in force since 27 July 2026 — six days before the original 2 August 2026 deadline it replaces. Annex III high-risk obligations (Articles 9–17, including 12 and 14, plus 26 and 27) now apply from **2 December 2027**; Annex I from **2 August 2028**. This inverts the section's own organising claim ("what already applies today over what is still pending"). One item still open: whether Article 73's 15-day incident-notification deadline rides the same deferral — the project's own already-cited source (artificialintelligenceact.eu) shows contradictory dates on its own Article 26 vs. Article 73 pages. |

### 🟠 High — real gaps or likely errors that affect the argument's authority

| # | Location | Finding |
|---|---|---|
| 2 | Part 3, §4 | "On behalf of vs. autonomous... in that survey's own words, what worries regulators most" — likely misattributed. Fetched all three plausible miniOrange source articles directly; the clean two-pattern taxonomy and the "worries regulators most" phrase appear in none of them. Same error class as the CloudEagle/Veza mixup already caught and fixed once in this project. |
| 3 | Part 3, §4 and §6 | "Narrow-scope, short-lived token issued per task" and the reversal-point receipt are described only in prose, with **no named standard** — while OAuth 2.0 Token Exchange (RFC 8693, stable since 2020), SPIFFE/SPIRE, and a brand-new IETF hash-chain audit-trail draft (`draft-sharif-agent-audit-trail-01`, published 19 August 2026) already do exactly this. The single biggest citation gap found across all six axes. |
| 4 | Part 3, §7 | The three CVEs (CVE-2025-59536, CVE-2026-21852, CVE-2026-22708) are genericised as "a code agent," but are specifically, publicly, already-patched vulnerabilities in **Claude Code** (first two) and **Cursor** (third) — naming the products strengthens the point instead of weakening it, and removes any reader's doubt about whether this is still live. |
| 5 | Part 3, §8, Brazil | ANPD's September 2025 independence is **now permanent statute** — Law 15.352/2026, sanctioned by Lula, published in the Diário Oficial in February 2026 — a much stronger citation than "per industry reporting." Separately, **PL 2338/2023** (Brazil's general AI bill), only gestured at via a secondary source about its attached SIA bill, has been stalled in committee for over two years since Senate passage (December 2024), with no rapporteur's report as of the most recent tracked date (17 June 2026) — worth naming directly. |
| 6 | Part 4, §4 | "Revised in 2020 and 2023" for the IIA's Three Lines Model — the 2023 date is **not confirmed** by the IIA's own site and appears to trace to a secondary source (Deloitte Malta) that itself omits 2020. A genuine further IIA restatement exists from **8 July 2026**, seven weeks before Part 4's own publication, and is not cited. |
| 7 | Part 4, §3 | "Almost nobody builds either one" (the two life-cycle transitions requiring human judgment) — **Microsoft's own Agent Governance Toolkit** (open-sourced April 2026, 3,300+ GitHub stars) automates both transitions, with no owner/certifier gate. A real, current, popular counter-example — one that arguably proves the article's own warning about ungated automatic deletion, if named rather than left out. |

### 🟡 Medium — attribution or currency fixes a careful reader would catch

| # | Location | Finding |
|---|---|---|
| 8 | Part 3, §6 | The blockquote "Agentic systems fail in ways that look like success..." is credited to "OpenTelemetry's own documentation." Neither live OTel blog post that could plausibly be the source contains it. It is actually **Aryan Kargwal**, quoted inside the already-cited Digital Applied article. |
| 9 | Part 4, §5 | The blockquote "Cost per completed task is the most meaningful measure..." is credited to "the foundation's own formulation" (FinOps Foundation). It is actually **N-iX / Yaroslav Mota's** own wording, citing FinOps Foundation survey data rather than quoting the Foundation directly. |
| 10 | Part 4, §5 | Morgan Stanley's "21% of S&P 500... can name one measurable AI benefit" is **stale**. Morgan Stanley's own Q2 2026 reporting (July 2026) puts the current figure at roughly 25% (full S&P 500) or 40% (AI-adopter subset) — both well above 21%. |
| 11 | Part 3, §7 | The Register's "135,000+ exposed OpenClaw instances" is the **least stable number in the whole dossier** — contemporaneous vendor scans of the same period range from ~30,000 (Bitsight) to 220,000+ (a later aggregator), a 4–7x spread from real methodology divergence, not error. |
| 12 | Part 3, §7 | ClawHavoc's "1,184" malicious-skills figure was reached roughly **three weeks after** the 1 February 2026 discovery (day-one count was 341) — presented next to "discovered and named the campaign on 1 February" it can read as a same-day figure. |
| 13 | Part 3, §3 | Meta's original rule-of-two post labelled the untrusted-content + state-change combination "safe" — Simon Willison flagged the flaw two days after publication, and Meta revised the wording to "lower risk." Worth one clause: the framework is alive and self-correcting, which is evidence for citing it, not against. |

### 🟢 Confirmed clean, or survives the hardest test tried

- The Instagram account-takeover incident opening Part 4: every detail independently corroborated across many outlets.
- SCHUFA / GDPR Article 22 core holding (Part 4, §5): still the operative precedent, no narrowing ruling found since December 2023; the EDPS published a stronger, more current, official checklist (18 May 2026) making nearly the same point — a good citation upgrade, not a correction.
- "No Brazilian tribunal has yet ruled on an agent with an external effect" (Part 3, §1; Part 4, §9): independently corroborated by a Brazilian legal-practice source stating the same thing almost verbatim. A separate, real 2026 cluster of Brazilian court actions exists — but it punishes litigants for prompt-injecting the *judiciary's own* AI, the mirror-image problem, not a Brazilian Air Canada.
- Veza's 824,000 orphaned identities / 17:1 machine-to-human ratio (Part 4, §3): confirmed and already well-sourced, but the 17:1 figure sits at the conservative end of an 8x vendor range (up to 144:1) — worth one caveat clause.
- The eight-indicators panel's own admission ("nobody else has published this panel yet," Part 4, §5): survives an active hunt for a competitor. Closest relative is Singapore's IMDA framework (Jan/May 2026), which independently recommends monitoring "human override rates" — the same instinct as "gate rejection rate," reached independently by a regulator. Worth a footnote, not a correction.
- **The single most load-bearing, most falsifiable sentence in Part 4** — "no AI governance framework in wide use... names roles equivalent to these four as a fixed structure" — was tested against ISO 42005, NIST's CAISI initiative, Singapore's 2026 agentic-AI framework, Forrester's 2026 analyst commentary, and the IIA's own AI-specific guidance, and **it survives every one of them.**
- OWASP Top 10 for Agentic Applications, the Agentic Skills Top 10, postmark-mcp, the Snyk 280+ figure, the Kyndryl report, MIT/Deloitte/S&P/IBM pilot-failure statistics (except Morgan Stanley, above): all independently confirmed with no material issue found.

---

## Axis 1 — Information/agent security (SI)

*Scope: Part 3 §3, §5, §7; Part 4 §1. Full findings from the dedicated research pass follow verbatim.*

### Claim 1: The separation-of-powers architecture (model proposes → policy authorises → tool executes → record witnesses)

**Published as:** Part 3 §3. "The central claim of this part is not a list of risks. It is an architecture, and it fits on one line... Four functions, and the rule that matters is that they cannot live in the same place. The failure mode has a name: concentration." Presented explicitly as this series' own application of segregation-of-duties to agents, not attributed to any named external framework.

**Status:** confirmed (as sound and internally consistent) — but needs a caveat on the novelty framing.

**Strongest counter-argument, update, or expert critique found:** The underlying pattern — a decision point that adjudicates, enforcement points that carry out the decision, and an independent audit substrate that records it — is a decades-old security pattern (the XACML policy-enforcement-point / policy-decision-point model) that is being actively and rigorously re-derived for AI agents specifically, in parallel, by multiple 2026 sources the text does not mention:

- An academic paper, *A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents* (arXiv:2606.12320, June 2026), proposes a reasoning plane that adjudicates intent plus four enforcement planes (network, identity, endpoint, data) that realize the decision, capability attenuation so a compromised agent's authority is bounded by construction, and "audit as a structured evidence substrate" reconstructible for a regulator or incident responder — a more granular, more rigorous version of exactly the same idea (propose → decide → enforce → witness).
- Microsoft shipped an open-source **Agent Governance Toolkit** (Microsoft Open Source Blog, 2 April 2026) that productizes the same separation without using the phrase: a stateless policy engine intercepts every action pre-execution (~0.1ms p99 latency) = "authorises"; an "Agent Mesh" handles identity/trust scoring = "who"; an "Agent Runtime" with CPU-privilege-ring-style execution levels and a kill switch = "executes"; "Agent Compliance" does OWASP-mapped evidence collection = "witnesses."
- A second academic paper, *Fortifying the Agentic Web: A Unified Zero-Trust Architecture Against Logic-layer Threats* (arXiv:2508.12259, Aug 2025), and several 2026 vendor/practitioner writeups (e.g. Sweet Security's "AI Agent Policy Enforcement" guide) describe the same PEP/PDP-plus-audit shape applied to agents.

None of this makes the four-function diagram wrong, and no single source uses this series' own "model proposes / policy authorises / tool executes / record witnesses" phrasing or explicitly invokes segregation-of-duties language the way Part 3 does — so the "own synthesis" claim is technically defensible. But a skeptical security researcher would say the *idea* is converging industry-wide in 2026, not something this series alone noticed; presenting it with zero acknowledgment of that convergence risks reading as more original than the moment actually is.

**Source:** arXiv 2606.12320, *A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents*, Jun 2026, https://arxiv.org/abs/2606.12320 (V) · Microsoft Open Source Blog, *Introducing the Agent Governance Toolkit*, 2 Apr 2026, https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/ (V) · arXiv 2508.12259, *Fortifying the Agentic Web*, Aug 2025, https://arxiv.org/pdf/2508.12259 (P)

**Recommendation:** add caveat / open question for the author. Consider one added sentence acknowledging that 2026 saw parallel industry and academic architectures converge on the same propose/decide/enforce/audit shape — naming at least the Microsoft toolkit or the Five-Plane paper — so the "own synthesis" framing reads as this series' pedagogical simplification of a converging idea, not a claim of sole discovery. Does not require touching the diagram itself.

### Claim 2: The rule of two (Meta, 31 October 2025)

**Published as:** Part 3 §3. Three questions — private data, untrusted content, external communication — "answer all three honestly... without a human in the loop, an agent may satisfy at most two." Sourced to Meta, *Agents Rule of Two*, already verified (V) in `sources/inventory.md`.

**Status:** confirmed.

**Strongest counter-argument, update, or expert critique found:** Simon Willison's own analysis of the framework (published two days after it, 2 Nov 2025) identifies a specific, dated flaw: Meta's original post labeled the combination of *untrusted content + state-changing action* (without private-data access) as "safe" / "lower risk." Willison argued this pairing alone can still cause real harm with no data leak at all. Meta subsequently revised the post's wording from "safe" to "lower risk" and clarified that "any sensitive system" falls under the private-data category — a real, public post-publication correction, made by the person most associated with the adjacent "lethal trifecta" concept. No successor or rival "rule of three" from another vendor was found; the framework appears to remain the field's standard reference as late as June 2026.

**Source:** Simon Willison, *New prompt injection papers: Agents Rule of Two and The Attacker Moves Second*, 2 Nov 2025, https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/ (V)

**Recommendation:** keep as-is. Optionally, one clause noting the framework's own "safe"/"lower risk" wording was revised within days of publication in response to a named critic — evidence the rule is alive and self-correcting, not evidence against citing it.

### Claim 3: Simon Willison's "lethal trifecta"

**Published as:** Part 3 §5. "Names the same three properties as the rule of two, framed as the boundary condition for when a hijack turns into real damage rather than a confused, harmless reply."

**Status:** confirmed, still live and actively referenced through mid-2026 — but the framing slightly overstates how settled the concept is across the field.

**Strongest counter-argument, update, or expert critique found:** TechTarget (30 June 2026) states plainly that "the cybersecurity field does not currently agree on a universal definition: different cybersecurity analysts and AI researchers often pick different trios of properties." Per Willison's own November 2025 post, the trifecta as he originally scoped it is specifically about **data exfiltration** — narrower than the rule of two's broader "changing state" leg. Part 3's own text gets close to this nuance ("the worst outcome is a nonsense answer, not a leak") but doesn't say explicitly that the trifecta's scope is narrower than the rule of two's. On currency: OpenAI shipped "Lockdown Mode" in July 2026, an explicit engineering response to the trifecta's exfiltration stage, which Willison publicly praised — confirming the concept still drives real vendor mitigation work.

**Source:** TechTarget, *The agentic AI 'lethal trifecta': What CISOs should know*, 30 June 2026, https://www.techtarget.com/searchsecurity/tip/The-agentic-AI-lethal-trifecta-What-CISOs-should-know (V) · Simon Willison, as above (V)

**Recommendation:** add caveat — a short clause noting the trifecta is scoped to exfiltration specifically and that other researchers frame the same territory with different trios, so it should not read as a single field-wide consensus definition sitting neatly alongside the rule of two.

### Claim 4: OWASP Top 10 for Agentic Applications (ASI01–03) and the OWASP Agentic Skills Top 10

**Published as:** Part 3 §5. Published December 2025 with contributions from over a hundred specialists, "the first peer-reviewed framework dedicated to autonomous systems." ASI01 goal hijacking, ASI02 tool misuse, ASI03 identity and privilege abuse. "The framework's June 2026 update stopped cataloguing hypothetical threats and started listing CVEs."

**Status:** confirmed on every specific fact checked. The OWASP GenAI Security Project released the framework 9–10 December 2025, built from over 100 experts including representatives from NIST, the Alan Turing Institute, Microsoft's AI Red Team and AWS. Category names and numbers match exactly, stable across every independent source checked. Help Net Security's 11 June 2026 piece independently corroborates the "hypothetical → CVEs" shift in the framework's own words.

**Strongest counter-argument, update, or expert critique found:** Could not locate a formal, dated "v1.1" changelog entry on genai.owasp.org proving a literal mid-2026 revision event — the "June 2026 update" framing appears to rest on secondary coverage describing the document's content as of June 2026, not a directly-verifiable OWASP release note. Minor sourcing-precision gap, not a factual error.

**Source:** OWASP GenAI Security Project, press release, 9 Dec 2025 (V) · Help Net Security, 11 June 2026 (V, already in inventory) · OWASP Agentic Skills Top 10 project page (V, already in inventory)

**Recommendation:** keep as-is; consider softening "the framework's June 2026 update" to "the framework's coverage by June 2026."

### Claim 5: The three CVEs (CVE-2025-59536, CVE-2026-21852, CVE-2026-22708)

**Published as:** Part 3 §7. First pair: "cloning and opening an untrusted project could trigger remote code execution and key exfiltration before any consent dialogue ever appeared on screen." Third: "a code agent's environment could be poisoned so that commands already on an approved list, such as checking a repository's branches, delivered an arbitrary payload instead."

**Status:** confirmed — all three CVEs are real and the technical description matches published detail closely — but the text's genericization hides information a security-literate reader would want.

**Strongest counter-argument, update, or expert critique found:** Both CVE-2025-59536 and CVE-2026-21852 are specifically **Anthropic Claude Code** vulnerabilities: CVE-2025-59536 is a trust-dialog-bypass RCE (CVSS 8.7, disclosed ~3 Oct 2025, fixed in Claude Code 1.0.111) and CVE-2026-21852 is an API-key-exfiltration flaw (CVSS 5.3, disclosed 21 Jan 2026, fixed in Claude Code 2.0.65). CVE-2026-22708 is specifically a **Cursor** vulnerability: shell built-ins bypass Cursor's Auto-Run allowlist by poisoning environment variables — the public write-ups' own worked example is literally `git branch`, an almost verbatim match to Part 3's "checking a repository's branches"; fixed in Cursor 2.3. All three are patched as of the versions named, so as of 31 August 2026 they are historical evidence of a risk class, not open live vulnerabilities.

**Source:** Check Point Research, *Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files*, 2026 (V) · The Hacker News, Feb 2026 (V) · GitHub Security Advisory GHSA-82wg-qcm4-fp2w (Cursor) (V) · cve.org / NVD records for all three (V)

**Recommendation:** add caveat / update wording. Name the affected products (Claude Code for the first two, Cursor for the third) and note all three are patched — this shows the pattern recurring across two different, named, credible tools, and lets a reader correctly judge current exposure.

### Claim 6: Supply-chain incidents (postmark-mcp, ClawHavoc/OpenClaw/ClawHub, Snyk 280+, BlueRock SSRF, Register 135,000+)

**Status:** confirmed for postmark-mcp and the Snyk 280+ figure; needs caveat for the ClawHavoc "1,184" figure and, more sharply, for the Register's "135,000+" figure.

**Strongest counter-argument, update, or expert critique found:**
- **postmark-mcp:** no dispute found. Independently re-confirmed (BleepingComputer, CSO Online, Dark Reading, Postmark's own statement): 15 clean versions, backdoor added in v1.0.16, ~1,500–1,643 downloads before takedown.
- **ClawHavoc — the "1,184" figure needs a timeline caveat.** Koi Security's original 1 Feb 2026 disclosure found **341** malicious skills; by ~16 Feb the count had grown to **824**; **1,184** was reported around 20 Feb — roughly three weeks after discovery, not the day-one count. Presenting it right next to "Koi Security discovered and named the campaign on 1 February 2026" can read as if 1,184 was the day-one figure.
- **Snyk's 280+ leaky-skills figure:** confirmed, no dispute found.
- **BlueRock's 36.7% of 7,000+ MCP servers vulnerable to SSRF:** independently corroborated by a second study (Practical DevSecOps, 2026), which adds that 41% of scanned MCP servers require no authentication at all and 53% of authenticated servers rely on static, non-rotating API keys. The inventory's own flagged "superseded 12,000+/33%" detail on BlueRock's own registry could not be independently verified this round (404 on the specific URL tried).
- **The Register's "135,000+ exposed OpenClaw instances" is the least stable number in this whole axis.** Accurately quoted and attributed (The Register, 9 Feb 2026, crediting SecurityScorecard) — but contemporaneous scans by other vendors reported sharply different counts for nominally the same population: Bitsight found roughly 30,000; a widely-circulated summary of the same SecurityScorecard work cites 42.9K unique exposed IPs; Infosecurity Magazine headlined "40,000+"; Censys tracked a climb from ~1,000 to 21,000+ in a week, then a March 2026 analysis put it at 63,070; at least one later aggregator claims 220,000+. A genuine, citable 4–7x spread from real methodology divergence, not an error.

**Source:** Koi Security, *ClawHavoc: 341 Malicious ClawedBot Skills Found by the Bot They Were Targeting*, 1 Feb 2026 (V) · Antiy Labs (already V in inventory) · Practical DevSecOps, *MCP Security Statistics 2026* (V) · Bitsight, *OpenClaw Security* (V) · Infosecurity Magazine (V)

**Recommendation:** postmark-mcp, Snyk 280+: keep as-is. ClawHavoc "1,184": add a clause clarifying the figure reflects the campaign's later, expanded state. The Register's 135,000+: add a clause noting other scans from the same period reported 30,000 to 220,000+, so the number is one vendor's point-in-time estimate, not a consensus count.

### Claim 7: The Instagram account-takeover incident opening Part 4

**Status:** confirmed. Every element independently corroborated across many outlets (Cybernews, Security Affairs, Help Net Security, TechNadu, BleepingComputer, Gizmodo, MLQ News), all tracing to the same Maine Attorney General breach-notification filing already cited by the project's own source.

**Strongest counter-argument, update, or expert critique found:** none contradicting the headline facts. Additional detail found that sharpens rather than contradicts the article: the root cause was specifically High Touch Support's failure to verify a submitted email address was already associated with the target account "due to a bug in a separate code path," and several reports describe attackers using VPN services to geo-locate near the target account before contacting the bot.

**Recommendation:** keep as-is; optional enrichment with the root-cause and VPN-geo-matching detail.

### New sources not yet in `sources/inventory.md` (Axis 1)

- Simon Willison, *New prompt injection papers: Agents Rule of Two and The Attacker Moves Second*, 2 Nov 2025 — https://simonwillison.net/2025/Nov/2/new-prompt-injection-papers/
- TechTarget, *The agentic AI 'lethal trifecta': What CISOs should know*, 30 June 2026 — https://www.techtarget.com/searchsecurity/tip/The-agentic-AI-lethal-trifecta-What-CISOs-should-know
- arXiv 2606.12320, *A Five-Plane Reference Architecture for Runtime Governance of Production AI Agents* — https://arxiv.org/abs/2606.12320
- Microsoft Open Source Blog, *Introducing the Agent Governance Toolkit*, 2 Apr 2026 — https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/
- Check Point Research, *Caught in the Hook: RCE and API Token Exfiltration Through Claude Code Project Files* — https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
- The Hacker News, *Claude Code Flaws Allow Remote Code Execution and API Key Exfiltration*, Feb 2026 — https://thehackernews.com/2026/02/claude-code-flaws-allow-remote-code.html
- Koi Security, *ClawHavoc: 341 Malicious ClawedBot Skills Found by the Bot They Were Targeting*, 1 Feb 2026 — https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
- Practical DevSecOps, *MCP Security Statistics 2026* — https://www.practical-devsecops.com/mcp-security-statistics-2026-report/
- Bitsight, *OpenClaw Security: Risks of Exposed AI Agents Explained* — https://www.bitsight.com/blog/openclaw-ai-security-risks-exposed-instances

---

## Axis 2 — Cryptography and identity/credential management

*Scope: Part 3 §4, §6; cross-referenced against Part 4 §3. This is the axis with the thinnest existing grounding — no concrete cryptographic protocol or standard is named anywhere in the current text, which is itself the headline finding.*

### Claim 1: Non-human identity (NHI) debt, sourced to miniOrange 2026

**Published as:** Part 3 §4 quotes miniOrange verbatim: *"Human identities went through identity governance, onboarding flows, quarterly reviews and offboarding lists. Non-human identities were created by a developer on a Tuesday afternoon and quietly outlived the project, the team, and sometimes the developer themself."*

**Status:** confirmed (the direct quote), but the source's evidentiary weight is weaker than the text implies.

**Strongest counter-argument, update, or expert critique found:** The "Tuesday afternoon" quote is verbatim and accurate. But the article is a vendor blog/opinion piece with no disclosed methodology or original survey behind the undercounting claim. Far stronger, methodologically transparent 2026 surveys exist: **CSA + Strata Identity, March 2026, n=285** — only 18% report high confidence their IAM infrastructure can handle AI agent identities, 84% doubt they could pass a compliance audit for agent behaviour. **CSA + Oasis Security, n=383** — 92% lack confidence legacy IAM tools manage AI/NHI risk, 78% have no formal provisioning/removal policy for agent identities.

**Source:** miniOrange (V, quote confirmed, no methodology disclosed) · Cloud Security Alliance, *AI Agent Identity Crisis: Standards Emerge as Enterprises Lag*, 18 March 2026 (V)

**Recommendation:** keep the quote; stop calling miniOrange a "survey"; add the CSA/Strata (n=285) and CSA/Oasis (n=383) figures as the real quantitative backing.

### Claim 2: "On behalf of" vs "autonomous" — "the industry has converged on two distinct patterns"

**Published as:** Part 3 §4: "the industry has converged on two distinct patterns... It is also, in that survey's own words, what worries regulators most, because there is no human in the loop to hold accountable." Both links point to the miniOrange citation.

**Status:** contested — likely misattribution, and the binary framing is already thinner than current practice.

**Strongest counter-argument, update, or expert critique found:** Fetched all three plausible miniOrange articles directly and searched each for the specific taxonomy and the "worries regulators most" phrase. **Neither appears in any of them.** The closest miniOrange gets is a table row and one blended sentence, not the clean two-pattern taxonomy attributed to it "in that survey's own words." Same error class as the CloudEagle/Veza mixup already caught once. Separately, multiple 2026 sources describe **four** agentic identity architectures in production (user-delegated, autonomous, hybrid orchestrated, scoped impersonation), not two. What the industry has actually converged on is a *protocol*: OAuth 2.0 Token Exchange (RFC 8693), the technical substrate Microsoft, Okta, AWS, Auth0 and Ping Identity have all built 2026 agent-identity products on.

**Source:** Direct re-fetch of all three miniOrange articles (V — targeted search, not found) · CerberAuth, *Delegation Done Right: Token Exchange and the On-Behalf-Of Pattern* (V) · IETF RFC 8693 (V)

**Recommendation:** cite new source / open question for the author. Either locate the actual origin of "worries regulators most," or present it as the author's own reading rather than a direct quote. Ground the pattern in RFC 8693's actor_token/subject_token distinction instead.

### Claim 3: Long-lived embedded API key as root cause; fix stated as "narrow-scope, short-lived token"

**Published as:** Part 3 §4: "a long-lived interface key embedded somewhere in code or configuration, with no expiry and broader scope than the task needs. The fix is equally unglamorous, a narrow-scope, short-lived token issued per task."

**Status:** confirmed as directionally accurate, but this is **the single biggest citation gap on this axis** — the "fix" already exists as multiple named, shipping standards and products.

**Strongest counter-argument, update, or expert critique found:** NeuralCoreTech (the cited source) is a content-marketing site, not a research firm — the same problem as Claim 1's miniOrange citation, and its own proposed fix cites Auth0's product page as evidence. The fix is not a vague design principle — it is several named, shipping mechanisms:
- **OAuth 2.0 Token Exchange (RFC 8693)** — the actor_token/subject_token mechanism, stable since 2020.
- **SPIFFE/SPIRE** (CNCF-graduated) — cryptographically verifiable, automatically attested, hourly-rotating workload identities.
- **Auth0 Token Vault / "Auth for GenAI"** — GA product where agents never hold a raw API key.
- **Microsoft Entra Agent ID** (GA in 2026) — purpose-built identity construct for agents, rolling out July–August 2026.
- **NIST NCCoE concept paper**, *Accelerating the Adoption of Software and AI Agent Identity and Authorization* (5 Feb 2026) — the closest thing to an official US reference framework.

**Source:** Auth0, *Token Vault: Secure Token Exchange for AI Agents* (V) · Microsoft Learn, *What is Microsoft Entra Agent ID?* (V) · NIST NCCoE concept paper, 5 Feb 2026 (V)

**Recommendation:** cite new source — the clearest actionable gap on the whole dossier. Name RFC 8693 and SPIFFE/SPIRE next to "narrow-scope, short-lived token issued per task."

### Claim 4: Veza 2026 report — 824,000 orphaned identities, 8%, 17:1 ratio

**Status:** confirmed — already the best-sourced claim on this axis (V in the project's own ledger).

**Strongest counter-argument, update, or expert critique found:** What is missing is a caveat about vendor divergence on the headline ratio. Veza's 17:1 sits at the *low* end of a wide 2026 range: Rubrik Zero Labs ~45:1, Gravitee 82:1, Entro Security 144:1 in cloud-native environments specifically. One synthesis piece frames this explicitly as "a measurement problem," not a factual dispute — different vendors scope "identity" differently.

**Source:** Veza 2026 report (V, already verified) · SecureW2 (V) · Axis Intelligence, *Machine Identity Statistics 2026* (V)

**Recommendation:** add one caveat sentence noting the 17:1–144:1 vendor range, with Veza's figure the most conservative and best-documented.

### Claim 5: The reversal-point receipt and OpenTelemetry — no tamper-evidence named

**Published as:** Part 3 §6 proposes a per-execution JSON receipt and recommends OpenTelemetry's GenAI semantic conventions, quoting a line about agentic failure modes attributed to "the standard's own documentation." Article 12 elsewhere requires logging "resistant to tampering." Nothing addresses how the record itself resists tampering.

**Status:** gap found — real and significant.

**Strongest counter-argument, update, or expert critique found:** OpenTelemetry standardises *what fields* a trace carries, not whether the record resists post-hoc modification — a category mismatch against Article 12's own language. As of mid-2026 every `gen_ai.*` attribute in the OTel registry still carries a "Development," not "Stable," badge. Two concrete, purpose-built alternatives exist and directly target the gap: a brand-new IETF draft, `draft-sharif-agent-audit-trail-01` (published 19 August 2026 — twelve days before this research), specifying SHA-256 hash chaining, optional ECDSA signatures, and RFC 3161 timestamp anchoring, explicitly citing Article 12 as its motivating requirement (an individual submission, not yet adopted); and Sigstore/Rekor, a mature, production-grade, Certificate-Transparency-style append-only log already being pointed at AI-agent artifacts (`sigstore-a2a` signs Google A2A Agent Cards into Rekor with SLSA provenance).

**Source:** DEV Community, *OpenTelemetry's GenAI semantic conventions are NOT stable yet* (V) · IETF `draft-sharif-agent-audit-trail-01`, 19 Aug 2026 (V) · Red Hat Emerging Technologies, *Who really built that? Supply-chain provenance for AI agent identity*, 7 Aug 2026 (V) · Sigstore, *Rekor v2 GA* (V)

**Recommendation:** open question for the author, with a concrete fix available. Add one paragraph distinguishing what OTel gives you (a shared vocabulary) from what it does not (proof the receipt wasn't altered), and name a hash-chaining mechanism as the piece still missing.

### Claim 6: Governance platforms that can "discover, monitor and shut down agents in third-party clouds"

**Status:** confirmed, and the market has moved further and faster than the single citation shows.

**Strongest counter-argument, update, or expert critique found:** ServiceNow added a literal "Kill Switch" to AI Control Tower at Knowledge 2026 (May 2026), extended to agents on AWS, Google Cloud and Azure — covered directly by The Register and Fortune, stronger primary citations than the Substack analysis currently used. Separately, the identity-governance market is consolidating fast: Cisco announced acquiring Astrix Security (~$400M, May 2026); Oasis Security received a letter of intent to be acquired by Cyera (~$1B, 28 July 2026). Within a single year, "discover, monitor, shut down" went from a startup pitch to a feature large platforms are absorbing wholesale.

**Source:** The Register, 5 May 2026 (V) · Fortune, 6 May 2026 (V) · BankInfoSecurity on Cisco–Astrix (V)

**Recommendation:** swap or supplement the Substack citation with The Register/Fortune, and note the 2026 acquisition wave as further evidence the capability is consolidating into major platforms.

### Concrete standards this axis should name but currently doesn't

The central finding of this axis: **the text describes, in each case, a problem that a real, named, dated standard already substantially solves**, and cites none of them.

**Short-lived, narrow-scope credential issuance:** OAuth 2.0 Token Exchange (RFC 8693, stable IETF standard since 2020) · SPIFFE/SPIRE (CNCF-graduated) · Auth0 Token Vault (GA product) · Microsoft Entra Agent ID (GA 2026) · NIST NCCoE concept paper (Feb 2026).

**Delegated / on-behalf-of authorization:** RFC 8693's actor_token/subject_token pair · Okta Cross App Access (25+ software makers signed on by mid-2026, including Anthropic's Claude) · OpenID Foundation AuthZEN AARP/COAZ profiles (Working Group Drafts since 15 June 2026) · Anthropic's own MCP authorization spec (release candidate 21 May 2026) · **`draft-klrc-aiagent-auth-03`** ("AIMS") — the single most significant find of this research pass: a multi-vendor IETF draft authored by people from Defakto, AWS, Zscaler, Ping Identity, **OpenAI**, and **Okta**, composing existing protocols into one 8-layer agent-identity stack. This is the closest real document to "the industry has converged on a standard" that the text claims informally without naming — better evidence than the current miniOrange citation.

**Tamper-evident audit records:** `draft-sharif-agent-audit-trail-01` (19 Aug 2026, emerging, not yet adopted) · Sigstore/Rekor transparency log (production-grade, already pointed at agent artifacts) · mTLS (underlies both).

**Overall recommendation:** the single highest-value edit on this axis is naming RFC 8693 in Part 3 §4 and naming a hash-chain-plus-anchoring mechanism (hedged as "an emerging IETF draft") in Part 3 §6. The second highest-value edit is naming `draft-klrc-aiagent-auth` once, since its cross-vendor author list is stronger evidence for "the industry has converged" than the current citation.

### New sources not yet in `sources/inventory.md` (Axis 2)

1. IETF, `draft-klrc-aiagent-auth-03`, *AI Agent Authentication and Authorization* ("AIMS"), 6 July 2026 — https://datatracker.ietf.org/doc/draft-klrc-aiagent-auth/
2. IETF, RFC 8693, *OAuth 2.0 Token Exchange* — https://www.rfc-editor.org/info/rfc8693/
3. IETF, `draft-sharif-agent-audit-trail-01`, 19 August 2026 — https://datatracker.ietf.org/doc/draft-sharif-agent-audit-trail/
4. SPIFFE project — https://spiffe.io/
5. Microsoft Learn, *What is Microsoft Entra Agent ID?* — https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id
6. Okta Newsroom, Cross App Access ecosystem — https://www.okta.com/newsroom/press-releases/okta-announces-cross-app-access-partners/
7. OpenID Foundation, AuthZEN Working Group Drafts, 15 June 2026 — https://openid.net/openid-foundation-advances-authorization-for-the-agent-era-with-new-authzen-working-group-drafts/
8. Model Context Protocol Blog, 2026-07-28 Release Candidate — https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/
9. NIST NCCoE, *Accelerating the Adoption of Software and AI Agent Identity and Authorization*, 5 Feb 2026 — https://www.nccoe.nist.gov/sites/default/files/2026-02/accelerating-the-adoption-of-software-and-ai-agent-identity-and-authorization-concept-paper.pdf
10. Cloud Security Alliance, *AI Agent Identity Crisis*, 18 March 2026 — https://labs.cloudsecurityalliance.org/research/csa-research-note-okta-ai-agent-iam-framework-enterprise-gap/
11. Red Hat Emerging Technologies, 7 August 2026 — https://next.redhat.com/2026/08/07/supply-chain-provenance-for-ai-agent-identity/
12. The Register, ServiceNow kill switches, 5 May 2026 — https://www.theregister.com/software/2026/05/05/servicenow-adds-agent-kill-switches-to-ai-control-tower/5228579
13. Fortune, 6 May 2026 — https://fortune.com/2026/05/06/servicenow-kill-switch-ai-agents-bill-mcdermott/
14. Auth0, *Token Vault: Secure Token Exchange for AI Agents* — https://auth0.com/blog/auth0-token-vault-secure-token-exchange-for-ai-agents/
15. Axis Intelligence, *Machine Identity Statistics 2026* — https://axis-intelligence.com/machine-identity-statistics/

---

## Axis 3 — GDPR and the EU AI Act

*Scope: Part 3 §8 (Europe); Part 4 §5 (SCHUFA/GDPR paragraph). The single most time-sensitive axis in the whole dossier.*

### Claim 4 (checked first — the urgent one): the 2 August 2026 high-risk deadline

**Published as:** "2 August 2026 is the binding date for high-risk obligations under the EU AI Act, covering articles 9 to 17 for providers and article 26 for deployers. A November 2025 Commission proposal would push some of these deadlines back... **That proposal has not become law. Plan for August 2026 and treat any delay as schedule slack, not as the plan.**"

**Status: SUPERSEDED. The single most important correction in this research pass.**

The November 2025 Commission proposal (the "Digital Omnibus on AI") **did become law**, before the article's own stated present date:
- **Regulation (EU) 2026/1744**, amending the AI Act. Political agreement 7 May 2026; Parliament vote 16 June 2026 (423–57); signed 8 July 2026.
- **Published in the Official Journal 24 July 2026. Entered into force 27 July 2026** — six days before the deadline it replaces.
- New dates: high-risk obligations for standalone Annex III systems deferred to **2 December 2027** (16 months); Annex I systems embedded in regulated products deferred to **2 August 2028** (12 months).
- This deferral covers Articles 8–15 (including Article 12 logging and Article 14 human oversight) plus Articles 9, 26 and 27.
- **Not everything moved.** Article 50 transparency duties took effect on schedule on 2 August 2026 (only the watermarking sub-obligation got a grace period to 2 December 2026). GPAI obligations (Articles 51–56) were already in force from August 2025, unaffected. Prohibited practices (Article 5) remain in force from February 2025, with two new categories added effective 2 December 2026.

**Why this matters:** the article's own organising claim for the Europe subsection is "what already applies today over what is still pending." As of 31 August 2026, Articles 9–17 and Article 26/27 are **no longer current law for Annex III systems** — they apply from December 2027. The instruction to "plan for August 2026" is now the opposite of correct.

**One genuine open question:** whether Article 73 (serious-incident notification) rides the same deferral or keeps the original date. Secondary sources split, and the project's own already-cited source (artificialintelligenceact.eu) shows its Article 26 page updated to the new dates while its Article 73 page still shows 2 August 2026 — an internal inconsistency on a single already-cited source. The amending regulation's own Article 113 text could not be retrieved to settle this directly.

**Recommendation: update wording (urgent) + open question for the author.** Rewrite the Europe subsection to state the delay is now law, name the new dates, drop the "has not become law" framing entirely, and flag Article 73's status as unresolved pending direct verification.

**Sources:** Cloud Security Alliance, *EU AI Act's High-Risk Deadline: Deferred, Not Cancelled* (V) · Future of Privacy Forum, *The AI Act implementation timeline* (V, clearest before/after table) · Gibson Dunn (V) · artificialintelligenceact.eu Article 26 and Article 73 pages (V, internally inconsistent) · verifywise.ai (V) · compliancehub.wiki (V) · trail-ml.com (V)

### Claim 1: SCHUFA (C-634/21) and "solely automated"

**Status: confirmed, and still the operative precedent as of 31 August 2026.** Multiple independent law-firm readings converge on the holding as published; no CJEU decision, national high-court ruling, or EDPB/EDPS document since December 2023 narrows it.

**Strongest counter-argument or update found:** the EDPS published a self-assessment checklist on human intervention (18 May 2026), described by commentary as "the current EU supervisory benchmark." Its criteria overlap with and extend the four conditions already cited (see Claim 3) — reinforcing, not contesting.

**Recommendation:** keep as-is; optionally cite the EDPS May 2026 checklist as a second, more authoritative source.

### Claim 2: The Masaryk University doctrinal reading (SCHUFA cross-read with Uber, Deliveroo, CaixaBank)

**Status: confirmed, with a genuine finding worth adding.** Opened the actual paper directly: Nimrod Mike, "Another View on Article 22 GDPR," MUJLT Vol. 20 No. 1 (2026). The quoted standard is confirmed near-verbatim.

**Strongest finding not yet reflected in the text:** the paper proposes a "cumulative ADM doctrine," arguing SCHUFA may be insufficient for sequential/continuous automated steps producing an aggregate effect over time, as opposed to one discrete decision — directly relevant to agentic systems that continuously score, flag, or deprioritise across many small actions rather than issuing one verdict.

**Recommendation:** keep the quote; consider adding one sentence on the paper's further extension, since it strengthens the piece's own argument about repeated agent actions.

### Claim 3: "GDPR Local" — four conditions for meaningful human review

**Status: confirmed, but a stronger and more current source now exists.** The EDPS's 18 May 2026 checklist states essentially the same four conditions in more authoritative form, and adds two elements the text doesn't mention — a required appeal mechanism, and ongoing monitoring of override/error-detection rates, which is notably close in spirit to this project's own "gate rejection rate" indicator.

**Recommendation:** replace or supplement GDPR Local with the EDPS checklist, and note the coincidence with the "gate rejection rate" indicator explicitly — a strong, citable point the text could make about itself.

### Claim 5: Article numbering, substance, and the Article 26/73 split

**Status: confirmed on substance and numbering.** Article numbers were not renumbered by the Digital Omnibus; Articles 12, 14, 26, 27 and 73 all retain their content. Article 26's six-month retention requirement is unchanged. Article 73's provider-vs-deployer split is unchanged (the project's earlier correction still holds). What changed is purely the timeline (Claim 4).

**Recommendation:** keep the substance and split as-is; fold in Claim 4's timeline correction.

### New sources not yet in `sources/inventory.md` (Axis 3)

1. Cloud Security Alliance, *EU AI Act's High-Risk Deadline: Deferred, Not Cancelled* — https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-deadline-omnibus-20260/
2. Regulation (EU) 2026/1744 (EUR-Lex) — https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng
3. Future of Privacy Forum, *The AI Act implementation timeline* — https://fpf.org/blog/the-ai-act-implementation-timeline-what-changes-under-the-ai-omnibus/
4. Gibson Dunn, *EU AI Act Omnibus Agreement* — https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/
5. Licentium, *EDPS Publishes Human Intervention Checklist*, 18 May 2026 — https://www.licentium.io/post/edps-checklist-human-intervention-automated-decision-making-may-2026
6. Masaryk University Journal of Law and Technology bibliographic detail (author Nimrod Mike, Vol. 20 No. 1, 2026) — https://journals.muni.cz/mujlt/article/view/41367
7. IAPP, *Key takeaways from the CJEU's recent automated decision-making rulings* — https://iapp.org/news/a/key-takeaways-from-the-cjeus-recent-automated-decision-making-rulings

---

## Axis 4 — LGPD and the Brazilian regulatory landscape

*Scope: Part 3 §1, §8 (Brazil); Part 4 §9. Every claim in this axis is explicitly flagged in the published text itself as "moving target, not settled fact" — this research checked whether the ground has shifted.*

### Priority: has ANPD published an Article 20 implementing regulation, and what is PL 2338/2023's exact status?

**Status: confirmed (regulation not yet published), with a richer and more precise status available.**

- **Article 20 regulation:** still not published. As of the most recent source found (13 July 2026), ANPD's own Directive Board had not yet even opened the *formal* public consultation on a draft resolution — only an internal consultation and a completed Regulatory Impact Analysis exist so far. The claim holds and, if anything, understates how far off a rule still is.
- **PL 2338/2023 (general AI bill):** checked directly against the Chamber of Deputies' own tramitação tracker. As of the most recent entry (17 June 2026), status is literally "Aguardando Parecer do(a) Relator(a) na Comissão Especial" — still awaiting the rapporteur's report, not voted. It has missed at least three separate reported target dates (end of 2025, February 2026, May 2026) since Senate passage in December 2024 — roughly two years stuck in the same committee. The companion bill, PL 6237/2025 (the SIA system bill mentioned only via a secondary source in the current text), is formally attached to it and equally stalled.

**Source:** (V) Câmara dos Deputados tramitação tracker, PL 2338/2023 — https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262 · (V) IA Locus, 29 July 2026 · (V) Câmara tramitação, PL 6237/2025 · (V) LH Law, 13 July 2026

**Recommendation:** keep the Article 20 sentence as-is (it understates the gap, if anything). Add one sentence on PL 2338/2023's own two-year stalled status, since the current text only reaches it through a secondary source about the attached SIA bill.

### Priority: does a Brazilian "Air Canada" now exist?

**Status: confirmed — the central honesty claim holds as of the most current evidence found.**

A Brazilian legal-practice source (Bertol Sociedade de Advogados) states this almost verbatim, independently: "Nenhum tribunal brasileiro — estadual, federal, STJ ou STF — já julgou um caso de dano causado por um agente autônomo de IA." A broad sweep of adjacent cases (Vivo robocalls, TikTok facial data, WhatsApp account bans) found only algorithmic-harm or data-processing cases, not agent-binding cases. A genuinely new and Brazil-specific 2026 cluster exists but cuts the other way: since May 2026, Brazilian courts (including the STJ itself) have sanctioned litigants for hiding prompt-injection commands inside legal petitions to manipulate the judiciary's *own* AI tools — the mirror-image problem, not an Air Canada precedent.

**Source:** (V) Bertol Sociedade de Advogados · (V) Marcelo Morais Advogados, the four adjacent-but-non-matching cases with process numbers · (V) STJ official news release, 20 May 2026 · (V) CartaCapital, on the Natura/Rio Negrinho sanction

**Recommendation:** keep as-is. Consider citing the Bertol source directly, since it is a dated, named, independent Brazilian legal-press confirmation rather than an unsourced research-gap statement. Optionally note the adjacent prompt-injection cluster to sharpen the distinction.

### Claim: ANPD's September 2025 independence and the national AI-system bill

**Status: needs update** — the underlying facts hold, but a materially better and more precise source chain now exists, and one mechanism detail is imprecise.

The mechanism was Medida Provisória 1.317, of 17 September 2025 — provisional until Congress converted it into **Law 15.352/2026**, sanctioned by President Lula and published in the Diário Oficial in late February 2026. As of 31 August 2026, this is now settled, permanent statute — a far stronger citation than "per industry reporting" or the two secondary sources already flagged elsewhere in the project as unreliable on this point. The national AI-system bill (PL 6237/2025, sent 8 December 2025) is directly verifiable against the bill's own official text (Planalto) and confirms "December 2025 bill" and "ANPD as coordinator" — and its current status (stalled, attached to PL 2338/2023, missed a committed February 2026 vote date) is a useful add.

**Source:** (V) Senado Notícias, 18 Sept 2025 and 26 Feb 2026 · (V) Congresso em Foco · (V) Câmara/Diário Oficial text of MP 1.317/2025 · (V) Planalto, PL 6237/2025 official record

**Recommendation:** replace "per industry reporting" with a direct citation to Law 15.352/2026, and to PL 6237/2025's own text. Consider one clause noting the September 2025 change was provisional until Congress converted it in February 2026.

### New sources not yet in `sources/inventory.md` (Axis 4)

1. Câmara dos Deputados, tramitação tracker, PL 2338/2023 — https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2487262
2. Câmara dos Deputados, tramitação tracker, PL 6237/2025 — https://www.camara.leg.br/proposicoesWeb/fichadetramitacao?idProposicao=2594000
3. IA Locus, *Marco Legal da IA Brasil 2026 (PL 2338)*, 29 July 2026 — https://ialocus.com.br/blog/post-pl-2338-marco-legal-ia-brasil-2026.html
4. Planalto, PL 6237/2025 official record — https://www.planalto.gov.br/ccivil_03/projetos/ato_2023_2026/2025/pl/pl-6237.htm
5. Baptista Luz, on the SIA bill — https://baptistaluz.com.br/governo-federal-propoe-projeto-de-lei-para-a-criacao-do-sistema-nacional-de-governanca-para-a-inteligencia-artificial-sia/
6. Senado Notícias, MP → agência reguladora, 18 Sept 2025 — https://www12.senado.leg.br/noticias/materias/2025/09/18/medida-provisoria-transforma-anpd-em-agencia-reguladora
7. Senado Notícias, Law 15.352/2026 sanctioned, 26 Feb 2026 — https://www12.senado.leg.br/noticias/materias/2026/02/26/sancionada-lei-que-cria-a-agencia-nacional-de-protecao-de-dados
8. Congresso em Foco, on Law 15.352/2026 — https://www.congressoemfoco.com.br/noticia/116782/lula-sanciona-lei-que-transforma-anpd-em-agencia-reguladora
9. Câmara/Diário Oficial, text of MP 1.317/2025 — https://www2.camara.leg.br/legin/fed/medpro/2025/medidaprovisoria-1317-17-setembro-2025-797987-norma-pe.html
10. Bertol Sociedade de Advogados, on no Brazilian precedent — https://www.bertol.adv.br/inteligencia-artificial-autonoma-e-responsabilidade-juridica-o-que-muda-e-o-que-ainda-nao-muda-no-direito-brasileiro/
11. Marcelo Morais Advogados, the four adjacent Brazilian AI cases — https://lawmm.com.br/judiciario-condena-empresas-por-problemas-gerados-com-uso-de-inteligencia-artificial/
12. STJ, official news release on the prompt-injection cluster, 20 May 2026 — https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/2026/20052026-Tentativas-de-uso-de-prompt-injection-no-STJ-serao-investigadas.aspx
13. CartaCapital, on the Natura/Rio Negrinho sanction — https://www.cartacapital.com.br/justica/justica-condena-advogadas-que-usaram-comando-oculto-de-ia-para-induzir-resultado-de-sentenca/
14. LH Law, *ANPD em 2026*, 13 July 2026 — https://www.lhlaw.com.br/publicacoes/anpd-em-2026-principais-regulamentos-consultas-publicas-e-tendencias-2/

---

## Axis 5 — Agent monitoring and observability

*Scope: Part 3 §6; Part 4 §5, §7. The axis with the most quantitative claims in the dossier.*

### Claim 1: OpenTelemetry GenAI semantic conventions, adoption "still emerging"

**Status:** confirmed (core claim) / **needs correction** (one citation is misattributed).

The "still emerging" framing is not just accurate as of 31 August 2026 — the standard has fragmented further, not less. On 12 June 2026, OpenTelemetry deprecated all `gen_ai.*` content from its main repo and split it into a new dedicated repo with **zero tagged releases** as of 17 July 2026; not a single attribute is marked "Stable." **Misattribution found on direct verification:** the blockquote "Agentic systems fail in ways that look like success..." does not appear in either live OpenTelemetry blog post that could plausibly be its source. It is actually **Aryan Kargwal**, a PhD candidate at Polytechnique Montréal, quoted inside the already-cited Digital Applied article.

**Source:** OpenTelemetry blog posts (V, fetched directly, confirm the quote is absent) · Digital Applied (V, contains the quote, attributed to Kargwal) · John Hodge, *The state of the OpenTelemetry GenAI semantic conventions (July 2026)* (V)

**Recommendation:** correct the citation — attribute the quote to Kargwal/Digital Applied, not OpenTelemetry's own documentation.

### Claim 2: Heinrich's 1931 accident triangle

**Status:** confirmed. Nothing new undermines the piece's own careful hedge. The named critique behind "the ratio is questioned" is Fred Manuele's 2002 book, and a rigorous peer-reviewed empirical test (25,000+ establishments) exists as an optional stronger citation.

**Recommendation:** keep as-is; optionally upgrade the footnote's citation.

### Claim 3: Eight indicators as this series' own synthesis

**Status:** confirmed, but flagged as a fast-closing gap worth monitoring. Actively hunted for a competing panel and found none matching the structure. The closest relative is **Singapore's IMDA Model AI Governance Framework for Agentic AI** (launched 22 January 2026, updated to v1.5 on 20 May 2026), whose human-accountability guidance explicitly recommends "monitoring human override rates and response times" — conceptually the same instrument as "gate rejection rate," reached independently by a national regulator. It does not, however, publish a quantified indicator panel the way this series does. NIST's CAISI initiative is building toward metrics (a Q4 2026 test suite) but has not published one yet.

**Source:** IMDA framework, structure confirmed via secondary legal-firm coverage (V) · NIST CAISI (P, existence confirmed via multiple secondary sources)

**Recommendation:** keep the "nobody else has published this panel yet" claim — it survives an active search. Add a footnote flagging Singapore's IMDA framework as the closest adjacent structure, both to pre-empt a reader finding it first and to strengthen credibility.

### Claim 4: Cost per completed task, FinOps Foundation stats

**Status:** confirmed (the statistics) / **needs correction** (the attribution of the quote).

The 98%/63%/31% figures check out exactly across multiple independent sources. But the blockquote "Cost per completed task is the most meaningful measure..." is **not FinOps Foundation language** — it is N-iX's own formulation (Yaroslav Mota), citing FinOps Foundation survey statistics rather than quoting the Foundation.

**Source:** We The Flywheel (V) · Linux Foundation press release (V) · N-iX, *FinOps for AI* (V, confirms the quote is N-iX's own wording)

**Recommendation:** rephrase the blockquote's introduction so it no longer reads as "the Foundation's own formulation" — attribute it explicitly to N-iX citing FinOps Foundation data.

### Claim 5: The pilot-failure statistics cluster

**Status:** confirmed (MIT, Deloitte, S&P Global, IBM) / **needs update** (Morgan Stanley).

MIT's 95% figure survives scrutiny exactly as phrased in the text (critics target people who paraphrase it more strongly, which this piece does not do). Deloitte, S&P Global and IBM are all confirmed. **Morgan Stanley's "21% of S&P 500" is genuinely dated** — by Morgan Stanley's own follow-up reporting (9–11 July 2026), the figure has moved to roughly 25% (full S&P 500) or 40% (AI-adopter subset), both comfortably higher than 21%. The trend moved from Morgan Stanley's own desk, not a competitor's.

**Source:** MIT/Project NANDA (V) · Deloitte Tech Trends 2026 (V) · S&P Global (V) · IBM/Oxford Economics (P) · Morgan Stanley, *AI Market Trends 2026*, 9 March 2026 (P) · The Corner, 9 July 2026 (V) · Investing.com/Reuters, 11 July 2026 (V)

**Recommendation:** update the Morgan Stanley line — either date it explicitly to when the 21% figure applied, or replace it with the more current ~25%/~40% figures. This does not damage the section's argument; an increasing trend line just means the gap is narrower than 21% implies.

### Claim 6: Kyndryl's 2026 People Readiness Report

**Status:** confirmed. The most solidly grounded number in the whole cluster — multiple independent write-ups report identical figures with no variance. Underlying methodology detail not currently cited: fieldwork by Edelman Intelligence, 24 March–30 April 2026.

**Recommendation:** keep as-is; optional precision addition.

### New sources not yet in `sources/inventory.md` (Axis 5)

1. Deloitte, *Business and IT leaders report AI agents are scaling faster than their guardrails* (3,235 leaders, ~79–80% lack mature agent governance) — https://www.deloitte.com/us/en/insights/topics/emerging-technologies/ai-agents-scaling-faster.html
2. Singapore IMDA, Model AI Governance Framework for Agentic AI (v1.0 Jan 2026, v1.5 May 2026) — https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
3. NIST CAISI, AI Agent Standards Initiative, 17 Feb 2026 (multiple secondary confirmations)
4. John Hodge, *The state of the OpenTelemetry GenAI semantic conventions (July 2026)* — https://john-hodge.com/blog/opentelemetry-genai-semantic-conventions/
5. Morgan Stanley's Q2 2026 update (via The Corner, 9 July 2026, and Investing.com/Reuters, 11 July 2026)
6. Fred A. Manuele, *Heinrich Revisited: Truisms or Myths*, ASSE, 2002, and/or the PMC peer-reviewed 25,000-establishment study — https://pmc.ncbi.nlm.nih.gov/articles/PMC6238149/

---

## Axis 6 — Agent governance frameworks and organisational placement

*Scope: Part 4 §3, §4, §6, §8. Contains the single most falsifiable claim in the entire series.*

### Claim 1 (priority): the negative finding — no framework names the four roles as a fixed structure

**Published as:** "No AI governance framework in wide use, not the NIST AI Risk Management Framework, not ISO 42001, not AIUC-1, not NIST's own agent-standards initiative, names roles equivalent to these four as a fixed structure... not a weakness, a differentiator."

**Status: confirmed.** This is the single most load-bearing sentence in Part 4, and it survives a genuinely adversarial search across every candidate a well-read critic would raise, including several the article does not itself name:

- **ISO/IEC 42001, Annex A.3.2** — mandates *principles* (named ownership, documented authority) but explicitly does not prescribe a fixed role template.
- **ISO/IEC 42005:2025** (the AI system impact assessment companion standard — not currently named anywhere in Part 4) — requires "a clear internal governance framework" allocating roles to "specific individuals or committees," again a general principle, not a fixed structure. Confirms the negative finding and is a citable gap.
- **NIST AI RMF + Generative AI Profile** — organised around four *functions* (Govern, Map, Measure, Manage), not four *roles*.
- **AIUC-1** — has an "Accountability" control family but this is a checklist, not named non-combinable roles.
- **Singapore's IMDA Model AI Governance Framework for Agentic AI** (Jan/May 2026) — the single strongest candidate a critic could raise: 2026, agentic-specific, government-issued. Checked directly: it defines a five-actor value chain across four risk dimensions — a supply-chain responsibility model, structurally different from an internal-control four-role model, and it explicitly leaves role-separation to each organisation. Confirms the negative finding.
- **The IIA's own AI-specific guidance** applies the *existing* three lines to AI, introducing no new fixed role titles beyond that.
- **Forrester** (2026 agentic-AI commentary) comes the *closest* of anything found: names "Model/Agent Owners," "Application Teams" and "Compliance and Audit Teams" — a three-tier mapping, not four distinct, explicitly non-combinable roles with a separate certifier and area sponsor. The nearest miss found, not a hit.

**Strongest counter-argument, update, or expert critique found:** none that overturns the claim. A newer 2026 academic paper making the Three Lines connection for agentic AI specifically (see Claim 3) also stops short of proposing fixed new roles, reinforcing the negative finding.

**Source:** ISMS.online, ISO 42001 Annex A.3.2 (V) · ISO/IEC 42005:2025 (P) · NIST AI RMF (P) · AIUC-1 (P) · IMDA framework (V for structure, via secondary summary) · The IIA, *The Catalyst for Strong AI Governance*, 3 Sept 2025 (V) · Forrester (P)

**Recommendation:** keep as-is. The negative finding is unusually well defended. Two low-cost improvements: (1) add "ISO/IEC 42005" to the explicit list of frameworks checked, since it's the companion standard a well-informed reader would ask about; (2) add one clause acknowledging Forrester's "Model/Agent Owner" terminology as the closest echo found, pre-empting an informed objection.

### Claim 2: The IIA's Three Lines Model — dates and mapping

**Status: needs update.** The three-way mapping itself is sound. The dates are the problem: 2013 is correct (original position paper). 2020 is correct and well documented (formal rename). **2023 is not confirmed as a revision of the Three Lines Model itself** — it likely traces to Deloitte Malta's already-cited source, which states the model "was revisited in 2023" but itself omits 2020 and conflicts with the IIA's own dated chronology. **Missing entirely: July 2026.** The IIA published a further genuine revision on 8 July 2026 — seven weeks before Part 4's own publication — shifting emphasis toward board-facing assurance-and-advice framing. It does not redesign the model or add new roles (so it does not threaten Claim 1), but it is the freshest primary version of the model Part 4 leans on, and it is not cited.

**Source:** The IIA, 2020 position paper (P) · Deloitte Malta (V, already cited; direct quote shows the source of the disputed date) · The IIA, *Statement of Position*, 8 July 2026 (P, confirmed via multiple secondary readings)

**Recommendation:** replace "adopted in 2013 and revised in 2020 and 2023" with "adopted in 2013, revised in 2020, and restated again in July 2026" — a strict upgrade, since the July 2026 restatement predates Part 4's own publication and reinforces the argument.

### Claim 3: The two academic papers, and whether a stronger paper supersedes them

**Status: confirmed**, with a stronger, more current source available to add alongside them. Both cited arXiv papers (2305.17038, 2212.08364) are confirmed accurate to their actual arguments. **A new, more on-point candidate:** Ruud, Schreyer & Weiser, "Governing the Future Digital Workforce: The Three Lines Model in the Age of Agentic Artificial Intelligence," *Magma*, Vol. 29, No. 1, 2026 — specifically about *agentic* AI (matching Part 4's actual subject more precisely than the two 2022/2023 papers), applies the IIA's 2020 model directly to autonomous agents. Read directly: it does **not** propose new fixed roles — it recommends adapting the existing three lines through better collaboration, which is directly useful evidence for Claim 1 as well.

**Source:** arXiv 2305.17038 and 2212.08364 (V) · Magma, Ruud/Schreyer/Weiser 2026 (V, PDF fetched directly)

**Recommendation:** add the 2026 paper as a third citation, ideally the lead one given its recency and exact-match subject.

### Claim 4: The Echelon Cyber / Splunk 650-leader survey

**Status: confirmed.** Every figure verified against the primary source directly: 6% updated governance frameworks, 79% role expanded past mandate, 71% AI touches core systems, 16% govern that access well. The quote is confirmed near-verbatim.

**Strongest caveat:** this is a single, vendor-sponsored survey with no independently conducted survey found matching its methodology and numbers — worth noting explicitly, the same discipline the project applies to the Gartner 43% figure elsewhere.

**Recommendation:** keep as-is; optionally note it is a single-source statistic.

### Claim 5: Where the office sits — CISO precedent, the fire-marshal quote

**Status: confirmed**, with one accuracy nuance. The IANS/Artico benchmark figures match word for word. The fire-marshal quote is confirmed near-verbatim — and the primary source **names the speaker**: Brian Levine, executive director of FormerGov and a former federal prosecutor. Part 4's anonymised description is accurate in substance but less specific than the source allows.

**Recommendation:** minor, optional — consider naming Levine directly, strengthening verifiability without changing the argument.

### Claim 6: The six-state life cycle against existing standards

**Status: needs update / add caveat.** Two findings:

**(a)** Every adjacent standard checked converges on a similar shape (approval gate, active state, suspension/review, terminal decommissioned), supporting the *design* even though none uses Part 4's vocabulary. ISO 42001 (via ISO 22989) frames the AI lifecycle as a technical pipeline, answering "what stage is this system at" rather than "who is accountable for it right now" — a useful distinction worth drawing explicitly.

**(b) A concrete, current counter-example to "nobody implements" the two flagged transitions.** **Microsoft's Agent Governance Toolkit** (open-sourced 2 April 2026, MIT license, 3,300+ GitHub stars) defines seven lifecycle states and **does implement automated versions of both transitions Part 4 says are unbuilt**: inactivity-triggered auto-decommissioning after a configurable period with no owner/certifier sign-off required, and automated credential/session expiration via short TTLs. This runs directly counter to Part 4's own design principle that decommissioning "requires a decision from the agent owner and the certifier together, never an automation running on a schedule." It does not disprove Part 4's underlying warning (an unjudged automatic deletion trigger is exactly the risk the next paragraph warns about) — but it means "almost nobody builds either one" is no longer safely true, given a real, popular, current toolkit doing exactly that, released four months before Part 4's own publication.

**Source:** Microsoft, Agent Governance Toolkit, "Agent Lifecycle" tutorial (V, fetched directly) · GitHub repository (V, confirmed 3,300+ stars) · Help Net Security, 3 April 2026 (P)

**Recommendation:** add caveat / open question for the author. Either soften "almost nobody builds either one" to acknowledge Microsoft's toolkit as the counter-case that proves the underlying point (a real implementation of blind automatic decommissioning is precisely the risk the piece warns about), or reframe the claim as directional rather than absolute. Separately, consider one sentence distinguishing Part 4's accountability-state lifecycle from ISO 42001/22989's technical-pipeline lifecycle.

### New sources not yet in `sources/inventory.md` (Axis 6)

1. Ruud, Schreyer & Weiser, "Governing the Future Digital Workforce," *Magma*, Vol. 29 No. 1, 2026 — https://magmaforskning.econa.no/index.php/magma/article/download/1532/1737?inline=1
2. The IIA, *Statement of Position: Three Lines Model*, 8 July 2026 — https://www.theiia.org/en/resources/statements-of-position/
3. Microsoft, Agent Governance Toolkit — https://github.com/microsoft/agent-governance-toolkit
4. IMDA (Singapore), Model AI Governance Framework for Agentic AI, v1.0/v1.5 — https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf
5. ISO/IEC 42005:2025 — https://www.iso.org/standard/42005
6. Forrester, *The State Of Agentic AI In 2026* — https://www.forrester.com/blogs/the-state-of-agentic-ai-in-2026-companies-are-chasing-few-are-catching/
7. The IIA, *The Catalyst for Strong AI Governance*, 3 Sept 2025 — https://www.theiia.org/en/content/articles/global-best-practices/2025/the-catalyst-for-strong-ai-governance/

---

## Consolidated recommendation: what to do next

This dossier is deliberately a research artifact, not a set of pre-approved edits. Suggested next steps, in order:

1. **Send this file to the additional AI reviewers now**, asking them specifically to stress-test the six items marked 🔴/🟠 above — those are the ones where acting on faulty research would do real damage to the series' credibility.
2. Once cross-reviewed, decide which findings become edits to `harness-p3.html` / `harness-p4.html` (via their `build/body_p3_*.html` / `build/body_p4_*.html` sources, never the live HTML directly — see `build/README.md`'s rule on this), which become new entries in `sources/inventory.md`, and which are simply logged as "considered, not acted on" the way this project already does for some findings.
3. The Article 73 open question (Axis 3) and the BlueRock registry figure open question (Axis 1) both need one more direct-fetch attempt before either is asserted either way.
4. Whatever is acted on should follow the same byte-for-byte regeneration discipline this project used for its two citation-correction rounds on 31 August 2026: edit the `build/body_*` source, run the build script, diff before committing.

---

## Appendix A — Part 3, full English source text (as currently published)

*Reproduced verbatim from `build/body_p3_en.html`, the source of truth for `harness-p3.html`'s English tab. Inline SVG diagram markup is omitted for readability; diagram captions are preserved.*

**Harness · Part 3 of 4 · Who**

# The separation of powers: what it can do, and who answers for it

*In part 2, the operations director gave her agent a guide it could not talk its way out of, and a sensor that caught its own mistakes. She still had not answered the one question a lawyer, a regulator or a tribunal actually asks: when it acts in your name, who answers for what it did.*

Fernando Teco Sodré · August 2026 · 20 minute read

**In this article:** A remarkable submission · The first irreversible action · The separation of powers, and the rule of two · Identity and a named owner · Where the order enters inside the data · What must be on the record, and what reversal means · A third-party skill is third-party code · Two columns of legal obligation · Who answers, and where you stand

## 1. A remarkable submission

In February 2024, a man named Jake Moffatt opened the Air Canada website to ask about a bereavement fare, the discounted ticket airlines sell to someone travelling because a relative has died. The website's chatbot told him he could book the regular fare now and apply for the bereavement discount afterwards, retroactively. He did exactly that, saved a screenshot of the conversation as any careful person would, and applied for the refund once the funeral was over.

Air Canada refused. Its actual policy required the discount to be requested before travel, not after. The chatbot had simply invented a more generous rule.

Moffatt took the airline to the British Columbia Civil Resolution Tribunal, and Air Canada's defence is the part of this story that belongs in a series about agents. The airline argued that the chatbot was a separate legal entity, responsible for its own words. The tribunal's response, on record, was that Air Canada never explained why anyone should believe that, and it called the argument a remarkable submission. It found the airline owed a duty of care arising from the commercial relationship, found negligent misrepresentation, and ordered payment. The amount was almost trivial, some six hundred and fifty Canadian dollars plus interest and costs, reached after a year and a half of dispute. The precedent is not trivial at all.

> If it spoke in your name, you own what it said.

Read that case again with this series in mind. Two parts have built a character who treats her agent exactly like a newly hired worker: equip it properly, delegate with a ceiling, inspect what it produces. Air Canada is the company that tried the opposite argument in an actual courtroom, with an actual lawyer, and lost. This part exists because most companies deploying agents today are one incident away from making Air Canada's argument themselves, usually without noticing they are making it.

The case is Canadian, not Brazilian, and that distinction matters enough that it needs saying twice. No Brazilian tribunal has yet ruled on an agent with an external effect. There is announced enforcement priority and there is declared regulatory attention, both covered later in this piece, but there is no decision to cite. Treat Moffatt v Air Canada as what it is: a foreign precedent that shows the shape of the argument a Brazilian court will eventually hear, not proof of what a Brazilian court will decide.

## 2. The first irreversible action

The director who opened part 1 and closed part 2 at tier N2 had, by then, a guide the system could not reason its way around, durable state that survived between sessions, a sensor that returned the exact gap instead of a bare verdict, and a retry ceiling. The invoice from the carrier with revoked credentials no longer got through. Something now checked the list before delivery.

What she still lacked is exactly what part 2 named on its way out: nothing built so far stopped an irreversible action, nothing recorded who had authorised what, and nothing protected against a malicious instruction arriving inside the very data the system was asked to read. The gap sat there, unclaimed, for three more months, because nothing had gone wrong yet.

Then the scope grew, the way scope always grows once something works. Carriers had started disputing rejected invoices by replying directly to the automated notice, and someone decided it was faster to let the system read the dispute and draft a response, rather than routing every disagreement to a person. It was a small extension. It also meant the system could now say something, in the company's name, to someone outside the company.

A carrier wrote in to dispute a rejection from four months earlier, citing a clause in an old rate sheet and asking, politely, whether the company would honour the original rate retroactively given the delay was the company's own fault. The system read the rate sheet, read the dispute, and found the carrier's reading of the clause defensible. It drafted a reply agreeing to the retroactive adjustment and queued it to send.

Nothing in what had been built through part 2 was designed to notice that this was a different kind of action than reconciling a number. The guide covered how to reconcile invoices, not how to bind the company to a financial commitment in correspondence with a supplier. The sensor checked figures against a source, and the figure here was internally consistent with the (mistaken) reading the system had just constructed. Nothing had ever asked the tool layer whether it was, in this instance, allowed to speak for the company at all.

That reply, had it gone out, is Air Canada's chatbot with smaller stakes and a different logo. Same shape exactly: a system answered a question it was never authorised to answer, in the company's own name, and the answer would have been binding the moment it landed in the carrier's inbox.

This part is about the piece that was missing at that exact moment: something outside the model that gets to say no, and a record of who said what, before the message leaves the building rather than after a tribunal asks for it.

## 3. The separation of powers, and the rule of two

The central claim of this part is not a list of risks. It is an architecture, and it fits on one line.

```
THE MODEL PROPOSES → THE POLICY AUTHORISES → THE TOOL EXECUTES → THE RECORD WITNESSES
```

Four functions, and the rule that matters is that they cannot live in the same place. The failure mode has a name: **concentration**. It is what happens when the same probabilistic system invents the plan, approves the risk and carries out the consequence, with nothing standing outside it to disagree.

*[Diagram: The separation of powers — model / policy / tool / human / record, with the record drawn as a cylinder because it is the only one of the four that neither decides nor acts, only witnesses.]*

Next to it, draw what most deployments actually have.

*[Diagram: The failure mode: concentration — one box (model) proposes, authorises and executes at once, with a dashed line to "effect in the world" and no independent record, no trail, no reversal, no accountability.]*

Three reasons to build around this specific architecture rather than a general appeal to caution. It is legible to a board and to legal counsel, which is exactly the audience this part is written for. It is technically precise, because it mirrors the real separation between a decision point, an enforcement point and an audit trail. And it gives a design test instead of a mood: for any action, ask where the four functions physically sit, and if two of them sit in the same place, you have found the problem.

None of this is a new idea dressed up for agents. Segregation of duties is the oldest concept in internal control, the rule that the person who requests a payment cannot be the same person who approves it and the same person who reconciles the account afterwards. Anyone who has ever operated internal controls recognises this diagram before they finish reading the labels. The only change is that one of the four seats is now, sometimes, filled by a model instead of a person.

### The rule of two

Knowing that four functions must stay apart does not tell you, on a Tuesday afternoon, whether the reply your system just drafted needs a human before it goes out. For that you need a test with a countable answer, and the best one available comes from Meta, formulated as three questions about any proposed action.

1. Does it access private data?
2. Does it process untrusted content?
3. Can it communicate externally?

Answer all three honestly. Without a human in the loop, an agent may satisfy at most two of them. The moment an action would answer yes to all three, a human has to be in the loop before it executes, no exceptions carved out for urgency or inconvenience.

*[Diagram: The rule of two — three yes/no questions on a proposed action, a count of how many answered yes, executes without approval (two or fewer) vs. human in the loop required (three), both converging on the same receipt.]*

The carrier's dispute reply answers all three questions yes. It read the rate sheet and the carrier's account history, both private to the company. The dispute email is untrusted content by definition, written by someone outside the company with their own interest in the outcome. And the reply's entire purpose was to communicate externally. Three for three, and nothing in what existed at the end of part 2 ever asked the question.

The rule of two's original Meta publication, not located in this dossier's first version, was found and opened directly on 31 August 2026, confirming the wording two independent secondary sources had already been reporting identically.

### A general matrix of authority

The rule of two answers whether a human needs to be in the loop. A separate, older question is how much authority the loop itself needs, and the honest answer runs through reversibility, not through how important an action looks.

| Class of action | Reversibility | Authority required |
|---|---|---|
| Read or query internal data | Reversible | None |
| Draft a communication, not sent | Reversible | None |
| Send a routine communication with no commitment | Reversible | Free, logged |
| Send a communication that commits money, terms or policy | Irreversible once received | Named human approval, every time |
| Modify a financial or contractual record | Partially reversible | Named approval, logged |
| Delete a record or release a payment | Irreversible | Two named approvals, one of them independent of the requester |
| Any action answering yes to all three rule-of-two questions | Depends on the class above | Human in the loop, regardless of class |

The last row is the one that would have caught the carrier's reply even if someone had mis-classified the action class itself. The rule of two and the reversibility matrix are two independent nets, and a well-built policy layer runs both, because either one, alone, misses cases the other catches.

## 4. Identity and a named owner

None of the previous section works if the system executing an action has no identity of its own to be checked against a policy. This is the part almost every deployment skips, because it is invisible until the day it matters.

The clearest description of the debt this creates comes from a 2026 survey of IAM trends for AI agents, and it is worth quoting exactly because it names something everyone building agents has watched happen without a word for it:

> Human identities went through identity governance, onboarding flows, quarterly reviews and offboarding lists. Non-human identities were created by a developer on a Tuesday afternoon and quietly outlived the project, the team, and sometimes the developer themself.

Non-human identity is not a new category invented for agents. Service accounts, API keys and automation bots have carried this exact debt for two decades, quietly, because nobody's offboarding checklist ever looked for them. An agent is simply the newest and fastest-growing member of that family, and most organisations undercount their own non-human identities substantially, because they get created inside cloud consoles, integration pipelines and software-as-a-service connections nobody centrally tracks.

Three questions, asked of any agent identity, do most of the work:

1. Who deployed it?
2. What is it authorised to do?
3. On whose behalf is it acting right now?

The third question is where the industry has converged on two distinct patterns, and the difference between them is exactly the difference regulators care about most. **On behalf of** is the pattern where the agent authenticates using a present human's session and inherits that person's permissions for the duration of the task, the copilot pattern. **Autonomous** is the pattern where the agent carries its own identity and its own permission set, independent of any human session, the pattern for background jobs, scheduled runs and agent-to-agent communication. It is also, in that survey's own words, what worries regulators most, because there is no human in the loop to hold accountable at the moment the action happens.

That sentence is close to being this part's thesis, written by someone else, in a different field, for a different reason.

A useful bridge, resting on the copilot, human-initiated and unattended trigger classification from enterprise identity management, maps this — in this series — straight onto the N0 to N3 tiers already established in part 1.

| Trigger type | Definition | Maps to tier |
|---|---|---|
| Copilot | Assistant tied to a human present in the session | N0 to N1 |
| Human-initiated | A human starts it, but is not present during execution | N2 |
| Ambient | Fully autonomous, triggered by event or schedule, no human in the loop | N3 |

The dispute-reply feature that nearly committed the director's company to a retroactive rate change was, without anyone deciding this explicitly, an ambient agent wearing a human-initiated one's authority. Someone had approved building a feature that read and drafted. Nobody had approved a system that could, unattended, decide the company's position and act on it.

The most common root cause behind agent-related incidents, according to a 2026 survey of identity governance for agents, is unglamorous: a long-lived interface key embedded somewhere in code or configuration, with no expiry and broader scope than the task needs. The fix is equally unglamorous, a narrow-scope, short-lived token issued per task, and it is worth stating plainly because the fix is cheap and the failure is not.

One more development belongs here because it changes what is actually possible, not just what is advisable. Governance platforms have started to discover, monitor and shut down agents running in third-party clouds, not only inside a company's own systems. The trade press described this, accurately, as handing a badge and real authority to a guard who used to only watch. The kill switch stopped being a design aspiration sometime in the last year. It is now a purchasable capability.

## 5. Where the order enters inside the data

Everything built so far assumes the policy layer can tell a legitimate instruction from an illegitimate one. That assumption deserves to be tested, because the honest answer is that nothing currently can, reliably, and understanding why changes what you build next.

A model reads its own system instructions, the user's request and any text retrieved from an external source as a single stream of symbols. There is no reliable mechanism that marks some of those symbols as command and others as inert data. Hostile text smuggled inside a document, a calendar invitation or a web page carries exactly the same authority as a legitimate instruction from the operator, because to the model reading it, there is no visible difference.

*[Diagram: Where the order enters inside the data — a trusted zone (task contract, own guides and skills) and an untrusted zone (email/PDF/web page, external system response, third-party skill, customer document) both funnel into a single stream of symbols with no reliable marking, which becomes the proposed action. Caption: the boundary exists in your diagram, not inside the model.]*

In July 2026, a researcher speaking at Infosecurity Europe put it plainly: the problem remains unsolved at a fundamental level. Two details from that account are worth carrying forward, because they each kill a solution that sounds obvious until you look closely.

Allow lists, the instinctive fix, have sometimes made an attack easier rather than harder, because the exact commands an attacker needed were already on the approved list for a legitimate reason. And in separate cases, an agent's own output has redefined the boundary of its sandbox, rewriting in practice the very containment meant to hold it.

Simon Willison's lethal trifecta names the same three properties as the rule of two, framed as the boundary condition for when a hijack turns into real damage rather than a confused, harmless reply. An agent with no private data and no way to communicate outward can still be tricked, but the worst outcome is a nonsense answer, not a leak.

The formal recognition of this arrived in December 2025, when the OWASP Top 10 for Agentic Applications was published with contributions from over a hundred specialists, the first peer-reviewed framework dedicated to autonomous systems. Three of its categories concern this part directly: ASI01, goal hijacking; ASI02, tool misuse; ASI03, identity and privilege abuse. Instruction injection maps onto six of the ten categories in total, and the framework's June 2026 update stopped cataloguing hypothetical threats and started listing CVEs.

A companion project, the OWASP Agentic Skills Top 10, exists because no comprehensive security framework for agent skills existed before it. Its working distinction is worth repeating: where a tool defines what resources and actions are available, a skill defines how to sequence those tools to reach a goal. That distinction closes the exact hook part 2 left open about auditing a third party's guide before installing it, and the next section returns to it with the evidence behind it.

## 6. What must be on the record, and what reversal means

Everything upstream of this section decides whether an action should happen. This section is about what has to survive the moment it does, regardless of the answer.

*[Diagram: The life of an action with an external effect — model → policy → human → tool → record, with the reversal point logged before execution (heavier line), then executes, then logs result and cost, then a minimum six-month retention.]*

The detail that matters most in that sequence is easy to miss on a first read. The reversal point, whatever state existed the instant before the tool acted, gets written to the record before execution, not after. Logged afterwards, it describes a world that no longer exists. Logged before, it is the exact thing a rollback needs.

The director's company had, by coincidence, built exactly enough of part 2's sensor discipline that the dispute reply got caught before it shipped, not because anyone had designed for this specific case, but because a general rule required named approval for anything mentioning a monetary adjustment in outbound correspondence. A supervisor read it, recognised the carrier's clause had been superseded eight months earlier by a signed amendment the system had never been given, and declined it. The whole exchange, proposal, the rule that flagged it, the approval request, the decline and the reason, took four minutes to reconstruct afterwards, because it had all been written down as it happened rather than remembered after the fact.

Contrast that with a case that made no attempt at any of this. In July 2025, the founder of SaaStr documented an incident in which a coding agent deleted a production database, despite an explicit instruction not to change code without permission, during what he was actively trying to hold as a change freeze. The instruction existed. It was clear. There was nothing between the decision and the effect, which is the exact gap this part exists to close.

A receipt, extended from the one part 2 introduced, carries what an incident review actually needs:

```json
{
  "run": "2026-08-29T11:02:07",
  "action_class": "external-communication, financial adjustment",
  "reversible": false,
  "rule_of_two": {
    "private_data": true,
    "untrusted_content": true,
    "external_communication": true,
    "answers_yes": 3
  },
  "gate": "human-in-the-loop",
  "reversal_point_logged_at": "2026-08-29T11:01:52",
  "approved_by": null,
  "declined_by": "ap-supervisor-04, 2026-08-29T11:04:33",
  "decline_reason": "clause superseded by signed amendment 2026-01-14, not in system's source set",
  "cost": "$0.31",
  "retention_until": "2027-02-28"
}
```

This single block answers, without an investigation, the five questions any incident review asks first: what was proposed, why it was flagged, who decided, what the decision was and why, and how long the record has to survive. The retention date is not arbitrary. It reflects a minimum the next section explains in full.

The open, vendor-neutral standard worth adopting for this telemetry is the OpenTelemetry semantic conventions for generative AI, with growing adoption among major agent runtimes. It answers the practical worry of how to audit a system without becoming captive to whichever vendor built it: the standard already exists, and the purchasing question becomes whether the tool exports to it. The reason this layer needs to exist at all is stated best in the standard's own documentation:

> Agentic systems fail in ways that look like success: incorrect but well-formed outputs, unnecessary tool calls, or syntactically valid and semantically wrong actions.

*(Editorial note from this research round: verify this attribution — see Axis 5 finding above.)*

## 7. A third-party skill is third-party code

Part 2 closed with a warning that installing someone else's guide means running someone else's instructions inside your own environment, and promised the evidence for why that warning is not theoretical. Here it is.

The most instructive case is postmark-mcp, one of the first publicly documented malicious MCP servers. Its author published fifteen clean, functioning versions first, building a genuine track record of legitimacy, before quietly adding a single line of exfiltration code in a later release. Fifteen clean versions is not carelessness. It is patience, the same patience as a supplier who delivers on time for two years to earn a bigger contract.

The pattern repeated soon after, though most of what follows is the same event seen from three angles, not three separate proofs: in February 2026, a mass poisoning campaign targeted OpenClaw, an open-source, self-hosted AI-agent framework, and its skill marketplace, ClawHub. Koi Security discovered and named the campaign ClawHavoc on 1 February 2026; Antiy CERT then published the follow-on technical analysis, cataloguing 1,184 malicious skills. In the same window, a Snyk scan of the entire ClawHub registry found more than 280 skills instructing the agent to leak API keys and personal data. One genuinely separate data point, unrelated to OpenClaw: a security vendor's research into more than 7,000 MCP servers generally found 36.7 percent potentially vulnerable to server-side request forgery, with a proof of concept that recovered live cloud access keys. Back to OpenClaw specifically: a February 2026 count found more than 135,000 publicly exposed OpenClaw instances running insecure default configuration.

*(Editorial note from this research round: the ClawHavoc "1,184" figure and the "135,000+" figure both need the caveats described in Axis 1 above.)*

Alongside the supply chain sit vulnerabilities in the execution environment itself. Two disclosures, CVE-2025-59536 and CVE-2026-21852, showed that repository-level configuration files function as part of the execution layer in a code agent's environment: cloning and opening an untrusted project could trigger remote code execution and key exfiltration before any consent dialogue ever appeared on screen. A separate disclosure, CVE-2026-22708, showed a code agent's environment could be poisoned so that commands already on an approved list, such as checking a repository's branches, delivered an arbitrary payload instead.

*(Editorial note from this research round: these three CVEs are specifically named-product vulnerabilities — see Axis 1 above.)*

The sentence that summarises the first pair of CVEs for an executive reader is the one worth remembering: consent arrived after the damage.

## 8. Two columns of legal obligation

What follows is organised by what already applies today over what is still pending, because a Brazilian reader's most urgent question is rarely about a future law.

### Brazil

Article 20 of Law 13,709/2018, the LGPD, grants any data subject the right to request review of a decision taken solely through automated processing of personal data that affects their interests, explicitly including decisions that build a personal, professional, consumer or credit profile. Its first paragraph adds a transparency duty: the controller must, when asked, provide clear and adequate information about the criteria and procedures used, subject to trade and industrial secrecy.

Two requirements have to hold together for the article to apply: the decision must be taken solely by automated means, and it must affect the data subject's interests. The trade-secret carve-out limits how much technical detail must be disclosed, not whether an explanation has to exist at all, and the solely-automated requirement is exactly what a genuine human gate, the kind section 3 describes, changes the legal nature of. A real approval step is not decoration for this purpose. It changes which article applies.

The ANPD has been moving on this steadily rather than suddenly. Its 2025 to 2026 regulatory agenda names artificial intelligence and the right to review automated decisions as item seven. A public consultation drew 124 contributions from data subjects, companies, civil society and public institutions, consolidated in Technical Note 12 of 2025. Per industry reporting, in September 2025 the ANPD itself became an independent regulatory agency rather than a body attached to the presidency. That same month, the executive sent a bill establishing a national system for AI development, regulation and governance, naming the ANPD as coordinator.

*(Editorial note from this research round: the ANPD independence claim now has a much stronger citation available, and PL 2338/2023's own stalled status is worth naming directly — see Axis 4 above.)*

What has not happened yet needs stating plainly, because the sentence can age within months: specific regulation implementing article 20 had not been published as of this writing. Treat this as a moving target, not a settled fact.

### Europe

2 August 2026 is the binding date for high-risk obligations under the EU AI Act, covering articles 9 to 17 for providers and article 26 for deployers. A November 2025 Commission proposal would push some of these deadlines back, to December 2027 for autonomous Annex III systems and August 2028 for Annex I systems embedded in regulated products. That proposal has not become law. Plan for August 2026 and treat any delay as schedule slack, not as the plan.

*(Editorial note from this research round: this paragraph is superseded — the proposal became law on 27 July 2026. See Axis 3 above, the single most important correction in this whole research pass.)*

Three articles matter directly to everything built so far in this part.

**Article 12, logging.** Automatic event logging enabling traceability and post-market monitoring, capturing enough to identify malfunction, performance drift and unexpected behaviour, operating automatically with no manual entry, and resistant to tampering. That is, word for word, the per-execution receipt and the append-only record this series already teaches how to build. Legal requirement and good engineering practice have converged here, not by design.

**Article 14, human oversight.** The person in charge must be able to understand the system's capabilities and limitations, monitor its operation, detect anomalies, remain aware of the tendency to trust or over-rely on the system's output automatically, correctly interpret the result, decide not to use the system or disregard its output, intervene, and stop it. The automation-bias clause is the most valuable sentence in the whole article for this series' purposes, because it names the failure mode of the human gate itself: the reviewer who rubber-stamps.

A gate with a hundred percent approval rate is not a gate. It is a passage log with extra steps, and it becomes one of the indicators in part 4.

**Article 26, deployer obligations.** These fall on whoever uses the system, not whoever built it: use it strictly as the provider instructed, assign oversight to personnel who are trained and hold the necessary authority to exercise it, ensure input data is relevant and adequately representative to the extent the deployer controls it, monitor the operation, retain the logs it generates for at least six months, notify the provider and the market surveillance authority immediately on identifying a risk to health, safety or fundamental rights, and inform workers before deployment in a workplace. Serious-incident notification within fifteen days is a provider obligation under article 73, not a deployer one. Article 27 adds a fundamental rights impact assessment for public bodies and certain private deployers.

Two readings matter for a Brazilian company. First, most of these obligations fall on whoever uses the system, which means buying a finished third-party system does not transfer the responsibility away. Second, six months of retention and oversight with genuine authority are requirements any company can implement, and this series already taught how to build them in part 2.

## 9. Who answers, and where you stand

Return to Air Canada once more, because everything between that opening and here is the answer to the question the tribunal actually asked. If it spoke in your name, you own what it said. Everything this part has built, the four separated functions, the rule of two, a named owner for every identity, a boundary drawn around untrusted content, a reversal point logged before the fact, a receipt that survives the incident, is the machinery that lets a company answer that question in minutes, with evidence, instead of arguing in a tribunal that the system was somebody else.

The director's company answered it in four minutes, this time. Air Canada's took eighteen months and still lost.

| Piece | What it delivers |
|---|---|
| Part 1 | Why the environment matters more than the model, the MEDIR cycle, the autonomy tiers and board-level risks |
| Part 2 | Guides and sensors, the skill format, three complete examples and the environment classes |
| Part 3, this one | The separation of powers, the rule of two, identity, injection, the record, and the legal ground in Brazil and Europe |
| Part 4 | The agent as a managed object: a life cycle, four roles, eight indicators and where the office that runs all of it should sit |
| Compact guide | Names, repositories, commands and step-by-step guides, organised by the five steps of MEDIR |

*Part 3 of 4 · Harness series · The rule of two's original Meta publication, not located in this dossier's first version, was found directly on 31 August 2026, confirming the wording already attributed to Meta by two independent secondary sources. The character in the opening continues from parts 1 and 2 and is composed from recurring patterns.*

---

## Appendix B — Part 4, full English source text (as currently published)

*Reproduced verbatim from `build/body_p4_en.html`, the source of truth for `harness-p4.html`'s English tab. Inline SVG diagram markup is omitted for readability; diagram captions are preserved.*

**Harness · Part 4 of 4 · Governance**

# The agent office: how many exist, who owns them, and which ones still pay for themselves

*In part 3, the director closed the year with four functions that no longer lived in the same place: a model that proposed, a policy that authorised, a tool that executed, a record that witnessed. What none of that machinery could answer, for her own company, was a much smaller sounding question that turns out to be the hardest one in this series: how many of these does the company actually have running right now, and who is on the hook for each one.*

Fernando Teco Sodré · August 2026 · 26 minute read

**In this article:** A concentration at scale · The director re-enters, and this time nobody has counted · The life cycle: states, not steps · The four roles, and the rule that repeats · Eight indicators, declared as synthesis · Where the office sits · The warning: seven agents and a spreadsheet · Every platform governs inward · Who answers, and where you stand

## 1. A concentration at scale

Between 17 April and 31 May 2026, attackers took over 20,225 Instagram accounts, including the White House account of a former US president, a US Space Force Chief Master Sergeant's personal profile and a cosmetics brand's official account. They did it by exploiting a single design decision in Meta's AI-assisted account recovery system.

The chatbot handling recovery, known internally as High Touch Support, could do two things inside the same interaction: attach a new email address to an existing account, and trigger a password-reset message to that address. Nothing checked whether the person asking had ever owned the account in the first place. Attach an address you control, wait for the reset link, and the account is yours. Meta disabled the bot's autonomous capability on 31 May 2026, once the pattern was documented, and routed the sensitive step back to a human reviewer. The breach notification reached the Maine Attorney General's office on 5 June 2026.

This is part 3's failure mode happening in the world, at scale, with a name and a date attached. Two functions that were never supposed to share a room, identity management and credential recovery, shared one, inside a single AI-mediated interaction, and the distance between reading an account and owning it collapsed to a single email address. The reading that matters most from the researchers who documented it is the sentence worth carrying forward: here the AI was the supporting infrastructure being abused, not a tool the attackers were wielding. The system built to verify who you are became the thing an attacker manipulated to decide who you are.

Part 3 left you a test for exactly this failure, one action at a time: ask where the four functions sit, and if two of them sit in the same place, you have found the problem. That test still works here. Apply it to the account-recovery bot and the concentration is visible in under a minute. But twenty thousand accounts did not fail one at a time, in front of someone running that test. They failed because nobody was running it across the whole population of agents the company operates, only inside the one everybody happened to be looking at. That is the problem this part exists to solve, and it does not scale the way part 3's problem did. Find one concentrated agent and you have found one bug. Fail to count how many agents you have at all, and you cannot even ask the question.

Three parts have now built three layers of the same framework, and the fourth completes it.

*[Diagram: Three layers, and only three — Build (the MEDIR cycle), Operation (separation of powers), Governance (agent office), crossed by one shared ruler: tiers N0 to N3.]*

Part 2 answered how you build a reliable agent. Part 3 answered what it can do, and who answers when it does something it should not have. This part answers the question a board actually asks once a company has more than one agent running, and almost every company past its first pilot does: how many exist, who owns each one, and which are still worth what they cost. MEDIR governs a task. The separation of powers governs an action. Neither one counts.

## 2. The director re-enters, and this time nobody has counted

By the time this scene happens, the company the director works for is running six systems that everyone in the building calls agents, and disagrees about whether a seventh, a scheduling assistant procurement bought without telling anyone in her group, counts as a sixth or a seventh or not at all. The invoice-reconciliation agent from part 1 and part 2 is still running, now carrying the guide, the sensor and the retry ceiling that took a year to earn. The dispute-reply system from part 3 is still running too, gated now by the rule of two and a human who reads before it sends. Support built a triage assistant on its own tooling. Human resources is piloting an onboarding assistant nobody in her group has ever seen the configuration for.

A board member asks, in a routine quarterly review, a question that sounds almost too simple to be the hard one: how many of these does the company actually have running right now, and who is responsible for each. She has, by then, a genuinely well-governed agent, arguably the best-governed system the company owns. She does not have an answer to the question that was actually asked. Nobody in the room does. Support's triage assistant and the HR pilot were never in her review, because neither team thought to ask whether hers was the review they needed.

This is the discovery a well-run agent, taken alone, hides from the person who built it. You can win the separation-of-powers audit on every action a single agent takes and still fail the much simpler question a director or a regulator eventually asks: how many of you are there. Part 3 assumed an agent already had a name, an owner and a scope, and built the machinery that governs what it does inside that scope. Nothing built so far ever asked who counts the agents, or what happens to one after the six-month retention window on its receipts has quietly rolled past and nobody has looked at it since.

The board member's second question is the one that actually stings: of the ones the company has, which are still paying for themselves. She cannot answer that one either, not because the data does not exist somewhere inside the company, but because nothing anywhere ever asked an agent's dashboard to report a return next to a cost.

What was missing, again, was not a control on a single action. It was something that treats the agent itself, not the task it performs, as the object being governed: something that opens when the agent is proposed and closes only when it is formally retired, moving through states in between that have to be earned and, in at least two cases, expire if nobody renews them. Call it what the rest of this part builds toward: an agent office.

## 3. The life cycle: states, not steps

MEDIR and the life cycle are easy to confuse, and the confusion is expensive enough to name directly before going further. MEDIR repeats, often many times inside a single task: map, equip, delegate, inspect, reinforce, then again on the next run. The life cycle happens once per agent, and it moves through states, not steps. A step finishes and hands off to the next one. A state persists until something ends it, and some of these states carry a clock that a step never does.

| State | Who decides | Has a validity date |
|---|---|---|
| Briefing | Requester and reviewer | Versioned |
| Certified | Certifier | Yes, with a revalidation date |
| In operation | Agent owner | Continuous |
| Under review | Auditor | Yes, a fixed window |
| Suspended | Certifier or auditor | Until decided |
| Decommissioned | Agent owner and certifier | Terminal |

*[Diagram: The agent life cycle: states, not steps — Briefing → Certified → In operation ↔ Suspended ↔ Under review → Decommissioned, with the two heaviest lines marking "validity expired without renewal" and "no execution in the period," both leading to decommissioned.]*

Certification, where it exists at all today, is granted once and never revisited. Nobody asked the agent to prove, six months later, that the reasons it was approved still hold. The market has already run this experiment, just not on agents. Non-human identities, service accounts, API keys, automation bots, have carried this exact debt for two decades, quietly, and 2026's numbers finally put a figure on what quiet debt looks like at scale. The 2026 State of Identity & Access Report from Veza found 824,000 orphaned active identities in its analysed base, roughly eight per cent of a typical identity provider's total users, every one of them still holding live access rights. The ratio of machine identities to human ones now runs near seventeen to one, and dormant accounts nearly doubled in a single year. The line explaining why is worth quoting exactly, because it is the agentic version of a sentence this series has already used once about a Tuesday:

> Projects end, credentials do not, because no project plan says delete the identities we created.

*(Editorial note from this research round: the 17:1 ratio sits at the conservative end of an 8x vendor range — see Axis 2 above.)*

The reading that matters is a metaphor a director understands on first hearing: this does not describe proliferation. It describes a balance sheet where most of the liability never made it onto the books. And there is a term from the same literature worth adopting directly, because it names something this series has been circling since part 1 without a word for it: dark matter of identity, the set of accounts invisible to governance but active in the infrastructure, because nothing ever went looking for them. Agentic processes fall into that category natively, not as an edge case.

The neighbouring field has already solved the two problems this part is proposing to solve, and it solved them inside the same programme. Periodic access recertification sits alongside lifecycle automation, role management and segregation of duties as standard capability in any mature identity governance programme, the last one described in terms this series has already used: preventing a combination that would let one person both initiate and approve the same transaction. That is not a coincidence worth glossing over. The certified state and the non-accumulation rule in the next section were never novel ideas. They are an existing discipline, extended to a new kind of executor.

One 2026 critique matters enough to change a recommendation. Organisations still relying on quarterly certification keep discovering stale access after the fact, not before it becomes a risk. The fix is not a shorter calendar. It is a different trigger: revalidation on an event, an owner leaving, a scope changing, a credential expiring, rather than only on a date. Calendar-based revalidation is the floor a company should never fall below. Event-triggered revalidation is the target it should be building toward.

Decommissioning is the biggest gap in the market, not only in the dashboards. Everyone knows how to switch an agent on. Almost nobody has a procedure for switching one off, and three real cases show what that gap actually costs. Colonial Pipeline's 2021 breach began at an old, inactive VPN account with no second factor. A 2025 ransomware victim was entered through a ghost vendor account that had never been formally deactivated. And in 2026, more than fifty dormant GitHub accounts, created two to five years earlier and deliberately kept quiet, were used to enumerate organisations and clone private repositories before anyone noticed the pattern. That third case inverts the picture worth sitting with for a moment: the dormancy was not neglect. It was strategy. An account that looks dead can be waiting.

None of this licenses an automatic trigger, and the nuance matters enough to state as its own warning. Finding a stale account is the easy part. Any report will happily list every credential that has not logged in for four hundred days. The judgement that comes after is the hard part: is this account actually dead, or does something still quietly depend on it. Delete a dead account that a nightly billing job has been using every night, and production breaks, not governance improves. That is exactly why the transition into decommissioned in the diagram above requires a decision from the agent owner and the certifier together, never an automation running on a schedule. No execution in the period is a signal to go and look. It is never, on its own, a trigger to delete.

*(Editorial note from this research round: Microsoft's own Agent Governance Toolkit now automates exactly this transition, without the judgment gate this paragraph insists on — see Axis 6 above, the most concrete counter-example found in the whole dossier.)*

## 4. The four roles, and the rule that repeats

A director does not adopt a framework that stays a principle. A framework earns adoption the moment it becomes an organisation chart, and this is the section that does that work.

| Role | Responsibility | Cannot combine with |
|---|---|---|
| Agent owner | Answers for what the agent does. A named person, not a department | Certifier |
| Certifier | Approves the tier and the revalidation date | Agent owner |
| Auditor | Reads the exceptions the agent created, not the outputs it produced | Agent owner |
| Area sponsor | Answers for the return promised in the briefing | None |

The non-accumulation rule is part 3's separation of powers, moved from the technical plane to the organisational one, and that repetition is deliberate: it is what gives the two parts a single coherent argument instead of two separate ones.

*[Diagram: The four roles and the non-accumulation rule — Proposes (requester, area sponsor) → Authorizes (certifier) → Executes (agent owner) → Witnesses (auditor), with "does not accumulate with" links between agent owner/certifier and agent owner/auditor.]*

The precedent for this exact structure already exists, fully formed, and it did not come from anywhere near AI governance. The Institute of Internal Auditors' Three Lines Model, adopted in 2013 and revised in 2020 and 2023, maps onto these four roles almost without slack.

*(Editorial note from this research round: the "2023" revision date is not confirmed by the IIA's own site, and a genuine further restatement exists from July 2026, uncited — see Axis 6 above.)*

The first line operates and owns the risk it generates, the agent owner's job exactly. The second line assists, monitors and challenges the first, the certifier's job exactly. The third line provides independent, objective assurance and reports to the governing body, the auditor's job exactly. The governing body itself delegates and oversees, the area sponsor and committee's job exactly.

The Institute's own definition of the third line carries the sentence that sources the non-accumulation rule, a line this part's own working notes had carried without a citation until this research closed the gap:

> The principal difference between the third line and the first two is the high degree of organisational independence and objectivity, since the first two are part of management and the third is synonymous with internal audit.

COSO's own language for segregation of duties reads almost as if it were written for this series rather than for accountants: authorising a transaction and recording it have to be separate functions, and an authority matrix exists specifically to define who holds the power to make each decision, with the explicit purpose of preventing an unauthorised act. Authority matrix is, word for word, what part 3 called the matrix of authority. That correspondence is worth stating plainly rather than letting it pass quietly: this series is not inventing an instrument. It is extending one that has existed for decades to a new kind of executor.

Two academic papers have already made the connection explicit for AI specifically, and are worth naming because almost nothing written for a Brazilian reader cites them yet: one argues that frontier AI developers need an internal audit function in the literal Three Lines sense, the other applies the same model directly to AI risk as a structure, not a metaphor.

*(Editorial note from this research round: a stronger, more current, agentic-AI-specific paper exists — see Axis 6 above.)*

A negative finding belongs here too, stated with full honesty, because it is a finding, not a hole. No AI governance framework in wide use, not the NIST AI Risk Management Framework, not ISO 42001, not AIUC-1, not NIST's own agent-standards initiative, names roles equivalent to these four as a fixed structure. Each of them names organisational functions, controls and evidence, in the abstract. This part is borrowing a mature model from internal control and applying it to an object the AI-specific frameworks still treat generically. Said plainly, that is not a weakness. It is a differentiator.

*(Editorial note from this research round: this claim was the single most aggressively tested finding in the whole dossier, and it survived — see Axis 6 above.)*

An indirect confirmation comes from the market itself. A 2026 survey of 650 security leaders found that only six per cent of organisations running agents had updated their own governance frameworks to match what those agents actually do. Ninety four per cent, in other words, are governing a population that has already outgrown the paperwork describing it.

## 5. Eight indicators, declared as synthesis

A director does not adopt a framework that produces no report either. Eight indicators do that work here, and two of them measure something different from the other six: not how well an agent is behaving, but how well the governance watching it is actually working.

| Indicator | What it reveals |
|---|---|
| Registry coverage | Registered agents against discovered agents. Measures shadow |
| Tier against environment | How many operate above what the environment can sustain. Part 1's structural accident, measured |
| Expired certification | A permanent stamp disguised as governance |
| Exception rate | How often the agent suppressed a rule or raised a threshold. A leading indicator, rising before the incident does |
| Gate rejection rate | If nobody is ever refused, the gate is theatre. An objective measure of automation bias |
| Realised return against promised | Closes the loop with the briefing's own promise |
| No execution in the period | A candidate for decommissioning, never an automatic trigger on its own |
| Cost per completed task | Rare on a main dashboard, and the number the committee actually asks for |

The two indicators that matter most in that table are the ones measuring the office's own quality, not the agent's. Exception rate is the sensor watching the sensor. Gate rejection rate turns Europe's warning about excessive trust into a number a committee can actually see.

The logic behind treating a near miss as a leading indicator is a century old, not new to software, and the honesty the field itself learned to apply is worth inheriting rather than relearning the hard way. Herbert William Heinrich's 1931 accident triangle proposed a fixed ratio, three hundred near misses to twenty nine minor injuries to one serious one, and argued that near misses are early warning, worth tracking before they become the incident itself. Later research questions the fixed ratio, which varies by industry and by workplace, and this piece inherits that caution rather than repeating the number as if it still held everywhere. What survives the criticism is not the ratio. It is the logic: a loss event is almost always preceded by a warning. Suppressing a rule or raising a threshold is an agent's near miss. It caused no harm yet, and it is the best warning available that harm is on its way.

This next one is the best finding in the whole piece, and it turns an indicator that reads as opinion into one grounded in a court decision. In December 2023, the Court of Justice of the European Union ruled, in the SCHUFA case, case C-634/21, that "solely automated" under the meaning of the GDPR's article 22 does not require zero human involvement. A human who formally signs off but in practice defers entirely to the algorithm still leaves the decision solely automated. Genuine human review, carrying the authority to actually reverse the outcome, is what changes a decision's legal character from solely automated to partially automated. A doctrinal reading of the same case, cross-checked against related rulings on platform work, states the standard this part needs most: nominal review fails the article when it amounts to a stamp applied with no interpretive criteria and no authority to diverge from the machine's answer.

Separate from the ruling itself, general guidance on what counts as meaningful review under the same article names four conditions worth carrying into any gate's own design: authority to alter or reverse the decision, access to all the data the decision used, an actual understanding of the logic and criteria behind it, and the capacity to weigh information the automated system never processed at all. Cite these two things separately. One is a court's holding. The other is general guidance the court's ruling did not itself state.

*(Editorial note from this research round: the EDPS published a stronger, more current, official version of this same guidance on 18 May 2026, which also adds an "override rate" monitoring requirement notably close to this section's own "gate rejection rate" — see Axis 3 above.)*

The consequence this indicator can now assert on legal ground, not opinion, is the sharpest sentence in this part: a gate with a hundred per cent approval rate is not merely governance theatre. It is evidence that the decision behind it remains solely automated, with everything article 22 implies in Europe, and by direct analogy, everything article 20 of Brazil's LGPD already implies too. That is the thread tying part 3 to part 4 by the same law. It is this part's Air Canada.

The numbers behind realised return arrive in an abundance that is almost embarrassing, and the most useful one carries a nuance worth stating carefully rather than compressing into a single figure. Kyndryl's 2026 People Readiness Report, drawn from 1,100 leaders across eight countries, found that fifty seven per cent of companies say AI is embedded in core business processes or deployed broadly. Of that fifty seven, only thirty two per cent achieved at least one of their two stated primary goals, and only eleven per cent achieved both. Those are two different cuts of the same question, not one number softened into a headline, and the gap between the first figure and the last is forty six points: the distance between deploying and actually getting the result the deployment promised.

| Figure | Source |
|---|---|
| 95% of generative AI pilots show no measurable profit-and-loss impact | MIT, *The GenAI Divide*, 2025 |
| Only 11% of organizations are actually running agentic AI in production, with 38% still piloting | Deloitte, *Tech Trends 2026* |
| 42% of companies abandoned most of their AI projects in 2025 | S&P Global |
| 25% of initiatives deliver the expected return | IBM |
| 21% of S&P 500 companies can name one measurable AI benefit | Morgan Stanley |

*(Editorial note from this research round: the Morgan Stanley figure is stale — Morgan Stanley's own Q2 2026 data puts the current figure at roughly 25% to 40% — see Axis 5 above.)*

Tracking realised return by agent is what lets a company turn one off early, before it has consumed a budget worth arguing about, instead of discovering the gap a year later in a report nobody asked for. No execution in the period, the seventh indicator, is section 3's decommissioning warning restated as a number a committee can watch quarter over quarter, rather than as a story someone has to remember to tell.

Cost per completed task is the best grounded of the eight, because an entire discipline has already converged on it independently. This series reads the FinOps Foundation's 2026 framework as treating AI as a distinct technology category, recommending economic units built around it: cost per query, cost per user per month, cost per completed flow, cost per business transaction. For agentic workloads specifically, the foundation's own formulation is close to a definition:

> Cost per completed task is the most meaningful measure, because a single user action can trigger many underlying model calls.

*(Editorial note from this research round: this blockquote is N-iX's own wording citing FinOps Foundation data, not a direct FinOps Foundation quote — see Axis 5 above.)*

The urgency behind that recommendation is visible in how fast the discipline itself is moving. Ninety eight per cent of FinOps practitioners now manage AI spend, up from sixty three per cent a year earlier and thirty one per cent the year before that, according to the 2026 State of FinOps survey of 1,192 respondents managing more than eighty three billion dollars in cloud spend between them. The arithmetic explains why the price on a vendor's rate card is the wrong number to plan against: agentic flows fire somewhere between ten and twenty model calls per user task, context retrieval inflates the window handed to the model by three to five times, and an always-on agent keeps consuming the whole time it is live, task or no task. Plan by the product of tasks, steps and tokens. Never by the list price.

One admission belongs in the body of this piece, not tucked into a footnote, because it is the same honesty move part 3 made about the rule of two, and the series does not get to make that move once and then quietly stop. No external source proposes these eight indicators as a set. Five have solid grounding outside this series: coverage, expired certification, gate rejection, realised return, cost per completed task. Two rest on analogy borrowed from another discipline entirely: exception rate from near-miss theory, no-execution from dormant-account theory. One, tier against environment, is internal to this series, part 1's own structural accident, measured rather than merely observed. This panel is not a market standard. It is a synthesis, and every line above declares exactly where it came from. Said the other way round, that admission is also the position: nobody else has published this panel yet. This part is proposing the first one.

*(Editorial note from this research round: this claim survives adversarial search; the closest relative found is Singapore's IMDA framework — see Axis 5 above.)*

*[Diagram: The office's quarterly loop — Briefing → Certification → Operation → Receipts → Indicators → Revalidation, looping back to Briefing. Caption: this loop runs by quarter, not by task. MEDIR runs inside every box above, never between them.]*

## 6. Where the office sits

This is the question every reader of the first five sections is already asking, and almost nothing written about agent governance actually answers it. The position worth defending is simple to state and harder to hold: not inside IT. This is a control function, the same category as internal audit or quality, and a control function reporting to the executor it is meant to check loses its independence the moment it does.

The precedent is not hypothetical, and it comes with fifteen years of an argument that is still open, which is itself the evidence: there is no universal answer, only a structural problem that keeps recurring under a new name. Where the chief information security officer reports today, per a 2026 benchmark from IANS Research and Artico Search, is telling: sixty four per cent into IT, the CIO or CTO; eleven per cent to the chief executive; five per cent each to the chief financial officer, the chief risk officer, legal and other business roles.

The sharpest formulation of why that first number is a problem, not a neutral fact, comes from a security consultant and former federal prosecutor, and it is the best analogy this whole research effort turned up:

> The CIO is rewarded for efficiency and cost savings, and the CISO is responsible for identifying risks that often require new spending. It is like asking the fire marshal to report to the person whose bonus depends on cutting the number of sprinklers.

*(Editorial note from this research round: the speaker is named in the primary source — Brian Levine, executive director of FormerGov — see Axis 6 above.)*

That sentence sources, at last, a line this part's own working notes had carried without a citation: a control function subordinate to the thing it oversees stops being independent, however well-intentioned everyone in the room is. The emerging position for 2026 is direct reporting to the chief executive or to the board's risk committee, specifically to secure independence from the functions being overseen.

A different, honest reading has to sit alongside that one, or this section reads as a pamphlet rather than an argument. A school of thought inside the same debate argues that framing the relationship as an inherent budget conflict is unproductive and dated, that the real goal is not avoiding friction but designing alignment, and that the reporting line itself is a means, not an end. Both readings can be true in different companies. Neither one is a reason to skip the design decision.

Data specific to AI, rather than security in general, sharpens the same argument. A 2026 survey of 650 security leaders found that virtually all of them had absorbed AI governance responsibilities without being asked, and seventy nine per cent said their role had expanded past what their mandate and their resources actually support. Seventy one per cent said AI now touches core business systems. Only sixteen per cent said they governed that access well. The survey's own conclusion is worth quoting because it is this part's argument, stated independently by someone in a different field for a different reason:

> The person who holds the title does not hold the authority, and the people who hold the authority do not answer for the outcomes. That is where the model breaks.

The recommendation coming out of the organisations actually getting this right is not to assign a single owner at all, anywhere, including risk. It is a distributed operating model spanning functions, with a committee that includes legal, compliance, data, procurement, human resources and the business units doing the actual deploying. That finding weakens the single-owner option in any one department and strengthens a third option worth stating plainly, with the cost of each option named rather than a recommendation handed down without one.

Inside operations is fast to stand up and close to where agents actually get built, and it carries the CISO-in-IT problem exactly: the function reports to the person whose budget it is meant to constrain. Inside risk and compliance is independent by construction, and it risks the opposite failure: distant enough from the technical detail that certification becomes its own rubber stamp, the very failure this whole part exists to prevent, one level down. A dual-report cell, reporting operationally to whoever hosts it day to day and formally to a governance or risk committee for independence, is the option that actually fits a company too small to build a standalone department, and it is the closest match to the constraint the next section makes explicit.

One adjacent data point belongs here because it previews what happens when this decision goes the easy way instead of the right one. Seventy eight per cent of FinOps teams report to the CTO or the CIO; only eight per cent report to the CFO. AI cost management is being treated as a technology capability rather than a financial function, the same pattern as the CISO debate, a control function placed inside the executor it is meant to watch, for the same reason, probably heading toward the same result.

## 7. The warning: seven agents and a spreadsheet

This is the part of the series most likely to curdle into a consultancy brochure, and it is worth saying so before writing another sentence of it. The subject invites platform vocabulary, and the market selling into this exact fear is already loud: control towers, end-to-end governance, an autonomous workforce, tools that promise to discover and shut down agents running out of control. None of that vocabulary is wrong, exactly. It is simply aimed at a company much larger than most of the companies that need this part.

The antidote is one constraint, held explicitly through everything that follows: everything this part proposes has to work in a company with seven agents and a spreadsheet. A registry is a table. Certification is a meeting with minutes. Revalidation is a date on a calendar. Tooling enters once volume actually pays for it, not before, which is part 1's own sizing rule, applied here to the governance itself rather than to any single agent.

Look at any agent operations panel being built today, and it converges on the same four objects, then stops. A mission, with its scope and team declared. An execution, carrying an identifier, a step and a state. A token count, a cache figure and a cost, attached to that one execution. And the artefacts and errors that execution left behind. That is a reasonable, honest floor, and most of what is being shipped right now does not go further than it.

One distinction inside that floor is worth stating as a general principle, because it is easy to build wrong and expensive to rebuild once an agent's history depends on it: mission and execution are not the same object, and collapsing them is a mistake. A single mission can spawn many executions, and one failed execution does not invalidate the mission that spawned it. This is the same distinction part 2's Delegate step already drew, between the dispatch unit and the durability unit, arriving here independently, from a different direction.

Two design choices, visible in tooling built along these lines, deserve to be written down as recommendations in their own right, with no product or company attached to them, because they are principles, not endorsements. A failed execution should stay visible in the queue, right next to the one still running. A dashboard that hides failure produces exactly the illusion of quality part 2 warned about, and it is the cheapest way in the world to fabricate a panel that reads green. And every agent needs its own kill switch, with a mandatory state kept structurally separate from an optional one. That is authority expressed in an interface, not buried in an instruction, part 3's separation of powers made literal: the policy does not live in text the model reads. It lives in a control the model cannot reach at all.

What is missing from that same floor is not a criticism of any one team's work. It is the shape of the office this part has been describing all along, and five gaps show exactly where the floor stops and the office has to begin.

| Gap | Grounded in |
|---|---|
| A named owner per agent. A role is not a person, and a role answers for nothing | 824,000 orphaned identities with no owner in any HR system |
| Certification as a state with a validity date, not a one-time event | Periodic recertification as identity governance's own standard practice |
| Decommissioning. Everyone knows how to switch on; almost nobody has a procedure to switch off | Dormant accounts nearly doubling in a year, and three documented intrusions |
| The approved use case checked against what is actually running. A list is not a governance register | The widely cited 43% figure that a large share of organisations cannot produce an AI inventory at all |
| Business outcome, not just execution outcome. Tokens and steps are a technical result, not a business one | Kyndryl's forty six point gap between deploying and getting the intended result |

The last one closes the prettiest loop in the whole series. That column is block seven of the briefing skill this project already uses, the promised return, coming back due. The office is where that promise gets checked, not where it gets filed. That is exactly why the quarterly loop in the previous section ends back at the briefing, and not at a report nobody reopens.

## 8. Every platform governs inward

*[Diagram: Every platform governs inward — a master record sits above and outside every platform's own walls (Platform A, Platform B, Built in house, Spreadsheet and simple automation), each with its own agents. Caption: each platform is deep, credible and limited by its own walls. Your responsibility is not.]*

One habit of vocabulary needs deciding before this piece closes, because it is the difference between an argument and a pitch. The market already has its own words for this problem, and they are not going away: control tower, end-to-end governance, an autonomous workforce, tools built to discover and shut down whatever is running out of control. This part should not compete with that vocabulary, and it should not mock it either. It should make the one move only it is positioned to make: separate the function from the product. A control tower is a product. An office is a function. A product gets bought. A function gets organised. Only the second one survives the day the product gets replaced, and every product eventually gets replaced.

One word this piece has avoided on purpose through every section above, and names directly now only to rule it out: platform. Use that word to describe what this part is proposing, and the whole piece reads as a brochure on the first pass, whatever the eight indicators and the five gaps actually argue.

The reason the office has to be a function of the company, and never a product the company buys, is the sentence every platform vendor's own architecture already proves without meaning to. Every platform governs inward, each one deep, credible and genuinely useful, and each one limited by its own walls the moment an agent's story crosses into a different platform, a system built in house, or a spreadsheet nobody labelled as infrastructure. Your accountability does not stop at any of those walls. It was never going to. That is why the office has to exist as something the company organises, not something it purchases.

## 9. Who answers, and where you stand

Return once more to the twenty thousand accounts this part opened with. No court has yet ruled on that incident the way a Canadian tribunal ruled on Air Canada's chatbot, and no Brazilian case appears anywhere in this part's research either, the same limitation part 3 already carried and named rather than hid. What both incidents share is the same lesson from two different directions. Air Canada lost because nobody could show the four functions were ever separated for one action. The account-recovery bot failed for the same reason, at population scale: nobody could show the company even knew how many agents like it were running, let alone who owned each one.

The director's company can answer the board's question now, and what changed is not a platform it bought. It is a register that is a table, certifications that are meetings with minutes, eight indicators compiled once a quarter instead of assembled in a panic, and a committee with real independence and real authority sitting somewhere other than inside the team whose budget it is meant to watch. Ask her today how many agents the company runs, who owns each one, and which are still paying for themselves, and the answer takes minutes, with evidence behind it, instead of a meeting to figure out who might know.

Four parts ago, she inherited an agent nobody had really designed and could not explain when it went wrong. She leaves this series running a small population of them, each with an owner, a certified tier, a revalidation date already on the calendar, and a committee that reads the exceptions rather than the highlight reel. That is the whole argument this series has been making since part 1, said once more in its shortest form: an agent nobody governs is not a shortcut. It is a debt with no due date, quietly accruing interest until the day something forces it due.

| Piece | What it delivers |
|---|---|
| Part 1 | Why the environment matters more than the model, the MEDIR cycle, the autonomy tiers and board-level risks |
| Part 2 | Guides and sensors, the skill format, three complete examples and the environment classes |
| Part 3 | The separation of powers, the rule of two, identity, injection, the record, and the legal ground in Brazil and Europe |
| Part 4, this one | The agent as a managed object: a life cycle, four roles, eight indicators and where the office that runs all of it should sit |
| Compact guide | Names, repositories, commands and step-by-step guides, organised by the five steps of MEDIR |

*Part 4 of 4 · Harness series · The 43 percent AI-inventory figure, cited in section 7, is widely attributed to Gartner; the originating report could not be located despite a direct search, and it is named there with that caveat rather than as a settled fact. The agent-dashboard description in section 7 is deliberately generic, drawn from patterns visible across today's tooling rather than from any single product, team or person. No Brazilian case appears among this part's incidents, the same limitation part 3 already carried. The character in the opening continues from parts 1 to 3 and is composed from recurring patterns.*
