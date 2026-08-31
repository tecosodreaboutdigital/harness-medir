# -*- coding: utf-8 -*-
# Reconstroi a serie real de palavras e tokens por marco (commit) do
# projeto, para o diario de bordo. Mesma disciplina do projeto de
# referencia (git + transcript de sessao), adaptada: metrica de
# conteudo (palavras, linhas de doc/script) em vez de LOC de aplicacao.
#
# Uso: python build/generate_logbook_metrics.py
# Escreve: docs/assets/logbook-metrics.json

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Arquivos que contam como "conteudo publicado" (palavras) e como
# "codigo do harness" (linhas). Um HTML pode nao existir ainda num
# commit antigo, tratado como zero nesse caso.
CONTENT_HTML = ['harness-p1.html', 'harness-p2.html', 'harness-p3.html', 'harness-toolkit.html',
                'harness-glossary.html', 'harness-sources.html']
CODE_GLOBS_PREFIXES = ['build/', 'TOOLS.md', 'sources/inventory.md']
GOV_DOCS = ['README.md', 'STANDARDS.md', 'STATUS.md', 'NEXT-STEPS.md']


def run(args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True, encoding='utf-8').stdout


def git_show(rev, path):
    r = subprocess.run(['git', 'show', '%s:%s' % (rev, path)], cwd=ROOT,
                        capture_output=True, text=True, encoding='utf-8', errors='replace')
    if r.returncode != 0:
        return None
    return r.stdout


def word_count_html(text):
    if text is None:
        return 0
    body = re.sub(r'<pre>.*?</pre>', ' ', text, flags=re.S)
    body = re.sub(r'<svg.*?</svg>', ' ', body, flags=re.S)
    body = re.sub(r'<script.*?</script>', ' ', body, flags=re.S)
    body = re.sub(r'<style.*?</style>', ' ', body, flags=re.S)
    body = re.sub(r'<[^>]+>', ' ', body)
    return len(body.split())


def line_count(text):
    if text is None:
        return 0
    return len(text.splitlines())


def list_repo_files_at(rev):
    out = run(['git', 'ls-tree', '-r', '--name-only', rev])
    return [l for l in out.splitlines() if l.strip()]


def commits():
    out = run(['git', 'log', '--reverse', '--pretty=format:%H|%aI|%s'])
    rows = []
    for line in out.splitlines():
        if not line.strip():
            continue
        h, iso, subj = line.split('|', 2)
        rows.append({'hash': h, 'iso': iso, 'subject': subj})
    return rows


def find_session_jsonl():
    base = os.path.expanduser('~/.claude/projects')
    target_suffix = 'AboutDigital-harness-medir'
    found = []
    if not os.path.isdir(base):
        return found
    for name in os.listdir(base):
        if name.endswith(target_suffix):
            proj_dir = os.path.join(base, name)
            for f in os.listdir(proj_dir):
                if f.endswith('.jsonl'):
                    found.append(os.path.join(proj_dir, f))
    return found


def load_usage_events(paths):
    events = []
    for p in paths:
        with open(p, encoding='utf-8') as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    d = json.loads(line)
                except Exception:
                    continue
                msg = d.get('message')
                ts = d.get('timestamp')
                if not (isinstance(msg, dict) and 'usage' in msg and ts):
                    continue
                u = msg['usage']
                events.append({
                    'ts': ts,
                    'input': u.get('input_tokens', 0) or 0,
                    'output': u.get('output_tokens', 0) or 0,
                    'cache_read': u.get('cache_read_input_tokens', 0) or 0,
                    'cache_creation': u.get('cache_creation_input_tokens', 0) or 0,
                })
    events.sort(key=lambda e: e['ts'])
    return events


def parse_iso(s):
    # git %aI gives e.g. 2026-08-30T12:36:00-03:00
    # transcript timestamp gives e.g. 2026-08-30T15:25:33.737Z
    return datetime.fromisoformat(s.replace('Z', '+00:00'))


def main():
    rows = commits()
    if not rows:
        print('sem commits, nada a fazer')
        return

    session_files = find_session_jsonl()
    events = load_usage_events(session_files)
    print('transcripts encontrados:', session_files)
    print('eventos de uso carregados:', len(events))

    # bucket de tokens: tudo que aconteceu ate o timestamp do commit,
    # e ainda nao foi atribuido a um commit anterior, entra neste marco.
    ev_idx = 0
    milestones = []
    cum_tokens = {'input': 0, 'output': 0, 'cache_read': 0, 'cache_creation': 0}

    for row in rows:
        commit_dt = parse_iso(row['iso'])
        bucket = {'input': 0, 'output': 0, 'cache_read': 0, 'cache_creation': 0}
        while ev_idx < len(events):
            e_dt = parse_iso(events[ev_idx]['ts'])
            if e_dt <= commit_dt:
                bucket['input'] += events[ev_idx]['input']
                bucket['output'] += events[ev_idx]['output']
                bucket['cache_read'] += events[ev_idx]['cache_read']
                bucket['cache_creation'] += events[ev_idx]['cache_creation']
                ev_idx += 1
            else:
                break
        for k in cum_tokens:
            cum_tokens[k] += bucket[k]

        files_at_commit = set(list_repo_files_at(row['hash']))

        words = 0
        for f in CONTENT_HTML:
            if f in files_at_commit:
                words += word_count_html(git_show(row['hash'], f))

        code_lines = 0
        for f in sorted(files_at_commit):
            if any(f == p or f.startswith(p) for p in CODE_GLOBS_PREFIXES):
                code_lines += line_count(git_show(row['hash'], f))

        gov_lines = 0
        for f in GOV_DOCS:
            if f in files_at_commit:
                gov_lines += line_count(git_show(row['hash'], f))

        milestones.append({
            'hash': row['hash'][:7],
            'timestamp': row['iso'],
            'subject': row['subject'],
            'words_published': words,
            'code_lines': code_lines,
            'governance_lines': gov_lines,
            'tokens_bucket': bucket,
            'tokens_cumulative': dict(cum_tokens),
        })

    # sobrou uso de sessao depois do ultimo commit (esta propria
    # conversa, ainda nao commitada no momento da extracao)
    remaining = {'input': 0, 'output': 0, 'cache_read': 0, 'cache_creation': 0}
    while ev_idx < len(events):
        remaining['input'] += events[ev_idx]['input']
        remaining['output'] += events[ev_idx]['output']
        remaining['cache_read'] += events[ev_idx]['cache_read']
        remaining['cache_creation'] += events[ev_idx]['cache_creation']
        ev_idx += 1

    out = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'session_files': session_files,
        'milestones': milestones,
        'tokens_since_last_commit': remaining,
    }

    out_dir = os.path.join(ROOT, 'docs', 'assets')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'logbook-metrics.json')
    with open(out_path, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    print('escrito em:', out_path)
    for m in milestones:
        t = m['tokens_cumulative']
        total = t['input'] + t['output'] + t['cache_read'] + t['cache_creation']
        print('%s  %-45s  palavras=%-6d  total_tokens_acum=%d' % (
            m['hash'], m['subject'][:45], m['words_published'], total))
    rtotal = remaining['input'] + remaining['output'] + remaining['cache_read'] + remaining['cache_creation']
    print('tokens desde o ultimo commit (ainda nesta sessao):', rtotal)


if __name__ == '__main__':
    main()
