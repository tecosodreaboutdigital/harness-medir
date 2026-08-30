# build

Corpos de texto e scripts de montagem usados para gerar os HTML da raiz.

## Como funciona

Cada artigo é montado em duas partes: um corpo em HTML com marcadores de glossário no formato `{{termo}}`, e um script Python que injeta o glossário, resolve os marcadores, prefixa os identificadores por idioma e cola tudo no envoltório de CSS.

O envoltório de CSS é extraído do arquivo já pronto anterior, para que os quatro documentos permaneçam idênticos em formatação. Alterar o CSS em um deles e regerar os outros propaga a mudança.

## Arquivos

| Arquivo | Papel |
|---|---|
| `body_p2_pt.html` | corpo da parte 2 em português |
| `body_kit_pt.html` | corpo do guia compacto, versão antiga a ser refeita |
| `body_en.html` | corpo da parte 1 em inglês |
| `build_p2.py` | monta `harness-p2.html` |
| `build_kit.py` | monta `harness-caixa-de-ferramentas.html` |
| `build_all.py` | monta a versão trilíngue da parte 1 |
| `build_en.py` | gerou a versão em inglês da parte 1 |
| `patch_p2.py` | histórico, aplicou seções novas na parte 2 |

## Regra crítica

A função `scope()` prefixa identificadores de âncora e marcadores de SVG por idioma. Todo conteúdo novo precisa passar por ela, senão as três versões de um mesmo documento colidem e as âncoras apontam para o idioma errado.
