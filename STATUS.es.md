*Lee en [English](STATUS.md) · [Português](STATUS.pt.md).*

# Estado

Situación al 30 de agosto de 2026.

Publicado en `github.com/tecosodreaboutdigital/harness-medir` (repositorio) y `tecosodreaboutdigital.github.io/harness-medir` (GitHub Pages, los archivos HTML se renderizan como página, no solo como código fuente).

**Protección de rama en `main`, configurada el 30 de agosto de 2026.** Definida directamente vía la API de GitHub: se exige un pull request para fusionar, se exige al menos una aprobación, una aprobación se descarta si llega un commit nuevo antes de fusionar, el force push y la eliminación de la rama están bloqueados. `enforce_admins` se dejó deliberadamente apagado, así que el flujo de push directo del dueño del repositorio a `main` sigue funcionando sin cambios. El efecto real de la regla recae sobre cualquier contribución futura que llegue desde un fork: debe revisarse y fusionarse a mano, nunca automáticamente, lo cual ya era cierto en la práctica (`allow_auto_merge` ya era `false`, y ningún colaborador aparte del dueño tiene acceso de escritura), pero ahora lo impone el propio GitHub, no solo la convención.

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

### Parte 3 · La separación de poderes: qué puede hacer, y quién responde por ello

`harness-p3.html`

Trilingüe por completo desde el 30 de agosto de 2026. Nueve secciones, cinco diagramas, todos incorporados y traducidos por completo. Cerca de 5.131 palabras en inglés, 5.468 en portugués, 5.676 en español, conteos cercanos entre los tres, como se espera de una traducción real y no un resumen.

Abre con Moffatt contra Air Canada, 2024 BCCRT 149: una empresa real argumentó en un tribunal real que su chatbot era una persona legal separada que responde sola, y perdió, declarado explícitamente como precedente extranjero, no brasileño. La directora reingresa en N2, a una pequeña extensión de función de distancia de una respuesta no autorizada que habría comprometido a la empresa, el eco directo del propio error de Air Canada. Tesis central: el modelo propone, la política autoriza, la herramienta ejecuta, el registro atestigua, cuatro funciones que no pueden vivir en el mismo lugar, con el modo de fallo nombrado, concentración. La regla de dos (dato privado, contenido no confiable, comunicación externa, como máximo dos sin humano en el bucle) sirve de herramienta operativa de la pieza, el equivalente de la matriz de guías y sensores de la parte 2, junto a una matriz general de autoridad basada en reversibilidad. La identidad gana un dueño nombrado y la distinción entre delegación en nombre de y autónoma; la inyección se trata como arquitectura, no configuración; un punto de reversión registrado antes de la ejecución, no después, ancla lo que debe quedar en el registro; el riesgo de cadena de suministro de un skill de terceros cierra el gancho que la parte 2 dejó abierto; las obligaciones legales corren en dos columnas, Brasil (artículo 20 de la LGPD, fechado como todavía no regulado específicamente) y Europa (artículos 12, 14 y 26 de la Ley de IA de la UE). Las dos obligaciones de honestidad que señaló la investigación se honran en el texto: el origen extranjero del precedente Air Canada, y la afirmación fechada sobre la regulación brasileña.

Barra de la serie y enlaces de glosario y fuentes ya implementados, según la arquitectura compartida de arriba.

### Parte 4 · La oficina de agentes: cuántos existen, quién es dueño de cada uno, y cuáles todavía se pagan a sí mismos

`harness-p4.html`

Inglés completo desde el 30 de agosto de 2026, cerca de 6.900 palabras, nueve secciones, cinco diagramas (D6 a D10, el D10 renderizado ahora para esta pieza, ver `diagrams/README.md`). El portugués y el español son por ahora un boceto honesto de "traducción en curso", el mismo estado por el que pasó la parte 3 más temprano ese mismo día antes de que llegara su propia traducción completa; `harness-p4.html` se lee bien en las tres pestañas, el inglés es simplemente el único completo hasta ahora.

Abre con las 20.225 cuentas de Instagram tomadas entre el 17 de abril y el 31 de mayo de 2026 mediante una sola interacción mediada por IA que combinó gestión de identidad y recuperación de credenciales, el modo de fallo por concentración de la parte 3 a escala poblacional, en lugar de en una sola acción. La directora reingresa operando seis sistemas que todos llaman agentes y no puede responder la pregunta más simple de un consejero: cuántos hay, y quién es dueño de cada uno. Tesis central: el ciclo de vida del agente, seis estados y no pasos, distinguido de MEDIR de forma explícita, con las dos transiciones que casi nadie implementa, certificación vencida y sin ejecución en el período, ambas llevando al desmantelamiento y ambas exigiendo una decisión humana, nunca una automatización. Cuatro roles bajo una regla de no acumulación reflejan la separación de poderes de la parte 3 en el plano organizacional, con una fuente nueva esta ronda, el Modelo de las Tres Líneas del Instituto de Auditores Internos, adoptado en 2013. Ocho indicadores se declaran explícitamente como síntesis, no estándar de mercado, con el indicador de tasa de rechazo en el portón fundamentado en la decisión del caso SCHUFA (TJUE, asunto C-634/21, diciembre de 2023), exactamente como funciona el fundamento legal de la parte 3, el hilo que une a las dos piezas. Dónde se ubica la oficina recurre al precedente de la línea de reporte del CISO, con fuente en un relevamiento de 2026 y la cita del jefe de bomberos y los rociadores. La restricción explícita atraviesa toda la pieza: todo lo que propone tiene que funcionar en una empresa con siete agentes y una hoja de cálculo, ilustrada con una descripción genérica y sin atribución de lo que ya hacen hoy los paneles de agentes y las cinco brechas más allá de ese piso. Cierra con el arco de la directora a lo largo de las cuatro partes y la tabla de cierre propia de la serie.

Diez entradas de glosario añadidas esta ronda (oficina de agentes, dueño del agente, certificador, patrocinador del área, regla de no acumulación, ciclo de vida, materia oscura de identidad, Heinrich, costo por tarea completada, Modelo de las Tres Líneas), en los tres idiomas, en orden alfabético; corregirlas también arregló cinco bugs de alfabetización preexistentes en el glosario en portugués y uno en el español, remanentes de una ronda anterior que tradujo términos sin reordenarlos. `harness-sources.html` ganó una sección de la parte 4, 32 fuentes incluida la decisión primaria del TJUE todavía sin localizar, en el mismo criterio V o P de la parte 3.

### Skill intake-briefing

`github.com/tecosodreaboutdigital/intake-briefing`, repositorio propio desde el 30 de agosto de 2026, renombrada de `levantando-briefing` ese mismo día, como parte de la reestructuración hacia el inglés primario ("levantando" era un verbo común en portugués, no un nombre propio establecido como lo son MEDIR y harness). Artefacto original del proyecto, completo, publicado, MIT. Cuatro archivos, cada uno con una traducción en portugués y español al lado: `SKILL.md`, `interview-script.md`, `briefing-template.md`, `README.md`.

Decide si la automatización debe existir, antes de discutir cómo funciona. Ocho bloques, una tabla determinista de derivación de banda, un veredicto con tres opciones incluyendo no hacerlo, y versionado con comparación bloque por bloque.

Llena un vacío verificado: existe abundante material sobre cómo especificar bien, casi nada sobre cómo decidir si vale la pena.

Separada del monorepo harness-medir para instalación independiente, en el mismo patrón que las demás skills citadas en la guía compacta. Activa en este entorno mediante una copia local en `.claude/skills/intake-briefing/`, fuera del control de versiones, ver `TOOLS.md`.

### Guía compacta de herramientas y skills

`harness-toolkit.html`

Reescrita por completo el 30 de agosto de 2026, y traducida al inglés y al español ese mismo día como parte de la reestructuración de idioma, con el inglés como pestaña predeterminada. Organizada por los cinco pasos del MEDIR, no por categoría de producto. Dieciocho fichas de seis campos, más una sección de diagnóstico de banda al inicio para quienes llegan de la parte 1. Cada paso del MEDIR lleva una crítica registrada, no solo una recomendación. La decimoctava, `impeccable`, se añadió a Inspeccionar después, cuando el proyecto empezó a curar también herramientas de QA de diseño, ver `TOOLS.md`.

Distribución: Mapear con cuatro fichas (intake-briefing, una guía inspirada en Karpathy, c4-skills, especificación antes del código con la crítica de Böckeler y Pocock), Equipar con tres (superpowers, mattpocock/skills, planning-with-files), Delegar con tres (holdfast, clases de entorno, orquestación programada con LangGraph), Inspeccionar con cuatro (dependency-cruiser, Stryker, Semgrep, sensors-cli), Reforzar con tres (ai-slop-cleaner, limpieza como cadencia, recolección de basura).

Cada herramienta citada está verificada en `sources/inventory.md`, incluidas tres fuentes añadidas en esta reescritura: Semgrep, LangGraph y GitHub Spec Kit con enlace directo.

Repositorio publicado y público, en `github.com/tecosodreaboutdigital/harness-medir`.

### Preparación de las partes 3 y 4

`sources/inventory.md`, `diagrams/`, `STANDARDS.md`, `README.md`, `STATUS.md`, `NEXT-STEPS.md`.

Sigue el dosier de trabajo `docs/harness-p3-p4-briefing.pt.md`, añadido el 30 de agosto de 2026 con un diagnóstico estructural, siete ejes de investigación y una especificación visual de nueve diagramas, y completa los tres primeros elementos de su cola de trabajo, bloque D.

Los documentos de gobernanza ahora describen cuatro partes organizadas alrededor de un marco de tres capas, construcción, operación, gobernanza, atravesadas por las bandas N0 a N3 como regla común, en lugar de tres partes más dos acompañantes. `STANDARDS.md` ganó una sección `Diagramas`: todo diagrama nace como especificación en Mermaid, el SVG en línea deriva de él y nunca lo sustituye, la misma regla que el propio dosier propuso.

`sources/inventory.md` ganó una sección nueva, 32 fuentes distribuidas en los siete ejes de investigación del dosier más el hallazgo que reformula la apertura de la parte 3, todas traspasadas con el estado V o P original. Dos llevan una nota explícita, no solo una letra de estado, porque el vacío que marcan cambia lo que la parte 3 puede afirmar: la publicación original de Meta sobre la regla de dos nunca se leyó en la fuente primaria, y el precedente Air Canada usado para abrir la pieza es canadiense, no brasileño.

`diagrams/` ganó nueve archivos SVG independientes, D1 a D9, renderizados a partir de las especificaciones Mermaid del dosier en el sistema visual del proyecto, en inglés porque es contenido nuevo y el inglés se escribe primero. El vocabulario de gobernanza que la parte 4 necesitó, dueño del agente, homologador, auditor, patrocinador del área, y recibo mantenido distinto de registro, se fijó en esta etapa justamente para que los diagramas y la prosa no se distanciaran entre sí. Un décimo, D10, el bucle trimestral propio de la oficina, se añadió en cuanto la redacción de la parte 4 confirmó que merecía su lugar, cerrando la sección de indicadores en lugar de abrir la pieza. Ver `diagrams/README.md` para el índice completo y qué nota de renderización cumple cada archivo.

Lo que queda de la cola del dosier: la traducción de la parte 4 al portugués y al español, y consolidar el playbook. Las partes 3 y 4 ya están escritas en inglés, ver abajo.

### Diagramas D1 a D9 validados por renderizado, y una arquitectura de serie compartida

Cierra la salvedad que la ronda anterior había registrado: los nueve SVG independientes (`diagrams/part3/`, `diagrams/part4/`) nunca se habían renderizado realmente, solo verificado como XML bien formado. Ahora sí, vía Chrome headless, y revisados visualmente. Cinco cargaban bugs reales de coordenadas, todos corregidos en la fuente SVG, ninguno en la especificación Mermaid detrás, ya que ninguno de los cinco era estructural: `D3` tenía líneas de conexión que salían del centro de una caja y cortaban el texto de cajas apiladas debajo, corregido haciendo que cada línea saliera del borde de la caja más cercano al destino; `D4` cargaba dos conectores superpuestos en su primer rombo, uno del largo correcto sin punta de flecha, el otro con punta de flecha que se pasaba hasta el interior del rombo, fusionados en uno solo; la leyenda de cierre de `D5` se desbordaba 82 píxeles del lienzo de 700px; la línea más gruesa de `D7` cortaba directo la caja `IN OPERATION`, y una curva cortaba `UNDER REVIEW`, ambas redirigidas, el lienzo ganando 24 píxeles de altura; la tercera y cuarta columna de `D9` se superponían en 40 píxeles, duplicando visiblemente un borde punteado. `D1`, `D2`, `D6` y `D8` no tenían ningún bug. Cada SVG ganó un `.png` correspondiente (escala 2x, fondo blanco opaco) para publicación en Medium, ya que el editor de Medium no renderiza ni SVG en línea pegado ni HTML arbitrario.

En paralelo, la serie ganó la navegación superior que le faltaba desde la reestructuración a cuatro partes: un componente único compartido `.topbar`, en una sola línea, centrado, fijo al desplazarse, reactivo al selector de idioma (`PARTE 1 · PARTE 2 · PARTE 3 · PARTE 4 | GUÍA COMPACTA · GLOSARIO · FUENTES { PT EN ES }`, la página actual en texto plano y una parte todavía no escrita atenuada y sin enlace). Reemplaza una barra que antes existía solo en `harness-p1.html`, fija en portugués sin importar la pestaña activa, alineada a la izquierda, no fija al desplazarse. Las secciones de glosario y fuentes que las partes 1 y 2 llevaban cada una se retiraron en favor de dos páginas nuevas, compartidas y trilingües, `harness-glossary.html` (56 entradas consolidadas, sin duplicados) y `harness-sources.html` (46 fuentes consolidadas, agrupadas en fundacionales y parte 3), y todo enlace de término y cita de la serie apunta ahora ahí. `harness-p1.html`, `harness-p2.html` y `harness-toolkit.html` se retrofitaron; `build_p2.py` y `build_toolkit.py` se actualizaron para reproducir la misma barra en una próxima regeneración, cerrando la brecha donde una reconstrucción deshacía el arreglo en silencio. Ver las secciones `Navegación cruzada` y `Glosario` de `STANDARDS.md` para la regla que esto ahora sigue.

---

## Sin empezar

### Estado de las traducciones

| Pieza | PT | EN | ES |
|---|---|---|---|
| Parte 1 | lista | lista | lista |
| Parte 2 | lista | lista | lista |
| Guía compacta | lista | lista | lista |
| Parte 3 | lista | lista | lista |
| Parte 4 | falta | lista | falta |
| Skill de briefing | lista | lista | lista |
| Documentos de gobernanza | lista | lista | lista |

### Playbook

Consolidación de las cuatro partes más la guía, sumando lo que todavía no existe: una plantilla de contrato de tarea, una plantilla de skill, una plantilla de recibo de ejecución, una matriz de riesgo, un diagnóstico de banda, una ruta de implementación, y una plantilla de registro de agentes y acta de homologación.

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

**La serie tiene cuatro partes, no tres, organizadas alrededor de tres capas, construcción, operación, gobernanza, atravesadas por la regla N0 a N3, decisión tomada el 30 de agosto de 2026.** Se consideró una cuarta capa, para alojar la propia regla, y se descartó: N0 a N3 ya cumple ese papel, y un segundo eje duplicaría vocabulario sin ganancia. Ver `docs/harness-p3-p4-briefing.pt.md`.

**El vocabulario de gobernanza de la parte 4 se fija antes de la prosa:** dueño del agente, homologador (el estado es homologado), auditor, patrocinador del área, y recibo mantenido distinto de registro. Fijado en la etapa de renderización de los diagramas, justamente para que los nueve archivos SVG en `diagrams/` y el texto futuro del artículo no se distancien entre sí.
