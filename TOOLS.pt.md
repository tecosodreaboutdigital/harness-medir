*Leia em [English](TOOLS.md) · [Español](TOOLS.es.md).*

# Ferramentas e skills usadas neste projeto

Registro do que este projeto de fato instalou e usa, não só do que cita. Um projeto sobre engenharia de harness que não instrumentasse a própria criação seria só um argumento bonito. Este documento é a instrumentação.

Atualizado em 30 de agosto de 2026. Cresce a cada skill nova que entra em uso, nunca é reescrito por inteiro.

---

## Coleções de terceiro instaladas

Seis coleções, trinta e uma skills, todas com licença MIT ou Apache 2.0. Instaladas localmente em `.claude/skills/`, fora do controle de versão (ver `.gitignore`): rodam neste ambiente, mas o código de terceiro não entra no histórico público deste repositório. Cada uma é citada como uma ficha no [guia compacto](harness-toolkit.html). Some `intake-briefing`, a skill própria do projeto tratada na próxima seção, e o ambiente tem 32 skills ativas ao todo.

| Coleção | Origem | Skills instaladas | Por que entrou |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, a coleção inteira | É o padrão de regra inegociável mais bandeiras vermelhas que `STANDARDS.md` já adota como padrão de escrita de skill deste projeto |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, seleção curada | Skills de escrita, clarificação e handoff de sessão. O conjunto de engenharia de software da coleção (TDD, arquitetura de código, merge conflict, TypeScript) ficou de fora por não se aplicar a um projeto de conteúdo, ver a lista completa abaixo |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, a coleção inteira | O modelo C4 e registro de decisão de arquitetura, relevante para a rodada de pesquisa da parte 3 |
| Guia inspirado em Karpathy | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | Guia comportamental contra erros comuns de LLM. Não é de fato do Karpathy, ver a ressalva completa em `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | Fonte real da matriz de cinco regras de limpeza citada na seção Reforçar da parte 2 |
| impeccable | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1 | Referência de QA de design para as próprias páginas HTML do projeto: 61 regras determinísticas de detector para tiques comuns de frontend gerado por IA, Apache-2.0, 30 contribuidores. Instalada só como documentação, ver a ressalva abaixo |

---

## As trinta e uma skills, por coleção

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (a pasta de origem chama essa skill de `c4designer`, mas o próprio cabeçalho interno do `SKILL.md` declara o nome `c4-model`; renomeamos a pasta local para bater com o nome declarado).

**Guia inspirado em Karpathy:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

**impeccable:** impeccable. **Instalação parcial, dita com honestidade:** copiamos `SKILL.md` e todo arquivo sob `reference/`, nada sob `scripts/`. O próprio cabeçalho da skill original lista `Bash(npx impeccable *)` e `Bash(node .../scripts/*)` como ferramentas permitidas, ligadas a 61 regras determinísticas de detector que precisam desses scripts para rodar sem LLM. Sem eles, `/impeccable audit` e os comandos irmãos ainda funcionam como crítica guiada por LLM contra as mesmas regras escritas, só sem o passe determinístico sem LLM. Toda outra skill desta página é markdown puro por natureza; impeccable é a primeira em que escolhemos deixar código para trás de propósito, exatamente porque o próprio checklist "antes de instalar qualquer coisa" do guia compacto (ver abaixo) trata um script não revisado que chama o sistema como um custo real, não um upgrade de graça.

---

## A skill própria do projeto

`intake-briefing` é criada por este projeto, não instalada de terceiro. Vivia como subpasta aqui dentro até 30 de agosto de 2026, quando ganhou repositório próprio, público, MIT, no mesmo dia: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renomeada de `levantando-briefing` mais tarde nesse mesmo dia, como parte da reestruturação para inglês primário). O harness-medir não guarda mais o conteúdo dela, só aponta para lá, no mesmo padrão que usa para apontar para as outras cinco coleções desta página.

Ela também não estava ativa neste ambiente até esta rodada: `.claude/skills/`, que é de onde este harness descobre skills de projeto, só tinha as trinta de terceiro. Corrigido: uma cópia dela vive em `.claude/skills/intake-briefing/`, fora do controle de versão, trazida do repositório próprio.

**Risco assumido, dito com honestidade:** essa cópia local pode ficar para trás se o repositório da skill for editado sem que a cópia aqui seja atualizada. É o mesmo tipo de risco que aceitamos para as trinta skills de terceiro, agora também para a nossa. Já aconteceu uma vez: o repositório ganhou `AGENTS.md`, `llms.txt`, `.claude-plugin/` e `briefings/`, mais uma seção `Installation` multiferramenta reescrita, em 31 de agosto de 2026, enquanto essa cópia local ainda carregava o retrato de 30 de agosto. Ressincronizada no mesmo dia; ver a própria seção `Instalação` do `README.md` para o detalhe multiferramenta que saiu dessa rodada.

---

## Auditoria antes de instalar

Aplicamos o próprio checklist do guia compacto, a seção "Antes de instalar qualquer coisa": ler o conteúdo, procurar instrução mandando o sistema buscar algo em rede externa, conferir a licença antes de decidir.

Uma varredura por padrões de rede ou execução (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) nas cinco fontes não encontrou nenhuma instrução automática de busca externa. Os únicos acertos foram um exemplo de código didático (um `fetch` simulado numa skill de teste do mattpocock/skills) e execução local legítima (`execFileSync` do superpowers, para renderizar um diagrama Mermaid em SVG, sem rede envolvida). Nenhuma das cinco fontes exigiu dependência externa não declarada para funcionar como skill isolada.

O impeccable foi auditado à parte, porque o repositório inteiro tem outro formato: um CLI de npm mais scripts de detector injetados no navegador, não uma skill em markdown puro. Lemos a árvore de `scripts/` antes de decidir, em vez de rodar `npx impeccable install` primeiro e ler depois. Ele chama Node e, para o detector visual, um navegador headless, ambos declarados abertamente no próprio `allowed-tools` do `SKILL.md`, não escondidos. Optamos por não instalar nada disso: a cópia em `.claude/skills/impeccable/` é só `SKILL.md` e `reference/`, ver a ressalva na tabela de coleções acima.

---

## Uma observação sobre o ambiente

Duas dessas coleções, superpowers e o guia inspirado em Karpathy, já estavam disponíveis globalmente neste ambiente antes desta instalação, provavelmente via um plugin já configurado na máquina. Instalamos a cópia local do projeto mesmo assim, de propósito: o objetivo é que o trabalho deste projeto continue reproduzível em qualquer máquina que clone o repositório e instale as mesmas trinta skills, sem depender do que está configurado globalmente numa máquina específica.

---

## Registro de uso real

Esta seção é o que separa "instalado" de "usado", e é a que mais vai crescer. Cada entrada nomeia a skill, o artefato que ela ajudou a produzir, e a data.

*Nenhum uso registrado no primeiro dia além da instalação em si, feita em 30 de agosto de 2026. Todo o trabalho deste projeto até aqui (o repositório, a reescrita do guia compacto, a tradução da parte 2, a reestruturação para inglês primário nos dois repositórios) foi feito com as ferramentas nativas do harness, sem nenhuma destas trinta skills.*

**`research`, 31 de agosto de 2026.** Usada diretamente, repetidamente, em escala real, nas duas rodadas de correção de citação do dia e na rodada posterior de pesquisa adversarial sobre as Partes 3 e 4: pesquisar uma afirmação contra fontes primárias reais e salvar os achados como um arquivo markdown, não um resumo de chat que desaparece quando a sessão termina. Se saiu bem toda vez, saída consistentemente bem fundamentada, salva num local sensato. Uma ineficiência real registrada em vez de escondida: a própria instrução de subir um agente de fundo soma uma camada redundante de delegação quando invocada de dentro de uma chamada que já é um agente de fundo. Agora citada por conta própria na seção Inspecionar do guia compacto, fechando a lacuna que o item 4 do `NEXT-STEPS.md` nomeou: estar instalada e auditada no nível da coleção não é a mesma alegação que estar individualmente verificada e citada.

---

## Onde isso aparece

Rodapé de `harness-p1.html`, `harness-p2.html` e `harness-toolkit.html`, nos três idiomas onde a peça é trilíngue. E no [diário de bordo](docs/logbook.html), trilíngue, com o detalhamento por marco, gerado a partir do git e do registro real de uso da sessão, nunca editado à mão.
