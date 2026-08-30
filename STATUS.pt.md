*Leia em [English](STATUS.md) · [Español](STATUS.es.md).*

# Estado

Situação em 30 de agosto de 2026.

Publicado em `github.com/tecosodreaboutdigital/harness-medir` (repositório) e `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, os arquivos HTML renderizam como página, não só como código-fonte).

---

## Pronto

### Reestruturação para inglês primário

O inglês se tornou o idioma de produção primário deste projeto nos dois repositórios públicos em 30 de agosto de 2026, decisão tomada no meio do caminho de um projeto que até então era primeiro-português. Todo documento de governança, o guia compacto e a skill de briefing foram renomeados e reescritos com o inglês na frente, com português e espanhol como traduções completas, e não o caminho inverso. Ver a seção Idiomas de `STANDARDS.md` para a regra em si.

Mecanicamente: `PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`, `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, além dos scripts e arquivos de dados correspondentes em `build/`. Toda referência cruzada nos dois repositórios foi varrida e corrigida, incluindo as URLs absolutas de blob do GitHub que apontavam para os antigos nomes de arquivo de governança e as âncoras prefixadas por idioma que ligam a Parte 2 ao guia compacto. As descrições de commit históricas dentro do diário do projeto foram deliberadamente mantidas citando os nomes de arquivo antigos onde isso era literalmente verdade no momento daquele commit, com uma nota acrescentada onde a renomeação posterior precisava ser reconhecida, para que o diário permaneça um registro fiel, e não um registro arrumado retroativamente.

As peças trilíngues já completas (`harness-p1.html`, `harness-p2.html`, `docs/logbook.html`) tiveram a aba padrão trocada de português para inglês: o atributo `<html lang>`, o botão ativo da barra de idioma e qual `<main>` fica oculto, tudo mudou, tanto nos arquivos já montados quanto nos scripts de montagem que os regeneram, para que uma nova montagem não reverta silenciosamente ao padrão em português.

Uma dica de idioma do navegador foi acrescentada às quatro páginas HTML trilíngues: se o idioma do navegador do visitante for português ou espanhol e ainda não corresponder à aba ativa, e nenhum link explícito com prefixo de idioma estiver roteando a página, um pequeno banner dispensável oferece a troca, redigido nesse idioma. Qualquer outro idioma de navegador cai para o inglês sem banner. O GitHub não executa JavaScript dentro do Markdown renderizado, então os doze arquivos do repositório da skill carregam, em vez disso, uma linha estática de navegação de idioma no topo de cada um.

### Diário de bordo

`docs/logbook.html`, trilíngue. Documenta a evolução do próprio projeto: palavras publicadas e tokens consumidos por marco, gerado a partir do git e do transcript real da sessão, nunca escrito à mão. Ver `build/generate_logbook_metrics.py` e `build/build_logbook.py`. Seis marcos registrados até aqui a partir do histórico completo do repositório, mais o que ainda está em sessão aberta.

### Parte 1 · O melhor modelo do mundo dentro de uma empresa sem processo

`harness-p1.html`

Trilíngue completa, treze seções mais o bloco de navegação, três diagramas, 26 verbetes de glossário. Cerca de 4.700 palavras em português, 4.500 em inglês, 4.700 em espanhol.

Conteúdo: cena de abertura com a diretora, o que é um harness, a analogia da delegação, a linhagem histórica com correção da atribuição do termo, quatro estudos de caso com números, o ciclo MEDIR, a tabela de equivalências com o vocabulário de qualidade, as faixas N0 a N3, riscos em nível de conselho, checklist de doze perguntas.

Barra de série e bloco "Onde você está" já implementados.

### Parte 2 · Guias e sensores: como um agente aprende a se corrigir

`harness-p2.html`

Trilíngue completa desde 30 de agosto de 2026. Dezessete seções, três diagramas, 26 verbetes de glossário por idioma. Cerca de 6.200 palavras em português, 6.350 em inglês, 6.450 em espanhol.

Reescrita por completo depois de uma primeira versão descartada. A versão descartada falhava por abandonar a personagem, não fazer histórico da parte 1, e organizar por conceito em vez de pelo ciclo.

Conteúdo: abre na quarta semana com a diretora tendo escrito o guia inteiro e o sistema liberando a nota de um fornecedor descredenciado. Seções ancoradas em Equipar, Delegar e Inspecionar, com Reforçar no fim. Inclui a matriz de guias e sensores, a comparação entre uma mensagem de erro que ensina e um alarme, o truque do limiar, a unidade de durabilidade, três exemplos completos com um SKILL.md real, as classes de ambiente cruzadas com as faixas, e a limpeza como cadência.

Tradução ao inglês em grafia britânica, ao espanhol por "tú". MEDIR e harness mantidos como nomes próprios nos três idiomas, conforme `STANDARDS.md`. Os exemplos de skill (nomes de arquivo, campos, valores) também foram traduzidos, não só a prosa ao redor.

O JavaScript de troca de idioma da parte 1 e da parte 2 ganhou roteamento por âncora: um link como `harness-p1.html#en-opening` agora seleciona a aba certa antes de rolar, em vez de sempre abrir na aba padrão. Sem esse ajuste, um leitor em inglês clicando em qualquer referência cruzada para a parte 1 sempre caía em português.

### Skill intake-briefing

`github.com/tecosodreaboutdigital/intake-briefing`, repositório próprio desde 30 de agosto de 2026, renomeada de `levantando-briefing` nesse mesmo dia, como parte da reestruturação para inglês primário ("levantando" era um verbo comum em português, não um nome próprio estabelecido como MEDIR e harness são). Artefato original do projeto, completo, publicado, MIT. Quatro arquivos, cada um com uma tradução em português e espanhol ao lado: `SKILL.md`, `interview-script.md`, `briefing-template.md`, `README.md`.

Decide se a automação deve existir, antes de discutir como ela funciona. Oito blocos, uma tabela determinística de derivação de faixa, um veredito com três opções incluindo não fazer, e versionamento com comparação bloco a bloco.

Preenche uma lacuna verificada: existe farto material sobre como especificar bem, quase nada sobre como decidir se vale a pena.

Separada do monorepo harness-medir para instalação independente, no mesmo padrão das demais skills citadas no guia compacto. Ativa neste ambiente via cópia local em `.claude/skills/intake-briefing/`, fora do controle de versão, ver `TOOLS.md`.

### Guia compacto de ferramentas e skills

`harness-toolkit.html`

Reescrito por completo em 30 de agosto de 2026, e traduzido para inglês e espanhol no mesmo dia como parte da reestruturação de idioma, com inglês como aba padrão. Organizado pelos cinco passos do MEDIR, não por categoria de produto. Dezoito fichas de seis campos, mais uma seção de diagnóstico de faixa no início para quem chega da parte 1. Cada passo do MEDIR carrega uma crítica registrada, não só uma recomendação. A décima oitava, `impeccable`, foi adicionada ao Inspecionar depois, quando o projeto passou a também curar ferramentas de QA de design, ver `TOOLS.md`.

Distribuição: Mapear com quatro fichas (intake-briefing, um guia inspirado em Karpathy, c4-skills, especificação antes do código com a crítica de Böckeler e Pocock), Equipar com três (superpowers, mattpocock/skills, planning-with-files), Delegar com três (holdfast, classes de ambiente, orquestração programada com LangGraph), Inspecionar com quatro (dependency-cruiser, Stryker, Semgrep, sensors-cli), Reforçar com três (ai-slop-cleaner, limpeza como cadência, coleta de lixo).

Toda ferramenta citada está verificada em `sources/inventory.md`, incluindo três fontes acrescentadas nesta reescrita: Semgrep, LangGraph e GitHub Spec Kit com link direto.

Repositório publicado e público, em `github.com/tecosodreaboutdigital/harness-medir`.

---

## Não iniciado

### Parte 3 · Governança de agentes

Escopo definido, base de pesquisa fraca. É a peça de maior valor comercial e a de fundação mais rasa.

Escopo: permissão imposta fora do modelo, instrução maliciosa que chega dentro de um dado ou de uma skill de terceiro, registro auditável, reversão, obrigações legais, e quem responde pelo que o agente fez.

O que ainda falta pesquisar, e é rodada dedicada, não complemento: literatura de segurança de agentes, incidentes reais documentados, a posição da autoridade brasileira de proteção de dados sobre decisão automatizada, obrigações regulatórias europeias para sistemas classificados como de alto risco, e o que já existe de padrão de auditoria de agentes.

Escrever agora produziria opinião bem escrita, não referência.

### Estado das traduções

| Peça | PT | EN | ES |
|---|---|---|---|
| Parte 1 | pronta | pronta | pronta |
| Parte 2 | pronta | pronta | pronta |
| Guia compacto | pronta | pronta | pronta |
| Parte 3 | falta | falta | falta |
| Skill de briefing | pronta | pronta | pronta |
| Documentos de governança | pronta | pronta | pronta |

### Playbook

Consolidação das três partes mais o guia, acrescentando o que ainda não existe: um modelo de contrato de tarefa, um modelo de skill, um modelo de recibo de execução, uma matriz de risco, um diagnóstico de faixa e uma trilha de implantação.

A skill de briefing já é o primeiro artefato operacional dele.

---

## Decisões tomadas que não devem ser revertidas sem motivo

**O inglês é o idioma de produção primário deste projeto, decisão tomada em 30 de agosto de 2026,** para os dois repositórios públicos, mesmo que a conversa de trabalho com o autor continue em português. Ver a seção Idiomas de `STANDARDS.md`.

**O termo harness não é traduzido.** Mantido em inglês pela mesma razão que ninguém traduziu kaizen, kanban ou poka-yoke. As alternativas arnês, arreio, cabresto e sela (equivalentes aproximados em português que evocam contenção) foram descartadas: uma metáfora de contenção vende a ideia errada para um leitor que já teme perder o controle.

**A atribuição correta do termo é Mitchell Hashimoto, fevereiro de 2026,** não Andrej Karpathy. Karpathy cunhou vibe coding e popularizou context engineering, e o nome dele aparece corretamente nesses contextos.

**Inspecionar, e não Instrumentar, para o passo I.** Instrumentar é tecnicamente mais preciso e coerente com o argumento de que qualidade não se inspeciona no fim da linha, mas Inspecionar é o termo do repertório do próprio autor e a sigla depende dele.

**Exemplos na escada indivíduo, equipe, área.** Não usar "empresa" nem um nível acima de área.

**A cena de abertura é composta,** não real, e isso é declarado no rodapé de cada peça. Se surgir um caso real anonimizado do ecossistema do autor, substituí-la melhoraria bastante o texto.

**O guia compacto vive separado dos artigos,** com data de revisão visível, porque envelhece mais rápido.

**O repositório da skill é renomeado para intake-briefing, e não mantido como levantando-briefing.** Diferente de harness e MEDIR, "levantando" nunca foi estabelecido como nome próprio que o leitor precisasse aprender, era simplesmente o verbo em português para a função da skill, por isso ele se traduz em vez de ficar fixo.
