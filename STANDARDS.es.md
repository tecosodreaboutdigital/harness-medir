*Lee en [English](STANDARDS.md) · [Português](STANDARDS.pt.md).*

# Estándares

Reglas innegociables de este proyecto. Lee antes de editar cualquier archivo.

---

## Escritura

**La raya está prohibida bajo cualquier circunstancia.** No la uses en ningún idioma. Reemplázala por una coma, dos puntos, paréntesis o punto final. Esta es la regla más violada y la más importante.

**El guion está permitido**, incluida la separación silábica automática en texto justificado.

**Registro de la prosa:** narrativo y argumentado, en la línea de Adam Grant, Brené Brown, Simon Sinek y Malcolm Gladwell. Nada de listas de viñetas amontonadas. El texto argumenta, no enumera.

**Tono:** directo. Sin introducción larga, sin transición vacía, sin conclusión redundante, sin refuerzo positivo.

**La corrección factual pesa más que la suavidad.** Las atribuciones equivocadas se corrigen en el texto. Una herramienta sin fuente verificada no se cita.

**Evitar:** palabras de relleno como "genuinamente", "honestamente", "simplemente" (y sus equivalentes en portugués e inglés). Evitar el abuso de la construcción "no es X, es Y". Evitar las comillas irónicas alrededor de términos inventados.

---

## Formato del documento

| Elemento | Especificación |
|---|---|
| Página | A4, márgenes de 2 cm arriba y abajo, 1,5 cm en los laterales |
| Cuerpo | Aptos o Aptos Light, 10,5, justificado |
| Título de nivel 1 | 14, negrita |
| Título de nivel 2 | 12 |
| Numeración de secciones | Número en la misma línea del título. Sin etiqueta pequeña arriba. Sin numeración de subelementos |
| Tablas | Ancho completo, encabezado centrado en 8, cuerpo en 9, sin sombreado, sin colores alternados |
| Pies de figura y notas al pie | Sin borde, cursiva, tamaño 9 |
| Cita destacada | Sin borde alguno, fondo gris azulado claro, tamaño 9, protegida contra saltos de página |
| Bloques de código | Mismo fondo que las citas destacadas, sin borde, 8,5 en impresión |
| Salida | Solo HTML. Nada de DOCX, nada de Markdown para los artículos |

Excepción a la última línea: las skills y las plantillas operativas nacen en Markdown, porque son artefactos de repositorio.

---

## Sistema visual

Diagramas SVG en línea, trazo de 0,7, sin relleno, sin color. Etiquetas en versalitas espaciadas. Leyendas en cursiva 9, sin borde.

Una excepción deliberada: el diagrama de bandas usa altura creciente de las cajas para representar autonomía.

Desvíos declarados del trazo de 0,7 y de la ausencia de relleno: una línea más gruesa (0,9 o 1,3) marca énfasis, el punto de reversión en D5 y las dos transiciones que nadie implementa en D7; los marcadores de punta de flecha usan trazo 1; D9 dibuja las paredes de las plataformas a 0,5; los gráficos del diario de bordo rellenan sus puntos de dato. Un tercer gris, `#c9c7bf`, dibuja líneas de vida y cajas secundarias junto a las dos tintas. La leyenda dentro del diagrama (`svg-cap`) es de 8,5 px, en versales espaciadas, sin cursiva; la cursiva 9 vale para el `figcaption` debajo. Todo diagrama lleva `<title>` y `<desc>`, además de `role="img"` y `aria-label`.

No usar bibliotecas de gráficos. No usar imágenes rasterizadas en las páginas. La única excepción son las exportaciones en PNG de los diagramas y de los gráficos del diario de bordo, generadas a partir del SVG para Medium, el README y las tarjetas de compartir; la página en sí sigue siendo vectorial.

---

## Diagramas

Todo diagrama desde la Parte 3 nace como boceto en Mermaid, un archivo md por diagrama en `diagrams/sketches/`, escrito en inglés, el idioma de autoría. No existe una canalización de renderización: nada en este proyecto convierte Mermaid en SVG de forma mecánica. El boceto es un plan estructural en texto plano, legible en diff, que GitHub renderiza de forma nativa cuando el archivo se abre allí, nada más. Los tres diagramas de la Parte 1 y los tres de la Parte 2 son anteriores a esta regla y no tienen boceto; si uno de ellos cambia, recibe un boceto antes.

El SVG autónomo en `diagrams/` se dibuja a mano, en el sistema visual del proyecto, para coincidir con la estructura del boceto. El SVG en línea de cada idioma del HTML es una copia suya con solo el texto traducido: `build/svg_check.py`, que `build/check_all.py` ejecuta, falla si la geometría de una copia en línea difiere del archivo autónomo. Esto es deliberado, no un atajo por falta de herramienta: un renderizador genérico de Mermaid produce su propio tema y su propio diseño automático, y ninguno de los dos coincide con el sistema de trazo fino, sin relleno, sin color de este proyecto, así que dibujar a mano es el camino directo, no un rodeo.

Al cambiar la estructura o una etiqueta, cambia primero el boceto en Mermaid, luego vuelve a dibujar el SVG a mano para que coincida. Cambiar solo el SVG deja el boceto desactualizado, y la próxima sesión trabaja con el mapa equivocado.

Cada diagrama trae, en el md, su propósito y una nota de renderización, incluyendo qué necesita saltar a la vista y la frase que lleva la leyenda.

---

## Glosario

Página única compartida desde el 30 de agosto de 2026: `harness-glossary.html`, trilingüe, una entrada por término para toda la serie (partes 1 a 4, la guía compacta). Ningún documento mantiene ya su propia sección de glosario; un término definido en la parte 2 queda disponible, sin cambios, para las partes 3 y 4.

Estilo de libro. Orden alfabético que ignora los acentos. Sin filete entre entradas. Término en negrita, dos puntos, definición en la misma línea, origen al final en cursiva con enlace. Sangría francesa. Los nombres propios se alfabetizan por apellido: "Deming, W. Edwards".

En el cuerpo del texto, el término aparece con subrayado punteado, con información al pasar el cursor (el atributo `data-tip` lleva la definición corta, mostrada localmente, sin navegar) y el clic lleva a `harness-glossary.html#<idioma>-<slug>`, llegando exactamente a esa entrada. Nunca enlazar un término a un ancla local `#g-slug` dentro del propio artículo, esa ancla ya no existe ahí.

Dos excepciones y una regla son deliberadas. El glosario en portugués tiene una entrada más que los otros dos (`g-hitl`, "human in the loop") porque el portugués mantiene esa expresión en inglés y la entrada explica por qué, así que 68 contra 67 no es un error. Lo mismo vale para la etiqueta HITL en el diagrama D4. Y "token", en el sentido de la unidad en la que los modelos leen y cobran texto, se queda como "token" en portugués y español, nunca traducido como "símbolo". Los ids del glosario son un slug neutro por término, igual en los tres idiomas (`g-agent`, `g-model`, `g-chart`, `g-cyb`, `g-context`); solo cambia el prefijo de idioma.

Cuando una parte nueva introduce un término, agrégalo directamente en `harness-glossary.html` (en los tres idiomas), manteniendo la posición alfabética, y enlázalo desde el cuerpo de la parte. No dupliques la definición de vuelta en la parte.

---

## Referencias

Página única compartida desde el 30 de agosto de 2026: `harness-sources.html`, trilingüe, agrupada por dónde se recopiló la investigación (fuentes fundacionales, luego un grupo por parte). Cada cita en cualquier parte apunta aquí; ningún documento mantiene ya su propia lista numerada de fuentes.

**Enlazar solo donde la URL fue verificada.** Cuando la fuente es conocida pero la dirección no fue comprobada, la entrada aparece en texto plano (clase `orig-plain`) con la brecha declarada en la propia entrada, nunca escondida.

Las referencias apuntan a la fuente primaria, nunca a un blog de consultoría ni a una vitrina de skills sin repositorio de origen visible.

Un inventario que solo recomienda no es un inventario, es un catálogo de proveedor. Cada entrada también indica cuándo no usarla.

---

## Navegación cruzada

Cuatro capas, todas implementadas:

1. **Barra de la serie**, un componente único compartido (`.topbar`) en la parte superior de cada documento, centrado en la página, fijo al desplazarse, `docs/logbook.html` incluido desde el 31 de agosto de 2026. Una sola línea: las partes numeradas unidas por `·`, una `|` antes de los documentos complementarios, luego guía compacta, glosario y fuentes también unidos por `·`, una segunda `|` antes de un pequeño ícono de línea escalonada que lleva al diario del proyecto, luego el selector de idioma entre llaves `{ }` al final. El ícono no lleva etiqueta de texto, solo un atributo `title` para el tooltip al pasar el mouse, así que nunca compite por espacio con las partes y los complementos; en el propio diario aparece como el indicador de página actual en vez de enlace, igual que una parte cuando es la página en la que ya estás. La página actual aparece como texto plano, no como enlace; una parte aún no publicada aparece atenuada y sin enlace. Las etiquetas, los destinos de la barra y el tooltip del ícono cambian de idioma junto con el selector, gobernados por el objeto `SERIES` y la llamada `setSeries()` dentro del `set()` de cada página, nunca duplicados a mano por idioma.
2. Enlaces en el cuerpo: las menciones a una banda o a MEDIR llevan a la sección correspondiente de la Parte 1. Las menciones a una herramienta llevan a su entrada en la guía compacta. Las menciones a un término del glosario llevan a `harness-glossary.html`. Las citas llevan a `harness-sources.html`.
3. Un bloque "Dónde estás" al final de cada pieza.
4. El propio glosario y la propia página de fuentes: una redacción por entrada, una sola página, enlazada desde todas partes.

---

## Idiomas

El inglés es el idioma de producción primario de este proyecto en los dos repositorios públicos, decisión tomada el 30 de agosto de 2026. El contenido nuevo se escribe primero en inglés; el portugués y el español son traducciones completas producidas a partir de él, nunca al revés. Esto no exige rehacer el contenido que ya estaba completo en los tres idiomas antes de esa fecha.

Tres versiones completas por pieza, en el mismo archivo, con selector. El inglés es la pestaña predeterminada.

**Español:** tratamiento de "tú", no de "usted".
**Inglés:** ortografía británica.
**MEDIR** se mantiene como nombre propio del método en los tres idiomas.

Los identificadores de ancla y los marcadores SVG llevan prefijo de idioma. Nunca generar contenido nuevo sin pasarlo por la función `scope()`.

Una pista de idioma del navegador se aplica en las nueve páginas HTML trilingües: si el idioma del navegador del visitante es portugués o español y no coincide con la pestaña activa, y ningún hash con prefijo de idioma ya está enrutando la página, un banner descartable en ese idioma ofrece el cambio. Cualquier otro idioma de navegador cae en silencio al inglés. GitHub renderiza los archivos Markdown del repositorio de la skill sin ejecutar JavaScript, así que el equivalente allí es una línea estática de navegación de idioma en la parte superior de cada archivo, no una línea adaptativa.

---

El rol "certifier" de la Parte 4 se escribe "homologador" en portugués (el acto es "homologação", el estado "homologado") y "certificador" en español. La familia portuguesa se eligió el 5 de octubre de 2026 porque la Parte 4, el glosario y STATUS ya la usaban en todas partes (24 apariciones frente a un residuo), y porque "homologar" lleva el sentido de una aprobación concedida por quien tiene la autoridad para concederla, que es el rol. No mezcles las dos dentro de un mismo idioma.

## Entrada de herramienta en la guía compacta

Seis campos, siempre en este orden, en prosa y no en una lista suelta:

1. Qué problema resuelve esto
2. Qué se gana en la práctica
3. Para quién es, por banda N0 a N3
4. Banda mínima
5. Cuándo no usarla
6. Cómo empezar en quince minutos

---

## Patrón de escritura de skills

Heredado de las mejores colecciones públicas y adoptado como estándar de este proyecto:

**Regla innegociable al principio,** corta y sin ambigüedad.

**Señales de alerta justo debajo:** las racionalizaciones que el sistema probablemente usará para justificar no seguir la regla. El objetivo no es enseñar la regla, que ya conoce, sino impedir que se convenza a sí mismo de no seguirla.

**Un criterio de listo verificable,** preferentemente la salida de un comando y no una opinión.

**Un tope de intentos** con una ruta de salida explícita.

**Una sección Nunca** al final.

**Límites honestos** declarados: qué se puso a prueba, qué es inferencia, qué no hace la skill.

## Comprobaciones

Toda regla objetiva de este archivo tiene una comprobación automática en `build/check_all.py`; una regla sin comprobación se marca como tal. Reglas que todavía no tienen comprobación: el nivel de lectura de la prosa, la elección de qué fuentes citar, la exactitud de una traducción más allá de las tildes y la paridad de estructura, y la calidad visual de un diagrama más allá de la geometría que compara `build/svg_check.py`. Esas quedan con el revisor.
