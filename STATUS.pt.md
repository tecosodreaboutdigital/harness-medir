*Leia em [English](STATUS.md) · [Español](STATUS.es.md).*

# Estado

Situação em 30 de agosto de 2026.

Publicado em `github.com/tecosodreaboutdigital/harness-medir` (repositório) e `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, os arquivos HTML renderizam como página, não só como código-fonte).

**Proteção de branch na `main`, configurada em 30 de agosto de 2026.** Definida direto pela API do GitHub: pull request é exigido pra mergear, pelo menos uma aprovação é exigida, uma aprovação é descartada se um commit novo chegar antes do merge, force push e exclusão da branch estão bloqueados. `enforce_admins` foi deliberadamente deixado desligado, então o fluxo de push direto do dono do repositório na `main` continua funcionando sem mudança. O efeito real da regra é sobre qualquer contribuição futura vinda de um fork: precisa ser revisada e mergeada à mão, nunca automaticamente, o que já era verdade na prática (`allow_auto_merge` já era `false`, e nenhum colaborador além do dono tem acesso de escrita), mas agora é imposto pelo próprio GitHub, não só por convenção.

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

### Parte 3 · A separação de poderes: o que ele pode fazer, e quem responde por isso

`harness-p3.html`

Trilíngue por completo desde 30 de agosto de 2026. Nove seções, cinco diagramas, todos embutidos e traduzidos por completo. Cerca de 5.131 palavras em inglês, 5.468 em português, 5.676 em espanhol, contagens próximas entre os três, como se espera de uma tradução de verdade e não um resumo.

Abre com Moffatt contra Air Canada, 2024 BCCRT 149: uma empresa real argumentou em um tribunal real que o chatbot dela era uma pessoa legal separada que responde sozinha, e perdeu, declarado explicitamente como precedente estrangeiro, não brasileiro. A diretora reentra em N2, a uma extensão pequena de recurso de distância de uma resposta não autorizada que teria comprometido a empresa, o eco direto do próprio erro da Air Canada. Tese central: o modelo propõe, a política autoriza, a ferramenta executa, o registro testemunha, quatro funções que não podem morar no mesmo lugar, com o modo de falha nomeado, concentração. A regra de dois (dado privado, conteúdo não confiável, comunicação externa, no máximo duas sem humano no laço) serve de ferramenta operacional da peça, o equivalente da matriz de guias e sensores da parte 2, ao lado de uma matriz geral de alçada baseada em reversibilidade. Identidade ganha dono nomeado e a distinção entre delegação em nome de e autônoma; injeção é tratada como arquitetura, não configuração; um ponto de reversão registrado antes da execução, não depois, ancora o que precisa estar no registro; o risco de cadeia de suprimento de uma skill de terceiro fecha o gancho que a parte 2 deixou aberto; obrigações legais correm em duas colunas, Brasil (artigo 20 da LGPD, datado como ainda não regulamentado especificamente) e Europa (artigos 12, 14 e 26 do AI Act europeu). As duas obrigações de honestidade que a pesquisa sinalizou são honradas no texto: a origem estrangeira do precedente Air Canada, e a afirmação datada sobre a regulamentação brasileira.

Barra de série e links de glossário e fontes já implementados, conforme a arquitetura compartilhada acima.

### Parte 4 · O escritório de agentes: quantos existem, quem é dono de cada um, e quais ainda se pagam

`harness-p4.html`

Totalmente trilíngue desde 31 de agosto de 2026. Nove seções, cinco diagramas (D6 a D10, o D10 renderizado agora para esta peça, ver `diagrams/README.md`), todos embutidos e traduzidos por completo, incluindo cada rótulo de SVG, conferido renderizando cada diagrama isolado nas três línguas antes de incorporá-lo ao artigo, sem estouro, sem sobreposição. Cerca de 6.889 palavras em inglês, 7.051 em português, 7.377 em espanhol, contagens próximas nas três línguas, como se espera de uma tradução de verdade, não de um resumo.

Abre com as 20.225 contas do Instagram tomadas entre 17 de abril e 31 de maio de 2026 por meio de uma única interação mediada por IA que combinou gestão de identidade e recuperação de credencial, o modo de falha por concentração da parte 3 em escala populacional, e não numa única ação. A diretora reentra tocando seis sistemas que todo mundo chama de agente e não consegue responder a pergunta mais simples de um conselheiro: quantos são, e quem é dono de cada um. Tese central: o ciclo de vida do agente, seis estados e não passos, distinguido do MEDIR de forma explícita, com as duas transições que quase ninguém implementa, homologação vencida e sem execução no período, ambas levando ao descomissionamento e ambas exigindo decisão humana, nunca automação. Quatro papéis sob uma regra de não acumulação espelham a separação de poderes da parte 3 no plano organizacional, com fonte nova nesta rodada, o Modelo das Três Linhas do Instituto dos Auditores Internos, adotado em 2013. Oito indicadores são declarados explicitamente como síntese, não padrão de mercado, com o indicador de reprovação no portão ancorado na decisão do caso SCHUFA (TJUE, processo C-634/21, dezembro de 2023), exatamente como funciona o fundamento jurídico da parte 3, o fio que amarra as duas peças. Onde o escritório fica busca o precedente da linha de reporte do CISO, com fonte num levantamento de 2026 e a citação do brigadista de incêndio e os aspersores. A restrição explícita atravessa a peça inteira: tudo que ela propõe precisa funcionar numa empresa com sete agentes e uma planilha, ilustrada por uma descrição genérica e sem atribuição do que os painéis de agente de hoje já fazem e as cinco lacunas além desse piso. Fecha com o arco da diretora ao longo das quatro partes e a tabela de fechamento própria da série.

Dez verbetes de glossário acrescentados nesta rodada (escritório de agentes, dono do agente, homologador, patrocinador da área, regra de não acumulação, ciclo de vida, matéria escura de identidade, Heinrich, custo por tarefa concluída, Modelo das Três Linhas), nos três idiomas, em ordem alfabética; corrigi-los também consertou cinco bugs de alfabetização preexistentes no glossário em português e um no espanhol, resquício de uma rodada anterior que traduziu termos sem reordená-los. `harness-sources.html` ganhou uma seção da parte 4, 32 fontes incluindo a decisão primária do TJUE ainda não localizada, na mesma marcação V ou P da parte 3.

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

### Preparação das partes 3 e 4

`sources/inventory.md`, `diagrams/`, `STANDARDS.md`, `README.md`, `STATUS.md`, `NEXT-STEPS.md`.

Segue o dossiê de trabalho `docs/harness-p3-p4-briefing.pt.md`, acrescentado em 30 de agosto de 2026 com um diagnóstico estrutural, sete eixos de pesquisa e uma especificação visual de nove diagramas, e completa os três primeiros itens da fila de trabalho dele, bloco D.

Os documentos de governança agora descrevem quatro partes organizadas em torno de um framework de três camadas, construção, operação, governança, atravessadas pelas faixas N0 a N3 como régua comum, em vez de três partes mais dois companheiros. `STANDARDS.md` ganhou uma seção `Diagramas`: todo diagrama nasce como especificação em Mermaid, o SVG inline deriva dele e nunca o substitui, na mesma regra que o próprio dossiê propôs.

`sources/inventory.md` ganhou uma seção nova, 32 fontes distribuídas nos sete eixos de pesquisa do dossiê mais o achado que reformula a abertura da parte 3, todas carregadas com o status V ou P original. Duas trazem uma nota explícita, não só uma letra de status, porque a lacuna que marcam muda o que a parte 3 pode afirmar: a publicação original da Meta sobre a regra de dois nunca foi lida na fonte primária, e o precedente Air Canada usado para abrir a peça é canadense, não brasileiro.

`diagrams/` ganhou nove arquivos SVG independentes, D1 a D9, renderizados a partir das especificações Mermaid do dossiê no sistema visual do projeto, em inglês porque é conteúdo novo e o inglês é escrito primeiro. O vocabulário de governança que a parte 4 precisou, dono do agente, homologador, auditor, patrocinador da área, e recibo mantido distinto de registro, foi fixado nesta etapa justamente para que os diagramas e a prosa não se afastassem um do outro. Um décimo, o D10, o laço trimestral do próprio escritório, foi acrescentado assim que a redação da parte 4 confirmou que ele merecia lugar, fechando a seção de indicadores em vez de abrir a peça. Ver `diagrams/README.md` para o índice completo e qual nota de renderização cada arquivo atende.

O que resta da fila do dossiê: a tradução da parte 4 para português e espanhol, e consolidar o playbook. As partes 3 e 4 já estão escritas em inglês, ver abaixo.

### Diagramas D1 a D9 validados por renderização, e uma arquitetura de série compartilhada

Fecha a ressalva que a rodada anterior tinha registrado: os nove SVGs independentes (`diagrams/part3/`, `diagrams/part4/`) nunca tinham sido de fato renderizados, só conferidos como XML bem formado. Agora foram, via Chrome headless, e conferidos visualmente. Cinco carregavam bugs reais de coordenada, todos corrigidos na fonte SVG, nenhum na especificação Mermaid por trás, já que nenhum dos cinco era estrutural: o `D3` tinha linhas de conexão saindo do centro de uma caixa e cortando o texto de caixas empilhadas abaixo, corrigido fazendo cada linha sair da borda da caixa mais próxima do destino; o `D4` carregava dois conectores sobrepostos no primeiro losango, um do tamanho certo sem seta, o outro com seta ultrapassando até o interior do losango, unificados num só; a legenda de fechamento do `D5` estourava 82 pixels o canvas de 700px; a linha mais grossa do `D7` cortava direto a caixa `IN OPERATION`, e uma curva cortava `UNDER REVIEW`, ambas rerroteadas, o canvas ganhando 24 pixels de altura; a terceira e a quarta coluna do `D9` se sobrepunham em 40 pixels, dobrando visivelmente uma borda tracejada. `D1`, `D2`, `D6` e `D8` não tinham bug nenhum. Cada SVG ganhou um `.png` correspondente (escala 2x, fundo branco opaco) para publicação no Medium, já que o editor do Medium não renderiza nem SVG inline colado nem HTML arbitrário.

Em paralelo, a série ganhou a navegação de topo que estava faltando desde a reestruturação para quatro partes: um componente único compartilhado `.topbar`, uma linha só, centralizado, fixo ao rolar, reativo ao seletor de idioma (`PARTE 1 · PARTE 2 · PARTE 3 · PARTE 4 | GUIA COMPACTO · GLOSSÁRIO · FONTES { PT EN ES }`, a página atual em texto simples e uma parte ainda não escrita esmaecida e sem link). Substitui uma barra que antes existia só em `harness-p1.html`, fixa em português independente da aba ativa, alinhada à esquerda, não fixa ao rolar. As seções de glossário e fontes que as partes 1 e 2 carregavam cada uma foram aposentadas em favor de duas páginas novas, compartilhadas e trilíngues, `harness-glossary.html` (56 verbetes consolidados, sem duplicata) e `harness-sources.html` (46 fontes consolidadas, agrupadas em fundadoras e parte 3), e todo link de termo e citação da série agora aponta pra lá. `harness-p1.html`, `harness-p2.html` e `harness-toolkit.html` foram retrofitados; `build_p2.py` e `build_toolkit.py` foram atualizados para reproduzir a mesma barra na próxima regeração, fechando a brecha em que um rebuild desfaria o conserto silenciosamente. Ver as seções `Navegação cruzada` e `Glossário` de `STANDARDS.md` para a regra que isso agora segue.

---

## Não iniciado

### Estado das traduções

| Peça | PT | EN | ES |
|---|---|---|---|
| Parte 1 | pronta | pronta | pronta |
| Parte 2 | pronta | pronta | pronta |
| Guia compacto | pronta | pronta | pronta |
| Parte 3 | pronta | pronta | pronta |
| Parte 4 | pronta | pronta | pronta |
| Skill de briefing | pronta | pronta | pronta |
| Documentos de governança | pronta | pronta | pronta |

### Playbook

Deliberadamente estacionado, fora do escopo da próxima sessão de conteúdo, decidido em 31 de agosto de 2026: as quatro partes são o argumento, o playbook é o ferramental derivado delas, e os dois não deveriam se confundir. O que ele vai conter, cada item rastreado até a parte que já o fundamenta, está registrado no item 3 de `NEXT-STEPS.md`, para que o plano sobreviva sem que ninguém precise reconstruí-lo de memória: um modelo de contrato de tarefa, um modelo de skill, um modelo de recibo de execução, uma matriz de risco por faixa, um diagnóstico de faixa, uma trilha de implantação de N0 a N3, e um modelo de registro de agentes mais ata de homologação. O D10, o laço próprio do escritório por trimestre, é candidato a abrir o documento, como uma segunda aparição legítima já que fecha a seção de indicadores da parte 4.

A skill de briefing já é o primeiro artefato operacional dele.

---

## Decisões tomadas que não devem ser revertidas sem motivo

**MEDIR continua escrito como uma palavra só, sem pontos entre as letras, decisão tomada em 31 de agosto de 2026.** O autor propôs `M.E.D.I.R.` para deixar a sigla mais clara logo no primeiro encontro. Considerado e deixado de lado: MEDIR também é o verbo comum medir, e só soa como essa palavra de verdade, pronunciável e perfeita tematicamente para um projeto sobre medir o comportamento de agentes, porque está escrita como uma palavra só. Letras separadas por ponto forçariam a leitura letra por letra e perderiam isso. Duas correções mais leves entraram no lugar, que resolvem o objetivo real (clareza desde o primeiro encontro, em qualquer peça que o leitor pouse primeiro) sem esse custo: a palavra MEDIR agora carrega a dica de glossário e o link padrão na primeira menção nas partes 2, 3, 4 e no guia compacto (antes não carregava, era o único verbete de glossário sem esse tratamento), e a parte 1 e o README dizem explicitamente, nas palavras do próprio leitor, que MEDIR é o verbo medir. Ver o verbete MEDIR em `harness-glossary.html` e a abertura de `README.pt.md`.

**O inglês é o idioma de produção primário deste projeto, decisão tomada em 30 de agosto de 2026,** para os dois repositórios públicos, mesmo que a conversa de trabalho com o autor continue em português. Ver a seção Idiomas de `STANDARDS.md`.

**O termo harness não é traduzido.** Mantido em inglês pela mesma razão que ninguém traduziu kaizen, kanban ou poka-yoke. As alternativas arnês, arreio, cabresto e sela (equivalentes aproximados em português que evocam contenção) foram descartadas: uma metáfora de contenção vende a ideia errada para um leitor que já teme perder o controle.

**A atribuição correta do termo é Mitchell Hashimoto, fevereiro de 2026,** não Andrej Karpathy. Karpathy cunhou vibe coding e popularizou context engineering, e o nome dele aparece corretamente nesses contextos.

**Inspecionar, e não Instrumentar, para o passo I.** Instrumentar é tecnicamente mais preciso e coerente com o argumento de que qualidade não se inspeciona no fim da linha, mas Inspecionar é o termo do repertório do próprio autor e a sigla depende dele.

**Exemplos na escada indivíduo, equipe, área.** Não usar "empresa" nem um nível acima de área.

**A cena de abertura é composta,** não real, e isso é declarado no rodapé de cada peça. Se surgir um caso real anonimizado do ecossistema do autor, substituí-la melhoraria bastante o texto.

**O guia compacto vive separado dos artigos,** com data de revisão visível, porque envelhece mais rápido.

**O repositório da skill é renomeado para intake-briefing, e não mantido como levantando-briefing.** Diferente de harness e MEDIR, "levantando" nunca foi estabelecido como nome próprio que o leitor precisasse aprender, era simplesmente o verbo em português para a função da skill, por isso ele se traduz em vez de ficar fixo.

**A série tem quatro partes, não três, organizadas em torno de três camadas, construção, operação, governança, atravessadas pela régua N0 a N3, decisão tomada em 30 de agosto de 2026.** Uma quarta camada foi considerada, para abrigar a própria régua, e descartada: N0 a N3 já cumpre esse papel, e um segundo eixo duplicaria vocabulário sem ganho. Ver `docs/harness-p3-p4-briefing.pt.md`.

**O vocabulário de governança da parte 4 é fixado antes da prosa:** dono do agente, homologador (o estado é homologado), auditor, patrocinador da área, e recibo mantido distinto de registro. Fixado na etapa de renderização dos diagramas, justamente para que os nove arquivos SVG em `diagrams/` e o texto futuro do artigo não se afastem um do outro.
