# -*- coding: utf-8 -*-
# Monta docs/diario-de-bordo.html trilingue a partir de
# docs/assets/diario-metrics.json (gerado por
# build/generate_diario_metrics.py). Reusa o envoltorio CSS e o
# JavaScript trilingue de harness-p2.html, mesmo padrao das outras
# pecas. Reexecutavel: os graficos e a linha do tempo sao gerados a
# partir do JSON, nunca escritos a mao.
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, 'docs', 'assets', 'diario-metrics.json'), encoding='utf-8') as fh:
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
        'pt': 'Trinta skills de terceiro instaladas para uso no projeto, auditadas antes de instalar. FERRAMENTAS.md criado como registro vivo do que é usado de fato.',
        'en': 'Thirty third-party skills installed for use on the project, audited before installing. FERRAMENTAS.md created as a living record of what is actually used.',
        'es': 'Treinta skills de terceros instaladas para uso en el proyecto, auditadas antes de instalar. FERRAMENTAS.md creado como registro vivo de lo que realmente se usa.',
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
    for i, (x, y, v) in enumerate(zip(xs, ys, values)):
        parts.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#1b1b19"/>' % (x, y))
        label_y = y - 10 if y > top + 16 else y + 16
        parts.append('<text class="svg-sub" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (x, label_y, y_fmt(v)))
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

<p class="byline">Fernando Teco Sodré · Gerado automaticamente, ver metodologia abaixo · Companheiro das partes 1, 2 e do guia compacto</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Um projeto jovem, uma sessão contínua até aqui. Os seis marcos abaixo são o histórico completo do repositório, não uma amostra. Cada sessão nova que fizer commit vira um marco novo nesta mesma página.</p></div>

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

<p>Fixa, documentada aqui, para repetir igual em toda atualização futura. Ver <code>build/generate_diario_metrics.py</code> e <code>build/build_diario.py</code> no repositório.</p>

<p><strong>Palavras.</strong> Contadas a partir do HTML publicado de cada commit (<code>git show &lt;hash&gt;:arquivo</code>), removendo marcação, bloco de código e SVG. Soma as partes 1, 2 e o guia compacto, nos idiomas que existiam naquele commit.</p>

<p><strong>Linhas.</strong> Contagem de linhas dos scripts de montagem em <code>build/</code> e dos documentos de governança (README, PADROES, ESTADO, PROXIMOS-PASSOS, FERRAMENTAS, inventário de fontes), por commit.</p>

<p><strong>Tokens.</strong> Soma real do campo <code>usage</code> de cada mensagem do assistente no transcript <code>.jsonl</code> desta sessão, em <code>~/.claude/projects/&lt;projeto&gt;/</code>. Cada evento é atribuído ao commit imediatamente seguinte, por ordem cronológica, mesma técnica usada em outro projeto do autor para o mesmo fim.</p>

<div class="rule-box"><span class="lbl">Viés conhecido</span><p>Leitura de cache cresce com o tamanho acumulado da sessão, não com o esforço do marco específico. Para comparar esforço real entre marcos, use a saída (output), não o total bruto. O total bruto aparece porque é o que a fatura cobra, a saída aparece porque é o que ensina.</p></div>

<p>Uma sessão contínua cobre o projeto inteiro até aqui, então não há reconstrução retroativa a fazer, ao contrário de projetos mais antigos com dezenas de sessões. Cada marco futuro soma a esta mesma série.</p>

<h2 id="fontes">5. Fontes</h2>

<ol class="sources">
<li>Histórico completo de commits deste repositório. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas e usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/FERRAMENTAS.md">FERRAMENTAS.md</a></li>
<li>Script gerador dos números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_diario_metrics.py">build/generate_diario_metrics.py</a></li>
</ol>

<div class="foot">
<p>Diário de bordo · Série Harness · Gerado automaticamente a partir do git e do registro de uso real da sessão, nunca editado à mão. Ver metodologia acima antes de citar qualquer número.</p>
</div>"""

TEMPLATE['en'] = """<p class="eyebrow">Harness · Project log · Live</p>

<h1>Project log</h1>

<p class="deck">This project argues that a harness should produce evidence about its own work, not opinion. This page applies that argument to itself: how much text got published, what it cost in tokens, milestone by milestone, with the numbers pulled straight from git history and this session's real usage record.</p>

<p class="byline">Fernando Teco Sodré · Generated automatically, see methodology below · Companion to parts 1, 2 and the compact guide</p>

<div class="rule-box"><span class="lbl">Status</span><p>A young project, one continuous session so far. The six milestones below are the repository's entire history, not a sample. Every new session that commits becomes a new milestone on this same page.</p></div>

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

<p>Fixed, documented here, to repeat identically on every future update. See <code>build/generate_diario_metrics.py</code> and <code>build/build_diario.py</code> in the repository.</p>

<p><strong>Words.</strong> Counted from the published HTML of each commit (<code>git show &lt;hash&gt;:file</code>), stripping markup, code blocks and SVG. Sums parts 1, 2 and the compact guide, in whichever languages existed at that commit.</p>

<p><strong>Lines.</strong> Line count of the build scripts under <code>build/</code> and the governance documents (README, PADROES, ESTADO, PROXIMOS-PASSOS, FERRAMENTAS, source inventory), per commit.</p>

<p><strong>Tokens.</strong> Real sum of the <code>usage</code> field on every assistant message in this session's <code>.jsonl</code> transcript, under <code>~/.claude/projects/&lt;project&gt;/</code>. Each event is assigned to the immediately following commit, in chronological order, the same technique used on another of the author's projects for the same purpose.</p>

<div class="rule-box"><span class="lbl">Known bias</span><p>Cache reads grow with the session's accumulated size, not with the specific milestone's effort. To compare real effort between milestones, use output, not the raw total. The raw total shows up because it is what the invoice charges, output shows up because it is what teaches.</p></div>

<p>One continuous session covers the entire project so far, so there is no retroactive reconstruction to do, unlike older projects with dozens of sessions. Every future milestone adds to this same series.</p>

<h2 id="fontes">5. Sources</h2>

<ol class="sources">
<li>Full commit history of this repository. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Record of installed and used skills. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/FERRAMENTAS.md">FERRAMENTAS.md</a></li>
<li>Script that generates the numbers. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_diario_metrics.py">build/generate_diario_metrics.py</a></li>
</ol>

<div class="foot">
<p>Project log · Harness series · Generated automatically from git and the session's real usage record, never edited by hand. See the methodology above before citing any number.</p>
</div>"""

TEMPLATE['es'] = """<p class="eyebrow">Harness · Diario de bordo · En vivo</p>

<h1>Diario de bordo del proyecto</h1>

<p class="deck">Este proyecto sostiene que un harness debe producir evidencia sobre su propio trabajo, no opinión. Esta página aplica ese argumento a sí misma: cuánto texto se publicó, cuánto costó en tokens, hito a hito, con los números extraídos directo del historial de git y del registro real de uso de esta sesión.</p>

<p class="byline">Fernando Teco Sodré · Generado automáticamente, ver metodología abajo · Compañero de las partes 1, 2 y de la guía compacta</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Un proyecto joven, una sesión continua hasta ahora. Los seis hitos de abajo son el historial completo del repositorio, no una muestra. Cada sesión nueva que haga commit se vuelve un hito nuevo en esta misma página.</p></div>

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

<p>Fija, documentada aquí, para repetir igual en cada actualización futura. Ver <code>build/generate_diario_metrics.py</code> y <code>build/build_diario.py</code> en el repositorio.</p>

<p><strong>Palabras.</strong> Contadas a partir del HTML publicado de cada commit (<code>git show &lt;hash&gt;:archivo</code>), quitando marcado, bloque de código y SVG. Suma las partes 1, 2 y la guía compacta, en los idiomas que existían en ese commit.</p>

<p><strong>Líneas.</strong> Conteo de líneas de los scripts de montaje en <code>build/</code> y de los documentos de gobernanza (README, PADROES, ESTADO, PROXIMOS-PASSOS, FERRAMENTAS, inventario de fuentes), por commit.</p>

<p><strong>Tokens.</strong> Suma real del campo <code>usage</code> de cada mensaje del asistente en el transcript <code>.jsonl</code> de esta sesión, en <code>~/.claude/projects/&lt;proyecto&gt;/</code>. Cada evento se asigna al commit inmediatamente siguiente, en orden cronológico, la misma técnica usada en otro proyecto del autor con el mismo fin.</p>

<div class="rule-box"><span class="lbl">Sesgo conocido</span><p>La lectura de caché crece con el tamaño acumulado de la sesión, no con el esfuerzo del hito específico. Para comparar el esfuerzo real entre hitos, usa la salida (output), no el total bruto. El total bruto aparece porque es lo que cobra la factura, la salida aparece porque es lo que enseña.</p></div>

<p>Una sesión continua cubre el proyecto entero hasta aquí, así que no hay reconstrucción retroactiva que hacer, a diferencia de proyectos más antiguos con decenas de sesiones. Cada hito futuro se suma a esta misma serie.</p>

<h2 id="fontes">5. Fuentes</h2>

<ol class="sources">
<li>Historial completo de commits de este repositorio. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas y usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/FERRAMENTAS.md">FERRAMENTAS.md</a></li>
<li>Script que genera los números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_diario_metrics.py">build/generate_diario_metrics.py</a></li>
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
    shell = p2[:p2.index('<div class="langbar">')]
    shell = shell.replace(
        '<title>Guias e sensores: como um agente aprende a se corrigir | Parte 2</title>',
        '<title>Diário de bordo | Harness</title>')

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
<button type="button" class="on" data-lang="pt">PT</button>
<button type="button" data-lang="en">EN</button>
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
  if(m){
    set(m[1]);
    var target=document.getElementById(h);
    if(target){setTimeout(function(){target.scrollIntoView();},0);}
  }
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button[data-lang]');
    if(b){set(b.dataset.lang);try{location.hash='';}catch(e){}window.scrollTo(0,0);}
  });
})();
</script>
</body>
</html>"""

    PT = scope(build_body('pt'), 'pt')
    EN = scope(build_body('en'), 'en')
    ES = scope(build_body('es'), 'es')

    doc = (shell + bar + '\n'
           + '<main class="page" id="doc-pt">\n' + PT + '\n</main>\n'
           + '<main class="page" id="doc-en" hidden>\n' + EN + '\n</main>\n'
           + '<main class="page" id="doc-es" hidden>\n' + ES + '\n</main>\n'
           + js)

    out_dir = os.path.join(ROOT, 'docs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'diario-de-bordo.html')
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(doc)

    ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
    hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
    print('broken:', sorted(hr - ids))
    print('escrito em:', out_path)


if __name__ == '__main__':
    main()
