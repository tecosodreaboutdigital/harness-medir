# -*- coding: utf-8 -*-
# Reconstroi a serie real de palavras e tokens por marco (commit) do
# projeto, para o diario de bordo. Mesma disciplina do projeto de
# referencia (git + transcript de sessao), adaptada: metrica de
# conteudo (palavras, linhas de doc/script) em vez de LOC de aplicacao.
#
# Custo em dinheiro portado de milestone-loc-tokens-ai-ledger (o proprio
# skill que este projeto gerou, ver NEXT-STEPS.md item 5): preco lido de
# docs/assets/prices.json, um livro-razao datado e apensado, nunca
# sobrescrito. Um marco sem entrada de preco vigente na sua data fica
# cost_recorded: null, nunca $0.00 inventado. Uma vez escrito, o custo
# de um marco nunca e recalculado retroativamente, mesmo que o livro-razao
# ganhe uma entrada nova depois, mesma regra da skill de origem.
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
PRICES_PATH = os.path.join(ROOT, 'docs', 'assets', 'prices.json')
PRICE_PROVIDER = 'anthropic'
PRICE_MODEL = 'claude-sonnet-5'
CURRENCY = 'USD'

# Arquivos que contam como "conteudo publicado" (palavras) e como
# "codigo do harness" (linhas). Um HTML pode nao existir ainda num
# commit antigo, tratado como zero nesse caso.
CONTENT_HTML = ['harness-p1.html', 'harness-p2.html', 'harness-p3.html', 'harness-p4.html', 'harness-toolkit.html',
                'harness-glossary.html', 'harness-sources.html', 'harness-playbook.html']
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
    # Uma mesma mensagem do assistente gera mais de uma linha no transcript
    # (um bloco de thinking, outro de texto ou uso de ferramenta), e cada
    # linha carrega o uso acumulado da mensagem inteira, repetido. Sem
    # deduplicar por message.id, o mesmo token e contado varias vezes: bug
    # real, achado e verificado por reuso direto deste script num projeto
    # externo (~2,17x de inflacao agregada nas 15 transcricoes desta
    # maquina), registrado em NEXT-STEPS.md. Mantem so a ultima ocorrencia
    # de cada id, que carrega o total final e mais completo da mensagem.
    by_id = {}
    unkeyed = []
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
                event = {
                    'ts': ts,
                    'input': u.get('input_tokens', 0) or 0,
                    'output': u.get('output_tokens', 0) or 0,
                    'cache_read': u.get('cache_read_input_tokens', 0) or 0,
                    'cache_creation': u.get('cache_creation_input_tokens', 0) or 0,
                }
                mid = msg.get('id')
                if mid:
                    by_id[mid] = event
                else:
                    unkeyed.append(event)
    events = list(by_id.values()) + unkeyed
    events.sort(key=lambda e: e['ts'])
    return events


def parse_iso(s):
    # git %aI gives e.g. 2026-08-30T12:36:00-03:00
    # transcript timestamp gives e.g. 2026-08-30T15:25:33.737Z
    return datetime.fromisoformat(s.replace('Z', '+00:00'))


def load_price_ledger(path):
    if not os.path.isfile(path):
        return []
    with open(path, encoding='utf-8') as fh:
        return json.load(fh)


def find_price_series(ledger, provider, model):
    for series in ledger:
        if series['provider'] == provider and series['model'] == model:
            return series
    return None


def price_at(series, target_date):
    # A entrada com effective_date mais recente que ainda seja <= a data
    # do marco, nunca a mais recente do livro-razao inteiro: um marco de
    # agosto nao deve ser precificado pelo preco vigente hoje.
    if series is None:
        return None
    eligible = [e for e in series['entries'] if e['effective_date'] <= target_date]
    if not eligible:
        return None
    return max(eligible, key=lambda e: e['effective_date'])


def compute_cost(tokens, price_entry):
    if price_entry is None:
        return None
    amount = (
        tokens.get('input', 0) / 1_000_000 * price_entry['input_price']
        + tokens.get('output', 0) / 1_000_000 * price_entry['output_price']
        + tokens.get('cache_read', 0) / 1_000_000 * price_entry['cache_read_price']
        + tokens.get('cache_creation', 0) / 1_000_000 * price_entry['cache_creation_price']
    )
    return round(amount, 4)


def load_previous_costs(path):
    # Um marco cujo custo ja foi escrito numa execucao anterior mantem
    # esse valor para sempre, mesmo que o livro-razao ganhe uma entrada
    # de preco nova depois. Sem isso, uma correcao de preco futura
    # reescreveria em silencio o custo ja publicado de um marco antigo.
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, encoding='utf-8') as fh:
            prev = json.load(fh)
    except (OSError, ValueError):
        return {}
    return {
        m['hash']: m['cost_recorded']
        for m in prev.get('milestones', [])
        if m.get('cost_recorded') is not None
    }


def main():
    rows = commits()
    if not rows:
        print('sem commits, nada a fazer')
        return

    session_files = find_session_jsonl()
    events = load_usage_events(session_files)
    print('transcripts encontrados:', session_files)
    print('eventos de uso carregados:', len(events))

    out_path_early = os.path.join(ROOT, 'docs', 'assets', 'logbook-metrics.json')
    previous_costs = load_previous_costs(out_path_early)
    price_ledger = load_price_ledger(PRICES_PATH)
    price_series = find_price_series(price_ledger, PRICE_PROVIDER, PRICE_MODEL)

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

        short_hash = row['hash'][:7]
        if short_hash in previous_costs:
            cost_recorded = previous_costs[short_hash]
        else:
            commit_date = row['iso'][:10]
            price_entry = price_at(price_series, commit_date)
            has_usage = any(bucket.values())
            cost = compute_cost(bucket, price_entry) if (price_entry and has_usage) else None
            cost_recorded = (
                {'amount': cost, 'currency': CURRENCY, 'priced_at': price_entry['effective_date'],
                 'provider': PRICE_PROVIDER, 'model': PRICE_MODEL}
                if cost is not None else None
            )

        milestones.append({
            'hash': short_hash,
            'timestamp': row['iso'],
            'subject': row['subject'],
            'words_published': words,
            'code_lines': code_lines,
            'governance_lines': gov_lines,
            'tokens_bucket': bucket,
            'tokens_cumulative': dict(cum_tokens),
            'cost_recorded': cost_recorded,
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

    # Custo projetado do uso ainda nao commitado, no preco vigente hoje.
    # Nunca congelado como o de um marco: recalcula a cada execucao ate
    # o proximo commit fechar o valor de verdade.
    today = datetime.now(timezone.utc).date().isoformat()
    remaining_price_entry = price_at(price_series, today)
    remaining_has_usage = any(remaining.values())
    remaining_cost = compute_cost(remaining, remaining_price_entry) if (remaining_price_entry and remaining_has_usage) else None
    remaining_cost_recorded = (
        {'amount': remaining_cost, 'currency': CURRENCY, 'priced_at': remaining_price_entry['effective_date'],
         'provider': PRICE_PROVIDER, 'model': PRICE_MODEL}
        if remaining_cost is not None else None
    )

    # So o nome do arquivo, nunca o caminho completo: o caminho absoluto
    # carrega o nome de usuario do sistema operacional, informacao pessoal
    # sem necessidade num artefato versionado e publico. Achado e corrigido
    # por reuso direto deste script num projeto externo, registrado em
    # NEXT-STEPS.md; o historico do git anterior a esta correcao foi
    # reescrito para remover as ocorrencias ja commitadas do caminho
    # completo.
    unpriced = sum(1 for m in milestones if m['cost_recorded'] is None)

    out = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'session_files': [os.path.basename(p) for p in session_files],
        'milestones': milestones,
        'tokens_since_last_commit': remaining,
        'cost_since_last_commit': remaining_cost_recorded,
        'unpriced_milestones': unpriced,
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
        cost_txt = '$%.4f' % m['cost_recorded']['amount'] if m['cost_recorded'] else 'sem preco'
        print('%s  %-45s  palavras=%-6d  total_tokens_acum=%d  custo=%s' % (
            m['hash'], m['subject'][:45], m['words_published'], total, cost_txt))
    rtotal = remaining['input'] + remaining['output'] + remaining['cache_read'] + remaining['cache_creation']
    print('tokens desde o ultimo commit (ainda nesta sessao):', rtotal)
    print('marcos sem preco vigente na data:', unpriced, 'de', len(milestones))


if __name__ == '__main__':
    main()
