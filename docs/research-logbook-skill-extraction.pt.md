# Pesquisa: fork ou construção própria para a skill de diário de bordo

Dossiê de trabalho interno, não é conteúdo publicado da série harness-medir. Levantado em 13 de setembro de 2026.

**Pergunta.** O item 5 de `NEXT-STEPS.pt.md` propõe extrair o motor de métrica de `docs/logbook.html` / `build/generate_logbook_metrics.py` para uma skill própria, instalável, em repositório público separado — seguindo o precedente do `intake-briefing`. A ideia evoluiu: em vez de só contar palavras/linhas/tokens, o resultado devia virar um painel HTML de marco de projeto com conversão de token para custo, preço configurável tanto no código-fonte quanto na interface já publicada (o usuário digita o preço, em qualquer moeda, e o painel recalcula ao vivo, sem backend). Esta pesquisa decide se esse painel deveria nascer como fork de um repositório GitHub maduro, como combinação de peças de dois ou três repositórios, ou construído do zero.

**Como foi feito.** Cinco agentes de pesquisa em paralelo, um por eixo, cada um rodando buscas reais (`gh search repos`, `gh api search/repositories`, `gh api repos/<org>/<repo>`) e lendo README/código-fonte real via `gh api contents` ou `WebFetch` de `raw.githubusercontent.com`, nunca por memória de treinamento. Todos os números de estrela e data de último commit abaixo foram capturados ao vivo em 13 de setembro de 2026 e mudam com o tempo.

**Legenda.** Cada linha de tabela carrega a fonte da verificação (comando `gh` ou URL) nas notas abaixo dela. Quando um repo teve leitura de README/código-fonte real (não só metadados), isso está dito explicitamente.

---

## Sumário

| Eixo | Achado central |
|---|---|
| 1. Governança de agente de IA | Um candidato relevante para o *conceito* (AgDR), zero como base de código do painel |
| 2. Contadores de LOC / atividade | `scc` chega mais perto de todos, mas erra exatamente no ponto central (custo real vs. hipotético, preço não é editável na UI publicada) |
| 3. Rastreadores de custo de token | Nenhum candidato cobre as três exigências ao mesmo tempo; a combinação é confirmada como o ponto realmente novo do projeto |
| 4. Geradores de changelog/diário | O espaço de changelog generators inteiro não tem métrica quantitativa de esforço; um achado periférico de 0 estrelas chega mais perto que qualquer ferramenta madura |
| 5. Comparadores de preço entre provedores | O mecanismo exato (preço editável, recálculo ao vivo, estático) existe e está maduro em `simonw/llm-prices`, mas é mecanismo trivial, não motivo de fork |

**Recomendação de fechamento:** construir do zero (opção c), estendendo o motor já validado deste repositório — não fork, não combinação de peças de terceiros como esqueleto. Ver seção final para a justificativa completa e os três padrões de implementação que vale estudar sem copiar código.

---

## Eixo 1. Governança de código para agentes de IA (registro de decisão, trilha de auditoria, changelog estruturado)

### Buscas rodadas

`gh search repos` para: "AI agent decision log", "AI agent audit trail", "agent changelog", "ADR agent", "AI governance changelog" (0 resultados), "AI agent accountability", "agent activity log", "LLM decision log" (0 resultados), "agent decision record", "AI agent traceability", "AI agent audit trail dashboard" (0), "structured changelog agent" (0), "AI agent governance log" (0), "agent decision log markdown" (0). Complementado com `gh repo view`, `gh api repos/.../commits`, `gh api repos/.../branches/main` e leitura do README real via `raw.githubusercontent.com` para os três candidatos mais relevantes.

### Candidatos verificados

| org/repo | estrelas | último commit | licença | o que faz (verificado no README) | fit com o projeto planejado |
|---|---|---|---|---|---|
| `me2resh/agent-decision-record` (AgDR) | 48 | 2026-07-23 no branch `main`; atividade de PR review ainda em 12–13/09/2026 | CC BY 4.0 declarada no README (GitHub classifica como "Other/NOASSERTION", não-SPDX) | Padrão aberto de "Agent Decision Record": arquivo Markdown com frontmatter (id, timestamp, agent, model, trigger, status), template estilo Y-statement, JSON Schema e validador em CI. Grava a decisão no momento em que o agente decide, com metadados de auditoria. Instalável como plugin/skill do Claude Code. | Candidato mais próximo do *conceito* do eixo (decisão de agente + trilha de auditoria + changelog em lockstep via GitHub Action). Mas zero das quatro funções centrais do projeto planejado: não conta LOC/palavras, não conta tokens, não converte custo, não é painel HTML. É formato de arquivo + validador, não dashboard. |
| `macromania/adr-agent` | 20 | 2025-05-29 (mais de um ano parado) | nenhuma declarada | Prompts + agente Python (LangChain/Azure OpenAI + FAISS) para ajudar um humano a *escrever* um ADR tradicional. Não é o agente auditando o próprio trabalho. | Fraco — é "ADR com ajuda de IA", não log de decisão feito pelo agente. Nenhuma métrica quantitativa, nenhum HTML. |
| `Trusted-Autonomy/TrustedAutonomy` | 7 | 2026-09-11 (ativo) | Apache-2.0 | Gateway MCP de staging: mudanças do agente viram "ChangeSets" revisados por humano antes de ir ao projeto real. Controle de aprovação em tempo de execução, não log estruturado. | Fraco — accountability de execução, não registro consultável. Zero relação com LOC/tokens/custo. |
| `aeoess/agent-passport-system` (APS) | 45 | 2026-09-10 (ativo) | Apache-2.0 | Identidade/delegação criptográfica (Ed25519) para agentes, recibos assinados hash-chained de cada ação, foco em autorização de alto risco. | Fraco — accountability de identidade/autorização, não log de decisão técnica nem changelog. |

Uma cauda de repositórios com 0–3 estrelas apareceu nas buscas por "AI agent decision log"/"AI governance changelog" (ex.: `ai-identity/forensic-audit-trail-spec`, já arquivado como superado pelo OCSF 1.9.0; `govos-sdk/govos`, sem licença nem estrelas) — descartados por falta de maturidade e de fit, nenhum chega perto de LOC/palavras/tokens/custo.

### Conclusão do eixo

Existe um candidato relevante para o *conceito* de governança de decisão de agente (`me2resh/agent-decision-record`), mas nenhum candidato forte para servir de base de fork do painel. O AgDR poderia inspirar, no máximo, um formato de entrada de dados (decisão documentada por marco) a ser consumido pelo painel — não há aqui esqueleto técnico de HTML estático de custo/tokens/LOC.

---

## Eixo 2. Contadores de linhas de código / atividade de repositório

### Buscas e verificações rodadas

Metadados via `gh api` para: `AlDanial/cloc`, `XAMPPRocky/tokei`, `boyter/scc`, `erikbern/git-of-theseus`, `acaudwell/Gource`, `git-quick-stats/git-quick-stats`, `o2sh/onefetch`, `src-d/hercules`, `hoxu/gitstats`, `IonicaBizau/git-stats`. READMEs reais lidos via `WebFetch`/`raw.githubusercontent.com` para confirmar formato de output (não assumido de memória). `gh api repos/boyter/scc/releases` para confirmar quando o `--report` HTML foi introduzido.

### Candidatos verificados

| org/repo | estrelas | último commit | licença | output real (verificado no README/release notes) | fit |
|---|---|---|---|---|---|
| `AlDanial/cloc` | 23.524 | 2026-09-08 | GPL-2.0 | Texto, markdown, csv, json, xml, yaml, sql. Sem HTML nativo. | Fora — sem HTML, sem marco, sem palavras, sem token/custo. |
| `XAMPPRocky/tokei` | 14.907 | 2026-09-06 | MIT/Apache-2.0 dual (API do GitHub reporta "Other" por causa da grafia `LICENCE-MIT`/`LICENCE-APACHE`) | Tabela de terminal, json, yaml, cbor. Sem HTML, sem histórico temporal nativo. | Fora. |
| `boyter/scc` | 8.742 | 2026-09-11 | MIT | Múltiplos formatos incluindo html/html-table; desde a v4.0.0 (~3 semanas antes da pesquisa) um `--report` que gera **HTML autocontido** (SVG inline, sem JS/rede externa) com breakdown por linguagem, timelines de linguagem/autor via git log, e estimativas COCOMO e **LOCOMO** (custo de LLM). | **O mais próximo de todos os candidatos verificados nos cinco eixos.** Mas: (1) LOCOMO é custo *hipotético de regenerar o código existente via LLM*, não tokens realmente consumidos durante o desenvolvimento; (2) preço configurável só por flag de CLI (`--locomo-input-price` etc.) antes de gerar o relatório, nunca editável dentro do HTML já publicado; (3) só conta linhas de código, nunca palavras; (4) a timeline é uma janela contínua de commits recentes, sem conceito de "marco" nomeado. |
| `erikbern/git-of-theseus` | 2.962 | 2023-11-25 (dormente) | Apache-2.0 | JSON + PNG via matplotlib (stack plot por coorte de ano). Nada de HTML. | Fora, e parado há quase 3 anos. |
| `acaudwell/Gource` | 13.137 | 2026-03-06 | GPL-3.0 | Visualização OpenGL em tempo real, exporta vídeo via ffmpeg. | Fora — nem é HTML. |
| `git-quick-stats/git-quick-stats` | 7.003 | 2026-04-18 | MIT | Terminal interativo, csv, json, heatmap ASCII. Sem HTML. | Fora. |
| `o2sh/onefetch` | 12.049 | 2026-09-13 | MIT | Terminal estilo neofetch, snapshot único, sem histórico temporal. | Fora. |
| `src-d/hercules` | 2.807 | 2023-02-07 (dormente; empresa dissolvida) | "Other" | Binário Go emite YAML/protobuf cru; precisa de `labours.py` externo para virar PNG. | Fora, efetivamente abandonado. |
| `hoxu/gitstats` | 1.678 | 2024-03-07 (dormente) | sem LICENSE raiz padrão (GPLv2/GPLv3 em `doc/`) | README confirma: "Currently HTML is the only output format" — gera diretório de HTML estático com tabelas e gráficos via Gnuplot, incluindo evolução de linhas de código no histórico linear. | Segunda aproximação mais próxima (HTML com evolução no tempo), mas exige toolchain local (Python + Gnuplot), sem marco nomeado, sem palavras, sem token/custo, sem manutenção há dois anos. |
| `IonicaBizau/git-stats` | 6.599 | 2025-11-09 | MIT | Nativamente terminal ANSI; HTML só via ferramenta companheira separada (`git-stats-html`). | Fora — HTML não é nativo. |

### Conclusão do eixo

Nenhum candidato produz, de fábrica, o HTML de marco/dashboard visual exigido (linhas **e** palavras por marco, tokens de LLM por marco, custo configurável ao vivo dentro do HTML publicado). `boyter/scc` é o mais maduro e ativo que chega perto — vale estudar seu LOCOMO como contraste conceitual (custo hipotético de regeneração vs. custo real de uso, que é exatamente a distinção que este projeto já acerta) — mas não serve de esqueleto de fork.

---

## Eixo 3. Rastreadores de uso e custo de token de LLM

### Buscas e verificações rodadas

`gh search repos` para "ccusage", "claude code usage", "llm cost tracker", "token cost calculator llm" (0 resultados). `gh api repos/<org>/<repo>` para: `ccusage/ccusage`, `AgentOps-AI/tokencost`, `BerriAI/litellm`, `Helicone/helicone`, `langfuse/langfuse`, `foyzulkarim/claude-lens`, `zhnd/lumo`, `ColeMurray/claude-code-otel`, `AeternaLabsHQ/claude-code-stats`, `0xelitesystem/prompt-cost-calculator`, `phuryn/claude-usage`, `gfargo/token-tally`. Leitura real de README via `raw.githubusercontent.com` para os principais. `gh api repos/BerriAI/litellm/contents/model_prices_and_context_window.json` confirmou a existência do arquivo de preços (2,4 MB).

### Candidatos verificados

| org/repo | estrelas | último commit | licença | arquitetura real (verificada) | preço configurável onde | fit |
|---|---|---|---|---|---|---|
| `ccusage/ccusage` | 18.528 | 2026-09-13 | "Other" (não-SPDX) | **CLI de terminal** (Rust/TS), lê JSONL local de 18+ agentes (Claude Code incluído), não gera HTML, sem servidor. | `ccusage.json` (dev-side); modo `--offline`. Sem UI. | Motor de leitura mais próximo do caso real (mesma fonte JSONL, mesmo problema de dedup que este repo já resolveu), mas é ferramenta de terminal, não painel publicável. Confirma que a abordagem do motor deste repo (ler JSONL, deduplicar por id de mensagem) é validada por um projeto de 18,5 mil estrelas. |
| `AeternaLabsHQ/claude-code-stats` | 35 | 2026-09-08 | MIT | Script Python **gera HTML estático** a partir de JSONL do Claude Code. README avisa explicitamente para **não publicar o output na internet**. | Preço vem de `config.json` no momento da geração — fica **embutido (baked-in)** no HTML gerado, não editável depois de publicado. | O mais próximo em forma (HTML estático + lê Claude Code), mas falha exatamente na característica diferencial do projeto planejado (preço fixo no build) — e o próprio autor desaconselha publicação pública, o oposto do requisito "sempre consultável publicamente". |
| `phuryn/claude-usage` | 2.217 | 2026-07-10 | MIT | Servidor Python local (`dashboard.py`, SQLite) em `localhost:8080`. Não é arquivo estático. | Tabela de preços fixa no código (hardcoded). | Não serve — tem backend (mesmo que local) e preço não configurável em lugar nenhum. |
| `AgentOps-AI/tokencost` | 2.008 | 2025-09-05 (~1 ano parado) | MIT | Biblioteca Python para embutir em código; tabela de preços estática. | Tabela estática no pacote, sem UI. | Não é HTML nem painel; lib para chamar de dentro de outro programa. |
| `BerriAI/litellm` | 58.635 | 2026-09-13 | "Other" (não-SPDX) | Proxy/gateway server (backend) + SDK. Mantém `model_prices_and_context_window.json`, a base de preços por modelo mais referenciada do ecossistema. | JSON de preços dev-side + dashboard administrativo do proxy (exige o serviço rodando). | Excelente fonte de dados de preço por modelo, péssimo fit arquitetural — gateway de produção, não arquivo estático. |
| `Helicone/helicone` | 6.153 | 2026-09-11 | Apache-2.0 | Plataforma de 5 serviços (frontend Next.js, worker Cloudflare, servidor Express, Postgres, ClickHouse, Minio), self-host via Docker Compose/Helm. | Via serviço, exige toda a stack rodando. | Confirma a premissa do briefing: backend + banco obrigatórios, nada estático. |
| `langfuse/langfuse` | 34.540 | 2026-09-13 | "Other" (não-SPDX) | Hospedado ou self-host via Docker Compose/Helm/Terraform + ClickHouse + worker. | Via serviço, nada client-side. | Mesma categoria de Helicone. |
| `0xelitesystem/prompt-cost-calculator` | 0 | 2026-08-27 | MIT | **Único arquivo HTML estático** (~600 linhas, JS vanilla, zero dependências/build), hospedável em GitHub Pages/Netlify/S3 sem servidor, recalcula custo ao vivo em JS. | Preço é uma constante no código-fonte (objeto `PROVIDERS` dentro do `<script>`) — **não há campo de input de preço na UI publicada.** Também não lê transcript/JSONL, só texto de prompt colado manualmente. | Mais próximo em arquitetura pura (HTML único, zero backend, JS puro), mas falha nos outros dois pontos centrais: preço não editável pelo usuário final na página publicada, e sem leitura de log de sessão/marco. |

Também checados e descartados por arquitetura de servidor/processo: `foyzulkarim/claude-lens` (246 estrelas, dashboard local Node), `zhnd/lumo` (147 estrelas, "local-first dashboard" com processo rodando), `ColeMurray/claude-code-otel` (497 estrelas, observabilidade OpenTelemetry).

### Conclusão do eixo

Nenhum candidato verificado é, ao mesmo tempo, (1) arquivo HTML estático sem backend, (2) leitor de transcript real de sessão de agente (JSONL) por marco de projeto, e (3) exibidor de preço de token como campo editável na própria interface do HTML já publicado, recalculando ao vivo. Os dois candidatos mais próximos dividem essas exigências entre si sem que nenhum cubra as três: `claude-code-stats` lê JSONL e gera HTML mas o preço é congelado no build (e o autor desaconselha publicar); `prompt-cost-calculator` é HTML único com recálculo ao vivo mas o preço é constante de código e não lê log algum. **Isso confirma, com evidência real e não suposição, que a combinação central do projeto planejado é de fato o ponto genuinamente não resolvido em nenhum lugar de referência.**

---

## Eixo 4. Geradores de "diário de bordo" / changelog de marco de projeto

### Buscas e verificações rodadas

`gh search repos` para "changelog generator", "release notes generator", "devlog generator", "commit activity dashboard" (0), "changelog metrics"/"changelog loc"/"changelog word count"/"changelog token usage" (quase todos 0 ou irrelevantes), "build in public dashboard", "worklog html generator", "project journal generator", "engineering changelog metrics", "git log statistics html", "cloc changelog", "token cost changelog", "llm token cost dashboard git", "milestone tracker effort". `gh api` para estrelas/licença/último push de: git-cliff, release-please, auto-changelog, conventional-changelog, semantic-release, standard-version, devlog-ai, devlog-generator, engineer-profile. Leitura real de README via `WebFetch` para os principais.

### Candidatos verificados

| org/repo | estrelas | último commit | licença | o que realmente faz (verificado) | métrica quantitativa de esforço? | fit |
|---|---|---|---|---|---|---|
| `orhun/git-cliff` | 12.230 | 2026-09-12 | Apache-2.0 | Gera changelog a partir de commits convencionais + parsers regex customizáveis, saída texto/markdown templável. | Não. | Sem fit — puro parser/formatador de mensagens. |
| `conventional-changelog/conventional-changelog` | 8.508 | 2026-09-13 | ISC | Gera changelog/release notes a partir de mensagens de commit e metadados. | Não. | Sem fit. |
| `googleapis/release-please` | 7.489 | 2026-09-11 | Apache-2.0 | Lê Conventional Commits e abre PRs de release com CHANGELOG.md + bump de versão. | Não. | Sem fit. |
| `conventional-changelog/standard-version` | 7.981 | 2026-07-16 | ISC | Automatiza versionamento semver + CHANGELOG a partir de conventional commits. | Não. | Sem fit. |
| `semantic-release/semantic-release` | 24.035 | 2026-09-13 | MIT | Analisa mensagens de commit (texto, não métrica) para decidir tipo de release e gerar notas. | Não. | Sem fit. |
| `cookpete/auto-changelog` | 1.398 | 2026-09-05 | MIT | CLI que gera changelog a partir de tags/histórico de commits, templates compact/keepachangelog/json/handlebars. | Não. | Sem fit. |
| `goswamiSiddharth/devlog-ai` | 0 | 2026-06-05 | MIT | Lê commits git locais, envia a um LLM local (Ollama), gera devlog markdown por período + site estático no GitHub Pages com "stats dashboard" (total de commits, "lines written" agregado). | Parcial — conta linhas, mas só como total agregado do projeto inteiro, não por marco individual; não conta tokens de LLM nem converte em custo (usa LLM local, sem custo de API). | **Fit mais próximo de todo o eixo**, mas incompleto: falta granularidade por marco, tokens e custo monetário. 0 estrelas, projeto pequeno/pessoal. |
| `DanielCuevas1208/engineer-profile` | 1 | 2026-09-12 | MIT | Monta portfólio estático a partir de dados de commits/releases, com verificação de deploy via hash SHA-256. "Metrics" da descrição são de auditoria/deploy (arquivos add/changed/removed), não de esforço. | Não. | Sem fit — nome enganoso. |

### Conclusão do eixo

No espaço inteiro de geradores de changelog/release-notes — incluindo os nichos de devlog e "build in public" — não existe ferramenta madura que combine registro de marco de projeto com contagem de LOC/palavras/tokens de LLM convertida em custo monetário. A esmagadora maioria (git-cliff, release-please, conventional-changelog, semantic-release, auto-changelog, standard-version) só categoriza e formata mensagens de commit em texto. O único achado com contagem quantitativa real (`devlog-ai`, 0 estrelas) soma linhas agregadas do projeto todo, sem granularidade por marco e sem tokens/custo — nenhum candidato serve como base de fork honesta para este eixo.

---

## Eixo 5. Comparadores de custo entre provedores de LLM

### Buscas e verificações rodadas

`gh api repos/simonw/llm-prices` (metadados), `gh api repos/simonw/llm-prices/contents` e `contents/scripts`/`contents/data` (estrutura de arquivos), `gh api .../contents/scripts/build.py` e `.../contents/index.html` (lidos e decodificados de base64 — código-fonte real, não descrição), `WebFetch https://www.llm-prices.com/` (comportamento ao vivo da página). `gh search repos` para "llm pricing calculator", "token cost calculator", "openai pricing calculator", "gpt cost calculator". `gh api orgs/ArtificialAnalysis/repos` e `gh api users/OpenRouterTeam/repos` para checar se os comparadores mais conhecidos do mercado (artificialanalysis.ai, openrouter.ai/models) têm componente open-source. `gh api repos/<owner>/<repo>` para candidatos secundários de baixa tração.

### Candidatos verificados

| Repo/site | Estrelas | Último commit | Licença | Arquitetura real (verificada no código) | Preço editável pelo usuário na UI publicada? | Fit |
|---|---|---|---|---|---|---|
| `simonw/llm-prices` (llm-prices.com) | 183 | 2026-09-04 | Nenhuma declarada (`license: null` na API, sem arquivo LICENSE) | Site 100% estático (HTML/CSS/JS puro, hospedado no Cloudflare Pages), sem backend. Preços em JSON por provedor, compilados por `scripts/build.py` em `current-v1.json`/`historical-v1.json`, carregados via `fetch` pelo JS do `index.html`. | **Sim, confirmado no código-fonte.** Há `<input type="number">` para preço de entrada, cache e saída, e outro para contagem de tokens; a função `calculateCost()` recalcula ao vivo; o estado é serializado na URL hash (sem servidor). | **É o achado mais próximo do mecanismo descrito em todos os cinco eixos.** Confirma que "preço editável pelo usuário final + recálculo client-side, sem backend" já existe, publicado, funcional e mantido ativamente. Mas é comparador de preço entre modelos, não painel de marcos de projeto — o fit é só no mecanismo isolado. |
| ArtificialAnalysis (org GitHub: Stirrup 606★, StirrupJS 21★, Optima 8★) | — | Stirrup: 2026-08-25 | não verificado (fora de escopo) | Nenhum dos três repos públicos é o site/comparador em si — são frameworks de agente. | Não aplicável. | Sem repo público do produto de comparação; artificialanalysis.ai é fechado. |
| OpenRouterTeam (org GitHub, ex.: ai-sdk-provider 685★, awesome-openrouter 470★) | — | vários até 2026-09-13 | vários (MIT em parte) | Nenhum repo listado é o frontend de preços do openrouter.ai/models — são SDKs, exemplos, docs. | Não aplicável. | Sem repo público do frontend de preços; fechado. |
| `costgoat/ai-pricing-calculators`, `TauqeerMustafa/token-cost-calculator`, `slashman413/token-cost-calculator`, `vbakshiusa/token-cost-calculator`, `alyonarout/TokenTrack` | 0–1 cada | vários 2025–2026 | nenhuma ou MIT | Baixa tração, alguns em Python (não client-side), nenhum verificado como referência de qualidade. | Não confirmado. | Irrelevantes como referência — sem tração, sem sinal de manutenção. |

### Conclusão do eixo

Existe sim uma referência real, aberta (código publicamente visível, embora sem licença declarada) e ativamente mantida — `simonw/llm-prices` — que implementa exatamente o mecanismo em questão. Ao mesmo tempo, esse mecanismo isolado (um `<input type="number">` de preço, uma função JS que multiplica por contagem de tokens e atualiza o DOM) é trivial de implementar do zero, poucas dezenas de linhas de JavaScript sem dependência nenhuma. Achar um bom exemplo confirmado não é, por si só, motivo suficiente para fork — o valor de um fork viria de outra coisa (arquitetura de dados por marco, motor de contagem), que este site não tem.

---

## Lacunas e ressalvas honestas

**Duas fontes ficaram com licença ambígua e isso importa para uma decisão de fork.** `simonw/llm-prices` não declara licença (`license: null` na API do GitHub, sem arquivo `LICENSE`) — código publicamente visível, mas sem termos de reuso formalizados; forkar literalmente esse repositório exigiria contato com o autor antes de redistribuir. `boyter/scc` é MIT (sem ambiguidade), mas `tokei`, `litellm` e `langfuse` aparecem como "Other" na API por convenções de nome de arquivo de licença não-padrão (`LICENCE-MIT` britânico, ou dual-license não lido automaticamente pelo GitHub) — não são "sem licença" de fato, só não-SPDX-padrão; nenhum desses é candidato a fork de qualquer forma, então a ambiguidade não afeta a recomendação final.

**Um achado não estava no escopo original dos cinco eixos e vale registrar.** `ccusage/ccusage` (18.528 estrelas, ativo) confirma de forma independente que a abordagem já usada por `build/generate_logbook_metrics.py` deste repositório — ler o JSONL de sessão do Claude Code e deduplicar eventos de uso — é a mesma abordagem de um projeto de referência do ecossistema, não uma solução isolada. Isso é evidência a favor da robustez do motor já construído aqui, não um candidato a fork (é CLI, não HTML).

**Não foi encontrado nenhum precedente brasileiro ou em português em nenhum dos cinco eixos.** Todas as buscas retornaram projetos em inglês; isso é esperado dado o domínio (ferramentas de desenvolvimento open-source), mas vale declarar que a ausência não foi verificada com termos em português — as buscas usaram termos em inglês por ser onde está o volume real do ecossistema GitHub, e essa escolha foi deliberada, não um vazio de busca.

---

## A decisão

**Recomendação: (c) construir do zero**, estendendo o motor já validado deste repositório — não fork de um repositório específico, não montagem de peças de terceiros como esqueleto técnico.

**Por que não (a), fork de um repositório específico.** Nenhum dos cerca de quarenta candidatos verificados nos cinco eixos cobre a combinação central do projeto planejado — marco de projeto + contagem de LOC/palavras + custo de token de LLM configurável ao vivo, tudo num HTML estático público. O candidato mais próximo de qualquer eixo (`boyter/scc`, eixo 2) erra o requisito mais importante: seu LOCOMO é custo hipotético de regenerar código existente via LLM, não tokens realmente consumidos durante o desenvolvimento, e seu preço só é configurável por flag de CLI antes de gerar o relatório, nunca editável na página já publicada. Forkar `scc` significaria herdar um parser de linguagens de programação inteiro (a real complexidade daquele projeto) para descartar a única parte que interessaria.

**Por que não (b), combinar peças de dois ou três repositórios.** As peças que existem não se encaixam por serem de naturezas arquiteturais opostas: os leitores de transcript de sessão de agente que existem são CLIs ou servidores locais (`ccusage`, `claude-code-stats`, `claude-usage`), nunca HTML estático publicável; os geradores de HTML estático de métricas de repositório que existem (`scc --report`, `gitstats`) não sabem nada sobre tokens de LLM nem sobre o formato JSONL de transcript de agente; e o único mecanismo de preço editável em HTML puro que existe (`simonw/llm-prices`) é deliberadamente simples o bastante para não valer a pena importar como dependência — copiar aquela função de poucas linhas não é "combinar repositórios", é reimplementar um padrão trivial. Não há sutura possível entre essas peças que produza menos trabalho do que escrever direto.

**Por que (c) é a resposta honesta, não a de conveniência.** O motor de métrica que já existe neste repositório (`build/generate_logbook_metrics.py`) já foi testado fora deste projeto — reuso real, não hipotético, em 11 de setembro de 2026, num projeto de cliente confidencial, achando e corrigindo três bugs reais (dobra de contagem de token, vazamento de path local, lacuna de ordem do glossário) — a mesma régua de generalização que o `intake-briefing` já tinha superado antes de virar skill própria. A parte que falta (LOC/palavras já existe; tokens já existe; o que falta é só a conversão para custo com preço configurável, tanto como constante no código quanto como campo de UI) é pequena o suficiente para não justificar herdar a complexidade de nenhum dos candidatos acima, e específica o suficiente (ler JSONL de agente + noção de marco nomeado + preço editável publicado) para não existir pronta em lugar nenhum verificado.

**Três padrões de implementação para estudar, não código para copiar:**

1. **De `simonw/llm-prices`:** o padrão de `<input type="number">` + função JS pura de recálculo + estado na URL hash, para o campo de preço editável na UI publicada. É código simples o bastante para reimplementar direto, mas vale olhar a implementação real antes, porque já resolveu os detalhes de UX (formatação de moeda, atualização ao digitar vs. ao confirmar).
2. **De `AeternaLabsHQ/claude-code-stats`, como contraste negativo:** a decisão de embutir o preço no momento da geração, e a advertência do próprio autor contra publicar o resultado, confirmam por evidência externa (não só por design interno) que preço fixo no build é o erro a evitar — o requisito de preço editável na página já publicada não é over-engineering, é a lição que outro projeto já pagou.
3. **De `boyter/scc` (LOCOMO), como contraste negativo:** a distinção entre custo hipotético de regenerar código via LLM e custo real de tokens consumidos durante o trabalho é exatamente a linha que este projeto já não cruza (o motor atual soma `usage` real do transcript, nunca estima) — vale manter essa distinção explícita na documentação da futura skill, porque é precisamente onde um projeto de referência do mercado tropeça.
