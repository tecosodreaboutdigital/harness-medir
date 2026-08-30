*Lee en [English](NEXT-STEPS.md) · [Português](NEXT-STEPS.pt.md).*

# Próximos pasos

En orden. Cada elemento trae su criterio de listo.

---

## Completado el 30 de agosto de 2026

**Repositorio público de GitHub creado**, en `github.com/tecosodreaboutdigital/harness-medir`. Commit inicial con los 23 archivos que existían en ese momento, sin datos sensibles. LICENSE (MIT) añadida dentro de lo que entonces era `skills/levantando-briefing/`, coherente con lo que el README de la skill ya declaraba. Sin licencia en la raíz, porque los artículos siguen bajo todos los derechos reservados.

**Guía compacta reescrita por completo.** Ver la entrada correspondiente en `STATUS.md` para el detalle. Criterio de listo cumplido: diecisiete fichas de seis campos, cada herramienta verificada en `sources/inventory.md` (tres fuentes nuevas verificadas en esa ronda: Semgrep, LangGraph, GitHub Spec Kit con enlace directo), y cada paso del MEDIR con una crítica registrada.

**Parte 2 traducida al inglés y al español**, en el mismo archivo, con el selector. `build/build_p2.py` reescrito para el ensamblado trilingüe, en el mismo patrón que `build/build_all.py` ya usaba: extrae el cuerpo en PT del archivo vigente (que es la fuente de la verdad, no `build/body_p2_pt.html`, que había quedado desactualizado), ensambla EN y ES a partir de `build/body_p2_en.html` y `build/body_p2_es.html`, prefija todo por idioma vía `scope()`. Los tres botones funcionan y no hay ninguna ancla rota. Como efecto secundario, el JavaScript de cambio de idioma en `harness-p1.html` y `harness-p2.html` ganó enrutamiento por ancla (`#en-opening` selecciona la pestaña correcta antes de desplazarse), para que un enlace cruzado entre las piezas en inglés o español no cayera siempre en la pestaña en portugués.

**Treinta skills de terceros instaladas para usarse en este proyecto**, cinco colecciones (superpowers completa, una selección curada de doce de mattpocock/skills, c4-skills completa, la guía inspirada en Karpathy, ai-slop-cleaner), todas MIT, todas auditadas contra el propio checklist de la guía compacta antes de instalarlas. Viven en `.claude/skills/`, fuera del control de versiones. Documentación completa, con un registro de uso real que crece por sesión, en `TOOLS.md`. Crédito visible en el pie de página de `harness-p1.html`, `harness-p2.html` (tres idiomas) y `harness-toolkit.html`.

**La skill separada en su propio repositorio**, en lo que entonces era `github.com/tecosodreaboutdigital/levantando-briefing`, público, MIT, en el mismo patrón que las demás skills citadas en la guía compacta. Eliminada de `skills/` dentro de harness-medir, que ahora solo apunta hacia allí.

**Diario de bordo creado**, `docs/logbook.html`, trilingüe, generado en dos pasos: `build/generate_logbook_metrics.py` reconstruye la serie real (palabras publicadas según `git show` en cada commit, líneas en `build/` y en los documentos de gobernanza, tokens sumados del `usage` real de cada mensaje en la transcripción `.jsonl` de la sesión, atribuidos al commit cronológicamente siguiente) y escribe `docs/assets/logbook-metrics.json`; `build/build_logbook.py` ensambla la página a partir de ese JSON, nunca escrita a mano. Dos gráficos SVG apilados, mismo eje X, sin eje Y doble. Seis hitos reales registrados (el historial completo del repositorio hasta ahora, no una muestra), más lo que todavía no había cerrado un hito.

**GitHub Pages activado**, publicando el repositorio en `tecosodreaboutdigital.github.io/harness-medir`. Se añadió `.nojekyll` para servir los archivos HTML tal como están, sin procesamiento de Jekyll. Sin eso, ningún artículo era realmente legible como página web allí, solo como código fuente en el visor de GitHub.

**Reestructuración hacia el inglés primario en los dos repositorios públicos.** El inglés se convirtió en el idioma de producción primario, decisión tomada a mitad de esta sesión. Todo documento de gobernanza fue renombrado y reescrito con el inglés por delante (`PADROES.md` → `STANDARDS.md`, `ESTADO.md` → `STATUS.md`, `PROXIMOS-PASSOS.md` → `NEXT-STEPS.md`, `FERRAMENTAS.md` → `TOOLS.md`, `fontes/inventario.md` → `sources/inventory.md`), cada uno con una traducción en portugués y español al lado. `harness-caixa-de-ferramentas.html` → `harness-toolkit.html`, `docs/diario-de-bordo.html` → `docs/logbook.html`, con los scripts correspondientes en `build/` renombrados y, en el caso de la guía compacta, reescritos en un ensamblado trilingüe con el inglés como pestaña predeterminada. `harness-p1.html`, `harness-p2.html` y `docs/logbook.html` tuvieron su pestaña predeterminada cambiada de portugués a inglés, tanto en los archivos compilados como en los scripts que los regeneran. Se añadió un banner de pista de idioma del navegador a las cuatro páginas trilingües (los navegadores en portugués o español reciben una oferta descartable de cambio, cualquier otro cae en silencio al inglés). El repositorio de la skill fue renombrado de `levantando-briefing` a `intake-briefing`, y cada uno de sus cuatro archivos fue reescrito con el inglés por delante, con traducciones `.pt.md`/`.es.md`, además de una línea estática de navegación de idioma en la parte superior de cada uno, ya que GitHub no ejecuta JavaScript dentro del Markdown renderizado. Ver `STATUS.md` para el detalle completo y la sección Idiomas de `STANDARDS.md` para la regla en sí.

**Cuatro skills recomendadas desde afuera, evaluadas, una adoptada.** `ponytail`, `no-ai-slop`, `taste-skill` e `impeccable` se compararon por relevancia, señal de mantenimiento, número de colaboradores y licencia antes de que cualquiera tocara este repositorio. `ponytail` (117 mil estrellas, con benchmark, mantenida activamente) habría resuelto la salvedad de atribución indebida que ya pesa sobre `karpathy-guidelines`, pero quedó de lado por ahora, no descartada. `no-ai-slop` es una skill de limpieza de prosa genuinamente útil cuya lista de palabras prohibidas incluye, por casualidad, el término central de este proyecto, "harness", y también quedó de lado hasta decidir cómo hacer la excepción. `taste-skill` se rechazó del todo: sus diez subskills usan exactamente el registro de hype que un proyecto sobre evidencia en vez de opinión no debería citar, y seis colaboradores contra 82 mil estrellas es una base frágil. `impeccable` se adoptó: Apache 2.0, 30 colaboradores, versionada (v4.1.2), deriva de la propia skill frontend-design de Anthropic, y sus 61 reglas determinísticas de detector encajan con la propia definición de Inspeccionar, evidencia en vez de opinión, aplicada específicamente al diseño de frontend. Instalada solo como documentación, `SKILL.md` y `reference/`, dejando fuera a propósito el árbol `scripts/` que necesita su CLI, ver `TOOLS.md`. Añadida como la decimoctava ficha de la guía compacta, en Inspeccionar, en los tres idiomas, ver `sources/inventory.md` para el registro de verificación.

**Preparación de las partes 3 y 4, los tres primeros elementos de la cola del dosier de trabajo.** `docs/harness-p3-p4-briefing.pt.md` fijó la cola en su bloque D, y esta ronda cerró los elementos 1 a 3. `README.md`, `STATUS.md`, `NEXT-STEPS.md` y `STANDARDS.md`, en los tres idiomas, ahora describen cuatro partes organizadas alrededor de un marco de tres capas, construcción, operación, gobernanza, atravesadas por las bandas N0 a N3, en lugar de tres partes más dos acompañantes, y `STANDARDS.md` ganó la regla de `Diagramas` que el dosier propuso: Mermaid primero, el SVG deriva y nunca sustituye. `sources/inventory.md` ganó una sección nueva que lleva las 32 fuentes del dosier distribuidas en siete ejes de investigación más el hallazgo Air Canada, estado V o P original preservado, con nota explícita en las dos que marcan un vacío real y no solo un enlace faltante: la fuente primaria de la regla de dos, y el hecho de que todavía no existe precedente brasileño. Se renderizaron nueve archivos SVG independientes, D1 a D9, en el nuevo directorio `diagrams/` a partir de las especificaciones Mermaid del dosier, en inglés por ser contenido nuevo, con el vocabulario de gobernanza de la parte 4 (dueño del agente, homologador, auditor, patrocinador del área, recibo mantenido distinto de registro) fijado en esta etapa para que los diagramas y la prosa futura no se distancien. Ver `STATUS.md` para el detalle completo y `diagrams/README.md` para el índice.

---

## 1. Escribir la parte 3

Investigación completa, ver `sources/inventory.md`. La propia sección de cierre del dosier, "Lo que la investigación cambia en la estructura planificada" en el bloque B, revisa el esbozo original de diez secciones a nueve. Reconstruida aquí para seguimiento, confirmar contra el dosier antes de redactar:

1. Air Canada abre la pieza: una empresa real argumentó en un tribunal real que su asistente era una persona legal separada, que responde sola, y perdió
2. La directora reingresa aquí, en N2, ante la primera acción irreversible, el contraste con el argumento de Air Canada es el punto
3. La separación de poderes, con la regla de dos como herramienta operativa, el equivalente de la matriz de guías y sensores de la parte 2
4. Identidad y un dueño nombrado: quién lo implementó, qué está autorizado a hacer, en nombre de quién actúa ahora
5. Cuando la orden llega dentro del dato
6. Qué necesita quedar registrado, y qué significa reversión en realidad
7. Una skill de terceros es código de terceros, cerrando el gancho que la parte 2 dejó abierto
8. Obligaciones legales en dos columnas, Brasil y Europa, lo que ya aplica antes de lo que sigue en trámite
9. Quién responde, y dónde estás, el cierre de la serie

Dos obligaciones de honestidad que el dosier marca explícitamente: declarar que el precedente Air Canada es extranjero, so pena de que un lector jurídico descalifique la pieza entera, y fechar la afirmación de que la regulación específica del artículo 20 de la LGPD todavía no se publicó, porque esa frase puede envejecer en meses.

**Listo cuando:** las tres versiones estén listas, el arco del personaje se cierre, la pieza funcione sola para un lector que no haya leído las anteriores, y los artefactos de matriz de autoridad y esquema de recibo estén en el texto.

---

## 2. Escribir la parte 4

Investigación no iniciada, alcance definido en el bloque A del dosier. Tesis central: el ciclo de vida del agente, estados y no pasos, distinguido de MEDIR con claridad suficiente para que el lector no confunda los dos.

Estructura a cubrir, según el dosier, orden sujeto a la redacción:

1. El ciclo de vida en sí, seis estados desde un briefing versionado hasta el desmantelamiento, con las dos transiciones que casi nadie implementa, homologación vencida y sin ejecución en el período, ambas llevando al desmantelamiento
2. Los cuatro roles y la regla de no acumulación, la misma separación de poderes de la parte 3, ahora en el plano organizacional
3. Los ocho indicadores, dos de los cuales miden la calidad de la propia gobernanza, no la del agente: la tasa de excepción, y la tasa de rechazo del propio portón
4. Dónde se sienta la oficina, y por qué no en TI, presentando las opciones realistas con el costo de cada una
5. La advertencia: esta es la pieza con mayor riesgo de convertirse en folleto de proveedor, y el antídoto es una restricción explícita que atraviesa el texto, todo lo que propone tiene que funcionar en una empresa con siete agentes y una hoja de cálculo
6. El argumento de cierre: toda plataforma gobierna hacia adentro, y por eso la oficina tiene que ser función de la empresa, no un producto que compra

**Listo cuando:** las tres versiones estén listas, el arco del personaje cierre la serie, los ocho indicadores estén definidos con fórmula, y el texto sostenga la restricción de siete agentes y una hoja de cálculo de principio a fin.

---

## 3. Consolidar el playbook

Reutiliza las cuatro partes y la guía, y agrega lo que todavía no existe:

- Plantilla de contrato de tarea
- Plantilla de skill, derivada de los tres ejemplos de la parte 2
- Plantilla de recibo de ejecución
- Matriz de riesgo por banda
- Diagnóstico de banda, versión cuestionario
- Ruta de implementación de N0 a N3
- Plantilla de registro de agentes y de acta de homologación

El D10, el bucle propio de la oficina por trimestre, no decidido para la parte 4, es un candidato fuerte para abrir el playbook, si queda fuera de la parte 4.

---

## Pendientes menores, a decidir en cualquier momento

**Caso real de apertura.** La escena es compuesta. Si surge un caso real anonimizado del ecosistema del autor, reemplazarla elevaría considerablemente el texto.

**Borde de la caja del índice.** Es el único borde de caja que queda en los documentos. Decidir si se elimina, para quedar coherente con la eliminación de los demás.

**Fondo de la cita destacada en la impresión.** Depende de si el navegador está configurado para imprimir gráficos de fondo. Una alternativa sin dependencias: un filete fino arriba y abajo del bloque.

**Ortografía del inglés.** Hoy es británica, y esa es la lectura predeterminada del proyecto. Si el público objetivo se desplaza hacia Estados Unidos, convertirla.

**Publicación.** Resuelta el 30 de agosto de 2026: GitHub Pages activo en `tecosodreaboutdigital.github.io/harness-medir`. Verificar, después del primer build automático, que los documentos se rendericen correctamente allí (el enlace con más probabilidad de necesitar ajuste es alguna ruta relativa entre ellos).

**Localizar la fuente primaria de la regla de dos.** Dos fuentes secundarias independientes la atribuyen a Meta con la misma formulación, suficiente para citar el contenido en la parte 3, no para enlazarla. Buscar de nuevo antes de cerrar esa pieza, ver `sources/inventory.md`.
