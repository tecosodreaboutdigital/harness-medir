*Leia em [English](NEXT-STEPS.md) · [Español](NEXT-STEPS.es.md).*

# Próximos passos

Em ordem. Cada item traz seu critério de pronto.

---

## Concluído em 30 de agosto de 2026

**Repositório GitHub público criado**, em `github.com/tecosodreaboutdigital/harness-medir`. Commit inicial com os 23 arquivos que existiam na época, sem dado sensível. LICENSE (MIT) acrescentada dentro do que então era `skills/levantando-briefing/`, coerente com o que o README da skill já declarava. Nenhuma licença na raiz, porque os artigos seguem todos os direitos reservados.

**Guia compacto reescrito por completo.** Ver a entrada correspondente em `STATUS.md` para o detalhamento. Critério de pronto cumprido: dezessete fichas de seis campos, toda ferramenta verificada em `sources/inventory.md` (três fontes novas verificadas nessa rodada: Semgrep, LangGraph, GitHub Spec Kit com link direto), e cada passo do MEDIR carregando uma crítica registrada.

**Parte 2 traduzida para inglês e espanhol**, no mesmo arquivo, com o seletor. `build/build_p2.py` reescrito para montagem trilíngue, no mesmo padrão que `build/build_all.py` já usava: extrai o corpo em PT do arquivo vigente (que é a fonte da verdade, não `build/body_p2_pt.html`, que estava desatualizado), monta EN e ES a partir de `build/body_p2_en.html` e `build/body_p2_es.html`, prefixa tudo por idioma via `scope()`. Os três botões funcionam e não há âncora quebrada. Como efeito colateral, o JavaScript de troca de idioma em `harness-p1.html` e `harness-p2.html` ganhou roteamento por âncora (`#en-opening` seleciona a aba certa antes de rolar), para que um link cruzado entre as peças em inglês ou espanhol não caísse sempre na aba em português.

**Trinta skills de terceiro instaladas para uso neste projeto**, cinco coleções (superpowers inteira, uma seleção curada de doze do mattpocock/skills, c4-skills inteira, o guia inspirado em Karpathy, ai-slop-cleaner), todas MIT, todas auditadas contra o próprio checklist do guia compacto antes de instalar. Vivem em `.claude/skills/`, fora do controle de versão. Documentação completa, com um registro de uso real que cresce a cada sessão, em `TOOLS.md`. Crédito visível no rodapé de `harness-p1.html`, `harness-p2.html` (três idiomas) e `harness-toolkit.html`.

**A skill separada em repositório próprio**, no que então era `github.com/tecosodreaboutdigital/levantando-briefing`, público, MIT, no mesmo padrão das demais skills citadas no guia compacto. Removida de `skills/` dentro do harness-medir, que agora só aponta para lá.

**Diário de bordo criado**, `docs/logbook.html`, trilíngue, gerado em duas etapas: `build/generate_logbook_metrics.py` reconstrói a série real (palavras publicadas por `git show` em cada commit, linhas em `build/` e nos documentos de governança, tokens somados do `usage` real de cada mensagem no transcript `.jsonl` da sessão, atribuídos ao commit cronologicamente seguinte) e escreve `docs/assets/logbook-metrics.json`; `build/build_logbook.py` monta a página a partir desse JSON, nunca escrita à mão. Dois gráficos SVG empilhados, mesmo eixo X, sem eixo Y duplo. Seis marcos reais registrados (o histórico completo do repositório até aqui, não uma amostra), mais o que ainda não tinha fechado marco.

**GitHub Pages ativado**, publicando o repositório em `tecosodreaboutdigital.github.io/harness-medir`. `.nojekyll` acrescentado para servir os arquivos HTML como estão, sem processamento Jekyll. Sem isso, nenhum artigo era de fato legível como página na web ali, só como código-fonte no visualizador do GitHub.

**Reestruturação para inglês primário nos dois repositórios públicos.** O inglês se tornou o idioma de produção primário, decisão tomada no meio desta sessão. Todo documento de governança renomeado e reescrito com o inglês na frente (`PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`), cada um com uma tradução em português e espanhol ao lado. `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, com os scripts correspondentes em `build/` renomeados e, no caso do guia compacto, reescritos numa montagem trilíngue com inglês como aba padrão. `harness-p1.html`, `harness-p2.html` e `docs/logbook.html` tiveram a aba padrão trocada de português para inglês, tanto nos arquivos montados quanto nos scripts que os regeneram. Um banner de dica de idioma do navegador foi acrescentado às quatro páginas trilíngues (navegadores em português ou espanhol recebem uma oferta dispensável de troca, qualquer outro cai silenciosamente para o inglês). O repositório da skill foi renomeado de `levantando-briefing` para `intake-briefing`, e cada um dos seus quatro arquivos foi reescrito com o inglês na frente, com traduções `.pt.md`/`.es.md`, além de uma linha estática de navegação de idioma no topo de cada um, já que o GitHub não executa JavaScript dentro do Markdown renderizado. Ver `STATUS.md` para o detalhamento completo e a seção Idiomas de `STANDARDS.md` para a regra em si.

**Quatro skills recomendadas de fora, avaliadas, uma adotada.** `ponytail`, `no-ai-slop`, `taste-skill` e `impeccable` foram comparadas por relevância, sinal de manutenção, número de contribuidores e licença antes de qualquer uma tocar este repositório. `ponytail` (117 mil estrelas, com benchmark, mantida ativamente) teria resolvido a ressalva de atribuição indevida que já pesa sobre `karpathy-guidelines`, mas ficou de fora por ora, não descartada. `no-ai-slop` é uma skill de limpeza de prosa genuinamente útil cuja lista de palavras banidas inclui, por acaso, o termo central deste projeto, "harness", e também ficou de fora até decidirmos como fazer a exceção. `taste-skill` foi recusada de vez: suas dez subskills usam exatamente o registro de hype que um projeto sobre evidência em vez de opinião não deveria citar, e seis contribuidores contra 82 mil estrelas é uma base frágil. `impeccable` foi adotada: Apache-2.0, 30 contribuidores, versionada (v4.1.2), deriva da própria skill frontend-design da Anthropic, e suas 61 regras determinísticas de detector combinam com a própria definição de Inspecionar, evidência em vez de opinião, aplicada especificamente a design de frontend. Instalada só como documentação, `SKILL.md` e `reference/`, deixando de propósito a árvore `scripts/` que o CLI dela precisa, ver `TOOLS.md`. Acrescentada como a décima oitava ficha do guia compacto, em Inspecionar, nos três idiomas, ver `sources/inventory.md` para o registro de verificação.

**Preparação das partes 3 e 4, os três primeiros itens da fila do dossiê de trabalho.** `docs/harness-p3-p4-briefing.pt.md` definiu a fila no bloco D, e esta rodada fechou os itens 1 a 3. `README.md`, `STATUS.md`, `NEXT-STEPS.md` e `STANDARDS.md`, nos três idiomas, agora descrevem quatro partes organizadas em torno de um framework de três camadas, construção, operação, governança, atravessadas pelas faixas N0 a N3, em vez de três partes mais dois companheiros, e `STANDARDS.md` ganhou a regra de `Diagramas` que o dossiê propôs: Mermaid primeiro, o SVG deriva e nunca substitui. `sources/inventory.md` ganhou uma seção nova carregando as 32 fontes do dossiê distribuídas em sete eixos de pesquisa mais o achado Air Canada, status V ou P original preservado, com nota explícita nas duas que marcam uma lacuna real e não só um link faltando: a fonte primária da regra de dois, e o fato de ainda não existir precedente brasileiro. Nove arquivos SVG independentes, D1 a D9, foram renderizados no novo diretório `diagrams/` a partir das especificações Mermaid do dossiê, em inglês por ser conteúdo novo, com o vocabulário de governança da parte 4 (dono do agente, homologador, auditor, patrocinador da área, recibo mantido distinto de registro) fixado nesta etapa para que os diagramas e a prosa futura não se afastem. Ver `STATUS.md` para o detalhamento completo e `diagrams/README.md` para o índice.

**Diagramas D1 a D9 validados por renderização, e uma arquitetura de série unificada.** Os nove SVGs independentes foram renderizados pela primeira vez (Chrome headless) e conferidos visualmente, fechando a ressalva da rodada anterior. Cinco carregavam bugs reais de coordenada (linhas de conexão cortando texto de caixa no D3, um conector duplicado no D4, uma legenda estourando o canvas no D5, uma linha atravessando uma caixa e uma curva cortando outra no D7, duas colunas sobrepostas no D9), todos corrigidos na fonte SVG; D1, D2, D6 e D8 não tinham bug nenhum. Cada SVG ganhou um `.png` correspondente (2x, fundo branco opaco) para publicação no Medium, já que o editor do Medium não renderiza SVG inline colado nem HTML arbitrário. Em paralelo, a série ganhou a navegação de topo que faltava: um componente único compartilhado `.topbar`, centralizado, fixo ao rolar, reativo ao seletor de idioma (objeto `SERIES` mais `setSeries()` dentro do `set()` de cada página), substituindo a barra inconsistente, só em português, não fixa, que antes existia apenas em `harness-p1.html`. As seções de glossário e fontes de cada artigo foram aposentadas em favor de duas páginas novas, compartilhadas e trilíngues, `harness-glossary.html` e `harness-sources.html`, consolidando e removendo duplicatas de todo termo e citação das partes 1 e 2; todo link de termo e toda citação na série agora apontam pra lá. `harness-p1.html`, `harness-p2.html` e `harness-toolkit.html` foram retrofitados (e `build_p2.py` / `build_toolkit.py` atualizados para reproduzir a mesma barra numa próxima regeração, pra que o conserto não seja silenciosamente desfeito). O corpo em inglês da parte 3 foi escrito por completo contra esse padrão novo e ligado em `harness-p3.html`; suas abas em português e espanhol foram traduzidas por completo na sequência, ver a seção 1 abaixo.

---

## 1. Escrever a parte 3, concluído

**Status: escrita e publicada em `harness-p3.html`, nos três idiomas.** As nove seções abaixo estão todas no corpo (`build/body_p3_en.html`, `_pt.html`, `_es.html`), com os cinco diagramas embutidos e traduzidos por completo (inclusive cada rótulo de SVG, conferido renderizando cada diagrama isolado nos três idiomas, sem estouro, sem sobreposição), os artefatos de matriz de alçada e esquema de recibo no texto, as duas obrigações de honestidade honradas, e o arco da personagem da Air Canada se fechando na seção 9. As contagens de palavras ficam próximas entre os três (EN 5.131, PT 5.468, ES 5.676), consistente com uma tradução de verdade e não um resumo. Mantida abaixo como registro de acompanhamento.

Pesquisa completa, ver `sources/inventory.md`. A própria seção de fechamento do dossiê, "O que a pesquisa muda na estrutura planejada" no bloco B, revisa o esboço original de dez seções para nove. Reconstruída aqui para acompanhamento, conferir contra o dossiê antes de redigir:

1. Air Canada abre a peça: uma empresa real argumentou em um tribunal real que o assistente dela era uma pessoa legal separada, que responde sozinha, e perdeu
2. A diretora reentra aqui, em N2, diante da primeira ação irreversível, o contraste com o argumento da Air Canada é o ponto
3. A separação de poderes, com a regra de dois como ferramenta operacional, o equivalente da matriz de guias e sensores da parte 2
4. Identidade e um dono nomeado: quem implantou, o que está autorizado a fazer, em nome de quem age agora
5. Quando a ordem chega dentro do dado
6. O que precisa estar registrado, e o que reversão significa de fato
7. Skill de terceiro é código de terceiro, fechando o gancho que a parte 2 deixou aberto
8. Obrigações legais em duas colunas, Brasil e Europa, o que já vale antes do que ainda está em tramitação
9. Quem responde, e onde você está, o fechamento da série

Duas obrigações de honestidade que o dossiê marca explicitamente: declarar que o precedente Air Canada é estrangeiro, sob pena de um leitor jurídico desqualificar a peça inteira, e datar a afirmação de que a regulamentação específica do artigo 20 da LGPD ainda não foi publicada, porque essa frase pode envelhecer em meses.

**Pronto quando:** as três versões estiverem prontas, o arco da personagem se fechar, a peça funcionar sozinha para um leitor que não leu as anteriores, e os artefatos de matriz de alçada e esquema de recibo estiverem no texto. **Cumprido, 30 de agosto de 2026.**

---

## 2. Escrever a parte 4, concluído

**Status: totalmente trilíngue e publicada em `harness-p4.html`, desde 31 de agosto de 2026.** Nove seções, cinco diagramas embutidos (D6 a D10, o D10 renderizado agora para esta peça, depois traduzido e revalidado visualmente nas três línguas antes de ser incorporado), a tabela dos seis estados do ciclo de vida, a tabela dos quatro papéis com a regra de não acumulação, a tabela dos oito indicadores com a admissão de honestidade de que o painel é síntese, o argumento da taxa de reprovação no portão ancorado no SCHUFA que amarra a parte 4 ao fundamento jurídico da parte 3, o precedente da linha de reporte do CISO para onde o escritório senta, a restrição de sete agentes e uma planilha sustentada ao longo de toda a seção de advertência, e a tabela de fechamento no mesmo padrão da parte 3. As contagens de palavras ficam próximas nas três línguas (inglês 6.889, português 7.051, espanhol 7.377), coerente com uma tradução de verdade, não um resumo. Dez novos verbetes de glossário acrescentados nos três idiomas; `harness-sources.html` ganhou uma seção da parte 4, 32 fontes.

Pesquisa completa, ver a seção da parte 4 em `sources/inventory.md` e `docs/research-part4.pt.md`. Tese central realizada: o ciclo de vida do agente, estados e não passos, distinguido do MEDIR com clareza suficiente para que o leitor não confunda os dois.

Estrutura coberta, na ordem em que foi de fato redigida:

1. Abre com a tomada das 20.225 contas do Instagram, o modo de falha por concentração da parte 3 em escala populacional
2. A diretora reentra tocando seis sistemas que ninguém contou, incapaz de responder a pergunta mais simples de um conselheiro
3. O ciclo de vida em si, seis estados de um briefing versionado até o descomissionamento, com as duas transições que quase ninguém implementa, homologação vencida e sem execução no período, ambas levando ao descomissionamento
4. Os quatro papéis e a regra de não acumulação, a mesma separação de poderes da parte 3, agora no plano organizacional, com fonte no Modelo das Três Linhas do Instituto dos Auditores Internos
5. Os oito indicadores, dois dos quais medem a qualidade da própria governança, não a do agente: a taxa de exceção, e a taxa de reprovação do próprio portão, fechados pelo D10, o laço trimestral do escritório
6. Onde o escritório senta, e por que não em TI, apresentando as opções realistas com o custo de cada uma
7. A advertência: o antídoto contra virar folheto de fornecedor é uma restrição explícita atravessando o texto, tudo o que ela propõe precisa funcionar em uma empresa com sete agentes e uma planilha
8. O argumento de fecho: toda plataforma governa para dentro, e é por isso que o escritório precisa ser função da empresa, não produto que ela compra
9. Quem responde, e onde você está: o arco da diretora se fecha ao longo das quatro partes

**Pronto quando:** as três versões estiverem prontas, o arco da personagem fechar a série, os oito indicadores estiverem definidos com fórmula, e o texto sustentar a restrição de sete agentes e uma planilha do início ao fim. **Cumprido por completo, 31 de agosto de 2026.**

---

## 3. Consolidar o playbook

Não iniciado, e de propósito fora do escopo da próxima sessão de conteúdo, decidido em 31 de agosto de 2026: as quatro partes são o argumento, o playbook é o ferramental derivado delas, e construí-lo agora, logo depois de fechar a série de artigos, embaçaria essa fronteira. Este item fica como o registro explícito e deliberadamente estacionado do que o playbook vai conter, para que a próxima sessão que pegar essa tarefa não precise reconstruir o plano do zero.

Reaproveita as quatro partes e o guia, e acrescenta sete modelos operacionais que ainda não existem, cada um rastreável até a peça que já introduziu o conceito por trás dele, não inventado do zero:

- Modelo de contrato de tarefa, a partir do contrato de tarefa do passo Mapear da parte 1
- Modelo de skill, derivado dos três exemplos completos da parte 2
- Modelo de recibo de execução, a partir do recibo original da parte 2, estendido na parte 3 com as respostas da regra de dois e o ponto de reversão
- Matriz de risco por faixa, a partir da matriz de alçada da parte 3 (classe de ação, reversibilidade, alçada exigida) cruzada com as faixas N0 a N3 da parte 1
- Diagnóstico de faixa, versão questionário, expandindo o checklist de doze perguntas da parte 1 num instrumento autônomo
- Trilha de implantação de N0 a N3, a progressão que a parte 1 só esboçou
- Modelo de registro de agentes e de ata de homologação, a partir dos estados do ciclo de vida e dos quatro papéis da parte 4, o registro respondendo "quantos existem" e a ata formalizando o ato do homologador

O D10, o laço próprio do escritório por trimestre, deixou de ser candidato do playbook: ele já foi publicado dentro da própria parte 4, fechando a seção dos oito indicadores. Ele ainda pode abrir o playbook como uma segunda aparição, legítima, já que ali organiza o documento inteiro em vez de competir consigo mesmo.

**Pronto quando, de fato, for retomado:** os sete modelos existem, cada um referenciado de volta à parte e à seção que o fundamenta, e o playbook abre com o D10 como seu próprio diagrama organizador.

---

## Pendências menores, a decidir a qualquer momento

**Caso real de abertura.** A cena é composta. Se surgir um caso real anonimizado do ecossistema do autor, substituí-la elevaria bastante o texto.

**Borda da caixa do sumário.** É a única borda de caixa que sobrou nos documentos. Decidir se ela sai, para ficar coerente com a remoção das demais.

**Fundo da citação em destaque na impressão.** Depende de o navegador estar configurado para imprimir gráficos de plano de fundo. Alternativa sem dependência: um filete fino acima e abaixo do bloco.

**Grafia do inglês.** Hoje é britânica, e essa é a leitura padrão do projeto agora. Se o público-alvo migrar para os Estados Unidos, converter.

**Publicação.** Resolvida em 30 de agosto de 2026: GitHub Pages ativo em `tecosodreaboutdigital.github.io/harness-medir`. Verificar, depois do primeiro build automático, se os documentos renderizam corretamente lá (o link com maior chance de precisar de ajuste é algum caminho relativo entre eles).

**Localizar a fonte primária da regra de dois.** Duas fontes secundárias independentes a atribuem à Meta com a mesma formulação, suficiente para citar o conteúdo na parte 3, não para linkar. Buscar de novo antes de a peça ser fechada, ver `sources/inventory.md`.
