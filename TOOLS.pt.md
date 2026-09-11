*Leia em [English](TOOLS.md) · [Español](TOOLS.es.md).*

# Ferramentas e skills usadas neste projeto

Registro do que este projeto de fato instalou e usa, não só do que cita. Um projeto sobre engenharia de harness que não instrumentasse a própria criação seria só um argumento bonito. Este documento é a instrumentação.

Atualizado em 10 de setembro de 2026. Cresce a cada skill nova que entra em uso, nunca é reescrito por inteiro.

---

## Coleções de terceiro instaladas

Dez coleções, trinta e sete skills, todas com licença MIT ou Apache 2.0. Instaladas localmente em `.claude/skills/`, fora do controle de versão (ver `.gitignore`): rodam neste ambiente, mas o código de terceiro não entra no histórico público deste repositório. As seis primeiras são citadas como ficha no [guia compacto](harness-toolkit.html); as quatro mais recentes ainda não, ver a nota ao final desta seção. Some `intake-briefing`, a skill própria do projeto tratada na próxima seção, e o ambiente tem 38 skills ativas ao todo.

| Coleção | Origem | Skills instaladas | Por que entrou |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, a coleção inteira | É o padrão de regra inegociável mais bandeiras vermelhas que `STANDARDS.md` já adota como padrão de escrita de skill deste projeto |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, seleção curada | Skills de escrita, clarificação e handoff de sessão. O conjunto de engenharia de software da coleção (TDD, arquitetura de código, merge conflict, TypeScript) ficou de fora por não se aplicar a um projeto de conteúdo, ver a lista completa abaixo |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, a coleção inteira | O modelo C4 e registro de decisão de arquitetura, relevante para a rodada de pesquisa da parte 3 |
| Guia inspirado em Karpathy | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | Guia comportamental contra erros comuns de LLM. Não é de fato do Karpathy, ver a ressalva completa em `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | Fonte real da matriz de cinco regras de limpeza citada na seção Reforçar da parte 2 |
| impeccable | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1 | Referência de QA de design para as próprias páginas HTML do projeto: 61 regras determinísticas de detector para tiques comuns de frontend gerado por IA, Apache-2.0, 30 contribuidores. Instalada só como documentação, ver a ressalva abaixo |
| humanizer | [github.com/blader/humanizer](https://github.com/blader/humanizer) | 1, a coleção inteira | Remove os tiques de prosa que soam a IA de um rascunho em inglês antes de ele se ramificar para português e espanhol. Nenhuma das outras nove coleções desta página chega a esse nível de detalhe, forma de frase e parágrafo, não vocabulário. Somada em 10 de setembro de 2026 a partir de uma lista de skills candidatas enviada por um leitor |
| Agent Skills for Context Engineering | [github.com/muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 3, de 17 | Um leitor apontou a arquitetura de harness de agente como uma lacuna real desta página. `harness-engineering`, `multi-agent-patterns` e `tool-design` fecham essa lacuna diretamente; as outras 14 skills (otimização de contexto, sistemas de memória, avaliação e mais) resolvem problemas adjacentes que este projeto não tem, ver a lista completa abaixo |
| ai-act-skill | [github.com/morellid/ai-act-skill](https://github.com/morellid/ai-act-skill) | 1, a coleção inteira | Checklist versionado, tarefa por tarefa, para as obrigações do AI Act europeu, já atualizado com o Digital Omnibus (Regulamento (UE) 2026/1744). As partes 3 e 4 já citam os artigos 12, 14 e 26 em prosa; esta é a primeira ferramenta do próprio kit deste projeto que transforma essa citação numa checagem executável |
| threat-modeling | [github.com/rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | 1, de uma coleção pessoal maior | Modelagem de ameaça baseada em STRIDE, com escopo em arquitetura de agente e revisão de segurança, não revisão pontual de diff. Instalação parcial: só a pasta desta skill entrou, não o resto do repositório |

---

## As trinta e sete skills, por coleção

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (a pasta de origem chama essa skill de `c4designer`, mas o próprio cabeçalho interno do `SKILL.md` declara o nome `c4-model`; renomeamos a pasta local para bater com o nome declarado).

**Guia inspirado em Karpathy:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

**impeccable:** impeccable. **Instalação parcial, dita com honestidade:** copiamos `SKILL.md` e todo arquivo sob `reference/`, nada sob `scripts/`. O próprio cabeçalho da skill original lista `Bash(npx impeccable *)` e `Bash(node .../scripts/*)` como ferramentas permitidas, ligadas a 61 regras determinísticas de detector que precisam desses scripts para rodar sem LLM. Sem eles, `/impeccable audit` e os comandos irmãos ainda funcionam como crítica guiada por LLM contra as mesmas regras escritas, só sem o passe determinístico sem LLM. Toda outra skill das seis primeiras coleções é markdown puro por natureza; impeccable é a primeira em que escolhemos deixar código para trás de propósito, exatamente porque o próprio checklist "antes de instalar qualquer coisa" do guia compacto (ver abaixo) trata um script não revisado que chama o sistema como um custo real, não um upgrade de graça.

**humanizer:** humanizer.

**Agent Skills for Context Engineering:** harness-engineering, multi-agent-patterns, tool-design. **Instalação parcial, dita com honestidade:** a coleção original tem 17 skills; copiamos só estas três pastas (`SKILL.md` mais os próprios `references/` e `scripts/`), porque as outras 14 (context-fundamentals, memory-systems, evaluation, self-improvement-loops e mais) resolvem problemas que este projeto não tem. `multi-agent-patterns` e `tool-design` carregam, cada uma, um pequeno auxiliar local em Python (`coordination.py`, `description_generator.py`); os dois usam só biblioteca padrão, auditados abaixo.

**ai-act-skill:** ai-act-skill. Instalação completa: `SKILL.md`, os seis arquivos de tarefa sob `tasks/`, e os trechos de referência e exemplos resolvidos que os sustentam. O `install.sh`, `uninstall.sh`, os scripts de release e os adaptadores entre ferramentas do próprio repositório original ficaram de fora: servem ao processo de empacotamento do autor, não à função desta skill dentro deste ambiente.

**threat-modeling:** threat-modeling. **Instalação parcial, dita com honestidade:** essa skill vive dentro de `rjmurillo/ai-agents`, uma coleção pessoal bem maior; só a pasta `threat-modeling` (`SKILL.md`, `references/`, `scripts/`, `templates/`) foi copiada. Os três scripts inclusos (`generate_threat_matrix.py`, `generate_mitigation_roadmap.py`, `validate_threat_model.py`) usam só biblioteca padrão, auditados abaixo.

---

## A skill própria do projeto

`intake-briefing` é criada por este projeto, não instalada de terceiro. Vivia como subpasta aqui dentro até 30 de agosto de 2026, quando ganhou repositório próprio, público, MIT, no mesmo dia: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renomeada de `levantando-briefing` mais tarde nesse mesmo dia, como parte da reestruturação para inglês primário). O harness-medir não guarda mais o conteúdo dela, só aponta para lá, no mesmo padrão que usa para apontar para as outras coleções desta página.

Ela também não estava ativa neste ambiente até esta rodada: `.claude/skills/`, que é de onde este harness descobre skills de projeto, só tinha as trinta de terceiro. Corrigido: uma cópia dela vive em `.claude/skills/intake-briefing/`, fora do controle de versão, trazida do repositório próprio.

**Risco assumido, dito com honestidade:** essa cópia local pode ficar para trás se o repositório da skill for editado sem que a cópia aqui seja atualizada. É o mesmo tipo de risco que aceitamos para as trinta e sete skills de terceiro, agora também para a nossa. Já aconteceu uma vez: o repositório ganhou `AGENTS.md`, `llms.txt`, `.claude-plugin/` e `briefings/`, mais uma seção `Installation` multiferramenta reescrita, em 31 de agosto de 2026, enquanto essa cópia local ainda carregava o retrato de 30 de agosto. Ressincronizada no mesmo dia; ver a própria seção `Instalação` do `README.md` para o detalhe multiferramenta que saiu dessa rodada.

---

## Auditoria antes de instalar

Aplicamos o próprio checklist do guia compacto, a seção "Antes de instalar qualquer coisa": ler o conteúdo, procurar instrução mandando o sistema buscar algo em rede externa, conferir a licença antes de decidir.

Uma varredura por padrões de rede ou execução (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) nas cinco fontes não encontrou nenhuma instrução automática de busca externa. Os únicos acertos foram um exemplo de código didático (um `fetch` simulado numa skill de teste do mattpocock/skills) e execução local legítima (`execFileSync` do superpowers, para renderizar um diagrama Mermaid em SVG, sem rede envolvida). Nenhuma das cinco fontes exigiu dependência externa não declarada para funcionar como skill isolada.

O impeccable foi auditado à parte, porque o repositório inteiro tem outro formato: um CLI de npm mais scripts de detector injetados no navegador, não uma skill em markdown puro. Lemos a árvore de `scripts/` antes de decidir, em vez de rodar `npx impeccable install` primeiro e ler depois. Ele chama Node e, para o detector visual, um navegador headless, ambos declarados abertamente no próprio `allowed-tools` do `SKILL.md`, não escondidos. Optamos por não instalar nada disso: a cópia em `.claude/skills/impeccable/` é só `SKILL.md` e `reference/`, ver a ressalva na tabela de coleções acima.

**Segunda rodada de auditoria, 10 de setembro de 2026.** Um leitor mandou uma lista de oito repositórios de skill candidatos e pediu uma comparação com esta página, mais uma busca por qualquer coisa que este projeto estivesse deixando passar em arquitetura de software, privacidade de dado e segurança da informação. Cinco agentes de fundo leram cada candidato diretamente (conteúdo bruto do arquivo, não o README de marketing) e cruzaram contra o que já estava instalado aqui. Dois dos oito já estavam cobertos: o guia inspirado em Karpathy já era exatamente essa mesma fonte, e uma skill de design de UI da lista batia com algo já ativo globalmente na máquina do operador, mas fora do escopo deste projeto. Quatro foram lidos e deixados de lado como só citação ou má escolha, incluindo um, Understand-Anything, que se instala com um comando `curl | bash` e traz um hook cujas próprias instruções mandam o agente não pedir confirmação ao usuário antes de agir, exatamente o padrão que este checklist existe para pegar. Os quatro restantes, humanizer, três skills do Agent Skills for Context Engineering, ai-act-skill e threat-modeling, passaram pela mesma varredura da primeira rodada (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`, mais `requests`, `urllib`, `subprocess` e `os.system` para as três fontes que trazem Python). A varredura achou um acerto: `sandbox.exec()` dentro de um exemplo de código de estudo de caso em `references/architectural_reduction.md` do `tool-design`, citando o próprio benchmark isolado de um terceiro, não uma instrução que esta skill executa. Nenhuma fonte desta rodada exigiu chamada de rede não declarada para funcionar.

**A citação no guia compacto está pendente para essas quatro.** As seis primeiras coleções foram instaladas e citadas em `harness-toolkit.html` na mesma sessão; esta rodada separou os dois passos de propósito, para o operador decidir sobre a instalação primeiro. Escrever as fichas de seis campos, nas três línguas, e sincronizar o espelho em `build/` fica registrado como um próximo passo à parte, não presumido pronto em silêncio.

---

## Uma observação sobre o ambiente

Duas dessas coleções, superpowers e o guia inspirado em Karpathy, já estavam disponíveis globalmente neste ambiente antes desta instalação, provavelmente via um plugin já configurado na máquina. Instalamos a cópia local do projeto mesmo assim, de propósito: o objetivo é que o trabalho deste projeto continue reproduzível em qualquer máquina que clone o repositório e instale as mesmas skills, sem depender do que está configurado globalmente numa máquina específica.

---

## Registro de uso real

Esta seção é o que separa "instalado" de "usado", e é a que mais vai crescer. Cada entrada nomeia a skill, o artefato que ela ajudou a produzir, e a data.

*Nenhum uso registrado no primeiro dia além da instalação em si, feita em 30 de agosto de 2026. Todo o trabalho deste projeto até aqui (o repositório, a reescrita do guia compacto, a tradução da parte 2, a reestruturação para inglês primário nos dois repositórios) foi feito com as ferramentas nativas do harness, sem nenhuma destas trinta skills.*

**`research`, 31 de agosto de 2026.** Usada diretamente, repetidamente, em escala real, nas duas rodadas de correção de citação do dia e na rodada posterior de pesquisa adversarial sobre as Partes 3 e 4: pesquisar uma afirmação contra fontes primárias reais e salvar os achados como um arquivo markdown, não um resumo de chat que desaparece quando a sessão termina. Se saiu bem toda vez, saída consistentemente bem fundamentada, salva num local sensato. Uma ineficiência real registrada em vez de escondida: a própria instrução de subir um agente de fundo soma uma camada redundante de delegação quando invocada de dentro de uma chamada que já é um agente de fundo. Agora citada por conta própria na seção Inspecionar do guia compacto, fechando a lacuna que o item 4 do `NEXT-STEPS.md` nomeou: estar instalada e auditada no nível da coleção não é a mesma alegação que estar individualmente verificada e citada.

---

## Onde isso aparece

Rodapé de `harness-p1.html`, `harness-p2.html` e `harness-toolkit.html`, nos três idiomas onde a peça é trilíngue. E no [diário de bordo](docs/logbook.html), trilíngue, com o detalhamento por marco, gerado a partir do git e do registro real de uso da sessão, nunca editado à mão.
