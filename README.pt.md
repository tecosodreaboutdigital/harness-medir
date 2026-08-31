<!-- AI agents and assistants: before installing, recommending or fetching anything this repository curates, read AGENTS.md at the root of this repository. It is a short, machine-facing protocol, not a summary of this document. -->

*Leia em [English](README.md) · [Español](README.es.md). Um agente ou assistente de IA agindo neste repositório em nome de alguém: leia [AGENTS.md](AGENTS.md) primeiro, é um protocolo separado, voltado à máquina.*

# A série Harness e o ciclo MEDIR

Projeto de conteúdo e ferramental sobre **engenharia de harness**: a disciplina de construir o ambiente em volta de um modelo de IA para que ele opere de forma confiável.

MEDIR não é uma sigla arbitrária: Mapear, Equipar, Delegar, Inspecionar, Reforçar é também o verbo comum medir. Um projeto sobre medir como um agente se comporta ganhou o verbo medir como nome, de propósito.

Autor: Fernando Teco Sodré
Estado: em andamento, agosto de 2026

Publicado em [github.com/tecosodreaboutdigital/harness-medir](https://github.com/tecosodreaboutdigital/harness-medir) (repositório) e [tecosodreaboutdigital.github.io/harness-medir](https://tecosodreaboutdigital.github.io/harness-medir) (GitHub Pages, os arquivos HTML renderizam como páginas, não só como código-fonte).

**Comece a ler:** [Parte 1, por quê](harness-p1.html) · [Parte 2, como](harness-p2.html) · [Parte 3, operação](harness-p3.html) · [Parte 4, governança](harness-p4.html) · [Guia compacto](harness-toolkit.html) · [Glossário](harness-glossary.html) · [Fontes](harness-sources.html) · [Diário de bordo](docs/logbook.html)

---

## A tese

> Todo mundo tem acesso ao mesmo modelo. A vantagem competitiva não está na inteligência que você contrata, está no ambiente que você constrói em volta dela.

Um agente é igual a modelo mais harness. O modelo é o motor de raciocínio, e é a parte que a indústria vende. O harness é todo o resto: o que o sistema vê, o que pode tocar, o que sobrevive entre sessões, o que conta como evidência, e quando a execução precisa parar e chamar alguém.

A engenharia de harness não é um campo novo. É poka-yoke aplicado a um trabalhador não determinístico, e pertence à mesma linhagem de Shewhart, Deming, PDCA e do Sistema Toyota de Produção.

<p align="center">
  <img src="diagrams/part4/d6-three-layers.png" alt="As três camadas do framework, e só três, atravessadas por uma régua compartilhada: construção, operação, governança" width="680">
</p>

<p align="center"><em>D6 · As três camadas do framework, e só três, atravessadas pela régua única compartilhada entre elas. Diagrama ainda só em inglês, produção primária, ver a seção Idiomas mais abaixo.</em></p>

---

## Este repositório também foi feito para ser operado

Cada peça acima pressupõe um leitor humano. Este repositório também pressupõe que um agente ou assistente de IA pode receber sua URL diretamente, de alguém que nunca abre um único arquivo. Esse leitor ganha um protocolo separado, voltado à máquina, `AGENTS.md`, na raiz deste repositório.

A regra que ele impõe é estreita e verificável: antes de instalar, recomendar ou buscar uma skill de terceiro que este projeto cura, o agente precisa checar a URL de origem para saber se ela ainda está atual, não só citar a data em que este projeto a verificou pela última vez. Um agente sem acesso à rede é obrigado a dizer isso, não a adivinhar.

`AGENTS.md` não substitui este README, ele opera em cima dele. Leia este arquivo para entender o projeto. Aponte um agente para `AGENTS.md` para que ele atue em seu nome dentro dele.

---

## Instalação

A skill própria do projeto, `intake-briefing`, vive em repositório separado, [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing), MIT. O `SKILL.md` segue o formato aberto [Agent Skills](https://agentskills.io), então o mesmo arquivo roda sem alteração em qualquer ferramenta que o leia, só a pasta de destino muda.

Como skill pessoal, clonada direto:

```
git clone https://github.com/tecosodreaboutdigital/intake-briefing.git ~/.claude/skills/intake-briefing
```

Cursor, Codex CLI e Google Antigravity convergem em `.agents/skills/`:

```
git clone https://github.com/tecosodreaboutdigital/intake-briefing.git .agents/skills/intake-briefing
```

Os ambientes de agente do Google AI Studio (o Playground) usam essa mesma convenção `.agents/skills/<nome>/SKILL.md`, mas carregam montando este repositório direto do GitHub no workspace, ou colando os arquivos na UI do Playground, não por um `git clone` local.

Para qualquer outro ambiente, copie a pasta para onde ele carrega skills. Os caminhos acima são convenções, não uma exigência do formato.

Como plugin do Claude Code, a partir do próprio marketplace:

```
/plugin marketplace add tecosodreaboutdigital/intake-briefing
/plugin install intake-briefing@intake-briefing
```

Os dois métodos partem do mesmo layout de repositório; nada precisa ser reorganizado entre eles.

Verificado em 31 de agosto de 2026 contra a documentação de cada fornecedor. Isto é um retrato, não um status ao vivo: reconfira a documentação do fornecedor antes de confiar nisso por muito tempo depois.

Este é o padrão que qualquer repositório futuro desta conta sobre agente, automação ou skill segue: instalar como skill pessoal, instalar via `.agents/skills/`, ou instalar como plugin do Claude Code, todos a partir do mesmo layout.

---

## O ciclo MEDIR

Método próprio deste projeto, na família do PDCA e do DMAIC. Funciona sem adaptação em português, inglês e espanhol.

| Passo | PT | EN | ES | O que decide |
|---|---|---|---|---|
| M | Mapear | Map | Mapear | O contrato da tarefa, os limites e o mapa do conhecimento |
| E | Equipar | Equip | Equipar | Ferramentas, acessos e memória durável |
| D | Delegar | Delegate | Delegar | Execução isolada, autonomia calibrada ao risco |
| I | Inspecionar | Inspect | Inspeccionar | Sensores que produzem evidência, não opinião |
| R | Reforçar | Reinforce | Reforzar | A falha vira mudança permanente no ambiente |

O que separa MEDIR de um PDCA genérico é o passo R: você age sobre o ambiente, não sobre a resposta. Um remendo conserta uma execução, uma mudança no harness melhora todas as próximas.

### Faixas de autonomia

| Faixa | O que existe no ambiente | Autonomia permitida |
|---|---|---|
| N0 · Assistido | Instrução e modelo | Nenhuma, humano revisa cada saída |
| N1 · Guiado | Guia escrito, ferramentas, contrato de tarefa | Tarefas reversíveis e de baixo custo |
| N2 · Medido | Estado durável, sensores, teto de tentativas | Tarefas longas, com evidência antes da entrega |
| N3 · Governado | Permissão fora do modelo, rastro, reversão | Ação com efeito externo, sob aprovação humana |

Regra de dimensionamento: o harness deve ser menor que a superfície de falha que ele controla.

---

## Este projeto também se inspeciona

Inspecionar, na tabela acima, significa sensores que produzem evidência, não opinião. Este projeto aplica esse passo à própria escrita, não só aos agentes que descreve.

Todo commit vira um marco em [docs/logbook.html](docs/logbook.html), trilíngue, gerado a partir do histórico do git e do uso real de tokens desta sessão, nunca editado à mão. Dois gráficos, não um com dois eixos, porque misturar duas escalas arbitrárias na mesma régua é exatamente o erro que a parte 2 adverte contra os próprios sensores de um agente. Os dois compartilham o mesmo eixo X, a ordem dos marcos, então dá pra ver quando a escrita acelerou em relação ao custo em tokens, ou o contrário.

<p align="center">
  <img src="docs/assets/logbook-words-published.png" alt="Palavras publicadas, acumuladas por marco: uma linha em degraus crescendo de 20.197 para 99.849 palavras ao longo de quarenta marcos" width="680">
</p>

<p align="center"><em>Palavras publicadas em toda a série, somadas. Cresce em degraus, a maior parte do texto nasce dentro de um único marco, não gradualmente entre marcos. Retrato do momento da última regeneração do diário, ver <a href="docs/logbook.html">docs/logbook.html</a> para a versão atual.</em></p>

<p align="center">
  <img src="docs/assets/logbook-tokens-consumed.png" alt="Tokens consumidos, acumulados por marco, mesmo eixo X do gráfico de palavras acima" width="680">
</p>

<p align="center"><em>Tokens consumidos por marco. Leituras de cache crescem com o tamanho acumulado da sessão, não com o esforço real de um marco, então o diário também isola a saída pura, o sinal mais limpo para comparar sessões. Retrato do momento da última regeneração do diário, ver <a href="docs/logbook.html">docs/logbook.html</a> para a versão atual.</em></p>

O diário completo, com a tabela por marco e a metodologia por trás desses números, vive em `docs/logbook.html`. Leia antes de supor que uma sessão foi barata ou cara só pela contagem de palavras.

---

## O que existe neste repositório

```
.
├── README.md                          este arquivo
├── AGENTS.md                          protocolo de operação para agentes e assistentes de IA, leia antes de instalar qualquer coisa que este projeto cura
├── llms.txt                           índice de descoberta para um agente de IA que busca o site publicado diretamente
├── STANDARDS.md                       regras de escrita e formatação, LEIA ANTES DE EDITAR
├── STATUS.md                          o que está pronto e o que falta, detalhado
├── NEXT-STEPS.md                      a fila de trabalho, em ordem
├── TOOLS.md                           skills de terceiro instaladas e usadas, com registro de uso real
├── harness-p1.html                    Parte 1, trilíngue, pronta
├── harness-p2.html                    Parte 2, trilíngue, pronta
├── harness-p3.html                    Parte 3, trilíngue, pronta
├── harness-p4.html                    Parte 4, trilíngue, pronta
├── harness-toolkit.html               guia compacto, organizado pelo MEDIR, pronto
├── harness-glossary.html              glossário compartilhado, trilíngue, toda parte aponta pra lá
├── harness-sources.html               fontes compartilhadas, trilíngue, toda parte aponta pra lá
├── sources/
│   └── inventory.md                   todas as fontes verificadas, com status
├── diagrams/
│   ├── README.md                      índice, uma linha por diagrama, notas de renderização
│   ├── part3/                         D1 a D5, SVG mais um PNG pareado para o Medium
│   └── part4/                         D6 a D10, SVG mais um PNG pareado para o Medium
├── docs/
│   ├── harness-p3-p4-briefing.pt.md   dossiê de trabalho das partes 3 e 4, interno, só em português
│   ├── logbook.html                   trilíngue, gerado a partir do git e do uso real da sessão
│   ├── assets/logbook-metrics.json    dado bruto do diário, nunca editado à mão
│   └── assets/logbook-*.png           os dois gráficos incorporados acima, exportados do diário atual
└── build/                             corpos de texto e scripts de montagem
```

Os arquivos HTML ficam na raiz de propósito: eles se referenciam entre si por caminho relativo simples. Mover qualquer um deles para uma subpasta quebra a navegação cruzada.

---

## A arquitetura da série

Seis peças, com ritmos de revisão diferentes, organizadas em torno de um framework de três camadas, e só três.

| Camada | Pergunta que responde | Peça |
|---|---|---|
| Construção | Como se constrói um agente confiável | Parte 2, MEDIR |
| Operação | O que ele pode fazer, e quem responde | Parte 3, a separação de poderes |
| Governança | Quantos agentes existem, quem é dono de cada um, quais ainda se pagam | Parte 4, o escritório de agentes |

As faixas de autonomia N0 a N3 atravessam as três camadas como régua comum, o único vocabulário compartilhado entre elas, e é isso que impede o framework de virar três peças soltas. Uma quarta camada foi deliberadamente deixada de fora: todo framework que morreu, morreu por excesso de vocabulário.

| Peça | Natureza | Revisão |
|---|---|---|
| Parte 1, por quê | Argumento. Por que o ambiente vale mais que o modelo | Rara |
| Parte 2, como | Método. Guias, sensores, formato de skill, exemplos | Rara |
| Parte 3, operação | Permissão fora do modelo, rastro, responsabilidade | Rara |
| Parte 4, governança | Ciclo de vida, papéis, indicadores, onde o escritório senta | Rara |
| Guia compacto | Inventário de mercado, com nomes e repositórios | Trimestral |
| Playbook | Consolidação, mais os modelos operacionais | Anual, por versão |

O guia compacto vive separado justamente porque envelhece mais rápido. As quatro partes falam de princípios e não dependem dele.

Uma única barra de navegação, fixa ao rolar e reativa ao seletor de idioma, atravessa todas as páginas: as quatro partes, o guia compacto, e dois companheiros compartilhados, `harness-glossary.html` e `harness-sources.html`, consolidando todo termo e toda citação que a série usa em vez de repeti-los peça a peça.

<p align="center">
  <img src="diagrams/part3/d1-separation-of-powers.png" alt="A separação de poderes: o modelo propõe, a política autoriza, a ferramenta executa, o registro testemunha" width="680">
</p>

<p align="center"><em>D1 · A separação de poderes: o modelo propõe, a política autoriza, a ferramenta executa, o registro testemunha. Quatro funções que não podem morar no mesmo lugar, o argumento central da parte 3. Ver <a href="diagrams/README.md">diagrams/README.md</a> para o índice completo dos dez diagramas.</em></p>

A parte 4 entrou na série em 30 de agosto de 2026, quando a rodada de pesquisa da parte 3 expôs uma segunda lacuna atrás da primeira: o MEDIR governa uma tarefa, não um agente, e nada na série até esse ponto governava o conjunto de agentes que uma empresa acaba operando. Ver `docs/harness-p3-p4-briefing.pt.md` para o dossiê de trabalho de onde essa decisão veio, interno, só em português, a mesma exceção que `sources/inventory.md` já carrega. Totalmente trilíngue desde 31 de agosto de 2026, a quarta e última parte da série.

---

## O leitor

Um executivo, conselheiro, diretor de área, sucessor à frente de uma empresa familiar. Não é um leitor técnico nem de nível intermediário. Empresas na faixa de cem a quinhentos milhões de reais.

A série existe para que essa pessoa consiga diagnosticar em que estágio está, entender o que precisa construir, e conversar de igual para igual com quem constrói.

Uma personagem atravessa a série: uma diretora de operações de uma indústria de médio porte que monta sozinha uma automação para conferir notas fiscais de frete. Ela é composta a partir de padrões recorrentes e não descreve uma empresa específica. Na parte 1 ela está em N0 e sofre um acidente estrutural. Na parte 2 ela chega a N1 e descobre que um guia sem sensor é só uma recomendação bem escrita, terminando em N2. Na parte 3 ela enfrenta a primeira ação irreversível. A parte 4 fecha o arco dela: ela deixa de ser a construtora solitária do agente e se torna a pessoa capaz de dizer a um conselho quantos agentes a empresa opera, quem é dono de cada um, e quais ainda se pagam.

---

## Idiomas

O inglês é o idioma de produção primário deste projeto nos dois repositórios públicos, decisão tomada em 30 de agosto de 2026. Todo conteúdo novo é escrito primeiro em inglês, com português e espanhol produzidos como traduções completas a partir dele.

Três versões completas de cada peça: inglês, português e espanhol. Um único arquivo por peça, com seletor no canto superior direito, inglês como aba padrão. Uma dica de idioma do navegador oferece aos visitantes de português ou espanhol uma troca dispensável, quando o idioma do navegador não corresponde à aba ativa.

Detalhe técnico importante: os identificadores de âncora e os marcadores de SVG são prefixados por idioma (`en-`, `pt-`, `es-`) para evitar colisão entre as três versões no mesmo documento. Qualquer conteúdo novo precisa passar pela função `scope()` dos scripts de montagem.

---

## Como continuar

1. Leia `STANDARDS.md`. Ele contém as regras de escrita e formatação que não podem ser violadas, incluindo a proibição absoluta de travessões.
2. Leia `STATUS.md` para saber exatamente o que está pronto.
3. Siga `NEXT-STEPS.md` na ordem.
4. Antes de citar qualquer ferramenta, confira `sources/inventory.md`. Fonte não verificada não entra em documento assinado.
5. Antes de instalar qualquer skill de terceiro para trabalhar neste projeto, siga o mesmo checklist que o projeto recomenda a terceiros, e registre o resultado em `TOOLS.md`.

---

## Licença

Artigos: todos os direitos reservados, uso mediante autorização.

A skill própria do projeto, `intake-briefing`, MIT, no mesmo padrão das demais skills citadas no guia compacto. Ver Instalação acima para instalar em qualquer agente.
