# Pesquisa da Parte 4: o escritório de agentes

Dossiê de trabalho. Levantado em 30 de agosto de 2026.

**Como usar.** Base de fatos verificados para sustentar o bloco A do dossiê anterior, que fixou tese, papéis, indicadores e argumento de fecho sem fonte. Não é o artigo. Ao integrar, o conteúdo verificado vai para `sources/inventory.md` no mesmo fluxo da parte 3.

**Legenda.** **V** verificada, URL confirmada em resultado de busca. **P** parcial, conteúdo confirmado por fonte secundária confiável, primária não lida. **N** não verificada, não citar com link.

---

## Sumário

| Eixo | Estado | Fontes | Observação |
|---|---|---|---|
| 0. Observação de campo | Terceiro | 0 | Protótipo alheio, sem autorização. Vale como convergência independente, nunca como origem do modelo |
| 1. Ciclo de vida do agente | Forte | 6 | Números de mercado melhores do que eu esperava |
| 2. Os quatro papéis | Forte | 5 | Precedente exato encontrado, e um achado sobre o que o mercado **não** nomeou |
| 3. Os oito indicadores | Média | 9 | Cinco sustentados por fonte externa, três são síntese do autor. Ver ressalva |
| 4. Onde o escritório senta | Forte | 4 | Precedente do CISO é ainda melhor do que o previsto, com citação memorável |
| 5. Calibração de vocabulário | Suficiente | 2 | Não precisa de mais |
| 6. Casos narrativos | Forte | 3 | Encontrado o equivalente do Air Canada, e ele é melhor |

---

## Eixo 0. Observação de campo: um protótipo de terceiro

**Estatuto desta fonte, declarado antes de tudo.** O que segue não é fonte primária deste projeto. É um protótipo construído por outra pessoa, mostrado informalmente ao autor por mensagem, ainda não publicado, e cujo criador estava pedindo sugestões e não oferecendo material para citação.

Consequências práticas, e nenhuma é negociável:

1. **A parte 4 não pode afirmar que seu modelo foi derivado de uma implementação real.** Essa afirmação seria falsa.
2. **Nada do protótipo pode ser reproduzido no artigo sem permissão escrita do autor:** nem captura de tela, nem nome do produto, nem descrição que permita identificá-lo.
3. **O valor desta observação é outro, e é legítimo:** ela é evidência convergente. Alguém competente, trabalhando de forma independente e sem contato com esta série, chegou a quatro objetos que mapeiam contra o MEDIR sem adaptação. Convergência independente é um argumento mais forte do que exemplo próprio, justamente porque não pode ser acusada de circularidade.

Se o autor do protótipo autorizar por escrito, isso vira estudo de caso creditado e a peça ganha muito. Sem autorização, entra apenas como observação genérica, sem identificação, no formato descrito no fim deste eixo.

### O que a convergência mostra

O protótipo observado opera com quatro objetos, e eles se mapeiam no ciclo sem adaptação.

| Objeto observado | Passo | O que resolve |
|---|---|---|
| Missão, com escopo e equipe declarados | Mapear | O contrato da tarefa instanciado antes da execução |
| Execução, com identificador, etapa e estado | Delegar | A unidade de despacho rastreável, distinta da missão que a originou |
| Contagem de símbolos, cache e economia por execução | Inspecionar | Sensor de custo exposto na tela principal, o que é raro |
| Artefatos e erros por execução | Inspecionar e Reforçar | O rastro que permite reconstruir o que aconteceu |

A distinção entre missão e execução é a mais importante das quatro. Uma missão pode gerar várias execuções, e uma execução falha não invalida a missão. É a mesma separação entre unidade de despacho e unidade de durabilidade que a parte 2 trata no passo Delegar, e ela apareceu de forma independente.

### Dois acertos que valem virar recomendação de projeto

Estes podem ser escritos como princípio, sem nenhuma referência ao protótipo, porque são recomendações e não citações.

**Execução falhada permanece visível na fila,** ao lado da que está rodando. Painel que esconde falha produz exatamente a ilusão de qualidade que a parte 2 alerta e que o eixo 3 mede pela taxa de reprovação. Esconder falha é a forma mais barata de fabricar um painel verde.

**Interruptor por agente, com estado obrigatório separado do opcional.** Isso é alçada expressa em interface, não em instrução. É a separação de poderes da parte 3 materializada: a política não está no texto que o modelo lê, está em um controle que ele não alcança.

### As cinco lacunas, e o que cada uma tem de base

Estas são as lacunas do modelo conceitual observado. Elas valem como projeto de escritório em geral, não como crítica a um trabalho específico, e é assim que devem ser escritas.

| Lacuna | Base neste dossiê |
|---|---|
| **Dono nomeado por agente.** Papéis não são pessoas, e papel não responde por nada | Eixo 1: 824.000 identidades ativas sem dono em nenhum sistema de RH, todas com direitos vivos |
| **Homologação como estado com validade,** e não como evento | Eixo 1: recertificação periódica é padrão em governança de identidade, com trimestral já sendo o piso |
| **Descomissionamento.** Todo mundo sabe ligar, quase ninguém tem procedimento para desligar | Eixo 1 e eixo 6: contas dormentes quase dobraram em um ano, três casos documentados de invasão por conta esquecida |
| **Caso de uso aprovado confrontado com o que roda.** É a diferença entre lista e registro de governança | Eixo 3, indicador 1: 43% das organizações não conseguem produzir um inventário de IA |
| **Resultado de negócio, não só de execução.** Símbolos e etapas são resultado técnico | Eixo 3, indicador 6: 46 pontos entre implantar e obter o resultado pretendido |

A última fecha o laço mais bonito da série: essa coluna é o bloco 7 da skill de briefing, o retorno prometido. O escritório é onde a promessa volta para ser conferida, e é por isso que o D10 termina no briefing e não em um relatório.

### Como escrever isso no artigo

**Sem autorização, que é o cenário padrão.** Uma frase de observação genérica, sem identificar nada: painéis de operação de agentes construídos hoje convergem para missão, execução, custo e artefato, e param aí. As cinco lacunas seguem como projeto de escritório, apoiadas nos números dos eixos seguintes, sem referência a implementação alguma.

**Com autorização escrita.** Estudo de caso creditado, com nome do autor e do projeto, revisado por ele antes da publicação. Nesse caso use desenho esquemático e nunca captura de tela: tela de protótipo envelhece rápido e desvia a atenção para a ferramenta em vez do método.

**Registro para a próxima sessão:** enquanto a autorização não existir e não estiver arquivada no repositório, vale o primeiro cenário.

---

## Eixo 1. Ciclo de vida do agente

**O que sustenta:** o D7, e a tese de que homologação sem validade é carimbo permanente.

### O número que faltava

A pesquisa anual de identidade e acesso da Veza, edição 2026, quantificou o problema que a parte 3 já tratava como qualitativo:

| Dado | Valor |
|---|---|
| Identidades ativas órfãs, sem dono em nenhum sistema de RH | 824.000 na base analisada |
| Proporção do total de usuários do provedor de identidade | Cerca de 8% |
| Todas elas | Ainda com direitos de acesso vivos |
| Identidades de máquina contra humanas | Aproximadamente 17 para 1 |
| Contas dormentes | Quase dobraram em um ano |
| Identidades órfãs | Alta de cerca de 40% |

A leitura que a fonte faz é a que interessa ao artigo, e é uma metáfora contábil que o seu leitor entende de imediato: isso não descreve proliferação, descreve um balanço em que a maior parte do passivo está fora dos livros.

E a formulação da causa raiz cabe em uma linha, que é a versão agêntica da frase da terça-feira que a parte 3 já usa:

> Projetos terminam, credenciais não, porque nenhum plano de projeto diz retire as identidades que criamos.

> Fonte: <https://www.cloudeagle.ai/blogs/why-every-team-is-quietly-building-up-non-human-identity-debt> · **V**

### O precedente fora do mundo de IA

Você pediu um precedente de certificação com validade para sustentar que homologação sem revalidação não é governança. Ele existe e é maduro: recertificação periódica de acesso é capacidade padrão de qualquer programa de governança de identidade, ao lado de automação de ciclo de vida, gestão de papéis e **segregação de funções**, esta última descrita exatamente como impedir combinações que permitiriam a uma só pessoa iniciar e aprovar uma transação.

Ou seja, o campo vizinho já resolveu as duas coisas que a parte 4 propõe, e resolveu junto, no mesmo programa. Isso é reforço forte para os eixos 1 e 2 ao mesmo tempo.

E há uma crítica de 2026 que vale citar, porque impede a parte 4 de recomendar carimbo trimestral como se fosse suficiente:

> Organizações que continuam dependendo de certificação trimestral vão continuar descobrindo acesso obsoleto depois do fato, não antes de ele virar risco. O sinal a observar é se revogação e recertificação estão se tornando orientadas a evento, e não apenas agendadas.

Isso muda uma recomendação da parte 4: revalidação por calendário é o piso, não o teto. O ideal é revalidação disparada por evento, como mudança de dono, mudança de escopo ou expiração de credencial.

> Fontes: <https://nhimg.org/articles/iga-solutions-in-2026-expose-the-limits-of-legacy-access-reviews/> · **V**
> <https://www.waldosecurity.com/post/best-identity-governance-administration-iga-solutions-in-2026> · **V**

### O mecanismo de acúmulo

A descrição de como a conta órfã nasce é transferível para agente sem nenhuma adaptação: contas de serviço sobrevivem aos projetos e às pessoas que as criaram, deixando contas dormentes com acesso privilegiado que atacantes descobrem por enumeração. Um microsserviço criado para um piloto é desativado, e a conta de serviço dele continua ativa em produção com direitos administrativos de banco.

E o alvo do programa maduro, dito em uma frase que serve de definição do estado homologado: contas criadas por fluxo padronizado que exige justificativa de negócio, atribui dono e estabelece cronograma de ciclo de vida desde o primeiro dia.

> Fontes: <https://www.obsidiansecurity.com/blog/service-account-security-best-practices> · **V**
> <https://www.scworld.com/risk-advisory/non-human-identities-are-outgrowing-your-governance-model> · **V**
> <https://thehackernews.com/2026/01/the-hidden-risk-of-orphan-accounts.html> · **V**

O último traz um termo que vale adotar no artigo: **matéria escura de identidade**, o conjunto de contas invisíveis à governança mas ativas na infraestrutura. E registra explicitamente que processos agênticos de IA estão nessa categoria, nativamente não governados.

---

## Eixo 2. Os quatro papéis e a não acumulação

**O que sustenta:** o D8, e a frase que estava no dossiê sem fonte.

### O precedente é exato

O Modelo das Três Linhas, do Instituto dos Auditores Internos, adotado formalmente em 2013 e revisado em 2020 e 2023, mapeia contra os quatro papéis quase sem folga:

| Três Linhas | Papel na parte 4 | Função |
|---|---|---|
| Primeira linha | Dono do agente | Opera e é responsável pelo risco que gera |
| Segunda linha | Homologador | Assiste, monitora e desafia a primeira linha |
| Terceira linha | Auditor | Garantia independente e objetiva, reporta ao órgão de governança |
| Órgão de governança | Patrocinador da área e comitê | Delega e supervisiona |

A definição da terceira linha traz a frase que sustenta a não acumulação: a principal diferença entre a terceira linha e as duas primeiras é o alto grau de independência organizacional e objetividade, sendo que as duas primeiras fazem parte da gestão e a terceira é sinônimo de auditoria interna.

> Fontes: <https://erm.ncsu.edu/library/article/cosos-take-on-the-three-lines-of-defense> · **V**
> <https://www.deloitte.com/mt/en/services/consulting-risk/perspectives/modernising-the-three-lines-of-defence-model.html> · **V**
> <https://pathlock.com/blog/internal-controls/coso-framework/> · **V**

Do COSO vem a formulação de segregação de funções que a série pode usar quase literalmente: segregação garante que autorizar e registrar transações sejam funções separadas, e a matriz de autoridade define quem tem poder de tomar cada decisão, com o propósito explícito de impedir ações não autorizadas.

Matriz de autoridade é, palavra por palavra, o que a parte 3 chamou de matriz de alçada. Vale registrar essa correspondência no texto: não estamos inventando um instrumento, estamos estendendo um que já existe a um novo tipo de executor.

### Dois achados acadêmicos que ninguém citou ainda

Existem dois artigos que aplicam explicitamente o Modelo das Três Linhas a risco de IA, e um deles argumenta que desenvolvedores de IA de fronteira precisam de função de auditoria interna. São material de fundamentação que eleva o nível da peça, e provavelmente nenhum concorrente brasileiro os conhece.

> Fontes: <https://arxiv.org/pdf/2305.17038> · **V**, *Frontier AI developers need an internal audit function*
> <https://arxiv.org/pdf/2212.08364> · **V**, *Three lines of defense against risks from AI*

### O achado negativo, que vale ser dito com todas as letras

Você perguntou se algum framework de governança de IA já nomeia papéis equivalentes aos quatro. **Não encontrei nenhum.** NIST AI RMF, ISO 42001, AIUC-1 e a iniciativa de padrões para agentes do NIST tratam de funções organizacionais, controles e evidência, mas nenhum fixa os papéis de dono do agente, homologador, auditor e patrocinador como estrutura nomeada.

Isso é um achado, não uma lacuna. A parte 4 deve dizer que está tomando emprestado um modelo maduro de controle interno e aplicando a um objeto que os frameworks de IA ainda tratam de forma genérica. É honesto e é diferenciador.

Uma confirmação indireta vem do mercado: a pesquisa Splunk de 2026 com 650 líderes de segurança encontrou que apenas 6% das organizações que rodam agentes atualizaram seus frameworks de governança para corresponder ao que aqueles agentes de fato fazem.

> Fonte: <https://echeloncyber.com/intelligence/entry/the-ai-governance-gap-no-ones-talking-about-why-your-ciso-cant-own-this-alone> · **V**

---

## Eixo 3. Os oito indicadores

Este é o eixo mais pesado e o resultado é misto. Vou linha por linha, e a ressalva geral está no fim.

### 1. Cobertura do registro

**Sustentado, e com número forte.** Segundo levantamento Gartner de 2025, **43% das organizações não conseguem produzir um inventário de IA**, que é requisito fundacional da regulação europeia, do NIST AI RMF e da ISO 42001.

Complementos úteis: 78% dos usuários de IA no trabalho estão trazendo as próprias ferramentas, fora da aprovação de TI, segundo o índice de tendências de trabalho da Microsoft de 2025. E projeção do Gartner de que, até 2027, IA sombra será fator contribuinte em 40% das falhas de IA corporativa.

> Fonte: <https://airia.com/blog/shadow-ai-statistics-key-data-points-every-ciso-needs-in-2026/> · **V** (agregadora, cita Gartner e Microsoft como primárias, **P** para os números individuais)

**Tentativa de verificação na origem primária, sem sucesso.** Busquei o comunicado ou relatório específico da Gartner por trás do número, incluindo busca direta no domínio gartner.com. Não localizei o relatório que sustenta especificamente "43% não conseguem produzir inventário de IA". Existem comunicados adjacentes da Gartner sobre maturidade e abandono de projeto de IA em 2025 e 2026, nenhum com esse número exato. Status permanece **P** para este número. No texto, atribuir com verbo que reflita a incerteza de origem, "segundo levantamento amplamente citado da Gartner", não "segundo a Gartner", e considerar se o número resiste a outra rodada de busca antes da publicação.

### 2. Faixa contra ambiente

**Interno à série.** Não precisa de fonte externa, como você já apontou. É o acidente estrutural da parte 1, medido.

### 3. Homologação vencida

**Sustentado pelo eixo 1.** A prática de recertificação de acesso é o precedente direto, com a crítica de 2026 de que certificação trimestral descobre acesso obsoleto depois do fato. Não precisa de fonte adicional.

### 4. Taxa de exceção

**Sustentado por analogia, com fundamento sólido, fonte de patente substituída nesta rodada.** A lógica do quase-acidente como indicador antecedente está estabelecida na ciência de segurança, na tradição que remonta ao triângulo de acidentes de Heinrich, 1931, proporção original de 300 quase-acidentes para 29 lesões menores para 1 lesão grave: quase-acidentes são aviso antecipado, e rastreá-los permite prever risco antes que ele vire incidente.

**Ressalva honesta que o próprio campo já faz, e que vale herdar no texto.** A proporção fixa de Heinrich é questionada pela literatura mais recente, a razão entre quase-acidentes, lesões menores e acidentes graves varia por indústria e ambiente de trabalho. O que sobrevive à crítica não é o número, é a lógica: o evento de perda quase sempre foi precedido por aviso.

A ponte para o artigo é direta e vale escrever assim: suprimir uma regra ou subir um limiar é o quase-acidente do agente. Não causou dano, e é o melhor aviso disponível de que o dano está a caminho.

> Fonte: <https://oshacommunity.com/osha/heinrichs-safety-triangle/> · **V**, substitui a fonte de patente da rodada anterior, que ficava estranha em nota de artigo executivo

### 5. Taxa de reprovação no portão

**Este é o melhor achado de toda a rodada, e ele transforma o indicador de opinião em exposição jurídica.**

**Verificado na fonte nesta rodada, com uma correção de precisão sobre a leitura anterior:** as três fontes abaixo respondem perguntas diferentes, e a rodada anterior as tinha citado juntas como se fossem uma só. Separando:

**A holding do próprio caso.** O Tribunal de Justiça da União Europeia, no caso SCHUFA de 2023, processo C-634/21, decidiu que "unicamente automatizado" inclui os casos em que um humano formalmente assina mas na prática defere inteiramente ao algoritmo. Revisão humana real, com autoridade para reverter, é o que faz o tratamento ser considerado parcialmente automatizado em vez de unicamente automatizado.

> Fonte: <https://www.legiscope.com/blog/gdpr-article-22-automated-decision-making.html> · **V**, confere quase literalmente: "the CJEU in SCHUFA (December 2023) clarified that 'solely' doesn't require zero human involvement. If a human formally signs off but in practice defers entirely to the algorithm, the decision is still 'solely automated'"

**A formulação mais próxima da lógica do próprio SCHUFA**, de uma análise doutrinária que cruza o caso com jurisprudência correlata (Uber, Deliveroo, CaixaBank): revisão nominal falha ao artigo 22 quando equivale a carimbo sem critério interpretativo ou autoridade para divergir.

> Fonte: <https://journals.muni.cz/mujlt/article/view/41367> · **V**, análise doutrinária do SCHUFA com jurisprudência nacional europeia

**Separado de propósito, e não parte da decisão do tribunal:** orientação geral do artigo 22 (não específica ao SCHUFA) sobre o que conta como revisão significativa. Vale citar como reforço geral, atribuído ao EDPB, não ao tribunal:

1. Autoridade para alterar ou reverter a decisão automatizada
2. Acesso a todos os dados relevantes usados no processo
3. Compreensão da lógica e dos critérios por trás da decisão
4. Capacidade de considerar informação adicional não processada pelo sistema automatizado

> Fonte: <https://gdprlocal.com/automated-decision-making-gdpr/> · **V** para o conteúdo, mas esta página não menciona o caso SCHUFA em nenhum momento, é orientação geral do EDPB. Citar as duas linhas acima separadamente no texto, nunca como se uma só fonte dissesse as duas coisas

E a consequência que a parte 4 pode afirmar com base legal, não com opinião: **um portão com cem por cento de aprovação não é apenas teatro de governança, é evidência de que a decisão continua sendo unicamente automatizada.** Com tudo o que isso implica sob o artigo 22 europeu e, por analogia direta, sob o artigo 20 da LGPD que a parte 3 já trata.

Isso amarra parte 3 e parte 4 pelo mesmo fio jurídico. É o equivalente, na parte 4, do que Air Canada foi na parte 3.

> Decisão original, processo C-634/21: **P**, referenciada nas três fontes, não lida diretamente

### 6. Retorno realizado contra prometido

**Sustentado, com abundância quase constrangedora.**

| Dado | Fonte |
|---|---|
| 95% dos pilotos de IA sem impacto mensurável em resultado | Estudo do MIT, *The GenAI Divide*, 2025 |
| 89% dos pilotos de agentes não chegam à produção | Deloitte, 2026 |
| 57% das empresas implantaram IA amplamente, apenas 11% atingiram seus dois principais objetivos | Kyndryl, Relatório de Prontidão de Pessoas 2026 |
| 42% das empresas abandonaram a maioria dos projetos de IA em 2025 | S&P Global |
| 25% das iniciativas entregando o retorno esperado | IBM |
| 21% das empresas do índice S&P 500 conseguiam citar um benefício mensurável de IA | Morgan Stanley |

O dado da Kyndryl é o mais eloquente e o que eu usaria: 46 pontos de distância entre implantar e obter o resultado pretendido. Mais de quatro em cada cinco organizações que implantaram estão rodando sistemas que não entregam aquilo para que foram construídos.

**Verificado na fonte primária nesta rodada, com uma camada extra de precisão que vale usar no texto.** O comunicado oficial da Kyndryl (2026 People Readiness Report, 1.100 líderes de negócio e tecnologia, oito países) mostra que os 57% e os 11% são dois recortes diferentes, não a mesma pergunta: 57% dizem que a IA está incorporada em processos centrais de negócio ou implantada amplamente na empresa; dentre essas, 32% atingiram pelo menos um dos dois principais objetivos declarados, e só 11% atingiram os dois. É a diferença entre "pelo menos um" e "os dois" que dá à frase seu peso real, e vale escrever assim no artigo em vez de comprimir num único número.

Existe ainda um dado que justifica o indicador diretamente: rastreamento de retorno por agente permite desligar sistemas de baixo desempenho cedo, antes que consumam orçamento relevante.

> Fontes: <https://www.legal.io/blog/5719519/MIT-Report-Finds-95-of-AI-Pilots-Fail-to-Deliver-ROI-Exposing-GenAI-Divide> · **V**
> <https://www.prnewswire.com/news-releases/kyndryl-report-ai-adoption-accelerates-as-workforce-readiness-becomes-the-roi-difference-maker-302810837.html> · **V**, comunicado oficial da Kyndryl, substitui a agregadora da rodada anterior para este número especificamente
> <https://www.terminal-x.ai/research/ai-roi-in-2026-why-most-enterprise-ai-fails-and-what-actually-works> · **V**
> <https://www.beri.net/article/ai-agent-adoption-enterprise-2026-gartner-idc> · **V**

### 7. Agentes sem execução no período

**Sustentado pelo eixo 1**, mesma família de conta dormente. Mas encontrei a nuance que faltava, e ela impede o indicador de virar botão de exclusão automática:

> Encontrar essas contas é fácil. Qualquer relatório lista de bom grado toda conta que não fez login nos últimos 400 dias. O difícil é o julgamento que vem em seguida: essa conta está de fato morta, ou algo ainda depende dela silenciosamente? Apague uma conta "morta" que um trabalho automático de faturamento usa toda noite e você quebrou a produção.

Isso vira uma advertência explícita no texto da parte 4: sem execução no período é sinal para investigar, não gatilho para desligar. E é exatamente por isso que a transição para descomissionado no D7 exige decisão de dono e homologador, não automação.

> Fonte: <https://techcommunity.microsoft.com/blog/educatordeveloperblog/afterlogin-we-turned-forgotten-account-cleanup-into-a-haunted-house-game-with-mi/4539781> · **V**

### 8. Custo por missão

**Sustentado por padrão de mercado, e é o mais bem fundamentado dos oito.**

A Fundação FinOps trata IA como categoria tecnológica distinta no framework de 2026, e recomenda unidades econômicas como custo por consulta, custo por usuário por mês, custo por conclusão de fluxo e custo por transação de negócio.

E a formulação específica para agentes é literalmente o nome do nosso indicador:

> Para cargas agênticas, **custo por tarefa concluída** é a medida mais significativa, porque uma única ação do usuário pode disparar muitas chamadas subjacentes ao modelo.

Contexto que sustenta a urgência: 98% dos praticantes de FinOps agora administram gasto com IA, contra 63% um ano antes e 31% dois anos antes, segundo o levantamento State of FinOps 2026, com 1.192 respondentes administrando mais de 83 bilhões de dólares em nuvem.

E a aritmética que explica por que o custo sobe mesmo com preço unitário caindo: fluxos agênticos disparam entre dez e vinte chamadas por tarefa do usuário, recuperação de contexto infla a janela em três a cinco vezes, e agentes sempre ligados consomem o tempo todo. Planeje pelo produto de tarefas vezes passos vezes símbolos, não pelo preço de tabela.

> Fontes: <https://www.n-ix.com/finops-for-ai/> · **V**
> <https://compresr.ai/blog/ai-finops-definitive-guide-costs-and-value> · **V**
> <https://wetheflywheel.com/en/guides/ai-finops-gpu-cost-management-2026/> · **V**

---

### A ressalva sobre o conjunto, que precisa entrar no artigo

Você antecipou isso e estava certo. **Nenhuma fonte externa propõe esses oito indicadores como conjunto.** Cinco têm base externa sólida (cobertura, homologação vencida, reprovação no portão, retorno realizado, custo por missão), dois têm base analógica de outra disciplina (taxa de exceção via quase-acidente, sem execução via conta dormente), e um é interno à série (faixa contra ambiente).

A parte 4 deve dizer isso explicitamente, no corpo do texto, em uma frase do tipo: este painel não é padrão de mercado, é síntese, e cada linha declara de onde veio. Isso é a lacuna equivalente à da regra de dois na parte 3, e tratá-la da mesma forma mantém a coerência de honestidade da série inteira.

Vantagem colateral: declarar isso converte uma fragilidade em posicionamento. O mercado não tem esse painel, e a série está propondo o primeiro.

---

## Eixo 4. Onde o escritório senta

**O precedente é ainda melhor do que o previsto, e vem com uma frase citável.**

O debate sobre a linha de reporte do responsável por segurança da informação tem quinze anos e continua aberto, o que por si só é o argumento: não existe modelo universal, existe um problema estrutural que reaparece.

Os números atuais, do relatório de referência IANS Research e Artico Search de 2026:

| Para onde o CISO reporta | Percentual |
|---|---|
| TI, tipicamente CIO ou CTO | 64% |
| CEO | 11% |
| CFO | 5% |
| Diretor de risco | 5% |
| Jurídico | 5% |
| Outros papéis de negócio | 5% |

E a formulação do conflito, atribuída a um consultor de segurança e ex-procurador federal, é a melhor analogia que encontrei em toda a pesquisa das duas partes:

> O CIO é recompensado por eficiência e economia, e o CISO é responsável por identificar riscos que frequentemente exigem novo gasto. É como pedir ao inspetor de incêndio que se reporte à pessoa cujo bônus depende de cortar o número de aspersores.

Isso sustenta, com fonte, a frase que estava solta no dossiê sobre função de controle subordinada ao executor perder independência. E a posição emergente para 2026 é descrita como reporte direto ao presidente ou ao comitê de risco do conselho, justamente para assegurar independência das funções que se fiscaliza.

Há também o contraponto honesto, que a parte 4 deve incluir para não parecer panfleto: uma corrente argumenta que enquadrar a relação como conflito orçamentário estrutural é contraproducente e ultrapassado, que o objetivo não é evitar atrito e sim projetar alinhamento, e que a linha de reporte é meio e não fim.

> Fontes: <https://www.csoonline.com/article/4136293/its-time-to-rethink-ciso-reporting-lines.html> · **V**
> <https://www.csoonline.com/article/4158505/the-endless-ciso-reporting-line-debate-and-what-it-says-about-cybersecurity-leadership.html> · **V**
> <https://www.vantedgesearch.com/resources/blogs/ciso-elevation-in-2026-why-cybersecurity-leadership-is-moving-to-the-c-suite-and-board-tables/> · **V**

### O dado específico de IA

A pesquisa Splunk de 2026, com 650 líderes de segurança, encontrou que praticamente todos absorveram responsabilidades de governança de IA, e **79% dizem que seus papéis se expandiram além do que mandato e recursos suportam**. Além disso, 71% dizem que a IA tem acesso a sistemas centrais de negócio, mas apenas 16% governam esse acesso bem.

E a conclusão da fonte é exatamente a posição que a parte 4 defende:

> A pessoa que tem o título não tem a autoridade, e as pessoas que têm a autoridade não respondem pelos resultados. É aí que o modelo quebra.

A recomendação observada nas organizações que estão conseguindo: não atribuir dono único, e sim construir modelo operacional de governança distribuído entre funções, com comitê incluindo jurídico, conformidade, dados, compras, recursos humanos e as áreas de negócio que implantam.

Isso reforça a opção de célula com reporte duplo, e enfraquece a opção de dono único em qualquer área, inclusive risco.

> Fonte: <https://echeloncyber.com/intelligence/entry/the-ai-governance-gap-no-ones-talking-about-why-your-ciso-cant-own-this-alone> · **V**

### Um dado adjacente que vale para a seção de custo

O levantamento State of FinOps 2026 encontrou que 78% dos times de FinOps reportam ao CTO ou CIO, e apenas 8% ao CFO. Gestão de custo de IA está sendo tratada como capacidade tecnológica, não função financeira. Isso é útil como paralelo: outra função de controle sendo colocada dentro do executor, pelo mesmo motivo, e provavelmente com o mesmo resultado.

> Fonte: <https://www.buildmvpfast.com/blog/ai-finops-function-token-budget-org-chart-2026> · **V**

---

## Eixo 5. Calibração de vocabulário

Não precisa de mais pesquisa. As fontes do botão de desligar já levantadas na parte 3 dão a textura, e o padrão do mercado é claro: torre de controle, governança de ponta a ponta, força de trabalho autônoma, descobrir e desligar agentes fora de controle.

**Recomendação de tom:** a parte 4 não deve competir com esse vocabulário nem ridicularizá-lo. Deve fazer o movimento que só ela pode fazer, que é distinguir função de produto. Torre de controle é produto. Escritório é função. Produto se compra, função se organiza, e a segunda sobrevive à troca do primeiro.

Uma palavra a evitar deliberadamente: **plataforma**. Se a parte 4 usar essa palavra para descrever o que propõe, a peça vira folheto na primeira leitura.

---

## Eixo 6. Casos narrativos

Encontrei o equivalente do Air Canada, e ele é melhor, porque é um caso de **concentração**, que é exatamente a tese da parte 3 e a justificativa da parte 4.

### O caso do assistente de recuperação de conta

Entre 17 de abril e 31 de maio de 2026, atacantes exploraram uma falha de autenticação no sistema de recuperação de conta assistida por IA de uma grande plataforma social, tomando **20.225 contas do Instagram**, incluindo alvos de alto perfil como a conta da Casa Branca de Barack Obama. A vulnerabilidade foi documentada na notificação de violação enviada ao Ministério Público do Maine em 5 de junho de 2026.

E aqui está a razão de ser o caso perfeito para esta série:

> A decisão de projeto que criou a superfície de ataque foi o grau de privilégio que o sistema detinha. A empresa concedeu ao assistente autoridade para associar novos endereços de e-mail a contas existentes **e** para disparar comunicações de redefinição de senha para esses endereços, combinando efetivamente gestão de identidade e recuperação de credencial em uma única interação mediada por IA.

Isso é o D2 acontecendo no mundo real, em escala, com nome e data. Duas funções que não podiam morar no mesmo lugar moraram, e a consequência foi vinte mil contas.

A distinção que a fonte faz também é útil: neste caso a IA era a infraestrutura de suporte sendo abusada, e não uma ferramenta usada pelos atacantes. Sistemas de verificação de identidade mediados por IA viram alvo de manipulação adversarial da camada de IA.

> Fonte: <https://labs.cloudsecurityalliance.org/research/csa-research-note-meta-ai-support-bot-account-takeover-20260/> · **V**

### Os casos de conta esquecida, para a seção de descomissionamento

| Caso | O que aconteceu |
|---|---|
| Colonial Pipeline, 2021 | Atacantes entraram por uma conta de rede privada antiga e inativa, sem autenticação de dois fatores |
| Indústria atingida por ransomware, 2025 | Acesso por uma conta "fantasma" de fornecedor terceiro que nunca foi desativada |
| Contas dormentes em repositório de código, 2026 | Mais de cinquenta contas criadas dois a cinco anos antes e deliberadamente mantidas inativas antes de serem usadas para enumerar organizações e clonar repositórios privados |

O terceiro é o mais interessante para a parte 4 porque inverte o quadro: a dormência não foi descuido, foi estratégia do atacante. Uma conta que parece morta pode estar esperando.

> Fontes: <https://thehackernews.com/2026/01/the-hidden-risk-of-orphan-accounts.html> · **V**
> <https://thehackernews.com/2026/07/dormant-github-accounts-help-attackers.html> · **V**

---

## A decisão sobre o D10

Recomendo **incluir na parte 4**, e o risco de confusão com o MEDIR se resolve sozinho por dois motivos.

O primeiro é de forma: o D7 é máquina de estados, o D10 é laço. São tipos visuais diferentes, e o leitor percebe isso antes de ler os rótulos.

O segundo é de posição: o D10 deve fechar a seção de indicadores, não abrir a peça. Ali ele funciona como resumo daquela seção, mostrando onde os oito se encontram, e não como um ciclo concorrente.

Com uma exigência de rótulo: o título do diagrama precisa carregar a cadência. Algo como "o ciclo trimestral do escritório", com a palavra trimestral no próprio título, para deixar explícito que este roda por período e o MEDIR roda por tarefa.

E ele pode aparecer duas vezes. Abrir o playbook com o mesmo diagrama é legítimo, porque ali ele cumpre outro papel, que é organizar o documento inteiro.

---

## As lacunas

**O conjunto dos oito indicadores é síntese, não padrão.** Precisa ser declarado no corpo do texto. Detalhado no eixo 3.

**Resolvida nesta rodada: a fonte do quase-acidente era documento de patente.** Substituída pelo triângulo de acidentes de Heinrich, com a ressalva honesta sobre a proporção fixa ser questionada. Ver eixo 3, indicador 4.

**Parcialmente resolvida: os números de mercado vinham majoritariamente de agregadoras.** O par 57%/11% da Kyndryl foi verificado no comunicado oficial nesta rodada e passa a **V**, com a precisão extra de que são dois recortes diferentes (32% atingiram ao menos um objetivo, 11% os dois). **O número da Gartner, 43% sem inventário de IA, continua P**: tentei localizar o relatório original, inclusive busca direta em gartner.com, e não encontrei. Deloitte, Microsoft e IANS não foram reverificados nesta rodada, mesma advertência da rodada anterior se aplica: nomeie a origem primária no texto, não a agregadora.

**Não encontrei caso brasileiro.** Mesma limitação da parte 3. Todos os casos narrativos são estrangeiros e isso precisa ser dito.

---

## O que a pesquisa muda na estrutura planejada

**A abertura da parte 4 está resolvida.** O caso do assistente de recuperação de conta, com as vinte mil contas e a decisão de projeto que concentrou duas funções em um só lugar. Ele conecta a parte 3 à parte 4 pelo mesmo mecanismo, e permite abrir dizendo que o problema da parte 3 não escala linearmente: quando são muitos agentes, ninguém sequer sabe quantas dessas concentrações existem.

**O indicador de reprovação no portão sobe de importância.** Com o SCHUFA, ele deixa de ser boa prática e passa a ser evidência jurídica. Merece parágrafo próprio e provavelmente uma citação em destaque.

**A seção de onde o escritório senta ganha o precedente do inspetor de incêndio e os aspersores.** É a melhor frase disponível para o argumento, e vem com fonte.

**Entra uma advertência nova na seção de descomissionamento**, que eu não tinha previsto: sem execução no período é sinal para investigar, não gatilho para desligar. Apagar a conta que o faturamento noturno usa quebra a produção.

**A revalidação ganha nuance:** por calendário é o piso, por evento é o alvo. Isso não estava no dossiê e melhora a recomendação.

**O achado negativo do eixo 2 vira posicionamento.** Nenhum framework de IA nomeia os quatro papéis. A série está emprestando um modelo maduro de controle interno e aplicando a um objeto que o mercado ainda trata genericamente. Dito com clareza, isso é autoridade, não fragilidade.
