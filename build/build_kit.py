# -*- coding: utf-8 -*-
import re, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p2 = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
shell = p2[:p2.index('<div class="langbar">')]
shell = shell.replace('<title>Guias e sensores: como um agente aprende a se corrigir | Parte 2</title>',
                    '<title>Caixa de ferramentas do harness | Documento companheiro</title>')
BODY = open(os.path.join(ROOT, 'build', 'body_kit_pt.html'), encoding='utf-8').read()
def scope(b, pref):
    b = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), b)
    b = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), b)
    return b
BODY = scope(BODY, 'pt')
bar = """<div class="langbar">
<button type="button" class="on" data-lang="pt">PT</button>
<button type="button" data-lang="en" disabled title="em preparo">EN</button>
<button type="button" data-lang="es" disabled title="en preparación">ES</button>
</div>"""
js = """<script>
(function(){var b=document.querySelector('.langbar');if(!b)return;
b.addEventListener('click',function(e){var t=e.target.closest('button[data-lang]:not([disabled])');
if(!t)return;b.querySelectorAll('button').forEach(function(x){x.classList.toggle('on',x===t);});window.scrollTo(0,0);});})();
</script>
</body>
</html>"""
doc = shell + bar + '\n<main class="page" id="doc-pt">\n' + BODY + '\n</main>\n' + js
out_path = os.path.join(ROOT, 'harness-caixa-de-ferramentas.html')
open(out_path, 'w', encoding='utf-8').write(doc)
ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
print('broken:', sorted(hr - ids))
b = re.sub(r'<pre>.*?</pre>', '', BODY, flags=re.S)
print('palavras:', len(re.sub(r'<[^>]+>', ' ', b).split()))
print('escrito em:', out_path)
