---
versao: 1
data: AAAA-MM-DD
area:
slug_da_tarefa:
solicitante:
revisor:
risco_de_governanca: nao          # sim, quando solicitante e revisor sao a mesma pessoa
exposicao:                        # interno | externo | externo indireto
faixa_recomendada:                # N0 | N1 | N2 | N3
faixa_determinada_por:
veredito:                         # fazer | simplificar | nao fazer
substitui:                        # v(N-1), ou vazio se for a primeira versao
mudancas_desde_a_versao_anterior:
  -
---

# Briefing: <nome da tarefa>

## 1. Identificação e governança

| Campo | Valor |
|---|---|
| Área | |
| Solicitante | |
| Revisor | |
| Data da entrevista | |
| Versão | |

## 2. Problema

**Incidente concreto relatado:**

**Frequência:**

**Quem sente:**

**Como é resolvido hoje:**

**Consequência de não fazer nada por doze meses:**

## 3. Exposição

| Campo | Valor |
|---|---|
| Classificação | interno / externo / externo indireto |
| Destinatário externo | |
| Destinatário sabe da automação | |
| Obrigação contratual ou regulatória | |

## 4. Integrações

| Sistema | Classificação | Dono do dado | Restrição contratual |
|---|---|---|---|
| | público / parceiro / cliente | | |

**Traz conteúdo escrito por terceiros:** sim / não
**Risco declarado:** conteúdo externo pode conter instrução dirigida ao sistema.

## 5. Volume e quantitativos

| Métrica | Valor | Origem |
|---|---|---|
| Ocorrências por mês | | |
| Pessoas envolvidas | | |
| Tempo por ocorrência | | |
| Pico | | |
| Taxa de erro atual | | |

Todo valor sem origem declarada deve constar como `desconhecido` com o responsável por levantar.

## 6. Entrada e saída

**Entrada:** formato, origem, variabilidade, qualidade

**Saída:** formato, destinatário, uso que ele faz

**Exemplo real anexado:** sim / não
Se não, a faixa fica travada em N1.

## 7. Retorno esperado

| Item | Valor | Origem |
|---|---|---|
| Horas liberadas por mês | | calculado do bloco 5 |
| Custo de um erro | | |
| Custo atual do processo | | |
| Destino do tempo liberado | | |

Se o destino do tempo liberado não estiver definido, o retorno é contábil e não operacional. Registre a distinção.

## 8. Risco, reversibilidade e alçada

| Campo | Valor |
|---|---|
| Reversibilidade | reversível / parcialmente reversível / irreversível |
| Pior caso se passar despercebido | |
| Quem aprova hoje | |

**Nunca pode acontecer:**
1.
2.
3.

## 9. Faixa recomendada

**Faixa:**
**Determinada por:**

Trava aplicada: sim / não. Se sim, qual.

## 10. Veredito

| Opção | Avaliação |
|---|---|
| Fazer agora | |
| Simplificar e refazer o briefing | |
| Não fazer | |

**Recomendação:**
**Justificativa em uma linha:**

A decisão é do revisor.

## 11. Contrato de tarefa resultante

Este bloco é o insumo direto do passo Mapear e alimenta a construção da skill.

**Entrega:**

**Não faz:**

**Pronto quando:**

**Nunca:**
