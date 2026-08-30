# -*- coding: utf-8 -*-
import re

p = '/home/claude/body_p2_pt.html'
s = open(p, encoding='utf-8').read()

# ---------- 1. indice: nova entrada ----------
s = s.replace(
'    <li><a href="#evolucao">Como um harness evolui</a></li>',
'    <li><a href="#ambientes">Em que ambiente isso é possível</a></li>\n    <li><a href="#evolucao">Como um harness evolui</a></li>')

# ---------- 2. renumerar secoes 12 em diante ----------
s = s.replace('<h2 id="evolucao">12. Como um harness evolui</h2>', '<h2 id="evolucao">13. Como um harness evolui</h2>')
s = s.replace('<h2 id="riscos-2">13. Riscos desta camada', '<h2 id="riscos-2">14. Riscos desta camada')
s = s.replace('<h2 id="glossario">14. Glossário</h2>', '<h2 id="glossario">15. Glossário</h2>')
s = s.replace('<h2 id="fontes">15. Fontes</h2>', '<h2 id="fontes">16. Fontes</h2>')

# ---------- 3. subsecao dentro da secao 5 ----------
nova_sub = """<h3>A regra inegociável e as bandeiras vermelhas</h3>

<p>Existe uma técnica de guia que aparece nas coleções de skills mais usadas hoje e que vale roubar, porque resolve um problema que ninguém formula direito.</p>

<p>O padrão é este: cada guia abre com uma regra inegociável, escrita de forma curta e sem ambiguidade, e logo abaixo traz uma lista de bandeiras vermelhas. As bandeiras não descrevem erros técnicos. Elas descrevem as racionalizações que o agente provavelmente vai usar para justificar não seguir a regra. Coisas como "só desta vez", ou o teste que passou na primeira tentativa sem nunca ter falhado, ou as palavras deveria, provavelmente e parece que aparecendo em um relato de verificação.</p>

<p>O raciocínio por trás disso é sutil e correto. O alvo do guia não é ensinar a regra, porque o sistema já a conhece. O alvo é impedir que ele se convença a não segui-la. São coisas diferentes, e a segunda é a que falha na prática.</p>

<div class="rule-box"><span class="lbl">Como aplicar</span><p>Ao escrever qualquer guia, depois de enunciar a regra, escreva a desculpa. Pergunte a si mesmo qual seria a justificativa mais plausível para descumpri-la, e coloque essa justificativa por escrito como sinal de alerta. Você está antecipando a negociação em vez de esperá-la acontecer.</p></div>

<h3>O truque do limiar</h3>"""

s = s.replace('<h3>O truque do limiar</h3>', nova_sub, 1)

# ---------- 4. nova secao 12 ----------
nova_secao = """<h2 id="ambientes">12. Em que ambiente isso é possível</h2>

<p>Chegando aqui, o leitor tem uma pergunta legítima e muito concreta: entendi guias, sensores e skills, mas onde exatamente eu faço isso. A resposta importa mais do que parece, porque a maior parte da frustração com agentes não vem do modelo nem do método. Vem de tentar montar um controle que o ambiente escolhido não sustenta.</p>

<p>Ferramentas mudam de nome e de dono depressa demais para servirem de estrutura em um texto que você vai usar por anos. Então vale organizar por classe de ambiente, que muda muito mais devagar.</p>

<table class="wrap">
<thead><tr><th>Classe de ambiente</th><th>O que ele aceita</th><th>Faixa viável</th></tr></thead>
<tbody>
<tr><td>Conversa com instruções</td><td>Guia sim. Sensor quase nenhum, porque não há execução nem estado que sobreviva à conversa</td><td>N0 a N1</td></tr>
<tr><td>Agente com arquivos e execução</td><td>Guia, verificação dura, memória fora da conversa, código determinístico rodando de verdade</td><td>N1 a N2</td></tr>
<tr><td>Orquestração programada</td><td>Tudo acima, mais laço com teto, política de alçada fora do modelo e registro por execução</td><td>N2 a N3</td></tr>
<tr><td>Geração assistida de software</td><td>Produz o artefato. O harness relevante é o do que foi gerado, não o do gerador</td><td>Não se aplica</td></tr>
</tbody>
</table>

<p>A <strong>conversa com instruções</strong> é onde quase todo mundo começa, e ela é honesta dentro do seu limite. Você escreve um guia, define um tom, dá exemplos, e obtém consistência real. O que não existe ali é sensor: não há como o sistema rodar uma conferência, comparar contra a fonte e se corrigir antes de você ler. Toda verificação é sua, depois. É por isso que esse ambiente sustenta bem tarefas reversíveis e sustenta mal qualquer coisa que precise de evidência.</p>

<p>O <strong>agente com arquivos e execução</strong> é o primeiro degrau em que o ciclo fecha sozinho. Existe sistema de arquivos, então existe estado que sobrevive entre sessões. Existe execução, então existe verificação dura. É aqui que o skill do capítulo anterior deixa de ser um documento bonito e passa a ser um mecanismo, porque o critério de pronto vira a saída de um comando.</p>

<p>A <strong>orquestração programada</strong> é onde entram as coisas que não são texto: o teto de tentativas que o sistema não pode ignorar, a tabela de alçada que ele não consegue reescrever, o registro que ele não consegue apagar. Note que nenhuma dessas três é uma instrução. São restrições do lado de fora. É por isso que N3 exige esse ambiente e não é alcançável apenas escrevendo melhor.</p>

<p>A <strong>geração assistida de software</strong> merece um parágrafo próprio, porque é a confusão mais comum. Quando alguém descreve um sistema em linguagem natural e recebe uma aplicação funcionando, essa pessoa não montou um harness. Ela gerou um artefato. E esse artefato, se for para produção, precisa exatamente de tudo o que este artigo descreve: contrato, verificação, alçada e registro. A ferramenta que gerou não fornece nada disso ao que foi gerado.</p>

<blockquote><p>A maior parte das frustrações com agentes vem de tentar operar em N2 dentro de um ambiente que só sustenta N1. O sistema não está falhando. Ele está sendo cobrado por um controle que ninguém lhe deu como construir.</p></blockquote>

<p>Uma consequência prática disso, para quem decide: a pergunta de compra não é qual ferramenta é a melhor. É até que faixa de autonomia eu preciso chegar nesta tarefa específica, e qual é a classe de ambiente mais simples que sustenta aquela faixa. Comprar acima da necessidade custa complexidade que ninguém vai manter. Comprar abaixo produz exatamente o acidente descrito na abertura da parte 1.</p>

<p>Nomes de produto, repositórios e roteiros de instalação ficam em um documento companheiro desta série, a caixa de ferramentas, que é datada e revisada separadamente justamente porque envelhece mais rápido que o resto.</p>

"""

s = s.replace('<h2 id="evolucao">13. Como um harness evolui</h2>', nova_secao + '<h2 id="evolucao">13. Como um harness evolui</h2>')

# ---------- 5. ponte para a parte 3 ganha o risco de terceiros ----------
s = s.replace(
'<p>A parte 3 trata do que sobra quando essa camada já funciona',
'<p>E há um quarto risco, que nasce no momento em que você começa a usar guias e sensores de terceiros: instalar uma skill de outra pessoa é executar instrução de outra pessoa dentro do seu ambiente. A recomendação de quem publica o formato é explícita, instale apenas de origem confiável e audite antes de usar, prestando atenção especial a trechos que mandam o sistema buscar algo em rede externa. Isso não é motivo para não usar. É motivo para ler antes.</p>\n\n<p>A parte 3 trata do que sobra quando essa camada já funciona')

open(p, 'w', encoding='utf-8').write(s)
print('patch aplicado')
