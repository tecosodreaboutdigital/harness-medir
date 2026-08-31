*Leia em [English](README.md) · [Español](README.es.md).*

# A série Harness e o ciclo MEDIR

Projeto de conteúdo e ferramental sobre **engenharia de harness**: a disciplina de construir o ambiente em volta de um modelo de IA para que ele opere de forma confiável.

Autor: Fernando Teco Sodré
Estado: em andamento, agosto de 2026

Publicado em [github.com/tecosodreaboutdigital/harness-medir](https://github.com/tecosodreaboutdigital/harness-medir) (repositório) e [tecosodreaboutdigital.github.io/harness-medir](https://tecosodreaboutdigital.github.io/harness-medir) (GitHub Pages, os arquivos HTML renderizam como páginas, não só como código-fonte).

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

## O que existe neste repositório

```
.
├── README.md                          este arquivo
├── STANDARDS.md                       regras de escrita e formatação, LEIA ANTES DE EDITAR
├── STATUS.md                          o que está pronto e o que falta, detalhado
├── NEXT-STEPS.md                      a fila de trabalho, em ordem
├── TOOLS.md                           skills de terceiro instaladas e usadas, com registro de uso real
├── harness-p1.html                    Parte 1, trilíngue, pronta
├── harness-p2.html                    Parte 2, trilíngue, pronta
├── harness-p3.html                    Parte 3, trilíngue, pronta
├── harness-p4.html                    Parte 4, inglês pronto, PT/ES pendente
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
│   └── assets/logbook-metrics.json    dado bruto do diário, nunca editado à mão
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

A parte 4 entrou na série em 30 de agosto de 2026, quando a rodada de pesquisa da parte 3 expôs uma segunda lacuna atrás da primeira: o MEDIR governa uma tarefa, não um agente, e nada na série até esse ponto governava o conjunto de agentes que uma empresa acaba operando. Ver `docs/harness-p3-p4-briefing.pt.md` para o dossiê de trabalho de onde essa decisão veio, interno, só em português, a mesma exceção que `sources/inventory.md` já carrega. O texto em inglês está completo desde o mesmo dia; a tradução para português e espanhol é o próximo marco de conteúdo do projeto.

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

A skill própria do projeto, `intake-briefing`, vive em repositório separado, [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing), MIT, no mesmo padrão das demais skills citadas no guia compacto.
