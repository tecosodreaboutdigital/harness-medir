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
# .claude/skills/ (as dez colecoes de terceiro mais o skill proprio,
# intake-briefing). NAO cobre toda ferramenta citada em
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
OUT_PATH = os.path.join(ROOT, 'toolkit.json')

MEDIR_STEPS = ['map', 'equip', 'delegate', 'inspect', 'reinforce', 'secure', 'govern']

INSTALL_NOTE = (
    "Clone the origin repository, locate this skill's own folder inside it "
    "(this project has not independently verified the exact internal path "
    "for every origin repo), and copy that folder to the target path for "
    "your tool. Check AGENTS.md at this project's root before installing: "
    "confirm the origin is still current first."
)


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
    section = extract_section(tools_text, '## Third-party collections installed', '## The thirty-seven skills')
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
    paragrafo correspondente em 'The thirty-seven skills, by collection'
    e extrai so os identificadores de skill individuais, descartando
    prosa de ressalva que segue no mesmo paragrafo."""
    section = extract_section(tools_text, '## The thirty-seven skills, by collection', '## The project')
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


def parse_own_skill(tools_text):
    section = extract_section(tools_text, '## The project\'s own skill', '## Audit before installing')
    m = re.search(r'https://github\.com/\S+?/intake-briefing', section)
    origin = m.group(0).rstrip('.,)') if m else 'https://github.com/tecosodreaboutdigital/intake-briefing'
    return {
        'id': 'intake-briefing',
        'kind': 'own_skill',
        'name': 'intake-briefing',
        'role': ('Runs a structured interview before any AI build, to decide whether the task '
                 'should be automated, what autonomy tier it should operate in, and what the '
                 'resulting task contract is.'),
        'medir_step': 'map',
        'origin': origin,
        'licence': 'MIT',
        'status': 'installed',
        'skills': ['intake-briefing'],
        'install': {
            'personal': 'git clone %s.git ~/.claude/skills/intake-briefing' % origin,
            'cursor_codex_antigravity': 'git clone %s.git .agents/skills/intake-briefing' % origin,
            'claude_code_plugin': (
                '/plugin marketplace add tecosodreaboutdigital/intake-briefing\n'
                '/plugin install intake-briefing@intake-briefing'
            ),
            'verified': "31 August 2026, against each vendor's own documentation. Snapshot, not live status.",
        },
    }


def build_entries(tools_text, inventory_text):
    collections = parse_collections_table(tools_text)
    names = [c['name'] for c in collections]
    skills_by_name = parse_skill_names_by_collection(tools_text, names)
    medir_by_name = parse_medir_steps(inventory_text, names)

    entries = []
    for c in collections:
        licence = extract_licence(c['role']) or 'MIT or Apache-2.0 (see TOOLS.md overview)'
        skill_ids = skills_by_name.get(c['name']) or [slugify(c['name'])]
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
                'cursor_codex_antigravity': '.agents/skills/<skill-id>/',
                'note': INSTALL_NOTE,
            },
        })
    entries.append(parse_own_skill(tools_text))
    return entries


def slugify(name):
    return re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')


def source_hash(tools_text, inventory_text):
    collections_block = extract_section(tools_text, '## Third-party collections installed', '## Audit before installing')
    tools_table_block = extract_section(inventory_text, '## Tools and skills', '## Part 3 and 4 research')
    digest = hashlib.sha256()
    digest.update(collections_block.encode('utf-8'))
    digest.update(tools_table_block.encode('utf-8'))
    return digest.hexdigest()


def build_manifest():
    tools_text = read(TOOLS_MD)
    inventory_text = read(INVENTORY_MD)
    return {
        'generated_by': 'build/generate_toolkit_manifest.py',
        'generated_at': date.today().isoformat(),
        'derived_from': ['TOOLS.md', 'sources/inventory.md', 'README.md'],
        'scope_note': (
            "Agent Skills actually installed in this project's .claude/skills/, plus this "
            'project\'s own operational artefacts (kind: "own_skill", and "template" once '
            'NEXT-STEPS.md item 3, the playbook, is consolidated). Does not cover every tool '
            'cited in sources/inventory.md: some of those are conventional software (a static '
            'analyser, an orchestration library), not an installable Agent Skill, and forcing '
            'them into this schema would assert an install path this project never verified.'
        ),
        'verification_note': (
            'This file is a snapshot, generated on the date above. Before installing anything '
            "listed here, follow AGENTS.md's protocol: fetch the origin URL and check "
            'whether it is still current. Do not present this file as live state.'
        ),
        'medir_steps': MEDIR_STEPS,
        'source_hash': source_hash(tools_text, inventory_text),
        'entries': build_entries(tools_text, inventory_text),
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
            print('toolkit.json is stale: TOOLS.md or sources/inventory.md changed since it was '
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
