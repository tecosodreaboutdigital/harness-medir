*Lee en [English](TOOLS.md) · [Português](TOOLS.pt.md).*

# Herramientas y skills usadas en este proyecto

Registro de lo que este proyecto realmente instaló y usa, no solo de lo que cita. Un proyecto sobre ingeniería de harness que no instrumentara su propia creación sería solo un argumento bonito. Este documento es la instrumentación.

Actualizado el 30 de agosto de 2026. Crece con cada skill nueva que entra en uso, nunca se reescribe por completo.

---

## Colecciones de terceros instaladas

Seis colecciones, treinta y una skills, todas con licencia MIT o Apache 2.0. Instaladas localmente en `.claude/skills/`, fuera del control de versiones (ver `.gitignore`): funcionan en este entorno, pero el código de terceros no entra en el historial público de este repositorio. Cada una se cita como una entrada en la [guía compacta](harness-toolkit.html). Suma `intake-briefing`, la skill propia del proyecto tratada en la sección siguiente, y el entorno tiene 32 skills activas en total.

| Colección | Origen | Skills instaladas | Por qué entró |
|---|---|---|---|
| superpowers | [github.com/obra/superpowers](https://github.com/obra/superpowers) | 14, la colección entera | Es el patrón de regla innegociable más señales de alerta que `STANDARDS.md` ya adopta como estándar de escritura de skills de este proyecto |
| mattpocock/skills | [github.com/mattpocock/skills](https://github.com/mattpocock/skills) | 12, selección curada | Skills de escritura, clarificación y traspaso de sesión. El conjunto de ingeniería de software de la colección (TDD, arquitectura de código, conflictos de merge, TypeScript) quedó fuera por no aplicarse a un proyecto de contenido, ver la lista completa abajo |
| c4-skills | [github.com/muthub-ai/c4-skills](https://github.com/muthub-ai/c4-skills) | 2, la colección entera | El modelo C4 y los registros de decisión de arquitectura, relevantes para la ronda de investigación de la parte 3 |
| Guía inspirada en Karpathy | [github.com/multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) | 1 | Guía de comportamiento contra errores comunes de LLM. No es realmente de Karpathy, ver la salvedad completa en `sources/inventory.md` |
| ai-slop-cleaner | [github.com/yeachan-heo/oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) | 1 | Fuente real de la matriz de cinco reglas de limpieza citada en la sección Reforzar de la parte 2 |
| impeccable | [github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable) | 1 | Referencia de QA de diseño para las propias páginas HTML del proyecto: 61 reglas determinísticas de detector para tics comunes de frontend generado por IA, Apache-2.0, 30 colaboradores. Instalada solo como documentación, ver la salvedad abajo |

---

## Las treinta y una skills, por colección

**superpowers:** brainstorming, dispatching-parallel-agents, executing-plans, finishing-a-development-branch, receiving-code-review, requesting-code-review, subagent-driven-development, systematic-debugging, test-driven-development, using-git-worktrees, using-superpowers, verification-before-completion, writing-plans, writing-skills.

**mattpocock/skills:** claude-handoff, grill-me, handoff, research, retro, teach, to-questionnaire, wait-what, writing-beats, writing-for-agents, writing-fragments, writing-shape.

**c4-skills:** adr-scribe, c4-model (la carpeta de origen llama a esta skill `c4designer`, pero el propio encabezado interno de `SKILL.md` declara el nombre `c4-model`; renombramos la carpeta local para que coincida con el nombre declarado).

**Guía inspirada en Karpathy:** karpathy-guidelines.

**ai-slop-cleaner:** ai-slop-cleaner.

**impeccable:** impeccable. **Instalación parcial, dicho con honestidad:** copiamos `SKILL.md` y cada archivo bajo `reference/`, nada bajo `scripts/`. El propio encabezado de la skill original lista `Bash(npx impeccable *)` y `Bash(node .../scripts/*)` como herramientas permitidas, ligadas a 61 reglas determinísticas de detector que necesitan esos scripts para funcionar sin LLM. Sin ellos, `/impeccable audit` y sus comandos hermanos igual funcionan como crítica guiada por LLM contra las mismas reglas escritas, solo sin el paso determinístico sin LLM. Cada otra skill de esta página es markdown puro por naturaleza; impeccable es la primera en la que elegimos dejar código atrás a propósito, justo porque el propio checklist "antes de instalar cualquier cosa" de la guía compacta (ver abajo) trata un script no revisado que ejecuta el sistema como un costo real, no una mejora gratis.

---

## La skill propia del proyecto

`intake-briefing` no está instalada desde un tercero, la crea este proyecto. Vivió como subcarpeta aquí dentro hasta el 30 de agosto de 2026, cuando obtuvo su propio repositorio público y MIT ese mismo día: [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing) (renombrada de `levantando-briefing` más tarde ese mismo día, como parte de la reestructuración hacia el inglés primario). harness-medir ya no guarda su contenido, solo apunta hacia allí, en el mismo patrón que usa para apuntar a las otras cinco colecciones de esta página.

Tampoco estaba activa en este entorno hasta esta ronda: `.claude/skills/`, que es donde este harness descubre las skills del proyecto, solo tenía las treinta de terceros. Corregido: una copia de ella vive en `.claude/skills/intake-briefing/`, fuera del control de versiones, traída de su propio repositorio.

**Riesgo aceptado, dicho con honestidad:** esta copia local puede quedarse atrás si el repositorio de la skill se edita sin actualizar la copia de aquí. Es el mismo tipo de riesgo que aceptamos para las treinta skills de terceros, ahora también para la nuestra. Ya pasó una vez: el repositorio ganó `AGENTS.md`, `llms.txt`, `.claude-plugin/` y `briefings/`, más una sección `Installation` multiherramienta reescrita, el 31 de agosto de 2026, mientras esta copia local todavía tenía el retrato del 30 de agosto. Resincronizada ese mismo día; ver la propia sección `Instalación` del `README.md` para el detalle multiherramienta que salió de esa ronda.

---

## Auditoría antes de instalar

Aplicamos el propio checklist de la guía compacta, la sección "Antes de instalar cualquier cosa": leer el contenido, buscar una instrucción que mande al sistema a buscar algo en una red externa, revisar la licencia antes de decidir.

Un rastreo de patrones de red o ejecución (`curl`, `wget`, `fetch(`, `eval(`, `child_process`, `Invoke-WebRequest`) en las cinco fuentes no encontró ninguna instrucción automática de acceso externo. Los únicos resultados fueron un ejemplo de código didáctico (un `fetch` simulado en una skill de prueba de mattpocock/skills) y ejecución local legítima (`execFileSync` de superpowers, para renderizar un diagrama Mermaid como SVG, sin red de por medio). Ninguna de las cinco fuentes requirió una dependencia externa no declarada para funcionar como skill independiente.

impeccable se auditó aparte, porque el repositorio completo tiene otra forma: un CLI de npm más scripts de detector inyectados en el navegador, no una skill en markdown puro. Leímos el árbol de `scripts/` antes de decidir, en vez de correr `npx impeccable install` primero y leer después. Ejecuta Node y, para el detector visual, un navegador headless, ambos declarados abiertamente en el propio `allowed-tools` de `SKILL.md`, no escondidos. Elegimos no instalar nada de eso: la copia en `.claude/skills/impeccable/` es solo `SKILL.md` y `reference/`, ver la salvedad en la tabla de colecciones arriba.

---

## Una observación sobre el entorno

Dos de estas colecciones, superpowers y la guía inspirada en Karpathy, ya estaban disponibles globalmente en este entorno antes de esta instalación, probablemente vía un plugin ya configurado en la máquina. Instalamos la copia local del proyecto de todas formas, a propósito: el objetivo es que el trabajo de este proyecto siga siendo reproducible en cualquier máquina que clone el repositorio e instale las mismas treinta skills, sin depender de lo que esté configurado globalmente en una máquina específica.

---

## Registro de uso real

Esta sección es lo que separa "instalada" de "usada", y es la que más va a crecer. Cada entrada nombra la skill, el artefacto que ayudó a producir, y la fecha.

*Todavía no hay uso registrado más allá de la instalación en sí, hecha el 30 de agosto de 2026. Todo el trabajo de este proyecto hasta ese punto (el repositorio, la reescritura de la guía compacta, la traducción de la parte 2, la reestructuración hacia el inglés primario en los dos repositorios) se hizo con las herramientas nativas del harness, sin ninguna de estas treinta skills. De aquí en adelante, todo uso real entra en este registro antes de reclamarse en cualquier artículo.*

---

## Dónde aparece esto

Pie de página de `harness-p1.html`, `harness-p2.html` y `harness-toolkit.html`, en los tres idiomas donde la pieza es trilingüe. Y en el [diario de bordo](docs/logbook.html), trilingüe, con el detalle por hito, generado a partir de git y del registro real de uso de la sesión, nunca editado a mano.
