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

No usar bibliotecas de gráficos. No usar imágenes rasterizadas.

---

## Glosario

Estilo de libro. Orden alfabético que ignora los acentos. Sin filete entre entradas. Término en negrita, dos puntos, definición en la misma línea, origen al final en cursiva con enlace. Sangría francesa.

En el cuerpo del texto, el término aparece con subrayado punteado, con información al pasar el cursor y enlace a la entrada.

Los nombres propios se alfabetizan por apellido: "Deming, W. Edwards".

---

## Referencias

**Enlazar solo donde la URL fue verificada.** Cuando la fuente es conocida pero la dirección no fue comprobada, la fuente aparece en texto plano sin enlace.

Las referencias apuntan a la fuente primaria, nunca a un blog de consultoría ni a una vitrina de skills sin repositorio de origen visible.

Un inventario que solo recomienda no es un inventario, es un catálogo de proveedor. Cada entrada también indica cuándo no usarla.

---

## Navegación cruzada

Cuatro capas, todas implementadas:

1. Barra de la serie en la parte superior de cada documento, junto al selector de idioma.
2. Enlaces en el cuerpo: las menciones a una banda o a MEDIR llevan a la sección correspondiente de la Parte 1. Las menciones a una herramienta llevan a su entrada en la guía compacta.
3. Un bloque "Dónde estás" al final de cada pieza.
4. Un glosario con una única redacción por entrada, replicada entre documentos.

---

## Idiomas

El inglés es el idioma de producción primario de este proyecto en los dos repositorios públicos, decisión tomada el 30 de agosto de 2026. El contenido nuevo se escribe primero en inglés; el portugués y el español son traducciones completas producidas a partir de él, nunca al revés. Esto no exige rehacer el contenido que ya estaba completo en los tres idiomas antes de esa fecha.

Tres versiones completas por pieza, en el mismo archivo, con selector. El inglés es la pestaña predeterminada.

**Español:** tratamiento de "tú", no de "usted".
**Inglés:** ortografía británica.
**MEDIR** se mantiene como nombre propio del método en los tres idiomas.

Los identificadores de ancla y los marcadores SVG llevan prefijo de idioma. Nunca generar contenido nuevo sin pasarlo por la función `scope()`.

Una pista de idioma del navegador se aplica en las cuatro páginas HTML trilingües: si el idioma del navegador del visitante es portugués o español y no coincide con la pestaña activa, y ningún hash con prefijo de idioma ya está enrutando la página, un banner descartable en ese idioma ofrece el cambio. Cualquier otro idioma de navegador cae en silencio al inglés. GitHub renderiza los archivos Markdown del repositorio de la skill sin ejecutar JavaScript, así que el equivalente allí es una línea estática de navegación de idioma en la parte superior de cada archivo, no una línea adaptativa.

---

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
