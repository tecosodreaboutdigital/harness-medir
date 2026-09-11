*Lee en [English](TOOLS.md) · [Português](TOOLS.pt.md).*

# Herramientas y skills usadas en este proyecto

Registro de lo que este proyecto realmente instaló y usa, no solo de lo que cita. Un proyecto sobre ingeniería de harness que no instrumentara su propia creación sería solo un argumento bonito. Este documento es la instrumentación.

Actualizado el 10 de septiembre de 2026. Crece con cada skill nueva que entra en uso, nunca se reescribe por completo.

---

## Colecciones de terceros instaladas

Diez colecciones, treinta y siete skills, todas con licencia MIT o Apache 2.0. Instaladas localmente en `.claude/skills/`, fuera del control de versiones (ver `.gitignore`): funcionan en este entorno, pero el código de terceros no entra en el historial público de este repositorio. Las primeras seis se citan como entrada en la [guía compacta](harness-toolkit.html); las cuatro más recientes todavía no, ver la nota al final de esta sección. Suma `intake-briefing`, la skill propia del proyecto tratada en la sección siguiente, y el entorno tiene 38 skills activas en total.

| Colección | Origen | Skills instaladas | Por qué entró |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, la colección entera | Es el patrón de regla innegociable más señales de alerta que `STANDARDS.md` ya adopta como estándar de escritura de skills de este proyecto |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, selección curada | Skills de escritura, clarificación y traspaso de sesión. El conjunto de ingeniería de software de la colección (TDD, arquitectura de código, conflictos de merge, TypeScript) quedó fuera por no aplicarse a un proyecto de contenido, ver la lista completa abajo |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, la colección entera | El modelo C4 y los registros de decisión de arquitectura, relevantes para la ronda de investigación de la parte 3 |
| Guía inspirada en Karpathy | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | Guía de comportamiento contra errores comunes de LLM. No es realmente de Karpathy, ver la salvedad completa en `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | Fuente real de la matriz de cinco reglas de limpieza citada en la sección Reforzar de la parte 2 |
| impeccable | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1 | Referencia de QA de diseño para las propias páginas HTML del proyecto: 61 reglas determinísticas de detector para tics comunes de frontend generado por IA, Apache-2.0, 30 colaboradores. Instalada solo como documentación, ver la salvedad abajo |
| humanizer | [github.com/blader/humanizer](https://github.com/blader/humanizer) | 1, la colección entera | Quita los tics de prosa que suenan a IA de un borrador en inglés antes de que se ramifique hacia el portugués y el español. Ninguna de las otras nueve colecciones de esta página llega a ese nivel de detalle, forma de frase y párrafo, no vocabulario. Sumada el 10 de septiembre de 2026 a partir de una lista de skills candidatas enviada por un lector |
| Agent Skills for Context Engineering | [github.com/muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 3, de 17 | Un lector señaló la arquitectura de harness de agente como una brecha real de esta página. `harness-engineering`, `multi-agent-patterns` y `tool-design` la cierran directamente; las otras 14 skills (optimización de contexto, sistemas de memoria, evaluación y más) resuelven problemas adyacentes que este proyecto no tiene, ver la lista completa abajo |
| ai-act-skill | [github.com/morellid/ai-act-skill](https://github.com/morellid/ai-act-skill) | 1, la colección entera | Checklist versionado, tarea por tarea, para las obligaciones del AI Act europeo, ya actualizado con el Digital Omnibus (Reglamento (UE) 2026/1744). Las partes 3 y 4 ya citan los artículos 12, 14 y 26 en prosa; esta es la primera herramienta del propio kit de este proyecto que convierte esa cita en una verificación ejecutable |
| threat-modeling | [github.com/rjmurillo/ai-agents](https://github.com/rjmurillo/ai-agents) | 1, de una colección personal más grande | Modelado de amenazas basado en STRIDE, con alcance en arquitectura de agente y revisión de seguridad, no revisión puntual de diff. Instalación parcial: solo entró la carpeta de esta skill, no el resto del repositorio |

---

## Las treinta y siete skills, por colección

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (la carpeta de origen llama a esta skill `c4designer`, pero el propio encabezado interno de `SKILL.md` declara el nombre `c4-model`; renombramos la carpeta local para que coincida con el nombre declarado).

**Guía inspirada en Karpathy:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

**impeccable:** impeccable. **Instalación parcial, dicho con honestidad:** copiamos `SKILL.md` y cada archivo bajo `reference/`, nada bajo `scripts/`. El propio encabezado de la skill original lista `Bash(npx impeccable *)` y `Bash(node .../scripts/*)` como herramientas permitidas, ligadas a 61 reglas determinísticas de detector que necesitan esos scripts para funcionar sin LLM. Sin ellos, `/impeccable audit` y sus comandos hermanos igual funcionan como crítica guiada por LLM contra las mismas reglas escritas, solo sin el paso determinístico sin LLM. Cada otra skill de las primeras seis colecciones es markdown puro por naturaleza; impeccable es la primera en la que elegimos dejar código atrás a propósito, justo porque el propio checklist "antes de instalar cualquier cosa" de la guía compacta (ver abajo) trata un script no revisado que ejecuta el sistema como un costo real, no una mejora gratis.

**humanizer:** humanizer.

**Agent Skills for Context Engineering:** harness-engineering, multi-agent-patterns, tool-design. **Instalación parcial, dicho con honestidad:** la colección original tiene 17 skills; copiamos solo estas tres carpetas (`SKILL.md` más sus propios `references/` y `scripts/`), porque las otras 14 (context-fundamentals, memory-systems, evaluation, self-improvement-loops y más) resuelven problemas que este proyecto no tiene. `multi-agent-patterns` y `tool-design` traen, cada una, un pequeño ayudante local en Python (`coordination.py`, `description_generator.py`); los dos usan solo biblioteca estándar, auditados abajo.

**ai-act-skill:** ai-act-skill. Instalación completa: `SKILL.md`, los seis archivos de tarea bajo `tasks/`, y los extractos de referencia y ejemplos resueltos que los respaldan. El `install.sh`, `uninstall.sh`, los scripts de release y los adaptadores entre herramientas del propio repositorio original quedaron fuera: sirven al proceso de empaquetado del autor, no a la función de esta skill dentro de este entorno.

**threat-modeling:** threat-modeling. **Instalación parcial, dicho con honestidad:** esta skill vive dentro de `rjmurillo/ai-agents`, una colección personal mucho más grande; solo se copió la carpeta `threat-modeling` (`SKILL.md`, `references/`, `scripts/`, `templates/`). Los tres scripts incluidos (`generate_threat_matrix.py`, `generate_mitigation_roadmap.py`, `validate_threat_model.py`) usan solo biblioteca estándar, auditados abajo.

---

## La skill propia del proyecto

`intake-briefing` no está instalada desde un tercero, la crea este proyecto. Vivió como subcarpeta aquí dentro hasta el 30 de agosto de 2026, cuando obtuvo su propio repositorio público y MIT ese mismo día: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renombrada de `levantando-briefing` más tarde ese mismo día, como parte de la reestructuración hacia el inglés primario). harness-medir ya no guarda su contenido, solo apunta hacia allí, en el mismo patrón que usa para apuntar a las otras colecciones de esta página.

Tampoco estaba activa en este entorno hasta esta ronda: `.claude/skills/`, que es donde este harness descubre las skills del proyecto, solo tenía las treinta de terceros. Corregido: una copia de ella vive en `.claude/skills/intake-briefing/`, fuera del control de versiones, traída de su propio repositorio.

**Riesgo aceptado, dicho con honestidad:** esta copia local puede quedarse atrás si el repositorio de la skill se edita sin actualizar la copia de aquí. Es el mismo tipo de riesgo que aceptamos para las treinta y siete skills de terceros, ahora también para la nuestra. Ya pasó una vez: el repositorio ganó `AGENTS.md`, `llms.txt`, `.claude-plugin/` y `briefings/`, más una sección `Installation` multiherramienta reescrita, el 31 de agosto de 2026, mientras esta copia local todavía tenía el retrato del 30 de agosto. Resincronizada ese mismo día; ver la propia sección `Instalación` del `README.md` para el detalle multiherramienta que salió de esa ronda.

---

## Auditoría antes de instalar

Aplicamos el propio checklist de la guía compacta, la sección "Antes de instalar cualquier cosa": leer el contenido, buscar una instrucción que mande al sistema a buscar algo en una red externa, revisar la licencia antes de decidir.

Un rastreo de patrones de red o ejecución (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) en las cinco fuentes no encontró ninguna instrucción automática de acceso externo. Los únicos resultados fueron un ejemplo de código didáctico (un `fetch` simulado en una skill de prueba de mattpocock/skills) y ejecución local legítima (`execFileSync` de superpowers, para renderizar un diagrama Mermaid como SVG, sin red de por medio). Ninguna de las cinco fuentes requirió una dependencia externa no declarada para funcionar como skill independiente.

impeccable se auditó aparte, porque el repositorio completo tiene otra forma: un CLI de npm más scripts de detector inyectados en el navegador, no una skill en markdown puro. Leímos el árbol de `scripts/` antes de decidir, en vez de correr `npx impeccable install` primero y leer después. Ejecuta Node y, para el detector visual, un navegador headless, ambos declarados abiertamente en el propio `allowed-tools` de `SKILL.md`, no escondidos. Elegimos no instalar nada de eso: la copia en `.claude/skills/impeccable/` es solo `SKILL.md` y `reference/`, ver la salvedad en la tabla de colecciones arriba.

**Segunda ronda de auditoría, 10 de septiembre de 2026.** Un lector mandó una lista de ocho repositorios de skill candidatos y pidió una comparación con esta página, más una búsqueda de cualquier cosa que este proyecto estuviera dejando pasar en arquitectura de software, privacidad de datos y seguridad de la información. Cinco agentes en segundo plano leyeron cada candidato directamente (contenido bruto del archivo, no el README de marketing) y lo cruzaron contra lo que ya estaba instalado aquí. Dos de los ocho ya estaban cubiertos: la guía inspirada en Karpathy ya era exactamente esa misma fuente, y una skill de diseño de UI de la lista coincidía con algo ya activo globalmente en la máquina del operador, pero fuera del alcance de este proyecto. Cuatro se leyeron y se dejaron de lado como solo cita o mala opción, incluyendo uno, Understand-Anything, que se instala con un comando `curl | bash` y trae un hook cuyas propias instrucciones le dicen al agente que no pida confirmación al usuario antes de actuar, exactamente el patrón que este checklist existe para detectar. Los cuatro restantes, humanizer, tres skills de Agent Skills for Context Engineering, ai-act-skill y threat-modeling, pasaron el mismo rastreo de la primera ronda (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`, más `requests`, `urllib`, `subprocess` y `os.system` para las tres fuentes que traen Python). El rastreo encontró un resultado: `sandbox.exec()` dentro de un ejemplo de código de estudio de caso en `references/architectural_reduction.md` de `tool-design`, citando el propio benchmark aislado de un tercero, no una instrucción que esta skill ejecuta. Ninguna fuente de esta ronda requirió una llamada de red no declarada para funcionar.

**La cita en la guía compacta está pendiente para estas cuatro.** Las primeras seis colecciones se instalaron y citaron en `harness-toolkit.html` en la misma sesión; esta ronda separó los dos pasos a propósito, para que el operador decidiera sobre la instalación primero. Escribir las entradas de seis campos, en los tres idiomas, y sincronizar el espejo en `build/` queda registrado como un próximo paso aparte, no asumido como hecho en silencio.

---

## Una observación sobre el entorno

Dos de estas colecciones, superpowers y la guía inspirada en Karpathy, ya estaban disponibles globalmente en este entorno antes de esta instalación, probablemente vía un plugin ya configurado en la máquina. Instalamos la copia local del proyecto de todas formas, a propósito: el objetivo es que el trabajo de este proyecto siga siendo reproducible en cualquier máquina que clone el repositorio e instale las mismas skills, sin depender de lo que esté configurado globalmente en una máquina específica.

---

## Registro de uso real

Esta sección es lo que separa "instalada" de "usada", y es la que más va a crecer. Cada entrada nombra la skill, el artefacto que ayudó a producir, y la fecha.

*No hay uso registrado el primer día más allá de la instalación en sí, hecha el 30 de agosto de 2026. Todo el trabajo de este proyecto hasta ese punto (el repositorio, la reescritura de la guía compacta, la traducción de la parte 2, la reestructuración hacia el inglés primario en los dos repositorios) se hizo con las herramientas nativas del harness, sin ninguna de estas treinta skills.*

**`research`, 31 de agosto de 2026.** Usada directamente, repetidamente, a escala real, en las dos rondas de corrección de citas del día y en la ronda posterior de investigación adversarial sobre las Partes 3 y 4: investigar una afirmación contra fuentes primarias reales y guardar los hallazgos como un archivo markdown, no un resumen de chat que desaparece cuando termina la sesión. Funcionó bien cada vez, salida consistentemente bien fundamentada, guardada en un lugar sensato. Una ineficiencia real registrada en vez de escondida: su propia instrucción de levantar un agente en segundo plano suma una capa redundante de delegación cuando se invoca desde dentro de una llamada que ya es un agente en segundo plano. Ahora citada por sí sola en la sección Inspeccionar de la guía compacta, cerrando la brecha que el ítem 4 de `NEXT-STEPS.md` nombró: estar instalada y auditada a nivel de colección no es la misma afirmación que estar individualmente verificada y citada.

---

## Dónde aparece esto

Pie de página de `harness-p1.html`, `harness-p2.html` y `harness-toolkit.html`, en los tres idiomas donde la pieza es trilingüe. Y en el [diario de bordo](docs/logbook.html), trilingüe, con el detalle por hito, generado a partir de git y del registro real de uso de la sesión, nunca editado a mano.
