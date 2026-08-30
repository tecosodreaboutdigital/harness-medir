# Ferramentas e skills usadas neste projeto

Registro do que este projeto instalou e usa de fato, não só do que cita. Um projeto sobre engenharia de harness que não instrumenta a própria criação seria só um argumento bonito. Este documento é a instrumentação.

Atualizado em 30 de agosto de 2026. Cresce a cada skill nova que entrar em uso, nunca é reescrito por inteiro.

---

## Coleções de terceiro instaladas

Cinco coleções, trinta skills, todas as licenças MIT. Instaladas localmente em `.claude/skills/`, fora do controle de versão (ver `.gitignore`): rodam neste ambiente, mas o código de terceiro não entra no histórico público deste repositório. Cada uma citada como ficha no [guia compacto](harness-toolkit.html). Some a `levantando-briefing`, a skill própria do projeto tratada na seção seguinte, e o ambiente tem 31 skills ativas ao todo.

| Coleção | Origem | Skills instaladas | Por que entrou |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, a coleção inteira | É o padrão de regra inegociável mais bandeiras vermelhas que `STANDARDS.md` já adota como padrão de escrita de skill deste projeto |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, seleção curada | Skills de escrita, clarificação e handoff de sessão. O conjunto de engenharia de software da coleção (TDD, arquitetura de código, merge conflict, TypeScript) ficou de fora por não se aplicar a um projeto de conteúdo, ver a lista completa abaixo |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, a coleção inteira | Modelo C4 e registro de decisão de arquitetura, relevante para a rodada de pesquisa da parte 3 |
| Guia inspirado em Karpathy | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | Guia comportamental contra erros comuns de LLM. Não é do Karpathy, ver a ressalva completa em `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | Fonte real da matriz de cinco regras de limpeza citada na parte 2, seção Reforçar |

---

## As trinta skills, por coleção

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (a pasta de origem chama essa skill de `c4designer`, o cabeçalho interno do `SKILL.md` declara o nome `c4-model`; renomeamos a pasta local para bater com o nome declarado).

**Guia inspirado em Karpathy:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

---

## A skill própria do projeto

`levantando-briefing` não é instalada de terceiro, é criada por este projeto. Vivia como subpasta aqui dentro até 30 de agosto de 2026, e nesse mesmo dia ganhou repositório próprio, público, MIT: [github.com/tecosodreaboutdigital/levantando-briefing](https://github.com/tecosodreaboutdigital/levantando-briefing). O harness-medir não guarda mais o conteúdo dela, só aponta, no mesmo padrão que aponta para as outras cinco coleções desta página.

Ela também não estava ativa neste ambiente até esta rodada: `.claude/skills/`, que é de onde este harness descobre skill de projeto, só tinha as trinta de terceiro. Corrigido: uma cópia dela vive em `.claude/skills/levantando-briefing/`, fora do controle de versão, buscada do repositório próprio.

**Risco assumido, dito com honestidade:** essa cópia local pode ficar para trás se o repositório da skill for editado sem atualizar a cópia aqui. É o mesmo tipo de risco que aceitamos para as trinta skills de terceiro, agora também para a nossa.

---

## Auditoria antes de instalar

Aplicamos o próprio checklist que o guia compacto recomenda, seção "Antes de instalar qualquer coisa": lemos o conteúdo, procuramos instrução mandando o sistema buscar algo em rede externa, conferimos a licença antes de decidir.

Varredura por padrão de rede ou execução (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) nas cinco fontes: nenhuma instrução de busca externa automática. Os únicos acertos foram exemplo de código didático (mock de `fetch` numa skill de teste do mattpocock/skills) e execução local legítima (`execFileSync` do superpowers para renderizar diagrama Mermaid em SVG, sem rede). Nenhuma das cinco fontes exigiu dependência externa não declarada para funcionar como skill isolada.

---

## Uma observação sobre o ambiente

Duas destas coleções, superpowers e o guia inspirado em Karpathy, já estavam disponíveis globalmente neste ambiente antes desta instalação, provavelmente via plugin já configurado na máquina. Instalamos a cópia local do projeto mesmo assim, de propósito: o objetivo é que o trabalho deste projeto continue reproduzível em qualquer máquina que clone o repositório e instale as mesmas trinta skills, sem depender do que está configurado globalmente em uma máquina específica.

---

## Registro de uso real

Esta seção é a que separa "instalado" de "usado", e é a que mais vai crescer. Cada entrada nomeia a skill, o artefato que ela ajudou a produzir, e a data.

*Nenhum uso registrado ainda além da instalação em si, feita em 30 de agosto de 2026. Todo o trabalho deste projeto até aqui (repositório, reescrita do guia compacto, tradução da parte 2) foi feito com as ferramentas nativas do harness, sem nenhuma destas trinta skills. A partir de agora, todo uso real entra aqui antes de ser reivindicado em qualquer artigo.*

---

## Onde isso aparece

Rodapé de `harness-p1.html`, `harness-p2.html` e `harness-toolkit.html`, nos três idiomas onde a peça for trilíngue. E no [diário de bordo](docs/logbook.html), trilíngue, com o detalhamento por marco, gerado a partir do git e do registro real de uso da sessão, nunca editado à mão.
