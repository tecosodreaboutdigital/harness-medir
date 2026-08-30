# -*- coding: utf-8 -*-
# Monta harness-p2.html trilingue (PT/EN/ES) a partir do arquivo PT
# vigente (fonte da verdade, ver build/LEIA-ME.md) mais os corpos
# em EN e ES escritos em build/body_p2_en.html e build/body_p2_es.html.
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

current = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
shell = current[:current.index('<div class="langbar">')]

i = current.index('<main class="page" id="doc-pt">') + len('<main class="page" id="doc-pt">')
j = current.index('</main>')
PT = current[i:j].strip()

EN = open(os.path.join(ROOT, 'build', 'body_p2_en.html'), encoding='utf-8').read().strip()
ES = open(os.path.join(ROOT, 'build', 'body_p2_es.html'), encoding='utf-8').read().strip()

def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(url\(#)([a-z0-9\-]+)(\))', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body

# PT ja esta com ids prefixados no arquivo vigente. EN e ES foram
# escritos com ids sem prefixo e precisam passar por scope().
EN = scope(EN, 'en')
ES = scope(ES, 'es')

bar = """<div class="langbar">
<button type="button" class="on" data-lang="pt">PT</button>
<button type="button" data-lang="en">EN</button>
<button type="button" data-lang="es">ES</button>
</div>"""

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

out_path = os.path.join(ROOT, 'harness-p2.html')
open(out_path, 'w', encoding='utf-8').write(doc)

# mantem build/body_p2_pt.html sincronizado com a fonte da verdade,
# para nao repetir o desvio historico registrado em build/LEIA-ME.md
open(os.path.join(ROOT, 'build', 'body_p2_pt.html'), 'w', encoding='utf-8').write(PT + '\n')

ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
for tag, name in ((PT, 'PT'), (EN, 'EN'), (ES, 'ES')):
    b = re.sub(r'<svg.*?</svg>', '', tag, flags=re.S)
    b = re.sub(r'<pre>.*?</pre>', '', b, flags=re.S)
    print(name, 'palavras:', len(re.sub(r'<[^>]+>', ' ', b).split()))
print('escrito em:', out_path)
