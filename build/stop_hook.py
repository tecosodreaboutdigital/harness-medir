# -*- coding: utf-8 -*-
# Hook de parada do Claude Code (item BLD.02): verify-on-stop aplicado a
# este projeto. Quando a sessao alterou arquivos publicados ou de
# governanca, roda build/check_all.py e impede o encerramento enquanto
# houver achado novo (codigo de saida 2 devolve o relatorio ao agente).
#
# Nao entra em laco: se o hook ja barrou uma vez neste turno
# (stop_hook_active), deixa encerrar e a CI segura o resto.
# Ligado em .claude/settings.json. Esse arquivo e este script so devem
# mudar com revisao humana no diff (ver [P3.02] da especificacao).
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WATCHED = ('harness-', 'index.html', 'llms.txt', 'toolkit.json', 'build/', 'playbook/',
           'sources/', 'docs/logbook.html', 'AGENTS.md', 'README', 'STATUS', 'NEXT-STEPS',
           'TOOLS', 'STANDARDS')


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    if payload.get('stop_hook_active'):
        return 0
    st = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True,
                        encoding='utf-8', cwd=ROOT)
    changed = [ln[3:].strip().strip('"') for ln in st.stdout.splitlines()]
    if not any(c.startswith(WATCHED) for c in changed):
        return 0
    p = subprocess.run([sys.executable, os.path.join(ROOT, 'build', 'check_all.py')],
                       capture_output=True, text=True, encoding='utf-8', cwd=ROOT)
    if p.returncode == 0:
        return 0
    sys.stderr.write('build/check_all.py encontrou achados novos; corrija antes de encerrar:\n')
    sys.stderr.write(p.stdout[-6000:])
    return 2


if __name__ == '__main__':
    sys.exit(main())
