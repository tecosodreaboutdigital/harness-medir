# harness-medir — Revisão de português: consolidação final

Este arquivo substitui todos os anteriores desta revisão (`revisao-portugues-harness-medir.md`, `revisao-portugues-harness-medir-rodada2.md`, `revisao-portugues-harness-medir-final.md`, `harness-medir-ontologia-e-alteracoes.md`, `harness-medir-fechamento-sensor-killswitch.md`). Nenhum deles precisa ser lido depois deste. Onde uma decisão mudou entre um arquivo e outro ao longo da conversa (por exemplo, "titular" foi cogitado e depois trocado por "proprietário"; "kill switch" em inglês foi cogitado e depois revertido para "botão de desligar"), o que vale é o que está escrito aqui.

**Correção feita nesta consolidação, em relação ao arquivo anterior:** os ids HTML do glossário (`id="pt-g-sensor"`, `id="pt-g-agent-owner"`, etc.) não mudam nunca, mesmo quando a palavra visível ao leitor muda. O próprio glossário já segue esse padrão (o id `en-g-reversibilidade` existe na versão em inglês, mantendo o slug em português). Isso elimina a necessidade de renomear qualquer id ou corrigir qualquer link, inclusive para "sensor" → "verificador". Só o texto dentro da tag muda.

**Escopo coberto:** README, STANDARDS, STATUS e TOOLS (as três versões em português enviadas), harness-glossary.html, harness-p1.html a harness-p4.html, harness-toolkit.html, harness-sources.html, docs/logbook.html. `NEXT-STEPS.pt.md` ficou de fora por decisão sua, documento interno de baixa relevância pro repositório público.

---

# PARTE 1 — Ontologia de português (referência permanente)

Sugestão mantida: este bloco pode virar `GLOSSARIO-DE-ESTILO.pt.md` na raiz do repositório, citado a partir de `STANDARDS.pt.md`.

## 1.1 Termos decididos

| Termo EN | Termo PT final | O que muda no texto | Não muda |
|---|---|---|---|
| agent owner | **proprietário do agente** (era "dono") | O texto visível em toda ocorrência | O id `pt-g-agent-owner` no glossário, e qualquer outro id |
| sensor | **verificador** (era "sensor") | O texto visível em toda ocorrência, exceto as exceções da seção 2.4 abaixo | O id `pt-g-sensor`, o nome da ferramenta `sensors-cli`, o título do artigo de Böckeler |
| human in the loop | **mantido em inglês** (era "no laço") | Troca "no laço" pela expressão em inglês, com verbete novo no glossário explicando a escolha | "laço" como laço de repetição/tentativa continua igual, não é a mesma coisa |
| lethal trifecta | **trinca letal** (era "trifeta letal") | O texto visível em toda ocorrência | O id do glossário, se houver, e o nome de Simon Willison como autor da formulação |
| kill switch | **botão de desligar** (confirmado, sem mudança) | Nada. O texto já usa esse termo em todas as ocorrências | — |
| submission (jurídico, Parte 3 §1) | **alegação** (era "submissão") | Título da seção e as três ocorrências no corpo | O nome do caso, Moffatt v Air Canada |
| negligent misrepresentation | **declaração falsa por negligência** (era "declaração negligente") | Uma ocorrência, Parte 3 §1 | — |
| "you own what it said" | **"você responde pelo que foi dito"** (era "você é dono do que foi dito") | Duas ocorrências, abertura e fechamento da Parte 3 | — |

## 1.2 Padrões de construção de frase (não são uma palavra, são um hábito a corrigir com moderação)

- **"não é X, é Y"**: `STANDARDS.pt.md` já proíbe o abuso desta construção. Pelo menos sete ocorrências reais encontradas (Parte 1 §4, §5; Parte 4 §2, §5; glossário `pt-g-agent-office`; `TOOLS.pt.md`). Reescrever pelo menos metade, variando a forma a cada vez, não trocando uma repetição por outra.
- **Substantivo composto no molde inglês "[adjetivo]-sounding [substantivo]"**: reescrever com verbo em português ("uma pergunta que soa menor" em vez de "uma pergunta de som menor"). O próprio texto já faz isso certo em outro lugar ("um indicador que soa como opinião"), prova de que o problema é de construção, não de vocabulário.
- **"contar" ambíguo entre contar números e contar uma história**: trocar por "contabilizar" quando o contexto permitir a leitura dupla, especialmente em títulos de seção.

## 1.3 O que já está bom (não mexer, serve de modelo)

- separação de poderes, matriz de alçada, regra de dois — reaproveitam vocabulário já consagrado em português.
- "o revisor que carimba", "dar crachá e autoridade real ao guarda que antes só observava" — metáforas traduzidas inteiras, não palavra por palavra.
- conversão de moeda nos exemplos (US$ 0,31 → R$ 1,55) — adapta o exemplo ao leitor brasileiro de verdade, não só troca símbolo.
- terminologia jurídica da LGPD e do AI Act europeu — precisa e consistente.
- `docs/logbook.html` — log técnico gerado automaticamente, registro terso e factual, sem os problemas de registro da prosa narrativa. Nenhuma alteração recomendada ali.

## 1.4 Verbete novo para o glossário (as três línguas, ordem alfabética por "h")

**Português**, a inserir em `harness-glossary.html`:
> **human in the loop**: Mantido em inglês nesta série de propósito. Não existe tradução em português igualmente natural fora do sentido técnico de laço de repetição; o espanhol da própria série usa "bucle" com sucesso, mas o português não tem equivalente com a mesma naturalidade. O termo já circula como jargão internacional de IA mesmo em texto em português.

---

# PARTE 2 — Lista de alterações, com localização exata e texto antes/depois

## 2.1 "dono do agente" → "proprietário do agente" (oito ocorrências)

**harness-glossary.html, linha 480 (o verbete em si):**

Antes:
> \<strong>dono do agente\</strong>: O papel que opera um agente e responde pelo risco que ele gera. Uma pessoa nomeada, nunca um departamento, e nunca combinado com o papel de homologador.

Depois:
> \<strong>proprietário do agente\</strong>: O papel que opera um agente e responde pelo risco que ele gera. Uma pessoa nomeada, nunca um departamento, e nunca combinado com o papel de homologador.

(O `id="pt-g-agent-owner"` não muda.)

**harness-glossary.html, linha 498 (verbete do Modelo das Três Linhas, menciona "dona do risco"):**

Antes:
> [...] Quadro do Instituto dos Auditores Internos que separa a gestão dona do risco (primeira linha) [...]

Depois:
> [...] Quadro do Instituto dos Auditores Internos que separa a gestão proprietária do risco (primeira linha) [...]

**harness-p4.html, linha 645:**

Antes:
> [...] a transição para descomissionado no diagrama acima exige uma decisão do dono do agente e do homologador juntos, nunca uma automação rodando numa agenda.

Depois:
> [...] a transição para descomissionado no diagrama acima exige uma decisão do proprietário do agente e do homologador juntos, nunca uma automação rodando numa agenda.

**harness-p4.html, linha 722 (duas ocorrências na mesma linha, "dona do risco" e "dono do agente"):**

Antes:
> [...] A primeira linha opera e é dona do risco que gera, exatamente o trabalho do \<a [...]\>dono do agente\</a\>. A segunda linha assiste, monitora e desafia a primeira [...]

Depois:
> [...] A primeira linha opera e é proprietária do risco que gera, exatamente o trabalho do \<a [...]\>proprietário do agente\</a\>. A segunda linha assiste, monitora e desafia a primeira [...]

(O texto do `data-tip` na mesma linha, que também diz "dono do agente" duas vezes, muda junto: "O papel que opera um agente..." e "Não pode ser exercido pelo dono do agente" → "pelo proprietário do agente".)

**harness-toolkit.html, linha 880:**

Antes:
> \<strong\>Problema.\</strong\> A parte 4 §3 é explícita que a transição para descomissionado exige uma decisão do dono do agente e do homologador juntos [...]

Depois:
> \<strong\>Problema.\</strong\> A parte 4 §3 é explícita que a transição para descomissionado exige uma decisão do proprietário do agente e do homologador juntos [...]

**STATUS.pt.md, linhas 71, 105, 161:** documento interno, mesma troca por consistência, prioridade baixa. A linha 161 é a mais importante das três porque registra a decisão de vocabulário por escrito: "dono do agente, homologador [...]" → "proprietário do agente, homologador [...]".

## 2.2 "você é dono do que foi dito" → "você responde pelo que foi dito" (duas ocorrências)

**harness-p3.html, linhas 482 e 918 (abertura e fechamento da Parte 3, frase idêntica nas duas):**

Antes:
> Se falou em seu nome, você é dono do que foi dito.

Depois:
> Se falou em seu nome, você responde pelo que foi dito.

## 2.3 "submissão" → "alegação", e "declaração negligente" → "declaração falsa por negligência"

**harness-p3.html, linha 462 (sumário):**

Antes:
> \<li\>\<a href="#pt-opening"\>Uma submissão notável\</a\>\</li\>

Depois:
> \<li\>\<a href="#pt-opening"\>Uma alegação e tanto\</a\>\</li\>

**harness-p3.html, linha 474 (título da seção 1):**

Antes:
> \<h2 id="pt-opening"\>1. Uma submissão notável\</h2\>

Depois:
> \<h2 id="pt-opening"\>1. Uma alegação e tanto\</h2\>

(O id `pt-opening` não muda.)

**harness-p3.html, linha 480 (corpo do parágrafo, as duas correções juntas):**

Antes:
> [...] e chamou o argumento de uma submissão notável. O tribunal considerou que a companhia tinha um dever de cuidado decorrente da relação comercial, encontrou declaração negligente, e determinou o pagamento.

Depois:
> [...] e chamou aquilo de uma alegação e tanto. O tribunal considerou que a companhia tinha um dever de cuidado decorrente da relação comercial, reconheceu declaração falsa por negligência, e determinou o pagamento.

**Verificar também:** qualquer referência à Parte 3 nas tabelas finais das outras partes que cite o título da seção 1 pelo nome antigo. Não encontrei nenhuma nesta revisão (as tabelas "onde você está" resumem a Parte 3 pelo conteúdo geral, não pelo título de cada seção), mas vale checar antes de fechar.

## 2.4 "sensor" → "verificador" (124 ocorrências, com quatro exceções)

**Regra geral:** dentro da seção em português de `harness-glossary.html`, `harness-p1.html`, `harness-p2.html`, `harness-p3.html`, `harness-p4.html` e `harness-toolkit.html`, trocar "sensor/sensores/Sensor/Sensores" por "verificador/verificadores/Verificador/Verificadores", exceto nos quatro casos abaixo. Contagem por arquivo: glossário 9, Parte 1 12, Parte 2 58, Parte 3 5, Parte 4 4, guia compacto 36.

**Exceção 1, nunca traduzir:** o nome da ferramenta real `sensors-cli` (`github.com/birgitta410/sensors-cli`), toda vez que aparece como nome próprio (título de ficha, texto de link, citação de repositório). Ocorre em `harness-toolkit.html` linhas 698, 707, 905, 907, 1012, e em `harness-sources.html` linhas 495 (mais as versões em inglês e espanhol, que não mudam de qualquer forma).

Exemplo de como separar as duas coisas na mesma frase (`harness-toolkit.html`, linha 907):

Antes:
> O sensors-cli, já coberto em Inspecionar, é um painel que roda vários sensores em intervalo e guarda histórico. [...] aponte [...] do mesmo jeito que ele já aponta para sensores de verificação dura [...]

Depois:
> O sensors-cli, já coberto em Inspecionar, é um painel que roda vários verificadores em intervalo e guarda histórico. [...] aponte [...] do mesmo jeito que ele já aponta para verificadores de verificação dura [...]

**Exceção 2, nunca traduzir:** o título do artigo de Birgitta Böckeler, "Maintainability sensors for coding agents", citado em inglês em `harness-sources.html` (prática já correta do projeto, todo título de fonte fica no idioma original).

**Exceção 3, não renomear:** o id `id="pt-g-sensor"` no glossário (linha 514) e o id `id="pt-src-bockeler-sensors"` / `id="pt-src-sensors-cli"` em `harness-sources.html`. Só o texto dentro da tag muda, o id fica igual, pelo padrão já explicado no início deste arquivo.

Exemplo completo do verbete (`harness-glossary.html`, linha 514):

Antes:
> \<p class="gitem" id="pt-g-sensor"\>\<strong\>sensor\</strong\>: Controle que age depois da execução, medindo o que foi produzido e devolvendo ao agente a informação necessária para que ele se corrija. Chamado de controle por realimentação. [...]\</p\>

Depois:
> \<p class="gitem" id="pt-g-sensor"\>\<strong\>verificador\</strong\>: Controle que age depois da execução, medindo o que foi produzido e devolvendo ao agente a informação necessária para que ele se corrija. Chamado de controle por realimentação. Chamado de "sensor" no artigo original de Böckeler, ver a fonte. [...]\</p\>

(Frase final acrescentada, opcional, credita o termo original em inglês já que a fonte citada logo depois usa "sensor".)

E o único link do repositório que aponta para esse verbete (`harness-p2.html`, linha 506), onde só o texto visível do link muda, o `href` fica igual:

Antes:
> \<a class="g" href="harness-glossary.html#pt-g-sensor" [...]\>Sensores\</a\> são os controles que observam. [...]

Depois:
> \<a class="g" href="harness-glossary.html#pt-g-sensor" [...]\>Verificadores\</a\> são os controles que observam. [...]

**Exceção 4, opcional, é escolha estética, não obrigação:** o campo `"sensores"` no JSON de exemplo do recibo (`harness-p2.html`, linhas 891 e 1988). Pode virar `"verificadores"` por consistência total, ou ficar como está, tratado como nome de campo técnico. Sem recomendação forte.

**Pontos de maior visibilidade, para conferir primeiro:**

Título da Parte 2 (h1):
> Antes: "Guias e sensores: como um agente aprende a se corrigir"
> Depois: "Guias e verificadores: como um agente aprende a se corrigir"

Sumário e títulos de seção da Parte 2 (linhas 468 a 470 do sumário, e os `<h2>` correspondentes nas linhas 670, 715, 751):
> "Inspecionar: o sensor que ensina" → "Inspecionar: o verificador que ensina"
> "Onde cada sensor dispara" → "Onde cada verificador dispara"
> "O que sensor nenhum pega" → "O que verificador nenhum pega"

(Os ids dessas seções, `pt-inspecionar`, `pt-onde-dispara`, `pt-nao-pega`, não contêm a palavra "sensor" e não mudam.)

Referências cruzadas nas tabelas finais das Partes 1, 3 e 4 ("Guias e sensores, o formato de skill, três exemplos completos..." resumindo a Parte 2): mesma troca, checar as três ocorrências.

## 2.5 "no laço" → "human in the loop" (seis ocorrências)

**harness-glossary.html, linha 510 (verbete "regra de dois"):**

Antes:
> [...] Sem humano no laço, um agente pode satisfazer no máximo duas delas. [...]

Depois:
> [...] Sem human in the loop, um agente pode satisfazer no máximo duas delas. [...]

**harness-p3.html, linha 603:**

Antes:
> Responda as três com honestidade. Sem humano no laço, um agente pode satisfazer no máximo duas delas. No momento em que uma ação responderia sim às três, um humano precisa estar no laço antes de ela executar, sem exceção aberta por urgência ou inconveniência.

Depois:
> Responda as três com honestidade. Sem human in the loop, um agente pode satisfazer no máximo duas delas. No momento em que uma ação responderia sim às três, é preciso ter um humano no processo de decisão antes de ela executar, sem exceção aberta por urgência ou inconveniência.

**harness-p3.html, linha 660:**

Antes:
> A regra de dois responde se um humano precisa estar no laço. Uma pergunta separada, mais antiga, é de quanta autoridade o próprio laço precisa, e a resposta honesta passa pela reversibilidade, não pela importância aparente de uma ação.

Depois:
> A regra de dois responde se a ação exige human in the loop. Uma pergunta separada, mais antiga, é de quanta autoridade essa presença humana precisa, e a resposta honesta passa pela reversibilidade, não pela importância aparente de uma ação.

**harness-p3.html, linha 671 (célula de tabela):**

Antes:
> \<td\>Humano no laço, independente da classe\</td\>

Depois:
> \<td\>Human in the loop, independente da classe\</td\>

**harness-p3.html, linha 695:**

Antes:
> [...] É também o padrão que mais preocupa reguladores, porque não há humano no laço para responsabilizar no momento em que a ação acontece. [...]

Depois:
> [...] É também o padrão que mais preocupa reguladores, porque não há human in the loop para responsabilizar no momento em que a ação acontece. [...]

**harness-p3.html, linha 706 (célula de tabela):**

Antes:
> \<td\>Totalmente autônomo, disparado por evento ou agenda, sem humano no laço\</td\>

Depois:
> \<td\>Totalmente autônomo, disparado por evento ou agenda, sem human in the loop\</td\>

**STATUS.pt.md, linha 59:** documento interno, mesma troca por consistência, prioridade baixa (é um parágrafo longo de changelog, a frase relevante é "no máximo duas sem humano no laço").

## 2.6 "trifeta letal" → "trinca letal" (duas ocorrências)

**harness-glossary.html, linha 522, e harness-p3.html, linha 773** (a segunda tem duas ocorrências na mesma linha): trocar "trifeta" por "trinca" em todas.

## 2.7 "Tier mínimo" → "Faixa mínima" (uma ocorrência, correção de inconsistência interna)

**harness-toolkit.html, linha 725** (ficha da skill `research`):

Antes:
> Tier mínimo. N1.

Depois:
> Faixa mínima. N1.

(Mesma ficha também tem "Para quem é." em vez de "Para quem.", e "N1 pra cima" em vez do "N1 em diante"/"N1 para cima" usado nas outras 28 fichas — ajustar os três juntos, já que aparentam ter sido escritos em separado do resto do documento.)

## 2.8 Construções de frase — exemplos concretos para reescrever

**"não é X, é Y", exemplo de maior repetição (Parte 4 §2, §8, e glossário `pt-g-agent-office`, quase idêntica nas três):**

Antes:
> Não é um produto que a empresa compra, é uma função que ela organiza.

Depois (variar a cada ocorrência, não repetir a mesma frase nova três vezes):
> A empresa organiza essa função, não a compra pronta.

**"TOOLS.pt.md", linha 44:**

Antes:
> `intake-briefing` não é instalada de terceiro, é criada por este projeto.

Depois:
> `intake-briefing` é criada por este projeto, não instalada de terceiro.

**"pergunta de som bem menor" (deck de abertura da Parte 4):**

Antes:
> [...] era uma pergunta de som bem menor que acaba sendo a mais difícil da série inteira [...]

Depois:
> [...] era uma pergunta que soa bem menor do que é, mas acaba sendo a mais difícil da série inteira [...]

**"ninguém contou" (título da Parte 4, seção 2):**

Antes:
> ## 2. A diretora volta à cena, e desta vez ninguém contou

Depois:
> ## 2. A diretora volta à cena, e desta vez ninguém contabilizou

---

# PARTE 3 — Conferência final antes de aplicar

Checklist de uma passada, para quem for rodar isso no Claude Code:

1. Trocar termo por termo, arquivo por arquivo, na ordem: glossário primeiro (é a fonte de verdade que as outras páginas linkam), depois Partes 1 a 4, depois o guia compacto, depois as fontes, depois os `.md` internos (STATUS, TOOLS).
2. Depois de cada arquivo, rodar uma busca por "sensor", "dono", "trifeta", "laço", "submissão", "Tier mínimo" no arquivo já editado, pra confirmar zero sobra, exceto as exceções documentadas na seção 2.4.
3. Nenhum id HTML muda em nenhum passo. Se alguma ferramenta de edição sugerir renomear um id porque o texto ao lado mudou, não aceitar automaticamente, conferir contra este arquivo primeiro.
4. `docs/logbook.html` e `NEXT-STEPS.pt.md` ficam de fora desta rodada.
