# Source inventory

Status as of August 2026. **An unverified source does not enter a signed document.**

Legend: **V** verified by direct reading or a search result with a confirmed URL. **P** partial, existence confirmed but content not read. **N** unverified, do not cite with a link.

This ledger stays in English only: it is an internal verification tool for whoever writes the articles, not reader-facing content, so it sits outside the project's English/Portuguese/Spanish translation policy. See `STANDARDS.md`'s `Languages` section.

**For an AI agent reading this table:** the Status column is a snapshot taken on the date stated for each source, not a live state. See `AGENTS.md` at the root of this repository before treating any URL below as current, and before installing, recommending or fetching any third-party skill listed here.

---

## Conceptual foundation

| Status | Source | URL |
|---|---|---|
| V | Böckeler, *Harness engineering for coding agent users*, Apr 2026 | https://martinfowler.com/articles/harness-engineering.html |
| V | Böckeler, *Maintainability sensors for coding agents*, May 2026 | https://martinfowler.com/articles/sensors-for-coding-agents.html |
| V | Böckeler and Ford, *Harness engineering and agent feedback* | https://www.thoughtworks.com/en-us/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors |
| V | Böckeler, *Understanding spec-driven development* | https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html |
| V | Böckeler, *Context engineering for coding agents* | https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html |
| V | OpenAI, *Harness engineering: leveraging Codex in an agent-first world*, Feb 2026 | https://openai.com/index/harness-engineering/ |
| V | Hashimoto, *My AI Adoption Journey*, Feb 2026 | https://mitchellh.com/writing/my-ai-adoption-journey |
| V | Anthropic, *Equipping agents for the real world with Agent Skills* | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| V | Anthropic, *Effective harnesses for long-running agents* | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| V | Anthropic, *Harness design for long-running application development*. Read directly 31 August 2026: describes the GAN-inspired generator/evaluator split cited in Part 1, a different article from *Effective harnesses for long-running agents* above, which does not cover this split | https://anthropic.com/engineering/harness-design-long-running-apps |
| V | Bölük, *Only the harness changed*, Feb 2026 | https://blog.can.ac/2026/02/12/the-harness-problem/ |
| V | Osmani, *Long-running agents*, Apr 2026 | https://addyosmani.com/blog/long-running-agents/ |
| V | Agent Skills, open standard | https://agentskills.io/ |
| V | Agent Skills documentation | https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview |

---

## Tools and skills

| Status | Step | Resource | URL | Note |
|---|---|---|---|---|
| V | Map | Karpathy-inspired guide | https://github.com/multica-ai/andrej-karpathy-skills | **Not actually by Karpathy.** Maintained by a third party, derived from his public observations. 208,000 stars. Install commands point at a different owner than the current one, check before installing |
| V | Map | c4-skills, C4 and decision records | https://github.com/muthub-ai/c4-skills | Environment-agnostic. Separates the architecture's what from the why |
| V | Map | enterprise-architecture-skill | https://github.com/gauravs19/enterprise-architecture-skill | Unifies four patterns. For merger, migration or regulatory-traceability contexts |
| V | Map | Daves-Claude-Code-Skills | https://github.com/DavidROliverBA/Daves-Claude-Code-Skills | Diagrams grounded in legibility research |
| V | Map | interview-me | https://github.com/Sorbh/interview-me | Technical-requirement interview. Complements this project's briefing skill, does not replace it |
| V | Map | grill-me-skill | https://github.com/robmitt/grill-me-skill | Pokes holes in an existing plan, does not gather requirements |
| V | Equip | superpowers | https://github.com/obra/superpowers | MIT. Non-negotiable-rule-plus-red-flags pattern |
| V | Equip | mattpocock/skills | https://github.com/mattpocock/skills | Philosophy opposite to superpowers: small, editable skills |
| V | Equip | planning-with-files | https://github.com/OthmanAdi/planning-with-files | Durable state on disk. About 26,000 stars. **Caveat:** the published effectiveness figure measures fidelity to the pattern, it is not derived from an objective |
| V | Delegate | holdfast | https://github.com/AndreAlmeidaDC/holdfast | MIT. Durable, partitioned execution. **New:** three commits. States honest limits, exercised in only one environment. No network dependency, quick to audit |
| V | Delegate | DeepSeek Harness | https://github.com/deepseek-ai/deepseek-harness | Open runtime, append-only log |
| V | Delegate | LangGraph | https://github.com/langchain-ai/langgraph | LangChain Inc. Low-level orchestration for stateful agents. Where a loop with a ceiling and an authority policy become code |
| V | Inspect | sensors-cli | https://github.com/birgitta410/sensors-cli | Dashboard with a firing history |
| V | Inspect | dependency-cruiser | https://github.com/sverweij/dependency-cruiser | Dependency rules |
| V | Inspect | Stryker | https://stryker-mutator.io/ | Mutation testing |
| V | Inspect | Semgrep | https://github.com/semgrep/semgrep | Semgrep, Inc. LGPL 2.1. Static analysis for security patterns, runs locally, code is not uploaded by default |
| V | Inspect | impeccable | https://github.com/pbakaus/impeccable | Apache 2.0. Derives from Anthropic's own frontend-design skill. 30 contributors, versioned (v4.1.2), 61 deterministic detector rules plus LLM-only critique. **Scoped install:** this project only copied `SKILL.md` and `reference/`, not the `scripts/` tree the detector rules need to run without an LLM, see `TOOLS.md` |
| V | Reinforce | ai-slop-cleaner | https://github.com/yeachan-heo/oh-my-claudecode | The real source of the cleanup skill cited in Part 2. Regression-safe flow, with a separate writer and reviewer |
| V | Map | GitHub Spec Kit | https://github.com/github/spec-kit | MIT. Named the spec-before-code category. Kiro, Tessl and OpenSpec cited via Böckeler's comparative review, with no directly verified link |
| V | Reference | autoresearch | https://github.com/karpathy/autoresearch | Reference agentic flow, this one actually by Karpathy |
| V | Curation | awesome-harness-engineering | https://github.com/ai-boost/awesome-harness-engineering | |

---

## Part 3 and 4 research: governance, security and law

Gathered 30 August 2026 for the working dossier `docs/harness-p3-p4-briefing.pt.md`. Status and notes preserved from that dossier's seven research axes plus the finding that reframed Part 3's opening. Two sources were marked **P** for a reason that mattered to the text, not just to the citation: the rule of two's original Meta publication and the Air Canada tribunal's original decision were never read at the primary source, only confirmed through secondary sources. **Both found and upgraded to V on 31 August 2026**, see the note on each row.

### Axis 1: the architecture of the problem

| Status | Source | URL | Note |
|---|---|---|---|
| V | Infosecurity Europe, OWASP researcher on prompt injection, Jul 2026 | https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/ | Allow lists sometimes helped an attacker, because the commands it needed were already approved. Sandbox output has redefined its own containment |
| V | Help Net Security, OWASP prompt injection coverage | https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/ | Names the rule of two, attributed to Meta |
| V | memx, the lethal trifecta | https://memx.app/blog/lethal-trifecta-ai-agent-data-exfiltration/ | Simon Willison's formulation: private data, untrusted content, external communication |
| V | Meta, *Agents Rule of Two: A Practical Approach to AI Agent Security*, 31 Oct 2025 | https://ai.meta.com/blog/practical-ai-agent-security/ | Found and read directly 31 August 2026, confirming the wording two independent secondary sources had already attributed to Meta. Linked in Part 3 and `harness-sources.html`, all three languages |
| V | OWASP Agentic Skills Top 10 project page | https://owasp.org/www-project-agentic-skills-top-10/ | Also lists the CVEs used in axis 2 |
| V | trydeepteam, OWASP Top 10 for agentic applications | https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications | ASI01, ASI02, ASI03 categories |
| P | OWASP Top 10 agentic framework, genai.owasp.org | not located | Referenced in an academic source, not read directly |

### Axis 2: documented incidents

| Status | Source | URL | Note |
|---|---|---|---|
| V | OWASP Agentic Skills Top 10 project page | https://owasp.org/www-project-agentic-skills-top-10/ | Lists CVE-2025-59536, CVE-2026-21852, CVE-2026-22708, CVE-2025-59532 with original disclosures |
| V | secops.group, securing agentic AI | https://secops.group/blog/securing-agentic-ai-the-owasp-top-10-and-beyond/ | Same CVE set, second reading |
| V | lasoft.org, who pays when the AI is wrong | https://lasoft.org/blog/who-pays-when-the-ai-is-wrong-rethinking-how-we-trust-ai/ | Secondary source for the SaaStr founder's account of a coding agent deleting a production database during a stated change freeze |

**Update, 31 August 2026: all five of the incidents below were located and linked** (see `harness-sources.html`). One correction found along the way: ClawHavoc was discovered and named by Koi Security on 1 Feb 2026, not by Antiy CERT — Antiy's report is a follow-on technical analysis, cited correctly for the 1,184 count but not for the discovery/naming. Also found: three of these five (ClawHavoc, Snyk's scan, SecurityScorecard's count) are three vendors reporting on the same underlying event — a Feb 2026 security crisis around one product, OpenClaw, and its skill marketplace, ClawHub — not five scattered, independent data points. Only postmark-mcp (Sept 2025, unrelated) and BlueRock's MCP-wide audit are genuinely separate.

| Status | Source | URL | Note |
|---|---|---|---|
| V | Koi Security, first malicious MCP in the wild, postmark-mcp | https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft | 25 Sep 2025. Fifteen clean npm versions, then one exfiltration line in v1.0.16. No primary source claims absolute "first ever," article now says "one of the first documented" |
| V | Snyk, malicious MCP server on npm, postmark-mcp | https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/ | Second reading of the same incident; explicitly does not claim original discovery ("by third-party analysis") |
| V | Antiy Labs, ClawHavoc campaign analysis | https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/ | 1,184 malicious skills against OpenClaw's ClawHub marketplace, 12 publisher accounts, one with 677 packages. Discovered/named by Koi Security, 1 Feb 2026; this is the follow-on technical read, not the discovery |
| V | Snyk, 280+ leaky skills, OpenClaw and ClawHub | https://snyk.io/blog/openclaw-skills-credential-leaks-research/ | 5 Feb 2026. 283 of 3,984 ClawHub skills leaking API keys, passwords, PII, credit-card numbers |
| V | BlueRock, MCP fURI, SSRF in Microsoft MarkItDown MCP, Jan 2026 | https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities | Vendor research (BlueRock sells MCP security products), not an independent audit. 7,000+ MCP servers scanned, 36.7% potentially SSRF-vulnerable; PoC recovered a real AWS access key via EC2 metadata. Resolved 31 Aug 2026: this is a dated snapshot of a continuous measurement, not a contradicted figure — BlueRock's public registry (mcp-trust.com, also mirrored at bluerock.io/products/mcp-trust-registry; the earlier `bluerock.io/mcp-trust-registry` URL was simply the wrong path, not a removed page) confirmed open and current the same day, showing 12,000+/33%, the same instrument with a larger sample |
| V | The Register, 135,000+ OpenClaw instances exposed | https://www.theregister.com/2026/02/09/openclaw_instances_exposed_vibe_code/ | 9 Feb 2026, attributed to SecurityScorecard STRIKE. These are OpenClaw instances specifically (default bind to all network interfaces), not MCP servers generically |

**Do not cite:** `owasp.org/www-project-agentic-skills-top-10/case-studies` was checked as a possible corroborating source for ClawHavoc and found to contradict the primary sources on basic facts (wrong discoverer, wrong month, SHA256 hashes that look like placeholder hex strings, unsourced dollar-loss figures). Treat as unreliable, added to "Do not cite" below.

### Axis 3: Brazil, ANPD and LGPD

| Status | Source | URL | Note |
|---|---|---|---|
| V | Confidata, AI, LGPD and privacy | https://confidata.com.br/blog/ia-lgpd-inteligencia-artificial-privacidade | LGPD article 20, the right to review automated decisions |
| V | Gutemberg Amorim, LGPD, AI and automated decisions | https://gutembergamorim.com.br/lgpd-ia-decisoes-automatizadas-e-discriminacao-algoritmica-o-direito-de-revisao-no-art-20-da-lgpd/ | Reading of article 20's two cumulative requirements |
| V | Farracha de Castro, automated decisions and AI, ANPD's regulatory perspective | https://farrachadecastro.com.br/farracha-de-castro/decisoes-automatizadas-e-inteligencia-artificial-perspectivas-regulatorias-segundo-a-anpd/ | Confirms ANPD's 2025-2026 regulatory agenda and Technical Note 12/2025. **Reverified 31 Aug 2026: the "2026-2027 priority map" detail does not appear in the article**, corrected in the text |
| V | Barbieri Advogados, AI regulation in Brazil | https://www.barbieriadvogados.com/regulamentacao-inteligencia-artificial-brasil/ | **Reverified 31 Aug 2026: the article covers PL 2.338/2023's status and a December 2025 bill creating the SIA system, not** ANPD's move to independent regulatory agency status in September 2025, which this project had attributed to it. Body text now attributes that claim to general industry reporting instead |

Article 20's specific-regulation status must be dated in Part 3's text: as of this research round, it had not been published, and that sentence can age within months.

### Axis 4: European regulation

| Status | Source | URL | Note |
|---|---|---|---|
| V | Cloud Security Alliance, EU AI Act high-risk compliance deadline | https://labs.cloudsecurityalliance.org/research/csa-research-note-eu-ai-act-high-risk-compliance-deadline-20/ | 2 August 2026 binding date, and the unpassed November 2025 Commission proposal to delay it |
| V | Augment Code, EU AI Act 2026 guide | https://www.augmentcode.com/guides/eu-ai-act-2026 | Second reading of the same deadline |
| V | artificialintelligenceact.eu, Article 26 | https://artificialintelligenceact.eu/article/26/ | Deployer obligations, six-month record retention, fifteen-day incident reporting |
| V | artificialintelligenceact.eu, Article 14 | https://artificialintelligenceact.eu/article/14/ | Human oversight, including the automation-bias clause |
| V | EU AI Act Service Desk, Article 26 | https://ai-act-service-desk.ec.europa.eu/en/ai-act/article-26 | Official EU reading of the same article |

### Axis 5: audit and logging standards

| Status | Source | URL | Note |
|---|---|---|---|
| V | balancedsec, NIST AI RMF or ISO 42001 | https://blog.balancedsec.com/p/nist-ai-rmf-or-iso-42001 | NIST AI RMF is self-declared, ISO/IEC 42001 is certifiable via its Statement of Applicability |
| V | Lumenova, agentic AI risks against OWASP and NIST | https://www.lumenova.ai/blog/agentic-ai-risks-owasp-nist/ | NIST's AI Agent Standards Initiative, announced 17 Feb 2026, four gaps in existing frameworks |
| V | arXiv 2607.02201, agentic risk taxonomy | https://arxiv.org/pdf/2607.02201 | Comparative survey of governance frameworks against the agentic stack |
| V | AIUC-1 | https://www.aiuc-1.com/ | Positioned as a SOC 2 equivalent for AI agents. Referenced in an academic source, not read directly in the first research round; site found and opened directly 31 August 2026, confirming the positioning |
| V | OpenTelemetry, generative AI observability | https://opentelemetry.io/blog/2026/genai-observability/ | Open, vendor-neutral semantic conventions for agent telemetry |
| V | Digital Applied, AI agent observability stack guide | https://www.digitalapplied.com/blog/ai-agent-observability-2026-tracing-monitoring-stack-guide | **Reverified 31 Aug 2026: the article describes OpenTelemetry-convention adoption as still emerging, not "already exported by most/major runtimes"** as this project's text overstated; corrected to "growing adoption" |

### Axis 6: authority and approval

| Status | Source | URL | Note |
|---|---|---|---|
| V | Built In, enterprise identity and access management | https://builtin.com/articles/enterprise-identity-access-management | Copilot, human-initiated and unattended trigger classification, mapped to N0 to N3 |
| V | NeuralCoreTech, AI agent identity governance 2026 | https://neuralcoretech.com/ai-agent-identity-governance-2026/ | On-behalf-of versus autonomous delegation patterns |
| V | The AI Economy, ServiceNow AI Control Tower | https://theaieconomy.substack.com/p/servicenow-ai-control-tower-knowledge-2026-enforcement | Governance platforms that can now discover, monitor and shut down agents in third-party clouds |

### Axis 7: non-human identity

| Status | Source | URL | Note |
|---|---|---|---|
| V | miniOrange, IAM trends for AI agents 2026 | https://www.miniorange.com/blog/iam-trends-ai-agents-2026/ | The Tuesday-afternoon identity that outlives the developer who created it |
| V | Built In, enterprise identity and access management | https://builtin.com/articles/enterprise-identity-access-management | Same source as axis 6, reused for the three-question identity checklist |
| V | NeuralCoreTech, AI agent identity governance 2026 | https://neuralcoretech.com/ai-agent-identity-governance-2026/ | Same source as axis 6, reused for long-lived embedded API keys as the most common root cause |
| V | arXiv 2501.09674, *Authenticated Delegation and Authorized AI Agents* | https://arxiv.org/abs/2501.09674 | Referenced in an academic source, not read directly in the first research round; paper found and opened directly 31 August 2026 |

### The Air Canada case and adjacent cases

| Status | Source | URL | Note |
|---|---|---|---|
| V | CanLII commentary, 2025CanLIIDocs1963 | https://www.canlii.org/en/commentary/doc/2025CanLIIDocs1963 | Analysis of Moffatt v Air Canada, 2024 BCCRT 149 |
| V | American Bar Association, BC tribunal confirms companies remain liable | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ | Air Canada argued the chatbot was a separate legal entity, and lost |
| V | McCarthy, Moffatt v Air Canada, misrepresentation by AI chatbot | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot/ | Third independent reading of the same decision |
| V | CanLII, original decision, *Moffatt v Air Canada*, 2024 BCCRT 149 | https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html | Address cited in secondary sources in the first research round, not opened directly; found and opened directly 31 August 2026. **This precedent is Canadian, not Brazilian.** No Brazilian case involving an agent with an external effect was found in this round, only announced enforcement priority and declared regulatory attention, see axis 3. Part 3 states the precedent's origin explicitly |
| V | Xoomar, chatbot liability, the Air Canada case | https://xoomar.com/technology/chatbot-liability-air-canada | Secondary source consolidating the Cursor April 2025 phantom-policy incident and the May 2025 AI-hallucination insurance product |

---

## Part 4 research: life cycle, roles, indicators, and where the office sits

Gathered 30 August 2026 for `docs/research-part4.pt.md`, answering the block A scope from the working dossier that had fixed the thesis, roles, indicators and closing argument with no source at all. A follow-up round the same day verified two load-bearing claims against a primary source (the SCHUFA holding, the Kyndryl figures) and attempted, without success, to verify a third (the Gartner 43% figure), see its note below.

### Axis 1: the agent life cycle

| Status | Source | URL | Note |
|---|---|---|---|
| N | CloudEagle, why every team is quietly building non-human identity debt | https://www.cloudeagle.ai/blogs/why-every-team-is-quietly-building-up-non-human-identity-debt | **Correction, 31 Aug 2026: this row was wrong.** This page never contained the 824,000/8%/17:1 figures — confirmed by direct reading and by the Wayback Machine, which has zero archived snapshots for this URL at any date. The 30 Aug "V" rating was almost certainly a mix-up with the real Veza report below, which was fresh news at the time. Downgraded to **N**; kept only for the record of the error, not as a source |
| V | Veza, 2026 State of Identity & Access Report, press release | https://veza.com/company/press-room/veza-identity-access-research-report-reveals-identity-permissions-sprawl-has-reached-critical-levels-amid-explosion-of-machine-and-ai-agent-identities-across-the-enterprise/ | The real source, found 31 Aug 2026. Primary, read directly: 824,000 orphaned accounts (8% of all accounts) with no HR-system owner but live entitlements; machine identities outnumber human users 17:1 (up from ~16:1 in 2024). Full PDF: https://veza.com/wp-content/uploads/2025/12/SOIA-2026-Veza.pdf. Methodology: 230bn+ permissions across 160 companies |
| V | Help Net Security, non-human identities push identity security into uncharted territory | https://www.helpnetsecurity.com/2025/12/30/identity-security-permissions-sprawl/ | 30 Dec 2025. Second reading of the Veza report, correctly attributed: orphaned identities up ~40% year over year, dormant accounts nearly doubled |
| V | nhimg.org, IGA solutions in 2026 expose the limits of legacy access reviews | https://nhimg.org/articles/iga-solutions-in-2026-expose-the-limits-of-legacy-access-reviews/ | Quarterly certification finds stale access after the fact, not before it becomes risk; recertification should trend event-driven, not just calendar-driven |
| V | Waldo Security, best IGA solutions in 2026 | https://www.waldosecurity.com/post/best-identity-governance-administration-iga-solutions-in-2026 | Second reading of the same point |
| V | Obsidian Security, service account security best practices | https://www.obsidiansecurity.com/blog/service-account-security-best-practices | How an orphaned account is born: a pilot's microservice is retired, its service account keeps running in production with administrative database rights |
| V | SC World, non-human identities are outgrowing your governance model | https://www.scworld.com/risk-advisory/non-human-identities-are-outgrowing-your-governance-model | Second reading of the same accumulation mechanism |
| V | The Hacker News, the hidden risk of orphan accounts | https://thehackernews.com/2026/01/the-hidden-risk-of-orphan-accounts.html | Coins "identity dark matter", accounts invisible to governance but active in infrastructure; states agentic AI processes fall natively into this category |

### Axis 2: the four roles and the non-accumulation rule

| Status | Source | URL | Note |
|---|---|---|---|
| V | NC State ERM, COSO's take on the three lines of defense | https://erm.ncsu.edu/library/article/cosos-take-on-the-three-lines-of-defense | The Three Lines Model (Institute of Internal Auditors, formalised 2013, revised 2020 and 2023) maps onto the four roles almost exactly: first line operates, second line assists and challenges, third line is independent assurance reporting to the governing body |
| V | Deloitte, modernising the three lines of defence model | https://www.deloitte.com/mt/en/services/consulting-risk/perspectives/modernising-the-three-lines-of-defence-model.html | Second reading of the same model |
| V | Pathlock, the COSO framework | https://pathlock.com/blog/internal-controls/coso-framework/ | Segregation of duties defined as keeping authorising and recording as separate functions; the authority matrix's stated purpose is preventing unauthorised action, matching Part 3's matrix of authority almost word for word |
| V | arXiv 2305.17038, frontier AI developers need an internal audit function | https://arxiv.org/pdf/2305.17038 | Academic application of the Three Lines Model to frontier AI risk |
| V | arXiv 2212.08364, three lines of defense against risks from AI | https://arxiv.org/pdf/2212.08364 | Second academic application of the same model |
| V | Echelon Cyber, the AI governance gap no one's talking about | https://echeloncyber.com/intelligence/entry/the-ai-governance-gap-no-ones-talking-about-why-your-ciso-cant-own-this-alone | Splunk 2026 survey, 650 security leaders: only 6% of organisations running agents updated their governance frameworks to match what those agents actually do. No AI governance framework (NIST AI RMF, ISO 42001, AIUC-1, NIST's agent standards initiative) names roles equivalent to the four proposed here, treated in the text as a positioning point, not a gap |

### Axis 3: the eight indicators

| Status | Source | URL | Note |
|---|---|---|---|
| P | Airia, shadow AI statistics every CISO needs in 2026 | https://airia.com/blog/shadow-ai-statistics-key-data-points-every-ciso-needs-in-2026/ | Aggregator citing Gartner (43% of organisations cannot produce an AI inventory) and Microsoft (78% of workplace AI users bring their own tools). The 43% figure's primary Gartner report was searched for directly, including on gartner.com, and not found. Stays **P**; attribute in the article to "widely cited Gartner research", not to Gartner directly |
| V | OSHA Community, Heinrich's safety triangle | https://oshacommunity.com/osha/heinrichs-safety-triangle/ | Replaces a patent-document citation from the first research round. Heinrich's 1931 accident triangle, 300 near misses to 29 minor injuries to 1 major injury. Modern literature questions the fixed ratio but not the underlying logic, that a loss event is almost always preceded by a warning |
| V | Legiscope, GDPR Article 22 automated decision-making | https://www.legiscope.com/blog/gdpr-article-22-automated-decision-making.html | The SCHUFA holding itself, CJEU, Dec 2023, case C-634/21: "solely automated" does not require zero human involvement; a human who formally signs off but in practice defers entirely to the algorithm still leaves the decision "solely automated" |
| V | Masaryk University Journal of Law and Technology, doctrinal analysis of SCHUFA | https://journals.muni.cz/mujlt/article/view/41367 | Formulation tied directly to SCHUFA's own reasoning, cross-read with Uber, Deliveroo and CaixaBank case law: nominal human review fails Article 22 when it amounts to rubber-stamping without interpretive criteria or authority to deviate |
| V | GDPR Local, automated decision-making under GDPR | https://gdprlocal.com/automated-decision-making-gdpr/ | General EDPB guidance on meaningful human review, four criteria, not specific to SCHUFA. Cite separately from the SCHUFA holding above, never as if one source made both points |
| V | CJEU, case C-634/21 (SCHUFA), official press release | https://curia.europa.eu/jcms/upload/docs/application/pdf/2023-12/cp230186en.pdf | Referenced in the two sources above in the first research round, not read directly; the court's own official press release found and opened directly 31 August 2026 |
| V | MIT, *The GenAI Divide*, 2025, via Legal.io | https://www.legal.io/blog/5719519/MIT-Report-Finds-95-of-AI-Pilots-Fail-to-Deliver-ROI-Exposing-GenAI-Divide | 95% of generative AI pilots show no measurable P&L impact |
| V | Kyndryl, 2026 People Readiness Report, via PR Newswire | https://www.prnewswire.com/news-releases/kyndryl-report-ai-adoption-accelerates-as-workforce-readiness-becomes-the-roi-difference-maker-302810837.html | Primary source, verified this round, 1,100 leaders across eight countries. 57% say AI is embedded in core processes or deployed broadly; of those, 32% achieved at least one of their top two AI goals and only 11% achieved both, two different cuts of the data, not one number |
| V | Deloitte, Agentic AI strategy, Tech Trends 2026 | https://www.deloitte.com/us/en/insights/topics/technology-management/tech-trends/2026/agentic-ai-strategy.html | Found 31 Aug 2026, replacing an unsourced "89% of pilots never reach production" that had circulated without a locatable Deloitte original. Deloitte's real, quotable pipeline: 30% exploring, 38% piloting, 14% ready to deploy, only 11% actively in production. The circulating "89%" is the arithmetic complement of 11% (100−11), invented by aggregator sites, not a Deloitte figure; even a generous 11-of-38 reading gives ~71%, not 89% |
| V | Terminal X, AI ROI in 2026, why most enterprise AI fails | https://www.terminal-x.ai/research/ai-roi-in-2026-why-most-enterprise-ai-fails-and-what-actually-works | Additional ROI-gap figures (S&P Global, IBM, Morgan Stanley); aggregator, individual numbers **P** |
| V | Beri.net, AI agent adoption in the enterprise, Gartner and IDC | https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc | Second aggregator, same caveat |
| V | Microsoft Tech Community, AfterLogin, forgotten account cleanup | https://techcommunity.microsoft.com/blog/educatordeveloperblog/afterlogin-we-turned-forgotten-account-cleanup-into-a-haunted-house-game-with-mi/4539781 | The nuance that keeps "no execution in the period" from becoming an auto-delete trigger: finding a stale account is easy, judging whether it is truly dead or something still depends on it silently is the hard part |
| V | N-iX, FinOps for AI | https://www.n-ix.com/finops-for-ai/ | FinOps Foundation's 2026 framework treats AI as its own technology category; for agentic workloads, cost per completed task is the recommended unit |
| V | Compresr, AI FinOps definitive guide | https://compresr.ai/blog/ai-finops-definitive-guide-costs-and-value | Second reading of cost-per-task as the agentic unit-economics measure |
| V | We The Flywheel, AI FinOps and GPU cost management 2026 | https://wetheflywheel.com/en/guides/ai-finops-gpu-cost-management-2026/ | State of FinOps 2026 survey, 1,192 respondents managing over $83bn in cloud spend: 98% of FinOps practitioners now manage AI spend, up from 63% a year earlier. Agentic flows fire 10 to 20 model calls per user task; plan by tasks times steps times tokens, not list price |

No external source proposes these eight indicators as a set. Five have solid external grounding (coverage, expired certification, gate rejection rate, realised return, cost per mission), two rest on analogy from another discipline (exception rate via near-miss theory, no-execution via dormant-account theory), and one is internal to the series (tier against environment). Part 4's text must say this explicitly, the same honesty move Part 3 made for the rule of two.

### Axis 4: where the office sits

| Status | Source | URL | Note |
|---|---|---|---|
| V | CSO Online, it's time to rethink CISO reporting lines | https://www.csoonline.com/article/4136293/its-time-to-rethink-ciso-reporting-lines.html | IANS Research and Artico Search 2026 benchmark: 64% of CISOs report into IT (CIO or CTO), 11% to the CEO, 5% each to the CFO, chief risk officer, legal and other business roles. Quotes a security consultant and former federal prosecutor: asking the CISO to report to the person whose bonus depends on cutting the number of sprinklers is asking the fire inspector to do the same |
| V | CSO Online, the endless CISO reporting line debate | https://www.csoonline.com/article/4158505/the-endless-ciso-reporting-line-debate-and-what-it-says-about-cybersecurity-leadership.html | The honest counterpoint: framing the relationship as a structural budget conflict is outdated, alignment is the goal, the reporting line is a means, not an end |
| V | VantEdge Search, CISO elevation in 2026 | https://www.vantedgesearch.com/resources/blogs/ciso-elevation-in-2026-why-cybersecurity-leadership-is-moving-to-the-c-suite-and-board-tables/ | Emerging position for 2026: direct reporting to the CEO or the board's risk committee, specifically to secure independence from the functions being overseen |
| V | Echelon Cyber, the AI governance gap no one's talking about | https://echeloncyber.com/intelligence/entry/the-ai-governance-gap-no-ones-talking-about-why-your-ciso-cant-own-this-alone | Same Splunk 650-leader survey as axis 2: 79% say their role expanded past its mandate and resources, 71% say AI touches core business systems, only 16% govern that access well. "The person who holds the title doesn't hold the authority, and the people who hold the authority don't answer for the outcomes." Recommends a distributed operating model over a single owner, even in risk |
| V | Build MVP Fast, AI FinOps function, token budget, org chart 2026 | https://www.buildmvpfast.com/blog/ai-finops-function-token-budget-org-chart-2026 | Adjacent parallel for the cost section: 78% of FinOps teams report to the CTO or CIO, only 8% to the CFO, the same pattern of a control function sitting inside the executor |

### Axis 5: vocabulary calibration

No new sources needed. Reuses the "kill switch" sources already verified in the Part 3 block above (control tower, end-to-end governance, autonomous-workforce vocabulary). Deliberate word to avoid in the article: "platform." A product is bought, a function is organised, and only the second survives the vendor being replaced.

### Axis 6: narrative cases

| Status | Source | URL | Note |
|---|---|---|---|
| V | Cloud Security Alliance, Meta AI support bot account takeover 2026 | https://labs.cloudsecurityalliance.org/research/csa-research-note-meta-ai-support-bot-account-takeover-20260/ | Verified in full against the primary source. Between 17 April and 31 May 2026, attackers took over 20,225 Instagram accounts, including the Obama White House account, a US Space Force Chief Master Sergeant's profile and Sephora's brand account, by exploiting Meta's High Touch Support chatbot: it could both link a new email to an existing account and trigger a password-reset message to that email in the same interaction, without verifying the requester owned the account. Breach notification filed with the Maine Attorney General 5 June 2026. Meta disabled the bot's autonomous capability 31 May 2026, routing sensitive changes to human review |
| V | The Hacker News, the hidden risk of orphan accounts | https://thehackernews.com/2026/01/the-hidden-risk-of-orphan-accounts.html | Reused from axis 1. Colonial Pipeline 2021, an old inactive VPN account with no two-factor authentication, as a decommissioning-adjacent case |
| V | The Hacker News, dormant GitHub accounts help attackers | https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html | Over fifty accounts created two to five years earlier, deliberately kept dormant before being used to enumerate organisations and clone private repositories: dormancy as attacker strategy, not neglect |
| V | Barracuda Networks, SOC case files: Akira ransomware exploiting a 'ghost' account | https://blog.barracuda.com/2025/02/05/soc-case-files-akira-ransomware-ghost-account | Found 31 Aug 2026, closing a previously uncited middle case (between Colonial Pipeline and the GitHub case above). Primary source, Barracuda's own MDR team: a manufacturing company breached via a third-party vendor account never deactivated when the vendor left; Akira ransomware; detected and isolated in about four minutes. Origin of the "ghost account" term retold by The Hacker News above, which already covered this exact case |

Same limitation as Part 3: no Brazilian case was found. Every narrative case above is foreign, and Part 4's text must say so.

---

## Do not cite

Skill showcases with no visible origin repository, no licence and no verifiable maintenance. Dozens of these exist, especially for code cleanup. The risk is twofold: unauditable content, and installing a third-party skill means executing a third party's instructions inside your own environment.

`owasp.org/www-project-agentic-skills-top-10/case-studies` — checked 31 Aug 2026 as a possible corroborating source for the ClawHavoc campaign. Contradicts the primary sources on basic facts: attributes discovery to Snyk instead of Koi Security, uses a January instead of February timeline, and lists SHA256 hashes that read as placeholder hex strings (e.g. `a1b2c3d4e5f6789012...`) plus unsourced dollar-loss figures. Do not cite.

---

## Numbers used in the articles

All verified. When citing, keep the caveat where one exists.

| Number | Source |
|---|---|
| The new format beat the old one in 14 of 16 models | Bölük |
| From 6.7% to 68.3% worst-case success rate | Bölük |
| Experiment cost: one afternoon and about three hundred dollars | Bölük |
| From thirtieth to fifth place, a 13.7-point gain (Terminal Bench 2.0, 52.8 to 66.5, model held fixed) | LangChain's own blog, Vivek Trivedy, 17 Feb 2026: https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering. Found 31 Aug 2026, replacing the earlier "via a secondary source" note |
| Improvement in 14 of 15 configurations, +14.5% average absolute gain (up to +44.0%) | arXiv 2606.14249, HarnessX/AEGIS (Darwin Agent Team), 12 Jun 2026: https://arxiv.org/abs/2606.14249. Found 31 Aug 2026, replacing the earlier unlinked "academic work" note |
| Five months, a team of 3 to 7, zero hand-written lines, about one million lines, about 1,500 pull requests | OpenAI |
| Thirty-three thousand stars in a few hours | DeepSeek Harness |
