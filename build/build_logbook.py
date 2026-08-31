# -*- coding: utf-8 -*-
# Monta docs/logbook.html trilingue a partir de
# docs/assets/logbook-metrics.json (gerado por
# build/generate_logbook_metrics.py). Reusa o envoltorio CSS e o
# JavaScript trilingue de harness-p2.html, mesmo padrao das outras
# pecas. Reexecutavel: os graficos e a linha do tempo sao gerados a
# partir do JSON, nunca escritos a mao.
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, 'docs', 'assets', 'logbook-metrics.json'), encoding='utf-8') as fh:
    DATA = json.load(fh)

MS = DATA['milestones']
REMAINING = DATA['tokens_since_last_commit']

# ---------- traducao das mensagens de commit, uma vez, por hash ----------
COMMIT_TXT = {
    'a732861': {
        'pt': 'Commit inicial. O repositório vai ao ar com o que já existia: as partes 1 e 2 em português, a skill de briefing, o inventário de fontes.',
        'en': 'Initial commit. The repository goes live with what already existed: parts 1 and 2 in Portuguese, the briefing skill, the source inventory.',
        'es': 'Commit inicial. El repositorio sale a la luz con lo que ya existía: las partes 1 y 2 en portugués, la skill de briefing, el inventario de fuentes.',
    },
    '1271135': {
        'pt': 'Guia compacto reescrito, organizado pelos cinco passos do MEDIR em vez de por categoria de produto. Dezessete fichas de seis campos, diagnóstico de faixa no início, crítica registrada em cada passo.',
        'en': 'Compact guide rewritten, organised by the five MEDIR steps instead of by product category. Seventeen six-field entries, a tier diagnostic at the start, a registered critique in every step.',
        'es': 'Guía compacta reescrita, organizada por los cinco pasos del MEDIR en vez de por categoría de producto. Diecisiete fichas de seis campos, diagnóstico de banda al inicio, crítica registrada en cada paso.',
    },
    'f5fbfa7': {
        'pt': 'Parte 2 traduzida para inglês e espanhol. O documento vira trilíngue, glossário e fontes replicados nos três idiomas, exemplos de skill traduzidos por completo.',
        'en': 'Part 2 translated into English and Spanish. The document becomes trilingual, glossary and sources replicated in all three languages, skill examples translated in full.',
        'es': 'Parte 2 traducida al inglés y al español. El documento se vuelve trilingüe, glosario y fuentes replicados en los tres idiomas, ejemplos de skill traducidos por completo.',
    },
    '111933a': {
        'pt': 'Trinta skills de terceiro instaladas para uso no projeto, auditadas antes de instalar. FERRAMENTAS.md criado como registro vivo do que é usado de fato (renomeado TOOLS.md em 30 de agosto de 2026, na reestruturação para inglês primário).',
        'en': 'Thirty third-party skills installed for use on the project, audited before installing. FERRAMENTAS.md created as a living record of what is actually used (renamed TOOLS.md on 30 August 2026, in the English-primary restructuring).',
        'es': 'Treinta skills de terceros instaladas para uso en el proyecto, auditadas antes de instalar. FERRAMENTAS.md creado como registro vivo de lo que realmente se usa (renombrado TOOLS.md el 30 de agosto de 2026, en la reestructuración a inglés primario).',
    },
    '51af961': {
        'pt': 'Correção: a skill própria do projeto, levantando-briefing, estava documentada junto das de terceiro. Separada, e ativada de fato neste ambiente.',
        'en': 'Fix: the project’s own skill, levantando-briefing, was documented alongside the third-party ones. Separated, and actually activated in this environment.',
        'es': 'Corrección: la skill propia del proyecto, levantando-briefing, estaba documentada junto con las de terceros. Separada, y activada de verdad en este entorno.',
    },
    '38444ac': {
        'pt': 'levantando-briefing ganha repositório próprio e público, no mesmo padrão das demais skills citadas. O harness-medir passa a só apontar para ela.',
        'en': 'levantando-briefing gets its own public repository, in the same pattern as the other cited skills. harness-medir now only points to it.',
        'es': 'levantando-briefing gana repositorio propio y público, en el mismo patrón que las demás skills citadas. harness-medir pasa a solo apuntar hacia allí.',
    },
    '3000e88': {
        'pt': 'Diário de bordo criado, trilíngue, gerado do git e do uso real da sessão. GitHub Pages ativado, com .nojekyll para servir os HTML como estão.',
        'en': 'Project log created, trilingual, generated from git and the session’s real usage. GitHub Pages enabled, with .nojekyll to serve the HTML files as they are.',
        'es': 'Diario de bordo creado, trilingüe, generado a partir de git y del uso real de la sesión. GitHub Pages activado, con .nojekyll para servir los HTML tal cual.',
    },
    '9d3892f': {
        'pt': 'Início da reestruturação para inglês primário. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md e as demais peças renomeadas para inglês, idioma padrão das peças já trilíngues trocado de PT para EN, aviso de idioma do navegador adicionado.',
        'en': 'Start of the English-primary restructuring. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md and the other pieces renamed to English, default tab of the already-trilingual pieces switched from PT to EN, browser-language hint added.',
        'es': 'Inicio de la reestructuración hacia el inglés primario. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md y las demás piezas renombradas al inglés, pestaña predeterminada de las piezas ya trilingües cambiada de PT a EN, pista de idioma del navegador añadida.',
    },
    '65d9c1e': {
        'pt': 'Guia compacto traduzido para inglês e espanhol, com inglês como aba padrão. Repositório da skill de briefing renomeado de levantando-briefing para intake-briefing.',
        'en': 'Compact guide translated into English and Spanish, with English as the default tab. The briefing skill’s repository renamed from levantando-briefing to intake-briefing.',
        'es': 'Guía compacta traducida al inglés y al español, con el inglés como pestaña predeterminada. Repositorio de la skill de briefing renombrado de levantando-briefing a intake-briefing.',
    },
    '1106102': {
        'pt': 'README, STANDARDS, STATUS, NEXT-STEPS e TOOLS reescritos em inglês como versão primária, cada um com tradução completa em português e espanhol. Fecha a reestruturação para inglês primário nos dois repositórios públicos.',
        'en': 'README, STANDARDS, STATUS, NEXT-STEPS and TOOLS rewritten in English as the primary version, each with a full Portuguese and Spanish translation. Closes the English-primary restructuring across both public repositories.',
        'es': 'README, STANDARDS, STATUS, NEXT-STEPS y TOOLS reescritos en inglés como versión primaria, cada uno con traducción completa al portugués y al español. Cierra la reestructuración hacia el inglés primario en los dos repositorios públicos.',
    },
    'd8ff518': {
        'pt': 'Diário de bordo regerado sobre o histórico real completo até aqui, quatro marcos novos documentados: a criação do próprio diário, o início e o fechamento da reestruturação para inglês primário, a tradução do guia compacto. Fecha a sessão 1.',
        'en': 'Project log regenerated over the full real history so far, four new milestones documented: the log’s own creation, the start and close of the English-primary restructuring, the compact guide’s translation. Closes session 1.',
        'es': 'Diario de bordo regenerado sobre el historial real completo hasta aquí, cuatro hitos nuevos documentados: la creación del propio diario, el inicio y el cierre de la reestructuración hacia el inglés primario, la traducción de la guía compacta. Cierra la sesión 1.',
    },
    'bb19deb': {
        'pt': 'Sessão 2. Quatro skills recomendadas de fora avaliadas (ponytail, no-ai-slop, taste-skill, impeccable) por relevância, manutenção, contribuidores e licença. Só impeccable adotada, como décima oitava ficha do guia compacto, em Inspecionar.',
        'en': 'Session 2. Four externally recommended skills evaluated (ponytail, no-ai-slop, taste-skill, impeccable) on relevance, maintenance, contributors and licence. Only impeccable adopted, as the compact guide’s eighteenth entry, in Inspect.',
        'es': 'Sesión 2. Cuatro skills recomendadas desde afuera evaluadas (ponytail, no-ai-slop, taste-skill, impeccable) por relevancia, mantenimiento, colaboradores y licencia. Solo impeccable adoptada, como la decimoctava ficha de la guía compacta, en Inspeccionar.',
    },
    'dbeb0c1': {
        'pt': 'Diário de bordo regerado para incluir o marco da curadoria de impeccable.',
        'en': 'Project log regenerated to include the impeccable curation milestone.',
        'es': 'Diario de bordo regenerado para incluir el hito de la curaduría de impeccable.',
    },
    'c5a3fa0': {
        'pt': 'Dossiê de trabalho para as partes 3 e 4 adicionado: diagnóstico em três camadas, sete eixos de pesquisa da parte 3 já com fontes verificadas, especificação de dez diagramas. Propõe uma quarta parte para a série, ainda não formalizada em README.md nem em STATUS.md por decisão explícita.',
        'en': 'Working dossier for parts 3 and 4 added: a three-layer diagnosis, seven research axes for part 3 already with verified sources, a ten-diagram specification. Proposes a fourth part for the series, not yet formalised in README.md or STATUS.md by explicit decision.',
        'es': 'Dosier de trabajo para las partes 3 y 4 añadido: diagnóstico en tres capas, siete ejes de investigación de la parte 3 ya con fuentes verificadas, especificación de diez diagramas. Propone una cuarta parte para la serie, todavía no formalizada en README.md ni en STATUS.md por decisión explícita.',
    },
    '223b64a': {
        'pt': 'Diário de bordo regerado para incluir os marcos que faltavam: a regeneração anterior do próprio diário, e o dossiê de trabalho das partes 3 e 4. O diário tinha ficado uma sessão atrasado em relação ao git.',
        'en': 'Project log regenerated to include the milestones that were missing: the log’s own previous regeneration, and the working dossier for parts 3 and 4. The log had fallen one session behind the git history.',
        'es': 'Diario de bordo regenerado para incluir los hitos que faltaban: la regeneración anterior del propio diario, y el dosier de trabajo de las partes 3 y 4. El diario se había quedado una sesión atrás respecto al historial de git.',
    },
    '35cc04d': {
        'pt': 'Fecha os três primeiros itens da fila do dossiê de partes 3 e 4: os documentos de governança passam a descrever quatro partes em três camadas, 32 fontes de pesquisa entram no inventário, nove diagramas Mermaid viram SVG desenhado à mão, prontos para as duas peças ainda não escritas.',
        'en': 'Closes the first three items of the parts 3 and 4 dossier’s work queue: the governance documents now describe four parts across three layers, 32 research sources enter the inventory, nine Mermaid sketches become hand-drawn SVG, ready for the two pieces still unwritten.',
        'es': 'Cierra los tres primeros elementos de la cola de trabajo del dosier de las partes 3 y 4: los documentos de gobernanza ahora describen cuatro partes en tres capas, 32 fuentes de investigación entran al inventario, nueve bocetos Mermaid se convierten en SVG dibujado a mano, listos para las dos piezas todavía sin escribir.',
    },
    '059d3f6': {
        'pt': 'Corrige a redação da regra de diagramas, que sugeria um pipeline automático de Mermaid para SVG nunca usado neste projeto, e registra a proteção de branch configurada na main via API do GitHub.',
        'en': 'Fixes the diagrams rule’s wording, which had suggested an automatic Mermaid-to-SVG pipeline this project never used, and records the branch protection configured on main via the GitHub API.',
        'es': 'Corrige la redacción de la regla de diagramas, que sugería una canalización automática de Mermaid a SVG que este proyecto nunca usó, y registra la protección de rama configurada en main vía la API de GitHub.',
    },
    'b81f378': {
        'pt': 'Diário de bordo regerado para incluir os marcos M15 a M17: o dossiê de trabalho das partes 3 e 4, o fechamento dos três primeiros itens da fila do dossiê, e a correção da regra de diagramas junto com a proteção de branch.',
        'en': 'Project log regenerated to include milestones M15 to M17: the parts 3 and 4 working dossier, the closing of the first three items of the dossier’s queue, and the diagrams rule fix alongside the branch protection.',
        'es': 'Diario de bordo regenerado para incluir los hitos M15 a M17: el dosier de trabajo de las partes 3 y 4, el cierre de los tres primeros elementos de la cola del dosier, y la corrección de la regla de diagramas junto con la protección de rama.',
    },
    '67f08a5': {
        'pt': 'Renderiza os nove SVGs dos diagramas pela primeira vez, via Chrome headless, e corrige cinco bugs reais de sobreposição de coordenada achados só por inspeção visual (texto cortado, conector duplicado, legenda estourando o canvas, linha atravessando caixa, colunas sobrepostas). Gera um PNG por diagrama para publicação no Medium.',
        'en': 'Renders the nine diagram SVGs for the first time, via headless Chrome, and fixes five real coordinate-overlap bugs found only by visual inspection (text cut by a line, a duplicate connector, a caption overflowing the canvas, a line crossing a box, overlapping columns). Generates one PNG per diagram for Medium publication.',
        'es': 'Renderiza los nueve SVG de los diagramas por primera vez, vía Chrome headless, y corrige cinco bugs reales de superposición de coordenadas encontrados solo por inspección visual (texto cortado, conector duplicado, leyenda desbordando el lienzo, línea atravesando una caja, columnas superpuestas). Genera un PNG por diagrama para publicación en Medium.',
    },
    'd1babbd': {
        'pt': 'Mergeia direto na main a validação dos diagramas e os PNGs para o Medium, por decisão do autor.',
        'en': 'Merges the diagram validation and the Medium PNGs directly into main, by the author’s decision.',
        'es': 'Mergea directamente en main la validación de los diagramas y los PNG para Medium, por decisión del autor.',
    },
    '6f1c33e': {
        'pt': 'Escreve a parte 3 completa nos três idiomas, com os cinco diagramas embutidos e totalmente traduzidos, e refaz a arquitetura de navegação da série: uma barra de topo única, centralizada e reativa ao idioma, e um glossário e uma página de fontes compartilhados, substituindo o que cada artigo carregava separado.',
        'en': 'Writes part 3 in full, all three languages, with the five diagrams inline and fully translated, and rebuilds the series’ navigation architecture: a single, centred, language-reactive top bar, and a shared glossary and sources page, replacing what each article used to carry on its own.',
        'es': 'Escribe la parte 3 completa en los tres idiomas, con los cinco diagramas incorporados y totalmente traducidos, y rehace la arquitectura de navegación de la serie: una barra superior única, centrada y reactiva al idioma, y un glosario y una página de fuentes compartidos, reemplazando lo que cada artículo llevaba por separado.',
    },
    '395c6cc': {
        'pt': 'Mergeia direto na main a parte 3 completa e a nova arquitetura de série, por decisão do autor.',
        'en': 'Merges the completed part 3 and the new series architecture directly into main, by the author’s decision.',
        'es': 'Mergea directamente en main la parte 3 completa y la nueva arquitectura de serie, por decisión del autor.',
    },
    '33a92e9': {
        'pt': 'Diário de bordo regerado, e três bugs reais corrigidos no processo: a contagem de palavras publicadas ignorava a parte 3, o glossário e as fontes, prestes a mostrar queda entre marcos onde na verdade houve crescimento; o extrator do envoltório cortava no marcador errado desde que a barra de topo chegou, arrastando a barra de série inteira para dentro do diário; o gráfico de crescimento sobrepunha rótulos vizinhos a partir de um certo número de marcos. Os três corrigidos na fonte, vinte e dois marcos completos.',
        'en': 'Project log regenerated, and three real bugs fixed along the way: the published-word count skipped part 3, the glossary and the sources page, about to show a fall between milestones where growth had actually happened; the shell extractor cut on the wrong marker once the top bar arrived, dragging the whole series bar into the log; the growth chart’s point labels started overlapping past a certain number of milestones. All three fixed at the source, twenty-two milestones complete.',
        'es': 'Diario de bordo regenerado, y tres bugs reales corregidos en el proceso: el conteo de palabras publicadas se saltaba la parte 3, el glosario y la página de fuentes, a punto de mostrar una caída entre hitos donde en realidad hubo crecimiento; el extractor del envoltorio cortaba en el marcador equivocado desde que llegó la barra superior, arrastrando la barra de serie entera hacia el diario; el gráfico de crecimiento superponía etiquetas vecinas a partir de cierto número de hitos. Los tres corregidos en la fuente, veintidós hitos completos.',
    },
    '241f320': {
        'pt': 'README atualizado nas três línguas: ganha uma linha apontando para o GitHub Pages publicado, a árvore de arquivos passa a listar a parte 3 e os dois companheiros compartilhados, e dois diagramas (D6, as três camadas do framework, e D1, a separação de poderes) entram como imagem, usando o PNG de fundo branco em vez do SVG de fundo transparente, ilegível no tema escuro do GitHub.',
        'en': 'README updated in all three languages: gains a line pointing at the published GitHub Pages site, the file tree now lists part 3 and the two shared companions, and two diagrams (D6, the framework’s three layers, and D1, the separation of powers) are embedded as images, using the white-background PNG rather than the transparent-background SVG, illegible in GitHub’s dark theme.',
        'es': 'README actualizado en los tres idiomas: gana una línea que apunta al GitHub Pages publicado, el árbol de archivos ahora lista la parte 3 y los dos compañeros compartidos, y dos diagramas (D6, las tres capas del marco, y D1, la separación de poderes) se incorporan como imagen, usando el PNG de fondo blanco en vez del SVG de fondo transparente, ilegible en el tema oscuro de GitHub.',
    },
    'b31515a': {
        'pt': 'A pesquisa da parte 4 chega pronta, seis eixos, entregue pelo autor fora da sessão, e passa por verificação de fonte primária nos dois achados mais carregados: o caso SCHUFA do TJUE, que torna a taxa de reprovação no portão exposição jurídica, e o caso das 20.225 contas do Instagram, que abre a peça. Quatro ajustes aplicados, as três fontes do SCHUFA separadas, a fonte de patente do quase-acidente trocada pelo triângulo de Heinrich, o par Kyndryl verificado na origem, o número da Gartner não localizado e mantido como parcial, e vinte e nove fontes integradas ao inventário.',
        'en': 'Part 4’s research arrives complete, six axes, delivered by the author outside the session, and goes through primary-source verification on its two most load-bearing findings: the CJEU’s SCHUFA case, which turns the gate rejection rate into legal exposure, and the 20,225-account Instagram case, which opens the piece. Four adjustments applied, the three SCHUFA sources separated, the near-miss patent source swapped for Heinrich’s triangle, the Kyndryl pair verified at the source, the Gartner figure not located and kept partial, and twenty-nine sources integrated into the inventory.',
        'es': 'La investigación de la parte 4 llega completa, seis ejes, entregada por el autor fuera de la sesión, y pasa por verificación de fuente primaria en sus dos hallazgos más cargados: el caso SCHUFA del TJUE, que convierte la tasa de rechazo en la puerta en exposición jurídica, y el caso de las 20.225 cuentas de Instagram, que abre la pieza. Cuatro ajustes aplicados, las tres fuentes del SCHUFA separadas, la fuente de patente del cuasi-accidente cambiada por el triángulo de Heinrich, el par de Kyndryl verificado en el origen, el número de Gartner no localizado y mantenido como parcial, y veintinueve fuentes integradas al inventario.',
    },
    'd972a35': {
        'pt': 'Eixo 0 adicionado ao dossiê da parte 4: uma observação de campo, um protótipo de terceiro mostrado informalmente ao autor. Uma correção recebida do próprio autor evitou um erro que teria sido grave, descrever o protótipo como fonte primária do projeto; o texto final trata a convergência como evidência independente, sem citar produto, empresa ou pessoa, e sem reprodução sem autorização escrita.',
        'en': 'Axis 0 added to Part 4’s dossier: a field observation, a third party’s prototype shown informally to the author. A correction from the author himself caught an error that would have been serious, describing the prototype as this project’s primary source; the final text treats the convergence as independent evidence instead, naming no product, company or person, and reproducing nothing without written authorisation.',
        'es': 'Eje 0 añadido al dosier de la parte 4: una observación de campo, un prototipo de un tercero mostrado informalmente al autor. Una corrección del propio autor evitó un error que habría sido grave, describir el prototipo como fuente primaria del proyecto; el texto final trata la convergencia como evidencia independiente, sin nombrar producto, empresa o persona, y sin reproducir nada sin autorización escrita.',
    },
}

MONTHS = {
    'pt': ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
    'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'es': ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
}


def fmt_time(iso, lang):
    # 2026-08-30T12:36:00-03:00 -> "30 ago, 12:36" (pt) etc.
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', iso)
    y, mo, d, h, mi = m.groups()
    return '%d %s, %s:%s' % (int(d), MONTHS[lang][int(mo) - 1], h, mi)


def fmt_int(n, lang):
    s = '{:,}'.format(int(n))
    if lang in ('pt', 'es'):
        s = s.replace(',', '.')
    return s


def fmt_millions(n, lang):
    v = n / 1_000_000
    s = ('%.1f' % v)
    if lang in ('pt', 'es'):
        s = s.replace('.', ',')
    return s


# ---------- SVG: grafico de crescimento, mesmo eixo X, sem eixo Y duplo ----------
def svg_growth_chart(marker_prefix, values, x_labels, y_fmt, caption, subcaption, viewbox_h=260):
    W, H = 700, viewbox_h
    left, right, top, bottom = 78, 652, 34, H - 66
    n = len(values)
    max_v = max(values) * 1.12 if max(values) > 0 else 1
    xs = [left + i * (right - left) / (n - 1) for i in range(n)]
    ys = [bottom - (v / max_v) * (bottom - top) for v in values]
    pts = ' '.join('%.1f,%.1f' % (x, y) for x, y in zip(xs, ys))

    parts = []
    parts.append('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (W, H, caption))
    # eixo
    parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9c7bf" stroke-width=".7"/>' % (left, bottom, right, bottom))
    # linha de nivel maximo, de referencia
    parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9c7bf" stroke-width=".5" stroke-dasharray="2,3"/>' % (left, top, right, top))
    parts.append('<text class="svg-sub" x="%d" y="%d" text-anchor="end">%s</text>' % (left - 6, top + 4, y_fmt(max_v)))
    parts.append('<text class="svg-sub" x="%d" y="%d" text-anchor="end">0</text>' % (left - 6, bottom + 4))
    # polilinha
    parts.append('<polyline points="%s" fill="none" stroke="#1b1b19" stroke-width="1"/>' % pts)
    # Value labels collide once there are enough milestones that neighbouring
    # points sit closer together than the label text is wide (seen for real at
    # 22 milestones: numbers overlapped into an unreadable smear). Space labels
    # out instead of dropping one on every point, always keeping the first and
    # last so the story's start and current state are never the ones omitted.
    max_labels = max(2, int((right - left) / 70))
    step = max(1, round((n - 1) / (max_labels - 1))) if n > 1 else 1
    labelled = set(range(0, n, step))
    labelled.add(0)
    # the forced last point can land right beside a regular-step point picked
    # up by range() above (seen for real: two labels touching at the tail,
    # "68,176 68,176"); drop anything crowding it before adding it back
    labelled = {i for i in labelled if i == n - 1 or (n - 1 - i) >= max(2, step // 2)}
    labelled.add(n - 1)
    # x-axis tick labels (M1, M2...) are short and safe at a tighter spacing,
    # but still thin them past the point where even "M99" would collide.
    x_max_labels = max(2, int((right - left) / 26))
    x_step = max(1, round((n - 1) / (x_max_labels - 1))) if n > 1 else 1
    x_labelled = set(range(0, n, x_step))
    x_labelled.add(0)
    x_labelled.add(n - 1)
    for i, (x, y, v) in enumerate(zip(xs, ys, values)):
        parts.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#1b1b19"/>' % (x, y))
        if i in labelled:
            label_y = y - 10 if y > top + 16 else y + 16
            parts.append('<text class="svg-sub" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (x, label_y, y_fmt(v)))
        if i in x_labelled:
            parts.append('<text class="svg-sub" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, H - 40, x_labels[i]))
    parts.append('<text class="svg-cap" x="%d" y="%d">%s</text>' % (left, H - 16, subcaption))
    parts.append('</svg>')
    return '\n'.join(parts)


def build_body(lang):
    T = TXT[lang]
    n = len(MS)
    x_labels = ['M%d' % (i + 1) for i in range(n)] + [T['now_short']]
    words_series = [m['words_published'] for m in MS] + [MS[-1]['words_published']]
    tok_series = [sum(m['tokens_cumulative'].values()) for m in MS]
    tok_series = tok_series + [tok_series[-1] + sum(REMAINING.values())]

    words_chart = svg_growth_chart(
        'w', words_series, x_labels,
        lambda v: fmt_int(v, lang),
        T['chart_words_alt'], T['chart_words_cap'])
    tok_chart = svg_growth_chart(
        't', tok_series, x_labels,
        lambda v: fmt_millions(v, lang) + T['million_suffix'],
        T['chart_tokens_alt'], T['chart_tokens_cap'])

    total_tokens_now = sum(MS[-1]['tokens_cumulative'].values()) + sum(REMAINING.values())
    total_words_now = MS[-1]['words_published']
    total_code_now = MS[-1]['code_lines']
    total_gov_now = MS[-1]['governance_lings'] if False else MS[-1]['governance_lines']

    kpi_rows = [
        (fmt_millions(total_tokens_now, lang) + T['million_suffix'], T['kpi_tokens']),
        (fmt_int(total_words_now, lang), T['kpi_words']),
        (fmt_int(total_code_now + total_gov_now, lang), T['kpi_lines']),
        (str(n), T['kpi_commits']),
    ]
    kpi_html = '\n'.join(
        '<div class="kpi"><span class="kpi-n">%s</span><span class="kpi-l">%s</span></div>' % (v, l)
        for v, l in kpi_rows)

    timeline_rows = []
    for i, m in enumerate(MS):
        desc = COMMIT_TXT[m['hash']][lang]
        bt = sum(m['tokens_bucket'].values())
        out_t = m['tokens_bucket']['output']
        timeline_rows.append(
            '<tr><td>M%d<br><span class="mono">%s</span></td>'
            '<td>%s<br><span class="mono">%s</span></td>'
            '<td>%s</td>'
            '<td>%s</td></tr>' % (
                i + 1, m['hash'],
                desc, fmt_time(m['timestamp'], lang),
                fmt_int(m['words_published'], lang),
                T['tokens_bucket_cell'] % (fmt_millions(bt, lang), fmt_int(out_t, lang))
            ))
    timeline_html = '\n'.join(timeline_rows)

    body = TEMPLATE[lang].format(
        kpi_html=kpi_html,
        words_chart=words_chart,
        tok_chart=tok_chart,
        timeline_html=timeline_html,
        remaining_millions=fmt_millions(sum(REMAINING.values()), lang),
    )
    return body


TXT = {
    'pt': {
        'now_short': 'agora',
        'million_suffix': ' mi',
        'chart_words_alt': 'Palavras publicadas por marco',
        'chart_words_cap': 'PALAVRAS PUBLICADAS, ACUMULADO POR MARCO',
        'chart_tokens_alt': 'Tokens consumidos por marco',
        'chart_tokens_cap': 'TOKENS CONSUMIDOS, ACUMULADO POR MARCO, MESMO EIXO X ACIMA',
        'kpi_tokens': 'tokens transacionados até agora',
        'kpi_words': 'palavras publicadas (PT+EN+ES)',
        'kpi_lines': 'linhas de script e documento de governança',
        'kpi_commits': 'marcos (commits) registrados',
        'tokens_bucket_cell': '%s mi<br><span class="mono">saída: %s</span>',
    },
    'en': {
        'now_short': 'now',
        'million_suffix': 'm',
        'chart_words_alt': 'Words published per milestone',
        'chart_words_cap': 'WORDS PUBLISHED, CUMULATIVE BY MILESTONE',
        'chart_tokens_alt': 'Tokens consumed per milestone',
        'chart_tokens_cap': 'TOKENS CONSUMED, CUMULATIVE BY MILESTONE, SAME X AXIS AS ABOVE',
        'kpi_tokens': 'tokens transacted so far',
        'kpi_words': 'words published (PT+EN+ES)',
        'kpi_lines': 'lines of script and governance document',
        'kpi_commits': 'milestones (commits) recorded',
        'tokens_bucket_cell': '%sm<br><span class="mono">output: %s</span>',
    },
    'es': {
        'now_short': 'ahora',
        'million_suffix': ' mi',
        'chart_words_alt': 'Palabras publicadas por hito',
        'chart_words_cap': 'PALABRAS PUBLICADAS, ACUMULADO POR HITO',
        'chart_tokens_alt': 'Tokens consumidos por hito',
        'chart_tokens_cap': 'TOKENS CONSUMIDOS, ACUMULADO POR HITO, MISMO EJE X DE ARRIBA',
        'kpi_tokens': 'tokens transaccionados hasta ahora',
        'kpi_words': 'palabras publicadas (PT+EN+ES)',
        'kpi_lines': 'líneas de script y documento de gobernanza',
        'kpi_commits': 'hitos (commits) registrados',
        'tokens_bucket_cell': '%s mi<br><span class="mono">salida: %s</span>',
    },
}

TEMPLATE = {}

TEMPLATE['pt'] = """<p class="eyebrow">Harness · Diário de bordo · Ao vivo</p>

<h1>Diário de bordo do projeto</h1>

<p class="deck">Este projeto argumenta que um harness deve produzir evidência sobre o próprio trabalho, não opinião. Esta página aplica esse argumento a si mesma: quanto texto foi publicado, quanto custou em tokens, marco a marco, com os números extraídos direto do histórico do git e do registro real de uso desta sessão.</p>

<p class="byline">Fernando Teco Sodré · Gerado automaticamente, ver metodologia abaixo · Companheiro das partes 1, 2, 3 e do guia compacto</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Os marcos abaixo são o histórico completo do repositório desde o primeiro commit, não uma amostra, já reunindo várias sessões de trabalho. Cada sessão nova que fizer commit vira um marco novo nesta mesma página.</p></div>

<nav class="toc">
  <p>Neste documento</p>
  <ol>
    <li><a href="#numeros">Números até agora</a></li>
    <li><a href="#evolucao">Evolução</a></li>
    <li><a href="#linha-do-tempo">Linha do tempo</a></li>
    <li><a href="#metodologia">Metodologia</a></li>
    <li><a href="#fontes">Fontes</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Números até agora</h2>

<p>Quatro números resumem o projeto neste instante. Todos recalculados a cada execução do gerador, nenhum digitado à mão.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>Dos tokens acima, cerca de {remaining_millions} mi ainda não fecharam marco: são desta sessão em andamento, ainda não commitados no momento em que este diário foi gerado.</p>

<h2 id="evolucao">2. Evolução</h2>

<p>Dois gráficos, não um só com dois eixos. É a mesma regra que a parte 2 deste projeto aplica a qualquer harness: não misture duas escalas arbitrárias na mesma régua. Os dois compartilham o eixo X, a ordem dos marcos, para que dê para comparar quando um acelerou em relação ao outro.</p>

<figure>
{words_chart}
<figcaption>Palavras publicadas nos três artigos (partes 1, 2 e guia compacto, somados). Cresce em degrau porque a maior parte do texto nasce dentro de um marco só, não gradualmente entre marcos.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transacionados, acumulado. Inclui leitura de cache, que cresce com o tamanho da sessão por natureza, não só com o trabalho novo. Ver a ressalva na metodologia.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Linha do tempo</h2>

<p>Um marco por commit. A coluna de tokens traz dois números: o total do intervalo, incluindo cache, e a saída pura, que é o sinal mais limpo para comparar esforço real entre marcos.</p>

<table class="wrap">
<thead><tr><th>Marco</th><th>O que aconteceu</th><th>Palavras publicadas</th><th>Tokens do intervalo</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Metodologia</h2>

<p>Fixa, documentada aqui, para repetir igual em toda atualização futura. Ver <code>build/generate_logbook_metrics.py</code> e <code>build/build_logbook.py</code> no repositório.</p>

<p><strong>Palavras.</strong> Contadas a partir do HTML publicado de cada commit (<code>git show &lt;hash&gt;:arquivo</code>), removendo marcação, bloco de código e SVG. Soma as partes 1, 2 e o guia compacto, nos idiomas que existiam naquele commit.</p>

<p><strong>Linhas.</strong> Contagem de linhas dos scripts de montagem em <code>build/</code> e dos documentos de governança (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, inventário de fontes), por commit.</p>

<p><strong>Tokens.</strong> Soma real do campo <code>usage</code> de cada mensagem do assistente no transcript <code>.jsonl</code> desta sessão, em <code>~/.claude/projects/&lt;projeto&gt;/</code>. Cada evento é atribuído ao commit imediatamente seguinte, por ordem cronológica, mesma técnica usada em outro projeto do autor para o mesmo fim.</p>

<div class="rule-box"><span class="lbl">Viés conhecido</span><p>Leitura de cache cresce com o tamanho acumulado da sessão, não com o esforço do marco específico. Para comparar esforço real entre marcos, use a saída (output), não o total bruto. O total bruto aparece porque é o que a fatura cobra, a saída aparece porque é o que ensina.</p></div>

<p>Uma sessão contínua cobre o projeto inteiro até aqui, então não há reconstrução retroativa a fazer, ao contrário de projetos mais antigos com dezenas de sessões. Cada marco futuro soma a esta mesma série.</p>

<h2 id="fontes">5. Fontes</h2>

<ol class="sources">
<li>Histórico completo de commits deste repositório. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas e usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script gerador dos números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Diário de bordo · Série Harness · Gerado automaticamente a partir do git e do registro de uso real da sessão, nunca editado à mão. Ver metodologia acima antes de citar qualquer número.</p>
</div>"""

TEMPLATE['en'] = """<p class="eyebrow">Harness · Project log · Live</p>

<h1>Project log</h1>

<p class="deck">This project argues that a harness should produce evidence about its own work, not opinion. This page applies that argument to itself: how much text got published, what it cost in tokens, milestone by milestone, with the numbers pulled straight from git history and this session's real usage record.</p>

<p class="byline">Fernando Teco Sodré · Generated automatically, see methodology below · Companion to parts 1, 2, 3 and the compact guide</p>

<div class="rule-box"><span class="lbl">Status</span><p>The milestones below are the repository's entire history since the first commit, not a sample, already spanning several working sessions. Every new session that commits becomes a new milestone on this same page.</p></div>

<nav class="toc">
  <p>In this document</p>
  <ol>
    <li><a href="#numeros">Numbers so far</a></li>
    <li><a href="#evolucao">Growth</a></li>
    <li><a href="#linha-do-tempo">Timeline</a></li>
    <li><a href="#metodologia">Methodology</a></li>
    <li><a href="#fontes">Sources</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Numbers so far</h2>

<p>Four numbers summarise the project at this instant. All recalculated on every run of the generator, none typed by hand.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>Of the tokens above, about {remaining_millions}m have not closed a milestone yet: they belong to this ongoing session, not committed yet at the moment this log was generated.</p>

<h2 id="evolucao">2. Growth</h2>

<p>Two charts, not one with two axes. It is the same rule this project's part 2 applies to any harness: do not mix two arbitrary scales on the same ruler. Both share the X axis, the order of milestones, so you can compare when one sped up relative to the other.</p>

<figure>
{words_chart}
<figcaption>Words published across the three articles (parts 1, 2 and the compact guide, summed). It grows in steps because most of the text is born within a single milestone, not gradually between milestones.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transacted, cumulative. Includes cache reads, which grow with session size by nature, not only with new work. See the caveat in the methodology.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Timeline</h2>

<p>One milestone per commit. The tokens column carries two numbers: the interval's total, including cache, and pure output, the cleanest signal for comparing real effort between milestones.</p>

<table class="wrap">
<thead><tr><th>Milestone</th><th>What happened</th><th>Words published</th><th>Interval tokens</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Methodology</h2>

<p>Fixed, documented here, to repeat identically on every future update. See <code>build/generate_logbook_metrics.py</code> and <code>build/build_logbook.py</code> in the repository.</p>

<p><strong>Words.</strong> Counted from the published HTML of each commit (<code>git show &lt;hash&gt;:file</code>), stripping markup, code blocks and SVG. Sums parts 1, 2 and the compact guide, in whichever languages existed at that commit.</p>

<p><strong>Lines.</strong> Line count of the build scripts under <code>build/</code> and the governance documents (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, source inventory), per commit.</p>

<p><strong>Tokens.</strong> Real sum of the <code>usage</code> field on every assistant message in this session's <code>.jsonl</code> transcript, under <code>~/.claude/projects/&lt;project&gt;/</code>. Each event is assigned to the immediately following commit, in chronological order, the same technique used on another of the author's projects for the same purpose.</p>

<div class="rule-box"><span class="lbl">Known bias</span><p>Cache reads grow with the session's accumulated size, not with the specific milestone's effort. To compare real effort between milestones, use output, not the raw total. The raw total shows up because it is what the invoice charges, output shows up because it is what teaches.</p></div>

<p>One continuous session covers the entire project so far, so there is no retroactive reconstruction to do, unlike older projects with dozens of sessions. Every future milestone adds to this same series.</p>

<h2 id="fontes">5. Sources</h2>

<ol class="sources">
<li>Full commit history of this repository. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Record of installed and used skills. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script that generates the numbers. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Project log · Harness series · Generated automatically from git and the session's real usage record, never edited by hand. See the methodology above before citing any number.</p>
</div>"""

TEMPLATE['es'] = """<p class="eyebrow">Harness · Diario de bordo · En vivo</p>

<h1>Diario de bordo del proyecto</h1>

<p class="deck">Este proyecto sostiene que un harness debe producir evidencia sobre su propio trabajo, no opinión. Esta página aplica ese argumento a sí misma: cuánto texto se publicó, cuánto costó en tokens, hito a hito, con los números extraídos directo del historial de git y del registro real de uso de esta sesión.</p>

<p class="byline">Fernando Teco Sodré · Generado automáticamente, ver metodología abajo · Compañero de las partes 1, 2, 3 y de la guía compacta</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Los hitos de abajo son el historial completo del repositorio desde el primer commit, no una muestra, ya reuniendo varias sesiones de trabajo. Cada sesión nueva que haga commit se vuelve un hito nuevo en esta misma página.</p></div>

<nav class="toc">
  <p>En este documento</p>
  <ol>
    <li><a href="#numeros">Números hasta ahora</a></li>
    <li><a href="#evolucao">Evolución</a></li>
    <li><a href="#linha-do-tempo">Línea de tiempo</a></li>
    <li><a href="#metodologia">Metodología</a></li>
    <li><a href="#fontes">Fuentes</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Números hasta ahora</h2>

<p>Cuatro números resumen el proyecto en este instante. Todos recalculados en cada ejecución del generador, ninguno escrito a mano.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>De los tokens de arriba, unos {remaining_millions} mi todavía no cerraron hito: son de esta sesión en curso, aún no confirmados en el momento en que se generó este diario.</p>

<h2 id="evolucao">2. Evolución</h2>

<p>Dos gráficos, no uno solo con dos ejes. Es la misma regla que la parte 2 de este proyecto aplica a cualquier harness: no mezcles dos escalas arbitrarias en la misma regla. Los dos comparten el eje X, el orden de los hitos, para poder comparar cuándo uno aceleró respecto al otro.</p>

<figure>
{words_chart}
<figcaption>Palabras publicadas en los tres artículos (partes 1, 2 y guía compacta, sumadas). Crece en escalón porque la mayor parte del texto nace dentro de un solo hito, no gradualmente entre hitos.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transaccionados, acumulado. Incluye lectura de caché, que crece con el tamaño de la sesión por naturaleza, no solo con el trabajo nuevo. Ver la salvedad en la metodología.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Línea de tiempo</h2>

<p>Un hito por commit. La columna de tokens trae dos números: el total del intervalo, incluyendo caché, y la salida pura, la señal más limpia para comparar el esfuerzo real entre hitos.</p>

<table class="wrap">
<thead><tr><th>Hito</th><th>Qué pasó</th><th>Palabras publicadas</th><th>Tokens del intervalo</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Metodología</h2>

<p>Fija, documentada aquí, para repetir igual en cada actualización futura. Ver <code>build/generate_logbook_metrics.py</code> y <code>build/build_logbook.py</code> en el repositorio.</p>

<p><strong>Palabras.</strong> Contadas a partir del HTML publicado de cada commit (<code>git show &lt;hash&gt;:archivo</code>), quitando marcado, bloque de código y SVG. Suma las partes 1, 2 y la guía compacta, en los idiomas que existían en ese commit.</p>

<p><strong>Líneas.</strong> Conteo de líneas de los scripts de montaje en <code>build/</code> y de los documentos de gobernanza (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, inventario de fuentes), por commit.</p>

<p><strong>Tokens.</strong> Suma real del campo <code>usage</code> de cada mensaje del asistente en el transcript <code>.jsonl</code> de esta sesión, en <code>~/.claude/projects/&lt;proyecto&gt;/</code>. Cada evento se asigna al commit inmediatamente siguiente, en orden cronológico, la misma técnica usada en otro proyecto del autor con el mismo fin.</p>

<div class="rule-box"><span class="lbl">Sesgo conocido</span><p>La lectura de caché crece con el tamaño acumulado de la sesión, no con el esfuerzo del hito específico. Para comparar el esfuerzo real entre hitos, usa la salida (output), no el total bruto. El total bruto aparece porque es lo que cobra la factura, la salida aparece porque es lo que enseña.</p></div>

<p>Una sesión continua cubre el proyecto entero hasta aquí, así que no hay reconstrucción retroactiva que hacer, a diferencia de proyectos más antiguos con decenas de sesiones. Cada hito futuro se suma a esta misma serie.</p>

<h2 id="fontes">5. Fuentes</h2>

<ol class="sources">
<li>Historial completo de commits de este repositorio. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas y usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script que genera los números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Diario de bordo · Serie Harness · Generado automáticamente a partir de git y del registro de uso real de la sesión, nunca editado a mano. Ver la metodología arriba antes de citar cualquier número.</p>
</div>"""


def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body


def main():
    p2 = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
    shell = p2[:p2.index('<div class="topbar">')]
    shell = shell.replace(
        '<title>Guides and sensors: how an agent learns to correct itself | Part 2</title>',
        '<title>Project log | Harness</title>')

    extra_css = """
.kpi-grid{display:flex;flex-wrap:wrap;gap:0;margin:20px 0 30px;border-top:.5pt solid var(--ink);border-bottom:.5pt solid var(--ink)}
.kpi{flex:1 1 22%;padding:16px 14px;border-right:.5pt solid var(--rule);display:flex;flex-direction:column;gap:4px}
.kpi:last-child{border-right:0}
.kpi-n{font-size:22px;font-weight:600;letter-spacing:-.01em}
.kpi-l{font-size:10.5px;color:var(--ink-faint);line-height:1.3}
.mono{font-family:"Consolas","Menlo",monospace;font-size:10.5px;color:var(--ink-faint)}
@media (max-width:640px){.kpi{flex:1 1 48%}}
"""
    shell = shell.replace('.eyebrow{', extra_css + '.eyebrow{')

    bar = """<div class="langbar">
<button type="button" data-lang="pt">PT</button>
<button type="button" class="on" data-lang="en">EN</button>
<button type="button" data-lang="es">ES</button>
</div>"""

    js = """<script>
(function(){
  var bar=document.querySelector('.langbar');
  var mains={pt:document.getElementById('doc-pt'),en:document.getElementById('doc-en'),es:document.getElementById('doc-es')};
  function set(l){
    for(var k in mains){mains[k].hidden=(k!==l);}
    bar.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.lang===l);});
    document.documentElement.lang=(l==='pt'?'pt-BR':l);
  }
  var h=location.hash.slice(1);
  var m=h.match(/^(en|es|pt)-/);
  var active='en';
  if(m){
    active=m[1];
    set(active);
    var target=document.getElementById(h);
    if(target){setTimeout(function(){target.scrollIntoView();},0);}
  }
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button[data-lang]');
    if(b){set(b.dataset.lang);try{location.hash='';}catch(e){}window.scrollTo(0,0);}
  });
  function dismissHint(){
    var d=document.querySelector('.lang-hint');
    if(d){d.remove();}
    try{localStorage.setItem('langHintDismissed','1');}catch(e){}
  }
  try{
    if(!m&&!localStorage.getItem('langHintDismissed')){
      var bl=(navigator.language||'').slice(0,2).toLowerCase();
      var msgs={pt:{text:'Esta p\\u00e1gina tamb\\u00e9m est\\u00e1 dispon\\u00edvel em portugu\\u00eas.',btn:'Ver em portugu\\u00eas'},es:{text:'Esta p\\u00e1gina tambi\\u00e9n est\\u00e1 disponible en espa\\u00f1ol.',btn:'Ver en espa\\u00f1ol'}};
      if(msgs[bl]&&bl!==active){
        var d=document.createElement('div');
        d.className='lang-hint';
        var span=document.createElement('span');
        span.textContent=msgs[bl].text;
        var right=document.createElement('span');
        var btn=document.createElement('button');
        btn.type='button';
        btn.textContent=msgs[bl].btn;
        btn.addEventListener('click',function(){dismissHint();set(bl);try{location.hash='';}catch(e){}window.scrollTo(0,0);});
        var x=document.createElement('button');
        x.type='button';
        x.className='x';
        x.setAttribute('aria-label','Close');
        x.textContent='\\u00d7';
        x.addEventListener('click',dismissHint);
        right.appendChild(btn);
        right.appendChild(x);
        d.appendChild(span);
        d.appendChild(right);
        bar.parentNode.insertBefore(d,bar.nextSibling);
      }
    }
  }catch(e){}
})();
</script>
</body>
</html>"""

    PT = scope(build_body('pt'), 'pt')
    EN = scope(build_body('en'), 'en')
    ES = scope(build_body('es'), 'es')

    doc = (shell + bar + '\n'
           + '<main class="page" id="doc-pt" hidden>\n' + PT + '\n</main>\n'
           + '<main class="page" id="doc-en">\n' + EN + '\n</main>\n'
           + '<main class="page" id="doc-es" hidden>\n' + ES + '\n</main>\n'
           + js)

    out_dir = os.path.join(ROOT, 'docs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'logbook.html')
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(doc)

    ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
    hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
    print('broken:', sorted(hr - ids))
    print('escrito em:', out_path)


if __name__ == '__main__':
    main()
