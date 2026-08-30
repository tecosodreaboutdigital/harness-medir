# Source inventory

Status as of August 2026. **An unverified source does not enter a signed document.**

Legend: **V** verified by direct reading or a search result with a confirmed URL. **P** partial, existence confirmed but content not read. **N** unverified, do not cite with a link.

This ledger stays in English only: it is an internal verification tool for whoever writes the articles, not reader-facing content, so it sits outside the project's English/Portuguese/Spanish translation policy. See `STANDARDS.md`'s `Languages` section.

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
| P | Anthropic, *Harness design for long-running application development* | https://anthropic.com/engineering/harness-design-long-running-apps |
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

Gathered 30 August 2026 for the working dossier `docs/harness-p3-p4-briefing.pt.md`. Status and notes preserved from that dossier's seven research axes plus the finding that reframed Part 3's opening. Two sources are marked **P** for a reason that matters to the text, not just to the citation: the rule of two's original Meta publication and the Air Canada tribunal's original decision were never read at the primary source, only confirmed through secondary sources, see the note on each row.

### Axis 1: the architecture of the problem

| Status | Source | URL | Note |
|---|---|---|---|
| V | Infosecurity Europe, OWASP researcher on prompt injection, Jul 2026 | https://www.infosecurity-magazine.com/news/infosec-europe-prompt-injection/ | Allow lists sometimes helped an attacker, because the commands it needed were already approved. Sandbox output has redefined its own containment |
| V | Help Net Security, OWASP prompt injection coverage | https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/ | Names the rule of two, attributed to Meta |
| V | memx, the lethal trifecta | https://memx.app/blog/lethal-trifecta-ai-agent-data-exfiltration/ | Simon Willison's formulation: private data, untrusted content, external communication |
| P | Meta, original publication of the rule of two | not located | Two independent secondary sources attribute it to Meta with the same wording, sufficient to cite the content, not to link it. Locate before Part 3 is signed off, see `docs/harness-p3-p4-briefing.pt.md` |
| V | OWASP Agentic Skills Top 10 project page | https://owasp.org/www-project-agentic-skills-top-10/ | Also lists the CVEs used in axis 2 |
| V | trydeepteam, OWASP Top 10 for agentic applications | https://www.trydeepteam.com/docs/frameworks-owasp-top-10-for-agentic-applications | ASI01, ASI02, ASI03 categories |
| P | OWASP Top 10 agentic framework, genai.owasp.org | not located | Referenced in an academic source, not read directly |

### Axis 2: documented incidents

| Status | Source | URL | Note |
|---|---|---|---|
| V | OWASP Agentic Skills Top 10 project page | https://owasp.org/www-project-agentic-skills-top-10/ | Lists CVE-2025-59536, CVE-2026-21852, CVE-2026-22708, CVE-2025-59532 with original disclosures |
| V | secops.group, securing agentic AI | https://secops.group/blog/securing-agentic-ai-the-owasp-top-10-and-beyond/ | Same CVE set, second reading |
| V | lasoft.org, who pays when the AI is wrong | https://lasoft.org/blog/who-pays-when-the-ai-is-wrong-rethinking-how-we-trust-ai/ | Secondary source for the SaaStr founder's account of a coding agent deleting a production database during a stated change freeze |

Named incidents without their own link, cited by name only: postmark-mcp (first malicious MCP server caught in real use, fifteen clean versions before one exfiltration line), ClawHavoc (Antiy CERT, Feb 2026, 1,184 malicious skills), Snyk's February 2026 scan (280+ skills leaking API keys and personal data), BlueRock's audit of 7,000+ MCP servers (36.7% potentially vulnerable to server-side request forgery), SecurityScorecard's February 2026 count (135,000+ publicly exposed instances with insecure default configuration).

### Axis 3: Brazil, ANPD and LGPD

| Status | Source | URL | Note |
|---|---|---|---|
| V | Confidata, AI, LGPD and privacy | https://confidata.com.br/blog/ia-lgpd-inteligencia-artificial-privacidade | LGPD article 20, the right to review automated decisions |
| V | Gutemberg Amorim, LGPD, AI and automated decisions | https://gutembergamorim.com.br/lgpd-ia-decisoes-automatizadas-e-discriminacao-algoritmica-o-direito-de-revisao-no-art-20-da-lgpd/ | Reading of article 20's two cumulative requirements |
| V | Farracha de Castro, automated decisions and AI, ANPD's regulatory perspective | https://farrachadecastro.com.br/farracha-de-castro/decisoes-automatizadas-e-inteligencia-artificial-perspectivas-regulatorias-segundo-a-anpd/ | ANPD's 2025-2026 regulatory agenda, Technical Note 12/2025, the 2026-2027 priority map |
| V | Barbieri Advogados, AI regulation in Brazil | https://www.barbieriadvogados.com/regulamentacao-inteligencia-artificial-brasil/ | ANPD's move to independent regulatory agency status, September 2025 |

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
| P | AIUC-1 | https://www.aiuc-1.com/ | Positioned as a SOC 2 equivalent for AI agents. Referenced in an academic source, not read directly |
| V | OpenTelemetry, generative AI observability | https://opentelemetry.io/blog/2026/genai-observability/ | Open, vendor-neutral semantic conventions for agent telemetry |
| V | Digital Applied, AI agent observability stack guide | https://www.digitalapplied.com/blog/ai-agent-observability-2026-tracing-monitoring-stack-guide | Major agent runtimes already export in the OpenTelemetry convention |

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
| P | arXiv 2501.09674, authenticated delegation and agent authorisation | https://arxiv.org/abs/2501.09674 | Referenced in an academic source, not read directly |

### The Air Canada case and adjacent cases

| Status | Source | URL | Note |
|---|---|---|---|
| V | CanLII commentary, 2025CanLIIDocs1963 | https://www.canlii.org/en/commentary/doc/2025CanLIIDocs1963 | Analysis of Moffatt v Air Canada, 2024 BCCRT 149 |
| V | American Bar Association, BC tribunal confirms companies remain liable | https://www.americanbar.org/groups/business_law/resources/business-law-today/2024-february/bc-tribunal-confirms-companies-remain-liable-information-provided-ai-chatbot/ | Air Canada argued the chatbot was a separate legal entity, and lost |
| V | McCarthy, Moffatt v Air Canada, misrepresentation by AI chatbot | https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot/ | Third independent reading of the same decision |
| P | CanLII, original decision, 2024 BCCRT 149 | https://canlii.ca/t/k2spq | Address cited in secondary sources, not opened directly. **This precedent is Canadian, not Brazilian.** No Brazilian case involving an agent with an external effect was found in this round, only announced enforcement priority and declared regulatory attention, see axis 3. Part 3 must state the precedent's origin explicitly |
| V | Xoomar, chatbot liability, the Air Canada case | https://xoomar.com/technology/chatbot-liability-air-canada | Secondary source consolidating the Cursor April 2025 phantom-policy incident and the May 2025 AI-hallucination insurance product |

---

## Do not cite

Skill showcases with no visible origin repository, no licence and no verifiable maintenance. Dozens of these exist, especially for code cleanup. The risk is twofold: unauditable content, and installing a third-party skill means executing a third party's instructions inside your own environment.

---

## Numbers used in the articles

All verified. When citing, keep the caveat where one exists.

| Number | Source |
|---|---|
| The new format beat the old one in 14 of 16 models | Bölük |
| From 6.7% to 68.3% worst-case success rate | Bölük |
| Experiment cost: one afternoon and about three hundred dollars | Bölük |
| From thirtieth to fifth place, a 13.7-point gain | LangChain, via a secondary source |
| Improvement in 14 of 15 configurations, 14.5% average | Academic work on automatic harness evolution |
| Five months, a team of 3 to 7, zero hand-written lines, about one million lines, about 1,500 pull requests | OpenAI |
| Thirty-three thousand stars in a few hours | DeepSeek Harness |
