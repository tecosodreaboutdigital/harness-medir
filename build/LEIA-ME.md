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
| `body_kit_pt.html` | corpo do guia compacto em português, editável, organizado pelo MEDIR |
| `body_en.html` | corpo da parte 1 em inglês |
| `build_p2.py` | monta `harness-p2.html` trilíngue |
| `build_kit.py` | monta `harness-caixa-de-ferramentas.html`, hoje só PT |
| `build_all.py` | monta a versão trilíngue da parte 1 |
| `build_en.py` | gerou a versão em inglês da parte 1 |
| `patch_p2.py` | histórico, aplicou seções novas na parte 2 antes de `build_p2.py` virar trilíngue |

## Regra crítica

A função `scope()` prefixa identificadores de âncora e marcadores de SVG por idioma. Todo conteúdo novo precisa passar por ela, senão as três versões de um mesmo documento colidem e as âncoras apontam para o idioma errado.

`build_p2.py` desde 30 de agosto de 2026 extrai o corpo PT direto do `harness-p2.html` vigente, que é a fonte da verdade, e regrava `body_p2_pt.html` a cada execução. Antes disso, `patch_p2.py` aplicava seções novas direto no HTML final sem atualizar o corpo em `build/`, e o arquivo ficou desatualizado por um tempo. Escreva os corpos EN e ES sem prefixo de idioma nos ids e âncoras (`id="abertura"`, não `id="pt-abertura"`), porque `scope()` cuida do prefixo no build.

Links cruzados para `harness-p1.html` com âncora precisam do prefixo do idioma de destino (`#en-opening`, `#es-apertura`, `#pt-abertura`), porque o JavaScript de troca de idioma lê o prefixo da URL para escolher a aba antes de rolar até o elemento. Um link sem esse prefixo, ou com o prefixo do idioma errado, sempre abre a parte 1 na aba PT.
