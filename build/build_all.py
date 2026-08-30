# -*- coding: utf-8 -*-
import unicodedata, re, os

OUT = '/mnt/user-data/outputs'
pt_file = open(os.path.join(OUT, 'harness-p1-pt.html'), encoding='utf-8').read()
en_file = open(os.path.join(OUT, 'harness-p1-en.html'), encoding='utf-8').read()

shell = pt_file[:pt_file.index('<main class="page">')]

def body_of(doc):
    i = doc.index('<main class="page">') + len('<main class="page">')
    j = doc.index('</main>')
    b = doc[i:j]
    b = re.sub(r'<div class="langbar">.*?</div>', '', b, flags=re.S)
    return b.strip()

PT = body_of(pt_file)
EN = body_of(en_file)

# ---------- glossario ES ----------
W = 'https://es.wikipedia.org/wiki/'
WE = 'https://en.wikipedia.org/wiki/'
G = [
("g-agente","agente","Sistema que combina un modelo de lenguaje con herramientas, memoria y reglas para ejecutar tareas de varias etapas, decidiendo en cada paso cuál es la siguiente acción. La ecuación corriente es agente igual a modelo más harness.","",""),
("g-agentsmd","AGENTS.md","Archivo en la raíz de un proyecto que orienta al agente sobre dónde está cada cosa, cuáles son las convenciones y qué no hacer. La buena práctica es tratarlo como índice corto, no como manual.","Especificación comunitaria","https://agents.md/"),
("g-andon","andon","Señal visual o sonora que muestra el estado del proceso e interrumpe la línea llamando ayuda inmediata cuando aparece un problema. En agentes equivale al escalamiento al humano con el contexto adjunto.","Sistema de Producción Toyota",WE+"Andon_(manufacturing)"),
("g-ashby","Ley de Ashby","Ley de la variedad requerida: un regulador solo consigue controlar un sistema si dispone de al menos tanta variedad como el sistema que gobierna. Explica por qué estandarizar tipos de tarea vuelve viable el control de agentes.","W. Ross Ashby, 1956",WE+"Variety_(cybernetics)"),
("g-cep","carta de control","Gráfico del control estadístico de proceso que separa la variación normal de un cambio real, permitiendo actuar solo cuando algo de hecho salió del patrón.","Walter Shewhart, Bell Labs, años veinte",WE+"Statistical_process_control"),
("g-cibernetica","cibernética","Ciencia del control y la comunicación en sistemas, biológicos o artificiales. Estudia cómo un sistema se mantiene rumbo a un objetivo mediante anticipación y realimentación.","Norbert Wiener, 1948",WE+"Cybernetics"),
("g-context","context engineering","Disciplina de decidir qué entra en el campo de visión del modelo en cada ejecución: qué documentos, reglas, ejemplos y resultados anteriores. Antecede al harness y sigue operando dentro de él.","Formulación de Birgitta Bockeler para agentes de código","https://martinfowler.com/articles/exploring-gen-ai/context-engineering-coding-agents.html"),
("g-deming","Deming, W. Edwards","Estadístico estadounidense que llevó el ciclo de Shewhart a Japón en los años cincuenta y lo transformó en fundamento de la gestión de la calidad moderna.","1900 a 1993",WE+"W._Edwards_Deming"),
("g-dmaic","DMAIC","Definir, medir, analizar, mejorar, controlar. Ciclo estructurado de conducción de proyectos Seis Sigma, y el pariente metodológico más cercano de MEDIR.","Motorola, años ochenta; consolidado por General Electric en los noventa",""),
("g-gan","redes generativas antagónicas","Arquitectura en la que una red genera contenido y otra evalúa, y ambas mejoran en la disputa. Inspiró la separación entre agente generador y agente evaluador en harnesses de larga duración.","Ian Goodfellow y colegas, 2014",""),
("g-gemba","gemba","El lugar real donde ocurre el trabajo. Ir al gemba significa observar el proceso directamente en lugar de discutir el informe sobre él. En agentes equivale a leer el rastro de la ejecución, y no solo el resultado.","Término japonés adoptado por la manufactura esbelta",WE+"Gemba"),
("g-harness","harness","Todo lo que existe en un agente excepto el modelo: las herramientas que puede usar, el contexto que ve, la memoria que sobrevive entre sesiones, los permisos que lo limitan, los sensores que lo miden y el registro de lo que hizo. La palabra designa el conjunto de equipos que canaliza la fuerza de un animal en una dirección útil.","Consolidado como disciplina en febrero de 2026","https://martinfowler.com/articles/harness-engineering.html"),
("g-jidoka","jidoka","Autonomación, o automatización con toque humano. La máquina detecta la anormalidad, se detiene sola y pide ayuda, para que el defecto no siga adelante en la línea.","Sistema de Producción Toyota",WE+"Autonomation"),
("g-kaizen","kaizen","Mejora continua hecha en pequeños incrementos, por todos y todo el tiempo, en lugar de grandes proyectos episódicos. Es el paso Reforzar del ciclo MEDIR.","Término japonés difundido por el Sistema de Producción Toyota",WE+"Kaizen"),
("g-kanban","kanban","Sistema visual de señalización que autoriza producción o movimiento solo cuando existe demanda real, evitando acumulación.","Taiichi Ohno, Sistema de Producción Toyota",WE+"Kanban"),
("g-linter","linter","Programa que analiza código automáticamente y señala violaciones de regla antes de que avance. En agentes, el mensaje de error del linter funciona como sensor: cuando enseña la corrección, el agente se arregla solo.","",""),
("g-append","log de solo anexión","Registro en el que nada puede alterarse ni borrarse, solo añadirse al final. Es la base técnica de cualquier rastro de auditoría confiable, y lo que permite reconstruir, reproducir y revertir una ejecución.","",""),
("g-modelo","modelo de lenguaje","El motor de razonamiento. Predice la continuación más probable de un texto y, por extensión, propone la siguiente acción. No ejecuta nada por su cuenta: quien ejecuta son las herramientas que el harness expone.","",""),
("g-pdca","PDCA","Planificar, hacer, verificar, actuar. Ciclo iterativo de mejora continua de procesos, también llamado ciclo de Shewhart o ciclo de Deming. Es el ancestro directo de cualquier método de control con realimentación, MEDIR incluido.","Walter Shewhart, años treinta; difundido por Deming desde los cincuenta",WE+"PDCA"),
("g-poka","poka-yoke","A prueba de error. Rediseñar el proceso o el dispositivo para que el error se vuelva imposible o sea detectado en el instante en que ocurre, en lugar de pedir más atención a quien ejecuta. Es la definición literal de lo que la ingeniería de harness hace con agentes.","Shigeo Shingo, dentro del Sistema de Producción Toyota",WE+"Poka-yoke"),
("g-prompt","prompt","La instrucción escrita que se le da al modelo en una ejecución. Importante, pero apenas un componente del sistema, y el único que la mayoría intenta ajustar cuando algo falla.","",""),
("g-pr","pull request","Propuesta de cambio en un sistema, sometida a revisión antes de ser incorporada. Es el punto natural de portero humano en flujos de trabajo con agentes.","",""),
("g-sandbox","sandbox","Entorno aislado donde ocurre la ejecución sin tocar los sistemas reales. Es lo que permite delegar autonomía sin que un error tenga consecuencia externa.","",""),
("g-shewhart","Shewhart, Walter","Físico y estadístico de los Bell Labs, creador del control estadístico de proceso y de la carta de control, y autor del ciclo que originó el PDCA.","1891 a 1967",WE+"Walter_A._Shewhart"),
("g-tps","Sistema de Producción Toyota","Sistema de producción construido sobre dos pilares, el just-in-time y el jidoka, y origen de la mayor parte del vocabulario de calidad citado en este artículo.","Taiichi Ohno y Eiji Toyoda, desde los años cincuenta",WE+"Toyota_Production_System"),
("g-vibe","vibe coding","Modo de programar en que se acepta lo que la IA genera sin revisar, devolviéndole los errores para que los corrija. Karpathy, que acuñó el término en 2025, lo describió como adecuado a proyectos desechables de fin de semana.","Andrej Karpathy, 2025",""),
]
def key(t):
    return ''.join(c for c in unicodedata.normalize('NFD', t.lower()) if unicodedata.category(c) != 'Mn')
G.sort(key=lambda e: key(e[1]))
items = []
for slug, term, defi, orig, link in G:
    tail = ''
    if orig or link:
        ref = ' <a href="%s">Fuente</a>' % link if link else ''
        tail = ' <em class="orig">%s.%s</em>' % (orig, ref) if orig else ' <em class="orig">%s</em>' % ref.strip()
    items.append('<p class="gitem" id="%s"><strong>%s</strong>: %s%s</p>' % (slug, term, defi, tail))
GLOSS_ES = '\n'.join(items)

def g(slug, tip, txt):
    return '<a class="g" href="#%s" data-tip="%s">%s</a>' % (slug, tip, txt)

T = {
 'model': g('g-modelo', "El motor de razonamiento. Predice la siguiente palabra o la siguiente accion, pero no ejecuta nada por si solo.", 'modelo'),
 'harness': g('g-harness', "Todo lo que existe en un agente excepto el modelo: herramientas, contexto, memoria, permisos, sensores y registro.", 'harness'),
 'kaizen': g('g-kaizen', "Mejora continua en pequenos incrementos, por todos y todo el tiempo, en lugar de proyectos episodicos.", 'kaizen'),
 'kanban': g('g-kanban', "Sistema visual de senalizacion que autoriza produccion o movimiento solo cuando existe demanda real.", 'kanban'),
 'poka': g('g-poka', "A prueba de error. Redisenar el proceso para que el error se vuelva imposible, en vez de pedir mas atencion.", 'poka-yoke'),
 'jidoka': g('g-jidoka', "Autonomacion. La maquina detecta la anormalidad y se detiene sola, para que el defecto no siga adelante.", 'jidoka'),
 'vibe': g('g-vibe', "Programar aceptando lo que la IA genera sin revisar. Karpathy lo describio como apto para proyectos desechables.", '&quot;vibe coding&quot;'),
 'context': g('g-context', "Disciplina de decidir que entra en el campo de vision del modelo en cada ejecucion: documentos, reglas, resultados.", '&quot;context engineering&quot;'),
 'cyb': g('g-cibernetica', "Ciencia del control y la comunicacion en sistemas. Estudia como un sistema se regula por anticipacion y realimentacion.", 'cibernético'),
 'ashby': g('g-ashby', "Ley de la variedad requerida: un regulador solo controla un sistema si tiene al menos tanta variedad como el.", 'Ley de Ashby'),
 'shewhart': g('g-shewhart', "Fisico de los Bell Labs, creador del control estadistico de proceso y del ciclo que origino el PDCA.", 'Walter Shewhart'),
 'deming': g('g-deming', "Estadistico que llevo el ciclo de Shewhart a Japon en los anos cincuenta y lo volvio base de la gestion de calidad.", 'Deming'),
 'pdca': g('g-pdca', "Planificar, hacer, verificar, actuar. Ciclo iterativo de mejora continua, tambien llamado ciclo de Shewhart.", 'PDCA'),
 'pdca2': g('g-pdca', "Planificar, hacer, verificar, actuar. Ciclo iterativo de mejora continua, tambien llamado ciclo de Shewhart.", 'PDCA'),
 'pr': g('g-pr', "Propuesta de cambio en un sistema, sometida a revision y aprobacion antes de ser incorporada.", 'pull requests'),
 'linter': g('g-linter', "Programa que analiza codigo automaticamente y senala violaciones de regla antes de que llegue a produccion.", 'linters'),
 'append': g('g-append', "Registro donde nada puede alterarse ni borrarse, solo anadirse. Base tecnica de cualquier rastro de auditoria.", 'log que solo acepta añadidos'),
 'andon': g('g-andon', "Senal visual o sonora que interrumpe la linea y llama ayuda inmediata cuando aparece un problema.", 'Andon'),
 'gemba': g('g-gemba', "El lugar real donde ocurre el trabajo. Ir al gemba es observar el proceso, no discutir el informe sobre el.", 'Gemba'),
 'chart': g('g-cep', "Grafico del control estadistico de proceso que muestra si la variacion es normal o si algo cambio.", 'Carta de control'),
 'dmaic': g('g-dmaic', "Definir, medir, analizar, mejorar, controlar. Ciclo estructurado de proyectos Seis Sigma.", 'DMAIC'),
 'prompt': g('g-prompt', "La instruccion escrita que se le da al modelo. Un componente del sistema, no el sistema.", 'prompt'),
}

ES = open('/home/claude/body_es.html', encoding='utf-8').read()
for k, v in T.items():
    ES = ES.replace('{{%s}}' % k, v)
ES = ES.replace('{{GLOSS}}', GLOSS_ES)

# ---------- prefixar ids e ancoras internas por idioma ----------
def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(url\(#)([a-z0-9\-]+)(\))', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body

PT, EN, ES = scope(PT, 'pt'), scope(EN, 'en'), scope(ES, 'es')

extra_css = """
.langbar{position:sticky;top:0;z-index:40;background:var(--paper);padding-top:10px}
main[hidden]{display:none}
"""
shell = shell.replace('.eyebrow{', extra_css + '.eyebrow{')

bar = """<div class="langbar">
<button type="button" class="on" data-lang="pt">PT</button>
<button type="button" data-lang="en">EN</button>
<button type="button" data-lang="es">ES</button>
</div>"""

shell = shell.replace('.langbar a{', '.langbar button{').replace('.langbar a.on{', '.langbar button.on{').replace('.langbar a:hover{', '.langbar button:hover{')
shell = shell.replace('  color:var(--ink-faint);\n  text-decoration:none;\n}', '  color:var(--ink-faint);\n  background:none;\n  cursor:pointer;\n  font-family:inherit;\n}', 1)

js = """<script>
(function(){
  var bar=document.querySelector('.langbar');
  var mains={pt:document.getElementById('doc-pt'),en:document.getElementById('doc-en'),es:document.getElementById('doc-es')};
  function set(l){
    for(var k in mains){mains[k].hidden=(k!==l);}
    bar.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.lang===l);});
    document.documentElement.lang=(l==='pt'?'pt-BR':l);
  }
  var h=location.hash.slice(1);
  var m=h.match(/^(en|es|pt)-/);
  if(m){
    set(m[1]);
    var target=document.getElementById(h);
    if(target){setTimeout(function(){target.scrollIntoView();},0);}
  }
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button[data-lang]');
    if(b){set(b.dataset.lang);try{location.hash='';}catch(e){}window.scrollTo(0,0);}
  });
})();
</script>
</body>
</html>"""

doc = (shell
 + bar + '\n'
 + '<main class="page" id="doc-pt">\n' + PT + '\n</main>\n'
 + '<main class="page" id="doc-en" hidden>\n' + EN + '\n</main>\n'
 + '<main class="page" id="doc-es" hidden>\n' + ES + '\n</main>\n'
 + js)

open(os.path.join(OUT, 'harness-p1.html'), 'w', encoding='utf-8').write(doc)
os.remove(os.path.join(OUT, 'harness-p1-pt.html'))
os.remove(os.path.join(OUT, 'harness-p1-en.html'))

ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
print('placeholders:', re.findall(r'\{\{[a-zA-Z]+\}\}', doc))
for tag, name in ((PT, 'PT'), (EN, 'EN'), (ES, 'ES')):
    b = re.sub(r'<svg.*?</svg>', '', tag, flags=re.S)
    print(name, 'palavras:', len(re.sub(r'<[^>]+>', ' ', b).split()))
