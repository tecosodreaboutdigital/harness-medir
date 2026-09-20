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
# A regra da skill de origem que este script agora tambem segue: congelar
# o fato de granularidade mais fina, derivar o preco depois. Um marco
# grava os tokens por modelo e por TTL de cache (tokens_split), nao so o
# custo, e uma execucao normal NUNCA reabre os tokens de um marco ja
# gravado: eles vem da transcricao, e a transcricao expira (o Claude Code
# apaga arquivos com mais de cleanupPeriodDays, 30 por padrao). Palavras
# e linhas de um marco tambem sao congeladas por hash, desde que as
# regras de contagem (CONTENT_HTML e afins) nao tenham mudado desde a
# gravacao, o que e verificado por count_rules_hash.
#
# Duas excecoes explicitas e auditadas a "custo gravado nunca muda":
#
# --reprice: a correcao de um preco que estava ERRADO (nao de um preco
# que mudou). Recalcula so o custo dos marcos ja gravados, a partir dos
# tokens ja gravados neles, contra o livro-razao como esta agora, sem ler
# git nem transcript. O custo anterior fica na lista repricings do marco.
# Ver a skill de origem, SKILL.md, "Correcting a price that was wrong".
#
# --enrich: a migracao unica de um marco gravado antes de os tokens
# ganharem o corte por modelo e por TTL. Re-deriva o corte das
# transcricoes e so o aplica se os quatro contadores originais (input,
# output, cache_read, cache_creation) re-derivados forem IDENTICOS aos
# gravados; senao recusa e deixa o marco intacto. Com --dry-run so
# imprime o relatorio. Ver a skill de origem, SKILL.md, "Enriching
# milestones recorded before a schema change". Tem prazo: depois que a
# transcricao expira, o marco nao pode mais ser enriquecido.
#
# Tokens de subagentes (<sessao>/subagents/*.jsonl): este script nunca os
# leu ate 20 de setembro de 2026, e desde entao eles CONTAM (decisao do
# autor no mesmo dia). O fato de cada fonte fica congelado a parte:
# tokens_bucket e tokens_split sao as sessoes-mae, subagent_tokens e o que
# os subagentes gravaram. O que os totais, os graficos e o custo leem e
# derivado a cada execucao, nunca congelado: tokens_total (a soma dos
# dois) e tokens_cumulative. Assim o guarda do --enrich, que compara so os
# contadores da sessao-mae com a transcricao, continua valendo.
#
# Uso: python build/generate_logbook_metrics.py                        (execucao normal)
#      python build/generate_logbook_metrics.py --recount              (recontar palavras/linhas de todos)
#      python build/generate_logbook_metrics.py --reprice [--note TEXTO] (ver acima)
#      python build/generate_logbook_metrics.py --enrich --dry-run     (ver acima, so relatorio)
#      python build/generate_logbook_metrics.py --enrich               (ver acima, grava)
# Escreve: docs/assets/logbook-metrics.json

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PRICES_PATH = os.path.join(ROOT, 'docs', 'assets', 'prices.json')
OUT_PATH = os.path.join(ROOT, 'docs', 'assets', 'logbook-metrics.json')
PRICE_PROVIDER = 'anthropic'
PRICE_MODEL = 'claude-sonnet-5'
CURRENCY = 'USD'
EXIT_SOME_REFUSED = 3

# Os quatro contadores originais, os unicos que tokens_bucket e
# tokens_cumulative carregam (build_logbook.py soma seus .values()).
# cache_creation_1h e um SUBCONJUNTO de cache_creation, por isso nunca
# entra numa soma: vive em tokens_split, a chave irma.
LEGACY_KINDS = ('input', 'output', 'cache_read', 'cache_creation')
SPLIT_FIELDS = LEGACY_KINDS + ('cache_creation_1h',)

# Arquivos que contam como "conteudo publicado" (palavras) e como
# "codigo do harness" (linhas). Um HTML pode nao existir ainda num
# commit antigo, tratado como zero nesse caso.
CONTENT_HTML = ['harness-p1.html', 'harness-p2.html', 'harness-p3.html', 'harness-p4.html', 'harness-toolkit.html',
                'harness-glossary.html', 'harness-sources.html', 'harness-playbook.html']
CODE_GLOBS_PREFIXES = ['build/', 'TOOLS.md', 'sources/inventory.md']
GOV_DOCS = ['README.md', 'STANDARDS.md', 'STATUS.md', 'NEXT-STEPS.md']

# Subir este numero sempre que word_count_html ou line_count mudar de
# comportamento: ele entra em count_rules_hash junto com as tres listas
# acima, e uma mudanca ali invalida as palavras e linhas congeladas.
COUNT_ALGORITHM_VERSION = 1


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


def count_rules_hash():
    payload = json.dumps({'content': CONTENT_HTML, 'code': CODE_GLOBS_PREFIXES, 'gov': GOV_DOCS,
                          'algorithm': COUNT_ALGORITHM_VERSION}, sort_keys=True)
    return hashlib.sha256(payload.encode('utf-8')).hexdigest()[:16]


def count_commit(row):
    # Palavras e linhas de um commit: funcao pura do conteudo dele e das
    # regras de contagem acima, por isso congelavel por hash.
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

    return words, code_lines, gov_lines


def _project_dir():
    base = os.path.expanduser('~/.claude/projects')
    target_suffix = 'AboutDigital-harness-medir'
    if not os.path.isdir(base):
        return None
    for name in os.listdir(base):
        if name.endswith(target_suffix):
            return os.path.join(base, name)
    return None


def find_session_jsonl():
    proj_dir = _project_dir()
    if proj_dir is None:
        return []
    return [os.path.join(proj_dir, f) for f in os.listdir(proj_dir) if f.endswith('.jsonl')]


def find_subagent_jsonl():
    # Um subagente despachado pela ferramenta Task grava a propria
    # transcricao em <projeto>/<uuid-da-sessao>/subagents/*.jsonl, nunca
    # como arquivo de primeiro nivel ao lado da sessao-mae. Sem isto,
    # nenhum token gasto por subagente aparece.
    proj_dir = _project_dir()
    if proj_dir is None:
        return []
    found = []
    for name in sorted(os.listdir(proj_dir)):
        sub_dir = os.path.join(proj_dir, name, 'subagents')
        if os.path.isdir(sub_dir):
            found.extend(os.path.join(sub_dir, f) for f in sorted(os.listdir(sub_dir)) if f.endswith('.jsonl'))
    return found


def _as_count(value):
    # Contagem de token vinda da transcricao: inteiro nao negativo, senao 0.
    # Um bool e int em Python, mas nunca e uma contagem.
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        return 0
    return value


def _one_hour_cache_writes(usage, cache_creation_total):
    # A parcela de 1 hora das escritas de cache de uma mensagem: uma
    # transcricao real traz usage.cache_creation = {ephemeral_5m_input_tokens,
    # ephemeral_1h_input_tokens}; linhas antigas ou parciais nao trazem, e
    # ai nada se sabe ser de 1 hora, entao 0. Limitada ao proprio
    # cache_creation_input_tokens da mensagem, sempre um subconjunto.
    breakdown = usage.get('cache_creation')
    if not isinstance(breakdown, dict):
        return 0
    return min(_as_count(breakdown.get('ephemeral_1h_input_tokens')), cache_creation_total)


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
                cache_creation = u.get('cache_creation_input_tokens', 0) or 0
                model = msg.get('model')
                event = {
                    'ts': ts,
                    'model': model if isinstance(model, str) and model else None,
                    'input': u.get('input_tokens', 0) or 0,
                    'output': u.get('output_tokens', 0) or 0,
                    'cache_read': u.get('cache_read_input_tokens', 0) or 0,
                    'cache_creation': cache_creation,
                    'cache_creation_1h': _one_hour_cache_writes(u, _as_count(cache_creation)),
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


def empty_bucket():
    return {k: 0 for k in LEGACY_KINDS}


def empty_split():
    return {'cache_creation_1h': 0, 'by_model': {}}


def add_event(bucket, split, event):
    for k in LEGACY_KINDS:
        bucket[k] += event[k]
    split['cache_creation_1h'] += event['cache_creation_1h']
    # Corte por modelo so para eventos que nomeiam um modelo E carregam
    # token: uma linha sem modelo fica so nos totais (nao ha como precifica-la
    # sem adivinhar o modelo), e uma linha sintetica de uso zero nao cria entrada.
    model = event['model']
    if model and any(event[k] for k in LEGACY_KINDS):
        per_model = split['by_model'].setdefault(model, {f: 0 for f in SPLIT_FIELDS})
        for f in SPLIT_FIELDS:
            per_model[f] += event[f]


def attribute_events(rows, events):
    # Tudo que aconteceu ate o timestamp do commit, e ainda nao foi
    # atribuido a um commit anterior, entra neste marco. Devolve um
    # (bucket, split) por commit e o que sobrou depois do ultimo commit.
    ev_idx = 0
    per_commit = []
    for row in rows:
        commit_dt = parse_iso(row['iso'])
        bucket, split = empty_bucket(), empty_split()
        while ev_idx < len(events) and parse_iso(events[ev_idx]['ts']) <= commit_dt:
            add_event(bucket, split, events[ev_idx])
            ev_idx += 1
        per_commit.append((bucket, split))
    remaining_bucket, remaining_split = empty_bucket(), empty_split()
    while ev_idx < len(events):
        add_event(remaining_bucket, remaining_split, events[ev_idx])
        ev_idx += 1
    return per_commit, (remaining_bucket, remaining_split)


def full_tokens(bucket, split):
    # Um dict so, no formato que o preco le: os quatro contadores, o
    # subconjunto de 1 hora e o corte por modelo. Ausente o corte (marco
    # gravado antes dele), so os quatro contadores.
    tokens = dict(bucket)
    if split:
        tokens['cache_creation_1h'] = split.get('cache_creation_1h', 0)
        tokens['by_model'] = split.get('by_model', {})
    return tokens


def total_tokens(tokens):
    return sum(tokens.get(k, 0) for k in LEGACY_KINDS)


def milestone_tokens(bucket, split, subagent):
    # Os tokens que os totais e o custo leem: as sessoes-mae mais os
    # subagentes, no formato que o preco le (quatro contadores, o
    # subconjunto de 1 hora e o corte por modelo somado modelo a modelo).
    # Sem corte da sessao-mae (marco anterior ao --enrich), so os quatro
    # contadores: sem by_model o preco cai na serie unica, nunca mistura.
    tokens = {k: bucket.get(k, 0) + (subagent.get(k, 0) if subagent else 0) for k in LEGACY_KINDS}
    if split is None:
        return tokens
    tokens['cache_creation_1h'] = split.get('cache_creation_1h', 0) + (subagent.get('cache_creation_1h', 0) if subagent else 0)
    by_model = {}
    for source in (split.get('by_model', {}), (subagent or {}).get('by_model', {})):
        for model, counters in source.items():
            acc = by_model.setdefault(model, {f: 0 for f in SPLIT_FIELDS})
            for f in SPLIT_FIELDS:
                acc[f] += counters.get(f, 0)
    tokens['by_model'] = by_model
    return tokens


def four_counters(tokens):
    return {k: tokens.get(k, 0) for k in LEGACY_KINDS}


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
    # agosto nao deve ser precificado pelo preco vigente hoje. Em empate de
    # data, a entrada gravada depois vence: e assim que uma entrada com
    # "corrects" substitui a errada sem que esta seja editada ou apagada.
    if series is None:
        return None
    best = None
    for e in series['entries']:
        if e['effective_date'] <= target_date and (best is None or e['effective_date'] >= best['effective_date']):
            best = e
    return best


def price_tokens(tokens, entry):
    # Precifica um conjunto de tokens com uma entrada do livro-razao.
    # Devolve (valor, tokens_de_1h_sem_preco): escritas de cache de 1 hora
    # so tem preco se a entrada trouxer cache_creation_1h_price, nunca sao
    # precificadas a taxa de 5 minutos.
    cache_creation = tokens.get('cache_creation', 0)
    one_hour = min(tokens.get('cache_creation_1h', 0), cache_creation)
    five_minute = cache_creation - one_hour
    amount = (
        tokens.get('input', 0) / 1_000_000 * entry['input_price']
        + tokens.get('output', 0) / 1_000_000 * entry['output_price']
        + tokens.get('cache_read', 0) / 1_000_000 * entry['cache_read_price']
        + five_minute / 1_000_000 * entry['cache_creation_price']
    )
    unpriced_one_hour = 0
    if one_hour:
        one_hour_price = entry.get('cache_creation_1h_price')
        if one_hour_price is None:
            unpriced_one_hour = one_hour
        else:
            amount += one_hour / 1_000_000 * one_hour_price
    return amount, unpriced_one_hour


def _unpriced(model, tokens, reason):
    return {'model': model, 'tokens': tokens, 'reason': reason}


def _why_no_entry(series, model, date):
    if series is None:
        return 'no price series for %s / %s in the ledger' % (PRICE_PROVIDER, model)
    earliest = min(e['effective_date'] for e in series['entries'])
    return 'no %s / %s price entry effective on or before %s (the series starts %s)' % (
        PRICE_PROVIDER, model, date, earliest)


def _why_no_one_hour_price(model, effective_date):
    return ('1-hour cache writes, but the %s / %s entry effective %s has no cache_creation_1h_price; '
            'they are not priced at the 5-minute rate' % (PRICE_PROVIDER, model, effective_date))


def price_milestone(tokens, ledger, date):
    # Um so lugar precifica um marco, para a execucao normal, --reprice e
    # --enrich, assim os tres nunca divergem. Devolve (cost_recorded,
    # unpriced): cost_recorded e null, nunca $0.00 inventado, quando nada
    # tem preco; unpriced lista cada parcela sem preco, com o motivo.
    # Com parcelas precificadas e outras nao, o valor cobre so as
    # precificadas: e um piso, nunca um chute.
    #
    # Um marco com by_model precifica cada modelo com a serie propria
    # (id exato do modelo, entrada vigente na data). Um marco sem by_model
    # (gravado antes do corte) mantem o comportamento original: todos os
    # tokens com a serie unica PRICE_MODEL.
    if total_tokens(tokens) == 0:
        return None, []

    by_model = tokens.get('by_model') or {}
    if not by_model:
        series = find_price_series(ledger, PRICE_PROVIDER, PRICE_MODEL)
        entry = price_at(series, date)
        if entry is None:
            return None, [_unpriced(PRICE_MODEL, total_tokens(tokens), _why_no_entry(series, PRICE_MODEL, date))]
        amount, unpriced_one_hour = price_tokens(tokens, entry)
        unpriced = []
        if unpriced_one_hour:
            unpriced.append(_unpriced(PRICE_MODEL, unpriced_one_hour,
                                      _why_no_one_hour_price(PRICE_MODEL, entry['effective_date'])))
        return {'amount': round(amount, 4), 'currency': CURRENCY, 'priced_at': entry['effective_date'],
                'provider': PRICE_PROVIDER, 'model': PRICE_MODEL}, unpriced

    total_amount = 0.0
    priced = {}
    unpriced = []
    for model in sorted(by_model):
        model_tokens = by_model[model]
        if total_tokens(model_tokens) == 0:
            continue
        series = find_price_series(ledger, PRICE_PROVIDER, model)
        entry = price_at(series, date)
        if entry is None:
            unpriced.append(_unpriced(model, total_tokens(model_tokens), _why_no_entry(series, model, date)))
            continue
        amount, unpriced_one_hour = price_tokens(model_tokens, entry)
        if unpriced_one_hour:
            unpriced.append(_unpriced(model, unpriced_one_hour, _why_no_one_hour_price(model, entry['effective_date'])))
        total_amount += amount
        priced[model] = {'amount': round(amount, 4), 'priced_at': entry['effective_date']}

    # Tokens contados no marco que nenhum by_model explica (linhas de
    # transcricao sem modelo): nao ha como precifica-los sem adivinhar.
    leftover = sum(max(tokens.get(k, 0) - sum(t.get(k, 0) for t in by_model.values()), 0) for k in LEGACY_KINDS)
    if leftover:
        unpriced.append(_unpriced(None, leftover, 'usage rows that name no model id; they cannot be priced '
                                                   'without guessing the model'))
    if not priced:
        return None, unpriced
    cost = {'amount': round(total_amount, 4), 'currency': CURRENCY,
            'priced_at': max(p['priced_at'] for p in priced.values()), 'provider': PRICE_PROVIDER,
            'model': next(iter(priced)) if len(priced) == 1 else 'multiple'}
    if len(priced) > 1:
        cost['by_model'] = priced
    return cost, unpriced


def partial_unpriced(cost, unpriced):
    # A lista unpriced so tem sentido num custo PARCIAL: parte dos tokens
    # precificada, parte nao. Um marco sem custo nenhum (cost_recorded:
    # null) ja diz tudo com o null, e repetir o motivo em cada um so
    # incharia o arquivo e faria todo marco sem preco parecer parcial.
    return unpriced if cost is not None else []


def load_previous(path):
    # O que uma execucao anterior gravou: custos, tokens, palavras e linhas
    # de um marco ja gravado viajam com ele, e a trilha de auditoria de um
    # --reprice ou --enrich tambem. Sem isso, uma execucao normal a
    # descartaria em silencio.
    if not os.path.isfile(path):
        return {}
    try:
        with open(path, encoding='utf-8') as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def _recorded_total(milestones):
    return sum(m['cost_recorded']['amount'] for m in milestones if m['cost_recorded'] is not None)


def reprice(note=None):
    if not os.path.isfile(OUT_PATH):
        raise SystemExit('--reprice precisa de %s ja existente: corrige custos ja gravados, a partir dos '
                         'tokens ja gravados nele. Rode uma geracao normal antes.' % OUT_PATH)
    with open(OUT_PATH, encoding='utf-8') as fh:
        data = json.load(fh)
    ledger = load_price_ledger(PRICES_PATH)
    now = datetime.now(timezone.utc).isoformat()

    before = _recorded_total(data['milestones'])
    changed = 0
    for m in data['milestones']:
        new_cost, new_unpriced = price_milestone(
            milestone_tokens(m['tokens_bucket'], m.get('tokens_split'), m.get('subagent_tokens')),
            ledger, m['timestamp'][:10])
        new_unpriced = partial_unpriced(new_cost, new_unpriced)
        old_cost = m['cost_recorded']
        if new_cost == old_cost and new_unpriced == m.get('unpriced', []):
            continue
        record = {'repriced_at': now, 'previous_cost': old_cost}
        if m.get('unpriced'):
            record['previous_unpriced'] = m['unpriced']
        record['reason'] = 'reprice'
        if note:
            record['note'] = note
        m.setdefault('repricings', []).append(record)
        m['cost_recorded'] = new_cost
        m.pop('unpriced', None)
        if new_unpriced:
            m['unpriced'] = new_unpriced
        changed += 1

    # A projecao do uso ainda nao commitado nunca foi congelada, e sai dos
    # tokens ja gravados: acompanha o livro-razao em vez de ficar no preco errado.
    today = datetime.now(timezone.utc).date().isoformat()
    remaining = dict(data['tokens_since_last_commit'], **data.get('tokens_since_last_commit_split', {}))
    data['cost_since_last_commit'] = price_milestone(remaining, ledger, today)[0]
    data['unpriced_milestones'] = sum(1 for m in data['milestones'] if m['cost_recorded'] is None)
    if changed:
        data['last_repriced_at'] = now

    with open(OUT_PATH, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    print('repricing de %d de %d marcos a partir dos tokens gravados; custo gravado %.4f -> %.4f %s'
          % (changed, len(data['milestones']), before, _recorded_total(data['milestones']), CURRENCY))


def plan_enrichment(milestones, derived_by_hash, subagent_by_hash, ledger):
    # Um item por marco candidato: os que ainda nao tem tokens_split. O
    # marco e enriquecido so se os quatro contadores originais
    # re-derivados das transcricoes forem IDENTICOS aos gravados. Uma
    # transcricao apagada, um historico reescrito ou um leitor que mudou
    # aparecem todos como diferenca aqui, e o marco e recusado, nunca
    # recebe um numero adivinhado. Nao altera nenhum argumento.
    plan = []
    for m in milestones:
        if 'tokens_split' in m:
            continue
        h = m['hash']
        derived = derived_by_hash.get(h)
        if derived is None:
            plan.append({'hash': h, 'status': 'refused', 'reason': 'commit_not_in_history'})
            continue
        bucket, split = derived
        differences = {k: (m['tokens_bucket'].get(k, 0), bucket[k]) for k in LEGACY_KINDS
                       if m['tokens_bucket'].get(k, 0) != bucket[k]}
        if differences:
            plan.append({'hash': h, 'status': 'refused', 'reason': 'counters_differ', 'differences': differences})
            continue

        date = m['timestamp'][:10]
        item = {'hash': h, 'status': 'enrich', 'split': split, 'subagent': subagent_by_hash.get(h),
                'priced': m['cost_recorded'] is not None}
        if item['priced']:
            old_amount = m['cost_recorded']['amount']
            one_hour_only, _ = price_milestone(full_tokens(bucket, {'cache_creation_1h': split['cache_creation_1h'],
                                                                     'by_model': {}}), ledger, date)
            new_cost, new_unpriced = price_milestone(full_tokens(bucket, split), ledger, date)
            new_unpriced = partial_unpriced(new_cost, new_unpriced)
            now_cost, now_unpriced = price_milestone(full_tokens(bucket, None), ledger, date)
            now_unpriced = partial_unpriced(now_cost, now_unpriced)
            item.update({
                'cost_recorded': new_cost, 'unpriced': new_unpriced, 'previous_amount': old_amount,
                'delta_one_hour': (one_hour_only['amount'] if one_hour_only else 0.0) - old_amount,
                'delta_model': (new_cost['amount'] if new_cost else 0.0) - (one_hour_only['amount'] if one_hour_only else 0.0),
                # O custo gravado ainda e o que o livro-razao de hoje da aos
                # tokens gravados? Se nao, parte da mudanca e um --reprice
                # pendente, nao o corte.
                'ledger_drift': now_cost != m['cost_recorded'] or now_unpriced != m.get('unpriced', []),
                'becomes_partial': bool(new_unpriced) and not m.get('unpriced'),
            })
        plan.append(item)
    return plan


def format_enrich_report(plan, total_milestones, transcript_files, usage_events, subagent_files, subagent_events,
                         dry_run):
    enriched = [r for r in plan if r['status'] == 'enrich']
    refused = [r for r in plan if r['status'] == 'refused']
    if dry_run:
        header = 'enrich (dry run): nada foi escrito'
        done, cost_subject = 'seriam enriquecidos', 'seriam enriquecidos'
    else:
        header = 'enrich: marcos enriquecidos no lugar; o custo anterior de cada um fica em repricings'
        done, cost_subject = 'enriquecidos', 'foram enriquecidos'
    lines = [
        header,
        'lidos %d arquivos de transcricao e %d eventos de uso (subagentes: %d arquivos, %d eventos)'
        % (transcript_files, usage_events, subagent_files, subagent_events),
        '%d de %d marcos foram gravados antes do corte por modelo e por TTL' % (len(plan), total_milestones),
        '%s: %d' % (done, len(enriched)),
        'recusados: %d' % len(refused),
    ]
    for r in refused:
        if r['reason'] == 'commit_not_in_history':
            why = 'commit nao encontrado no historico do git (reescrito ou rebaseado?)'
        else:
            why = '; '.join('%s gravado %s, re-derivado %s' % (k, '{:,}'.format(a), '{:,}'.format(b))
                            for k, (a, b) in r['differences'].items())
        lines.append('  %s: %s' % (r['hash'], why))
    priced = [r for r in enriched if r['priced']]
    lines.append('desses, %d tem custo gravado (o custo e recalculado, com trilha de auditoria) e %d nao tem '
                 '(so ganham o corte dos tokens, o custo segue null)' % (len(priced), len(enriched) - len(priced)))
    if priced:
        before = sum(r['previous_amount'] for r in priced)
        after = sum(r['cost_recorded']['amount'] if r['cost_recorded'] else 0.0 for r in priced)
        lines.extend([
            'custo gravado dos marcos que %s: %.4f -> %.4f %s (%+.4f)' % (cost_subject, before, after, CURRENCY,
                                                                          after - before),
            '  escritas de cache de 1 hora: %+.4f' % sum(r['delta_one_hour'] for r in priced),
            '  mistura de modelos: %+.4f' % sum(r['delta_model'] for r in priced),
        ])
        partial = [r for r in priced if r['becomes_partial']]
        lines.append('ficariam parciais (algum token sem preco): %d' % len(partial))
        for r in partial:
            lines.append('  %s: %s' % (r['hash'], ', '.join(
                '%s (%s tokens)' % (u['model'] or 'sem id de modelo', '{:,}'.format(u['tokens'])) for u in r['unpriced'])))
        drifted = sum(1 for r in priced if r['ledger_drift'])
        if drifted:
            lines.append('AVISO: %d desses marcos ja gravam um custo diferente do que o livro-razao de hoje da aos '
                         'tokens gravados; rode --reprice antes para a mudanca acima mostrar so o corte' % drifted)
    captured = [r for r in enriched if r['subagent'] is not None]
    if captured:
        sub_total = sum(total_tokens(r['subagent']) for r in captured)
        lines.append('subagentes: %d marcos ganham subagent_tokens (%s tokens no total, fora dos totais publicados)'
                     % (len(captured), '{:,}'.format(sub_total)))
    return '\n'.join(lines)


def enrich(dry_run):
    if not os.path.isfile(OUT_PATH):
        raise SystemExit('--enrich precisa de %s ja existente: migra marcos ja gravados. Rode uma geracao '
                         'normal antes.' % OUT_PATH)
    with open(OUT_PATH, encoding='utf-8') as fh:
        data = json.load(fh)
    rows = commits()
    session_files = find_session_jsonl()
    subagent_files = find_subagent_jsonl()
    events = load_usage_events(session_files)
    sub_events = load_usage_events(subagent_files)
    derived, _ = attribute_events(rows, events)
    sub_derived, _ = attribute_events(rows, sub_events)
    derived_by_hash = {row['hash'][:7]: pair for row, pair in zip(rows, derived)}
    # Os subagentes nao tem contadores gravados para conferir (nunca foram
    # lidos), entao a unica prova de que a transcricao daquele periodo
    # sobrevive e o guarda dos contadores de primeiro nivel: so entram
    # marcos que passaram nele.
    subagent_by_hash = {}
    for row, (bucket, split) in zip(rows, sub_derived):
        subagent_by_hash[row['hash'][:7]] = full_tokens(bucket, split)

    ledger = load_price_ledger(PRICES_PATH)
    plan = plan_enrichment(data['milestones'], derived_by_hash, subagent_by_hash, ledger)
    print(format_enrich_report(plan, len(data['milestones']), len(session_files), len(events),
                               len(subagent_files), len(sub_events), dry_run))
    exit_code = EXIT_SOME_REFUSED if any(r['status'] == 'refused' for r in plan) else 0
    if dry_run:
        return exit_code

    by_hash = {r['hash']: r for r in plan if r['status'] == 'enrich'}
    now = datetime.now(timezone.utc).isoformat()
    for m in data['milestones']:
        result = by_hash.get(m['hash'])
        if result is None:
            continue
        if result['priced']:
            record = {'repriced_at': now, 'previous_cost': m['cost_recorded']}
            if m.get('unpriced'):
                record['previous_unpriced'] = m['unpriced']
            record['reason'] = 'enrich'
            m.setdefault('repricings', []).append(record)
            m['cost_recorded'] = result['cost_recorded']
            m.pop('unpriced', None)
            if result['unpriced']:
                m['unpriced'] = result['unpriced']
        m['tokens_split'] = result['split']
        if result['subagent'] is not None:
            m['subagent_tokens'] = result['subagent']
    data['unpriced_milestones'] = sum(1 for m in data['milestones'] if m['cost_recorded'] is None)
    data['last_enriched_at'] = now
    data['subagent_transcript_files'] = len(subagent_files)
    data['subagent_tokens_note'] = SUBAGENT_NOTE
    with open(OUT_PATH, 'w', encoding='utf-8') as fh:
        json.dump(data, fh, ensure_ascii=False, indent=2)
    return exit_code


SUBAGENT_NOTE = ('Subagent transcripts (<session>/subagents/*.jsonl) were never read before 20 September 2026. '
                 'subagent_tokens on a milestone holds what they recorded, captured while the transcripts still '
                 'existed, split by model and by cache lifetime. They are counted: tokens_total is tokens_bucket (the '
                 'parent sessions) plus subagent_tokens, and tokens_cumulative, the totals, the charts and the cost '
                 'are all built from tokens_total, priced per model. tokens_bucket and tokens_split stay the parent '
                 'sessions alone, because they are the frozen fact that --enrich checks against the transcripts.')


def main(recount=False):
    rows = commits()
    if not rows:
        print('sem commits, nada a fazer')
        return

    session_files = find_session_jsonl()
    subagent_files = find_subagent_jsonl()
    events = load_usage_events(session_files)
    sub_events = load_usage_events(subagent_files)
    print('transcripts encontrados:', [os.path.basename(p) for p in session_files])
    print('eventos de uso carregados:', len(events), '| subagentes:', len(subagent_files), 'arquivos,',
          len(sub_events), 'eventos')

    previous = load_previous(OUT_PATH)
    prev_ms = {m['hash']: m for m in previous.get('milestones', [])}
    price_ledger = load_price_ledger(PRICES_PATH)

    # Contagem de palavras e linhas congelada por hash so vale se as regras
    # de contagem nao mudaram desde a gravacao. Sem a marca de uma execucao
    # anterior (a primeira depois desta mudanca), ou com a marca diferente
    # (uma pagina entrou em CONTENT_HTML, por exemplo), recontar tudo.
    rules = count_rules_hash()
    reuse_counts = (not recount) and previous.get('count_rules_hash') == rules
    if reuse_counts:
        print('regras de contagem inalteradas: palavras e linhas dos marcos ja gravados reaproveitadas')
    else:
        why = '--recount' if recount else ('sem marca anterior' if 'count_rules_hash' not in previous
                                           else 'regras de contagem mudaram')
        print('recontando palavras e linhas de todos os marcos (%s); pode levar varios minutos' % why)

    derived, (remaining, remaining_split) = attribute_events(rows, events)
    sub_derived, (sub_remaining, sub_remaining_split) = attribute_events(rows, sub_events)

    milestones = []
    cum_tokens = empty_bucket()
    count_changes = 0
    tokens_frozen = 0
    tokens_differ = 0

    for row, (derived_bucket, derived_split), (sub_bucket, sub_split) in zip(rows, derived, sub_derived):
        short_hash = row['hash'][:7]
        prev = prev_ms.get(short_hash)

        # Os tokens de um marco ja gravado nunca sao reabertos: vem do
        # arquivo, nao da transcricao, que expira. So um commit novo deriva.
        if prev is not None and 'tokens_bucket' in prev:
            bucket = {k: prev['tokens_bucket'].get(k, 0) for k in LEGACY_KINDS}
            split = prev.get('tokens_split')
            subagent = prev.get('subagent_tokens')
            tokens_frozen += 1
            if bucket != derived_bucket:
                tokens_differ += 1
        else:
            bucket, split = derived_bucket, derived_split
            subagent = full_tokens(sub_bucket, sub_split)
        tokens = milestone_tokens(bucket, split, subagent)
        total = four_counters(tokens)
        for k in cum_tokens:
            cum_tokens[k] += total[k]

        if reuse_counts and prev is not None:
            words, code_lines, gov_lines = prev['words_published'], prev['code_lines'], prev['governance_lines']
        else:
            words, code_lines, gov_lines = count_commit(row)
            if prev is not None and (words, code_lines, gov_lines) != (
                    prev['words_published'], prev['code_lines'], prev['governance_lines']):
                count_changes += 1
                print('  contagem mudou em %s: palavras %d->%d, codigo %d->%d, governanca %d->%d' % (
                    short_hash, prev['words_published'], words, prev['code_lines'], code_lines,
                    prev['governance_lines'], gov_lines))

        if prev is not None and prev.get('cost_recorded') is not None:
            # Custo ja gravado nunca muda numa execucao normal.
            cost_recorded, unpriced_list = prev['cost_recorded'], prev.get('unpriced', [])
        else:
            cost_recorded, unpriced_list = price_milestone(tokens, price_ledger, row['iso'][:10])
            unpriced_list = partial_unpriced(cost_recorded, unpriced_list)

        milestone = {
            'hash': short_hash,
            'timestamp': row['iso'],
            'subject': row['subject'],
            'words_published': words,
            'code_lines': code_lines,
            'governance_lines': gov_lines,
            'tokens_bucket': bucket,
            'tokens_total': total,
            'tokens_cumulative': dict(cum_tokens),
            'cost_recorded': cost_recorded,
        }
        if split is not None:
            milestone['tokens_split'] = split
        if subagent is not None:
            milestone['subagent_tokens'] = subagent
        if unpriced_list:
            milestone['unpriced'] = unpriced_list
        if prev is not None and prev.get('repricings'):
            milestone['repricings'] = prev['repricings']
        milestones.append(milestone)

    print('tokens congelados de %d marcos (%d diferem da re-derivacao das transcricoes atuais: mantido o gravado)'
          % (tokens_frozen, tokens_differ))
    if not reuse_counts and count_changes:
        print('AVISO: %d marcos ganharam palavras ou linhas diferentes das gravadas' % count_changes)

    # Custo projetado do uso ainda nao commitado, no preco vigente hoje.
    # Nunca congelado como o de um marco: recalcula a cada execucao ate
    # o proximo commit fechar o valor de verdade.
    today = datetime.now(timezone.utc).date().isoformat()
    remaining_tokens = milestone_tokens(remaining, remaining_split, full_tokens(sub_remaining, sub_remaining_split))
    remaining_cost_recorded, _ = price_milestone(remaining_tokens, price_ledger, today)
    unpriced = sum(1 for m in milestones if m['cost_recorded'] is None)

    # So o nome do arquivo, nunca o caminho completo: o caminho absoluto
    # carrega o nome de usuario do sistema operacional, informacao pessoal
    # sem necessidade num artefato versionado e publico. Achado e corrigido
    # por reuso direto deste script num projeto externo, registrado em
    # NEXT-STEPS.md; o historico do git anterior a esta correcao foi
    # reescrito para remover as ocorrencias ja commitadas do caminho
    # completo.
    out = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'session_files': [os.path.basename(p) for p in session_files],
        'count_rules_hash': rules,
        'milestones': milestones,
        'tokens_since_last_commit': four_counters(remaining_tokens),
        'tokens_since_last_commit_split': {'cache_creation_1h': remaining_tokens.get('cache_creation_1h', 0),
                                           'by_model': remaining_tokens.get('by_model', {})},
        'cost_since_last_commit': remaining_cost_recorded,
        'unpriced_milestones': unpriced,
    }
    for key in ('last_repriced_at', 'last_enriched_at', 'subagent_transcript_files'):
        if previous.get(key):
            out[key] = previous[key]
    out['subagent_tokens_note'] = SUBAGENT_NOTE

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w', encoding='utf-8') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=2)

    print('escrito em:', OUT_PATH)
    for m in milestones:
        t = m['tokens_cumulative']
        total = sum(t.values())
        cost_txt = '$%.4f' % m['cost_recorded']['amount'] if m['cost_recorded'] else 'sem preco'
        print('%s  %-45s  palavras=%-6d  total_tokens_acum=%d  custo=%s' % (
            m['hash'], m['subject'][:45], m['words_published'], total, cost_txt))
    print('tokens desde o ultimo commit (ainda nesta sessao):', sum(four_counters(remaining_tokens).values()))
    print('marcos sem preco vigente na data:', unpriced, 'de', len(milestones))
    partial = [m['hash'] for m in milestones if m.get('unpriced')]
    if partial:
        print('AVISO: marcos com parcela sem preco (custo e so um piso):', partial)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Gera docs/assets/logbook-metrics.json (ver o cabecalho do arquivo).')
    parser.add_argument('--reprice', action='store_true', help='corrige o custo de marcos gravados (ver cabecalho)')
    parser.add_argument('--enrich', action='store_true', help='migra marcos gravados antes do corte por modelo/TTL')
    parser.add_argument('--dry-run', action='store_true', help='com --enrich, so imprime o relatorio')
    parser.add_argument('--recount', action='store_true', help='recontar palavras e linhas de todos os marcos')
    parser.add_argument('--note', help='com --reprice, o motivo, gravado em cada registro de repricings')
    args = parser.parse_args()
    if args.dry_run and not args.enrich:
        parser.error('--dry-run so faz sentido com --enrich')
    if sum([args.reprice, args.enrich]) > 1:
        parser.error('--reprice e --enrich sao mutuamente exclusivos')
    if args.recount and (args.reprice or args.enrich):
        parser.error('--recount so vale numa execucao normal')
    if args.note and not args.reprice:
        parser.error('--note so vale com --reprice')
    if args.reprice:
        reprice(args.note)
    elif args.enrich:
        sys.exit(enrich(args.dry_run))
    else:
        main(recount=args.recount)
