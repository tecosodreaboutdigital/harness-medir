---
name: levantando-briefing
description: Conduz uma entrevista estruturada antes de qualquer construção com IA, para decidir se a tarefa deve ser automatizada, em que faixa de autonomia ela deve operar, e qual é o contrato de tarefa resultante. Use quando alguém pedir para automatizar um processo, criar um agente, montar uma skill ou construir uma automação, e ainda não existir um briefing versionado.
---

# Levantando briefing

Esta skill não especifica como construir. Ela decide se deve ser construído, com que grau de autonomia, e produz o contrato de tarefa que alimenta os passos seguintes do ciclo MEDIR.

Existe farto material sobre como especificar bem. Quase nada sobre como decidir se vale a pena. Esta skill cobre a segunda pergunta, que vem antes.

## Contrato da tarefa

**Entrega:** um arquivo de briefing versionado contendo o contrato de tarefa, a faixa de autonomia recomendada e um veredito de viabilidade com opções.

**Não faz:** não desenha solução técnica, não escolhe ferramenta, não escreve código, não estima prazo de desenvolvimento e não aprova nada.

**Pronto quando:** os oito blocos foram percorridos, cada resposta obrigatória está preenchida ou explicitamente marcada como desconhecida com o responsável por descobrir, a faixa foi derivada pela tabela de decisão, e o arquivo foi salvo no padrão de versionamento.

## Regra inegociável

**Nenhum número entra no briefing sem origem declarada.**

Se o entrevistado não sabe um quantitativo, registre desconhecido e quem vai descobrir. Nunca estime em nome dele.

Bandeiras vermelhas. Pare se você se pegar pensando assim:

- "deve ser mais ou menos umas cinquenta por dia"
- "o ganho provavelmente é grande"
- "isso normalmente leva uns vinte minutos"
- "posso assumir que é interno"
- "dá para inferir a área pelo contexto"

Nenhuma das cinco é levantamento. Todas são invenção com voz de autoridade, e um briefing com número inventado é pior que briefing nenhum, porque autoriza decisão com base falsa.

## Como conduzir

1. Uma pergunta por vez. Nunca despeje o questionário inteiro.
2. Sempre que a resposta for abstrata demais para um estranho agir a partir dela, pergunte de novo, mais específico.
3. Quando o entrevistado se contradisser, aponte a contradição na hora e peça que ele decida.
4. Ao final de cada bloco, repita em uma frase o que entendeu e peça confirmação antes de avançar.
5. Se um bloco revelar que a tarefa não deve existir, diga isso imediatamente. Não termine a entrevista por educação.

O roteiro completo de perguntas, com as reformulações para quando a resposta vier vaga, está em `roteiro.md`. Leia esse arquivo antes de começar a entrevista.

## Os oito blocos

### 1. Identificação e governança

Obrigatório. Sem isso o briefing não é rastreável e não serve para comparação histórica.

- Área ou departamento responsável
- Quem está solicitando, com cargo
- Quem vai revisar e aprovar este briefing, nominalmente
- Versão deste briefing e o que mudou em relação à anterior, se houver

O revisor nunca é o solicitante. Se a mesma pessoa ocupa os dois papéis, registre isso explicitamente como risco de governança no briefing.

### 2. Problema

- Qual é a dor, descrita como um evento concreto e não como um objetivo
- Quem sente essa dor, por nome de função
- Com que frequência ela acontece
- O que acontece hoje, sem nada automatizado
- O que acontece se ficar exatamente como está pelos próximos doze meses

A última pergunta é a mais reveladora do bloco. Se a resposta for nada de grave, o veredito provavelmente é não fazer agora.

### 3. Exposição: interno ou externo

Esta classificação muda tudo o que vem depois. Ela é obrigatória e não admite talvez.

- O resultado fica dentro da empresa ou chega a alguém de fora
- Se chega a alguém de fora, quem é: cliente, fornecedor, órgão regulador, público geral
- O destinatário externo sabe que há automação envolvida
- Existe obrigação contratual ou regulatória sobre esse resultado

Um resultado que chega a cliente é sempre irreversível na prática, mesmo quando é tecnicamente possível corrigir depois. Retratação custa mais que o erro.

### 4. Integrações

- A tarefa precisa ler ou escrever em algum sistema além dos arquivos locais
- Para cada sistema, classifique: público, privado de fornecedor ou parceiro, ou privado do cliente
- Quem é o dono do dado em cada um deles
- Existe contrato ou acordo que limite o uso desse dado

Sistema privado de cliente é a classificação de maior risco de todas, e por três razões: o dado não é seu, a responsabilidade por vazamento é sua, e a autorização pode ser revogada sem aviso.

Registre também se alguma integração traz conteúdo escrito por terceiros. Texto vindo de fora pode conter instrução dirigida ao sistema, e isso precisa aparecer no briefing como risco declarado.

### 5. Volume e quantitativos

Todos com origem declarada.

- Quantas ocorrências por dia, semana ou mês
- Quantas pessoas envolvidas hoje
- Quanto tempo cada ocorrência consome, hoje, por pessoa
- Qual é o pico e quando ele acontece
- Qual é a taxa de erro atual, se conhecida

Se o volume for baixo e o tempo por ocorrência for pequeno, diga isso ao entrevistado antes de continuar. Automatizar algo que acontece três vezes por mês e leva dez minutos raramente se paga.

### 6. Entrada e saída

- O que entra, em que formato, vindo de onde, com que qualidade
- A entrada é padronizada ou varia
- O que sai, em que formato, para quem
- Quem consome a saída e o que faz com ela
- Existe um exemplo real de entrada e de saída boa que possa ser anexado

O último item é o mais valioso do bloco inteiro. Um exemplo real de saída boa vale mais que três parágrafos descrevendo o que seria uma saída boa.

### 7. Retorno esperado

- Horas liberadas por período, calculadas a partir do bloco 5
- Erro evitado, com o custo de um erro quando acontece
- Custo atual do processo, se conhecido
- O que a pessoa liberada passaria a fazer

A última pergunta separa ganho real de ganho contábil. Se ninguém sabe o que a pessoa faria com o tempo liberado, o ganho ainda não existe.

### 8. Risco, reversibilidade e alçada

- A ação produzida é reversível, parcialmente reversível ou irreversível
- Qual é o pior resultado possível se sair errado e ninguém perceber
- Quem aprova antes de a ação ter efeito
- O que nunca pode acontecer, em nenhuma hipótese

O último item vira a seção Nunca da skill que for construída depois. Colete com cuidado.

## Derivação da faixa

Aplique a tabela na ordem. A primeira linha que der verdadeira define a faixa mínima, e as seguintes não reduzem.

| Condição | Faixa mínima |
|---|---|
| Ação irreversível com efeito externo | N3 |
| Integração com sistema privado de cliente | N3 |
| Efeito externo, mesmo reversível | N2 |
| Integração com sistema de fornecedor ou parceiro | N2 |
| Volume acima de cem ocorrências por mês | N2 |
| Interno, reversível, sem integração privada | N1 |
| Nenhum sensor identificável para a saída | teto em N1, independente do restante |

A última linha é uma trava, não uma faixa. Se ninguém consegue descrever como verificar que a saída está correta, a tarefa não sobe de N1 por mais atraente que o retorno pareça. Sem verificação não existe autonomia responsável.

Registre no briefing tanto a faixa quanto qual linha da tabela a determinou.

## Veredito

Sempre três opções, nunca uma recomendação única.

**Fazer agora.** Volume justifica, retorno é mensurável, faixa é compatível com o ambiente disponível, e existe sensor identificável.

**Simplificar e refazer o briefing.** O escopo atual não se paga ou exige faixa acima do ambiente disponível. Aponte o que precisa ser cortado e o que muda na conta se for cortado.

**Não fazer.** Volume baixo, retorno não identificável, ou risco desproporcional. Escreva o motivo em uma frase e o que precisaria mudar para reconsiderar.

Apresente as três com a recomendação marcada e a justificativa em uma linha cada. A decisão é do revisor, não sua.

## Versionamento

O briefing existe para ser comparado ao longo do tempo. Sem versão, ele vira um documento morto.

Nome do arquivo:

```
briefing-<area>-<slug-da-tarefa>-v<N>.md
```

Cabeçalho obrigatório em todo briefing, no formato de `modelo-briefing.md`:

```
versao: 3
data: 2026-08-30
area: operacoes
solicitante: Nome, Cargo
revisor: Nome, Cargo
faixa_recomendada: N2
faixa_determinada_por: efeito externo, mesmo reversivel
veredito: simplificar
substitui: v2
mudancas_desde_a_versao_anterior:
  - volume corrigido de 40 para 320 ocorrencias por mes, origem: relatorio de chamados
  - integracao com sistema do cliente descartada
  - faixa caiu de N3 para N2
```

Ao gerar uma nova versão, leia a anterior primeiro e preencha o campo de mudanças comparando bloco a bloco. Nunca sobrescreva a versão anterior. O valor histórico está justamente em ver a estimativa mudar quando o número real aparece.

## Nunca

- Nunca invente número, prazo, volume ou percentual.
- Nunca marque uma tarefa como interna sem perguntar explicitamente.
- Nunca omita o veredito de não fazer quando ele for o correto.
- Nunca conclua a entrevista com blocos obrigatórios em branco. Marque desconhecido e nomeie quem descobre.
- Nunca registre o solicitante como revisor sem sinalizar o risco de governança.
- Nunca avance para desenho de solução dentro desta skill. Ela termina no briefing.

## Arquivos desta skill

```
levantando-briefing/
├── SKILL.md              este arquivo
├── roteiro.md            as perguntas, com reformulações para resposta vaga
└── modelo-briefing.md    o modelo de saída, com cabeçalho de versionamento
```

## Origem

Parte da série Harness e do playbook MEDIR. O briefing é a porta de entrada do passo Mapear: ele decide se a tarefa existe e em que faixa opera, antes de qualquer discussão sobre ferramenta.

Licença MIT.
