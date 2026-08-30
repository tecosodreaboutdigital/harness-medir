# -*- coding: utf-8 -*-
import unicodedata, re, os

OUT = '/mnt/user-data/outputs'
p1 = open(os.path.join(OUT, 'harness-p1.html'), encoding='utf-8').read()
shell = p1[:p1.index('<div class="langbar">')]
shell = shell.replace('<title>O melhor modelo do mundo dentro de uma empresa sem processo | Parte 1</title>',
                      '<title>Guias e sensores: como um agente aprende a se corrigir | Parte 2</title>')

code_css = """
pre{
  background:var(--fill);
  padding:14px 16px;
  margin:20px 0;
  overflow-x:auto;
  border:0;
  print-color-adjust:exact;
  -webkit-print-color-adjust:exact;
  page-break-inside:avoid;
}
pre code{
  font-family:var(--font-mono,"Consolas","Menlo",monospace);
  font-size:11.5px;
  line-height:1.5;
  white-space:pre;
  color:var(--ink);
}
p code{
  font-family:var(--font-mono,"Consolas","Menlo",monospace);
  font-size:12.5px;
  background:var(--fill);
  padding:1px 4px;
}
"""
serie_css = '''
.serie{
  display:flex;
  gap:18px;
  align-items:baseline;
  font-size:11px;
  letter-spacing:.14em;
  text-transform:uppercase;
  padding:0 0 16px;
  margin:0 0 26px;
  border-bottom:.5pt solid var(--rule);
}
.serie a{color:var(--ink-faint);border:0;text-decoration:none}
.serie a:hover{color:var(--ink)}
.serie a.cur{color:var(--ink)}
.serie span{color:var(--rule)}
'''
shell = shell.replace('.gitem{', code_css + serie_css + '.gitem{')
shell = shell.replace('  .gitem .orig{font-size:9pt;font-style:italic}',
  '  .gitem .orig{font-size:9pt;font-style:italic}\n  pre{font-size:8.5pt;padding:6pt 8pt;background:#eef1f4;border:0;page-break-inside:avoid}\n  pre code{font-size:8.5pt}\n  p code{font-size:9pt}')

W = 'https://en.wikipedia.org/wiki/'
G = [
("g-agente","agente","Sistema que combina um modelo de linguagem com ferramentas, memória e regras para executar tarefas de várias etapas. A equação corrente é agente igual a modelo mais harness.","",""),
("g-alcada","alçada","O limite do que alguém, ou algum sistema, pode decidir sozinho. Em harness, é definida por classe de ação e imposta fora do modelo.","",""),
("g-analise","análise estática","Verificação automática feita sobre o trabalho sem executá-lo, procurando violações de regra, tamanho excessivo, duplicidade e estrutura irregular.","",""),
("g-cadencia","cadência","Frequência fixa em que uma verificação roda, independente de haver tarefa em andamento. É o que detecta deriva, que nenhuma execução isolada revela.","",""),
("g-cobertura","cobertura de teste","Percentual do trabalho que foi executado pelos testes. Informa que algo foi executado, não que o efeito foi verificado, o que a torna um indicador enganoso quando usada sozinha.","",""),
("g-contrato","contrato da tarefa","Definição escrita, antes da execução, do que a tarefa entrega, quais são seus limites e como saber que terminou. É o passo Mapear do ciclo MEDIR.","",""),
("g-deriva","deriva","Degradação gradual que não acontece em nenhuma execução específica, e sim ao longo de dezenas delas. Só é detectada por sensores que rodam em cadência.","",""),
("g-divulgacao","divulgação progressiva","Princípio pelo qual o agente carrega apenas a informação que a tarefa exige, em níveis: primeiro o resumo, depois o corpo, depois os anexos. É o que permite guias grandes sem custo de leitura.","Anthropic, Agent Skills","https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills"),
("g-guia","guia","Controle que age antes da execução, aumentando a probabilidade de o agente acertar na primeira tentativa: regras, convenções, exemplos, contrato da tarefa. Chamado de controle antecipatório.","Formulação de Birgitta Bockeler","https://martinfowler.com/articles/harness-engineering.html"),
("g-harness","harness","Tudo o que existe em um agente exceto o modelo: ferramentas, contexto, memória duradoura, permissões, sensores e registro do que foi feito.","Consolidado como disciplina em fevereiro de 2026","https://martinfowler.com/articles/harness-engineering.html"),
("g-injecao","injeção de contexto","Inserção de texto no campo de leitura do agente durante a execução. É perigosa quando vem de fora sem controle, e é a técnica central do sensor que ensina quando vem do seu próprio harness.","",""),
("g-jidoka","jidoka","Autonomação. A máquina detecta a anormalidade, para sozinha e chama ajuda, para que o defeito não siga adiante na linha.","Sistema Toyota de Produção",W+"Autonomation"),
("g-medir","MEDIR","Ciclo de engenharia de harness em cinco passos: Mapear, Equipar, Delegar, Inspecionar e Reforçar. Descrito na parte 1 desta série.","",""),
("g-modelo","modelo de linguagem","O motor de raciocínio. Propõe a próxima ação, mas não executa nada por conta própria: quem executa são as ferramentas que o harness expõe.","",""),
("g-mutacao","teste de mutação","Técnica que introduz pequenas alterações propositais no trabalho e verifica se os testes as detectam. Revela testes que executam o código sem verificar nada.","",""),
("g-pdca","PDCA","Planejar, fazer, verificar, agir. Ciclo iterativo de melhoria contínua, também chamado de ciclo de Shewhart. Ancestral direto do MEDIR.","Walter Shewhart, anos 1930",W+"PDCA"),
("g-poka","poka-yoke","À prova de erro. Redesenhar o processo para que o erro se torne impossível, em vez de pedir mais atenção a quem executa.","Shigeo Shingo, Sistema Toyota de Produção",W+"Poka-yoke"),
("g-portao","portão","Ponto do fluxo em que nada avança sem que uma condição seja satisfeita. Diferente de uma instrução, um portão não pode ser ignorado por quem executa.","",""),
("g-recibo","recibo de execução","Registro compacto do que produziu um resultado: contrato usado, fontes consultadas, sensores acionados, tentativas, custo, quem aprovou e ponto de reversão.","",""),
("g-regressao","teste de regressão","Verificação que detecta quando uma mudança quebrou algo que funcionava antes. É o principal sensor de manutenção de qualquer sistema que continua evoluindo.","",""),
("g-reversibilidade","reversibilidade","Critério que organiza a delegação: uma ação reversível custa o preço de desfazê-la, uma ação irreversível custa o preço do erro. É a régua correta para definir alçada, e não a importância aparente da ação.","",""),
("g-sandbox","sandbox","Ambiente isolado onde a execução acontece sem tocar nos sistemas reais. Permite delegar autonomia sem que um erro tenha consequência externa.","",""),
("g-sensor","sensor","Controle que age depois da execução, medindo o que foi produzido e devolvendo ao agente a informação necessária para que ele se corrija. Chamado de controle por realimentação.","Formulação de Birgitta Bockeler","https://martinfowler.com/articles/sensors-for-coding-agents.html"),
("g-skill","skill","Pasta contendo um arquivo SKILL.md com cabeçalho de nome e descrição, mais instruções, arquivos de apoio e código opcional. Formato aberto para empacotar conhecimento de procedimento para agentes.","Anthropic, outubro de 2025; padrão aberto desde dezembro de 2025","https://agentskills.io/"),
("g-teto","teto de tentativas","Número máximo de vezes que um agente pode repetir uma tarefa antes de parar e escalar. Sem ele, um laço de correção pode consumir tempo e custo indefinidamente.","",""),
("g-verificacao","verificação dura","Verificação determinística e rápida, que dá sempre a mesma resposta para a mesma entrada. Oposta à verificação por julgamento, que é semântica, cara e probabilística.","",""),
]
def key(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')
G.sort(key=lambda e: key(e[1]))
items = []
for slug, term, defi, orig, link in G:
    tail = ''
    if orig or link:
        ref = ' <a href="%s">Fonte</a>' % link if link else ''
        tail = ' <em class="orig">%s.%s</em>' % (orig, ref) if orig else ' <em class="orig">%s</em>' % ref.strip()
    items.append('<p class="gitem" id="%s"><strong>%s</strong>: %s%s</p>' % (slug, term, defi, tail))
GLOSS = '\n'.join(items)

def g(slug, tip, txt):
    return '<a class="g" href="#%s" data-tip="%s">%s</a>' % (slug, tip, txt)

T = {
 'medir': g('g-medir', "Ciclo em cinco passos: Mapear, Equipar, Delegar, Inspecionar e Reforcar. Descrito na parte 1 da serie.", 'ciclo MEDIR'),
 'guia': g('g-guia', "Controle que age antes da execucao, para aumentar a chance de acerto na primeira tentativa.", 'Guias'),
 'sensor': g('g-sensor', "Controle que age depois da execucao, medindo o resultado e devolvendo ao agente como se corrigir.", 'Sensores'),
 'skill': g('g-skill', "Pasta com um arquivo SKILL.md, instrucoes, arquivos de apoio e codigo opcional. Formato aberto.", 'skill'),
 'divulgacao': g('g-divulgacao', "O agente carrega so a informacao que a tarefa exige, em niveis: resumo, corpo, anexos.", 'divulgação progressiva'),
 'recibo': g('g-recibo', "Registro compacto do que produziu um resultado: contrato, fontes, sensores, tentativas, custo e aprovacao.", 'recibo'),
 'teto': g('g-teto', "Numero maximo de vezes que um agente pode repetir uma tarefa antes de parar e escalar.", 'teto'),
 'deriva': g('g-deriva', "Degradacao gradual que nao acontece em nenhuma execucao especifica, e sim ao longo de dezenas delas.", 'deriva'),
 'reversibilidade': g('g-reversibilidade', "Criterio que organiza a delegacao: acao reversivel custa o preco de desfazer, irreversivel custa o preco do erro.", 'reversibilidade'),
}

BODY = open('/home/claude/body_p2_pt.html', encoding='utf-8').read()
for k, v in T.items():
    BODY = BODY.replace('{{%s}}' % k, v)
BODY = BODY.replace('{{GLOSS}}', GLOSS)

def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(url\(#)([a-z0-9\-]+)(\))', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body
BODY = scope(BODY, 'pt')

serie = '''<nav class="serie">
<a href="harness-p1.html">Parte 1</a>
<a class="cur" href="harness-p2.html">Parte 2</a>
<span>Parte 3</span>
<a href="harness-caixa-de-ferramentas.html">Guia compacto</a>
</nav>'''

bar = """<div class="langbar">
<button type="button" class="on" data-lang="pt">PT</button>
<button type="button" data-lang="en" disabled title="em preparo">EN</button>
<button type="button" data-lang="es" disabled title="en preparación">ES</button>
</div>"""

js = """<script>
(function(){
  var bar=document.querySelector('.langbar');
  if(!bar) return;
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button[data-lang]:not([disabled])');
    if(!b) return;
    bar.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===b);});
    window.scrollTo(0,0);
  });
})();
</script>
</body>
</html>"""

doc = shell + bar + serie + '\n<main class="page" id="doc-pt">\n' + BODY + '\n</main>\n' + js
open(os.path.join(OUT, 'harness-p2.html'), 'w', encoding='utf-8').write(doc)

ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
print('placeholders:', re.findall(r'\{\{[a-zA-Z]+\}\}', doc))
b = re.sub(r'<svg.*?</svg>', '', BODY, flags=re.S)
b = re.sub(r'<pre>.*?</pre>', '', b, flags=re.S)
print('palavras (sem codigo):', len(re.sub(r'<[^>]+>', ' ', b).split()))
print('verbetes:', len(G))
