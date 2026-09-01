# -*- coding: utf-8 -*-
# Monta docs/logbook.html trilingue a partir de
# docs/assets/logbook-metrics.json (gerado por
# build/generate_logbook_metrics.py). Reusa o envoltorio CSS e o
# JavaScript trilingue de harness-p2.html, mesmo padrao das outras
# pecas. Reexecutavel: os graficos e a linha do tempo sao gerados a
# partir do JSON, nunca escritos a mao.
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(ROOT, 'docs', 'assets', 'logbook-metrics.json'), encoding='utf-8') as fh:
    DATA = json.load(fh)

MS = DATA['milestones']
REMAINING = DATA['tokens_since_last_commit']

# ---------- traducao das mensagens de commit, uma vez, por hash ----------
COMMIT_TXT = {
    'a732861': {
        'pt': 'Commit inicial. O repositório vai ao ar com o que já existia: as partes 1 e 2 em português, a skill de briefing, o inventário de fontes.',
        'en': 'Initial commit. The repository goes live with what already existed: parts 1 and 2 in Portuguese, the briefing skill, the source inventory.',
        'es': 'Commit inicial. El repositorio sale a la luz con lo que ya existía: las partes 1 y 2 en portugués, la skill de briefing, el inventario de fuentes.',
    },
    '1271135': {
        'pt': 'Guia compacto reescrito, organizado pelos cinco passos do MEDIR em vez de por categoria de produto. Dezessete fichas de seis campos, diagnóstico de faixa no início, crítica registrada em cada passo.',
        'en': 'Compact guide rewritten, organised by the five MEDIR steps instead of by product category. Seventeen six-field entries, a tier diagnostic at the start, a registered critique in every step.',
        'es': 'Guía compacta reescrita, organizada por los cinco pasos del MEDIR en vez de por categoría de producto. Diecisiete fichas de seis campos, diagnóstico de banda al inicio, crítica registrada en cada paso.',
    },
    'f5fbfa7': {
        'pt': 'Parte 2 traduzida para inglês e espanhol. O documento vira trilíngue, glossário e fontes replicados nos três idiomas, exemplos de skill traduzidos por completo.',
        'en': 'Part 2 translated into English and Spanish. The document becomes trilingual, glossary and sources replicated in all three languages, skill examples translated in full.',
        'es': 'Parte 2 traducida al inglés y al español. El documento se vuelve trilingüe, glosario y fuentes replicados en los tres idiomas, ejemplos de skill traducidos por completo.',
    },
    '111933a': {
        'pt': 'Trinta skills de terceiro instaladas para uso no projeto, auditadas antes de instalar. FERRAMENTAS.md criado como registro vivo do que é usado de fato (renomeado TOOLS.md em 30 de agosto de 2026, na reestruturação para inglês primário).',
        'en': 'Thirty third-party skills installed for use on the project, audited before installing. FERRAMENTAS.md created as a living record of what is actually used (renamed TOOLS.md on 30 August 2026, in the English-primary restructuring).',
        'es': 'Treinta skills de terceros instaladas para uso en el proyecto, auditadas antes de instalar. FERRAMENTAS.md creado como registro vivo de lo que realmente se usa (renombrado TOOLS.md el 30 de agosto de 2026, en la reestructuración a inglés primario).',
    },
    '51af961': {
        'pt': 'Correção: a skill própria do projeto, levantando-briefing, estava documentada junto das de terceiro. Separada, e ativada de fato neste ambiente.',
        'en': 'Fix: the project’s own skill, levantando-briefing, was documented alongside the third-party ones. Separated, and actually activated in this environment.',
        'es': 'Corrección: la skill propia del proyecto, levantando-briefing, estaba documentada junto con las de terceros. Separada, y activada de verdad en este entorno.',
    },
    '38444ac': {
        'pt': 'levantando-briefing ganha repositório próprio e público, no mesmo padrão das demais skills citadas. O harness-medir passa a só apontar para ela.',
        'en': 'levantando-briefing gets its own public repository, in the same pattern as the other cited skills. harness-medir now only points to it.',
        'es': 'levantando-briefing gana repositorio propio y público, en el mismo patrón que las demás skills citadas. harness-medir pasa a solo apuntar hacia allí.',
    },
    '3000e88': {
        'pt': 'Diário de bordo criado, trilíngue, gerado do git e do uso real da sessão. GitHub Pages ativado, com .nojekyll para servir os HTML como estão.',
        'en': 'Project log created, trilingual, generated from git and the session’s real usage. GitHub Pages enabled, with .nojekyll to serve the HTML files as they are.',
        'es': 'Diario de bordo creado, trilingüe, generado a partir de git y del uso real de la sesión. GitHub Pages activado, con .nojekyll para servir los HTML tal cual.',
    },
    '9d3892f': {
        'pt': 'Início da reestruturação para inglês primário. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md e as demais peças renomeadas para inglês, idioma padrão das peças já trilíngues trocado de PT para EN, aviso de idioma do navegador adicionado.',
        'en': 'Start of the English-primary restructuring. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md and the other pieces renamed to English, default tab of the already-trilingual pieces switched from PT to EN, browser-language hint added.',
        'es': 'Inicio de la reestructuración hacia el inglés primario. PADROES.md, ESTADO.md, PROXIMOS-PASSOS.md, FERRAMENTAS.md y las demás piezas renombradas al inglés, pestaña predeterminada de las piezas ya trilingües cambiada de PT a EN, pista de idioma del navegador añadida.',
    },
    '65d9c1e': {
        'pt': 'Guia compacto traduzido para inglês e espanhol, com inglês como aba padrão. Repositório da skill de briefing renomeado de levantando-briefing para intake-briefing.',
        'en': 'Compact guide translated into English and Spanish, with English as the default tab. The briefing skill’s repository renamed from levantando-briefing to intake-briefing.',
        'es': 'Guía compacta traducida al inglés y al español, con el inglés como pestaña predeterminada. Repositorio de la skill de briefing renombrado de levantando-briefing a intake-briefing.',
    },
    '1106102': {
        'pt': 'README, STANDARDS, STATUS, NEXT-STEPS e TOOLS reescritos em inglês como versão primária, cada um com tradução completa em português e espanhol. Fecha a reestruturação para inglês primário nos dois repositórios públicos.',
        'en': 'README, STANDARDS, STATUS, NEXT-STEPS and TOOLS rewritten in English as the primary version, each with a full Portuguese and Spanish translation. Closes the English-primary restructuring across both public repositories.',
        'es': 'README, STANDARDS, STATUS, NEXT-STEPS y TOOLS reescritos en inglés como versión primaria, cada uno con traducción completa al portugués y al español. Cierra la reestructuración hacia el inglés primario en los dos repositorios públicos.',
    },
    'd8ff518': {
        'pt': 'Diário de bordo regerado sobre o histórico real completo até aqui, quatro marcos novos documentados: a criação do próprio diário, o início e o fechamento da reestruturação para inglês primário, a tradução do guia compacto. Fecha a sessão 1.',
        'en': 'Project log regenerated over the full real history so far, four new milestones documented: the log’s own creation, the start and close of the English-primary restructuring, the compact guide’s translation. Closes session 1.',
        'es': 'Diario de bordo regenerado sobre el historial real completo hasta aquí, cuatro hitos nuevos documentados: la creación del propio diario, el inicio y el cierre de la reestructuración hacia el inglés primario, la traducción de la guía compacta. Cierra la sesión 1.',
    },
    'bb19deb': {
        'pt': 'Sessão 2. Quatro skills recomendadas de fora avaliadas (ponytail, no-ai-slop, taste-skill, impeccable) por relevância, manutenção, contribuidores e licença. Só impeccable adotada, como décima oitava ficha do guia compacto, em Inspecionar.',
        'en': 'Session 2. Four externally recommended skills evaluated (ponytail, no-ai-slop, taste-skill, impeccable) on relevance, maintenance, contributors and licence. Only impeccable adopted, as the compact guide’s eighteenth entry, in Inspect.',
        'es': 'Sesión 2. Cuatro skills recomendadas desde afuera evaluadas (ponytail, no-ai-slop, taste-skill, impeccable) por relevancia, mantenimiento, colaboradores y licencia. Solo impeccable adoptada, como la decimoctava ficha de la guía compacta, en Inspeccionar.',
    },
    'dbeb0c1': {
        'pt': 'Diário de bordo regerado para incluir o marco da curadoria de impeccable.',
        'en': 'Project log regenerated to include the impeccable curation milestone.',
        'es': 'Diario de bordo regenerado para incluir el hito de la curaduría de impeccable.',
    },
    'c5a3fa0': {
        'pt': 'Dossiê de trabalho para as partes 3 e 4 adicionado: diagnóstico em três camadas, sete eixos de pesquisa da parte 3 já com fontes verificadas, especificação de dez diagramas. Propõe uma quarta parte para a série, ainda não formalizada em README.md nem em STATUS.md por decisão explícita.',
        'en': 'Working dossier for parts 3 and 4 added: a three-layer diagnosis, seven research axes for part 3 already with verified sources, a ten-diagram specification. Proposes a fourth part for the series, not yet formalised in README.md or STATUS.md by explicit decision.',
        'es': 'Dosier de trabajo para las partes 3 y 4 añadido: diagnóstico en tres capas, siete ejes de investigación de la parte 3 ya con fuentes verificadas, especificación de diez diagramas. Propone una cuarta parte para la serie, todavía no formalizada en README.md ni en STATUS.md por decisión explícita.',
    },
    '223b64a': {
        'pt': 'Diário de bordo regerado para incluir os marcos que faltavam: a regeneração anterior do próprio diário, e o dossiê de trabalho das partes 3 e 4. O diário tinha ficado uma sessão atrasado em relação ao git.',
        'en': 'Project log regenerated to include the milestones that were missing: the log’s own previous regeneration, and the working dossier for parts 3 and 4. The log had fallen one session behind the git history.',
        'es': 'Diario de bordo regenerado para incluir los hitos que faltaban: la regeneración anterior del propio diario, y el dosier de trabajo de las partes 3 y 4. El diario se había quedado una sesión atrás respecto al historial de git.',
    },
    '35cc04d': {
        'pt': 'Fecha os três primeiros itens da fila do dossiê de partes 3 e 4: os documentos de governança passam a descrever quatro partes em três camadas, 32 fontes de pesquisa entram no inventário, nove diagramas Mermaid viram SVG desenhado à mão, prontos para as duas peças ainda não escritas.',
        'en': 'Closes the first three items of the parts 3 and 4 dossier’s work queue: the governance documents now describe four parts across three layers, 32 research sources enter the inventory, nine Mermaid sketches become hand-drawn SVG, ready for the two pieces still unwritten.',
        'es': 'Cierra los tres primeros elementos de la cola de trabajo del dosier de las partes 3 y 4: los documentos de gobernanza ahora describen cuatro partes en tres capas, 32 fuentes de investigación entran al inventario, nueve bocetos Mermaid se convierten en SVG dibujado a mano, listos para las dos piezas todavía sin escribir.',
    },
    '059d3f6': {
        'pt': 'Corrige a redação da regra de diagramas, que sugeria um pipeline automático de Mermaid para SVG nunca usado neste projeto, e registra a proteção de branch configurada na main via API do GitHub.',
        'en': 'Fixes the diagrams rule’s wording, which had suggested an automatic Mermaid-to-SVG pipeline this project never used, and records the branch protection configured on main via the GitHub API.',
        'es': 'Corrige la redacción de la regla de diagramas, que sugería una canalización automática de Mermaid a SVG que este proyecto nunca usó, y registra la protección de rama configurada en main vía la API de GitHub.',
    },
    'b81f378': {
        'pt': 'Diário de bordo regerado para incluir os marcos M15 a M17: o dossiê de trabalho das partes 3 e 4, o fechamento dos três primeiros itens da fila do dossiê, e a correção da regra de diagramas junto com a proteção de branch.',
        'en': 'Project log regenerated to include milestones M15 to M17: the parts 3 and 4 working dossier, the closing of the first three items of the dossier’s queue, and the diagrams rule fix alongside the branch protection.',
        'es': 'Diario de bordo regenerado para incluir los hitos M15 a M17: el dosier de trabajo de las partes 3 y 4, el cierre de los tres primeros elementos de la cola del dosier, y la corrección de la regla de diagramas junto con la protección de rama.',
    },
    '67f08a5': {
        'pt': 'Renderiza os nove SVGs dos diagramas pela primeira vez, via Chrome headless, e corrige cinco bugs reais de sobreposição de coordenada achados só por inspeção visual (texto cortado, conector duplicado, legenda estourando o canvas, linha atravessando caixa, colunas sobrepostas). Gera um PNG por diagrama para publicação no Medium.',
        'en': 'Renders the nine diagram SVGs for the first time, via headless Chrome, and fixes five real coordinate-overlap bugs found only by visual inspection (text cut by a line, a duplicate connector, a caption overflowing the canvas, a line crossing a box, overlapping columns). Generates one PNG per diagram for Medium publication.',
        'es': 'Renderiza los nueve SVG de los diagramas por primera vez, vía Chrome headless, y corrige cinco bugs reales de superposición de coordenadas encontrados solo por inspección visual (texto cortado, conector duplicado, leyenda desbordando el lienzo, línea atravesando una caja, columnas superpuestas). Genera un PNG por diagrama para publicación en Medium.',
    },
    'd1babbd': {
        'pt': 'Mergeia direto na main a validação dos diagramas e os PNGs para o Medium, por decisão do autor.',
        'en': 'Merges the diagram validation and the Medium PNGs directly into main, by the author’s decision.',
        'es': 'Mergea directamente en main la validación de los diagramas y los PNG para Medium, por decisión del autor.',
    },
    '6f1c33e': {
        'pt': 'Escreve a parte 3 completa nos três idiomas, com os cinco diagramas embutidos e totalmente traduzidos, e refaz a arquitetura de navegação da série: uma barra de topo única, centralizada e reativa ao idioma, e um glossário e uma página de fontes compartilhados, substituindo o que cada artigo carregava separado.',
        'en': 'Writes part 3 in full, all three languages, with the five diagrams inline and fully translated, and rebuilds the series’ navigation architecture: a single, centred, language-reactive top bar, and a shared glossary and sources page, replacing what each article used to carry on its own.',
        'es': 'Escribe la parte 3 completa en los tres idiomas, con los cinco diagramas incorporados y totalmente traducidos, y rehace la arquitectura de navegación de la serie: una barra superior única, centrada y reactiva al idioma, y un glosario y una página de fuentes compartidos, reemplazando lo que cada artículo llevaba por separado.',
    },
    '395c6cc': {
        'pt': 'Mergeia direto na main a parte 3 completa e a nova arquitetura de série, por decisão do autor.',
        'en': 'Merges the completed part 3 and the new series architecture directly into main, by the author’s decision.',
        'es': 'Mergea directamente en main la parte 3 completa y la nueva arquitectura de serie, por decisión del autor.',
    },
    '33a92e9': {
        'pt': 'Diário de bordo regerado, e três bugs reais corrigidos no processo: a contagem de palavras publicadas ignorava a parte 3, o glossário e as fontes, prestes a mostrar queda entre marcos onde na verdade houve crescimento; o extrator do envoltório cortava no marcador errado desde que a barra de topo chegou, arrastando a barra de série inteira para dentro do diário; o gráfico de crescimento sobrepunha rótulos vizinhos a partir de um certo número de marcos. Os três corrigidos na fonte, vinte e dois marcos completos.',
        'en': 'Project log regenerated, and three real bugs fixed along the way: the published-word count skipped part 3, the glossary and the sources page, about to show a fall between milestones where growth had actually happened; the shell extractor cut on the wrong marker once the top bar arrived, dragging the whole series bar into the log; the growth chart’s point labels started overlapping past a certain number of milestones. All three fixed at the source, twenty-two milestones complete.',
        'es': 'Diario de bordo regenerado, y tres bugs reales corregidos en el proceso: el conteo de palabras publicadas se saltaba la parte 3, el glosario y la página de fuentes, a punto de mostrar una caída entre hitos donde en realidad hubo crecimiento; el extractor del envoltorio cortaba en el marcador equivocado desde que llegó la barra superior, arrastrando la barra de serie entera hacia el diario; el gráfico de crecimiento superponía etiquetas vecinas a partir de cierto número de hitos. Los tres corregidos en la fuente, veintidós hitos completos.',
    },
    '241f320': {
        'pt': 'README atualizado nas três línguas: ganha uma linha apontando para o GitHub Pages publicado, a árvore de arquivos passa a listar a parte 3 e os dois companheiros compartilhados, e dois diagramas (D6, as três camadas do framework, e D1, a separação de poderes) entram como imagem, usando o PNG de fundo branco em vez do SVG de fundo transparente, ilegível no tema escuro do GitHub.',
        'en': 'README updated in all three languages: gains a line pointing at the published GitHub Pages site, the file tree now lists part 3 and the two shared companions, and two diagrams (D6, the framework’s three layers, and D1, the separation of powers) are embedded as images, using the white-background PNG rather than the transparent-background SVG, illegible in GitHub’s dark theme.',
        'es': 'README actualizado en los tres idiomas: gana una línea que apunta al GitHub Pages publicado, el árbol de archivos ahora lista la parte 3 y los dos compañeros compartidos, y dos diagramas (D6, las tres capas del marco, y D1, la separación de poderes) se incorporan como imagen, usando el PNG de fondo blanco en vez del SVG de fondo transparente, ilegible en el tema oscuro de GitHub.',
    },
    'b31515a': {
        'pt': 'A pesquisa da parte 4 chega pronta, seis eixos, entregue pelo autor fora da sessão, e passa por verificação de fonte primária nos dois achados mais carregados: o caso SCHUFA do TJUE, que torna a taxa de reprovação no portão exposição jurídica, e o caso das 20.225 contas do Instagram, que abre a peça. Quatro ajustes aplicados, as três fontes do SCHUFA separadas, a fonte de patente do quase-acidente trocada pelo triângulo de Heinrich, o par Kyndryl verificado na origem, o número da Gartner não localizado e mantido como parcial, e vinte e nove fontes integradas ao inventário.',
        'en': 'Part 4’s research arrives complete, six axes, delivered by the author outside the session, and goes through primary-source verification on its two most load-bearing findings: the CJEU’s SCHUFA case, which turns the gate rejection rate into legal exposure, and the 20,225-account Instagram case, which opens the piece. Four adjustments applied, the three SCHUFA sources separated, the near-miss patent source swapped for Heinrich’s triangle, the Kyndryl pair verified at the source, the Gartner figure not located and kept partial, and twenty-nine sources integrated into the inventory.',
        'es': 'La investigación de la parte 4 llega completa, seis ejes, entregada por el autor fuera de la sesión, y pasa por verificación de fuente primaria en sus dos hallazgos más cargados: el caso SCHUFA del TJUE, que convierte la tasa de rechazo en la puerta en exposición jurídica, y el caso de las 20.225 cuentas de Instagram, que abre la pieza. Cuatro ajustes aplicados, las tres fuentes del SCHUFA separadas, la fuente de patente del cuasi-accidente cambiada por el triángulo de Heinrich, el par de Kyndryl verificado en el origen, el número de Gartner no localizado y mantenido como parcial, y veintinueve fuentes integradas al inventario.',
    },
    'd972a35': {
        'pt': 'Eixo 0 adicionado ao dossiê da parte 4: uma observação de campo, um protótipo de terceiro mostrado informalmente ao autor. Uma correção recebida do próprio autor evitou um erro que teria sido grave, descrever o protótipo como fonte primária do projeto; o texto final trata a convergência como evidência independente, sem citar produto, empresa ou pessoa, e sem reprodução sem autorização escrita.',
        'en': 'Axis 0 added to Part 4’s dossier: a field observation, a third party’s prototype shown informally to the author. A correction from the author himself caught an error that would have been serious, describing the prototype as this project’s primary source; the final text treats the convergence as independent evidence instead, naming no product, company or person, and reproducing nothing without written authorisation.',
        'es': 'Eje 0 añadido al dosier de la parte 4: una observación de campo, un prototipo de un tercero mostrado informalmente al autor. Una corrección del propio autor evitó un error que habría sido grave, describir el prototipo como fuente primaria del proyecto; el texto final trata la convergencia como evidencia independiente, sin nombrar producto, empresa o persona, y sin reproducir nada sin autorización escrita.',
    },
    'c4bd34c': {
        'pt': 'Diário de bordo regerado com quatro marcos novos: a regeração anterior que corrigiu três bugs, o README enriquecido com diagramas embutidos, a pesquisa da parte 4 verificada e integrada ao inventário de fontes, o eixo 0 corrigido. Vinte e seis marcos completos, 68.176 palavras publicadas.',
        'en': 'Project log regenerated with four new milestones: the previous regeneration that fixed three bugs, the README enriched with embedded diagrams, part 4’s research verified and integrated into the source inventory, axis 0 corrected. Twenty-six milestones complete, 68,176 words published.',
        'es': 'Diario de bordo regenerado con cuatro hitos nuevos: la regeneración anterior que corrigió tres bugs, el README enriquecido con diagramas incorporados, la investigación de la parte 4 verificada e integrada al inventario de fuentes, el eje 0 corregido. Veintiséis hitos completos, 68.176 palabras publicadas.',
    },
    'f7dd32b': {
        'pt': 'Parte 4 escrita por completo em inglês: o caso das 20.225 contas do Instagram como abertura, ciclo de vida do agente, quatro papéis ancorados no Modelo das Três Linhas do IIA, oito indicadores declarados como síntese, o indicador de reprovação no portão fundamentado no caso SCHUFA do TJUE. D10 desenhado do zero e validado por renderização. De brinde, quatro bugs reais preexistentes corrigidos: travessão proibido pelas próprias normas do projeto, e seis entradas do glossário fora de ordem alfabética em português e espanhol.',
        'en': 'Part 4 written in full in English: the 20,225-account Instagram case as the opening, the agent life cycle, four roles anchored in the IIA’s Three Lines Model, eight indicators declared as synthesis, the gate-rejection-rate indicator grounded in the CJEU’s SCHUFA ruling. D10 designed from scratch and validated by rendering. As a bonus, four real pre-existing bugs fixed: an em dash forbidden by the project’s own rules, and six glossary entries out of alphabetical order in Portuguese and Spanish.',
        'es': 'Parte 4 escrita por completo en inglés: el caso de las 20.225 cuentas de Instagram como apertura, ciclo de vida del agente, cuatro roles anclados en el Modelo de las Tres Líneas del IIA, ocho indicadores declarados como síntesis, el indicador de rechazo en el portón fundamentado en el caso SCHUFA del TJUE. D10 diseñado desde cero y validado por renderizado. De regalo, cuatro bugs reales preexistentes corregidos: un guion largo prohibido por las propias normas del proyecto, y seis entradas del glosario fuera de orden alfabético en portugués y español.',
    },
    'afff681': {
        'pt': 'Parte 4 completada em português (7.051 palavras) e espanhol (7.377 palavras), traduzida por dois agentes em paralelo a partir do inglês publicado. Os cinco diagramas traduzidos e validados à parte, um por um, renderizados isoladamente antes de entrar no artigo; achei e corrigi uma legenda truncada em espanhol nesse processo. A evolução para um playbook documentada, sem construir, nos dois locais que o projeto já usa para trabalho planejado.',
        'en': 'Part 4 completed in Portuguese (7,051 words) and Spanish (7,377 words), translated by two parallel agents from the published English. The five diagrams translated and validated separately, one by one, rendered standalone before entering the article; caught and fixed a truncated Spanish caption in that process. The playbook’s evolution documented, without building it, in the two places the project already uses for planned work.',
        'es': 'Parte 4 completada en portugués (7.051 palabras) y español (7.377 palabras), traducida por dos agentes en paralelo a partir del inglés publicado. Los cinco diagramas traducidos y validados aparte, uno por uno, renderizados aislados antes de entrar al artículo; encontré y corregí una leyenda truncada en español en ese proceso. La evolución hacia un playbook documentada, sin construirla, en los dos lugares que el proyecto ya usa para trabajo planeado.',
    },
    'd3d8f18': {
        'pt': 'O autor propôs trocar MEDIR por M.E.D.I.R. em toda a prosa, para deixar a sigla mais clara desde a partida. Levantamento honesto antes de executar: 245 ocorrências, nenhuma em minúscula fora de detalhe técnico. Recomendação dada e aceita, manter MEDIR sem pontos, porque a palavra só soa como o verbo medir de verdade escrita inteira. No lugar, duas correções reais: a palavra MEDIR passa a levar o tratamento de glossário que nunca tinha em nenhum lugar, e a parte 1 e o README passam a dizer explicitamente que MEDIR também é medir.',
        'en': 'The author proposed replacing MEDIR with M.E.D.I.R. throughout the prose, to make the acronym clearer from the start. An honest count before acting: 245 occurrences, none lowercase outside technical detail. Recommendation given and accepted, keep MEDIR without periods, because the word only sounds like the real verb measure when written whole. Two real fixes went in instead: the word MEDIR now carries the glossary treatment it never had anywhere, and part 1 and the README now state explicitly that MEDIR is also the verb to measure.',
        'es': 'El autor propuso cambiar MEDIR por M.E.D.I.R. en toda la prosa, para dejar la sigla más clara desde el principio. Conteo honesto antes de actuar: 245 apariciones, ninguna en minúscula fuera de detalle técnico. Recomendación dada y aceptada, mantener MEDIR sin puntos, porque la palabra solo suena como el verbo medir de verdad cuando está escrita entera. En su lugar, dos correcciones reales: la palabra MEDIR ahora lleva el tratamiento de glosario que nunca tuvo en ningún lado, y la parte 1 y el README ahora dicen explícitamente que MEDIR también es medir.',
    },
    'dc492ac': {
        'pt': 'Diário de bordo regerado com quatro marcos novos: a regeração anterior (marcos M23 a M26), a parte 4 escrita em inglês com D10 e quatro bugs reais corrigidos, a parte 4 completada em português e espanhol com os diagramas validados e o playbook documentado, e o estudo do M.E.D.I.R. que manteve MEDIR e fechou duas lacunas reais de clareza. Trinta marcos completos, 94.127 palavras publicadas. De brinde, um bug real corrigido no próprio gerador: harness-p4.html nunca entrava na contagem de palavras desde que a página existe, subcontando o total publicado desde a parte 4 em inglês.',
        'en': 'Project log regenerated with four new milestones: the previous regeneration (M23 to M26), Part 4 written in English with D10 and four real bugs fixed, Part 4 completed in Portuguese and Spanish with the diagrams validated and the playbook documented, and the MEDIR-with-dots study that kept MEDIR and closed two real clarity gaps. Thirty milestones complete, 94,127 words published. As a bonus, a real bug fixed in the generator itself: harness-p4.html had never entered the word count since the page existed, undercounting the published total since Part 4 in English.',
        'es': 'Diario de bordo regenerado con cuatro hitos nuevos: la regeneración anterior (hitos M23 a M26), la parte 4 escrita en inglés con D10 y cuatro bugs reales corregidos, la parte 4 completada en portugués y español con los diagramas validados y el playbook documentado, y el estudio del M.E.D.I.R. que mantuvo MEDIR y cerró dos brechas reales de claridad. Treinta hitos completos, 94.127 palabras publicadas. De regalo, un bug real corregido en el propio generador: harness-p4.html nunca había entrado en el conteo de palabras desde que la página existe, subestimando el total publicado desde la parte 4 en inglés.',
    },
    '3586b9a': {
        'pt': 'AGENTS.md e llms.txt criados, o repositório passa a poder ser operado por um agente de IA, não só lido por um: protocolo de verificação obrigatório antes de instalar qualquer skill da curadoria, com saída explícita para quando não há acesso à rede. O diário de bordo ganhou visibilidade real no README, com os dois gráficos do projeto (palavras publicadas e tokens consumidos) incorporados como imagem, exportados do próprio diário pelo mesmo método de captura que os diagramas já usam.',
        'en': 'AGENTS.md and llms.txt created, the repository becomes operable by an AI agent, not only readable by one: a mandatory verification protocol before installing any curated skill, with an explicit exit path for when no network access exists. The project log gained real visibility in the README, with the project’s own two charts (words published and tokens consumed) embedded as images, exported from the log itself via the same capture method the diagrams already use.',
        'es': 'Se crearon AGENTS.md y llms.txt, el repositorio pasa a poder ser operado por un agente de IA, no solo leído por uno: un protocolo de verificación obligatorio antes de instalar cualquier skill de la curación, con una salida explícita para cuando no hay acceso a la red. El diario de bordo ganó visibilidad real en el README, con los dos gráficos propios del proyecto (palabras publicadas y tokens consumidos) incorporados como imagen, exportados del propio diario con el mismo método de captura que ya usan los diagramas.',
    },
    '48f6bae': {
        'pt': 'Diário de bordo regerado para incluir o marco da criação de AGENTS.md, llms.txt e a nova seção do próprio diário no README. build/build_logbook.py ganhou as traduções de commit que faltavam no dicionário (dc492ac e o próprio 3586b9a). Trinta e um marcos completos, 94.265 palavras publicadas, os dois gráficos do README reexportados do mesmo diário, para não ficarem um marco atrasados em relação a ele.',
        'en': 'Project log regenerated to include the milestone for AGENTS.md, llms.txt and the log’s own new section in the README. build/build_logbook.py gained the commit translations that were missing from the dictionary (dc492ac and 3586b9a itself). Thirty-one milestones complete, 94,265 words published, the README’s two charts re-exported from this same log, so they would not sit one milestone behind it.',
        'es': 'Diario de bordo regenerado para incluir el hito de la creación de AGENTS.md, llms.txt y la nueva sección del propio diario en el README. build/build_logbook.py ganó las traducciones de commit que faltaban en el diccionario (dc492ac y el propio 3586b9a). Treinta y un hitos completos, 94.265 palabras publicadas, los dos gráficos del README reexportados desde este mismo diario, para que no quedaran un hito atrasados respecto a él.',
    },
    '85b248b': {
        'pt': 'GitHub Pages checado pela primeira vez desde que foi ao ar: a URL nua dava 404 por falta de index.html na raiz, corrigido com um redirecionamento mínimo para harness-p1.html. README.md ganhou uma seção Installation completa, nas três línguas, duplicando de propósito as instruções já verificadas do repositório intake-briefing (skill pessoal, .agents/skills/ para Cursor, Codex CLI e Google Antigravity, Google AI Studio, plugin do Claude Code via marketplace), cada afirmação por fornecedor checada de novo, direto na documentação oficial. O card do intake-briefing no guia compacto ganhou o mesmo detalhe, e a cópia local da skill, que tinha ficado para trás do repositório canônico recém-reempacotado, foi ressincronizada.',
        'en': 'GitHub Pages checked for the first time since it went live: the bare URL 404’d for lack of an index.html at the root, fixed with a minimal redirect to harness-p1.html. README.md gained a full Installation section, all three languages, deliberately duplicating the intake-briefing repository’s own already-verified instructions (personal skill, .agents/skills/ for Cursor, Codex CLI and Google Antigravity, Google AI Studio, a Claude Code plugin from its marketplace), each vendor claim checked again, straight against the official documentation. The compact guide’s intake-briefing card gained the same detail, and the skill’s local copy, which had fallen behind the newly repackaged canonical repository, was resynced.',
        'es': 'GitHub Pages revisado por primera vez desde que se publicó: la URL desnuda daba 404 por falta de un index.html en la raíz, corregido con una redirección mínima a harness-p1.html. README.md ganó una sección Installation completa, en los tres idiomas, duplicando a propósito las instrucciones ya verificadas del repositorio intake-briefing (skill personal, .agents/skills/ para Cursor, Codex CLI y Google Antigravity, Google AI Studio, un plugin de Claude Code desde su marketplace), cada afirmación por proveedor revisada de nuevo, directo contra la documentación oficial. El card de intake-briefing en la guía compacta ganó el mismo detalle, y la copia local de la skill, que se había quedado atrás del repositorio canónico recién reempaquetado, se resincronizó.',
    },
    '05e82dd': {
        'pt': 'Diário de bordo regerado com dois marcos novos: o próprio commit anterior (a regeração do marco M31) e a correção da URL nua do GitHub Pages com a instalação multiferramenta do intake-briefing. Trinta e quatro marcos completos, 94.476 palavras publicadas, cerca de 1.026 milhões de tokens transacionados, os dois gráficos do README reexportados via Playwright/Chromium headless local para não ficarem um marco atrasados.',
        'en': 'Project log regenerated with two new milestones: the previous commit itself (the M31 regeneration) and the GitHub Pages bare-URL fix alongside the intake-briefing multi-tool installation. Thirty-four milestones complete, 94,476 words published, about 1,026 million tokens transacted, the README’s two charts re-exported via a local headless Playwright/Chromium so they would not sit one milestone behind.',
        'es': 'Diario de bordo regenerado con dos hitos nuevos: el propio commit anterior (la regeneración del hito M31) y la corrección de la URL desnuda de GitHub Pages junto con la instalación multiherramienta de intake-briefing. Treinta y cuatro hitos completos, 94.476 palabras publicadas, cerca de 1.026 millones de tokens transaccionados, los dos gráficos del README reexportados vía Playwright/Chromium headless local para que no quedaran un hito atrasados.',
    },
    'f613e93': {
        'pt': 'Ícone do diário adicionado à barra de série compartilhada, nas oito páginas HTML, com tooltip via title traduzido nas três línguas em vez de texto. docs/logbook.html ganhou a barra completa pela primeira vez. Dois bugs reais achados e corrigidos no processo: a injeção do CSS do aviso de idioma em build_p2.py não era idempotente e vinha duplicando o bloco a cada regeração havia sessões (sete cópias acumuladas), e um atributo data-icon sem valor virava string vazia, falsa em JavaScript, quebrando a tradução do tooltip sem quebrar o link. Um terceiro quase-erro pego no caminho: o texto de instalação multiferramenta do card do intake-briefing tinha sido escrito só no HTML compilado, nunca na fonte, e quase se perdeu na primeira regeração desta rodada.',
        'en': 'Logbook icon added to the shared series bar, across all eight HTML pages, with a title-attribute tooltip translated in all three languages instead of text. docs/logbook.html gained the full bar for the first time. Two real bugs found and fixed along the way: the language-hint CSS injection in build_p2.py was not idempotent and had been duplicating the block on every regeneration for sessions (seven copies accumulated), and a bare data-icon attribute resolved to an empty, falsy string in JavaScript, breaking the tooltip’s translation without breaking its link. A third near-miss caught in passing: the intake-briefing card’s multi-tool installation text had been written only into the compiled HTML, never into its source, and nearly got lost on this round’s first regeneration.',
        'es': 'Ícono del diario añadido a la barra de serie compartida, en las ocho páginas HTML, con tooltip vía atributo title traducido en los tres idiomas en vez de texto. docs/logbook.html ganó la barra completa por primera vez. Dos bugs reales encontrados y corregidos en el camino: la inyección del CSS del aviso de idioma en build_p2.py no era idempotente y venía duplicando el bloque en cada regeneración desde hacía sesiones (siete copias acumuladas), y un atributo data-icon sin valor se resolvía como cadena vacía, falsa en JavaScript, rompiendo la traducción del tooltip sin romper su enlace. Un tercer casi-error atrapado de paso: el texto de instalación multiherramienta del card de intake-briefing se había escrito solo en el HTML compilado, nunca en su fuente, y casi se pierde en la primera regeneración de esta ronda.',
    },
    'dd880e9': {
        'pt': 'Diário de bordo regerado com dois marcos novos: a regeração anterior dos marcos M33 e M34, e o ícone do diário na topbar, com os dois bugs reais corrigidos no processo (CSS do aviso de idioma duplicado, tooltip do ícone que não traduzia). Trinta e seis marcos completos, 94.345 palavras publicadas, cerca de 1.117,9 milhões de tokens transacionados, os dois gráficos do README reexportados via Playwright/Chromium headless local.',
        'en': 'Project log regenerated with two new milestones: the previous M33/M34 regeneration, and the log’s own icon in the topbar, with the two real bugs it exposed fixed along the way (a duplicated language-hint CSS block, an icon tooltip that failed to translate). Thirty-six milestones complete, 94,345 words published, about 1,117.9 million tokens transacted, the README’s two charts re-exported via a local headless Playwright/Chromium.',
        'es': 'Diario de bordo regenerado con dos hitos nuevos: la regeneración anterior de los hitos M33 y M34, y el ícono del diario en la topbar, con los dos bugs reales corregidos en el proceso (CSS del aviso de idioma duplicado, tooltip del ícono que no traducía). Treinta y seis hitos completos, 94.345 palabras publicadas, cerca de 1.117,9 millones de tokens transaccionados, los dos gráficos del README reexportados vía Playwright/Chromium headless local.',
    },
    'd34b9d1': {
        'pt': 'Dois problemas reais apontados pelo autor: a legenda do gráfico de palavras no diário ainda dizia "três peças" (partes 1, 2 e guia compacto), herdada de quando só essas existiam, embora o gerador já some sete peças há tempos — corrigido nas três línguas, com o mesmo erro achado por acaso no próprio guia compacto ("companheiro das partes 1, 2 e 3", faltando a parte 4). E harness-sources.html misturava, numa seção genérica sem rótulo, as fontes da parte 1 e da parte 2, dando a falsa impressão de que a parte 2 não tinha fonte própria — dividida em três seções (parte 1, 9 itens; parte 2, 1 item, já que a parte 2 nunca teve fase de dossiê como as partes 3 e 4; guia compacto, 7 itens que nunca apareceram no texto de nenhuma parte). Revisão pontual, sem marco novo no próprio diário por decisão do autor.',
        'en': 'Two real problems flagged by the author: the log’s words-published chart caption still said "three pieces" (parts 1, 2 and the compact guide), inherited from when only those existed, even though the generator has summed seven pieces for a while — fixed in all three languages, with the same error found by chance in the compact guide itself ("companion to parts 1, 2 and 3," missing part 4). And harness-sources.html mixed part 1’s and part 2’s sources into one unlabeled generic section, giving the false impression part 2 had no source of its own — split into three sections (part 1, 9 items; part 2, 1 item, since part 2 never went through a research-dossier phase like parts 3 and 4; the compact guide, 7 items that never appeared in any part’s text). A point fix, no new milestone in the log itself by the author’s decision.',
        'es': 'Dos problemas reales señalados por el autor: la leyenda del gráfico de palabras del diario todavía decía "tres piezas" (partes 1, 2 y la guía compacta), heredada de cuando solo esas existían, aunque el generador ya suma siete piezas desde hace tiempo — corregido en los tres idiomas, con el mismo error encontrado por casualidad en la propia guía compacta ("compañero de las partes 1, 2 y 3", sin la parte 4). Y harness-sources.html mezclaba, en una sección genérica sin etiqueta, las fuentes de la parte 1 y la parte 2, dando la falsa impresión de que la parte 2 no tenía fuente propia — dividida en tres secciones (parte 1, 9 elementos; parte 2, 1 elemento, ya que la parte 2 nunca pasó por una fase de dosier de investigación como las partes 3 y 4; guía compacta, 7 elementos que nunca aparecieron en el texto de ninguna parte). Revisión puntual, sin hito nuevo en el propio diario por decisión del autor.',
    },
    '691efb3': {
        'pt': 'Navegação: as quatro tabelas "onde você está" (partes 1 a 4) ficam idênticas em estrutura nas três línguas, cada uma linkando todas as outras partes existentes — a tabela da parte 1 não existia em EN/ES, partes 1 e 2 não linkavam a parte 3 nem tinham linha da parte 4, e 6 links da parte 2 apontavam pro idioma errado no guia compacto. Erros de fato corrigidos: a ressalva dos "43% da Gartner" (parte 4) estava isolada numa nota de rodapé apontando pra seção errada; a notificação de incidente em 15 dias do AI Act estava atribuída ao artigo 26 em vez do 73; a publicação original da Meta sobre a regra de dois e mais 3 fontes marcadas "não localizada" foram encontradas; 1 link morto virou nota honesta; mais 6 fontes citadas com detalhes que as páginas não sustentam foram corrigidas. Criada a classe .src (sublinhado sólido) e inseridos 211 links de citação nas partes 1 a 4, ligando afirmações reais do texto (caso Air Canada, estatísticas, estudos) às fontes correspondentes, antes completamente desconectadas. Onde não existe fonte real, a lacuna foi assinalada em vez de citação inventada.',
        'en': 'Navigation: the four "where you are" tables (parts 1 to 4) become identical in structure across all three languages, each linking every other existing part — part 1’s table did not exist in EN/ES, parts 1 and 2 did not link part 3 or carry a part 4 row, and 6 part-2 links pointed at the wrong language in the compact guide. Factual corrections: the "Gartner 43%" caveat (part 4) sat isolated in a footnote pointing at the wrong section; the AI Act’s 15-day incident notification was attributed to article 26 instead of 73; Meta’s original rule-of-two publication and 3 other "not located" sources were found; 1 dead link became an honest note; 6 more sources cited with details their pages don’t support were corrected. A new .src class (solid underline) was created and 211 citation links inserted across parts 1 to 4, tying real claims in the text (the Air Canada case, statistics, studies) to their matching sources, previously completely disconnected. Where no real source exists, the gap was flagged rather than fabricated.',
        'es': 'Navegación: las cuatro tablas "dónde estás" (partes 1 a 4) quedan idénticas en estructura en los tres idiomas, cada una enlazando todas las demás partes existentes — la tabla de la parte 1 no existía en EN/ES, las partes 1 y 2 no enlazaban la parte 3 ni tenían fila de la parte 4, y 6 enlaces de la parte 2 apuntaban al idioma equivocado en la guía compacta. Correcciones de hecho: la salvedad del "43% de Gartner" (parte 4) estaba aislada en una nota al pie que apuntaba a la sección equivocada; la notificación de incidente en 15 días del AI Act estaba atribuida al artículo 26 en vez del 73; la publicación original de Meta sobre la regla de dos y otras 3 fuentes marcadas "no localizada" fueron encontradas; 1 enlace muerto se volvió una nota honesta; otras 6 fuentes citadas con detalles que sus páginas no sostienen fueron corregidas. Se creó la clase .src (subrayado sólido) y se insertaron 211 enlaces de cita en las partes 1 a 4, uniendo afirmaciones reales del texto (el caso Air Canada, estadísticas, estudios) con sus fuentes correspondientes, antes completamente desconectadas. Donde no existe una fuente real, la brecha quedó señalada en vez de una cita inventada.',
    },
    '441f26b': {
        'pt': 'Pesquisa dedicada, cruzada entre múltiplos agentes e validada de forma independente pelo autor em outras ferramentas de IA, fechando lacunas deixadas na rodada anterior. Parte 1: o ganho da LangChain (top 30 pro top 5, +13,7 pontos no Terminal Bench 2.0) e o paper de evolução automática de harness (arXiv 2606.14249, HarnessX/AEGIS) tinham os números certos mas nenhuma fonte localizável — agora têm, e Karpathy ganhou citação dos próprios posts que cunharam "vibe coding" e popularizaram "context engineering". Parte 2: a "categoria inteira de ferramentas" de limpeza de skills já tinha resposta parada no inventário interno do projeto (ai-slop-cleaner), nunca linkada — citação adicionada, alegação de categoria suavizada. Parte 3: as cinco estatísticas de cadeia de suprimento são reais, mas três das quatro "não foi caso isolado" eram o mesmo evento (a crise do OpenClaw/ClawHub de fevereiro de 2026) contado por três fornecedores diferentes, não quatro provas independentes — corrigida também uma atribuição errada (Koi Security descobriu o ClawHavoc, não a Antiy CERT). Parte 4: a citação da CloudEagle pros "824 mil identidades órfãs" nunca sustentou esse número (confirmado até pelo Wayback Machine) — a fonte real é o próprio relatório da Veza; o "89% dos pilotos" da Deloitte era conta errada (100 menos 11) de um número que ela de fato publicou; o caso de ransomware de 2025 ganhou fonte primária (Barracuda). sources/inventory.md atualizado, corpos em build/ sincronizados e confirmados por regeneração byte a byte.',
        'en': 'Dedicated research, cross-checked across multiple agents and independently validated by the author in other AI tools, closing gaps left open in the previous round. Part 1: LangChain’s benchmark climb (top 30 to top 5, +13.7 points on Terminal Bench 2.0) and the automated-harness-evolution paper (arXiv 2606.14249, HarnessX/AEGIS) had the right numbers but no locatable source — now they do, and Karpathy gained citations from his own posts that coined "vibe coding" and popularized "context engineering". Part 2: the "entire category of tools" for skill cleanup already had an answer sitting in the project’s own internal inventory (ai-slop-cleaner), never linked — citation added, the category claim softened. Part 3: the five supply-chain statistics are all real, but three of the four "not an isolated case" examples were the same event (the February 2026 OpenClaw/ClawHub crisis) reported by three different vendors, not four independent proofs — a wrong attribution was also fixed (Koi Security discovered ClawHavoc, not Antiy CERT). Part 4: the CloudEagle citation for "824,000 orphaned identities" never supported that number (confirmed even via the Wayback Machine) — the real source is Veza’s own report; Deloitte’s "89% of pilots" was a miscalculated complement (100 minus 11) of a number the firm actually published; the 2025 ransomware case gained a primary source (Barracuda). sources/inventory.md updated, build/ bodies synced and confirmed via byte-for-byte regeneration.',
        'es': 'Investigación dedicada, cruzada entre múltiples agentes y validada de forma independiente por el autor en otras herramientas de IA, cerrando brechas dejadas en la ronda anterior. Parte 1: el salto de LangChain (top 30 a top 5, +13,7 puntos en Terminal Bench 2.0) y el paper de evolución automática de harness (arXiv 2606.14249, HarnessX/AEGIS) tenían los números correctos pero ninguna fuente localizable — ahora la tienen, y Karpathy ganó citas de sus propias publicaciones que acuñaron "vibe coding" y popularizaron "context engineering". Parte 2: la "categoría entera de herramientas" de limpieza de skills ya tenía respuesta esperando en el inventario interno del proyecto (ai-slop-cleaner), nunca enlazada — cita añadida, alegación de categoría suavizada. Parte 3: las cinco estadísticas de cadena de suministro son reales, pero tres de las cuatro "no fue un caso aislado" eran el mismo evento (la crisis de OpenClaw/ClawHub de febrero de 2026) contado por tres proveedores distintos, no cuatro pruebas independientes — se corrigió también una atribución errónea (Koi Security descubrió ClawHavoc, no Antiy CERT). Parte 4: la cita de CloudEagle para "824 mil identidades huérfanas" nunca sostuvo ese número (confirmado incluso vía Wayback Machine) — la fuente real es el propio informe de Veza; el "89% de los pilotos" de Deloitte era una cuenta errónea (100 menos 11) de un número que la firma sí publicó; el caso de ransomware de 2025 ganó fuente primaria (Barracuda). sources/inventory.md actualizado, cuerpos en build/ sincronizados y confirmados por regeneración byte a byte.',
    },
    '636b8ca': {
        'pt': 'Diário de bordo regerado com quatro marcos novos: a regeração anterior (M35/M36), o ícone do diário na topbar, e as duas rodadas de correção de citação do dia (navegação entre partes, localização de fontes primárias). Quarenta marcos completos, 99.849 palavras publicadas, cerca de 1.292,6 milhões de tokens transacionados. Os dois gráficos do README reexportados a partir deste mesmo diário, via Chrome headless local com escala de dispositivo 2x nativa. Um bug real corrigido no processo: a primeira tentativa de exportação tinha dobrado manualmente o tamanho da fonte pra compensar a escala 2x, sobrepondo os rótulos do eixo X a partir de 40 marcos; corrigido renderizando em tamanho nativo com escala de dispositivo real, que o Chrome já trata sozinho.',
        'en': 'Project log regenerated with four new milestones: the previous regeneration (M35/M36), the log’s icon in the topbar, and the day’s two citation-correction rounds (navigation between parts, primary-source location). Forty milestones complete, 99,849 words published, about 1,292.6 million tokens transacted. The README’s two charts re-exported from this same log, via local headless Chrome at a native 2x device scale. A real bug fixed along the way: the first export attempt had manually doubled the font size to compensate for the 2x scale, overlapping the x-axis labels past 40 milestones; fixed by rendering at native size with real device scaling, which Chrome already handles on its own.',
        'es': 'Diario de bordo regenerado con cuatro hitos nuevos: la regeneración anterior (M35/M36), el ícono del diario en la topbar, y las dos rondas de corrección de citas del día (navegación entre partes, localización de fuentes primarias). Cuarenta hitos completos, 99.849 palabras publicadas, cerca de 1.292,6 millones de tokens transaccionados. Los dos gráficos del README reexportados desde este mismo diario, vía Chrome headless local con escala de dispositivo 2x nativa. Un bug real corregido en el proceso: el primer intento de exportación había duplicado manualmente el tamaño de fuente para compensar la escala 2x, superponiendo las etiquetas del eje X a partir de 40 hitos; corregido renderizando a tamaño nativo con escala de dispositivo real, que Chrome ya maneja por sí solo.',
    },
    '4d94744': {
        'pt': 'Cinco entradas marcadas P (fonte não lida diretamente) no inventário de fontes já tinham sido de fato resolvidas em harness-sources.html mas nunca sincronizadas de volta: a publicação original da Meta sobre a regra de dois, a decisão original do caso Air Canada, a página da AIUC-1, o paper arXiv da delegação autenticada, e o comunicado do caso SCHUFA. NEXT-STEPS.md fecha o item da regra de dois, já resolvido mas não marcado, e registra um item novo: uma pergunta direta sobre a skill research (instalada, auditada, nunca citada nominalmente) expôs uma lacuna maior — partes 3 e 4 não citam nenhuma ferramenta concreta de terceiro pro próprio argumento, ao contrário da parte 2. Processo de quatro perguntas registrado pra repetir a cada skill considerada.',
        'en': 'Five entries marked P (source not read directly) in the source inventory had in fact already been resolved in harness-sources.html but never synced back: the original Meta rule-of-two publication, the original Air Canada case decision, the AIUC-1 page, the authenticated-delegation arXiv paper, and the SCHUFA case press release. NEXT-STEPS.md closes the rule-of-two item, already resolved but unmarked, and logs a new one: a direct question about the research skill (installed, audited, never named) exposed a bigger gap — parts 3 and 4 cite no concrete third-party tool for their own argument, unlike part 2. A four-question process was recorded to repeat for every skill considered from here on.',
        'es': 'Cinco entradas marcadas P (fuente no leída directamente) en el inventario de fuentes ya se habían resuelto de hecho en harness-sources.html pero nunca se sincronizaron de vuelta: la publicación original de Meta sobre la regla de dos, la decisión original del caso Air Canada, la página de AIUC-1, el paper de arXiv sobre delegación autenticada, y el comunicado del caso SCHUFA. NEXT-STEPS.md cierra el ítem de la regla de dos, ya resuelto pero sin marcar, y registra uno nuevo: una pregunta directa sobre la skill research (instalada, auditada, nunca citada nominalmente) expuso una brecha mayor — las partes 3 y 4 no citan ninguna herramienta concreta de terceros para su propio argumento, a diferencia de la parte 2. Se registró un proceso de cuatro preguntas para repetir con cada skill considerada de aquí en adelante.',
    },
    '8933aa7': {
        'pt': 'Achado por verificação direta, não por leitura de NEXT-STEPS.md: build/body_sources_*.html não era tocado desde a última regeneração anterior às duas rodadas de correção de citação do dia, que editaram harness-sources.html diretamente sem atualizar a fonte da verdade declarada em build/. Rodar build_sources.py do jeito que estava reverteria dezoito citações corrigidas de volta ao estado errado ou não localizado, sem aviso nenhum. Corrigido extraindo os três corpos atuais e corretos do harness-sources.html vigente e regravando em build/, mesmo padrão autocurativo que build_p2.py já usa. Duas cópias inofensivas da mesma causa raiz corrigidas junto: harness-glossary.html e harness-toolkit.html sem a classe CSS de tooltip de citação .src. build/README.md ganhou um parágrafo nomeando o risco.',
        'en': 'Found by direct verification, not by reading NEXT-STEPS.md: build/body_sources_*.html had not been touched since the regeneration before the day’s two citation-correction rounds, which edited harness-sources.html directly without updating the declared source of truth in build/. Running build_sources.py as it stood would have reverted eighteen corrected citations back to their wrong or unlocated state, with no warning at all. Fixed by extracting the three current, correct bodies from the live harness-sources.html and writing them back into build/, the same self-healing pattern build_p2.py already uses. Two harmless copies of the same root cause fixed alongside it: harness-glossary.html and harness-toolkit.html were missing the .src citation-tooltip CSS class. build/README.md gained a paragraph naming the risk.',
        'es': 'Encontrado por verificación directa, no por lectura de NEXT-STEPS.md: build/body_sources_*.html no se había tocado desde la regeneración anterior a las dos rondas de corrección de citas del día, que editaron harness-sources.html directamente sin actualizar la fuente de verdad declarada en build/. Correr build_sources.py tal como estaba habría revertido dieciocho citas corregidas de vuelta a su estado erróneo o no localizado, sin ningún aviso. Corregido extrayendo los tres cuerpos actuales y correctos del harness-sources.html vigente y reescribiéndolos en build/, el mismo patrón autocurativo que ya usa build_p2.py. Dos copias inofensivas de la misma causa raíz corregidas junto con esta: a harness-glossary.html y harness-toolkit.html les faltaba la clase CSS de tooltip de cita .src. build/README.md ganó un párrafo que nombra el riesgo.',
    },
    '6e818fa': {
        'pt': 'Pesquisa adversarial em seis eixos (SI, criptografia, GDPR, AI Act, LGPD, monitoramento, governança) sobre as Partes 3 e 4, um agente de fundo por eixo com busca real, cruzada com um pacote independente das outras IAs do autor — os dois convergiram quase linha a linha. Achado crítico: a Parte 3 dizia que a prorrogação do AI Act europeu "ainda não virou lei"; já tinha virado, Regulamento (UE) 2026/1744, em vigor desde 27 de julho. Outras correções: produtos reais nomeados nos três CVEs, RFC 8693 e SPIFFE/SPIRE citados, a Lei 15.352/2026 real no lugar de "per industry reporting", duas citações mal atribuídas corrigidas. harness-toolkit.html ganha duas seções novas, Secure e Govern, fechando a lacuna de ferramenta concreta que o item 4 pedia.',
        'en': 'Six-axis adversarial research (SI, cryptography, GDPR, AI Act, LGPD, monitoring, governance) across Parts 3 and 4, one background agent per axis with live search, cross-checked against an independently produced package from the author’s other AI tools — the two converged almost line for line. Critical finding: Part 3 said the EU AI Act delay "had not become law"; it already had, Regulation (EU) 2026/1744, in force since 27 July. Other corrections: real products named for the three CVEs, RFC 8693 and SPIFFE/SPIRE cited, Brazil’s real Law 15,352/2026 in place of "per industry reporting", two misattributed quotes fixed. harness-toolkit.html gains two new sections, Secure and Govern, closing the concrete-tool gap item 4 asked for.',
        'es': 'Investigación adversarial en seis ejes (SI, criptografía, GDPR, AI Act, LGPD, monitoreo, gobernanza) sobre las Partes 3 y 4, un agente de fondo por eje con búsqueda real, cruzada con un paquete independiente de las otras IAs del autor — los dos convergieron casi línea por línea. Hallazgo crítico: la Parte 3 decía que la prórroga del AI Act europeo "todavía no se había convertido en ley"; ya lo era, Reglamento (UE) 2026/1744, en vigor desde el 27 de julio. Otras correcciones: productos reales nombrados en los tres CVE, RFC 8693 y SPIFFE/SPIRE citados, la Ley 15.352/2026 real en lugar de "per industry reporting", dos citas mal atribuidas corregidas. harness-toolkit.html gana dos secciones nuevas, Secure y Govern, cerrando la brecha de herramienta concreta que pedía el ítem 4.',
    },
    'eba4458': {
        'pt': 'Lacuna levantada pelo próprio autor ao revisar a rodada de pesquisa anterior: as entradas de Secure respondiam quem é o agente e se sua ação é testemunhada, nenhuma perguntava o que é o dado em si. Pesquisa dedicada achou dois tracks reais: redação de PII (Presidio, que saiu da Microsoft pra uma organização independente em 2026 sem quebra de manutenção) e classificação de dado como fronteira de acesso (Microsoft Purview, com uma limitação real registrada — sua própria matriz de suporte não cobre agentes Claude Enterprise). Duas lacunas genuínas verificadas e não preenchidas: nenhuma ferramenta madura pra minimização real de dado, nenhum framework normativo de privacy-by-design específico pra agente ainda existe.',
        'en': 'A gap raised by the author directly while reviewing the previous research round: Secure’s entries answered who the agent is and whether its actions are witnessed, none asked what the data itself is. Dedicated research found two real tracks: PII redaction (Presidio, which moved from Microsoft to an independent organisation in 2026 with no break in maintenance) and data classification as an access boundary (Microsoft Purview, with a real limitation stated outright, its own support matrix does not cover Claude Enterprise agents). Two genuine gaps checked and left unfilled: no mature tool yet exists for true data minimisation, no standards body has published an agent-specific privacy-by-design framework.',
        'es': 'Una brecha planteada por el propio autor al revisar la ronda de investigación anterior: las entradas de Secure respondían quién es el agente y si su acción queda registrada, ninguna preguntaba qué es el dato en sí. Una investigación dedicada encontró dos vías reales: redacción de PII (Presidio, que pasó de Microsoft a una organización independiente en 2026 sin interrupción de mantenimiento) y clasificación de datos como frontera de acceso (Microsoft Purview, con una limitación real declarada sin rodeos, su propia matriz de soporte no cubre agentes Claude Enterprise). Dos brechas genuinas verificadas y no rellenadas: todavía no existe una herramienta madura para la minimización real de datos, ninguna entidad normativa ha publicado un marco de privacidad desde el diseño específico para agentes.',
    },
    '0bce5f0': {
        'pt': 'Todas as correções e as duas seções novas do dia levadas pro português e pro espanhol, despachadas em duas traduções paralelas cobrindo os quatro pares de arquivo (Parte 3, Parte 4, fontes, guia). Nomeação das seções novas: "Proteger" nas duas línguas, evitando colisão com a seção "seguranca" já existente; "Governar" em português, "Gobernar" em espanhol. Os dois agentes rodaram os próprios builds ao terminar, sem commitar; verificado do zero depois: sequência de seções 1 a 14 idêntica e correta nas três línguas, e duas rodadas de build consecutivas com o mesmo diff stat exato, confirmando idempotência de verdade.',
        'en': 'All of the day’s corrections and the two new sections carried into Portuguese and Spanish, dispatched as two parallel translations covering the four file pairs (Part 3, Part 4, sources, guide). Naming the new sections: "Proteger" in both languages, avoiding a clash with the existing "seguranca" section; "Governar" in Portuguese, "Gobernar" in Spanish. Both agents ran their own builds on finishing, without committing; verified from scratch afterwards: section sequence 1 to 14 identical and correct in all three languages, and two consecutive build passes producing the exact same diff stat, confirming real idempotency.',
        'es': 'Todas las correcciones del día y las dos secciones nuevas llevadas al portugués y al español, despachadas como dos traducciones paralelas que cubren los cuatro pares de archivo (Parte 3, Parte 4, fuentes, guía). Nombrado de las secciones nuevas: "Proteger" en ambos idiomas, evitando choque con la sección "seguranca" ya existente; "Governar" en portugués, "Gobernar" en español. Los dos agentes corrieron sus propios builds al terminar, sin hacer commit; verificado desde cero después: secuencia de secciones 1 a 14 idéntica y correcta en los tres idiomas, y dos rondas de build consecutivas con el mismo diff stat exacto, confirmando idempotencia real.',
    },
    '6b2a015': {
        'pt': 'Duas pendências do item 4 fechadas: quatro fontes do Secure (Presidio, Purview, Model Armor, Bedrock Guardrails) que só existiam como link inline entraram na bibliografia do guia, nas três línguas. A skill research ganhou entrada própria de seis campos em Inspecionar, encaixe natural já que a própria seção existe pra "produzir evidência em vez de opinião". TOOLS.md, nas três línguas, ganhou o primeiro registro real do próprio log de uso, que desde 30 de agosto dizia "nenhum uso registrado ainda" apesar da skill já ter sido usada de verdade várias vezes.',
        'en': 'Two item-4 loose ends closed: four Secure sources (Presidio, Purview, Model Armor, Bedrock Guardrails) that only existed as inline links entered the guide’s bibliography, all three languages. The research skill gained its own six-field entry in Inspect, a natural fit since the section exists precisely to "produce evidence instead of opinion." TOOLS.md, all three languages, gained the first real entry in its own usage log, which had said "no usage logged yet" since 30 August despite the skill already having been used for real several times.',
        'es': 'Dos cabos sueltos del ítem 4 cerrados: cuatro fuentes de Secure (Presidio, Purview, Model Armor, Bedrock Guardrails) que solo existían como enlace en línea entraron a la bibliografía de la guía, en los tres idiomas. La skill research ganó su propia ficha de seis campos en Inspeccionar, un encaje natural ya que la sección existe justamente para "producir evidencia en vez de opinión". TOOLS.md, en los tres idiomas, ganó la primera entrada real de su propio registro de uso, que desde el 30 de agosto decía "aún no hay uso registrado" pese a que la skill ya se había usado de verdad varias veces.',
    },
    'e43f1e5': {
        'pt': 'Registro pontual: NEXT-STEPS.md fecha o item 4 por completo, sem resíduo aberto.',
        'en': 'Point fix: NEXT-STEPS.md closes item 4 in full, with nothing left open.',
        'es': 'Registro puntual: NEXT-STEPS.md cierra el ítem 4 por completo, sin nada abierto.',
    },
    '2d46202': {
        'pt': 'As duas últimas perguntas de verificação da rodada fechadas com fonte primária. Artigo 73: o texto do Regulamento (UE) 2026/1744, aberto direto no EUR-Lex, limita o adiamento às três primeiras seções do Capítulo III, onde vive o artigo 26 — o artigo 73 fica no Capítulo IX, nunca citado nessa cláusula; a "inconsistência" já registrada entre as páginas dos dois artigos não era bug do site. Registro da BlueRock: a URL testada antes só estava com o caminho errado; o registro certo (mcp-trust.com) confirma ao vivo a cifra 12.000+/33% que já constava como "possivelmente superada" — é a mesma medição contínua numa amostra maior, não um número contraditório.',
        'en': 'The round’s last two verification questions closed with a primary source. Article 73: the text of Regulation (EU) 2026/1744, opened directly on EUR-Lex, limits the deferral to Chapter III’s first three sections, where article 26 lives, article 73 sits in Chapter IX, never named in that clause; the "inconsistency" already logged between the two articles’ pages was not a site bug. BlueRock’s registry: the URL tested before simply had the wrong path; the real registry (mcp-trust.com) confirms live the 12,000+/33% figure already logged as "possibly superseded", the same continuous measurement on a larger sample, not a contradicted number.',
        'es': 'Las dos últimas preguntas de verificación de la ronda cerradas con fuente primaria. Artículo 73: el texto del Reglamento (UE) 2026/1744, abierto directamente en EUR-Lex, limita el aplazamiento a las tres primeras secciones del Capítulo III, donde vive el artículo 26; el artículo 73 está en el Capítulo IX, nunca nombrado en esa cláusula; la "inconsistencia" ya registrada entre las páginas de ambos artículos no era un bug del sitio. Registro de BlueRock: la URL probada antes simplemente tenía la ruta equivocada; el registro real (mcp-trust.com) confirma en vivo la cifra 12.000+/33% ya registrada como "posiblemente superada", la misma medición continua sobre una muestra mayor, no un número contradicho.',
    },
    '71e2033': {
        'pt': 'Pedido direto do autor: auditoria exaustiva de link interno e validação ao vivo de toda URL externa dos últimos commits. Checador próprio confirmou 430 referências de citação cruzada nas cinco páginas trilíngues, zero quebrada — uma classe de erro que o broken: [] dos scripts de build nunca vê. Das 39 URLs externas checadas, 37 bateram exatamente; duas não. A mais séria: a alegação de que o Agent Governance Toolkit da Microsoft "automatiza descomissionamento sem aprovação" não se sustentou na leitura direta do código-fonte bruto — o toolkit detecta candidato automaticamente, mas a chamada que muda o estado é separada e explícita, disparada por ninguém sozinho. Corrigido nas três línguas, reformulado como "gancho vazio" em vez de "falha já embarcada", argumento mais forte e honesto que o exagero anterior.',
        'en': 'A direct ask from the author: an exhaustive internal-link audit and live validation of every external URL from the recent commits. A purpose-built checker confirmed 430 cross-file citation references across the five trilingual pages, zero broken, a class of error the build scripts’ own broken: [] check never sees. Of 39 external URLs checked, 37 matched exactly; two did not. The more serious one: the claim that Microsoft’s Agent Governance Toolkit "automates decommissioning with no approval" did not hold up against a direct read of the raw source code, the toolkit detects candidates automatically, but the function that changes state is a separate, explicit call nothing invokes on its own. Corrected in all three languages, reframed as an "empty hook" rather than a "shipped failure", a stronger and more honest argument than the earlier overstatement.',
        'es': 'Un pedido directo del autor: una auditoría exhaustiva de enlaces internos y validación en vivo de cada URL externa de los commits recientes. Un verificador propio confirmó 430 referencias de cita cruzada en las cinco páginas trilingües, cero rotas, una clase de error que el propio broken: [] de los scripts de build nunca detecta. De 39 URLs externas revisadas, 37 coincidieron exactamente; dos no. La más seria: la afirmación de que el Agent Governance Toolkit de Microsoft "automatiza la baja sin aprobación" no se sostuvo al leer directamente el código fuente crudo, el toolkit detecta candidatos automáticamente, pero la función que cambia el estado es una llamada separada y explícita que nada dispara por sí sola. Corregido en los tres idiomas, replanteado como un "gancho vacío" en vez de una "falla ya embarcada", un argumento más fuerte y honesto que la exageración anterior.',
    },
    'd2dba82': {
        'pt': 'Diário de bordo regerado com dez marcos novos: as duas sincronizações de build já registradas antes da sessão, o bug de reversão de citações corrigido em build_sources.py, a pesquisa adversarial de seis eixos que criou as seções Secure e Govern no guia compacto, a camada de proteção de dado, a sincronização de português e espanhol, o fechamento do item 4 com citação própria da skill research, as duas verificações pendentes resolvidas (artigo 73 do AI Act, registro da BlueRock), e a correção da alegação exagerada sobre o Agent Governance Toolkit. Cinquenta marcos completos, 114.396 palavras publicadas, cerca de 1.724,9 milhões de tokens transacionados.',
        'en': 'Project log regenerated with ten new milestones: the two build syncs already logged before this session, the citation-reversion bug fixed in build_sources.py, the six-axis adversarial research that created the compact guide’s Secure and Govern sections, the data-protection layer, the Portuguese and Spanish sync, the item 4 closure with the research skill’s own citation, the two pending verifications resolved (AI Act article 73, the BlueRock registry), and the fix to the overstated Agent Governance Toolkit claim. Fifty milestones complete, 114,396 words published, about 1,724.9 million tokens transacted.',
        'es': 'Diario de bordo regenerado con diez hitos nuevos: las dos sincronizaciones de build ya registradas antes de esta sesión, el bug de reversión de citas corregido en build_sources.py, la investigación adversarial de seis ejes que creó las secciones Secure y Govern en la guía compacta, la capa de protección de datos, la sincronización de portugués y español, el cierre del ítem 4 con cita propia de la skill research, las dos verificaciones pendientes resueltas (artículo 73 del AI Act, registro de BlueRock), y la corrección de la alegación exagerada sobre el Agent Governance Toolkit. Cincuenta hitos completos, 114.396 palabras publicadas, cerca de 1.724,9 millones de tokens transaccionados.',
    },
    '7a801ab': {
        'pt': 'Revisão de português aplicada nos seis artigos e docs internos, a partir de um documento de consolidação enviado pelo autor: sensor vira verificador (127 ocorrências), dono do agente vira proprietário do agente (21 ocorrências, incluindo duas tabelas e um rótulo de SVG que a lista original tinha deixado de fora), trifeta letal vira trinca letal, humano no laço vira human in the loop com verbete novo no glossário, submissão vira alegação. Antes de aplicar qualquer troca, quatro agentes em paralelo auditaram o documento contra os arquivos reais e acharam lacunas genuínas: o pipeline de build exigia editar o espelho em build/, não só o HTML publicado, e a construção "não é X, é Y" foi recalibrada de "pelo menos sete" pra cerca de trinta e três ocorrências reais, com boa parte reescrita variando a forma a cada vez.',
        'en': 'Portuguese-language revision applied across the six articles and internal docs, from a consolidation document the author sent over: sensor becomes verificador (127 occurrences), dono do agente becomes proprietário do agente (21 occurrences, including two tables and an SVG label the original list had missed), trifeta letal becomes trinca letal, humano no laço becomes human in the loop with a new glossary entry, submissão becomes alegação. Before applying any of it, four parallel agents audited the document against the real files and found genuine gaps: the build pipeline required editing the build/ mirror, not just the published HTML, and the "não é X, é Y" construction was recalibrated from "at least seven" to about thirty-three real occurrences, a good share of them rewritten with varied phrasing each time.',
        'es': 'Revisión de portugués aplicada en los seis artículos y documentos internos, a partir de un documento de consolidación que envió el autor: sensor pasa a verificador (127 apariciones), dono do agente pasa a proprietário do agente (21 apariciones, incluyendo dos tablas y una etiqueta SVG que la lista original había dejado fuera), trifeta letal pasa a trinca letal, humano no laço pasa a human in the loop con verbete nuevo en el glosario, submissão pasa a alegação. Antes de aplicar cualquier cambio, cuatro agentes en paralelo auditaron el documento contra los archivos reales y encontraron brechas genuinas: el pipeline de build exigía editar el espejo en build/, no solo el HTML publicado, y la construcción "no es X, es Y" se recalibró de "al menos siete" a unas treinta y tres apariciones reales, buena parte reescritas variando la forma cada vez.',
    },
    'cc88efb': {
        'pt': 'A pedido do autor, segunda passada semântica sobre a mesma revisão: maquinaria vira engrenagem (3 ocorrências), mais concreta e alinhada ao fio de manufatura que já corre pela série inteira (poka-yoke, Toyota, Deming). E o refrão "quais ainda se pagam" da parte 4 vira "quais ainda valem o que custam" (9 ocorrências), corrigindo uma inconsistência interna, já que uma passagem do próprio texto usava a segunda frase, e removendo a ambiguidade reflexiva que o espanhol já resolvia com "a sí mismos" e o português não tinha.',
        'en': 'At the author’s request, a second semantic pass over the same revision: maquinaria becomes engrenagem (gearing, 3 occurrences), more concrete and in line with the manufacturing thread already running through the whole series (poka-yoke, Toyota, Deming). And part 4’s "quais ainda se pagam" refrain becomes "quais ainda valem o que custam" (9 occurrences), fixing an internal inconsistency, since one passage of the text already used the second phrasing, and removing the reflexive ambiguity Spanish already resolved with "a sí mismos" and Portuguese lacked.',
        'es': 'A pedido del autor, segunda pasada semántica sobre la misma revisión: maquinaria pasa a engrenagem (engranaje, 3 apariciones), más concreta y alineada con el hilo de manufactura que ya recorre toda la serie (poka-yoke, Toyota, Deming). Y el estribillo "quais ainda se pagam" de la parte 4 pasa a "quais ainda valem o que custam" (9 apariciones), corrigiendo una inconsistencia interna, ya que un pasaje del propio texto ya usaba la segunda frase, y quitando la ambigüedad reflexiva que el español ya resolvía con "a sí mismos" y el portugués no tenía.',
    },
}

MONTHS = {
    'pt': ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez'],
    'en': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'es': ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic'],
}


def fmt_time(iso, lang):
    # 2026-08-30T12:36:00-03:00 -> "30 ago, 12:36" (pt) etc.
    m = re.match(r'(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2})', iso)
    y, mo, d, h, mi = m.groups()
    return '%d %s, %s:%s' % (int(d), MONTHS[lang][int(mo) - 1], h, mi)


def fmt_int(n, lang):
    s = '{:,}'.format(int(n))
    if lang in ('pt', 'es'):
        s = s.replace(',', '.')
    return s


def fmt_millions(n, lang):
    v = n / 1_000_000
    s = ('%.1f' % v)
    if lang in ('pt', 'es'):
        s = s.replace('.', ',')
    return s


# ---------- SVG: grafico de crescimento, mesmo eixo X, sem eixo Y duplo ----------
def svg_growth_chart(marker_prefix, values, x_labels, y_fmt, caption, subcaption, viewbox_h=260):
    W, H = 700, viewbox_h
    left, right, top, bottom = 78, 652, 34, H - 66
    n = len(values)
    max_v = max(values) * 1.12 if max(values) > 0 else 1
    xs = [left + i * (right - left) / (n - 1) for i in range(n)]
    ys = [bottom - (v / max_v) * (bottom - top) for v in values]
    pts = ' '.join('%.1f,%.1f' % (x, y) for x, y in zip(xs, ys))

    parts = []
    parts.append('<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (W, H, caption))
    # eixo
    parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9c7bf" stroke-width=".7"/>' % (left, bottom, right, bottom))
    # linha de nivel maximo, de referencia
    parts.append('<line x1="%d" y1="%d" x2="%d" y2="%d" stroke="#c9c7bf" stroke-width=".5" stroke-dasharray="2,3"/>' % (left, top, right, top))
    parts.append('<text class="svg-sub" x="%d" y="%d" text-anchor="end">%s</text>' % (left - 6, top + 4, y_fmt(max_v)))
    parts.append('<text class="svg-sub" x="%d" y="%d" text-anchor="end">0</text>' % (left - 6, bottom + 4))
    # polilinha
    parts.append('<polyline points="%s" fill="none" stroke="#1b1b19" stroke-width="1"/>' % pts)
    # Value labels collide once there are enough milestones that neighbouring
    # points sit closer together than the label text is wide (seen for real at
    # 22 milestones: numbers overlapped into an unreadable smear). Space labels
    # out instead of dropping one on every point, always keeping the first and
    # last so the story's start and current state are never the ones omitted.
    max_labels = max(2, int((right - left) / 70))
    step = max(1, round((n - 1) / (max_labels - 1))) if n > 1 else 1
    labelled = set(range(0, n, step))
    labelled.add(0)
    # the forced last point can land right beside a regular-step point picked
    # up by range() above (seen for real: two labels touching at the tail,
    # "68,176 68,176"); drop anything crowding it before adding it back
    labelled = {i for i in labelled if i == n - 1 or (n - 1 - i) >= max(2, step // 2)}
    labelled.add(n - 1)
    # x-axis tick labels (M1, M2...) are short and safe at a tighter spacing,
    # but still thin them past the point where even "M99" would collide.
    x_max_labels = max(2, int((right - left) / 26))
    x_step = max(1, round((n - 1) / (x_max_labels - 1))) if n > 1 else 1
    x_labelled = set(range(0, n, x_step))
    x_labelled.add(0)
    x_labelled.add(n - 1)
    for i, (x, y, v) in enumerate(zip(xs, ys, values)):
        parts.append('<circle cx="%.1f" cy="%.1f" r="3" fill="#1b1b19"/>' % (x, y))
        if i in labelled:
            label_y = y - 10 if y > top + 16 else y + 16
            parts.append('<text class="svg-sub" x="%.1f" y="%.1f" text-anchor="middle">%s</text>' % (x, label_y, y_fmt(v)))
        if i in x_labelled:
            parts.append('<text class="svg-sub" x="%.1f" y="%d" text-anchor="middle">%s</text>' % (x, H - 40, x_labels[i]))
    parts.append('<text class="svg-cap" x="%d" y="%d">%s</text>' % (left, H - 16, subcaption))
    parts.append('</svg>')
    return '\n'.join(parts)


def build_body(lang):
    T = TXT[lang]
    n = len(MS)
    x_labels = ['M%d' % (i + 1) for i in range(n)] + [T['now_short']]
    words_series = [m['words_published'] for m in MS] + [MS[-1]['words_published']]
    tok_series = [sum(m['tokens_cumulative'].values()) for m in MS]
    tok_series = tok_series + [tok_series[-1] + sum(REMAINING.values())]

    words_chart = svg_growth_chart(
        'w', words_series, x_labels,
        lambda v: fmt_int(v, lang),
        T['chart_words_alt'], T['chart_words_cap'])
    tok_chart = svg_growth_chart(
        't', tok_series, x_labels,
        lambda v: fmt_millions(v, lang) + T['million_suffix'],
        T['chart_tokens_alt'], T['chart_tokens_cap'])

    total_tokens_now = sum(MS[-1]['tokens_cumulative'].values()) + sum(REMAINING.values())
    total_words_now = MS[-1]['words_published']
    total_code_now = MS[-1]['code_lines']
    total_gov_now = MS[-1]['governance_lings'] if False else MS[-1]['governance_lines']

    kpi_rows = [
        (fmt_millions(total_tokens_now, lang) + T['million_suffix'], T['kpi_tokens']),
        (fmt_int(total_words_now, lang), T['kpi_words']),
        (fmt_int(total_code_now + total_gov_now, lang), T['kpi_lines']),
        (str(n), T['kpi_commits']),
    ]
    kpi_html = '\n'.join(
        '<div class="kpi"><span class="kpi-n">%s</span><span class="kpi-l">%s</span></div>' % (v, l)
        for v, l in kpi_rows)

    timeline_rows = []
    for i, m in enumerate(MS):
        desc = COMMIT_TXT[m['hash']][lang]
        bt = sum(m['tokens_bucket'].values())
        out_t = m['tokens_bucket']['output']
        timeline_rows.append(
            '<tr><td>M%d<br><span class="mono">%s</span></td>'
            '<td>%s<br><span class="mono">%s</span></td>'
            '<td>%s</td>'
            '<td>%s</td></tr>' % (
                i + 1, m['hash'],
                desc, fmt_time(m['timestamp'], lang),
                fmt_int(m['words_published'], lang),
                T['tokens_bucket_cell'] % (fmt_millions(bt, lang), fmt_int(out_t, lang))
            ))
    timeline_html = '\n'.join(timeline_rows)

    body = TEMPLATE[lang].format(
        kpi_html=kpi_html,
        words_chart=words_chart,
        tok_chart=tok_chart,
        timeline_html=timeline_html,
        remaining_millions=fmt_millions(sum(REMAINING.values()), lang),
    )
    return body


TXT = {
    'pt': {
        'now_short': 'agora',
        'million_suffix': ' mi',
        'chart_words_alt': 'Palavras publicadas por marco',
        'chart_words_cap': 'PALAVRAS PUBLICADAS, ACUMULADO POR MARCO',
        'chart_tokens_alt': 'Tokens consumidos por marco',
        'chart_tokens_cap': 'TOKENS CONSUMIDOS, ACUMULADO POR MARCO, MESMO EIXO X ACIMA',
        'kpi_tokens': 'tokens transacionados até agora',
        'kpi_words': 'palavras publicadas (PT+EN+ES)',
        'kpi_lines': 'linhas de script e documento de governança',
        'kpi_commits': 'marcos (commits) registrados',
        'tokens_bucket_cell': '%s mi<br><span class="mono">saída: %s</span>',
    },
    'en': {
        'now_short': 'now',
        'million_suffix': 'm',
        'chart_words_alt': 'Words published per milestone',
        'chart_words_cap': 'WORDS PUBLISHED, CUMULATIVE BY MILESTONE',
        'chart_tokens_alt': 'Tokens consumed per milestone',
        'chart_tokens_cap': 'TOKENS CONSUMED, CUMULATIVE BY MILESTONE, SAME X AXIS AS ABOVE',
        'kpi_tokens': 'tokens transacted so far',
        'kpi_words': 'words published (PT+EN+ES)',
        'kpi_lines': 'lines of script and governance document',
        'kpi_commits': 'milestones (commits) recorded',
        'tokens_bucket_cell': '%sm<br><span class="mono">output: %s</span>',
    },
    'es': {
        'now_short': 'ahora',
        'million_suffix': ' mi',
        'chart_words_alt': 'Palabras publicadas por hito',
        'chart_words_cap': 'PALABRAS PUBLICADAS, ACUMULADO POR HITO',
        'chart_tokens_alt': 'Tokens consumidos por hito',
        'chart_tokens_cap': 'TOKENS CONSUMIDOS, ACUMULADO POR HITO, MISMO EJE X DE ARRIBA',
        'kpi_tokens': 'tokens transaccionados hasta ahora',
        'kpi_words': 'palabras publicadas (PT+EN+ES)',
        'kpi_lines': 'líneas de script y documento de gobernanza',
        'kpi_commits': 'hitos (commits) registrados',
        'tokens_bucket_cell': '%s mi<br><span class="mono">salida: %s</span>',
    },
}

TEMPLATE = {}

TEMPLATE['pt'] = """<p class="eyebrow">Harness · Diário de bordo · Ao vivo</p>

<h1>Diário de bordo do projeto</h1>

<p class="deck">Este projeto argumenta que um harness deve produzir evidência sobre o próprio trabalho, não opinião. Esta página aplica esse argumento a si mesma: quanto texto foi publicado, quanto custou em tokens, marco a marco, com os números extraídos direto do histórico do git e do registro real de uso desta sessão.</p>

<p class="byline">Fernando Teco Sodré · Gerado automaticamente, ver metodologia abaixo · Companheiro das partes 1 a 4 e do guia compacto</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Os marcos abaixo são o histórico completo do repositório desde o primeiro commit, não uma amostra, já reunindo várias sessões de trabalho. Cada sessão nova que fizer commit vira um marco novo nesta mesma página.</p></div>

<nav class="toc">
  <p>Neste documento</p>
  <ol>
    <li><a href="#numeros">Números até agora</a></li>
    <li><a href="#evolucao">Evolução</a></li>
    <li><a href="#linha-do-tempo">Linha do tempo</a></li>
    <li><a href="#metodologia">Metodologia</a></li>
    <li><a href="#fontes">Fontes</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Números até agora</h2>

<p>Quatro números resumem o projeto neste instante. Todos recalculados a cada execução do gerador, nenhum digitado à mão.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>Dos tokens acima, cerca de {remaining_millions} mi ainda não fecharam marco: são desta sessão em andamento, ainda não commitados no momento em que este diário foi gerado.</p>

<h2 id="evolucao">2. Evolução</h2>

<p>Dois gráficos, não um só com dois eixos. É a mesma regra que a parte 2 deste projeto aplica a qualquer harness: não misture duas escalas arbitrárias na mesma régua. Os dois compartilham o eixo X, a ordem dos marcos, para que dê para comparar quando um acelerou em relação ao outro.</p>

<figure>
{words_chart}
<figcaption>Palavras publicadas nas sete peças da série (partes 1 a 4, guia compacto, glossário e fontes, somados). Cresce em degrau porque a maior parte do texto nasce dentro de um marco só, não gradualmente entre marcos.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transacionados, acumulado. Inclui leitura de cache, que cresce com o tamanho da sessão por natureza, não só com o trabalho novo. Ver a ressalva na metodologia.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Linha do tempo</h2>

<p>Um marco por commit. A coluna de tokens traz dois números: o total do intervalo, incluindo cache, e a saída pura, que é o sinal mais limpo para comparar esforço real entre marcos.</p>

<table class="wrap">
<thead><tr><th>Marco</th><th>O que aconteceu</th><th>Palavras publicadas</th><th>Tokens do intervalo</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Metodologia</h2>

<p>Fixa, documentada aqui, para repetir igual em toda atualização futura. Ver <code>build/generate_logbook_metrics.py</code> e <code>build/build_logbook.py</code> no repositório.</p>

<p><strong>Palavras.</strong> Contadas a partir do HTML publicado de cada commit (<code>git show &lt;hash&gt;:arquivo</code>), removendo marcação, bloco de código e SVG. Soma as partes 1 a 4, o guia compacto, o glossário e as fontes, nos idiomas que existiam naquele commit.</p>

<p><strong>Linhas.</strong> Contagem de linhas dos scripts de montagem em <code>build/</code> e dos documentos de governança (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, inventário de fontes), por commit.</p>

<p><strong>Tokens.</strong> Soma real do campo <code>usage</code> de cada mensagem do assistente no transcript <code>.jsonl</code> desta sessão, em <code>~/.claude/projects/&lt;projeto&gt;/</code>. Cada evento é atribuído ao commit imediatamente seguinte, por ordem cronológica, mesma técnica usada em outro projeto do autor para o mesmo fim.</p>

<div class="rule-box"><span class="lbl">Viés conhecido</span><p>Leitura de cache cresce com o tamanho acumulado da sessão, não com o esforço do marco específico. Para comparar esforço real entre marcos, use a saída (output), não o total bruto. O total bruto aparece porque é o que a fatura cobra, a saída aparece porque é o que ensina.</p></div>

<p>Uma sessão contínua cobre o projeto inteiro até aqui, então não há reconstrução retroativa a fazer, ao contrário de projetos mais antigos com dezenas de sessões. Cada marco futuro soma a esta mesma série.</p>

<h2 id="fontes">5. Fontes</h2>

<ol class="sources">
<li>Histórico completo de commits deste repositório. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas e usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script gerador dos números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Diário de bordo · Série Harness · Gerado automaticamente a partir do git e do registro de uso real da sessão, nunca editado à mão. Ver metodologia acima antes de citar qualquer número.</p>
</div>"""

TEMPLATE['en'] = """<p class="eyebrow">Harness · Project log · Live</p>

<h1>Project log</h1>

<p class="deck">This project argues that a harness should produce evidence about its own work, not opinion. This page applies that argument to itself: how much text got published, what it cost in tokens, milestone by milestone, with the numbers pulled straight from git history and this session's real usage record.</p>

<p class="byline">Fernando Teco Sodré · Generated automatically, see methodology below · Companion to parts 1 to 4 and the compact guide</p>

<div class="rule-box"><span class="lbl">Status</span><p>The milestones below are the repository's entire history since the first commit, not a sample, already spanning several working sessions. Every new session that commits becomes a new milestone on this same page.</p></div>

<nav class="toc">
  <p>In this document</p>
  <ol>
    <li><a href="#numeros">Numbers so far</a></li>
    <li><a href="#evolucao">Growth</a></li>
    <li><a href="#linha-do-tempo">Timeline</a></li>
    <li><a href="#metodologia">Methodology</a></li>
    <li><a href="#fontes">Sources</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Numbers so far</h2>

<p>Four numbers summarise the project at this instant. All recalculated on every run of the generator, none typed by hand.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>Of the tokens above, about {remaining_millions}m have not closed a milestone yet: they belong to this ongoing session, not committed yet at the moment this log was generated.</p>

<h2 id="evolucao">2. Growth</h2>

<p>Two charts, not one with two axes. It is the same rule this project's part 2 applies to any harness: do not mix two arbitrary scales on the same ruler. Both share the X axis, the order of milestones, so you can compare when one sped up relative to the other.</p>

<figure>
{words_chart}
<figcaption>Words published across the series' seven pieces (parts 1 to 4, the compact guide, the glossary and the sources, summed). It grows in steps because most of the text is born within a single milestone, not gradually between milestones.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transacted, cumulative. Includes cache reads, which grow with session size by nature, not only with new work. See the caveat in the methodology.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Timeline</h2>

<p>One milestone per commit. The tokens column carries two numbers: the interval's total, including cache, and pure output, the cleanest signal for comparing real effort between milestones.</p>

<table class="wrap">
<thead><tr><th>Milestone</th><th>What happened</th><th>Words published</th><th>Interval tokens</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Methodology</h2>

<p>Fixed, documented here, to repeat identically on every future update. See <code>build/generate_logbook_metrics.py</code> and <code>build/build_logbook.py</code> in the repository.</p>

<p><strong>Words.</strong> Counted from the published HTML of each commit (<code>git show &lt;hash&gt;:file</code>), stripping markup, code blocks and SVG. Sums parts 1 to 4, the compact guide, the glossary and the sources, in whichever languages existed at that commit.</p>

<p><strong>Lines.</strong> Line count of the build scripts under <code>build/</code> and the governance documents (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, source inventory), per commit.</p>

<p><strong>Tokens.</strong> Real sum of the <code>usage</code> field on every assistant message in this session's <code>.jsonl</code> transcript, under <code>~/.claude/projects/&lt;project&gt;/</code>. Each event is assigned to the immediately following commit, in chronological order, the same technique used on another of the author's projects for the same purpose.</p>

<div class="rule-box"><span class="lbl">Known bias</span><p>Cache reads grow with the session's accumulated size, not with the specific milestone's effort. To compare real effort between milestones, use output, not the raw total. The raw total shows up because it is what the invoice charges, output shows up because it is what teaches.</p></div>

<p>One continuous session covers the entire project so far, so there is no retroactive reconstruction to do, unlike older projects with dozens of sessions. Every future milestone adds to this same series.</p>

<h2 id="fontes">5. Sources</h2>

<ol class="sources">
<li>Full commit history of this repository. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Record of installed and used skills. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script that generates the numbers. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Project log · Harness series · Generated automatically from git and the session's real usage record, never edited by hand. See the methodology above before citing any number.</p>
</div>"""

TEMPLATE['es'] = """<p class="eyebrow">Harness · Diario de bordo · En vivo</p>

<h1>Diario de bordo del proyecto</h1>

<p class="deck">Este proyecto sostiene que un harness debe producir evidencia sobre su propio trabajo, no opinión. Esta página aplica ese argumento a sí misma: cuánto texto se publicó, cuánto costó en tokens, hito a hito, con los números extraídos directo del historial de git y del registro real de uso de esta sesión.</p>

<p class="byline">Fernando Teco Sodré · Generado automáticamente, ver metodología abajo · Compañero de las partes 1 a 4 y de la guía compacta</p>

<div class="rule-box"><span class="lbl">Estado</span><p>Los hitos de abajo son el historial completo del repositorio desde el primer commit, no una muestra, ya reuniendo varias sesiones de trabajo. Cada sesión nueva que haga commit se vuelve un hito nuevo en esta misma página.</p></div>

<nav class="toc">
  <p>En este documento</p>
  <ol>
    <li><a href="#numeros">Números hasta ahora</a></li>
    <li><a href="#evolucao">Evolución</a></li>
    <li><a href="#linha-do-tempo">Línea de tiempo</a></li>
    <li><a href="#metodologia">Metodología</a></li>
    <li><a href="#fontes">Fuentes</a></li>
  </ol>
</nav>

<h2 id="numeros">1. Números hasta ahora</h2>

<p>Cuatro números resumen el proyecto en este instante. Todos recalculados en cada ejecución del generador, ninguno escrito a mano.</p>

<div class="kpi-grid">
{kpi_html}
</div>

<p>De los tokens de arriba, unos {remaining_millions} mi todavía no cerraron hito: son de esta sesión en curso, aún no confirmados en el momento en que se generó este diario.</p>

<h2 id="evolucao">2. Evolución</h2>

<p>Dos gráficos, no uno solo con dos ejes. Es la misma regla que la parte 2 de este proyecto aplica a cualquier harness: no mezcles dos escalas arbitrarias en la misma regla. Los dos comparten el eje X, el orden de los hitos, para poder comparar cuándo uno aceleró respecto al otro.</p>

<figure>
{words_chart}
<figcaption>Palabras publicadas en las siete piezas de la serie (partes 1 a 4, guía compacta, glosario y fuentes, sumadas). Crece en escalón porque la mayor parte del texto nace dentro de un solo hito, no gradualmente entre hitos.</figcaption>
</figure>

<figure>
{tok_chart}
<figcaption>Tokens transaccionados, acumulado. Incluye lectura de caché, que crece con el tamaño de la sesión por naturaleza, no solo con el trabajo nuevo. Ver la salvedad en la metodología.</figcaption>
</figure>

<h2 id="linha-do-tempo">3. Línea de tiempo</h2>

<p>Un hito por commit. La columna de tokens trae dos números: el total del intervalo, incluyendo caché, y la salida pura, la señal más limpia para comparar el esfuerzo real entre hitos.</p>

<table class="wrap">
<thead><tr><th>Hito</th><th>Qué pasó</th><th>Palabras publicadas</th><th>Tokens del intervalo</th></tr></thead>
<tbody>
{timeline_html}
</tbody>
</table>

<h2 id="metodologia">4. Metodología</h2>

<p>Fija, documentada aquí, para repetir igual en cada actualización futura. Ver <code>build/generate_logbook_metrics.py</code> y <code>build/build_logbook.py</code> en el repositorio.</p>

<p><strong>Palabras.</strong> Contadas a partir del HTML publicado de cada commit (<code>git show &lt;hash&gt;:archivo</code>), quitando marcado, bloque de código y SVG. Suma las partes 1 a 4, la guía compacta, el glosario y las fuentes, en los idiomas que existían en ese commit.</p>

<p><strong>Líneas.</strong> Conteo de líneas de los scripts de montaje en <code>build/</code> y de los documentos de gobernanza (README, STANDARDS, STATUS, NEXT-STEPS, TOOLS, inventario de fuentes), por commit.</p>

<p><strong>Tokens.</strong> Suma real del campo <code>usage</code> de cada mensaje del asistente en el transcript <code>.jsonl</code> de esta sesión, en <code>~/.claude/projects/&lt;proyecto&gt;/</code>. Cada evento se asigna al commit inmediatamente siguiente, en orden cronológico, la misma técnica usada en otro proyecto del autor con el mismo fin.</p>

<div class="rule-box"><span class="lbl">Sesgo conocido</span><p>La lectura de caché crece con el tamaño acumulado de la sesión, no con el esfuerzo del hito específico. Para comparar el esfuerzo real entre hitos, usa la salida (output), no el total bruto. El total bruto aparece porque es lo que cobra la factura, la salida aparece porque es lo que enseña.</p></div>

<p>Una sesión continua cubre el proyecto entero hasta aquí, así que no hay reconstrucción retroactiva que hacer, a diferencia de proyectos más antiguos con decenas de sesiones. Cada hito futuro se suma a esta misma serie.</p>

<h2 id="fontes">5. Fuentes</h2>

<ol class="sources">
<li>Historial completo de commits de este repositorio. <a href="https://github.com/tecosodreaboutdigital/harness-medir/commits/main">github.com/tecosodreaboutdigital/harness-medir</a></li>
<li>Registro de skills instaladas y usadas. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/TOOLS.md">TOOLS.md</a></li>
<li>Script que genera los números. <a href="https://github.com/tecosodreaboutdigital/harness-medir/blob/main/build/generate_logbook_metrics.py">build/generate_logbook_metrics.py</a></li>
</ol>

<div class="foot">
<p>Diario de bordo · Serie Harness · Generado automáticamente a partir de git y del registro de uso real de la sesión, nunca editado a mano. Ver la metodología arriba antes de citar cualquier número.</p>
</div>"""


def scope(body, pref):
    body = re.sub(r'(\sid=")([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    body = re.sub(r'(href="#)([a-z0-9\-]+)(")', lambda m: m.group(1) + pref + '-' + m.group(2) + m.group(3), body)
    return body


def main():
    p2 = open(os.path.join(ROOT, 'harness-p2.html'), encoding='utf-8').read()
    shell = p2[:p2.index('<div class="topbar">')]
    shell = shell.replace(
        '<title>Guides and sensors: how an agent learns to correct itself | Part 2</title>',
        '<title>Project log | Harness</title>')

    extra_css = """
.kpi-grid{display:flex;flex-wrap:wrap;gap:0;margin:20px 0 30px;border-top:.5pt solid var(--ink);border-bottom:.5pt solid var(--ink)}
.kpi{flex:1 1 22%;padding:16px 14px;border-right:.5pt solid var(--rule);display:flex;flex-direction:column;gap:4px}
.kpi:last-child{border-right:0}
.kpi-n{font-size:22px;font-weight:600;letter-spacing:-.01em}
.kpi-l{font-size:10.5px;color:var(--ink-faint);line-height:1.3}
.mono{font-family:"Consolas","Menlo",monospace;font-size:10.5px;color:var(--ink-faint)}
@media (max-width:640px){.kpi{flex:1 1 48%}}
"""
    shell = shell.replace('.eyebrow{', extra_css + '.eyebrow{')
    # .topbar .icon-link ja vem no shell extraido de harness-p2.html,
    # nao precisa de injecao propria aqui (um replace incondicional
    # duplicaria a regra, o mesmo bug corrigido acima para LANG_HINT_CSS).

    # docs/logbook.html vive uma pasta abaixo da raiz, entao os links
    # para as outras seis pecas levam o prefixo ../. O icone do proprio
    # diario aparece como item corrente (cur), sem link, como nas
    # outras paginas quando o item e a propria pagina.
    SERIES_ORDER = ['p1', 'p2', 'p3', 'p4', 'guide', 'glossary', 'sources']
    FILES = {'p1': '../harness-p1.html', 'p2': '../harness-p2.html', 'p3': '../harness-p3.html',
             'p4': '../harness-p4.html', 'guide': '../harness-toolkit.html',
             'glossary': '../harness-glossary.html', 'sources': '../harness-sources.html'}
    LABELS_EN = {'p1': 'Part 1', 'p2': 'Part 2', 'p3': 'Part 3', 'p4': 'Part 4',
                 'guide': 'Compact guide', 'glossary': 'Glossary', 'sources': 'Sources'}
    topbar_pieces = []
    for i, key in enumerate(SERIES_ORDER):
        if i > 0:
            topbar_pieces.append('<span class="sep pipe">|</span>' if key == 'guide' else '<span class="sep">·</span>')
        topbar_pieces.append('<a href="%s#en-" data-key="%s">%s</a>' % (FILES[key], key, LABELS_EN[key]))
    topbar_pieces.append('<span class="sep pipe">|</span>')
    topbar_pieces.append('<span class="cur icon-link" data-key="logbook" data-icon="1" title="Project log" '
                          'aria-label="Project log"><svg viewBox="0 0 16 16" width="14" height="14" '
                          'aria-hidden="true" focusable="false"><polyline points="1,13 5,13 5,9 9,9 9,4 15,4" '
                          'fill="none" stroke="currentColor" stroke-width="1.3"/></svg></span>')
    topbar = ('<div class="topbar">\n<nav class="serie">\n' + '\n'.join(topbar_pieces) + '\n</nav>\n'
              '<span class="brace">{</span>\n')

    bar = topbar + """<div class="langbar">
<button type="button" data-lang="pt">PT</button>
<button type="button" class="on" data-lang="en">EN</button>
<button type="button" data-lang="es">ES</button>
</div>
<span class="brace">}</span>
</div>"""

    js = """<script>
(function(){
  var bar=document.querySelector('.langbar');
  var mains={pt:document.getElementById('doc-pt'),en:document.getElementById('doc-en'),es:document.getElementById('doc-es')};
  var SERIES={p1:{file:'../harness-p1.html',label:{en:'Part 1',pt:'Parte 1',es:'Parte 1'}},p2:{file:'../harness-p2.html',label:{en:'Part 2',pt:'Parte 2',es:'Parte 2'}},p3:{file:'../harness-p3.html',label:{en:'Part 3',pt:'Parte 3',es:'Parte 3'}},p4:{file:'../harness-p4.html',label:{en:'Part 4',pt:'Parte 4',es:'Parte 4'}},guide:{file:'../harness-toolkit.html',label:{en:'Compact guide',pt:'Guia compacto',es:'Gu\\u00eda compacta'}},glossary:{file:'../harness-glossary.html',label:{en:'Glossary',pt:'Gloss\\u00e1rio',es:'Glosario'}},sources:{file:'../harness-sources.html',label:{en:'Sources',pt:'Fontes',es:'Fuentes'}},logbook:{file:'',label:{en:'Project log',pt:'Di\\u00e1rio de bordo',es:'Diario de bordo'}}};
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

    PT = scope(build_body('pt'), 'pt')
    EN = scope(build_body('en'), 'en')
    ES = scope(build_body('es'), 'es')

    doc = (shell + bar + '\n'
           + '<main class="page" id="doc-pt" hidden>\n' + PT + '\n</main>\n'
           + '<main class="page" id="doc-en">\n' + EN + '\n</main>\n'
           + '<main class="page" id="doc-es" hidden>\n' + ES + '\n</main>\n'
           + js)

    out_dir = os.path.join(ROOT, 'docs')
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'logbook.html')
    with open(out_path, 'w', encoding='utf-8') as fh:
        fh.write(doc)

    ids = set(re.findall(r'\sid="([a-z0-9\-]+)"', doc))
    hr = set(re.findall(r'href="#([a-z0-9\-]+)"', doc))
    print('broken:', sorted(hr - ids))
    print('escrito em:', out_path)


if __name__ == '__main__':
    main()
