# levantando-briefing

**Uma skill que decide se a automação deve existir, antes de discutir como ela funciona.**

Existe farto material sobre como especificar bem uma tarefa para um agente de IA. Quase nada sobre como decidir se ela deve ser feita. Esta skill cobre a segunda pergunta, que vem antes.

---

## O problema

O comportamento padrão de um sistema de linguagem é obediência solícita. Pedem uma automação e ele começa a produzir, sem perguntar o volume, sem perguntar quem recebe o resultado, sem perguntar o que acontece se sair errado.

As skills de entrevista que existem hoje resolvem metade disso, e resolvem bem: levantam requisito técnico, sondam caso de borda, travam em falha de segurança. Nenhuma pergunta quantas vezes por mês, quanto custa o erro, quem revisa, se o resultado sai da empresa, ou se vale a pena fazer.

Isso não é levantamento de requisito. É briefing de negócio, e é a pergunta que quem decide faz primeiro.

---

## O que ela entrega

Três coisas, sempre:

**Um contrato de tarefa.** O que entrega, o que não faz, quando está pronto e o que nunca pode acontecer. É o insumo direto da construção que vier depois.

**Uma faixa de autonomia recomendada,** de N0 a N3, derivada por tabela a partir de reversibilidade, exposição externa, tipo de integração e volume. O leitor descobre em que faixa a tarefa deve operar antes de escolher qualquer ferramenta.

**Um veredito com três opções:** fazer agora, simplificar e refazer o briefing, ou não fazer. A terceira opção é a que nenhuma skill de mercado oferece, e costuma ser a mais valiosa.

---

## Princípios

**Nenhum número entra sem origem declarada.** Se o entrevistado não sabe, registra desconhecido e quem vai descobrir. Um briefing com número inventado é pior que briefing nenhum, porque autoriza decisão com base falsa.

**Sem verificação não existe autonomia.** Se ninguém consegue descrever como conferir que a saída está correta, a faixa trava em N1 por mais atraente que o retorno pareça.

**O revisor não é o solicitante.** Quando for a mesma pessoa, o briefing registra isso como risco de governança.

**Versionar é o ponto.** O valor histórico está em ver a estimativa mudar quando o número real aparece. Nunca sobrescreva a versão anterior.

---

## Os oito blocos

| # | Bloco | O que decide |
|---|---|---|
| 1 | Identificação e governança | Rastreabilidade e quem aprova |
| 2 | Problema | Se a dor existe de verdade |
| 3 | Exposição, interno ou externo | O risco de tudo o que vem depois |
| 4 | Integrações | De quem é o dado e o que pode ser feito com ele |
| 5 | Volume e quantitativos | Se a conta fecha |
| 6 | Entrada e saída | Se existe como verificar o resultado |
| 7 | Retorno esperado | Se o ganho é real ou contábil |
| 8 | Risco, reversibilidade e alçada | Em que faixa isso pode operar |

---

## Instalação

```
git clone https://github.com/tecosodreaboutdigital/harness-medir.git
cp -r harness-medir/skills/levantando-briefing ~/.claude/skills/levantando-briefing
```

Para outros ambientes, copie a pasta para onde eles carregam skills. O caminho acima é a convenção de um ambiente específico, não uma exigência do formato.

**Dependências:** nenhuma. É texto.

---

## Uso

```
/levantando-briefing
/levantando-briefing "queremos automatizar a conferência de notas de frete"
/levantando-briefing briefings/briefing-operacoes-notas-frete-v2.md
```

O terceiro caso lê a versão anterior e gera a seguinte, preenchendo o campo de mudanças bloco a bloco.

---

## O que tem na pasta

```
levantando-briefing/
├── SKILL.md              a skill
├── roteiro.md            as perguntas, com reformulações para resposta vaga
├── modelo-briefing.md    o modelo de saída, com cabeçalho de versionamento
└── README.md             este arquivo
```

---

## Limites honestos

**Não substitui entrevista técnica.** Ela decide se faz e em que faixa. O detalhamento de como fazer é outro trabalho, e existem boas skills de terceiros para isso.

**Não estima prazo nem custo de desenvolvimento.** Deliberadamente. Estimativa de prazo em briefing vira compromisso, e compromisso antes de desenho é como se produz atraso.

**A tabela de faixas é opinativa.** Os limiares saíram de experiência e não de estudo. Ajuste para a sua realidade e registre o ajuste.

**Sem suíte de avaliação.** O teste que vale é direto: conduza dois briefings da mesma tarefa com pessoas diferentes e compare os números que saíram. Se divergirem muito, o problema está nas perguntas, não nos entrevistados.

---

## Origem

Parte da série Harness e do ciclo MEDIR: Mapear, Equipar, Delegar, Inspecionar, Reforçar. Este briefing é a porta de entrada do passo Mapear.

MIT.
