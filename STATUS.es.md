*Lee en [English](STATUS.md) · [Português](STATUS.pt.md).*

# Estado

Situación al 30 de agosto de 2026.

Publicado en `github.com/tecosodreaboutdigital/harness-medir` (repositorio) y `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, los archivos HTML se renderizan como página, no solo como código fuente).

---

## Listo

### Reestructuración hacia el inglés primario

El inglés se convirtió en el idioma de producción primario de este proyecto en los dos repositorios públicos el 30 de agosto de 2026, decisión tomada a mitad de camino de un proyecto que hasta entonces era primero-portugués. Todo documento de gobernanza, la guía compacta y la skill de briefing fueron renombrados y reescritos con el inglés por delante, con el portugués y el español como traducciones completas, y no al revés. Ver la sección Idiomas de `STANDARDS.md` para la regla en sí.

Mecánicamente: `PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`, `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, además de los scripts y archivos de datos correspondientes en `build/`. Cada referencia cruzada en los dos repositorios fue revisada y corregida, incluidas las URLs absolutas de blob de GitHub que apuntaban a los antiguos nombres de archivo de gobernanza y las anclas con prefijo de idioma que enlazan la Parte 2 con la guía compacta. Las descripciones de commits históricos dentro del diario del proyecto se dejaron deliberadamente nombrando los archivos antiguos donde eso era literalmente cierto en el momento de ese commit, con una nota añadida donde el cambio de nombre posterior necesitaba reconocerse, para que el diario siga siendo un relato fiel, y no uno ordenado en retrospectiva.

Las piezas trilingües ya completas (`harness-p1.html`, `harness-p2.html`, `docs/logbook.html`) tuvieron su pestaña predeterminada cambiada de portugués a inglés: el atributo `<html lang>`, el botón activo de la barra de idioma y qué `<main>` queda oculto, todo se movió, tanto en los archivos ya compilados como en los scripts de compilación que los regeneran, para que una nueva compilación no revierta en silencio al valor predeterminado en portugués.

Se añadió una pista de idioma del navegador a las cuatro páginas HTML trilingües: si el idioma del navegador del visitante es portugués o español y todavía no coincide con la pestaña activa, y ningún enlace explícito con prefijo de idioma está enrutando la página, un pequeño banner descartable ofrece el cambio, redactado en ese idioma. Cualquier otro idioma de navegador cae al inglés sin banner. GitHub no ejecuta JavaScript dentro del Markdown renderizado, así que los doce archivos del repositorio de la skill llevan, en cambio, una línea estática de navegación de idioma en la parte superior de cada uno.

### Diario de bordo

`docs/logbook.html`, trilingüe. Documenta la evolución del propio proyecto: palabras publicadas y tokens consumidos por hito, generado a partir de git y de la transcripción real de la sesión, nunca escrito a mano. Ver `build/generate_logbook_metrics.py` y `build/build_logbook.py`. Seis hitos registrados hasta ahora a partir del historial completo del repositorio, más lo que todavía está en la sesión abierta.

### Parte 1 · El mejor modelo del mundo dentro de una empresa sin proceso

`harness-p1.html`

Totalmente trilingüe, trece secciones más el bloque de navegación, tres diagramas, 26 entradas de glosario. Cerca de 4.700 palabras en portugués, 4.500 en inglés, 4.700 en español.

Contenido: una escena de apertura con la directora, qué es un harness, la analogía de la delegación, el linaje histórico con una corrección a la atribución del término, cuatro casos de estudio con números, el ciclo MEDIR, la tabla de equivalencias con el vocabulario de calidad, las bandas N0 a N3, riesgos a nivel de consejo, un checklist de doce preguntas.

Barra de la serie y bloque "Dónde estás" ya implementados.

### Parte 2 · Guías y sensores: cómo un agente aprende a corregirse

`harness-p2.html`

Totalmente trilingüe desde el 30 de agosto de 2026. Diecisiete secciones, tres diagramas, 26 entradas de glosario por idioma. Cerca de 6.200 palabras en portugués, 6.350 en inglés, 6.450 en español.

Reescrita por completo después de una primera versión descartada. La versión descartada fallaba por abandonar al personaje, no continuar la historia de la parte 1, y organizarse por concepto en lugar de por el ciclo.

Contenido: abre en la cuarta semana con la directora habiendo escrito toda la guía y el sistema liberando la factura de un proveedor desacreditado. Secciones ancladas en Equipar, Delegar e Inspeccionar, con Reforzar al final. Incluye la matriz de guías y sensores, la comparación entre un mensaje de error que enseña y una alarma, el truco del umbral, la unidad de durabilidad, tres ejemplos completos con un SKILL.md real, las clases de entorno cruzadas con las bandas, y la limpieza como cadencia.

Traducción al inglés en ortografía británica, al español por "tú". MEDIR y harness se mantienen como nombres propios en los tres idiomas, según `STANDARDS.md`. Los ejemplos de skill (nombres de archivo, campos, valores) también se tradujeron, no solo la prosa alrededor.

El JavaScript de cambio de idioma de la parte 1 y la parte 2 ganó enrutamiento por ancla: un enlace como `harness-p1.html#en-opening` ahora selecciona la pestaña correcta antes de desplazarse, en lugar de abrir siempre en la pestaña predeterminada. Sin ese ajuste, un lector en inglés que hiciera clic en cualquier referencia cruzada hacia la parte 1 siempre terminaba en portugués.

### Skill intake-briefing

`github.com/tecosodreaboutdigital/intake-briefing`, repositorio propio desde el 30 de agosto de 2026, renombrada de `levantando-briefing` ese mismo día, como parte de la reestructuración hacia el inglés primario ("levantando" era un verbo común en portugués, no un nombre propio establecido como lo son MEDIR y harness). Artefacto original del proyecto, completo, publicado, MIT. Cuatro archivos, cada uno con una traducción en portugués y español al lado: `SKILL.md`, `interview-script.md`, `briefing-template.md`, `README.md`.

Decide si la automatización debe existir, antes de discutir cómo funciona. Ocho bloques, una tabla determinista de derivación de banda, un veredicto con tres opciones incluyendo no hacerlo, y versionado con comparación bloque por bloque.

Llena un vacío verificado: existe abundante material sobre cómo especificar bien, casi nada sobre cómo decidir si vale la pena.

Separada del monorepo harness-medir para instalación independiente, en el mismo patrón que las demás skills citadas en la guía compacta. Activa en este entorno mediante una copia local en `.claude/skills/intake-briefing/`, fuera del control de versiones, ver `TOOLS.md`.

### Guía compacta de herramientas y skills

`harness-toolkit.html`

Reescrita por completo el 30 de agosto de 2026, y traducida al inglés y al español ese mismo día como parte de la reestructuración de idioma, con el inglés como pestaña predeterminada. Organizada por los cinco pasos del MEDIR, no por categoría de producto. Diecisiete fichas de seis campos, más una sección de diagnóstico de banda al inicio para quienes llegan de la parte 1. Cada paso del MEDIR lleva una crítica registrada, no solo una recomendación.

Distribución: Mapear con cuatro fichas (intake-briefing, una guía inspirada en Karpathy, c4-skills, especificación antes del código con la crítica de Böckeler y Pocock), Equipar con tres (superpowers, mattpocock/skills, planning-with-files), Delegar con tres (holdfast, clases de entorno, orquestación programada con LangGraph), Inspeccionar con cuatro (dependency-cruiser, Stryker, Semgrep, sensors-cli), Reforzar con tres (ai-slop-cleaner, limpieza como cadencia, recolección de basura).

Cada herramienta citada está verificada en `sources/inventory.md`, incluidas tres fuentes añadidas en esta reescritura: Semgrep, LangGraph y GitHub Spec Kit con enlace directo.

Repositorio publicado y público, en `github.com/tecosodreaboutdigital/harness-medir`.

---

## Sin empezar

### Parte 3 · Gobernanza de agentes

Alcance definido, base de investigación débil. Es la pieza de mayor valor comercial y la de base más superficial.

Alcance: permiso impuesto fuera del modelo, instrucciones maliciosas que llegan dentro de un dato o de una skill de terceros, un registro auditable, reversión, obligaciones legales, y quién responde por lo que hizo el agente.

Lo que aún falta investigar, y es una ronda dedicada, no un complemento: literatura de seguridad de agentes, incidentes reales documentados, la posición de la autoridad brasileña de protección de datos sobre decisiones automatizadas, obligaciones regulatorias europeas para sistemas clasificados como de alto riesgo, y lo que ya existe como estándar de auditoría de agentes.

Escribirla ahora produciría una opinión bien escrita, no una referencia.

### Estado de las traducciones

| Pieza | PT | EN | ES |
|---|---|---|---|
| Parte 1 | lista | lista | lista |
| Parte 2 | lista | lista | lista |
| Guía compacta | lista | lista | lista |
| Parte 3 | falta | falta | falta |
| Skill de briefing | lista | lista | lista |
| Documentos de gobernanza | lista | lista | lista |

### Playbook

Consolidación de las tres partes más la guía, sumando lo que todavía no existe: una plantilla de contrato de tarea, una plantilla de skill, una plantilla de recibo de ejecución, una matriz de riesgo, un diagnóstico de banda y una ruta de implementación.

La skill de briefing ya es su primer artefacto operativo.

---

## Decisiones tomadas que no deben revertirse sin motivo

**El inglés es el idioma de producción primario de este proyecto, decisión tomada el 30 de agosto de 2026,** para los dos repositorios públicos, aunque la conversación de trabajo con el autor siga en portugués. Ver la sección Idiomas de `STANDARDS.md`.

**El término harness no se traduce.** Se mantiene en inglés por la misma razón por la que nadie tradujo kaizen, kanban o poka-yoke. Las alternativas arnés, arreo, cabestro y silla (equivalentes aproximados en español que evocan contención) se descartaron: una metáfora de contención le vende la idea equivocada a un lector que ya teme perder el control.

**La atribución correcta del término es Mitchell Hashimoto, febrero de 2026,** no Andrej Karpathy. Karpathy acuñó vibe coding y popularizó context engineering, y su nombre aparece correctamente en esos contextos.

**Inspeccionar, y no Instrumentar, para el paso I.** Instrumentar es técnicamente más preciso y coherente con el argumento de que la calidad no se inspecciona al final de la línea, pero Inspeccionar es el término del propio repertorio del autor y la sigla depende de él.

**Ejemplos en la escalera individuo, equipo, área.** No usar "empresa" ni un nivel por encima de área.

**La escena de apertura es compuesta,** no real, y eso se declara en el pie de página de cada pieza. Si surge un caso real anonimizado del ecosistema del autor, reemplazarla mejoraría considerablemente el texto.

**La guía compacta vive aparte de los artículos,** con una fecha de revisión visible, porque envejece más rápido.

**El repositorio de la skill se renombra a intake-briefing, y no se mantiene como levantando-briefing.** A diferencia de harness y MEDIR, "levantando" nunca se estableció como nombre propio que el lector necesitara aprender, era simplemente el verbo en portugués para la función de la skill, por eso se traduce en lugar de quedar fijo.
