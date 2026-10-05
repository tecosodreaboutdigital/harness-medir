# -*- coding: utf-8 -*-
# Gera toolkit.json, a forma legivel por maquina da mesma curadoria que
# TOOLS.md e sources/inventory.md ja carregam para leitura humana. Nasceu
# de um achado de leitor real: um agente (Codex CLI, Antigravity, Claude
# Code, Cursor) solto direto num projeto de terceiro, apontado so para a
# URL deste repositorio, nao consegue montar sozinho "quais skills
# existem, qual o papel de cada uma, como eu baixo para o meu projeto"
# sem cruzar TOOLS.md, sources/inventory.md e harness-toolkit.html a mao.
#
# Escopo deliberado, v1: so os Agent Skills de fato instalados em
# .claude/skills/ (as nove colecoes de terceiro mais as duas skills
# proprias, intake-briefing e milestone-loc-tokens-ai-ledger). NAO cobre
# toda ferramenta citada em
# sources/inventory.md (Semgrep, Stryker, LangGraph e outras sao
# ferramentas de software convencionais, sem um "comando de instalacao
# de skill" uniforme, forcar isso no mesmo schema seria inventar um fato
# que a fonte nao sustenta). Templates do playbook (NEXT-STEPS.md item 3)
# entram aqui como kind:"template" quando esse item for consolidado, ver
# build/README.md.
#
# Nunca editado a mao: TOOLS.md e sources/inventory.md sao a fonte da
# verdade, este script deriva o resto. Mesma disciplina de
# generate_logbook_metrics.py.
#
# Uso: python build/generate_toolkit_manifest.py
#      python build/generate_toolkit_manifest.py --check   (nao escreve,
#      sai com codigo 1 se o toolkit.json commitado estiver desatualizado
#      em relacao a TOOLS.md/sources/inventory.md agora)
import hashlib
import json
import os
import re
import sys
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_MD = os.path.join(ROOT, 'TOOLS.md')
INVENTORY_MD = os.path.join(ROOT, 'sources', 'inventory.md')
PLAYBOOK_README = os.path.join(ROOT, 'playbook', 'README.md')
PLAYBOOK_BODY_EN = os.path.join(ROOT, 'build', 'body_playbook_en.html')
OUT_PATH = os.path.join(ROOT, 'toolkit.json')
UPSTREAM_PATH = os.path.join(ROOT, 'sources', 'upstream.json')

MEDIR_STEPS = ['map', 'equip', 'delegate', 'inspect', 'reinforce', 'secure', 'govern']

# Convencao .agents/skills/, lida na documentacao de cada ferramenta em 5 de
# outubro de 2026 (build/check_upstream.py nao cobre isto: sao paginas de
# documentacao, nao repositorios). "evidence" diz de onde saiu cada linha.
AGENTS_SKILLS_CONVENTION = {
    'project_path': '.agents/skills/<skill-id>/',
    'user_path': '~/.agents/skills/<skill-id>/',
    'verified_at': '2026-10-05',
    'read_by': [
        {'tool': 'Cursor', 'evidence': 'https://cursor.com/docs/skills (project .agents/skills/ and user ~/.agents/skills/)'},
        {'tool': 'Codex CLI', 'evidence': 'https://developers.openai.com/codex/skills (scans .agents/skills from the working directory up to the repository root)'},
        {'tool': 'Gemini CLI', 'evidence': 'https://geminicli.com/docs/cli/skills/ (.agents/skills/ alias, ahead of .gemini/skills/ in the same tier)'},
        {'tool': 'OpenCode', 'evidence': 'https://opencode.ai/docs/skills/ (.agents/skills/ and ~/.agents/skills/; it also reads .claude/skills/ and ~/.claude/skills/)'},
        {'tool': 'Mistral Vibe, OpenClaw', 'evidence': 'arXiv:2609.00006 section 12.5 and Table 10 (source-code study, July 2026)'},
    ],
    'not_reverified': [
        {'tool': 'Google Antigravity', 'reason': 'its documentation page opened on 2026-10-05 but exposed no text this check could read; the path was last confirmed on 2026-08-31'},
    ],
    'note': ('A convention several tools converge on, not a standard any of them guarantees. '
             'Claude Code reads .claude/skills/ and ~/.claude/skills/ instead.'),
}

INSTALL_NOTE = (
    "Clone the origin repository, locate this skill's own folder inside it "
    "(this project has not independently verified the exact internal path "
    "for every origin repo), and copy that folder to the target path for "
    "your tool. Check AGENTS.md at this project's root before installing: "
    "confirm the origin is still current first."
)


def load_upstream():
    """sources/upstream.json, escrito por build/check_upstream.py. Opcional:
    sem ele o manifesto sai como antes, sem os campos de proveniencia."""
    if not os.path.exists(UPSTREAM_PATH):
        return None
    return json.loads(read(UPSTREAM_PATH))


def repo_record(upstream, origin_url):
    """Acha o registro do repositorio de uma origem, por nome (owner/repo)."""
    if not upstream:
        return None
    slug = re.sub(r'^https?://github\.com/', '', origin_url).strip('/').removesuffix('.git').lower()
    for rid, rec in upstream['repos'].items():
        if rec.get('repo', '').lower() == slug:
            return rec
    return None


def provenance(upstream, origin_url, skill_ids, own):
    rec = repo_record(upstream, origin_url)
    if not rec or 'error' in rec:
        return {}
    spdx = rec.get('licence_spdx')
    has_file = bool(rec.get('licence_file'))
    declared = rec.get('licence_declared_in_readme')
    if has_file and spdx and spdx != 'NOASSERTION':
        licence, note = spdx, None
    elif has_file:
        licence, note = 'see LICENSE file (SPDX id not detected)', None
    elif declared:
        licence = declared
        note = 'declared in the README, no LICENSE file in the repository: a weaker grant than a licence file'
    else:
        licence = None
        note = 'no licence file and none declared in the README: by default all rights stay with the author'
    counts = {}
    audit = {'contains_scripts': False, 'network_calls_in_scripts': False, 'registers_hooks': False,
             'declares_dependencies': False, 'script_files': [], 'network_flagged_files': []}
    for sk in skill_ids:
        res = (upstream.get('skills') or {}).get(sk)
        if not res:
            continue
        counts[res['status']] = counts.get(res['status'], 0) + 1
        a = res.get('audit') or {}
        audit['contains_scripts'] |= a.get('contains_scripts', False)
        audit['network_calls_in_scripts'] |= bool(a.get('network_calls_in_scripts'))
        audit['registers_hooks'] |= a.get('registers_hooks', False)
        audit['declares_dependencies'] |= a.get('declares_dependencies', False)
        audit['script_files'] += ['%s: %s' % (sk, f) for f in a.get('script_files', [])]
        audit['network_flagged_files'] += ['%s: %s' % (sk, f) for f in a.get('network_calls_in_scripts', [])]
    owner = rec['repo'].split('/')[0].lower()
    out = {
        'verified_at': upstream['checked_at'][:10],
        'upstream': {
            'repo': rec['repo'], 'archived': rec['archived'], 'head_sha': rec['head_sha'],
            'head_date': (rec.get('head_date') or '')[:10], 'stars': rec.get('stars'),
        },
        'licence': licence,
        'licence_file': has_file,
        'trust_tier': 'own' if owner == 'tecosodreaboutdigital' else 'community',
        'pinned_ref': None,
        'pinned_ref_note': ('The installed copies never recorded the commit they came from. Instead, each '
                            "skill's SKILL.md was compared with the origin's default branch on verified_at: "
                            'see installed_vs_upstream.'),
        'installed_vs_upstream': counts,
        'audit': dict(audit, method=('scan of the installed copy by build/check_upstream.py on verified_at: '
                                     'it finds signals (scripts, network calls inside scripts, hook registration, '
                                     'dependency manifests), it does not prove their absence. A flagged file '
                                     'still needs a person to read it.')),
    }
    if note:
        out['licence_note'] = note
    return out


def read(path):
    with open(path, encoding='utf-8') as fh:
        return fh.read()


def extract_section(text, start_heading, end_heading=None):
    start = text.index(start_heading) + len(start_heading)
    if end_heading:
        end = text.index(end_heading, start)
        return text[start:end]
    return text[start:]


def extract_licence(*texts):
    for text in texts:
        m = re.search(r'Apache[- ]2\.0|Apache 2\.0|MIT', text)
        if m:
            return m.group(0).replace(' ', '-') if 'Apache' in m.group(0) else m.group(0)
    return None


def parse_collections_table(tools_text):
    """Le a tabela 'Third-party collections installed' de TOOLS.md."""
    section = extract_section(tools_text, '## Third-party collections installed', '## The thirty-six skills')
    rows = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) != 4 or cells[0] == 'Collection':
            continue
        name, origin_cell, count, why = cells
        m = re.search(r'\[([^\]]+)\]\(([^)]+)\)', origin_cell)
        origin_url = m.group(2) if m else origin_cell
        rows.append({
            'name': name,
            'origin': origin_url,
            'skills_installed_text': count,
            'role': why,
        })
    return rows


def parse_skill_names_by_collection(tools_text, collection_names):
    """Para cada nome de colecao ja conhecido (da tabela acima), acha o
    paragrafo correspondente em 'The thirty-six skills, by collection'
    e extrai so os identificadores de skill individuais, descartando
    prosa de ressalva que segue no mesmo paragrafo."""
    section = extract_section(tools_text, '## The thirty-six skills, by collection', '## The project')
    result = {}
    for name in collection_names:
        label = '**%s:**' % name
        idx = section.find(label)
        if idx == -1:
            result[name] = []
            continue
        after = section[idx + len(label):]
        # Fim de frase real = ponto seguido de espaco/quebra de linha/fim
        # de texto, nao qualquer ponto (evita cortar em "SKILL.md").
        m = re.search(r'\.(?=\s|$)', after)
        segment = after[:m.start()] if m else after
        # remove um nivel de parenteses (ressalvas tipo o caso c4-model)
        segment = re.sub(r'\([^()]*\)', '', segment)
        items = []
        for raw in segment.split(','):
            token = raw.strip().strip('`').strip()
            if token and ' ' not in token:
                items.append(token)
        result[name] = items
    return result


def parse_medir_steps(inventory_text, collection_names):
    """Le a tabela 'Tools and skills' de sources/inventory.md e casa cada
    colecao conhecida contra o campo Resource, por substring, para achar
    o passo do MEDIR que ela fundamenta."""
    section = extract_section(inventory_text, '## Tools and skills', '## Part 3 and 4 research')
    rows = []
    for line in section.splitlines():
        line = line.strip()
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) < 4 or cells[0] == 'Status':
            continue
        status, step, resource = cells[0], cells[1], cells[2]
        rows.append((status, step, resource))
    result = {}
    for name in collection_names:
        key = name.lower()
        match = next((r for r in rows if key in r[2].lower()), None)
        result[name] = match[1].lower() if match else None
    return result


# Every skill this project has produced for itself, not installed from a
# third party. Adding a second one (13-14 September 2026) turned what was a
# single hardcoded function into this list: each entry still gets its
# origin URL parsed out of TOOLS.md's own prose, same discipline as before,
# rather than trusting a URL typed twice in two different files.
OWN_SKILLS = [
    {
        'id': 'intake-briefing',
        'role': ('Runs a structured interview before any AI build, to decide whether the task '
                 'should be automated, what autonomy tier it should operate in, and what the '
                 'resulting task contract is.'),
        'medir_step': 'map',
        'url_pattern': r'https://github\.com/\S+?/intake-briefing',
        'default_origin': 'https://github.com/tecosodreaboutdigital/intake-briefing',
        'plugin_slug': 'intake-briefing',
        'verified': "31 August 2026, against each vendor's own documentation. Snapshot, not live status.",
    },
    {
        'id': 'milestone-loc-tokens-ai-ledger',
        'role': ("Generates a self-hosted, static HTML dashboard tracking a project's lines of "
                 'code, words, and LLM token cost per git commit, against a dated, multi-source, '
                 'editable price ledger. Generalises this project\'s own diary engine.'),
        'medir_step': 'inspect',
        'url_pattern': r'https://github\.com/\S+?/milestone-loc-tokens-ai-ledger',
        'default_origin': 'https://github.com/tecosodreaboutdigital/milestone-loc-tokens-ai-ledger',
        'plugin_slug': 'milestone-loc-tokens-ai-ledger',
        'verified': "13 September 2026, against each vendor's own documentation. Snapshot, not live status.",
    },
]


def parse_own_skills(tools_text, upstream=None):
    section = extract_section(tools_text, "## The project's own skills", '## Audit before installing')
    entries = []
    for spec in OWN_SKILLS:
        m = re.search(spec['url_pattern'], section)
        origin = m.group(0).rstrip('.,)') if m else spec['default_origin']
        prov = provenance(upstream, origin, [spec['id']], own=True)
        if prov:
            prov.pop('licence', None)  # as skills proprias sao MIT, ja declarado abaixo
        entries.append({
            'id': spec['id'],
            'kind': 'own_skill',
            'name': spec['id'],
            'role': spec['role'],
            'medir_step': spec['medir_step'],
            'origin': origin,
            'licence': 'MIT',
            'status': 'installed',
            'skills': [spec['id']],
            'install': {
                'personal': 'git clone %s.git ~/.claude/skills/%s' % (origin, spec['id']),
                'agents_skills_convention': 'git clone %s.git .agents/skills/%s' % (origin, spec['id']),
                'claude_code_plugin': (
                    '/plugin marketplace add tecosodreaboutdigital/%s\n'
                    '/plugin install %s@%s' % (spec['plugin_slug'], spec['plugin_slug'], spec['plugin_slug'])
                ),
                'verified': spec['verified'],
            },
            **prov,
        })
    return entries


def parse_playbook_templates(readme_text, body_en_text):
    """Le a tabela de playbook/README.md (Template | File | Grounded in) e
    a tabela equivalente de build/body_playbook_en.html (Template | Grounded
    in | What it answers), na mesma ordem de linha, e casa as duas por
    indice, nao por nome, ja que os dois arquivos sao mantidos juntos por
    este projeto e a ordem e garantida."""
    readme_rows = []
    for line in readme_text.splitlines():
        line = line.strip()
        if not line.startswith('|') or line.startswith('|---'):
            continue
        cells = [c.strip() for c in line.strip('|').split('|')]
        if len(cells) != 3 or cells[0] == 'Template':
            continue
        name, file_cell, grounded_in = cells
        file_name = file_cell.strip('`')
        readme_rows.append((name, file_name, grounded_in))

    body_rows = []
    for line in body_en_text.splitlines():
        line = line.strip()
        if not line.startswith('<tr><td>') or 'playbook/' not in line:
            continue
        cells = re.findall(r'<td>(.*?)</td>', line)
        if len(cells) != 3:
            continue
        name = re.sub(r'<[^>]+>', '', cells[0])
        role = re.sub(r'<[^>]+>', '', cells[2])
        body_rows.append((name, role))

    entries = []
    for i, (name, file_name, grounded_in) in enumerate(readme_rows):
        role = body_rows[i][1] if i < len(body_rows) else None
        entries.append({
            'id': slugify(file_name.rsplit('.', 1)[0]),
            'kind': 'template',
            'name': name,
            'role': role,
            'grounded_in': grounded_in,
            'path': 'playbook/%s' % file_name,
            'status': 'available',
        })
    return entries


def build_entries(tools_text, inventory_text, playbook_readme_text=None, playbook_body_text=None, upstream=None):
    collections = parse_collections_table(tools_text)
    names = [c['name'] for c in collections]
    skills_by_name = parse_skill_names_by_collection(tools_text, names)
    medir_by_name = parse_medir_steps(inventory_text, names)

    entries = []
    for c in collections:
        licence = extract_licence(c['role']) or 'MIT or Apache-2.0 (see TOOLS.md overview)'
        skill_ids = skills_by_name.get(c['name']) or [slugify(c['name'])]
        prov = provenance(upstream, c['origin'], skill_ids, own=False)
        if prov:
            licence = prov.pop('licence') or 'none'
        entries.append({
            'id': slugify(c['name']),
            'kind': 'collection',
            'name': c['name'],
            'role': c['role'],
            'medir_step': medir_by_name.get(c['name']),
            'origin': c['origin'],
            'licence': licence,
            'status': 'installed',
            'skills_installed_text': c['skills_installed_text'],
            'skills': skill_ids,
            'install': {
                'origin_clone': 'git clone %s' % c['origin'],
                'claude_code_personal': '~/.claude/skills/<skill-id>/',
                'claude_code_project': '.claude/skills/<skill-id>/',
                'agents_skills_convention': AGENTS_SKILLS_CONVENTION['project_path'],
                'note': INSTALL_NOTE,
            },
            **prov,
        })
    entries.extend(parse_own_skills(tools_text, upstream))
    if playbook_readme_text is not None and playbook_body_text is not None:
        entries.extend(parse_playbook_templates(playbook_readme_text, playbook_body_text))
    return entries


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def source_hash(tools_text, inventory_text, playbook_readme_text=None, upstream_text=None):
    collections_block = extract_section(tools_text, '## Third-party collections installed', '## Audit before installing')
    tools_table_block = extract_section(inventory_text, '## Tools and skills', '## Part 3 and 4 research')
    digest = hashlib.sha256()
    digest.update(collections_block.encode('utf-8'))
    digest.update(tools_table_block.encode('utf-8'))
    if playbook_readme_text is not None:
        digest.update(playbook_readme_text.encode('utf-8'))
    if upstream_text is not None:
        digest.update(upstream_text.encode('utf-8'))
    return digest.hexdigest()


def build_manifest():
    tools_text = read(TOOLS_MD)
    inventory_text = read(INVENTORY_MD)
    playbook_readme_text = read(PLAYBOOK_README) if os.path.exists(PLAYBOOK_README) else None
    playbook_body_text = read(PLAYBOOK_BODY_EN) if os.path.exists(PLAYBOOK_BODY_EN) else None
    upstream = load_upstream()
    upstream_text = read(UPSTREAM_PATH) if upstream else None
    return {
        'generated_by': 'build/generate_toolkit_manifest.py',
        'generated_at': date.today().isoformat(),
        'derived_from': ['TOOLS.md', 'sources/inventory.md', 'sources/upstream.json', 'playbook/README.md', 'README.md'],
        'agents_skills_convention': AGENTS_SKILLS_CONVENTION,
        'scope_note': (
            "Agent Skills actually installed in this project's .claude/skills/, plus this "
            'project\'s own operational artefacts (kind: "own_skill" for intake-briefing and '
            'milestone-loc-tokens-ai-ledger, "template" for the nine playbook files, see '
            'playbook/README.md). Does not '
            'cover every tool cited in sources/inventory.md: some of those are conventional '
            'software (a static analyser, an orchestration library), not an installable Agent '
            'Skill, and forcing them into this schema would assert an install path this '
            'project never verified.'
        ),
        'verification_note': (
            'This file is a snapshot, generated on the date above. Before installing anything '
            "listed here, follow AGENTS.md's protocol: fetch the origin URL and check "
            'whether it is still current. Do not present this file as live state. '
            'Per-entry verified_at, upstream and installed_vs_upstream come from '
            'sources/upstream.json, which build/check_upstream.py rewrites from the GitHub API.'
        ),
        'medir_steps': MEDIR_STEPS,
        'source_hash': source_hash(tools_text, inventory_text, playbook_readme_text, upstream_text),
        'entries': build_entries(tools_text, inventory_text, playbook_readme_text, playbook_body_text, upstream),
    }


def main():
    check_only = '--check' in sys.argv
    manifest = build_manifest()
    if check_only:
        if not os.path.exists(OUT_PATH):
            print('toolkit.json does not exist yet, run without --check first.')
            sys.exit(1)
        committed = json.loads(read(OUT_PATH))
        if committed.get('source_hash') != manifest['source_hash']:
            print('toolkit.json is stale: TOOLS.md, sources/inventory.md, sources/upstream.json or the playbook changed since it was '
                  'last generated. Run python build/generate_toolkit_manifest.py to refresh it.')
            sys.exit(1)
        print('toolkit.json: up to date.')
        sys.exit(0)

    with open(OUT_PATH, 'w', encoding='utf-8') as fh:
        json.dump(manifest, fh, indent=2, ensure_ascii=False)
        fh.write('\n')
    print('wrote %s (%d entries)' % (OUT_PATH, len(manifest['entries'])))


if __name__ == '__main__':
    main()
