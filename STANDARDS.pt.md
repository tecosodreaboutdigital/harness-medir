*Leia em [English](STANDARDS.md) · [Español](STANDARDS.es.md).*

# Padrões

Regras não negociáveis deste projeto. Leia antes de editar qualquer arquivo.

---

## Escrita

**Travessão é proibido em qualquer circunstância.** Não use em nenhum idioma. Substitua por vírgula, dois pontos, parênteses ou ponto final. Esta é a regra mais violada e a mais importante.

**Hífen é permitido**, inclusive hifenização automática no texto justificado.

**Registro da prosa:** narrativo e argumentado, na linha de Adam Grant, Brené Brown, Simon Sinek e Malcolm Gladwell. Nada de despejo de bullets. O texto argumenta, não lista.

**Tom:** direto. Sem introdução longa, sem transição vazia, sem conclusão redundante, sem reforço positivo.

**Correção factual tem prioridade sobre suavização.** Atribuições erradas são corrigidas no texto. Ferramenta sem fonte verificada não é citada.

**Evitar:** palavras de preenchimento como "genuinamente", "honestamente", "simplesmente" (e seus equivalentes em inglês e espanhol). Evitar o abuso da construção "não é X, é Y". Evitar aspas de ironia em torno de termos inventados.

---

## Formatação de documento

| Elemento | Especificação |
|---|---|
| Página | A4, margens de 2 cm em cima e embaixo, 1,5 cm nas laterais |
| Corpo | Aptos ou Aptos Light, 10,5, justificado |
| Título nível 1 | 14, negrito |
| Título nível 2 | 12 |
| Numeração de seções | Número na própria linha do título. Sem rótulo pequeno acima. Sem numeração de subitens |
| Tabelas | Largura total, cabeçalho centralizado em 8, corpo em 9, sem sombreamento, sem cores alternadas |
| Legendas de figura e notas de rodapé | Sem borda, itálico, tamanho 9 |
| Citação em destaque | Sem borda nenhuma, fundo cinza azulado claro, tamanho 9, protegida contra quebra de página |
| Blocos de código | Mesmo fundo das citações em destaque, sem borda, 8,5 na impressão |
| Saída | Somente HTML. Nada de DOCX, nada de Markdown para artigos |

Exceção à última linha: skills e modelos operacionais nascem em Markdown, porque são artefatos de repositório.

---

## Sistema visual

Diagramas em SVG inline, traço de 0,7, sem preenchimento, sem cor. Rótulos em versaletes espaçados. Legendas em itálico 9, sem borda.

Uma exceção deliberada: o diagrama de faixas usa altura crescente das caixas para representar autonomia.

Não usar bibliotecas de gráfico. Não usar imagens rasterizadas.

---

## Diagramas

Todo diagrama nasce como rascunho em Mermaid, dentro do arquivo md correspondente. Não existe pipeline de renderização: nada neste projeto transforma o Mermaid no SVG inline de forma mecânica. O rascunho é um plano estrutural em texto puro, legível em diff, e que o GitHub renderiza nativamente quando o arquivo é aberto lá, nada além disso.

O SVG inline no HTML é desenhado à mão, no sistema visual do projeto, para bater com a estrutura do rascunho. Isso é deliberado, não um atalho por falta de ferramenta: um renderizador genérico de Mermaid produz o tema e o layout automático dele, e nenhum dos dois bate com o sistema de traço fino, sem preenchimento, sem cor deste projeto, então desenhar à mão é o caminho direto, não um contorno.

Ao alterar estrutura ou rótulo, altere primeiro o rascunho em Mermaid, depois redesenhe o SVG à mão pra bater com ele. Alterar apenas o SVG deixa o rascunho desatualizado e a próxima sessão trabalha com o mapa errado.

Cada diagrama traz, no md, o propósito e a nota de renderização, incluindo o que precisa saltar aos olhos e a frase que a legenda carrega.

---

## Glossário

Página única compartilhada desde 30 de agosto de 2026: `harness-glossary.html`, trilíngue, um verbete por termo para a série inteira (partes 1 a 4, o guia compacto). Nenhum documento mantém mais sua própria seção de glossário; um termo definido na parte 2 fica disponível, sem mudança, para as partes 3 e 4.

Estilo de livro. Ordem alfabética ignorando acentos. Sem filete entre verbetes. Termo em negrito, dois pontos, definição na mesma linha, origem ao final em itálico com link. Recuo pendente. Nomes próprios entram pelo sobrenome: "Deming, W. Edwards".

No corpo do texto, o termo aparece sublinhado em pontilhado, com dica ao passar o cursor (o atributo `data-tip` carrega a definição curta, mostrada localmente, sem navegar) e o clique leva a `harness-glossary.html#<idioma>-<slug>`, chegando exatamente naquele verbete. Nunca linkar um termo para uma âncora local `#g-slug` dentro do próprio artigo, essa âncora não existe mais lá.

Quando uma parte nova introduz um termo, acrescente-o direto em `harness-glossary.html` (nos três idiomas), mantendo a posição alfabética, e linke a ele a partir do corpo da parte. Não duplique a definição de volta na parte.

---

## Referências

Página única compartilhada desde 30 de agosto de 2026: `harness-sources.html`, trilíngue, agrupada por onde a pesquisa foi levantada (fontes fundadoras, depois um grupo por parte). Toda citação em qualquer parte aponta pra cá; nenhum documento mantém mais sua própria lista numerada de fontes.

**Link só onde a URL foi verificada.** Quando a origem é conhecida mas o endereço não foi conferido, a entrada aparece em texto simples (classe `orig-plain`) com a lacuna declarada na própria entrada, nunca escondida.

Referências apontam para a fonte primária, nunca para blog de consultoria ou vitrine de skills sem repositório de origem visível.

Um inventário que só recomenda não é inventário, é catálogo de fornecedor. Toda ficha traz também quando não usar.

---

## Navegação cruzada

Quatro camadas, todas implementadas:

1. **Barra de série**, um componente único compartilhado (`.topbar`) no topo de cada documento, centralizado na página, fixo ao rolar, `docs/logbook.html` incluído desde 31 de agosto de 2026. Uma linha só: as partes numeradas ligadas por `·`, uma `|` antes dos documentos companheiros, depois guia compacto, glossário e fontes também ligados por `·`, uma segunda `|` antes de um pequeno ícone de linha em degraus que leva ao diário do projeto, depois o seletor de idioma entre chaves `{ }` no fim. O ícone não carrega rótulo de texto, só um atributo `title` para o tooltip ao passar o mouse, então nunca disputa espaço com as partes e companheiros; no próprio diário, ele aparece como o indicador de página atual em vez de link, igual a uma parte aparece quando é a página em que você já está. A página atual aparece como texto simples, não como link; uma parte ainda não publicada aparece esmaecida e sem link. Os rótulos, os destinos da barra e o tooltip do ícone trocam de idioma junto com o seletor, dirigidos pelo objeto `SERIES` e pela chamada `setSeries()` dentro do `set()` de cada página, nunca duplicados à mão por idioma.
2. Links no corpo: menções a uma faixa ou ao MEDIR levam à seção correspondente da parte 1. Menções a uma ferramenta levam à ficha dela no guia compacto. Menções a um termo do glossário levam a `harness-glossary.html`. Citações levam a `harness-sources.html`.
3. Um bloco "Onde você está" ao fim de cada peça.
4. O próprio glossário e a própria página de fontes: uma redação por verbete, uma página só, linkada de todo lugar.

---

## Idiomas

O inglês é o idioma de produção primário deste projeto nos dois repositórios públicos, decisão tomada em 30 de agosto de 2026. Todo conteúdo novo é escrito primeiro em inglês; português e espanhol são traduções completas produzidas a partir dele, nunca o caminho inverso. Isso não exige refazer conteúdo que já estava completo nos três idiomas antes dessa data.

Três versões completas por peça, no mesmo arquivo, com seletor. Inglês é a aba padrão.

**Espanhol:** tratamento por "tú", não "usted".
**Inglês:** grafia britânica.
**MEDIR** permanece como nome próprio do método nos três idiomas.

Identificadores de âncora e marcadores de SVG são prefixados por idioma. Nunca gerar conteúdo novo sem passar pela função `scope()`.

Uma dica de idioma do navegador se aplica nas quatro páginas HTML trilíngues: se o idioma do navegador do visitante for português ou espanhol e não corresponder à aba ativa, e nenhuma âncora com prefixo de idioma já estiver roteando a página, um banner dispensável nesse idioma oferece a troca. Qualquer outro idioma de navegador cai silenciosamente para o inglês. O GitHub renderiza os arquivos Markdown do repositório da skill sem executar JavaScript, então o equivalente lá é uma linha estática de navegação de idioma no topo de cada arquivo, não uma linha adaptativa.

---

## Ficha de ferramenta no guia compacto

Seis campos, sempre nesta ordem, em prosa e não em lista solta:

1. Qual problema isso resolve
2. O que você ganha na prática
3. Para quem serve, por faixa N0 a N3
4. Faixa mínima
5. Quando não usar
6. Como começar em quinze minutos

---

## Padrão de escrita de skill

Herdado das melhores coleções públicas e adotado como padrão do projeto:

**Regra inegociável no topo,** curta e sem ambiguidade.

**Bandeiras vermelhas logo abaixo:** as racionalizações que o sistema provavelmente vai usar para justificar não seguir a regra. O alvo não é ensinar a regra, que ele já conhece, é impedir que ele se convença a não segui-la.

**Critério de pronto verificável,** de preferência a saída de um comando e não uma opinião.

**Teto de tentativas** com caminho de saída explícito.

**Seção Nunca** ao final.

**Limites honestos** declarados: o que foi exercitado, o que é inferência, o que a skill não faz.
