*Lee esto en [English](README.md) · [Português](README.pt.md).*

# build

Cuerpos de texto y scripts de ensamblado que generan las páginas HTML de la raíz, más las verificaciones que las mantienen honestas.

## Cómo funciona

Cada página se ensambla a partir de dos partes: un cuerpo HTML por idioma, y un script de Python que prefija todo identificador por idioma (`scope()`), termina cada bloque de idioma (`common.py`) y lo pega todo en la envoltura de CSS compartida.

La envoltura se extrae de la página terminada que ya existe, para que todas las páginas sigan idénticas en formato. Cambiar el CSS en una y regenerar las demás propaga el cambio.

Páginas ensambladas aquí: `harness-p1.html` a `harness-p4.html`, `harness-toolkit.html`, `harness-playbook.html`, `harness-glossary.html`, `harness-sources.html` y `docs/logbook.html`.

## Archivos

| Archivo | Papel |
|---|---|
| `body_p1_{pt,en,es}.html` | cuerpos de la parte 1, extraídos del `harness-p1.html` publicado el 5 de octubre de 2026. El PT se reescribe en cada build; el EN y el ES son editables |
| `body_p2_{pt,en,es}.html` | cuerpos de la parte 2. El PT se reescribe en cada build; el EN y el ES son editables |
| `body_p3_*`, `body_p4_*`, `body_playbook_*`, `body_toolkit_*`, `body_glossary_*`, `body_sources_*` | cuerpos de las demás páginas, uno por idioma, todos editables. Son la fuente de la verdad |
| `build_p1.py`, `build_p2.py` | ensamblan la parte 1 y la parte 2. Autorreferentes: la envoltura y el cuerpo PT se leen de vuelta de la página publicada |
| `build_p3.py`, `build_p4.py`, `build_playbook.py`, `build_toolkit.py`, `build_glossary.py`, `build_sources.py` | ensamblan las demás páginas a partir de los tres `body_*` de cada una. Nunca leen de vuelta la página publicada |
| `build_logbook.py` | ensambla `docs/logbook.html` en tres idiomas a partir de `docs/assets/logbook-metrics.json`, incluido el gráfico de costo |
| `common.py` | reglas compartidas por todos los scripts de ensamblado: el ancla de arriba y el fragmento de idioma en los enlaces entre páginas, el atributo `lang` en cada `<main>` |
| `generate_logbook_metrics.py` | reconstruye `docs/assets/logbook-metrics.json` a partir de git, de las transcripciones reales de la sesión y de `docs/assets/prices.json`, nunca editado a mano. Modos: normal, `--recount`, `--reprice`, `--enrich [--dry-run]`, ver abajo |
| `docs/assets/prices.json` | libro mayor de precios fechado y de solo añadir (dato fuente, no script). Un hito lee la entrada vigente en su propia fecha y el costo calculado queda congelado después |
| `generate_toolkit_manifest.py` | reconstruye `toolkit.json` a partir de `TOOLS.md`, `sources/inventory.md` y `playbook/README.md`, nunca editado a mano. `--check` solo informa si está desactualizado |
| `check_all.py` | el verificador único, ver "Verificaciones" abajo |
| `svg_check.py`, `check_upstream.py` | `svg_check.py` compara la geometría de cada SVG en línea con el archivo autónomo en `diagrams/` (lo ejecuta `check_all.py` en "paridad"). `check_upstream.py` lee cada origen curado desde la API de GitHub hacia `sources/upstream.json`; necesita `gh` con sesión iniciada y se ejecuta a mano, no por las comprobaciones |
| `check_glossary_order.py`, `check_readme_snapshot.py` | dos verificaciones que `check_all.py` ejecuta, también usables por separado |
| `check_known.json` | hallazgos que existían antes de `check_all.py`. Un trinquete: solo puede encogerse |
| `stop_hook.py` | hook de parada de Claude Code, conectado en `.claude/settings.json`: ejecuta `check_all.py` cuando la sesión cambió archivos publicados e impide terminar ante un hallazgo nuevo |
| `legacy/` | `build_all.py`, `build_en.py` y `patch_p2.py`, históricos, movidos aquí el 5 de octubre de 2026 para que ningún agente los ejecute por error. Los dos primeros usan rutas fijas de sandbox y no corren en este repositorio; `build_p1.py` los reemplazó |

## Verificaciones

`python build/check_all.py` ejecuta diez comprobaciones de una vez: rayas, orden del glosario, texto alternativo de los gráficos del README, `toolkit.json`, enlaces y anclas, coherencia entre partes, hechos repetidos entre glosario y partes, tildes ausentes en portugués y español, ortografía estadounidense en inglés y paridad de secciones, tablas, SVG y tooltips entre los tres idiomas. Cada hallazgo indica el archivo, la línea, el pasaje y la corrección esperada.

Los hallazgos que existían antes del script están en `build/check_known.json` y no hacen fallar la ejecución. Cualquier hallazgo fuera de esa lista sí. Cuando se corrige uno, el script lo avisa, y `python build/check_all.py --write-baseline` lo quita de la lista. La lista solo puede encogerse. `--only NOMBRE` ejecuta una comprobación, `--strict` ignora la lista, `-v` imprime también los hallazgos conocidos.

Dos cosas lo ejecutan sin que nadie lo pida: el hook de parada (`stop_hook.py`), que protege la sesión de trabajo, y `.github/workflows/check.yml`, que protege el sitio publicado en cada push y pull request, ediciones manuales incluidas. La configuración del hook y el script son la parte de la instalación que solo debe cambiar con una persona leyendo el diff.

## Reglas críticas

`scope()` prefija identificadores de ancla y marcadores de SVG por idioma. Todo contenido nuevo tiene que pasar por ella, o las tres versiones de un mismo documento colisionan y las anclas apuntan al idioma equivocado. Escribe los cuerpos EN y ES sin prefijo de idioma en ids y anclas (`id="apertura"`, no `id="es-apertura"`), porque `scope()` pone el prefijo en el build.

`build_p1.py` y `build_p2.py` extraen el cuerpo PT directamente de la página publicada, que es la fuente de la verdad, y reescriben `body_p1_pt.html` y `body_p2_pt.html` en cada ejecución. Edita el texto PT de la parte 1 o de la parte 2 en la página publicada y luego reconstruye. Antes del 5 de octubre de 2026 la parte 1 no tenía ningún script de build: sus cuerpos PT y ES existían solo dentro de la página ensamblada, y `body_en.html` se había quedado una revisión entera atrás.

Los otros seis scripts **no** leen de vuelta la página publicada. Leen los tres idiomas de `build/body_*`. Editar una página publicada a mano sin reflejar el cambio en su cuerpo es invisible hasta la próxima regeneración, que revierte la edición sin aviso. Ocurrió el 31 de agosto de 2026, cuando `build/body_sources_*.html` quedó dos rondas de correcciones de citas por detrás de `harness-sources.html`. Ejecuta el script después de cualquier edición directa, o edita solo el cuerpo y deja que el script monte el archivo final.

Los enlaces entre páginas, en un cuerpo, se escriben sin fragmento (`href="harness-p2.html"`). `common.py` los reescribe a `harness-p2.html#pt-top`, `#en-top` o `#es-top`, según el bloque de idioma en que estén, porque el JavaScript de cambio de idioma lee el prefijo de la URL para elegir la pestaña antes de desplazarse. Un enlace sin prefijo, o con el prefijo del idioma equivocado, abre la otra página en la pestaña en inglés. Los enlaces con ancla explícita necesitan el prefijo del idioma de destino (`#en-opening`, `#es-apertura`, `#pt-abertura`). Cada bloque de idioma también empieza con un elemento de id `<idioma>-top`, lleva el atributo `lang` (`pt-BR`, `en-GB`, `es`), y el título de la pestaña acompaña el cambio de idioma, tomado del `<h1>` del bloque.

Renombrar un término del glosario cambia la letra que decide su posición pero no mueve la fila: ejecuta `python build/check_glossary_order.py` después de cualquier cambio de terminología, antes de reconstruir. Hallazgo del 11 de septiembre de 2026 (dos entradas en portugués fuera de orden durante once días sin que nadie lo notara, ver `NEXT-STEPS.md`).

Editar `TOOLS.md` (la tabla de colecciones instaladas, o la lista de skills por colección) o la tabla "Tools and skills" de `sources/inventory.md` sin ejecutar `python build/generate_toolkit_manifest.py` a continuación deja `toolkit.json` desactualizado, igual que editar `harness-sources.html` sin reflejarlo en `build/` deja que el build siguiente revierta la edición. `--check` informa la divergencia (hash de las secciones fuente) sin escribir nada.

## Costo en dinero, portado de vuelta desde `milestone-loc-tokens-ai-ledger`

El 14 de septiembre de 2026 `generate_logbook_metrics.py` incorporó la misma lógica de precio fechado y de solo añadir que ya había construido la skill que este proyecto generó (`milestone-loc-tokens-ai-ledger`, ver `NEXT-STEPS.md` punto 5): `load_price_ledger`, `find_price_series`, `price_at` y `compute_cost`, que leen `docs/assets/prices.json`. El costo de un hito se calcula una vez, al precio vigente en la fecha de ese hito, y nunca se recalcula después, aunque el libro mayor reciba una entrada nueva; `load_previous` lo garantiza leyendo el `logbook-metrics.json` de la ejecución anterior antes de sobrescribirlo.

**Un precio equivocado, corregido el 20 de septiembre de 2026.** La entrada del 13 de septiembre registró Sonnet 5 a US$3/15, pero el precio cobrado es US$2/10 (el aumento previsto para el 1 de septiembre se canceló, según la página de precios de Anthropic leída ese día, junto con la visión general de modelos). La entrada equivocada sigue en el libro mayor, y una segunda, con `corrects` y el motivo, la reemplaza: en un empate de fecha, `price_at` elige la entrada escrita después. Como una ejecución normal nunca recalcula un costo grabado, `python build/generate_logbook_metrics.py --reprice` es el camino explícito y auditado para ese caso, portado de `milestone-loc-tokens-ai-ledger`: recalcula solo el costo de los hitos ya grabados, a partir de los tokens ya grabados en ellos, sin leer git ni ninguna transcripción, y guarda el costo anterior en `repricings` dentro del propio hito. Ejecutarlo de nuevo, sin entrada nueva en el libro mayor, no cambia nada. No uses `--reprice` para un cambio de precio normal: una entrada con `effective_date` posterior ya deja cada hito antiguo al precio vigente en su fecha.

**El límite del reprice, cerrado el 20 de septiembre de 2026.** `tokens_bucket` guarda solo los cuatro contadores originales, porque así los suma `build_logbook.py` (`sum(m['tokens_bucket'].values())`). El port solía fijar el precio de toda escritura de caché a `cache_creation_price`, y en las transcripciones de este proyecto toda escritura de caché leída es de 1 hora, a un precio más alto. El corte por modelo y por TTL de caché vive ahora en una clave hermana, `tokens_split`, y `price_milestone` fija el precio de cada modelo con su propia serie y las escrituras de 1 hora al precio de 1 hora. Una escritura de 1 hora bajo una entrada sin `cache_creation_1h_price` queda sin precio, nunca al precio de 5 minutos. Los 79 hitos que ya existían se migraron con `--enrich`, y el costo grabado de los 14 que tenían uno pasó de US$77,7944 a US$83,1673 (+US$5,3729), medido hito a hito.

**Límite honesto, no escondido.** `docs/assets/prices.json` tiene tres series, todas desde el 13 de septiembre de 2026: Sonnet 5, Opus 5 y Haiku 4.5. Las dos últimas entraron el 20 de septiembre de 2026 bajo una suposición registrada en cada entrada (el precio leído ese día vale desde el 13 de septiembre, sin fuente que date el cambio), ver `NEXT-STEPS.md` punto 6. Todo hito anterior muestra `cost_recorded: null` en la salida y "sin precio" en el diario publicado, nunca un costo inventado. Eso es lo esperado, no un bug: este script no afirma un precio que no verificó. A diferencia del propio motor de tokens (una sesión continua que cubre todo el proyecto), el precio de un LLM cambia por decisión comercial del proveedor, no por uso de este proyecto, así que no se puede reconstruir retroactivamente sin una fuente real para cada fecha.

## Congelamiento, `--enrich` y `--recount`, portados de `milestone-loc-tokens-ai-ledger` el 20 de septiembre de 2026

La regla: congelar el hecho de granularidad más fina y derivar el precio después. Un costo grabado es un número derivado; los tokens, por modelo y por TTL de caché, son el hecho.

- **Ejecución normal.** Nunca reabre los tokens de un hito ya grabado (`tokens_bucket`, `tokens_split`): vienen del archivo, no de la transcripción, porque Claude Code borra las transcripciones pasado `cleanupPeriodDays` (30 días por defecto). Solo un commit nuevo deriva tokens. Palabras y líneas también se reutilizan por hash de commit, mientras `count_rules_hash` (una huella de `CONTENT_HTML`, `CODE_GLOBS_PREFIXES`, `GOV_DOCS` y `COUNT_ALGORITHM_VERSION`) sea la misma de la ejecución que las grabó. Sin la marca, o con una distinta, el script recuenta todo y avisa por qué; el primer recuento completo tardó unos ocho minutos, una ejecución normal tarda cerca de un segundo. **Sube `COUNT_ALGORITHM_VERSION` siempre que `word_count_html` o `line_count` cambien de comportamiento**, o los recuentos congelados siguen valiendo con una regla que ya no es la misma.
- **`--recount`.** Fuerza el recuento de palabras y líneas de todos los hitos e imprime toda diferencia contra lo grabado. Sirve de prueba de que una refactorización no movió ningún número publicado.
- **`--reprice`.** Como antes, ahora con fijación de precio por modelo y por TTL: recalcula solo el costo, a partir de los tokens grabados, sin leer git ni transcripciones.
- **`--enrich [--dry-run]`.** La migración única de un hito grabado antes del corte por modelo y TTL. Solo enriquece un hito si sus cuatro contadores originales, rederivados de las transcripciones, son exactamente iguales a los grabados; si no, se niega y lo deja intacto, y el código de salida es 3. Un hito con costo grabado tiene el costo recalculado y gana un registro en `repricings` con `"reason": "enrich"`; uno sin costo solo gana el corte de tokens. **Lee el informe del `--dry-run` antes de ejecutar de verdad, y haz commit de `logbook-metrics.json` antes**, para que el estado anterior quede en git. Tiene plazo: cuando la transcripción expira, el hito ya no puede enriquecerse.
- **Subagentes.** Claude Code archiva las transcripciones de subagentes en `<sesión>/subagents/*.jsonl`, no junto a la sesión madre, y este script nunca las leyó hasta el 20 de septiembre de 2026 (unos 257 millones de tokens ese día, un quinto más que el total contado). Desde entonces **cuentan**, por decisión del autor: se capturan por hito en `subagent_tokens` (hecho congelado, por modelo y TTL), y lo que leen los totales, los gráficos y el costo es `tokens_total`, la suma de `tokens_bucket` (sesiones madre) y `subagent_tokens`, derivada en cada ejecución, nunca congelada. `tokens_bucket` y `tokens_split` siguen siendo solo de sesiones madre, porque son el hecho que la guarda de `--enrich` contrasta con la transcripción. Un token de subagente se atribuye al próximo commit de este repositorio, donde sea que ocurriera el trabajo, y 43 de las 114 transcripciones también nombran la ruta de otro repositorio (41 de ellas `milestone-loc-tokens-ai-ledger`, cuyo diario propio cuenta esas 41 por su ruta): los dos diarios no deben sumarse. `--reprice --note TEXTO` graba el motivo en cada registro de `repricings`.
- **`unpriced`.** La lista de tokens sin precio solo se graba en un costo parcial. Un hito sin ningún costo ya lo dice todo con `cost_recorded: null`.

## Al regenerar el diario de bordo, en orden

El diario describe los commits anteriores, así que la regeneración viene después de ellos. El commit de la propia regeneración es siempre el único hito sin narrativa, y la regeneración siguiente lo describe.

1. `python build/generate_logbook_metrics.py` (cerca de un segundo; recontar todo solo con `--recount` o si cambian las reglas de conteo).
2. Escribir la narrativa de los hitos nuevos en `COMMIT_TXT`, en `build_logbook.py`, en tres idiomas. El build se detiene con un `KeyError` en el hash que falta, a propósito.
3. `python build/build_logbook.py`.
4. Reexportar los tres gráficos del README desde `docs/logbook.html` a `docs/assets/logbook-*.png`, con un recorte exacto de 616 por 230 a 2x, que da 1232 por 460 (sin el recorte sale 462).
5. Actualizar, en los tres README, el texto alternativo del gráfico de palabras (palabras y número de hitos) y comprobar con `python build/check_readme_snapshot.py`.
6. `python build/generate_toolkit_manifest.py --check`, y luego `python build/check_all.py`.

## Si `generate_logbook_metrics.py` se reutiliza en otro repositorio

Hallazgo por reutilización directa en un proyecto externo más pequeño, registrado en `NEXT-STEPS.md`: el script funciona bien aquí, pero carga tres decisiones implícitas que necesitan ajuste manual antes de correr en cualquier otro lugar, ninguna expuesta como parámetro de línea de comandos.

1. **El sufijo del directorio de sesión** (`target_suffix` en `_project_dir()`, usado por `find_session_jsonl()` y `find_subagent_jsonl()`) es específico de este clon, en esta máquina. No existe forma segura de descubrirlo por algoritmo, porque la sanitización de rutas de Claude Code es un detalle interno no documentado. Lista `~/.claude/projects/` una vez y confirma el nombre real antes de cambiar el sufijo.
2. **`CONTENT_HTML`, `CODE_GLOBS_PREFIXES` y `GOV_DOCS`** están fijados para la estructura de archivos de este repositorio. Reescribe los tres por completo para cualquier otro proyecto.
3. **La deduplicación de uso por `message.id`**, dentro de `load_usage_events()`, tiene que entrar en cualquier copia nueva de este script desde el principio. Sin ella, el conteo de tokens se duplica (hallazgo real aquí, corregido en septiembre de 2026, ver `NEXT-STEPS.md`), porque un mismo mensaje del asistente genera más de una línea en la transcripción, cada una con el total acumulado del mensaje entero, repetido.
