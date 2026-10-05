# -*- coding: utf-8 -*-
# Pedacos compartilhados pelos scripts de montagem (build_p1.py a
# build_p4.py, build_glossary.py, build_sources.py, build_toolkit.py,
# build_playbook.py, build_logbook.py). Existe para que uma regra de
# montagem mude num lugar so, e nao em nove copias.
import re

LANG_ATTR = {'pt': 'pt-BR', 'en': 'en-GB', 'es': 'es'}

# Link do corpo para outra pagina da serie, sem fragmento. Sem fragmento
# de lingua, a pagina de destino abre na aba EN, mesmo para quem vem do
# PT ou do ES (item TR.01 da especificacao de 5 de outubro de 2026).
PAGE_LINK = re.compile(r'href="((?:\.\./)?(?:harness-[a-z0-9]+|docs/logbook|logbook)\.html)"')


def finish(body, lang):
    """Acrescenta o fragmento de lingua aos links entre paginas e o id de topo.

    Idempotente: o PT das partes 1 e 2 e extraido da propria pagina
    publicada, entao ja chega aqui com as duas coisas feitas.
    """
    body = PAGE_LINK.sub(lambda m: 'href="%s#%s-top"' % (m.group(1), lang), body)
    if 'id="%s-top"' % lang not in body:
        body = '<span id="%s-top"></span>\n' % lang + body
    return body


def main_block(lang, body, hidden=False):
    """O <main> de uma lingua, com lang no atributo e o corpo ja acabado."""
    return '<main class="page" id="doc-%s"%s lang="%s">\n%s\n</main>\n' % (
        lang, ' hidden' if hidden else '', LANG_ATTR[lang], finish(body, lang))


def main_open_re(lang):
    """Regex que acha a abertura do <main> de uma lingua, com ou sem atributos extras."""
    return re.compile(r'<main class="page" id="doc-%s"[^>]*>' % lang)


# ---------------------------------------------------------------------
# Metadados de pagina e datas geradas (itens PG.01, PG.02, BLD.06 e
# TR.08 da especificacao de 5 de outubro de 2026). Chamado por cada
# build_*.py logo antes de gravar a pagina, para que a regra viva num
# lugar so. Idempotente: o bloco de metadados e delimitado por marcas e
# substituido, e as assinaturas sao reescritas, nunca acrescentadas.
# ---------------------------------------------------------------------
import os
import subprocess
import datetime
import html as _html

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_URL = 'https://tecosodreaboutdigital.github.io/harness-medir/'
OG_IMAGE = 'diagrams/part4/d6-three-layers.png'
WPM = 238  # palavras por minuto de leitura silenciosa de um adulto

# arquivo publicado -> (prefixo dos corpos em build/, descricao em ingles)
PAGE_META = {
    'harness-p1.html': ('p1', 'A freight-invoice automation that worked in the demo and failed in production, and why the environment around an AI model is worth more than the model: the harness, the MEDIR cycle and four bands of maturity.'),
    'harness-p2.html': ('p2', 'How an AI agent learns to correct itself: guides and sensors, the five MEDIR steps in practice, the environments they run in, and the risks specific to this layer.'),
    'harness-p3.html': ('p3', 'The separation of powers for AI agents: who proposes, who authorises, who executes and who keeps the record, with the rule of two, identity, prompt injection, the audit record and accountability.'),
    'harness-p4.html': ('p4', 'The agent office: how many agents a company has, who owns each, which autonomy tier each has earned and which still pay for themselves. Life cycle, roles, indicators and why it cannot be bought as a product.'),
    'harness-toolkit.html': ('toolkit', 'The compact guide to the tools and skills behind the MEDIR cycle, each with a verification date, plus the checklist to run before installing anything.'),
    'harness-glossary.html': ('glossary', 'Every term the Harness series uses, defined once, in English, Portuguese and Spanish.'),
    'harness-sources.html': ('sources', 'Every citation the Harness series uses, with what each source does and does not support and the date it was checked.'),
    'harness-playbook.html': ('playbook', 'Eight operational templates derived from the four parts: receipt, risk matrix, rollout, agent registry, skill, starter guides and tier diagnostic.'),
    'docs/logbook.html': (None, 'Words published, tokens consumed and cost recorded per milestone of the Harness project, generated from git and the real usage of its sessions, subagents included.'),
}

_FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E"
            "%3Cpolyline points='1,13 5,13 5,9 9,9 9,4 15,4' fill='none' stroke='%235c6b52' stroke-width='1.6'/%3E%3C/svg%3E")

MONTHS = {
    'en': ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
    'pt': ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
    'es': ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'],
}
_MONTH_RX = {
    'en': re.compile(r'\b(%s) (20\d\d)' % '|'.join(MONTHS['en'])),
    'pt': re.compile(r'\b(%s) de (20\d\d)' % '|'.join(m + '|' + m.capitalize() for m in MONTHS['pt'])),
    'es': re.compile(r'\b(%s) de (20\d\d)' % '|'.join(m + '|' + m.capitalize() for m in MONTHS['es'])),
}
_READ_RX = {
    'en': (re.compile(r'\d+[ -]minute read'), '%d minute read'),
    'pt': (re.compile(r'Leitura de \d+ minutos'), 'Leitura de %d minutos'),
    'es': (re.compile(r'Lectura de \d+ minutos'), 'Lectura de %d minutos'),
}


def _git(*args):
    try:
        return subprocess.run(['git'] + list(args), cwd=_ROOT, capture_output=True, text=True,
                              encoding='utf-8', timeout=20).stdout.strip()
    except Exception:
        return ''


def source_date(prefix):
    """Data da ultima alteracao dos corpos de uma pagina: a do ultimo commit,
    ou a de hoje se algum corpo tem mudanca ainda nao commitada."""
    if not prefix:
        return None
    spec = 'build/body_%s_*.html' % prefix
    if _git('status', '--porcelain', '--', spec):
        return datetime.date.today()
    d = _git('log', '-1', '--format=%cs', '--', spec)
    try:
        return datetime.date.fromisoformat(d)
    except ValueError:
        return None


def _words(main_html):
    t = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', main_html, flags=re.S)
    return len(re.sub(r'<[^>]+>', ' ', t).split())


def _stamp(doc, prefix):
    date = source_date(prefix)

    def per_main(m):
        lang, block = m.group(1), m.group(0)
        by = re.search(r'<p class="byline">(.*?)</p>', block, re.S)
        if not by:
            return block
        txt = by.group(1)
        if date:
            def mo(mm):
                name = MONTHS[lang][date.month - 1]
                if mm.group(1)[0].isupper():
                    name = name.capitalize()
                sep = ' ' if lang == 'en' else ' de '
                return name + sep + str(date.year)
            txt = _MONTH_RX[lang].sub(mo, txt, count=1)
        rx, fmt = _READ_RX[lang]
        if rx.search(txt):
            n = max(1, round(_words(block) / WPM))
            txt = rx.sub(lambda _m: fmt % n, txt, count=1)
        return block.replace(by.group(0), '<p class="byline">%s</p>' % txt, 1)

    return re.sub(r'<main class="page" id="doc-(en|pt|es)".*?</main>', per_main, doc, flags=re.S)


def _meta(filename, doc, desc):
    t = re.search(r'<title>(.*?)</title>', doc, re.S)
    title = _html.unescape(t.group(1)).strip() if t else 'Harness series'
    url = BASE_URL + filename
    e = lambda s: _html.escape(s, quote=True)
    img = BASE_URL + (OG_IMAGE if filename != 'docs/logbook.html' else 'docs/assets/logbook-words-published.png')
    lines = [
        '<!-- site-meta -->',
        '<meta name="description" content="%s">' % e(desc),
        '<link rel="canonical" href="%s">' % url,
        '<link rel="alternate" hreflang="x-default" href="%s">' % url,
        '<link rel="icon" href="%s">' % _FAVICON,
        '<meta property="og:type" content="article">',
        '<meta property="og:site_name" content="The Harness series">',
        '<meta property="og:title" content="%s">' % e(title),
        '<meta property="og:description" content="%s">' % e(desc),
        '<meta property="og:url" content="%s">' % url,
        '<meta property="og:image" content="%s">' % img,
        '<meta name="twitter:card" content="summary_large_image">',
        '<meta name="twitter:title" content="%s">' % e(title),
        '<meta name="twitter:description" content="%s">' % e(desc),
        '<meta name="twitter:image" content="%s">' % img,
        '<!-- /site-meta -->',
    ]
    return '\n'.join(lines)


def finish_page(doc, filename):
    """Metadados do <head> e assinaturas geradas, para a pagina `filename`."""
    prefix, desc = PAGE_META[filename]
    doc = re.sub(r'<!-- site-meta -->.*?<!-- /site-meta -->\n?', '', doc, flags=re.S)
    meta = _meta(filename, doc, desc)
    doc = re.sub(r'(</title>)', lambda m: m.group(1) + '\n' + meta, doc, count=1)
    return _stamp(doc, prefix)
