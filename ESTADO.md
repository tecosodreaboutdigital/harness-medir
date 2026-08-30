# Estado

Situação em 30 de agosto de 2026.

---

## Pronto

### Parte 1 · O melhor modelo do mundo dentro de uma empresa sem processo

`harness-p1.html`

Trilíngue completa, treze seções mais o bloco de navegação, três diagramas, 26 verbetes de glossário. Cerca de 4.700 palavras em português, 4.500 em inglês, 4.700 em espanhol.

Conteúdo: cena de abertura com a diretora, o que é um harness, a analogia da delegação, a linhagem histórica com correção da atribuição do termo, quatro estudos de caso com números, o ciclo MEDIR, a tabela de equivalências com o vocabulário de qualidade, as faixas N0 a N3, riscos em nível de conselho, checklist de doze perguntas.

Barra de série e bloco "Onde você está" já implementados.

### Parte 2 · Guias e sensores: como um agente aprende a se corrigir

`harness-p2.html`

Português apenas. Dezessete seções, três diagramas, 26 verbetes. Cerca de 6.200 palavras.

Reescrita completa depois de uma primeira versão descartada. A versão descartada falhava por abandonar a personagem, não fazer histórico da parte 1 e organizar por conceito em vez de pelo ciclo.

Conteúdo: abre na quarta semana com a diretora tendo escrito o guia inteiro e o sistema liberando nota de fornecedor descredenciado. Seções ancoradas em Equipar, Delegar e Inspecionar, com Reforçar no fim. Inclui a matriz de guias e sensores, a comparação entre mensagem de erro que ensina e alarme, o truque do limiar, a unidade de durabilidade, três exemplos completos com SKILL.md real, as classes de ambiente cruzadas com as faixas, e limpeza como cadência.

### Skill levantando-briefing

`skills/levantando-briefing/`

Artefato original do projeto, completo e pronto para repositório público. Quatro arquivos: SKILL.md, roteiro.md, modelo-briefing.md, README.md.

Decide se a automação deve existir, antes de discutir como funciona. Oito blocos, tabela determinística de derivação de faixa, veredito com três opções incluindo não fazer, e versionamento com comparação bloco a bloco.

Preenche uma lacuna verificada: existe farto material sobre como especificar, quase nada sobre como decidir se vale.

---

## Parcial

### Guia compacto de ferramentas e skills

`harness-caixa-de-ferramentas.html`

Existe em português, mas em formato antigo que precisa ser refeito. Dois problemas conhecidos:

**Organizado por categoria de produto**, que é a lógica de quem cataloga. Precisa ser organizado pelos cinco passos do MEDIR, que é a lógica de quem usa.

**As entradas são descritivas, não são fichas.** Falta o formato de seis campos definido em PADROES.md, e falta o material novo levantado depois: holdfast, planning-with-files, o guia inspirado em Karpathy, as skills de arquitetura, a limpeza como padrão com fonte verificada, e a nossa própria skill de briefing.

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
| Parte 2 | pronta | falta | falta |
| Guia compacto | a refazer | falta | falta |
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
