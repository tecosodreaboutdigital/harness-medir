# Estado

Situação em 30 de agosto de 2026.

Publicado em `github.com/tecosodreaboutdigital/harness-medir` (repositório) e `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, os HTML renderizam como página, não só como código-fonte).

---

## Pronto

### Diário de bordo

`docs/diario-de-bordo.html`, trilíngue. Documenta a evolução do próprio projeto: palavras publicadas e tokens consumidos por marco, gerado a partir do git e do transcript real da sessão, nunca escrito à mão. Ver `build/generate_diario_metrics.py` e `build/build_diario.py`. Seis marcos até aqui, o histórico completo do repositório, mais o que ainda está em sessão aberta.

### Parte 1 · O melhor modelo do mundo dentro de uma empresa sem processo

`harness-p1.html`

Trilíngue completa, treze seções mais o bloco de navegação, três diagramas, 26 verbetes de glossário. Cerca de 4.700 palavras em português, 4.500 em inglês, 4.700 em espanhol.

Conteúdo: cena de abertura com a diretora, o que é um harness, a analogia da delegação, a linhagem histórica com correção da atribuição do termo, quatro estudos de caso com números, o ciclo MEDIR, a tabela de equivalências com o vocabulário de qualidade, as faixas N0 a N3, riscos em nível de conselho, checklist de doze perguntas.

Barra de série e bloco "Onde você está" já implementados.

### Parte 2 · Guias e sensores: como um agente aprende a se corrigir

`harness-p2.html`

Trilíngue completa desde 30 de agosto de 2026. Dezessete seções, três diagramas, 26 verbetes por idioma. Cerca de 6.200 palavras em português, 6.350 em inglês, 6.450 em espanhol.

Reescrita completa depois de uma primeira versão descartada. A versão descartada falhava por abandonar a personagem, não fazer histórico da parte 1 e organizar por conceito em vez de pelo ciclo.

Conteúdo: abre na quarta semana com a diretora tendo escrito o guia inteiro e o sistema liberando nota de fornecedor descredenciado. Seções ancoradas em Equipar, Delegar e Inspecionar, com Reforçar no fim. Inclui a matriz de guias e sensores, a comparação entre mensagem de erro que ensina e alarme, o truque do limiar, a unidade de durabilidade, três exemplos completos com SKILL.md real, as classes de ambiente cruzadas com as faixas, e limpeza como cadência.

Tradução inglesa em grafia britânica, espanhola por "tú". MEDIR e harness mantidos como nome próprio nos três idiomas, conforme `PADROES.md`. Os exemplos de skill (nomes de arquivo, campos, valores) foram traduzidos também, não só a prosa ao redor.

O JavaScript de troca de idioma da parte 1 e da parte 2 ganhou roteamento por âncora: um link do tipo `harness-p1.html#en-opening` agora seleciona a aba certa antes de rolar, em vez de sempre abrir na aba PT padrão. Sem esse ajuste, um leitor em inglês clicando em qualquer referência cruzada para a parte 1 caía sempre em português.

### Skill levantando-briefing

`github.com/tecosodreaboutdigital/levantando-briefing`, repositório próprio desde 30 de agosto de 2026. Artefato original do projeto, completo, publicado, MIT. Quatro arquivos: SKILL.md, roteiro.md, modelo-briefing.md, README.md.

Decide se a automação deve existir, antes de discutir como funciona. Oito blocos, tabela determinística de derivação de faixa, veredito com três opções incluindo não fazer, e versionamento com comparação bloco a bloco.

Preenche uma lacuna verificada: existe farto material sobre como especificar, quase nada sobre como decidir se vale.

Separada do monorepo harness-medir para instalação independente, no mesmo padrão das demais skills citadas no guia compacto. Ativa neste ambiente via cópia local em `.claude/skills/levantando-briefing/`, fora do controle de versão, ver `FERRAMENTAS.md`.

### Guia compacto de ferramentas e skills

`harness-caixa-de-ferramentas.html`

Reescrito por completo em 30 de agosto de 2026. Organizado pelos cinco passos do MEDIR, não por categoria de produto. Dezessete fichas de seis campos, mais seção de diagnóstico de faixa no início para quem chega da parte 1. Cada passo do MEDIR tem crítica registrada, não só recomendação.

Distribuição: Mapear com quatro fichas (levantando-briefing, guia inspirado em Karpathy, c4-skills, especificação antes do código com a crítica de Böckeler e Pocock), Equipar com três (superpowers, mattpocock/skills, planning-with-files), Delegar com três (holdfast, classes de ambiente, orquestração programada com LangGraph), Inspecionar com quatro (dependency-cruiser, Stryker, Semgrep, sensors-cli), Reforçar com três (ai-slop-cleaner, limpeza como cadência, coleta de lixo).

Toda ferramenta citada está verificada em `fontes/inventario.md`, incluindo três fontes adicionadas nesta reescrita: Semgrep, LangGraph e GitHub Spec Kit com link direto.

Repositório publicado, público, em `github.com/tecosodreaboutdigital/harness-medir`.

---

## Não iniciado

### Parte 3 · Governança de agentes

Escopo definido, base de pesquisa fraca. É a peça de maior valor comercial e a que está com a fundação mais rasa.

Escopo: permissão imposta fora do modelo, instrução maliciosa que chega dentro de um dado ou de uma skill de terceiro, registro auditável, reversão, obrigações legais, e quem responde pelo que o agente fez.

O que falta pesquisar, e é rodada dedicada, não complemento: literatura de segurança de agentes, incidentes reais documentados, posição da autoridade brasileira sobre decisão automatizada, obrigações regulatórias europeias para sistemas de alto risco, e o que já existe de padrão de auditoria de agentes.

Escrever agora produziria opinião bem escrita, não referência.

### Traduções pendentes

| Peça | PT | EN | ES |
|---|---|---|---|
| Parte 1 | pronta | pronta | pronta |
| Parte 2 | pronta | pronta | pronta |
| Guia compacto | pronta | falta | falta |
| Parte 3 | falta | falta | falta |
| Skill de briefing | pronta | falta | falta |

### Playbook

Consolidação das três partes mais o guia, acrescido do que ainda não existe: modelo de contrato de tarefa, modelo de skill, modelo de recibo de execução, matriz de risco, diagnóstico de faixa e trilha de implantação.

A skill de briefing já é o primeiro artefato operacional dele.

---

## Decisões tomadas que não devem ser revertidas sem motivo

**O termo harness não é traduzido.** Mantido em inglês pela mesma razão que ninguém traduziu kaizen, kanban ou poka-yoke. Foram descartadas as alternativas arnês, arreio, cabresto e sela: metáfora de contenção vende a ideia errada para um leitor que já teme perder controle.

**A atribuição correta do termo é Mitchell Hashimoto, fevereiro de 2026**, não Andrej Karpathy. Karpathy cunhou vibe coding e popularizou context engineering, e o nome dele aparece corretamente nesses contextos.

**Inspecionar, e não Instrumentar,** no passo I. Instrumentar é tecnicamente mais preciso e coerente com o argumento de que qualidade não se inspeciona no fim da linha, mas Inspecionar é o termo do repertório do autor e a sigla depende dele.

**Exemplos na escada indivíduo, time, área.** Não usar equipe nem empresa.

**Cena de abertura composta,** não real, e isso está declarado no rodapé de cada peça. Se surgir um caso real anonimizado, substituir melhora bastante o texto.

**Guia compacto separado dos artigos,** com data de revisão visível, porque envelhece mais rápido.
