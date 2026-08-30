# -*- coding: utf-8 -*-
import unicodedata, re, os

OUT = '/mnt/user-data/outputs'
pt = open(os.path.join(OUT, 'harness-p1-pt.html'), encoding='utf-8').read()
shell = pt[:pt.index('<main class="page">')]
shell = shell.replace('<html lang="pt-BR">', '<html lang="en">')
shell = shell.replace('<title>O melhor modelo do mundo dentro de uma empresa sem processo | Parte 1</title>',
                      '<title>The best model in the world inside a company with no process | Part 1</title>')

W = 'https://en.wikipedia.org/wiki/'
G = [
("g-agent","agent","A system that combines a language model with tools, memory and rules to carry out multi-step tasks, deciding at each step what to do next. The working equation is agent equals model plus harness.","",""),
("g-agentsmd","AGENTS.md","A file at the root of a project that tells the agent where things are, what the conventions are and what not to do. Good practice treats it as a short index, not a manual.","Community specification","https://agents.md/"),
("g-andon","andon","A visual or audible signal that shows process status and halts the line to call for immediate help when a problem appears. With agents, it is escalation to a human with the context attached.","Toyota Production System",W+"Andon_(manufacturing)"),
("g-append","append-only log","A record in which nothing can be altered or deleted, only added at the end. It is the technical basis of any trustworthy audit trail, and what makes an execution reconstructable, replayable and reversible.","",""),
("g-ashby","Ashby's Law","The law of requisite variety: a regulator can only control a system if it has at least as much variety as the system it governs. It explains why standardising task types makes agent control achievable.","W. Ross Ashby, 1956",W+"Variety_(cybernetics)"),
("g-context","context engineering","The discipline of deciding what enters the model's field of view on each run: which documents, rules, examples and prior results. It precedes the harness and keeps operating inside it.","Birgitta Bockeler's formulation for coding agents","https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html"),
("g-chart","control chart","A statistical process control graph that separates ordinary variation from a real change, so you act only when something has genuinely shifted.","Walter Shewhart, Bell Labs, 1920s",W+"Statistical_process_control"),
("g-cyb","cybernetics","The science of control and communication in systems, biological or artificial. It studies how a system holds course toward a goal through anticipation and feedback.","Norbert Wiener, 1948",W+"Cybernetics"),
("g-deming","Deming, W. Edwards","American statistician who took Shewhart's cycle to Japan in the 1950s and turned it into the foundation of modern quality management.","1900 to 1993",W+"W._Edwards_Deming"),
("g-dmaic","DMAIC","Define, measure, analyse, improve, control. The structured cycle for running Six Sigma projects, and the closest methodological relative of MEDIR.","Motorola, 1980s; consolidated by General Electric in the 1990s",""),
("g-gemba","gemba","The real place where work happens. Going to the gemba means observing the process directly instead of discussing the report about it. With agents, it means reading the execution trace, not just the output.","Japanese term adopted by lean manufacturing",W+"Gemba"),
("g-gan","generative adversarial networks","An architecture in which one network generates and another evaluates, both improving through the contest. It inspired the separation between generator and evaluator agents in long-running harnesses.","Ian Goodfellow and colleagues, 2014",""),
("g-harness","harness","Everything in an agent except the model: the tools it can use, the context it sees, the memory that survives between sessions, the permissions that bound it, the sensors that measure it and the record of what it did. The word denotes the equipment that channels an animal's strength in a useful direction.","Established as a discipline in February 2026","https://martinfowler.com/articles/harness-engineering.html"),
("g-jidoka","jidoka","Autonomation, or automation with a human touch. The machine detects the abnormality, stops itself and calls for help, so the defect does not travel down the line.","Toyota Production System",W+"Autonomation"),
("g-kaizen","kaizen","Continuous improvement in small increments, by everyone and all the time, rather than in episodic projects. It is the Reinforce step of the MEDIR cycle.","Japanese term spread through the Toyota Production System",W+"Kaizen"),
("g-kanban","kanban","A visual signalling system that authorises production or movement only when real demand exists, preventing accumulation.","Taiichi Ohno, Toyota Production System",W+"Kanban"),
("g-model","language model","The reasoning engine. It predicts the most likely continuation of a text and, by extension, proposes the next action. It executes nothing on its own: the tools the harness exposes do that.","",""),
("g-linter","linter","A program that analyses code automatically and flags rule violations before it moves on. With agents, the linter's error message acts as a sensor: when it teaches the fix, the agent repairs itself.","",""),
("g-pdca","PDCA","Plan, do, check, act. The iterative cycle of continuous process improvement, also known as the Shewhart or Deming cycle. It is the direct ancestor of any feedback-based control method, MEDIR included.","Walter Shewhart, 1930s; spread by Deming from the 1950s",W+"PDCA"),
("g-poka","poka-yoke","Mistake-proofing. Redesigning the process or the device so the error becomes impossible or is caught the instant it occurs, instead of asking for more attention from whoever executes. It is the literal definition of what harness engineering does with agents.","Shigeo Shingo, within the Toyota Production System",W+"Poka-yoke"),
("g-prompt","prompt","The written instruction given to the model on a run. Important, but only one component of the system, and the only one most people try to adjust when something fails.","",""),
("g-pr","pull request","A proposed change to a system, submitted for review before being merged. It is the natural point for a human gate in agent workflows.","",""),
("g-sandbox","sandbox","An isolated environment where execution happens without touching real systems. It is what allows autonomy to be delegated without an error having external consequences.","",""),
("g-shewhart","Shewhart, Walter","Physicist and statistician at Bell Labs, creator of statistical process control and the control chart, and author of the cycle that became PDCA.","1891 to 1967",W+"Walter_A._Shewhart"),
("g-tps","Toyota Production System","A production system built on two pillars, just-in-time and jidoka, and the origin of most of the quality vocabulary cited in this article.","Taiichi Ohno and Eiji Toyoda, from the 1950s",W+"Toyota_Production_System"),
("g-vibe","vibe coding","A way of programming in which you accept whatever the AI generates without reviewing it, feeding errors back for it to fix. Karpathy, who coined the term in 2025, described it as suited to throwaway weekend projects.","Andrej Karpathy, 2025",""),
]

def key(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')
G.sort(key=lambda e: key(e[1]))

items = []
for slug, term, defi, orig, link in G:
    tail = ''
    if orig or link:
        ref = ' <a href="%s">Source</a>' % link if link else ''
        tail = ' <em class="orig">%s.%s</em>' % (orig, ref) if orig else ' <em class="orig">%s</em>' % ref.strip()
    items.append('<p class="gitem" id="%s"><strong>%s</strong>: %s%s</p>' % (slug, term, defi, tail))
GLOSS = '\n'.join(items)

T = {}
def g(slug, tip, txt):
    return '<a class="g" href="#%s" data-tip="%s">%s</a>' % (slug, tip, txt)

T['model'] = g('g-model', "The reasoning engine. It predicts the next word or the next action, but executes nothing on its own.", 'model')
T['harness'] = g('g-harness', "Everything in an agent except the model: tools, context, memory, permissions, sensors and record.", 'harness')
T['kaizen'] = g('g-kaizen', "Continuous improvement in small increments, by everyone and all the time, rather than episodic projects.", 'kaizen')
T['kanban'] = g('g-kanban', "A visual signalling system that authorises production or movement only when real demand exists.", 'kanban')
T['poka'] = g('g-poka', "Mistake-proofing. Redesign the process so the error becomes impossible, instead of demanding more attention.", 'poka-yoke')
T['jidoka'] = g('g-jidoka', "Autonomation. The machine detects the abnormality and stops itself, so the defect does not travel on.", 'jidoka')
T['vibe'] = g('g-vibe', "Programming by accepting whatever the AI generates without review. Karpathy called it fit for throwaway projects.", '&quot;vibe coding&quot;')
T['context'] = g('g-context', "The discipline of deciding what enters the model&#39;s field of view on each run: documents, rules, results.", '&quot;context engineering&quot;')
T['cyb'] = g('g-cyb', "The science of control and communication in systems. Studies how a system regulates itself by anticipation and feedback.", 'cybernetic')
T['ashby'] = g('g-ashby', "The law of requisite variety: a regulator only controls a system if it has at least as much variety as it does.", "Ashby&#39;s Law")
T['shewhart'] = g('g-shewhart', "Bell Labs physicist, creator of statistical process control and of the cycle that became PDCA.", 'Walter Shewhart')
T['deming'] = g('g-deming', "American statistician who took Shewhart&#39;s cycle to Japan in the 1950s and made it the basis of quality management.", 'Deming')
T['pdca'] = g('g-pdca', "Plan, do, check, act. The iterative cycle of continuous improvement, also called the Shewhart cycle.", 'PDCA')
T['pdca2'] = g('g-pdca', "Plan, do, check, act. The iterative cycle of continuous improvement, also called the Shewhart cycle.", 'PDCA')
T['pr'] = g('g-pr', "A proposed change to a system, submitted for review and approval before being merged.", 'pull requests')
T['linter'] = g('g-linter', "A program that analyses code automatically and flags rule violations before it reaches production.", 'linters')
T['append'] = g('g-append', "A record where nothing can be altered or deleted, only added. The technical basis of any audit trail.", 'append-only log')
T['andon'] = g('g-andon', "A visual or audible signal that halts the line and calls for immediate help when a problem appears.", 'Andon')
T['gemba'] = g('g-gemba', "The real place where work happens. Going to the gemba means observing the process, not the report about it.", 'Gemba')
T['chart'] = g('g-chart', "A statistical process control graph showing whether variation is normal or something has changed.", 'Control chart')
T['dmaic'] = g('g-dmaic', "Define, measure, analyse, improve, control. The structured cycle of Six Sigma projects.", 'DMAIC')
T['prompt'] = g('g-prompt', "The written instruction given to the model. A component of the system, not the system.", 'prompt')

BODY = open('/home/claude/body_en.html', encoding='utf-8').read()
for k, v in T.items():
    BODY = BODY.replace('{{%s}}' % k, v)
BODY = BODY.replace('{{GLOSS}}', GLOSS)

open(os.path.join(OUT, 'harness-p1-en.html'), 'w', encoding='utf-8').write(shell + BODY)

ids = set(re.findall(r'id="(g-[a-z0-9\-]+)"', shell + BODY))
hr = set(re.findall(r'href="#(g-[a-z0-9\-]+)"', shell + BODY))
print('broken anchors:', hr - ids)
b = re.sub(r'<style.*?</style>', '', shell + BODY, flags=re.S)
b = re.sub(r'<svg.*?</svg>', '', b, flags=re.S)
print('words:', len(re.sub(r'<[^>]+>', ' ', b).split()))
print('placeholders left:', re.findall(r'\{\{[a-zA-Z]+\}\}', BODY))
