# -*- coding: utf-8 -*-
# Verificador unico do repositorio (item BLD.01 da especificacao de
# 5 de outubro de 2026). Roda, nesta ordem, as checagens que ate aqui
# existiam soltas ou so como regra escrita no STANDARDS.md:
#
#   dash       travessao e en dash em arquivo publicado
#   glossary   ordem alfabetica do glossario (check_glossary_order.py)
#   readme     alt text dos graficos do README (check_readme_snapshot.py)
#   manifest   toolkit.json em dia (generate_toolkit_manifest.py --check)
#   links      ancoras internas, links entre paginas e fragmento de lingua
#   parts      consistencia entre partes ("Part N of 4", listas de partes)
#   facts      fatos repetidos entre glossario e partes
#   diacritics palavras PT e ES sem acento onde o dicionario exige
#   spelling   ortografia americana em EN (o projeto usa a britanica)
#   parity     contagem de secoes, tabelas, SVG e tooltips entre linguas
#
# Cada achado diz arquivo, linha, trecho e a correcao esperada, o mesmo
# padrao do "sensor que ensina" da Parte 2.
#
# Catraca (ratchet): o repositorio ja tinha achados antes deste script
# existir, e a especificacao os corrige em ondas. Eles ficam registrados
# em build/check_known.json e NAO derrubam a execucao; qualquer achado
# fora dessa lista derruba. Quando um achado e corrigido, o script avisa
# que a linha da lista ficou velha, e `--write-baseline` a remove. A
# lista so deve encolher.
#
# Uso:
#   python build/check_all.py                  tudo, com a catraca
#   python build/check_all.py --only dash      uma checagem
#   python build/check_all.py --strict         ignora a catraca
#   python build/check_all.py --write-baseline regrava build/check_known.json
# Sai com 1 se houver achado novo (ou, com --strict, qualquer achado).
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KNOWN = os.path.join(ROOT, 'build', 'check_known.json')

try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

EM, EN_ = '—', '–'

# Trechos que carregam travessao por escolha do editor original, nao do
# projeto. Versionado aqui, uma linha por excecao, com o motivo.
DASH_EXCEPTIONS = [
    # Titulo publicado do Statement of Position do IIA, citado literalmente.
    'Statement of Position',
]

PAGES = ['harness-p1.html', 'harness-p2.html', 'harness-p3.html', 'harness-p4.html',
         'harness-playbook.html', 'harness-toolkit.html', 'harness-glossary.html',
         'harness-sources.html', 'docs/logbook.html']
LANGS = ('en', 'pt', 'es')

MAIN_OPEN = re.compile(r'<main\b[^>]*\bid="doc-(en|pt|es)"')


def rel(path):
    return os.path.relpath(path, ROOT).replace(os.sep, '/')


def read_lines(path):
    with open(path, encoding='utf-8') as f:
        return f.read().split('\n')


def lang_of_lines(lines):
    """Para cada linha, a lingua do <main> que a contem (ou None)."""
    out, cur = [], None
    for ln in lines:
        m = MAIN_OPEN.search(ln)
        if m:
            cur = m.group(1)
        out.append(cur)
        if '</main>' in ln:
            cur = None
    return out


def body_lang(path):
    m = re.search(r'_(en|pt|es)\.html$', path)
    return m.group(1) if m else None


def published_files():
    return [os.path.join(ROOT, p) for p in PAGES if os.path.exists(os.path.join(ROOT, p))]


def body_files():
    return sorted(glob.glob(os.path.join(ROOT, 'build', 'body_*.html')))


def md_files():
    out = glob.glob(os.path.join(ROOT, '*.md'))
    out += glob.glob(os.path.join(ROOT, 'playbook', '*.md'))
    out += glob.glob(os.path.join(ROOT, 'sources', '*.md'))
    out += [os.path.join(ROOT, 'llms.txt')]
    return sorted(p for p in out if os.path.exists(p))


# Cada achado: (check, arquivo, linha, trecho, correcao)
def F(check, path, line, snippet, fix):
    return (check, rel(path) if os.path.isabs(path) else path, line, snippet.strip()[:140], fix)


# ---------------------------------------------------------------- dash
def check_dash():
    out = []
    for path in published_files() + body_files() + md_files():
        for i, ln in enumerate(read_lines(path), 1):
            if (EM in ln or EN_ in ln) and not any(x in ln for x in DASH_EXCEPTIONS):
                ch = 'travessao' if EM in ln else 'en dash'
                k = ln.index(EM if EM in ln else EN_)
                out.append(F('dash', path, i, ln[max(0, k - 50):k + 50],
                             f'{ch}: trocar por virgula, dois pontos, parenteses ou ponto final'))
    return out


# ---------------------------------------------------- subprocess checks
def run_script(check, script, args, fix):
    p = subprocess.run([sys.executable, os.path.join(ROOT, 'build', script)] + args,
                       capture_output=True, text=True, encoding='utf-8', cwd=ROOT)
    if p.returncode == 0:
        return []
    msg = (p.stdout + p.stderr).strip().replace('\n', ' | ')
    return [F(check, 'build/' + script, 0, msg, fix)]


def check_glossary():
    return run_script('glossary', 'check_glossary_order.py', [],
                      'mover a entrada para a posicao alfabetica em build/body_glossary_*.html')


def check_readme():
    return run_script('readme', 'check_readme_snapshot.py', [],
                      'atualizar o alt text dos graficos nos tres README')


def check_manifest():
    return run_script('manifest', 'generate_toolkit_manifest.py', ['--check'],
                      'rodar python build/generate_toolkit_manifest.py')


# --------------------------------------------------------------- links
HREF = re.compile(r'href="([^"]*)"')
ID = re.compile(r'\bid="([^"]+)"')


def ids_of(path, _cache={}):
    if path not in _cache:
        with open(path, encoding='utf-8') as f:
            _cache[path] = set(ID.findall(f.read()))
    return _cache[path]


def check_links():
    out = []
    for path in published_files():
        lines = read_lines(path)
        langs = lang_of_lines(lines)
        mine = ids_of(path)
        for i, (ln, lg) in enumerate(zip(lines, langs), 1):
            for href in HREF.findall(ln):
                if href.startswith('#') and len(href) > 1:
                    if href[1:] not in mine:
                        out.append(F('links', path, i, href, 'ancora sem id correspondente na pagina'))
                    continue
                m = re.match(r'(harness-[a-z0-9]+\.html|docs/logbook\.html|\.\./harness-[a-z0-9]+\.html)(#(.*))?$', href)
                if not m:
                    continue
                target = os.path.normpath(os.path.join(os.path.dirname(path), m.group(1)))
                frag = m.group(3)
                if not os.path.exists(target):
                    out.append(F('links', path, i, href, 'pagina de destino nao existe'))
                elif frag:
                    if frag.endswith('-'):
                        continue  # prefixo de lingua que o JavaScript completa (barra superior)
                    if frag not in ids_of(target):
                        out.append(F('links', path, i, href, 'ancora sem id no arquivo de destino'))
                    elif lg and not frag.startswith(lg + '-'):
                        out.append(F('links', path, i, href, f'fragmento de outra lingua dentro do bloco {lg.upper()}'))
                elif lg and lg != 'en':
                    out.append(F('links', path, i, href,
                                 f'link entre paginas sem fragmento abre a aba EN para o leitor {lg.upper()}; usar #{lg}-top'))
    return out


# --------------------------------------------------------------- parts
PARTS_BAD = [
    (re.compile(r'\b(?:Part|Parte|Pieza)\s+[1-4]\s+(?:of|de)\s+(?:3|three|tres|três)\b', re.I),
     'a serie tem quatro partes: "Part N of 4"'),
    (re.compile(r'\bparts?\s+2\s+and\s+3\b|\bpartes?\s+2\s+(?:e|y)\s+3\b', re.I),
     'lista de partes sem a Parte 4: "parts 2 to 4"'),
]


def check_parts():
    out = []
    for path in published_files() + body_files():
        lines = read_lines(path)
        langs = lang_of_lines(lines) if path.endswith('.html') and 'body_' not in path else [None] * len(lines)
        for i, ln in enumerate(lines, 1):
            for rx, fix in PARTS_BAD:
                m = rx.search(ln)
                if m:
                    out.append(F('parts', path, i, ln[max(0, m.start() - 40):m.end() + 40], fix))
    return out


# --------------------------------------------------------------- facts
FACTS = [
    (re.compile(r'primary publication not located|publica[cç][aã]o prim[aá]ria n[aã]o localizada|publicaci[oó]n primaria no localizada', re.I),
     'a fonte primaria da regra de dois foi localizada em 31 de agosto de 2026 (Meta, 31 de outubro de 2025)'),
    (re.compile(r'(?:revised|revisado|revisada|revisto)\s+2020\s+(?:and|e|y)\s+2023|2020\s+(?:e|y|and)\s+2023', re.I),
     'Three Lines Model: "adopted 2013, revised 2020, restated July 2026" (a data de 2023 nao foi confirmada)'),
]


def check_facts():
    out = []
    for path in published_files() + body_files():
        for i, ln in enumerate(read_lines(path), 1):
            for rx, fix in FACTS:
                m = rx.search(ln)
                if m:
                    out.append(F('facts', path, i, ln[max(0, m.start() - 40):m.end() + 40], fix))
    return out


# ---------------------------------------------------------- diacritics
# Formas que, sem acento, nao sao palavra valida na lingua indicada.
NO_ACCENT = {
    'pt': r'execucao|execucoes|orfa|orfas|orfao|nao|voce|voces|informacao|informacoes|decisao|decisoes|'
          r'verificacao|verificacoes|autorizacao|producao|tambem|acao|acoes|politica|politicas|'
          r'organizacao|configuracao|governanca|responsavel|responsaveis|memoria|obrigatorio|'
          r'avaliacao|operacao|operacoes|descricao|conclusao|excecao|excecoes|ate|codigo',
    'es': r'ejecucion|disenar|redisenar|diseno|informacion|decision|verificacion|'
          r'autorizacion|produccion|tambien|accion|politica|politicas|organizacion|'
          r'configuracion|gobernanza|responsable?s?|memoria|obligatorio|evaluacion|operacion|descripcion|'
          r'conclusion|excepcion|codigo|huerfanas?|huerfanos?|sesion|razon',
}
NO_ACCENT_RX = {k: re.compile(r'\b(' + v + r')\b', re.I) for k, v in NO_ACCENT.items()}
# Palavras que existem sem acento com outro sentido: nao entram na lista
# acima de proposito (pt "ate", es "responsable" e "memoria" sao validas).
NO_ACCENT_RX['pt'] = re.compile(NO_ACCENT_RX['pt'].pattern.replace('|ate|', '|').replace('|memoria|', '|'), re.I)
NO_ACCENT_RX['es'] = re.compile(NO_ACCENT_RX['es'].pattern.replace('|responsable?s?|', '|').replace('|memoria|', '|'), re.I)
ATTR_STRIP = re.compile(r'\b(?:href|id|class|src|for|name|data-[a-z-]*key|viewBox|d|points|style)="[^"]*"')
TAG_STRIP = re.compile(r'<(?!/?\w)')


def check_diacritics():
    out = []
    targets = [(p, None) for p in published_files()] + [(p, body_lang(p)) for p in body_files()]
    for path, fixed in targets:
        lines = read_lines(path)
        langs = lang_of_lines(lines) if fixed is None else [fixed] * len(lines)
        for i, (ln, lg) in enumerate(zip(lines, langs), 1):
            if lg not in ('pt', 'es'):
                continue
            clean = ATTR_STRIP.sub('', ln)
            for m in NO_ACCENT_RX[lg].finditer(clean):
                out.append(F('diacritics', path, i, clean[max(0, m.start() - 40):m.end() + 40],
                             f'"{m.group(1)}" sem acento em {lg.upper()}: restaurar a grafia acentuada'))
    return out


# ------------------------------------------------------------ spelling
US = re.compile(r'\b(authoriz\w*|organiz\w*|recogniz\w*|summariz\w*|minimiz\w*|prioritiz\w*|behavior\w*|'
                r'analyz\w*|centraliz\w*|standardiz\w*|normaliz\w*|utiliz\w*|categoriz\w*|optimiz\w*|'
                r'customiz\w*|initializ\w*|favor\w*|labor\b|catalog\b|license\b)', re.I)
# "license" e "organization" sao grafias aceitas em partes do ingles
# britanico (Oxford) e nomes proprios; o que e nome proprio entra na
# lista de conhecidos, nao aqui.
# Nomes proprios de ferramenta que carregam a grafia americana.
PROPER_NOUNS = {'analyzer'}
SKIP_BLOCK = re.compile(r'<(style|script)\b.*?</\1>', re.S)


def check_spelling():
    out = []
    targets = [(p, None) for p in published_files()] + [(p, body_lang(p)) for p in body_files()]
    for path, fixed in targets:
        text = open(path, encoding='utf-8').read()
        text = SKIP_BLOCK.sub(lambda m: '\n' * m.group(0).count('\n'), text)
        lines = text.split('\n')
        langs = lang_of_lines(lines) if fixed is None else [fixed] * len(lines)
        for i, (ln, lg) in enumerate(zip(lines, langs), 1):
            if lg != 'en':
                continue
            clean = ATTR_STRIP.sub('', ln)
            for m in US.finditer(clean):
                if m.group(1).lower() in PROPER_NOUNS:
                    continue
                out.append(F('spelling', path, i, clean[max(0, m.start() - 40):m.end() + 40],
                             f'"{m.group(1)}": ortografia britanica (-ise, -our, -ogue, licence)'))
    return out


# -------------------------------------------------------------- parity
METRICS = {'h2': r'<h2\b', 'h3': r'<h3\b', 'table': r'<table\b', 'svg': r'<svg\b', 'tooltips': r'data-tip="'}


def check_parity():
    out = []
    for path in published_files():
        lines = read_lines(path)
        langs = lang_of_lines(lines)
        counts = {lg: {k: 0 for k in METRICS} for lg in LANGS}
        for ln, lg in zip(lines, langs):
            if lg in counts:
                for k, rx in METRICS.items():
                    counts[lg][k] += len(re.findall(rx, ln))
        if not any(any(v.values()) for v in counts.values()):
            continue
        for k in METRICS:
            vals = {lg: counts[lg][k] for lg in LANGS}
            if len(set(vals.values())) > 1:
                out.append(F('parity', path, 0, f'{k}: ' + ', '.join(f'{lg.upper()} {n}' for lg, n in vals.items()),
                             'as tres linguas devem ter a mesma contagem; conferir a traducao'))
    return out


CHECKS = [
    ('dash', check_dash), ('glossary', check_glossary), ('readme', check_readme),
    ('manifest', check_manifest), ('links', check_links), ('parts', check_parts),
    ('facts', check_facts), ('diacritics', check_diacritics), ('spelling', check_spelling),
    ('parity', check_parity),
]


def key(f):
    check, path, _line, snippet, _fix = f
    h = hashlib.sha1(re.sub(r'\s+', ' ', snippet).encode('utf-8')).hexdigest()[:12]
    return f'{check}|{path}|{h}'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--only', choices=[n for n, _ in CHECKS])
    ap.add_argument('--strict', action='store_true')
    ap.add_argument('--write-baseline', action='store_true')
    ap.add_argument('--verbose', '-v', action='store_true', help='lista tambem os achados conhecidos')
    args = ap.parse_args()

    known = {}
    if os.path.exists(KNOWN):
        known = json.load(open(KNOWN, encoding='utf-8'))['known']

    findings = []
    for name, fn in CHECKS:
        if args.only and name != args.only:
            continue
        res = fn()
        print(f'{name:11s} {len(res)} achado(s)')
        findings += res

    if args.write_baseline:
        if args.only:
            sys.exit('--write-baseline exige rodar todas as checagens (sem --only)')
        data = {'_': 'Achados anteriores a build/check_all.py. So deve encolher; ver o cabecalho do script.',
                'known': {key(f): f'{f[1]}:{f[2]} {f[3]}' for f in findings}}
        with open(KNOWN, 'w', encoding='utf-8', newline='\n') as fh:
            json.dump(data, fh, ensure_ascii=False, indent=1, sort_keys=True)
            fh.write('\n')
        print(f'baseline gravado: {len(findings)} achado(s) em {rel(KNOWN)}')
        return 0

    seen, new = set(), []
    for f in findings:
        k = key(f)
        seen.add(k)
        if args.strict or k not in known:
            new.append(f)
    stale = [k for k in known if k not in seen and (not args.only or k.startswith(args.only + '|'))]

    shown = findings if args.verbose else new
    for check, path, line, snippet, fix in shown:
        tag = '' if (args.strict or key((check, path, line, snippet, fix)) not in known) else ' (conhecido)'
        loc = f'{path}:{line}' if line else path
        print(f'  [{check}] {loc}{tag}\n      {snippet}\n      -> {fix}')
    if stale:
        print(f'{len(stale)} achado(s) conhecido(s) foram corrigidos; rode --write-baseline para tirar da lista.')
    print(f'{len(findings)} achado(s) no total, {len(findings) - len(new) if not args.strict else 0} conhecido(s), {len(new)} novo(s).')
    return 1 if new else 0


if __name__ == '__main__':
    sys.exit(main())
