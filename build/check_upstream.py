# -*- coding: utf-8 -*-
# Consulta ao vivo a origem de cada skill ou ferramenta curada por este
# projeto e grava o resultado, datado, em sources/upstream.json. E o
# passo 2 e 3 do protocolo do AGENTS.md (buscar a origem, ver se esta
# arquivada, quando foi o ultimo commit) feito por script, para que o
# manifesto toolkit.json carregue o que foi lido e quando, e nao so o
# que alguem escreveu uma vez.
#
# O que le, por repositorio (API do GitHub, via `gh api`, precisa de `gh`
# autenticado): arquivado ou nao, licenca declarada (SPDX), se existe
# arquivo de licenca, branch padrao, commit e data do HEAD, ultimo push,
# estrelas. Para cada skill instalada em .claude/skills/, compara o
# SKILL.md local com o do HEAD da origem. As copias locais nunca
# registraram o commit de que vieram, entao esta comparacao e a unica
# prova de proveniencia possivel: igual ao HEAD de hoje, ou diferente.
#
# Uso:
#   python build/check_upstream.py            consulta e grava sources/upstream.json
#   python build/check_upstream.py --repos    so os repositorios (sem comparar skills)
# Nunca afirma estado de uma origem que nao conseguiu ler: erro de rede ou
# de permissao vira "error" no registro, nao um valor inventado.
import base64
import hashlib
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, 'build'))
OUT = os.path.join(ROOT, 'sources', 'upstream.json')
SKILLS_DIR = os.path.join(ROOT, '.claude', 'skills')

# id usado no toolkit.json (ou nome curto) -> owner/repo. As colecoes
# instaladas vem primeiro; depois as ferramentas citadas so no guia.
REPOS = {
    'superpowers': 'obra/superpowers',
    'mattpocock-skills': 'mattpocock/skills',
    'c4-skills': 'muthub-ai/c4-skills',
    'karpathy-inspired-guide': 'multica-ai/andrej-karpathy-skills',
    'ai-slop-cleaner': 'yeachan-heo/oh-my-claudecode',
    'humanizer': 'blader/humanizer',
    'agent-skills-for-context-engineering': 'muratcankoylan/Agent-Skills-for-Context-Engineering',
    'ai-act-skill': 'morellid/ai-act-skill',
    'threat-modeling': 'rjmurillo/ai-agents',
    'intake-briefing': 'tecosodreaboutdigital/intake-briefing',
    'milestone-loc-tokens-ai-ledger': 'tecosodreaboutdigital/milestone-loc-tokens-ai-ledger',
    # citadas so no guia compacto
    'holdfast': 'AndreAlmeidaDC/holdfast',
    'planning-with-files': 'OthmanAdi/planning-with-files',
    'sensors-cli': 'birgitta410/sensors-cli',
    'autoresearch': 'karpathy/autoresearch',
    'deepseek-harness': 'deepseek-ai/deepseek-harness',
    'langgraph': 'langchain-ai/langgraph',
    'agent-governance-toolkit': 'microsoft/agent-governance-toolkit',
    'presidio': 'data-privacy-stack/presidio',
    'spec-kit': 'github/spec-kit',
    'dependency-cruiser': 'sverweij/dependency-cruiser',
    'semgrep': 'semgrep/semgrep',
    'rekor': 'sigstore/rekor',
    'spire': 'spiffe/spire',
    'langfuse': 'langfuse/langfuse',
    'awesome-harness-engineering': 'ai-boost/awesome-harness-engineering',
}
# skills cuja pasta de origem tem outro nome
ALIASES = {'c4-model': ['c4designer']}


def gh(path, raw=False):
    cmd = ['gh', 'api', path]
    if raw:
        cmd = ['gh', 'api', '-H', 'Accept: application/vnd.github.raw', path]
    p = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
    if p.returncode != 0:
        return None, (p.stderr or p.stdout).strip().splitlines()[-1][:160] if (p.stderr or p.stdout).strip() else 'error'
    if raw:
        return p.stdout, None
    return json.loads(p.stdout), None


def repo_facts(slug):
    meta, err = gh('repos/' + slug)
    if meta is None:
        return {'repo': slug, 'error': err}
    head, herr = gh('repos/%s/commits/%s' % (slug, meta['default_branch']))
    lic_file, _ = gh('repos/%s/license' % slug)
    readme, _ = gh('repos/%s/readme' % slug, raw=True)
    declared = None
    if readme:
        m = re.search(r'(?im)^#{1,3}\s*licen[sc]es?\s*$\s+(\S[^\n]{0,80})', readme)
        declared = m.group(1).strip() if m else None
    return {
        'repo': meta['full_name'],
        'archived': meta['archived'],
        'disabled': meta.get('disabled', False),
        'default_branch': meta['default_branch'],
        'licence_spdx': (meta.get('license') or {}).get('spdx_id'),
        'licence_file': (lic_file or {}).get('path') if lic_file else None,
        'licence_declared_in_readme': declared,
        'head_sha': head['sha'] if head else None,
        'head_date': head['commit']['committer']['date'] if head else None,
        'pushed_at': meta.get('pushed_at'),
        'stars': meta.get('stargazers_count'),
        'html_url': meta['html_url'],
    }


def norm(text):
    return '\n'.join(l.rstrip() for l in text.replace('\r\n', '\n').split('\n')).strip()


def compare_skill(slug, branch, skill, tree):
    if tree is None:
        return {'status': 'not_compared', 'reason': 'tree unavailable'}
    local = os.path.join(SKILLS_DIR, skill, 'SKILL.md')
    if not os.path.exists(local):
        return {'status': 'not_compared', 'reason': 'no local SKILL.md'}
    names = [skill] + ALIASES.get(skill, [])
    cands = [t['path'] for t in tree['tree'] if t['type'] == 'blob' and t['path'].endswith('/SKILL.md')
             and t['path'].split('/')[-2] in names]
    if not cands and any(t['path'] == 'SKILL.md' for t in tree['tree']):
        cands = ['SKILL.md']
    if not cands:
        why = 'tree truncated' if tree.get('truncated') else 'no SKILL.md under that name upstream'
        return {'status': 'not_found_upstream', 'reason': why}
    cands.sort(key=lambda p: (len(p), p))
    path = cands[0]
    up, err = gh('repos/%s/contents/%s?ref=%s' % (slug, path, branch), raw=True)
    if up is None:
        return {'status': 'not_compared', 'reason': err, 'path': path}
    a = norm(open(local, encoding='utf-8', errors='replace').read())
    b = norm(up)
    return {'status': 'identical' if a == b else 'differs', 'path': path,
            'local_sha256': hashlib.sha256(a.encode()).hexdigest()[:16],
            'upstream_sha256': hashlib.sha256(b.encode()).hexdigest()[:16], 'candidates': len(cands)}


SCRIPT_EXT = ('.py', '.sh', '.js', '.mjs', '.cjs', '.ts', '.ps1', '.bat', '.rb')
NET_RX = re.compile(r'urllib|requests\.(get|post|put)|http\.client|httpx|aiohttp|fetch\(|\bcurl\b|\bwget\b|socket\.|axios|XMLHttpRequest')
DEP_FILES = ('requirements.txt', 'package.json', 'pyproject.toml', 'Pipfile', 'Gemfile', 'go.mod', 'Cargo.toml')


def audit_local(skill):
    """Varredura da copia instalada. E um sensor, nao uma auditoria: acha
    sinais (scripts, chamadas de rede em script, registro de hook,
    manifesto de dependencia), nao prova a ausencia deles."""
    root = os.path.join(SKILLS_DIR, skill)
    scripts, net, hooks, deps = [], [], [], []
    for dp, dn, fn in os.walk(root):
        if '.git' in dp.split(os.sep):
            continue
        for f in fn:
            rel = os.path.relpath(os.path.join(dp, f), root).replace(os.sep, '/')
            low = f.lower()
            if low.endswith(SCRIPT_EXT):
                scripts.append(rel)
                try:
                    if NET_RX.search(open(os.path.join(dp, f), encoding='utf-8', errors='replace').read()):
                        net.append(rel)
                except OSError:
                    pass
            if f in DEP_FILES:
                deps.append(rel)
            if low in ('hooks.json', 'settings.json') or '/hooks/' in '/' + rel:
                hooks.append(rel)
    skill_md = os.path.join(root, 'SKILL.md')
    if os.path.exists(skill_md):
        head = open(skill_md, encoding='utf-8', errors='replace').read(2000)
        if re.search(r'(?m)^hooks\s*:', head):
            hooks.append('SKILL.md (frontmatter)')
    return {'contains_scripts': bool(scripts), 'script_files': scripts[:12], 'network_calls_in_scripts': net[:12],
            'registers_hooks': bool(hooks), 'hook_files': hooks[:12], 'declares_dependencies': bool(deps), 'dependency_files': deps[:12]}


def main():
    only_repos = '--repos' in sys.argv
    now = datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%MZ')
    out = {'checked_at': now, 'method': 'GitHub API through gh, read live on checked_at',
           'repos': {}, 'skills': {}}
    for rid, slug in REPOS.items():
        out['repos'][rid] = repo_facts(slug)
        r = out['repos'][rid]
        print('%-40s %s' % (rid, ('ERROR ' + r['error']) if 'error' in r else
                            'archived=%s head=%s lic=%s file=%s' % (r['archived'], (r['head_date'] or '')[:10], r['licence_spdx'], bool(r['licence_file']))))
    if not only_repos:
        import generate_toolkit_manifest as g
        tools = g.read(g.TOOLS_MD)
        cols = g.parse_collections_table(tools)
        by = g.parse_skill_names_by_collection(tools, [c['name'] for c in cols])
        origin_to_id = {v.lower(): k for k, v in REPOS.items()}
        trees = {}
        for c in cols:
            slug = re.sub(r'^https://github.com/', '', c['origin']).strip('/')
            rid = origin_to_id.get(slug.lower())
            if not rid or 'error' in out['repos'].get(rid, {}):
                continue
            r = out['repos'][rid]
            tree, _ = gh('repos/%s/git/trees/%s?recursive=1' % (slug, r['head_sha']))
            for sk in by.get(c['name'], []):
                out['skills'][sk] = dict(collection=rid, **compare_skill(slug, r['default_branch'], sk, tree), audit=audit_local(sk))
        for sk, res in sorted(out['skills'].items()):
            print('  %-34s %s' % (sk, res['status']))
    for own in ('intake-briefing', 'milestone-loc-tokens-ai-ledger'):
        if own in out['repos'] and 'error' not in out['repos'][own] and own not in out['skills'] and not only_repos:
            r = out['repos'][own]
            tree, _ = gh('repos/%s/git/trees/%s?recursive=1' % (r['repo'], r['head_sha']))
            out['skills'][own] = dict(collection=own, **compare_skill(r['repo'], r['default_branch'], own, tree), audit=audit_local(own))
            print('  %-34s %s' % (own, out['skills'][own]['status']))
    with open(OUT, 'w', encoding='utf-8', newline='\n') as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    print('gravado:', os.path.relpath(OUT, ROOT))


if __name__ == '__main__':
    main()
