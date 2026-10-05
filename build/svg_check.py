# -*- coding: utf-8 -*-
# Confere que o SVG inline de cada lingua tem a mesma geometria do SVG autonomo
# em diagrams/ (item DG.08 da especificacao de 5 de outubro de 2026). O texto
# muda por lingua; tudo o mais (formas, posicoes, tracos, marcadores) nao pode.
# Usado por build/check_all.py; tambem roda sozinho: python build/svg_check.py
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LANGS = ('en', 'pt', 'es')
# arquivo autonomo, prefixo de id no inline, corpo que o contem
DIAGRAMS = {
    'D1': ('diagrams/part3/d1-separation-of-powers.svg', 'p3d1', 'body_p3_{lang}.html'),
    'D2': ('diagrams/part3/d2-concentration.svg', 'p3d2', 'body_p3_{lang}.html'),
    'D3': ('diagrams/part3/d3-order-inside-the-data.svg', 'p3d3', 'body_p3_{lang}.html'),
    'D4': ('diagrams/part3/d4-rule-of-two.svg', 'p3d4', 'body_p3_{lang}.html'),
    'D5': ('diagrams/part3/d5-life-of-an-action.svg', 'p3d5', 'body_p3_{lang}.html'),
    'D6': ('diagrams/part4/d6-three-layers.svg', 'p4d6', 'body_p4_{lang}.html'),
    'D7': ('diagrams/part4/d7-agent-lifecycle.svg', 'p4d7', 'body_p4_{lang}.html'),
    'D8': ('diagrams/part4/d8-four-roles.svg', 'p4d8', 'body_p4_{lang}.html'),
    'D9': ('diagrams/part4/d9-platforms-govern-inward.svg', 'p4d9', 'body_p4_{lang}.html'),
    'D10': ('diagrams/part4/d10-quarterly-loop.svg', 'p4d10', 'body_p4_{lang}.html'),
}
TEXT_RX = re.compile(r'(<text[^>]*>).*?(</text>)', re.S)


def rd(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read().replace('\r\n', '\n')


def skeleton(svg, dnum, prefix):
    """O SVG sem o que muda por lingua: texto, aria-label, title, desc, xmlns, prefixo de id."""
    s = svg
    s = re.sub(r'<title>.*?</title>\s*', '', s, flags=re.S)
    s = re.sub(r'<desc>.*?</desc>\s*', '', s, flags=re.S)
    s = TEXT_RX.sub(r'\1\2', s)
    s = re.sub(r' aria-label="[^"]*"', '', s)
    s = s.replace(' xmlns="http://www.w3.org/2000/svg"', '')
    s = s.replace(prefix + '-', dnum.lower() + '-').replace('-' + prefix, '-' + dnum.lower())
    s = re.sub(r'\b(en|pt|es)-' + re.escape(dnum.lower()) + '-', dnum.lower() + '-', s)
    return re.sub(r'\s+', ' ', s).strip()


def find_inline(body, prefix):
    i = body.find(prefix + '-')
    if i < 0:
        return None
    a = body.rfind('<svg', 0, i)
    b = body.index('</svg>', i) + 6
    return body[a:b]


def problems():
    out = []
    for dnum, (path, prefix, body_t) in DIAGRAMS.items():
        full = os.path.join(ROOT, path)
        if not os.path.exists(full):
            out.append((path, 'arquivo autonomo ausente'))
            continue
        master = skeleton(rd(full), dnum, dnum.lower())
        for lang in LANGS:
            bp = os.path.join(ROOT, 'build', body_t.format(lang=lang))
            inline = find_inline(rd(bp), prefix)
            if inline is None:
                out.append((rel(bp), '%s: nenhum SVG inline com o prefixo %s' % (dnum, prefix)))
                continue
            if skeleton(inline, dnum, prefix) != master:
                out.append((rel(bp), '%s: a geometria do SVG inline difere do autonomo %s' % (dnum, path)))
            n_master = len(TEXT_RX.findall(rd(full)))
            n_inline = len(TEXT_RX.findall(inline))
            if n_master != n_inline:
                out.append((rel(bp), '%s: %d textos no autonomo, %d no inline' % (dnum, n_master, n_inline)))
    return out


def rel(p):
    return os.path.relpath(p, ROOT).replace(os.sep, '/')


if __name__ == '__main__':
    probs = problems()
    for f, m in probs:
        print('%s: %s' % (f, m))
    print('svg_check:', 'ok' if not probs else '%d problema(s)' % len(probs))
    sys.exit(1 if probs else 0)
