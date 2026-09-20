# build

Corpos de texto e scripts de montagem usados para gerar os HTML da raiz.

## Como funciona

Cada artigo é montado em duas partes: um corpo em HTML com marcadores de glossário no formato `{{termo}}`, e um script Python que injeta o glossário, resolve os marcadores, prefixa os identificadores por idioma e cola tudo no envoltório de CSS.

O envoltório de CSS é extraído do arquivo já pronto anterior, para que os quatro documentos permaneçam idênticos em formatação. Alterar o CSS em um deles e regerar os outros propaga a mudança.

## Arquivos

| Arquivo | Papel |
|---|---|
| `body_p2_pt.html` | corpo da parte 2 em português, regenerado a cada build, não editar direto |
| `body_p2_en.html` | corpo da parte 2 em inglês, editável |
| `body_p2_es.html` | corpo da parte 2 em espanhol, editável |
| `body_toolkit_pt.html` | corpo do guia compacto em português, editável, organizado pelo MEDIR |
| `body_en.html` | corpo da parte 1 em inglês |
| `build_p2.py` | monta `harness-p2.html` trilíngue |
| `build_toolkit.py` | monta `harness-toolkit.html`, hoje só PT |
| `build_logbook.py` | monta `docs/logbook.html` trilíngue a partir de `docs/assets/logbook-metrics.json`, incluindo o terceiro gráfico de custo |
| `generate_logbook_metrics.py` | reconstrói `docs/assets/logbook-metrics.json` a partir do git, dos transcripts reais da sessão e de `docs/assets/prices.json`, nunca editado à mão. Modos: normal, `--recount`, `--reprice`, `--enrich [--dry-run]`, ver abaixo |
| `docs/assets/prices.json` | livro-razão de preço datado e apensado (não é script, é dado-fonte), nunca sobrescrito, um marco lê a entrada vigente na própria data e o valor calculado fica congelado depois disso |
| `check_glossary_order.py` | verifica ordem alfabética das entradas de `body_glossary_*.html` nas três línguas, roda antes de qualquer build depois de renomear um termo |
| `generate_toolkit_manifest.py` | reconstrói `toolkit.json` a partir de `TOOLS.md` e `sources/inventory.md`, nunca editado à mão; `--check` só verifica se está desatualizado |
| `build_all.py` | histórico, montou a versão trilíngue da parte 1; usa caminhos fixos de sandbox, não roda neste repositório como está |
| `build_en.py` | histórico, gerou a versão em inglês da parte 1; mesma limitação de `build_all.py` |
| `patch_p2.py` | histórico, aplicou seções novas na parte 2 antes de `build_p2.py` virar trilíngue |

## Regra crítica

A função `scope()` prefixa identificadores de âncora e marcadores de SVG por idioma. Todo conteúdo novo precisa passar por ela, senão as três versões de um mesmo documento colidem e as âncoras apontam para o idioma errado.

`build_p2.py` desde 30 de agosto de 2026 extrai o corpo PT direto do `harness-p2.html` vigente, que é a fonte da verdade, e regrava `body_p2_pt.html` a cada execução. Antes disso, `patch_p2.py` aplicava seções novas direto no HTML final sem atualizar o corpo em `build/`, e o arquivo ficou desatualizado por um tempo. Escreva os corpos EN e ES sem prefixo de idioma nos ids e âncoras (`id="abertura"`, não `id="pt-abertura"`), porque `scope()` cuida do prefixo no build.

Links cruzados para `harness-p1.html` com âncora precisam do prefixo do idioma de destino (`#en-opening`, `#es-apertura`, `#pt-abertura`), porque o JavaScript de troca de idioma lê o prefixo da URL para escolher a aba antes de rolar até o elemento. Um link sem esse prefixo, ou com o prefixo do idioma errado, sempre abre a parte 1 na aba PT.

`build_sources.py`, `build_glossary.py` e `build_toolkit.py` **não** são autorreferentes como `build_p2.py`: os três leem o corpo das três línguas direto de `build/body_sources_*.html`, `body_glossary_*.html` e `body_toolkit_*.html`, sem nunca extrair de volta do HTML publicado. Editar `harness-sources.html`, `harness-glossary.html` ou `harness-toolkit.html` à mão, sem espelhar a mesma mudança no corpo correspondente em `build/`, é invisível até a próxima regeneração, que reverte a edição sem aviso, achado em 31 de agosto de 2026 quando `build/body_sources_*.html` ficou duas rodadas de correção de citação desatualizado em relação ao `harness-sources.html` vigente. Rode o script depois de qualquer edição direta em uma dessas três páginas, ou edite só o corpo em `build/` e deixe o script montar o arquivo final.

Renomear um termo do glossário muda a letra que decide sua posição, mas não move a linha sozinho: rode `python build/check_glossary_order.py` depois de qualquer mudança de terminologia, antes de reconstruir. Achado em 11 de setembro de 2026 (duas entradas em português fora de ordem por onze dias, sem ninguém notar, ver `NEXT-STEPS.md`).

Editar `TOOLS.md` (a tabela de coleções instaladas, ou a lista de skills por coleção) ou a tabela "Tools and skills" de `sources/inventory.md` sem rodar `python build/generate_toolkit_manifest.py` na sequência deixa `toolkit.json` desatualizado, do mesmo jeito que editar `harness-sources.html` sem espelhar em `build/` deixa o build seguinte reverter a edição. `--check` acusa a divergência (hash das duas seções-fonte) sem escrever nada; rode antes de commitar qualquer mudança num dos dois arquivos-fonte.

## Custo em dinheiro, portado de volta de `milestone-loc-tokens-ai-ledger`

`generate_logbook_metrics.py` ganhou, em 14 de setembro de 2026, a mesma lógica de preço datado e apensado que a própria skill que este projeto gerou (`milestone-loc-tokens-ai-ledger`, ver `NEXT-STEPS.md` item 5) já tinha construído: `load_price_ledger`, `find_price_series`, `price_at` e `compute_cost`, lendo `docs/assets/prices.json`. O custo de um marco é calculado uma vez, no preço vigente na data desse marco, e nunca recalculado depois, mesmo que o livro-razão ganhe uma entrada nova; `load_previous` garante isso lendo o `logbook-metrics.json` da execução anterior antes de sobrescrever.

**Preço que estava errado, corrigido em 20 de setembro de 2026.** A entrada de 13 de setembro registrou o Sonnet 5 a US$3/15, mas o preço cobrado é US$2/10 (o aumento previsto para 1º de setembro foi cancelado, conforme a página de preços da Anthropic, lida na data, junto com a visão geral de modelos). A entrada errada continua no livro-razão, e uma segunda, com `corrects` e a nota do motivo, a substitui: em empate de data, `price_at` escolhe a entrada gravada depois. Como um custo gravado nunca é recalculado por uma execução normal, `python build/generate_logbook_metrics.py --reprice` é o caminho explícito e auditado para esse caso, portado de `milestone-loc-tokens-ai-ledger`: recalcula só o custo dos marcos já gravados, a partir dos tokens já gravados neles, sem ler git nem transcrição, e guarda o custo anterior em `repricings` no próprio marco. Rodar de novo, sem entrada nova no livro-razão, não muda nada. Não use `--reprice` para uma mudança normal de preço: uma entrada com `effective_date` posterior já deixa cada marco antigo no preço que valia na sua data. Aqui, ele levou o custo gravado de US$105,66 para US$70,44 em onze marcos.

**O limite do reprice, fechado em 20 de setembro de 2026.** `tokens_bucket` guarda só os quatro contadores originais, porque é assim que `build_logbook.py` os soma (`sum(m['tokens_bucket'].values())`). Antes, o port precificava toda escrita de cache a `cache_creation_price` (US$2,50 por milhão), e nas transcrições deste projeto todas as escritas de cache lidas são de 1 hora, a US$4,00. O corte por modelo e por TTL agora vive numa chave irmã, `tokens_split`, e `price_milestone` precifica cada modelo com a própria série e as escritas de 1 hora ao preço de 1 hora; uma escrita de 1 hora sob uma entrada sem `cache_creation_1h_price` fica sem preço, nunca ao preço de 5 minutos. Os 79 marcos que já existiam foram migrados com `--enrich`, e o custo gravado dos 14 que tinham um foi de US$77,7944 para US$83,1673 (+US$5,3729), medido marco a marco, o número que a estimativa anterior de cerca de US$4,82 para onze marcos apontava.

**Limite honesto, não escondido:** `docs/assets/prices.json` só tem uma série verificada (Sonnet 5, a partir de 13 de setembro de 2026). Todo marco anterior a essa data mostra `cost_recorded: null` na saída e "sem preço" no diário publicado, nunca um custo inventado. Isso é esperado, não um bug: este script não afirma um preço que não verificou. Ao contrário do próprio motor de tokens (uma sessão contínua cobrindo o projeto inteiro), o preço de LLM muda por decisão comercial do fornecedor, não por uso deste projeto, então não há como reconstruir retroativamente sem uma fonte real para cada data.

## Congelamento, `--enrich` e `--recount`, portados de `milestone-loc-tokens-ai-ledger` em 20 de setembro de 2026

A regra: congelar o fato de granularidade mais fina e derivar o preço depois. Um custo gravado é um número derivado; os tokens, por modelo e por TTL de cache, são o fato.

- **Execução normal.** Nunca reabre os tokens de um marco já gravado (`tokens_bucket`, `tokens_split`): eles vêm do arquivo, não da transcrição, porque o Claude Code apaga transcrições depois de `cleanupPeriodDays` (30 dias por padrão). Só um commit novo deriva tokens. Palavras e linhas também são reaproveitadas por hash de commit, desde que `count_rules_hash` (uma impressão digital de `CONTENT_HTML`, `CODE_GLOBS_PREFIXES`, `GOV_DOCS` e `COUNT_ALGORITHM_VERSION`) seja a mesma da execução que as gravou. Sem a marca, ou com uma marca diferente, o script reconta tudo e avisa por que; a primeira recontagem completa levou cerca de oito minutos, uma execução normal leva cerca de um segundo. **Suba `COUNT_ALGORITHM_VERSION` sempre que `word_count_html` ou `line_count` mudar de comportamento**, senão as contagens congeladas continuam valendo com uma regra que já não é a mesma.
- **`--recount`.** Força a recontagem de palavras e linhas de todos os marcos e imprime toda diferença contra o que estava gravado. Serve de prova de que uma refatoração não mexeu em nenhum número publicado.
- **`--reprice`.** Como antes, agora com a precificação por modelo e por TTL: recalcula só o custo, a partir dos tokens gravados, sem ler git nem transcrição.
- **`--enrich [--dry-run]`.** A migração única de um marco gravado antes do corte por modelo e TTL. Só enriquece um marco se os quatro contadores originais, re-derivados das transcrições, forem exatamente iguais aos gravados; senão recusa e o deixa intacto, e o código de saída é 3. Um marco com custo gravado tem o custo recalculado e ganha um registro em `repricings` com `"reason": "enrich"`; um marco sem custo só ganha o corte dos tokens. **Leia o relatório do `--dry-run` antes de rodar de verdade, e commite o `logbook-metrics.json` antes**, para o estado anterior ficar no git. Tem prazo: depois que a transcrição expira, o marco não pode mais ser enriquecido.
- **Subagentes.** O Claude Code arquiva as transcrições de subagentes em `<sessão>/subagents/*.jsonl`, não ao lado da sessão-mãe, e este script nunca as leu até 20 de setembro de 2026 (cerca de 257 milhões de tokens naquele dia, um quinto a mais que o total contado). Desde então elas **contam**, por decisão do autor: são capturadas por marco em `subagent_tokens` (fato congelado, por modelo e TTL) e o que os totais, os gráficos e o custo leem é `tokens_total`, a soma de `tokens_bucket` (sessões-mãe) com `subagent_tokens`, derivada a cada execução, nunca congelada. `tokens_bucket` e `tokens_split` continuam só das sessões-mãe, porque são o fato que o guarda do `--enrich` confere contra a transcrição. Um token de subagente é atribuído ao próximo commit deste repositório, onde quer que o trabalho tenha acontecido, e 43 das 114 transcrições também citam o caminho de outro repositório (41 o `milestone-loc-tokens-ai-ledger`, cujo diário próprio conta essas 41 pelo caminho dele): os dois diários não devem ser somados. `--reprice --note TEXTO` grava o motivo em cada registro de `repricings`.
- **`unpriced`.** A lista de tokens sem preço só é gravada num custo parcial. Um marco sem custo nenhum já diz tudo com `cost_recorded: null`.

## Se `generate_logbook_metrics.py` for reutilizado em outro repositório

Achado por reuso direto num projeto externo menor, registrado em `NEXT-STEPS.md`: o script funciona bem aqui, mas carrega três decisões implícitas que precisam de ajuste manual antes de rodar em qualquer outro lugar, nenhuma delas exposta como parâmetro de linha de comando.

1. **O sufixo de diretório de sessão** (`target_suffix` em `_project_dir()`, usado por `find_session_jsonl()` e `find_subagent_jsonl()`) é específico deste clone, nesta máquina. Não existe forma segura de descobri-lo por algoritmo, a sanitização de caminho do Claude Code é detalhe interno não documentado. Liste `~/.claude/projects/` uma vez e confirme o nome real antes de trocar o sufixo.
2. **`CONTENT_HTML`, `CODE_GLOBS_PREFIXES` e `GOV_DOCS`** são hardcoded para a estrutura de arquivos deste repositório. Reescreva os três por completo para qualquer outro projeto.
3. **A deduplicação de uso por `message.id`**, dentro de `load_usage_events()`, precisa entrar em qualquer cópia nova deste script desde o início. Sem ela, a contagem de tokens dobra (achado real aqui, corrigido em setembro de 2026, ver `NEXT-STEPS.md`), porque uma mesma mensagem do assistente gera mais de uma linha no transcript, cada uma carregando o total acumulado da mensagem inteira, repetido.
