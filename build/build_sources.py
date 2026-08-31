# -*- coding: utf-8 -*-
# Monta harness-sources.html trilingue (EN/PT/ES) a partir dos tres
# corpos em build/body_sources_en.html, body_sources_pt.html e
# body_sources_es.html. Segue exatamente o padrao simetrico de
# build_toolkit.py: os tres corpos sao fonte, sem prefixo de idioma
# nos ids, prefixados por scope() no build. O envoltorio (head, CSS,
# a barra de topo unificada) e extraido de harness-p2.html vigente,
# que ja carrega a barra de serie compartilhada desde 30/08/2026.
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

p2 = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
shell = p2[:p2.index('<div class="topbar">')]
shell = shell.replace(
    '<title>Guides and sensors: how an agent learns to correct itself | Part 2</title>',
    '<title>Sources | Harness series</title>')

EN = open(os.path.join(ROOT, 'build', 'body_sources_en.html'), encoding='utf-8').read().strip()
PT = open(os.path.join(ROOT, 'build', 'body_sources_pt.html'), encoding='utf-8').read().strip()
ES = open(os.path.join(ROOT, 'build', 'body_sources_es.html'), encoding='utf-8').read().strip()

def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body

EN = scope(EN, 'en')
PT = scope(PT, 'pt')
ES = scope(ES, 'es')

CUR = 'sources'
SERIES_ORDER = ['p1', 'p2', 'p3', 'p4', 'guide', 'glossary', 'sources']
FILES = {'p1': 'harness-p1.html', 'p2': 'harness-p2.html', 'p3': 'harness-p3.html',
         'p4': 'harness-p4.html', 'guide': 'harness-toolkit.html',
         'glossary': 'harness-glossary.html', 'sources': 'harness-sources.html'}
LABELS_EN = {'p1': 'Part 1', 'p2': 'Part 2', 'p3': 'Part 3', 'p4': 'Part 4',
             'guide': 'Compact guide', 'glossary': 'Glossary', 'sources': 'Sources'}
EXISTS = {'p1', 'p2', 'p3', 'p4', 'guide', 'glossary', 'sources'}  # p4 now written

def topbar_html(cur):
    pieces = []
    for i, key in enumerate(SERIES_ORDER):
        if i > 0:
            if key == 'guide':
                pieces.append('<span class="sep pipe">|</span>')
            else:
                pieces.append('<span class="sep">·</span>')
        label = LABELS_EN[key]
        if key == cur:
            pieces.append('<span class="cur" data-key="%s">%s</span>' % (key, label))
        elif key in EXISTS:
            pieces.append('<a href="%s#en-" data-key="%s">%s</a>' % (FILES[key], key, label))
        else:
            pieces.append('<span class="pending" data-key="%s">%s</span>' % (key, label))
    pieces.append('<span class="sep pipe">|</span>')
    pieces.append('<a class="icon-link" href="docs/logbook.html#en-" data-key="logbook" data-icon="1" '
                   'title="Project log" aria-label="Project log"><svg viewBox="0 0 16 16" width="14" '
                   'height="14" aria-hidden="true" focusable="false"><polyline points="1,13 5,13 5,9 9,9 9,4 15,4" '
                   'fill="none" stroke="currentColor" stroke-width="1.3"/></svg></a>')
    return ('<div class="topbar">\n<nav class="serie">\n' + '\n'.join(pieces) + '\n</nav>\n'
            '<span class="brace">{</span>\n<div class="langbar">\n'
            '<button type="button" data-lang="pt">PT</button>\n'
            '<button type="button" class="on" data-lang="en">EN</button>\n'
            '<button type="button" data-lang="es">ES</button>\n</div>\n'
            '<span class="brace">}</span>\n</div>')

bar = topbar_html(CUR)

js = """<script>
(function(){
  var bar=document.querySelector('.langbar');
  var mains={pt:document.getElementById('doc-pt'),en:document.getElementById('doc-en'),es:document.getElementById('doc-es')};
  var SERIES={p1:{file:'harness-p1.html',label:{en:'Part 1',pt:'Parte 1',es:'Parte 1'}},p2:{file:'harness-p2.html',label:{en:'Part 2',pt:'Parte 2',es:'Parte 2'}},p3:{file:'harness-p3.html',label:{en:'Part 3',pt:'Parte 3',es:'Parte 3'}},p4:{file:'harness-p4.html',label:{en:'Part 4',pt:'Parte 4',es:'Parte 4'}},guide:{file:'harness-toolkit.html',label:{en:'Compact guide',pt:'Guia compacto',es:'Gu\\u00eda compacta'}},glossary:{file:'harness-glossary.html',label:{en:'Glossary',pt:'Gloss\\u00e1rio',es:'Glosario'}},sources:{file:'harness-sources.html',label:{en:'Sources',pt:'Fontes',es:'Fuentes'}},logbook:{file:'docs/logbook.html',label:{en:'Project log',pt:'Di\\u00e1rio de bordo',es:'Diario de bordo'}}};
  function setSeries(l){
    document.querySelectorAll('.serie [data-key]').forEach(function(el){
      var info=SERIES[el.dataset.key];
      if(!info)return;
      if(el.dataset.icon){el.title=info.label[l];}else{el.textContent=info.label[l];}
      if(el.tagName==='A'){el.setAttribute('href',info.file+'#'+l+'-');}
    });
  }
  function set(l){
    for(var k in mains){mains[k].hidden=(k!==l);}
    bar.querySelectorAll('button').forEach(function(b){b.classList.toggle('on',b.dataset.lang===l);});
    document.documentElement.lang=(l==='pt'?'pt-BR':l);
    setSeries(l);
  }
  var h=location.hash.slice(1);
  var m=h.match(/^(en|es|pt)-/);
  var active='en';
  if(m){
    active=m[1];
    set(active);
    var target=document.getElementById(h);
    if(target){setTimeout(function(){target.scrollIntoView();},0);}
  }
  bar.addEventListener('click',function(e){
    var b=e.target.closest('button[data-lang]');
    if(b){set(b.dataset.lang);try{location.hash='';}catch(e){}window.scrollTo(0,0);}
  });
  function dismissHint(){
    var d=document.querySelector('.lang-hint');
    if(d){d.remove();}
    try{localStorage.setItem('langHintDismissed','1');}catch(e){}
  }
  try{
    if(!m&&!localStorage.getItem('langHintDismissed')){
      var bl=(navigator.language||'').slice(0,2).toLowerCase();
      var msgs={pt:{text:'Esta p\\u00e1gina tamb\\u00e9m est\\u00e1 dispon\\u00edvel em portugu\\u00eas.',btn:'Ver em portugu\\u00eas'},es:{text:'Esta p\\u00e1gina tambi\\u00e9n est\\u00e1 disponible en espa\\u00f1ol.',btn:'Ver en espa\\u00f1ol'}};
      if(msgs[bl]&&bl!==active){
        var d=document.createElement('div');
        d.className='lang-hint';
        var span=document.createElement('span');
        span.textContent=msgs[bl].text;
        var right=document.createElement('span');
        var btn=document.createElement('button');
        btn.type='button';
        btn.textContent=msgs[bl].btn;
        btn.addEventListener('click',function(){dismissHint();set(bl);try{location.hash='';}catch(e){}window.scrollTo(0,0);});
        var x=document.createElement('button');
        x.type='button';
        x.className='x';
        x.setAttribute('aria-label','Close');
        x.textContent='\\u00d7';
        x.addEventListener('click',dismissHint);
        right.appendChild(btn);
        right.appendChild(x);
        d.appendChild(span);
        d.appendChild(right);
        bar.parentNode.insertBefore(d,bar.nextSibling);
      }
    }
  }catch(e){}
})();
</script>
</body>
</html>"""

doc = (shell
 + bar + '\n'
 + '<main class="page" id="doc-pt" hidden>\n' + PT + '\n</main>\n'
 + '<main class="page" id="doc-en">\n' + EN + '\n</main>\n'
 + '<main class="page" id="doc-es" hidden>\n' + ES + '\n</main>\n'
 + js)

out_path = os.path.join(ROOT, 'harness-sources.html')
open(out_path, 'w', encoding='utf-8').write(doc)

ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
for tag, name in ((PT, 'PT'), (EN, 'EN'), (ES, 'ES')):
    print(name, 'palavras:', len(re.sub(r'<[^>]+>', ' ', tag).split()))
print('escrito em:', out_path)
