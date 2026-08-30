# Inventário de fontes

Status em agosto de 2026. **Fonte não verificada não entra em documento assinado.**

Legenda: **V** verificada por leitura direta ou resultado de busca com URL confirmada. **P** parcial, existência confirmada mas conteúdo não lido. **N** não verificada, não citar com link.

---

## Fundação conceitual

| Status | Fonte | URL |
|---|---|---|
| V | Böckeler, *Harness engineering for coding agent users*, abr/2026 | https://martinfowler.com/articles/harness-engineering.html |
| V | Böckeler, *Maintainability sensors for coding agents*, mai/2026 | https://martinfowler.com/articles/sensors-for-coding-agents.html |
| V | Böckeler e Ford, *Harness engineering and agent feedback* | https://www.thoughtworks.com/en-us/insights/blog/generative-ai/harness-engineering-agent-feedback-exploring-ai-coding-sensors |
| V | Böckeler, *Understanding spec-driven development* | https://www.martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html |
| V | Böckeler, *Context engineering for coding agents* | https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html |
| V | OpenAI, *Harness engineering: leveraging Codex in an agent-first world*, fev/2026 | https://openai.com/index/harness-engineering/ |
| V | Hashimoto, *My AI Adoption Journey*, fev/2026 | https://mitchellh.com/writing/my-ai-adoption-journey |
| V | Anthropic, *Equipping agents for the real world with Agent Skills* | https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills |
| V | Anthropic, *Effective harnesses for long-running agents* | https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents |
| P | Anthropic, *Harness design for long-running application development* | https://anthropic.com/engineering/harness-design-long-running-apps |
| V | Bölük, *Only the harness changed*, fev/2026 | https://blog.can.ac/2026/02/12/the-harness-problem/ |
| V | Osmani, *Long-running agents*, abr/2026 | https://addyosmani.com/blog/long-running-agents/ |
| V | Agent Skills, padrão aberto | https://agentskills.io/ |
| V | Documentação de Agent Skills | https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview |

---

## Ferramentas e skills

| Status | Passo | Recurso | URL | Nota |
|---|---|---|---|---|
| V | Mapear | Guia inspirado em Karpathy | https://github.com/multica-ai/andrej-karpathy-skills | **Não é do Karpathy.** Mantido por terceiros, derivado de observações públicas dele. 208 mil estrelas. Comandos de instalação apontam para dono diferente do atual, conferir antes de instalar |
| V | Mapear | c4-skills, C4 e registro de decisão | https://github.com/muthub-ai/c4-skills | Agnóstica de ambiente. Separa o que da arquitetura do porquê |
| V | Mapear | enterprise-architecture-skill | https://github.com/gauravs19/enterprise-architecture-skill | Unifica quatro padrões. Para contexto de fusão, migração ou rastreabilidade regulatória |
| V | Mapear | Daves-Claude-Code-Skills | https://github.com/DavidROliverBA/Daves-Claude-Code-Skills | Diagramas com fundamento em pesquisa de legibilidade |
| V | Mapear | interview-me | https://github.com/Sorbh/interview-me | Entrevista de requisito técnico. Complementa a nossa skill de briefing, não substitui |
| V | Mapear | grill-me-skill | https://github.com/robmitt/grill-me-skill | Fura plano existente, não levanta |
| V | Equipar | superpowers | https://github.com/obra/superpowers | MIT. Padrão de regra inegociável mais bandeiras vermelhas |
| V | Equipar | mattpocock/skills | https://github.com/mattpocock/skills | Filosofia oposta ao superpowers: skills pequenas e editáveis |
| V | Equipar | planning-with-files | https://github.com/OthmanAdi/planning-with-files | Estado durável em disco. Cerca de 26 mil estrelas. **Ressalva:** o número de eficácia divulgado mede fidelidade ao padrão, não deriva de objetivo |
| V | Delegar | holdfast | https://github.com/AndreAlmeidaDC/holdfast | MIT. Execução particionada durável. **Novo:** três commits. Declara limites honestos, exercitado só em um ambiente. Sem dependência de rede, auditável rápido |
| V | Delegar | DeepSeek Harness | https://github.com/deepseek-ai/deepseek-harness | Runtime aberto, registro apenas-anexação |
| V | Inspecionar | sensors-cli | https://github.com/birgitta410/sensors-cli | Painel com histórico de disparos |
| V | Inspecionar | dependency-cruiser | https://github.com/sverweij/dependency-cruiser | Regras de dependência |
| V | Inspecionar | Stryker | https://stryker-mutator.io/ | Teste de mutação |
| V | Reforçar | ai-slop-cleaner | https://github.com/yeachan-heo/oh-my-claudecode | Fonte real da skill de limpeza. Fluxo à prova de regressão, com separação escritor e revisor |
| V | Referência | GitHub Spec Kit | mencionado em fonte verificada | Deu nome à categoria de especificação antes do código |
| V | Referência | autoresearch | https://github.com/karpathy/autoresearch | Fluxo agêntico de referência, este sim do Karpathy |
| V | Curadoria | awesome-harness-engineering | https://github.com/ai-boost/awesome-harness-engineering | |

---

## Não citar

Vitrines de skills sem repositório de origem visível, sem licença e sem manutenção verificável. Existem dezenas delas, especialmente para limpeza de código. O risco é duplo: conteúdo não auditável, e instalar skill de terceiro é executar instrução de terceiro dentro do próprio ambiente.

---

## Números usados nos artigos

Todos verificados. Ao citar, manter a ressalva quando houver.

| Número | Fonte |
|---|---|
| Formato novo superou o antigo em 14 de 16 modelos | Bölük |
| De 6,7% para 68,3% de taxa de sucesso no pior caso | Bölük |
| Custo do experimento: uma tarde e cerca de trezentos dólares | Bölük |
| Do trigésimo para o quinto lugar, ganho de 13,7 pontos | LangChain, via fonte secundária |
| Melhora em 14 de 15 configurações, média de 14,5% | Trabalho acadêmico sobre evolução automática de harness |
| Cinco meses, equipe de 3 a 7, zero linha escrita à mão, cerca de um milhão de linhas, cerca de 1.500 pull requests | OpenAI |
| Trinta e três mil estrelas em poucas horas | DeepSeek Harness |
