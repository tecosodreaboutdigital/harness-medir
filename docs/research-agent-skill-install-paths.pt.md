# Pesquisa: caminhos de instalação de skill por ambiente

Documento de trabalho interno. Levantado em 13 de setembro de 2026.

**Estatuto deste documento.** Isto é insumo de pesquisa para a seção de instalação da futura skill `milestone-loc-tokens-ai-ledger` (ainda não criada). **Não é conteúdo publicado da série harness-medir** e não deve receber `git add`/`git commit` — fica fora do controle de versão deste repositório, como qualquer rascunho de bastidor.

**O que este documento faz.** Reverifica, contra a documentação OFICIAL atual de cada fornecedor (aberta e lida nesta sessão, nunca por memória de treinamento), o baseline registrado pelo repositório-irmão `intake-briefing` em 31/08/2026 sobre onde cada ambiente de IA espera encontrar uma skill instalável ou um arquivo de instrução de projeto. Cada afirmação abaixo carrega a URL exatamente consultada, a data de hoje, e um veredito.

**Legenda.**
- **CONFIRMADO (C)** — a fonte oficial do próprio fornecedor foi aberta nesta sessão e confirma a afirmação, sem ambiguidade relevante.
- **PARCIAL (P)** — a fonte oficial existe mas é vaga, incompleta, ou internamente inconsistente entre páginas oficiais do mesmo fornecedor; ou uma fonte secundária respeitável cobre o detalhe faltante ao lado de uma fonte oficial vaga. A ressalva específica é sempre nomeada.
- **NÃO VERIFICADO (N)** — nenhuma fonte oficial foi encontrada. Nunca afirmar suporte neste caso; no máximo registrar um sinal secundário, rotulado explicitamente como tal.

---

## Sumário

| # | Item | Veredito | Caminho/convenção segundo a fonte oficial |
|---|---|---|---|
| 1 | Claude Code (skills + plugin/marketplace) | **CONFIRMADO** | `~/.claude/skills/<nome>/SKILL.md` (pessoal), `.claude/skills/<nome>/SKILL.md` (projeto), `<plugin>/skills/<nome>/SKILL.md` (plugin); `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json`, comandos `/plugin marketplace add` e `/plugin install` |
| 2 | Cursor | **CONFIRMADO** | `.cursor/skills/` e `.agents/skills/` (projeto, ambos primários); `~/.cursor/skills/` e `~/.agents/skills/` (pessoal); compatibilidade retroativa com `.claude/skills/` e `.codex/skills/`. Separadamente, `AGENTS.md` na raiz é suportado como alternativa a `.cursor/rules/*.mdc` |
| 3 | OpenAI Codex CLI | **CONFIRMADO** | `AGENTS.md` hierárquico (`~/.codex/AGENTS.md` → raiz do git até o diretório atual); skills em `.agents/skills/` (`$CWD`, `$CWD/..`, `$REPO_ROOT`) e `$HOME/.agents/skills` |
| 4 | Google Antigravity | **PARCIAL** | Convenção de projeto confirmada e consistente: `.agents/skills/<nome>/SKILL.md`. Caminho pessoal/global **inconsistente entre três páginas oficiais** do próprio antigravity.google (três strings diferentes encontradas) |
| 5a | Gemini CLI | **CONFIRMADO**, com alerta de descontinuação | `GEMINI.md` (contexto) e `.gemini/skills/` ou alias `.agents/skills/` (projeto), `~/.gemini/skills/` ou alias `~/.agents/skills/` (pessoal). Mas o produto standalone está sendo descontinuado para contas individuais desde 18/06/2026, conforme blog oficial do Google |
| 5b | Gemini (chat comum) | **PARCIAL** | Só instrução customizada colada manualmente (texto) + arquivos de conhecimento anexados a um Gem; nenhuma menção oficial a carregar arquivo de projeto ou repositório |
| 6 | VS Code (via extensão Copilot) | **CONFIRMADO** | `.github/copilot-instructions.md` (instrução clássica) **e**, separadamente, o padrão mais novo "Agent Skills": `.github/skills/`, `.claude/skills/`, `.agents/skills/` (projeto) e `~/.copilot/skills/`, `~/.agents/skills/` (pessoal), com suporte nomeado ao "agent mode" do VS Code |
| 7 | Padrão aberto "Agent Skills" (agentskills.io) | **CONFIRMADO** | Padrão real, mantido em `github.com/agentskills/agentskills`, originado pela Anthropic. Cursor, OpenAI (Codex/ChatGPT), Google Antigravity, Gemini CLI e GitHub Copilot/VS Code **cada um confirma a adoção na própria documentação oficial**, com link direto para agentskills.io ou para o repositório do padrão |

---

## 1. Claude Code

### Skills: caminhos pessoal, de projeto e de plugin

A documentação oficial atual (`code.claude.com/docs/en/skills`) confirma, sem alteração em relação ao baseline de 31/08/2026:

> "~/.claude/skills/<skill-name>/SKILL.md" (pessoal)
> "`.claude/skills/<skill-name>/SKILL.md`" (projeto)
> "`<plugin>/skills/<skill-name>/SKILL.md`" (plugin)

E a página declara explicitamente a filiação ao padrão aberto:

> "Claude Code skills follow the [Agent Skills](https://agentskills.io) open standard, which works across multiple AI tools. Claude Code extends the standard with additional features like invocation control, subagent execution, and dynamic context injection."

> Fonte: <https://code.claude.com/docs/en/skills> · consultada em 13/09/2026 · **CONFIRMADO**

### Plugin e marketplace

A documentação oficial (`code.claude.com/docs/en/plugin-marketplaces`) confirma, também sem alteração:

> "Create `.claude-plugin/marketplace.json` in your repository root."
> "Create a `plugin.json` file that describes the plugin. The manifest goes in the `.claude-plugin/` directory" (ou seja, `.claude-plugin/plugin.json` dentro da pasta do plugin).

Comandos confirmados como sintaxe atual, sem aviso de depreciação:

```
/plugin marketplace add ./my-marketplace
/plugin install quality-review-plugin@my-plugins
```

com equivalentes não interativos `claude plugin marketplace add` e `claude plugin install`. A página referencia notas de versão até pelo menos `v2.1.239`, o que indica manutenção ativa bem depois da data do baseline (31/08/2026), sem sinal de mudança estrutural nos três caminhos nem nos dois comandos.

> Fonte: <https://code.claude.com/docs/en/plugin-marketplaces> · consultada em 13/09/2026 · **CONFIRMADO**

**Veredito:** CONFIRMADO. Os três caminhos de skill e o mecanismo de plugin/marketplace (`.claude-plugin/marketplace.json`, `.claude-plugin/plugin.json`, `/plugin marketplace add`, `/plugin install`) permanecem exatamente como registrado em 31/08/2026, agora verificados contra a doc oficial atual, com o adendo de que a própria Anthropic nomeia explicitamente o padrão `agentskills.io` como a base do formato SKILL.md do Claude Code.

---

## 2. Cursor

A suposição do baseline era de que Cursor "converge" para `.agents/skills/<nome>/SKILL.md` sem necessariamente ter documentação própria confirmando isso. Isso está desatualizado para menos, não para mais: a Cursor **hoje documenta oficialmente e por nome** um mecanismo próprio de "Agent Skills".

### Skills

`cursor.com/docs/context/skills` apresenta uma tabela de "Skill directories" com quatro caminhos primários e mais dois de compatibilidade retroativa:

- Projeto (primário, ambos): `.agents/skills/` e `.cursor/skills/`
- Pessoal (primário, ambos): `~/.agents/skills/` e `~/.cursor/skills/`
- Compatibilidade retroativa adicional: `.claude/skills/`, `.codex/skills/` (projeto) e `~/.claude/skills/`, `~/.codex/skills/` (pessoal)

E a página fecha citando o padrão pelo nome, com link direto:

> "Agent Skills is an open standard. Learn more at [agentskills.io](https://agentskills.io)."

Um exemplo de estrutura de pasta é dado explicitamente como:

```
.agents/
└── skills/
    └── my-skill/
        └── SKILL.md
```

Nota de leitura: um usuário de Cursor com skills salvas em `~/.cursor/skills/` precisa sincronizar explicitamente esse caminho para uso com Cloud Agents; skills de projeto (`.cursor/skills/` ou `.agents/skills/`) ficam disponíveis automaticamente.

> Fonte: <https://cursor.com/docs/context/skills> · consultada em 13/09/2026 · **CONFIRMADO**

### AGENTS.md e .cursor/rules — mecanismo separado

`cursor.com/docs/rules` documenta, em página distinta da de skills:

> "`AGENTS.md` is a simple markdown file for defining agent instructions. Place it in your project root as an alternative to `.cursor/rules`."
> "Project rules live in `.cursor/rules` as `.mdc` files and are version-controlled."

Esta página de rules não menciona SKILL.md nem "Agent Skills" em nenhum momento — é um mecanismo deliberadamente separado do de skills, não uma alternativa a ele.

> Fonte: <https://cursor.com/docs/rules> · consultada em 13/09/2026 · **CONFIRMADO**

**Veredito:** CONFIRMADO. A Cursor documenta oficialmente, por nome e com link direto a agentskills.io, um mecanismo nativo de "Agent Skills" (SKILL.md), com caminho próprio (`.cursor/skills/`) coexistindo com o caminho do padrão aberto (`.agents/skills/`) e compatibilidade retroativa explícita para os caminhos de Claude Code e Codex CLI. Isso é mais forte do que o baseline registrou: não é apenas convergência de pasta, é adoção documentada e nomeada.

---

## 3. OpenAI Codex CLI

### AGENTS.md

A página do próprio repositório oficial (`github.com/openai/codex/blob/main/docs/agents_md.md`) redireciona (308) para `developers.openai.com/codex/guides/agents-md`, que por sua vez redireciona (308) para `learn.chatgpt.com/docs/agent-configuration/agents-md`. As três URLs pertencem à própria OpenAI (o domínio final é a plataforma de documentação/aprendizado da OpenAI, com a mesma marca "OpenAI Developers"); registro essa cadeia de redirecionamento por transparência, já que a URL final consultada difere do domínio nomeado na missão (`developers.openai.com`).

Na página final:

> "Codex reads `AGENTS.md` files before doing any work."

A hierarquia documentada:

1. Escopo global: `~/.codex/AGENTS.override.md` (se existir), senão `~/.codex/AGENTS.md`
2. Escopo de projeto: da raiz do git até o diretório de trabalho atual, verificando `AGENTS.override.md` e depois `AGENTS.md` em cada diretório do caminho
3. Arquivos mais próximos do diretório atual sobrescrevem orientação anterior (concatenação da raiz para baixo)

> Fonte: <https://learn.chatgpt.com/docs/agent-configuration/agents-md> (redirecionada de developers.openai.com/codex/guides/agents-md) · consultada em 13/09/2026 · **CONFIRMADO**

### Skills

`developers.openai.com/codex/skills` redireciona (308) para `learn.chatgpt.com/docs/build-skills`, também doc oficial da OpenAI:

> "A skill is a directory with a `SKILL.md` file plus optional scripts and references."
> "Skills build on the [open agent skills standard](https://agentskills.io)."
> "Standalone skills are available in the ChatGPT desktop app, Codex CLI, and IDE extension."

Caminhos documentados especificamente para Codex CLI:

- Repositório: `$CWD/.agents/skills`, `$CWD/../.agents/skills`, `$REPO_ROOT/.agents/skills`
- Usuário: `$HOME/.agents/skills`
- Administração/compartilhado: `/etc/codex/skills`, mais skills `SYSTEM` empacotadas com o próprio Codex

> Fonte: <https://learn.chatgpt.com/docs/build-skills> (redirecionada de developers.openai.com/codex/skills) · consultada em 13/09/2026 · **CONFIRMADO**

**Veredito:** CONFIRMADO. O Codex CLI lê `AGENTS.md` hierarquicamente (confirmado, não é só um arquivo único na raiz — é uma cadeia de arquivos por diretório) e também suporta uma pasta de skills própria em `.agents/skills/`, com a própria OpenAI citando o "open agent skills standard" (agentskills.io) como base. Isso atualiza o baseline de 31/08/2026, que registrava Codex CLI apenas convergindo para `.agents/skills/<nome>/SKILL.md` sem confirmação — agora está confirmado, com detalhe extra de precedência de diretório para AGENTS.md que o baseline não continha.

---

## 4. Google Antigravity

Antigravity tem documentação oficial pública real em `antigravity.google/docs/`, não apenas cobertura de terceiros — isso já resolve a pergunta mais básica da missão ("existe doc oficial suficiente?" — sim). Mas essa documentação, consultada em três páginas diferentes hoje, não é internamente consistente sobre um detalhe: o caminho pessoal/global.

### Convenção de projeto — consistente nas três páginas

`antigravity.google/docs/ide/skills`:

> "Every skill needs a `SKILL.md` file with YAML frontmatter at the top."
> Workspace: `<workspace-root>/.agents/skills/<skill-folder>/`
> "Antigravity now defaults to `.agents/skills`, but still maintains backward support for `.agent/skills`."
> Link para <https://agentskills.io/home>

`antigravity.google/docs/skills/` repete a mesma convenção de projeto (`.agents/skills/<skill-folder>/`) e o mesmo link para agentskills.io.

`antigravity.google/docs/cli/plugins/`, específica da CLI, também confirma skills de workspace em `.agents/skills/` na raiz do projeto (arquivos `.md`), mas aqui dentro de uma estrutura maior de plugin: bundle em `~/.gemini/antigravity-cli/plugins/<plugin_name>/`, contendo `plugin.json` obrigatório mais `skills/`, `agents/`, `rules/`, `hooks.json`, `mcp_config.json` opcionais. Esta página específica de CLI não cita agentskills.io.

### Caminho pessoal/global — inconsistente entre as três páginas oficiais

| Página oficial | Caminho global/pessoal documentado |
|---|---|
| `antigravity.google/docs/ide/skills` | `~/.gemini/antigravity/skills/<skill-folder>/` |
| `antigravity.google/docs/skills/` | `~/.gemini/config/skills/<skill-folder>/` |
| `antigravity.google/docs/cli/plugins/` | `~/.gemini/antigravity-cli/skills/` (específico da CLI) |

Três strings diferentes para três páginas do mesmo produto, consultadas no mesmo dia. É plausível que IDE, CLI e uma terceira superfície genérica tenham escopos pessoais realmente distintos (o produto é novo, lançado como marca unificada em maio de 2026 e ainda mudando rápido — ver seção 5a), mas a documentação, como está hoje, não deixa isso claro por si só, e nenhuma das três páginas reconhece ou explica a diferença em relação às outras duas.

> Fontes: <https://antigravity.google/docs/ide/skills> · consultada em 13/09/2026
> <https://antigravity.google/docs/skills/> · consultada em 13/09/2026
> <https://antigravity.google/docs/cli/plugins/> · consultada em 13/09/2026

**Veredito:** PARCIAL. A convenção de projeto (`.agents/skills/<nome>/SKILL.md`) está confirmada e é consistente nas três páginas oficiais, incluindo referência nomeada ao padrão aberto agentskills.io em duas delas. O caminho pessoal/global, porém, é vago por inconsistência interna da própria documentação oficial do fornecedor — não por falta de fonte oficial, mas porque a fonte oficial se contradiz entre si mesma. Recomendo, ao escrever a instalação da skill futura, citar apenas o caminho de projeto para Antigravity e marcar o caminho pessoal como "a confirmar antes de publicar", não presumir qual dos três está correto.

---

## 5. Gemini

### 5a. Gemini CLI

A convenção de contexto de projeto está confirmada na fonte primária, o próprio repositório mantenedor:

`github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md`:

> "Context files, which use the default name `GEMINI.md`"

Carregado de `~/.gemini/GEMINI.md` (global), dos diretórios de workspace configurados e de diretórios ancestrais até uma raiz confiável; o nome do arquivo é configurável via `context.fileName` em `settings.json`.

A convenção de skills, também na fonte primária:

`github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md`:

> "Based on the [Agent Skills](https://agentskills.io) open standard, a 'skill' is a self-contained directory that packages instructions and assets into a discoverable capability."

Caminhos: pessoal `~/.gemini/skills/` ou o alias `~/.agents/skills/`; de projeto `.gemini/skills/` ou o alias `.agents/skills/`.

> Fontes: <https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md> · consultada em 13/09/2026 · **CONFIRMADO**
> <https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md> · consultada em 13/09/2026 · **CONFIRMADO**

**Alerta crítico, não presente no baseline de 31/08/2026: o produto está sendo descontinuado para uso individual.**

O blog oficial do Google para desenvolvedores, publicado em 19/05/2026, declara:

> "On June 18, 2026, Gemini CLI and Gemini Code Assist IDE extensions will stop serving requests for Google AI Pro and Ultra, as well as those using it free of charge."
> "...we're unifying our efforts into Google Antigravity, our premier agent-first development platform," com a Antigravity CLI como a nova interface de terminal.

Contas com licença Gemini Code Assist Standard ou Enterprise mantêm acesso ao Gemini CLI legado. O post não trata do destino do próprio repositório GitHub `google-gemini/gemini-cli`, mas reabri e li o README diretamente hoje (13/09/2026): o repositório continua público, acessível, sem qualquer aviso de arquivamento ou depreciação no próprio README, e os arquivos de documentação de skills/GEMINI.md citados acima continuam publicados e inalterados nele.

> Fonte: <https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/> · publicado 19/05/2026, consultado em 13/09/2026 · **CONFIRMADO**
> Repositório reaberto e conferido diretamente: <https://github.com/google-gemini/gemini-cli> · consultado em 13/09/2026 · **CONFIRMADO** (sem aviso de arquivamento)

**Veredito:** CONFIRMADO para a convenção técnica (GEMINI.md + `.gemini/skills/`/`.agents/skills/`, com referência nomeada a agentskills.io, na fonte primária do próprio mantenedor). Mas com um alerta que precisa ir na skill futura em destaque: como produto standalone voltado a contas individuais gratuitas, Pro e Ultra, o Gemini CLI já parou de atender pedidos desde 18/06/2026, substituído pela Antigravity CLI. Contas com licença Gemini Code Assist Standard ou Enterprise mantêm acesso ao CLI legado (correção de consistência: uma versão anterior deste veredito restringia isso só a Enterprise, divergindo do parágrafo logo acima; a citação original do blog do Google não nomeia nenhum dos dois planos pagos, só declara quem para de ser atendido, então "Standard ou Enterprise" é a leitura mais fiel ao que foi de fato dito). Recomendar "Gemini CLI" para um usuário individual novo, sem essa ressalva, seria desatualizado a partir de hoje.

### 5b. Gemini (chat comum, gemini.google.com)

A Central de Ajuda oficial do Gemini confirma que instrução customizada existe, mas só como texto colado manualmente:

> "Only available in the Gemini mobile app, the Gemini web app at gemini.google.com, Gemini in Chrome (...), and Gemini on your smartwatch."
> "Enter the instructions you want Gemini Apps to apply to every chat."

Nenhuma menção a carregar um arquivo de projeto ou repositório automaticamente — o único método descrito é a digitação/colagem manual.

> Fonte: <https://support.google.com/gemini/answer/16598625?hl=en> · consultada em 13/09/2026

Sobre Gems (assistentes customizados dentro do Gemini): a página oficial descreve apenas dois tipos de insumo — instruções digitadas e "arquivos de conhecimento" anexados (upload do dispositivo, Google Drive, notebooks do NotebookLM). Nenhuma menção a montar um repositório ou carregar uma pasta de projeto.

> Fonte: <https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop> · consultada em 13/09/2026

Sobre "Gemini Extensions": pela cobertura oficial encontrada (páginas de ajuda do Gemini e do blog de desenvolvedores do Google, sem uma página única e definitiva sobre o assunto lida por completo nesta sessão), Extensions conectam o Gemini a outros serviços do Google (Gmail, Agenda, Keep, Tasks, Drive) para executar ações — é uma categoria diferente de "carregar instrução de projeto", não um substituto funcional.

**Veredito:** PARCIAL. A ausência de um mecanismo de carregamento automático de arquivo de projeto não é afirmada explicitamente em nenhuma frase do tipo "não suportamos X" — segue a ressalva da própria missão de que fornecedores raramente documentam o que não fazem. Mas encontrei fonte oficial que descreve exaustivamente os únicos dois métodos de dar contexto (instrução colada, arquivos de conhecimento anexados), e nenhum dos dois é "arquivo de projeto" ou "repositório". Isso é evidência direta o bastante para não ser tratado como puro silêncio, mas não é uma negação explícita — por isso PARCIAL, não CONFIRMADO nem NÃO VERIFICADO.

---

## 6. VS Code

VS Code em si não tem skills nativas — é o editor hospedando uma extensão. Duas coisas relevantes rodam dentro dele: a extensão do GitHub Copilot (coberta nesta seção) e a extensão do Claude Code (coberta pelo veredito do item 1 acima, já que usa exatamente os mesmos caminhos `.claude/skills/`/`~/.claude/skills/`).

### Instrução clássica: .github/copilot-instructions.md

A referência oficial (`docs.github.com/en/copilot/reference/custom-instructions-support`) traz uma matriz de suporte por superfície. Resumo confirmado: GitHub.com (Copilot Chat, cloud agent, code review), **Visual Studio Code** (todos os três), Visual Studio, JetBrains, Eclipse, Xcode e Copilot CLI suportam `.github/copilot-instructions.md`.

O guia de criação (`docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot`) confirma o caminho exato:

> "In the root of your repository, create a file named `.github/copilot-instructions.md`."

> Fontes: <https://docs.github.com/en/copilot/reference/custom-instructions-support> · consultada em 13/09/2026 · **CONFIRMADO**
> <https://docs.github.com/copilot/customizing-copilot/adding-custom-instructions-for-github-copilot> · consultada em 13/09/2026 · **CONFIRMADO**

### Mecanismo mais novo, e que o baseline de 31/08/2026 não continha: "Agent Skills" para GitHub Copilot

`docs.github.com/en/copilot/concepts/agents/about-agent-skills`:

> "Project skills, stored in your repository (`.github/skills`, `.claude/skills`, or `.agents/skills`)"
> "Personal skills, stored in your home directory and shared across projects (`~/.copilot/skills` or `~/.agents/skills`)"
> "Agent skills work with Copilot cloud agent, Copilot code review, the GitHub Copilot CLI, the GitHub Copilot app, and agent mode in Visual Studio Code and JetBrains IDEs."

Essa página do GitHub chama a especificação de "an open standard" mas linka para o repositório GitHub do padrão, não para o domínio agentskills.io diretamente.

`code.visualstudio.com/docs/copilot/customization/agent-skills`, específica do VS Code, confirma os mesmos caminhos e adiciona:

> "Learn more about the Agent Skills standard at agentskills.io."

> Fontes: <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills> · consultada em 13/09/2026 · **CONFIRMADO**
> <https://code.visualstudio.com/docs/copilot/customization/agent-skills> · consultada em 13/09/2026 · **CONFIRMADO**

**Veredito:** CONFIRMADO, e mais completo que o baseline. Dentro do VS Code, a extensão do GitHub Copilot suporta oficialmente dois mecanismos, não um: o clássico `.github/copilot-instructions.md` (instrução única de repositório) e o mais novo "Agent Skills" (`.github/skills/`, `.claude/skills/`, `.agents/skills/` de projeto; `~/.copilot/skills/`, `~/.agents/skills/` pessoal), este último nomeado com "agent mode" do VS Code explicitamente listado como superfície suportada. A extensão do Claude Code, separadamente, também roda dentro do VS Code — para essa, vale o veredito do item 1.

---

## 7. O padrão aberto "Agent Skills" (agentskills.io)

Esta seção existe para responder à pergunta crítica da missão: a "convergência" de Cursor, Codex CLI e Antigravity para `.agents/skills/` é adoção oficial de um padrão, ou só acidente de convenção de pasta que nenhum deles documenta oficialmente?

**Resposta, sem meias palavras: é adoção oficial, documentada, e não um acidente.**

### O que agentskills.io diz de si mesmo

Abri `agentskills.io` diretamente hoje:

> "The Agent Skills format was originally developed by [Anthropic](https://www.anthropic.com/), released as an open standard, and has been adopted by a growing number of agent products."

A página hospeda um "Client Showcase" que lista dezenas de ferramentas, cada uma com um link direto para a documentação oficial DAQUELA ferramenta (não uma alegação apenas do site agentskills.io) — entre elas: Cursor (`cursor.com/docs/context/skills`), Gemini CLI (`geminicli.com/docs/cli/skills/`), GitHub Copilot (`docs.github.com/en/copilot/concepts/agents/about-agent-skills`), VS Code (`code.visualstudio.com/docs/copilot/customization/agent-skills`), ChatGPT & Codex (`developers.openai.com/codex/skills/`), Claude Code (`code.claude.com/docs/en/skills`), Claude (`platform.claude.com/docs/en/agents-and-tools/agent-skills/overview`), e cerca de 35 outras ferramentas (Junie, OpenCode, OpenHands, Goose, Kiro, Databricks Genie Code, Roo Code, Factory, entre outras).

**Achado relevante por ausência:** Google Antigravity **não aparece** nesta lista de clientes do site agentskills.io, apesar de a própria documentação da Antigravity (seção 4 acima) linkar para agentskills.io de forma independente. Isso sugere que a lista do site é mantida manualmente e ainda não foi atualizada para incluir a Antigravity — não que a Antigravity não adote o padrão (ela adota, pela própria doc dela).

> Fonte: <https://agentskills.io> · consultada em 13/09/2026 · **CONFIRMADO**

### O repositório do padrão

`github.com/agentskills/agentskills` confirma a mesma origem (Anthropic) e a mesma alegação de adoção, mas não enumera adotantes no próprio README — remete ao Client Showcase do site.

> Fonte: <https://github.com/agentskills/agentskills> · consultada em 13/09/2026 · **CONFIRMADO** (quanto à origem/manutenção; a lista de adotantes está no site, não no README)

### Cruzamento contra os itens 2, 3 e 4 — o teste que realmente importa

A pergunta não é o que agentskills.io afirma sobre os outros. É o que **a documentação oficial de cada um desses outros fornecedores** afirma sobre si mesma. Já verificado nesta sessão:

- **Cursor** (`cursor.com/docs/context/skills`, seção 2 acima): "Agent Skills is an open standard. Learn more at agentskills.io." — citação direta, nome do padrão, link para o domínio.
- **OpenAI / Codex CLI e ChatGPT** (`learn.chatgpt.com/docs/build-skills`, redirecionada de `developers.openai.com/codex/skills`, seção 3 acima): "Skills build on the open agent skills standard," com link para agentskills.io e para `agentskills.io/specification`.
- **Google Antigravity** (`antigravity.google/docs/ide/skills` e `.../docs/skills/`, seção 4 acima): "Skills are an open standard for extending agent capabilities," com link para `agentskills.io/home`.
- **Gemini CLI** (`github.com/google-gemini/gemini-cli/blob/main/docs/cli/skills.md`, seção 5a acima): "Based on the Agent Skills open standard," com link para agentskills.io, na documentação do próprio repositório mantenedor.
- **GitHub Copilot / VS Code** (seção 6 acima): a página do GitHub nomeia "an open standard" e linka o repositório do padrão; a página específica do VS Code linka agentskills.io diretamente.

Em nenhum dos cinco casos a citação veio só do lado do agentskills.io — em todos os cinco, foi a própria documentação oficial do fornecedor, aberta nesta sessão, que citou o nome do padrão e apontou para ele.

**Veredito:** CONFIRMADO. O padrão aberto Agent Skills é real, mantido (github.com/agentskills/agentskills), originado pela Anthropic, e — isto é o que a missão pediu para ser dito sem ambiguidade — **não é uma convenção de pasta compartilhada por acidente**. Cursor, OpenAI (Codex CLI e ChatGPT), Google Antigravity, Gemini CLI e GitHub Copilot/VS Code cada um documenta, na própria fonte oficial, a adoção nomeada do padrão, com link direto para agentskills.io ou para o repositório do padrão. A única ressalva que sobrevive é de manutenção do site (Antigravity ausente do Client Showcase, aparentemente por atraso de atualização da lista, não por ausência de adoção real).

---

## Tabela-resumo final

| # | Item | Veredito | Caminho/arquivo de convenção real, segundo a fonte oficial |
|---|---|---|---|
| 1 | Claude Code | **CONFIRMADO** | `~/.claude/skills/<nome>/SKILL.md` · `.claude/skills/<nome>/SKILL.md` · `<plugin>/skills/<nome>/SKILL.md` · `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json` · `/plugin marketplace add` · `/plugin install` |
| 2 | Cursor | **CONFIRMADO** | `.cursor/skills/` e `.agents/skills/` (projeto) · `~/.cursor/skills/` e `~/.agents/skills/` (pessoal) · `AGENTS.md` na raiz como alternativa a `.cursor/rules/*.mdc` |
| 3 | OpenAI Codex CLI | **CONFIRMADO** | `AGENTS.md` hierárquico (`~/.codex/AGENTS.md` → raiz do git → cwd) · skills em `.agents/skills/` (`$CWD`, `$CWD/..`, `$REPO_ROOT`, `$HOME`) |
| 4 | Google Antigravity | **PARCIAL** | Projeto: `.agents/skills/<nome>/SKILL.md` (consistente). Pessoal/global: inconsistente entre três páginas oficiais (`~/.gemini/antigravity/skills/`, `~/.gemini/config/skills/`, `~/.gemini/antigravity-cli/skills/`) — não usar sem reconferir antes de publicar |
| 5a | Gemini CLI | **CONFIRMADO**, com alerta | `GEMINI.md` (contexto) · `.gemini/skills/` ou `.agents/skills/` (projeto) · `~/.gemini/skills/` ou `~/.agents/skills/` (pessoal). Alerta: produto standalone descontinuado para contas free/Pro/Ultra desde 18/06/2026, substituído pela Antigravity CLI |
| 5b | Gemini (chat comum) | **PARCIAL** | Nenhum caminho de arquivo confirmado; só instrução colada manualmente + arquivos de conhecimento anexados a um Gem |
| 6 | VS Code (extensão GitHub Copilot) | **CONFIRMADO** | `.github/copilot-instructions.md` (clássico) · `.github/skills/`, `.claude/skills/`, `.agents/skills/` (projeto, Agent Skills) · `~/.copilot/skills/`, `~/.agents/skills/` (pessoal, Agent Skills). Extensão do Claude Code dentro do VS Code: ver item 1 |
| 7 | Padrão aberto "Agent Skills" (agentskills.io) | **CONFIRMADO** | Mantido em `github.com/agentskills/agentskills`, originado pela Anthropic. Adoção nomeada e documentada, na própria fonte oficial de cada um, por Cursor, OpenAI/Codex, Google Antigravity, Gemini CLI e GitHub Copilot/VS Code — não é convenção de pasta por acidente |

---

*Todas as URLs acima foram efetivamente abertas nesta sessão em 13 de setembro de 2026, via WebSearch para localizar e WebFetch para ler o conteúdo, conforme o protocolo de `AGENTS.md` deste repositório. Nenhuma afirmação de veredito acima se apoia em memória de treinamento não verificada nesta sessão.*
