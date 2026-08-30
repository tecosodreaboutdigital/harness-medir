# -*- coding: utf-8 -*-
# Monta harness-toolkit.html trilingue (EN/PT/ES) a partir dos tres
# corpos em build/body_toolkit_en.html, build/body_toolkit_pt.html e
# build/body_toolkit_es.html. Ingles e a lingua padrao do projeto
# desde 30 de agosto de 2026 (ver STANDARDS.md), entao os tres corpos
# sao tratados de forma simetrica aqui: nenhum deles e "extraido do
# arquivo vigente" como PT era em build_p2.py antes desta reescrita,
# os tres sao arquivos-fonte editaveis em build/, sem prefixo de
# idioma nos ids e ancoras, prefixados por scope() no build.
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

p2 = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
shell = p2[:p2.index('<div class="langbar">')]
shell = shell.replace(
    '<title>Guides and sensors: how an agent learns to correct itself | Part 2</title>',
    '<title>The harness toolkit | Companion document</title>')

EN = open(os.path.join(ROOT, 'build', 'body_toolkit_en.html'), encoding='utf-8').read().strip()
PT = open(os.path.join(ROOT, 'build', 'body_toolkit_pt.html'), encoding='utf-8').read().strip()
ES = open(os.path.join(ROOT, 'build', 'body_toolkit_es.html'), encoding='utf-8').read().strip()

def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body

EN = scope(EN, 'en')
PT = scope(PT, 'pt')
ES = scope(ES, 'es')

bar = """<div class="langbar">
<button type="button" data-lang="pt">PT</button>
<button type="button" class="on" data-lang="en">EN</button>
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

out_path = os.path.join(ROOT, 'harness-toolkit.html')
open(out_path, 'w', encoding='utf-8').write(doc)

ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
for tag, name in ((PT, 'PT'), (EN, 'EN'), (ES, 'ES')):
    b = re.sub(r'<pre>.*?</pre>', '', tag, flags=re.S)
    print(name, 'palavras:', len(re.sub(r'<[^>]+>', ' ', b).split()))
print('escrito em:', out_path)
