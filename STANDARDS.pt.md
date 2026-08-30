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

## Glossário

Estilo de livro. Ordem alfabética ignorando acentos. Sem filete entre verbetes. Termo em negrito, dois pontos, definição na mesma linha, origem ao final em itálico com link. Recuo pendente.

No corpo do texto, o termo aparece sublinhado em pontilhado, com dica ao passar o cursor e link para o verbete.

Nomes próprios entram pelo sobrenome: "Deming, W. Edwards".

---

## Referências

**Link só onde a URL foi verificada.** Quando a origem é conhecida mas o endereço não foi conferido, a origem aparece em texto sem link.

Referências apontam para a fonte primária, nunca para blog de consultoria ou vitrine de skills sem repositório de origem visível.

Um inventário que só recomenda não é inventário, é catálogo de fornecedor. Toda ficha traz também quando não usar.

---

## Navegação cruzada

Quatro camadas, todas implementadas:

1. Barra de série no topo de cada documento, ao lado do seletor de idioma.
2. Links no corpo: menções a uma faixa ou ao MEDIR levam à seção correspondente da parte 1. Menções a uma ferramenta levam à ficha dela no guia compacto.
3. Um bloco "Onde você está" ao fim de cada peça.
4. Um glossário com redação única por verbete, replicada entre documentos.

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
