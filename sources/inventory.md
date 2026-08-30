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
