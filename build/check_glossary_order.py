# -*- coding: utf-8 -*-
# Verifica que as entradas do glossario estao em ordem alfabetica dentro
# de cada lingua, no proprio arquivo-fonte (build/body_glossary_*.html),
# antes de qualquer prefixo de escopo entrar no build. Nao ordena nada:
# so aponta onde a ordem quebrou, para quem mantem o arquivo corrigir a
# posicao a mao, o mesmo padrao de evidencia dos demais scripts de
# build/ ('broken: [...]').
#
# Por que existe: renomear o termo visivel de uma entrada (ex. sensor ->
# verificador, dono do agente -> proprietario do agente, revisao de
# portugues de 31 de agosto de 2026) muda a letra que decide sua posicao,
# mas nao move a linha sozinho. Duas entradas ficaram fora de ordem por
# dias no arquivo publicado antes disso ser notado, porque nenhum script
# rodava esta checagem. Reforca o achado 3 do reuso do harness num
# projeto externo, registrado em NEXT-STEPS.md.
#
# Uso: python build/check_glossary_order.py
# Sai com codigo 1 se achar alguma quebra de ordem, 0 se estiver limpo.
import os
import re
import sys
import unicodedata

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FILES = {
    'EN': 'body_glossary_en.html',
    'PT': 'body_glossary_pt.html',
    'ES': 'body_glossary_es.html',
}

ITEM_RE = re.compile(r'<p class="gitem" id="([a-z0-9\-]+)"><strong>(.*?)</strong>', re.S)


def sort_key(term):
    # Remove qualquer tag residual, normaliza NFKD e descarta os
    # caracteres combinantes (acento, cedilha) antes de comparar, para
    # que "verificador" não sofra colação incorreta de acentuação, e
    # para que a ordem avaliada seja a mesma que um leitor humano
    # reconheceria como alfabética em português, inglês ou espanhol.
    term = re.sub(r'<[^>]+>', '', term)
    term = unicodedata.normalize('NFKD', term.casefold())
    term = ''.join(c for c in term if unicodedata.category(c) != 'Mn')
    return term


def check(lang, path):
    with open(path, encoding='utf-8') as fh:
        text = fh.read()
    items = ITEM_RE.findall(text)
    broken = []
    for (prev_id, prev_term), (cur_id, cur_term) in zip(items, items[1:]):
        if sort_key(cur_term) < sort_key(prev_term):
            broken.append((prev_id, prev_term, cur_id, cur_term))
    return broken


def main():
    any_broken = False
    for lang, fname in FILES.items():
        path = os.path.join(ROOT, 'build', fname)
        broken = check(lang, path)
        if broken:
            any_broken = True
            print('broken order (%s):' % lang)
            for prev_id, prev_term, cur_id, cur_term in broken:
                print('  "%s" (%s) comes right before "%s" (%s), out of order' % (
                    prev_term, prev_id, cur_term, cur_id))
        else:
            print('%s: ok' % lang)
    sys.exit(1 if any_broken else 0)


if __name__ == '__main__':
    main()
