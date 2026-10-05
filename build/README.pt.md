*Leia em [English](README.md) · [Español](README.es.md).*

# build

Corpos de texto e scripts de montagem que geram as páginas HTML da raiz, mais as verificações que os mantêm honestos.

## Como funciona

Cada página é montada em duas partes: um corpo em HTML por idioma, e um script Python que prefixa todo identificador por idioma (`scope()`), acaba cada bloco de idioma (`common.py`) e cola tudo no envoltório de CSS compartilhado.

O envoltório é extraído da página pronta que já existe, para que todas as páginas permaneçam idênticas em formatação. Alterar o CSS em uma delas e regerar as outras propaga a mudança.

Páginas montadas aqui: `harness-p1.html` a `harness-p4.html`, `harness-toolkit.html`, `harness-playbook.html`, `harness-glossary.html`, `harness-sources.html` e `docs/logbook.html`.

## Arquivos

| Arquivo | Papel |
|---|---|
| `body_p1_{pt,en,es}.html` | corpos da parte 1, extraídos do `harness-p1.html` publicado em 5 de outubro de 2026. O PT é regravado a cada build; o EN e o ES são editáveis |
| `body_p2_{pt,en,es}.html` | corpos da parte 2. O PT é regravado a cada build; o EN e o ES são editáveis |
| `body_p3_*`, `body_p4_*`, `body_playbook_*`, `body_toolkit_*`, `body_glossary_*`, `body_sources_*` | corpos das demais páginas, um por idioma, todos editáveis. São a fonte da verdade |
| `build_p1.py`, `build_p2.py` | montam a parte 1 e a parte 2. Autorreferentes: o envoltório e o corpo PT são lidos de volta da página publicada |
| `build_p3.py`, `build_p4.py`, `build_playbook.py`, `build_toolkit.py`, `build_glossary.py`, `build_sources.py` | montam as demais páginas a partir dos três `body_*` de cada uma. Nunca leem a página publicada de volta |
| `build_logbook.py` | monta `docs/logbook.html` trilíngue a partir de `docs/assets/logbook-metrics.json`, incluindo o gráfico de custo |
| `common.py` | regras compartilhadas por todos os scripts de montagem: a âncora de topo e o fragmento de idioma nos links entre páginas, o atributo `lang` em cada `<main>` |
| `generate_logbook_metrics.py` | reconstrói `docs/assets/logbook-metrics.json` a partir do git, dos transcripts reais da sessão e de `docs/assets/prices.json`, nunca editado à mão. Modos: normal, `--recount`, `--reprice`, `--enrich [--dry-run]`, ver abaixo |
| `docs/assets/prices.json` | livro-razão de preço datado e apensado (dado-fonte, não script). Um marco lê a entrada vigente na própria data e o custo calculado fica congelado depois disso |
| `generate_toolkit_manifest.py` | reconstrói `toolkit.json` a partir de `TOOLS.md`, `sources/inventory.md` e `playbook/README.md`, nunca editado à mão. `--check` só informa se está desatualizado |
| `check_all.py` | o verificador único, ver "Verificações" abaixo |
| `svg_check.py`, `check_upstream.py` | `svg_check.py` compara a geometria de cada SVG inline com o arquivo autônomo em `diagrams/` (rodado pelo `check_all.py` em "paridade"). `check_upstream.py` lê cada origem curada pela API do GitHub para `sources/upstream.json`; precisa do `gh` autenticado e roda à mão, não pelas checagens |
| `check_glossary_order.py`, `check_readme_snapshot.py` | duas verificações que o `check_all.py` roda, também usáveis sozinhas |
| `check_known.json` | achados que existiam antes do `check_all.py`. Uma catraca: só pode encolher |
| `stop_hook.py` | hook de parada do Claude Code, ligado em `.claude/settings.json`: roda o `check_all.py` quando a sessão alterou arquivos publicados e impede o encerramento diante de um achado novo |
| `legacy/` | `build_all.py`, `build_en.py` e `patch_p2.py`, históricos, movidos para cá em 5 de outubro de 2026 para que nenhum agente os execute por engano. Os dois primeiros usam caminhos fixos de sandbox e não rodam neste repositório; o `build_p1.py` os substituiu |

## Verificações

`python build/check_all.py` roda dez checagens de uma vez: travessões, ordem do glossário, texto alternativo dos gráficos do README, `toolkit.json`, links e âncoras, consistência entre partes, fatos repetidos entre glossário e partes, acentos ausentes em português e espanhol, ortografia americana em inglês e paridade de seções, tabelas, SVG e tooltips entre as três línguas. Cada achado diz o arquivo, a linha, o trecho e a correção esperada.

Os achados que existiam antes do script estão em `build/check_known.json` e não derrubam a execução. Qualquer achado fora dessa lista derruba. Quando um é corrigido, o script avisa, e `python build/check_all.py --write-baseline` o tira da lista. A lista só pode encolher. `--only NOME` roda uma checagem, `--strict` ignora a lista, `-v` imprime também os achados conhecidos.

Duas coisas o rodam sem que ninguém peça: o hook de parada (`stop_hook.py`), que protege a sessão de trabalho, e `.github/workflows/check.yml`, que protege o site publicado a cada push e pull request, edição manual inclusive. A configuração do hook e o script são a parte da instalação que só deve mudar com uma pessoa lendo o diff.

## Regras críticas

`scope()` prefixa identificadores de âncora e marcadores de SVG por idioma. Todo conteúdo novo precisa passar por ela, senão as três versões de um mesmo documento colidem e as âncoras apontam para o idioma errado. Escreva os corpos EN e ES sem prefixo de idioma nos ids e âncoras (`id="abertura"`, não `id="pt-abertura"`), porque `scope()` cuida do prefixo no build.

`build_p1.py` e `build_p2.py` extraem o corpo PT direto da página publicada, que é a fonte da verdade, e regravam `body_p1_pt.html` e `body_p2_pt.html` a cada execução. Edite o texto PT da parte 1 ou da parte 2 na página publicada e depois reconstrua. Antes de 5 de outubro de 2026 a parte 1 não tinha script de build nenhum: os corpos PT e ES existiam só dentro da página montada, e `body_en.html` tinha ficado uma revisão inteira para trás.

Os outros seis scripts **não** leem a página publicada de volta. Leem as três línguas de `build/body_*`. Editar uma página publicada à mão, sem espelhar a mudança no corpo, é invisível até a próxima regeneração, que reverte a edição sem aviso. Foi o que aconteceu em 31 de agosto de 2026, quando `build/body_sources_*.html` ficou duas rodadas de correção de citação atrás de `harness-sources.html`. Rode o script depois de qualquer edição direta, ou edite só o corpo e deixe o script montar o arquivo final.

Links entre páginas, num corpo, são escritos sem fragmento (`href="harness-p2.html"`). O `common.py` os reescreve para `harness-p2.html#pt-top`, `#en-top` ou `#es-top`, conforme o bloco de idioma em que estão, porque o JavaScript de troca de idioma lê o prefixo da URL para escolher a aba antes de rolar. Um link sem prefixo, ou com o prefixo do idioma errado, abre a outra página na aba em inglês. Links com âncora explícita precisam do prefixo do idioma de destino (`#en-opening`, `#es-apertura`, `#pt-abertura`). Cada bloco de idioma também começa com um elemento de id `<idioma>-top`, leva o atributo `lang` (`pt-BR`, `en-GB`, `es`), e o título da aba acompanha a troca de idioma, tirado do `<h1>` do bloco.

Renomear um termo do glossário muda a letra que decide sua posição, mas não move a linha sozinho: rode `python build/check_glossary_order.py` depois de qualquer mudança de terminologia, antes de reconstruir. Achado em 11 de setembro de 2026 (duas entradas em português fora de ordem por onze dias, sem ninguém notar, ver `NEXT-STEPS.md`).

Editar `TOOLS.md` (a tabela de coleções instaladas, ou a lista de skills por coleção) ou a tabela "Tools and skills" de `sources/inventory.md` sem rodar `python build/generate_toolkit_manifest.py` na sequência deixa `toolkit.json` desatualizado, do mesmo jeito que editar `harness-sources.html` sem espelhar em `build/` deixa o build seguinte reverter a edição. `--check` acusa a divergência (hash das seções-fonte) sem escrever nada.

## Custo em dinheiro, portado de volta de `milestone-loc-tokens-ai-ledger`

`generate_logbook_metrics.py` ganhou, em 14 de setembro de 2026, a mesma lógica de preço datado e apensado que a própria skill que este projeto gerou (`milestone-loc-tokens-ai-ledger`, ver `NEXT-STEPS.md` item 5) já tinha construído: `load_price_ledger`, `find_price_series`, `price_at` e `compute_cost`, lendo `docs/assets/prices.json`. O custo de um marco é calculado uma vez, no preço vigente na data desse marco, e nunca recalculado depois, mesmo que o livro-razão ganhe uma entrada nova; `load_previous` garante isso lendo o `logbook-metrics.json` da execução anterior antes de sobrescrever.

**Preço que estava errado, corrigido em 20 de setembro de 2026.** A entrada de 13 de setembro registrou o Sonnet 5 a US$3/15, mas o preço cobrado é US$2/10 (o aumento previsto para 1º de setembro foi cancelado, conforme a página de preços da Anthropic, lida na data, junto com a visão geral de modelos). A entrada errada continua no livro-razão, e uma segunda, com `corrects` e a nota do motivo, a substitui: em empate de data, `price_at` escolhe a entrada gravada depois. Como um custo gravado nunca é recalculado por uma execução normal, `python build/generate_logbook_metrics.py --reprice` é o caminho explícito e auditado para esse caso, portado de `milestone-loc-tokens-ai-ledger`: recalcula só o custo dos marcos já gravados, a partir dos tokens já gravados neles, sem ler git nem transcrição, e guarda o custo anterior em `repricings` no próprio marco. Rodar de novo, sem entrada nova no livro-razão, não muda nada. Não use `--reprice` para uma mudança normal de preço: uma entrada com `effective_date` posterior já deixa cada marco antigo no preço que valia na sua data. Aqui, ele levou o custo gravado de US$105,66 para US$70,44 em onze marcos.

**O limite do reprice, fechado em 20 de setembro de 2026.** `tokens_bucket` guarda só os quatro contadores originais, porque é assim que `build_logbook.py` os soma (`sum(m['tokens_bucket'].values())`). Antes, o port precificava toda escrita de cache a `cache_creation_price` (US$2,50 por milhão), e nas transcrições deste projeto todas as escritas de cache lidas são de 1 hora, a US$4,00. O corte por modelo e por TTL agora vive numa chave irmã, `tokens_split`, e `price_milestone` precifica cada modelo com a própria série e as escritas de 1 hora ao preço de 1 hora; uma escrita de 1 hora sob uma entrada sem `cache_creation_1h_price` fica sem preço, nunca ao preço de 5 minutos. Os 79 marcos que já existiam foram migrados com `--enrich`, e o custo gravado dos 14 que tinham um foi de US$77,7944 para US$83,1673 (+US$5,3729), medido marco a marco, o número que a estimativa anterior de cerca de US$4,82 para onze marcos apontava.

**Limite honesto, não escondido:** `docs/assets/prices.json` tem três séries, todas a partir de 13 de setembro de 2026: Sonnet 5, Opus 5 e Haiku 4.5. As duas últimas entraram em 20 de setembro de 2026 sob uma suposição registrada em cada entrada (o preço lido naquele dia vale desde 13 de setembro, sem fonte que date a mudança), ver `NEXT-STEPS.md` item 6. Todo marco anterior a essa data mostra `cost_recorded: null` na saída e "sem preço" no diário publicado, nunca um custo inventado. Isso é esperado, não um bug: este script não afirma um preço que não verificou. Ao contrário do próprio motor de tokens (uma sessão contínua cobrindo o projeto inteiro), o preço de LLM muda por decisão comercial do fornecedor, não por uso deste projeto, então não há como reconstruir retroativamente sem uma fonte real para cada data.

## Congelamento, `--enrich` e `--recount`, portados de `milestone-loc-tokens-ai-ledger` em 20 de setembro de 2026

A regra: congelar o fato de granularidade mais fina e derivar o preço depois. Um custo gravado é um número derivado; os tokens, por modelo e por TTL de cache, são o fato.

- **Execução normal.** Nunca reabre os tokens de um marco já gravado (`tokens_bucket`, `tokens_split`): eles vêm do arquivo, não da transcrição, porque o Claude Code apaga transcrições depois de `cleanupPeriodDays` (30 dias por padrão). Só um commit novo deriva tokens. Palavras e linhas também são reaproveitadas por hash de commit, desde que `count_rules_hash` (uma impressão digital de `CONTENT_HTML`, `CODE_GLOBS_PREFIXES`, `GOV_DOCS` e `COUNT_ALGORITHM_VERSION`) seja a mesma da execução que as gravou. Sem a marca, ou com uma marca diferente, o script reconta tudo e avisa por que; a primeira recontagem completa levou cerca de oito minutos, uma execução normal leva cerca de um segundo. **Suba `COUNT_ALGORITHM_VERSION` sempre que `word_count_html` ou `line_count` mudar de comportamento**, senão as contagens congeladas continuam valendo com uma regra que já não é a mesma.
- **`--recount`.** Força a recontagem de palavras e linhas de todos os marcos e imprime toda diferença contra o que estava gravado. Serve de prova de que uma refatoração não mexeu em nenhum número publicado.
- **`--reprice`.** Como antes, agora com a precificação por modelo e por TTL: recalcula só o custo, a partir dos tokens gravados, sem ler git nem transcrição.
- **`--enrich [--dry-run]`.** A migração única de um marco gravado antes do corte por modelo e TTL. Só enriquece um marco se os quatro contadores originais, re-derivados das transcrições, forem exatamente iguais aos gravados; senão recusa e o deixa intacto, e o código de saída é 3. Um marco com custo gravado tem o custo recalculado e ganha um registro em `repricings` com `"reason": "enrich"`; um marco sem custo só ganha o corte dos tokens. **Leia o relatório do `--dry-run` antes de rodar de verdade, e commite o `logbook-metrics.json` antes**, para o estado anterior ficar no git. Tem prazo: depois que a transcrição expira, o marco não pode mais ser enriquecido.
- **Subagentes.** O Claude Code arquiva as transcrições de subagentes em `<sessão>/subagents/*.jsonl`, não ao lado da sessão-mãe, e este script nunca as leu até 20 de setembro de 2026 (cerca de 257 milhões de tokens naquele dia, um quinto a mais que o total contado). Desde então elas **contam**, por decisão do autor: são capturadas por marco em `subagent_tokens` (fato congelado, por modelo e TTL) e o que os totais, os gráficos e o custo leem é `tokens_total`, a soma de `tokens_bucket` (sessões-mãe) com `subagent_tokens`, derivada a cada execução, nunca congelada. `tokens_bucket` e `tokens_split` continuam só das sessões-mãe, porque são o fato que o guarda do `--enrich` confere contra a transcrição. Um token de subagente é atribuído ao próximo commit deste repositório, onde quer que o trabalho tenha acontecido, e 43 das 114 transcrições também citam o caminho de outro repositório (41 o `milestone-loc-tokens-ai-ledger`, cujo diário próprio conta essas 41 pelo caminho dele): os dois diários não devem ser somados. `--reprice --note TEXTO` grava o motivo em cada registro de `repricings`.
- **`unpriced`.** A lista de tokens sem preço só é gravada num custo parcial. Um marco sem custo nenhum já diz tudo com `cost_recorded: null`.

## Ao regerar o diário de bordo, em ordem

O diário descreve os commits anteriores, então a regeneração vem depois deles. O commit da própria regeneração é sempre o único marco sem narrativa, e a regeneração seguinte o descreve.

1. `python build/generate_logbook_metrics.py` (cerca de um segundo; recontar tudo só com `--recount` ou se as regras de contagem mudarem).
2. Escrever a narrativa dos marcos novos em `COMMIT_TXT`, em `build_logbook.py`, nas três línguas. O build para com `KeyError` no hash que falta, de propósito.
3. `python build/build_logbook.py`.
4. Reexportar os três gráficos do README a partir de `docs/logbook.html`, em `docs/assets/logbook-*.png`, com um recorte exato de 616 por 230 a 2x, que dá 1232 por 460 (sem o recorte sai 462).
5. Atualizar, nos três README, o texto alternativo do gráfico de palavras (palavras e número de marcos) e conferir com `python build/check_readme_snapshot.py`.
6. `python build/generate_toolkit_manifest.py --check`, e depois `python build/check_all.py`.

## Se `generate_logbook_metrics.py` for reutilizado em outro repositório

Achado por reuso direto num projeto externo menor, registrado em `NEXT-STEPS.md`: o script funciona bem aqui, mas carrega três decisões implícitas que precisam de ajuste manual antes de rodar em qualquer outro lugar, nenhuma delas exposta como parâmetro de linha de comando.

1. **O sufixo de diretório de sessão** (`target_suffix` em `_project_dir()`, usado por `find_session_jsonl()` e `find_subagent_jsonl()`) é específico deste clone, nesta máquina. Não existe forma segura de descobri-lo por algoritmo, a sanitização de caminho do Claude Code é detalhe interno não documentado. Liste `~/.claude/projects/` uma vez e confirme o nome real antes de trocar o sufixo.
2. **`CONTENT_HTML`, `CODE_GLOBS_PREFIXES` e `GOV_DOCS`** são hardcoded para a estrutura de arquivos deste repositório. Reescreva os três por completo para qualquer outro projeto.
3. **A deduplicação de uso por `message.id`**, dentro de `load_usage_events()`, precisa entrar em qualquer cópia nova deste script desde o início. Sem ela, a contagem de tokens dobra (achado real aqui, corrigido em setembro de 2026, ver `NEXT-STEPS.md`), porque uma mesma mensagem do assistente gera mais de uma linha no transcript, cada uma carregando o total acumulado da mensagem inteira, repetido.
