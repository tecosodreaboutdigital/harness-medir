# Roteiro de entrevista

Leia este arquivo antes de iniciar a entrevista. Uma pergunta por vez.

Cada bloco traz a pergunta de abertura, as reformulações para quando a resposta vier vaga, e o critério de saída que indica que o bloco está completo.

---

## Bloco 1 · Identificação e governança

**Abertura:** De que área é essa demanda, e quem está pedindo?

**Se vier vago:**
- "Um nome e um cargo, para eu registrar. O briefing precisa ser rastreável."
- "E quem vai revisar isso antes de virar decisão?"

**Se o revisor for o próprio solicitante:** "Registro assim, mas vou marcar como risco de governança. Ninguém revisa o próprio pedido com o mesmo rigor. Existe alguém que possa fazer a leitura crítica?"

**Saída:** área, solicitante com cargo, revisor com cargo, e número de versão definido.

---

## Bloco 2 · Problema

**Abertura:** Me descreve a última vez que esse problema aconteceu. Não o problema em geral, a última vez.

**Se vier abstrato:**
- "Isso é o objetivo. Eu quero o incidente. O que aconteceu, quando, com quem?"
- "Quem ficou sabendo? O que essa pessoa teve que fazer?"

**Perguntas seguintes:**
1. Com que frequência isso acontece?
2. Quem sente essa dor no dia a dia, por função?
3. Como isso é resolvido hoje, sem nada automatizado?
4. E se ficar exatamente como está pelos próximos doze meses, o que acontece?

**Atenção na pergunta 4.** Se a resposta for alguma variação de nada de grave, registre isso literalmente. É o indicador mais forte de veredito negativo, e ele aparece cedo.

**Saída:** um incidente concreto descrito, frequência, função afetada, processo atual e consequência da inação.

---

## Bloco 3 · Exposição

**Abertura:** O resultado disso fica dentro da empresa ou chega a alguém de fora?

Esta pergunta não admite talvez. Insista até obter uma das duas respostas.

**Se for externo:**
1. Chega a quem? Cliente, fornecedor, órgão regulador, público?
2. Essa pessoa sabe que existe automação envolvida?
3. Existe contrato ou norma que diga alguma coisa sobre esse resultado?

**Se o entrevistado disser interno mas o resultado alimentar algo externo:** "Então a saída direta é interna, mas ela vira insumo de algo que sai. Vou registrar como externo indireto, porque o risco viaja junto."

**Saída:** classificação binária registrada, destinatário nomeado se externo, e obrigação contratual mapeada.

---

## Bloco 4 · Integrações

**Abertura:** Para fazer isso, precisa ler ou escrever em algum sistema além de arquivos?

**Para cada sistema mencionado:**
1. Esse sistema é público, é de um fornecedor ou parceiro, ou é do cliente?
2. Quem é o dono do dado ali dentro?
3. Existe contrato limitando o que pode ser feito com esse dado?

**Se houver sistema de cliente:** "Isso muda a faixa recomendada para o topo. O dado não é seu, a responsabilidade por vazamento é, e a autorização pode ser revogada sem aviso. Confirma que é necessário mesmo?"

**Pergunta obrigatória de fechamento:** Alguma dessas integrações traz texto escrito por gente de fora, como e-mail, formulário, documento enviado ou comentário?

Se sim, registre como risco declarado: conteúdo externo pode conter instrução dirigida ao sistema.

**Saída:** lista de sistemas classificados, donos de dado nomeados, e sinalização de conteúdo externo.

---

## Bloco 5 · Volume e quantitativos

**Abertura:** Quantas vezes isso acontece por mês? E de onde vem esse número?

**A segunda parte é obrigatória em toda resposta numérica.** Se não houver origem:
- "Isso é estimativa ou tem relatório? Se for estimativa, registro como desconhecido e coloco quem vai levantar."

**Perguntas seguintes:**
1. Quantas pessoas participam disso hoje?
2. Quanto tempo cada ocorrência toma, por pessoa?
3. Tem pico? Quando?
4. Alguém mede a taxa de erro atual?

**Se volume baixo e tempo curto:** "Pelo que você me deu, isso soma cerca de X horas por mês. Vale eu continuar? Automatizar volume baixo costuma custar mais do que rende."

Não continue por educação. Ofereça a saída.

**Saída:** volume com origem, pessoas envolvidas, tempo unitário, pico e taxa de erro, cada um com origem ou marcado desconhecido com responsável.

---

## Bloco 6 · Entrada e saída

**Abertura:** O que entra nesse processo, e em que formato?

**Perguntas seguintes:**
1. Essa entrada é sempre igual ou varia bastante?
2. Qual é a qualidade dela? Vem limpa ou precisa de tratamento?
3. O que sai no final, e para quem?
4. O que essa pessoa faz com o que recebe?

**Pergunta de fechamento, a mais importante do bloco:** Você consegue me mandar um exemplo real de entrada, e um exemplo de uma saída que você considerou boa?

**Se disser que não tem:** "Sem um exemplo de saída boa, ninguém consegue verificar se o resultado está certo, nem eu nem o sistema. Isso vai travar a faixa em N1. Consegue produzir um exemplo?"

**Saída:** formato de entrada, variabilidade, formato de saída, consumidor final, e existência ou não de exemplo real.

---

## Bloco 7 · Retorno esperado

**Abertura:** Com os números do bloco anterior, isso dá cerca de X horas por mês. Confere?

Faça a conta na frente do entrevistado e mostre.

**Perguntas seguintes:**
1. Quando dá errado hoje, quanto custa o erro?
2. Alguém já calculou o custo atual desse processo?
3. E a pessoa que hoje faz isso, o que ela passaria a fazer?

**Atenção na pergunta 3.** Se ninguém souber, registre literalmente: destino do tempo liberado não definido. Isso muda a leitura do retorno de ganho real para ganho contábil, e o revisor precisa ver essa distinção.

**Saída:** horas liberadas calculadas, custo do erro, custo atual se conhecido, e destino do tempo liberado.

---

## Bloco 8 · Risco, reversibilidade e alçada

**Abertura:** Se o sistema fizer isso errado e ninguém perceber na hora, dá para desfazer?

**Classifique em três:** reversível, parcialmente reversível, irreversível.

**Perguntas seguintes:**
1. Qual é o pior resultado possível se sair errado e passar despercebido?
2. Hoje, quem aprova antes de isso ter efeito?
3. O que nunca pode acontecer, em nenhuma hipótese?

**A pergunta 3 merece tempo.** Peça pelo menos três respostas. Elas viram a seção Nunca da skill que for construída depois, e é a seção que mais evita incidente.

**Saída:** classificação de reversibilidade, pior caso descrito, alçada atual nomeada, e lista de proibições absolutas.

---

## Fechamento

1. Aplique a tabela de derivação de faixa do SKILL.md, em ordem.
2. Diga ao entrevistado qual faixa saiu e qual condição a determinou.
3. Apresente as três opções de veredito, com a recomendação marcada.
4. Gere o arquivo no formato de `modelo-briefing.md`.
5. Confirme com o entrevistado quem é o revisor e informe que a decisão é dele.

**Nunca encerre dizendo que vai começar a construir.** Esta skill termina no briefing.
