# -*- coding: utf-8 -*-
# Confere que o texto alternativo do grafico de palavras do README, nos tres
# idiomas, cita a mesma contagem de palavras e de marcos que
# docs/assets/logbook-metrics.json. O README carrega esses numeros como um
# retrato da ultima regeneracao do diario, e um retrato que ninguem confere
# envelhece em silencio: em 20 de setembro de 2026 ele dizia "setenta e seis
# marcos" com 85 no arquivo de dados, porque so a contagem de palavras tinha
# sido atualizada. Mesma ideia de check_glossary_order.py: uma checagem
# permanente no lugar de uma leitura atenta.
#
# Uso: python build/check_readme_snapshot.py
# Sai com 0 se os tres README batem com o JSON, 1 se algum diverge.

import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, 'docs', 'assets', 'logbook-metrics.json')

# Por arquivo: o rotulo do numero de palavras e o do numero de marcos naquele idioma.
LANGS = {
    'README.md': ('words', 'milestones'),
    'README.pt.md': ('palavras', 'marcos'),
    'README.es.md': ('palabras', 'hitos'),
}


def digits(text):
    return int(re.sub(r'[.,\s]', '', text))


def main():
    with open(DATA, encoding='utf-8') as fh:
        milestones = json.load(fh)['milestones']
    want_words = milestones[-1]['words_published']
    want_count = len(milestones)
    failed = False
    for name, (words_label, count_label) in LANGS.items():
        with open(os.path.join(ROOT, name), encoding='utf-8') as fh:
            text = fh.read()
        alt = re.search(r'<img src="docs/assets/logbook-words-published\.png" alt="([^"]*)"', text)
        if not alt:
            print('%s: no alt text found for the words chart' % name)
            failed = True
            continue
        alt = alt.group(1)
        words = re.findall(r'(\d[\d.,]*) %s' % words_label, alt)
        count = re.findall(r'(\d+) %s' % count_label, alt)
        got_words = digits(words[-1]) if words else None
        got_count = int(count[-1]) if count else None
        ok = got_words == want_words and got_count == want_count
        print('%-14s alt says %s %s, %s %s | data has %s, %s | %s' % (
            name, got_words, words_label, got_count, count_label, want_words, want_count, 'ok' if ok else 'STALE'))
        failed = failed or not ok
    return 1 if failed else 0


if __name__ == '__main__':
    sys.exit(main())
