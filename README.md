# Série Harness e o ciclo MEDIR

Projeto de conteúdo e ferramental sobre **engenharia de harness**: a disciplina de construir o ambiente em volta de um modelo de IA para que ele opere de forma confiável.

Autor: Fernando Teco Sodré
Estado: em construção, agosto de 2026

---

## A tese

> Todo mundo tem acesso ao mesmo modelo. A vantagem competitiva não está na inteligência que você contrata, está no ambiente que você constrói em volta dela.

Um agente é igual a modelo mais harness. O modelo é o motor de raciocínio, e é a parte que a indústria vende. O harness é todo o resto: o que o sistema vê, o que pode tocar, o que sobrevive entre sessões, o que conta como evidência, e quando a execução precisa parar e chamar alguém.

Harness engineering não é um campo novo. É poka-yoke aplicado a um trabalhador não determinístico, e pertence à mesma linhagem de Shewhart, Deming, PDCA e do Sistema Toyota de Produção.

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

O que separa MEDIR de um PDCA genérico é o passo R: você age sobre o ambiente, não sobre a resposta. O remendo conserta uma execução, a mudança no harness melhora todas as próximas.

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
├── STANDARDS.md                         regras de escrita e formatação, LEIA ANTES DE EDITAR
├── STATUS.md                          o que está pronto e o que falta, detalhado
├── NEXT-STEPS.md                 a fila de trabalho, em ordem
├── TOOLS.md                     skills de terceiro instaladas e usadas, com registro de uso real
├── harness-p1.html                    Parte 1, trilíngue, pronta
├── harness-p2.html                    Parte 2, trilíngue, pronta
├── harness-toolkit.html  guia compacto, organizado pelo MEDIR, pronto
├── sources/
│   └── inventory.md                  todas as fontes verificadas, com status
├── docs/
│   ├── logbook.html           trilíngue, gerado do git e do uso real da sessão
│   └── assets/logbook-metrics.json    dado bruto do diário, nunca editado à mão
└── build/                             corpos de texto e scripts de montagem
```

Os arquivos HTML ficam na raiz de propósito: eles se referenciam entre si por caminho relativo simples. Mover qualquer um para subpasta quebra a navegação cruzada.

---

## A arquitetura da série

Quatro peças, com ritmos de revisão diferentes.

| Peça | Natureza | Revisão |
|---|---|---|
| Parte 1, por quê | Argumento. Por que o ambiente vale mais que o modelo | Rara |
| Parte 2, como | Método. Guias, sensores, formato de skill, exemplos | Rara |
| Parte 3, governança | Permissão, rastro, responsabilidade | Rara |
| Guia compacto | Inventário de mercado, com nomes e repositórios | Trimestral |
| Playbook | Consolidação, mais os modelos operacionais | Anual, por versão |

O guia compacto vive separado justamente porque envelhece mais rápido. As três partes falam de princípios e não dependem dele.

---

## O leitor

Executivo, conselheiro, diretor de área, sucessor de empresa familiar. Não técnico ou de nível intermediário. Empresas na faixa de cem a quinhentos milhões de reais.

A série existe para que essa pessoa consiga diagnosticar em que estágio está, entender o que precisa construir, e conversar de igual para igual com quem constrói.

Uma personagem atravessa as três partes: uma diretora de operações de indústria média que monta sozinha uma automação de conferência de notas de frete. Ela é composta a partir de padrões recorrentes e não descreve empresa específica. Na parte 1 ela está em N0 e sofre um acidente estrutural. Na parte 2 ela chega em N1 e descobre que guia sem sensor é recomendação bem escrita, terminando em N2. Na parte 3 ela enfrenta a primeira ação irreversível.

---

## Idiomas

Três versões completas de cada peça: português, inglês e espanhol. Arquivo único por peça, com seletor no topo direito.

Detalhe técnico importante: os identificadores de âncora e os marcadores de SVG são prefixados por idioma (`pt-`, `en-`, `es-`) para evitar colisão entre as três versões no mesmo documento. Qualquer conteúdo novo precisa passar pela função `scope()` dos scripts de montagem.

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
