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
