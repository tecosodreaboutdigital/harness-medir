*Lee en [English](README.md) · [Português](README.pt.md).*

# La serie Harness y el ciclo MEDIR

Proyecto de contenido y herramientas sobre **ingeniería de harness**: la disciplina de construir el entorno alrededor de un modelo de IA para que opere de forma confiable.

Autor: Fernando Teco Sodré
Estado: en curso, agosto de 2026

Publicado en [github.com/tecosodreaboutdigital/harness-medir](https://github.com/tecosodreaboutdigital/harness-medir) (repositorio) y [tecosodreaboutdigital.github.io/harness-medir](https://tecosodreaboutdigital.github.io/harness-medir) (GitHub Pages, los archivos HTML se renderizan como páginas, no solo como código fuente).

---

## La tesis

> Todo el mundo tiene acceso al mismo modelo. La ventaja competitiva no está en la inteligencia que contratas, está en el entorno que construyes a su alrededor.

Un agente es igual a modelo más harness. El modelo es el motor de razonamiento, y es la parte que la industria vende. El harness es todo lo demás: lo que el sistema ve, lo que puede tocar, lo que sobrevive entre sesiones, lo que cuenta como evidencia, y cuándo la ejecución necesita detenerse y llamar a alguien.

La ingeniería de harness no es un campo nuevo. Es poka-yoke aplicado a un trabajador no determinista, y pertenece al mismo linaje de Shewhart, Deming, PDCA y el Sistema de Producción Toyota.

<p align="center">
  <img src="diagrams/part4/d6-three-layers.png" alt="Las tres capas del marco, y solo tres, atravesadas por una regla compartida: construcción, operación, gobernanza" width="680">
</p>

<p align="center"><em>D6 · Las tres capas del marco, y solo tres, atravesadas por la única regla compartida entre ellas. Diagrama todavía solo en inglés, producción primaria, ver la sección Idiomas más abajo.</em></p>

---

## El ciclo MEDIR

Método propio de este proyecto, en la familia del PDCA y el DMAIC. Funciona sin adaptación en portugués, inglés y español.

| Paso | PT | EN | ES | Qué decide |
|---|---|---|---|---|
| M | Mapear | Map | Mapear | El contrato de la tarea, los límites y el mapa del conocimiento |
| E | Equipar | Equip | Equipar | Herramientas, accesos y memoria duradera |
| D | Delegar | Delegate | Delegar | Ejecución aislada, autonomía calibrada al riesgo |
| I | Inspecionar | Inspect | Inspeccionar | Sensores que producen evidencia, no opinión |
| R | Reforçar | Reinforce | Reforzar | El fallo se vuelve cambio permanente en el entorno |

Lo que separa a MEDIR de un PDCA genérico es el paso R: actúas sobre el entorno, no sobre la respuesta. Un parche arregla una ejecución, un cambio en el harness mejora todas las siguientes.

### Bandas de autonomía

| Banda | Qué existe en el entorno | Autonomía permitida |
|---|---|---|
| N0 · Asistido | Instrucción y modelo | Ninguna, el humano revisa cada salida |
| N1 · Guiado | Guía escrita, herramientas, contrato de tarea | Tareas reversibles y de bajo costo |
| N2 · Medido | Estado duradero, sensores, tope de intentos | Tareas largas, con evidencia antes de la entrega |
| N3 · Gobernado | Permiso fuera del modelo, rastro, reversión | Acción con efecto externo, bajo aprobación humana |

Regla de dimensionamiento: el harness debe ser menor que la superficie de fallo que controla.

---

## Qué hay en este repositorio

```
.
├── README.md                          este archivo
├── STANDARDS.md                       reglas de escritura y formato, LEE ANTES DE EDITAR
├── STATUS.md                          qué está listo y qué falta, en detalle
├── NEXT-STEPS.md                      la cola de trabajo, en orden
├── TOOLS.md                           skills de terceros instaladas y usadas, con registro de uso real
├── harness-p1.html                    Parte 1, trilingüe, lista
├── harness-p2.html                    Parte 2, trilingüe, lista
├── harness-p3.html                    Parte 3, trilingüe, lista
├── harness-p4.html                    Parte 4, inglés listo, PT/ES pendiente
├── harness-toolkit.html               guía compacta, organizada por MEDIR, lista
├── harness-glossary.html              glosario compartido, trilingüe, cada parte apunta ahí
├── harness-sources.html               fuentes compartidas, trilingüe, cada parte apunta ahí
├── sources/
│   └── inventory.md                   todas las fuentes verificadas, con estado
├── diagrams/
│   ├── README.md                      índice, una fila por diagrama, notas de renderización
│   ├── part3/                         D1 a D5, SVG más un PNG emparejado para Medium
│   └── part4/                         D6 a D10, SVG más un PNG emparejado para Medium
├── docs/
│   ├── harness-p3-p4-briefing.pt.md   dosier de trabajo de las partes 3 y 4, interno, solo en portugués
│   ├── logbook.html                   trilingüe, generado a partir de git y del uso real de la sesión
│   └── assets/logbook-metrics.json    el dato bruto del diario, nunca editado a mano
└── build/                             cuerpos de texto y scripts de ensamblado
```

Los archivos HTML viven en la raíz a propósito: se referencian entre sí por ruta relativa simple. Mover cualquiera de ellos a una subcarpeta rompe la navegación cruzada.

---

## La arquitectura de la serie

Seis piezas, con ritmos de revisión distintos, organizadas alrededor de un marco de tres capas, y solo tres.

| Capa | Pregunta que responde | Pieza |
|---|---|---|
| Construcción | Cómo se construye un agente confiable | Parte 2, MEDIR |
| Operación | Qué puede hacer, y quién responde | Parte 3, la separación de poderes |
| Gobernanza | Cuántos agentes existen, quién es dueño de cada uno, cuáles todavía se pagan solos | Parte 4, la oficina de agentes |

Las bandas de autonomía N0 a N3 atraviesan las tres capas como regla común, el único vocabulario compartido entre ellas, y es eso lo que impide que el marco se convierta en tres piezas sueltas. Se dejó fuera a propósito una cuarta capa: todo marco que ha muerto, murió por exceso de vocabulario.

| Pieza | Naturaleza | Revisión |
|---|---|---|
| Parte 1, por qué | Argumento. Por qué el entorno vale más que el modelo | Poco frecuente |
| Parte 2, cómo | Método. Guías, sensores, formato de skill, ejemplos | Poco frecuente |
| Parte 3, operación | Permiso fuera del modelo, rastro, responsabilidad | Poco frecuente |
| Parte 4, gobernanza | Ciclo de vida, roles, indicadores, dónde se sienta la oficina | Poco frecuente |
| Guía compacta | Inventario de mercado, con nombres y repositorios | Trimestral |
| Playbook | Consolidación, más las plantillas operativas | Anual, por versión |

La guía compacta vive aparte justamente porque envejece más rápido. Las cuatro partes hablan de principios y no dependen de ella.

Una única barra de navegación, fija al desplazarse y reactiva al selector de idioma, atraviesa todas las páginas: las cuatro partes, la guía compacta, y dos compañeros compartidos, `harness-glossary.html` y `harness-sources.html`, que consolidan cada término y cada cita que la serie usa en lugar de repetirlos pieza por pieza.

<p align="center">
  <img src="diagrams/part3/d1-separation-of-powers.png" alt="La separación de poderes: el modelo propone, la política autoriza, la herramienta ejecuta, el registro testimonia" width="680">
</p>

<p align="center"><em>D1 · La separación de poderes: el modelo propone, la política autoriza, la herramienta ejecuta, el registro testimonia. Cuatro funciones que no pueden vivir en el mismo lugar, el argumento central de la parte 3. Ver <a href="diagrams/README.md">diagrams/README.md</a> para el índice completo de los diez diagramas.</em></p>

La parte 4 se sumó a la serie el 30 de agosto de 2026, cuando la ronda de investigación de la parte 3 expuso una segunda brecha detrás de la primera: MEDIR gobierna una tarea, no un agente, y nada en la serie hasta ese punto gobernaba el conjunto de agentes que una empresa termina operando. Ver `docs/harness-p3-p4-briefing.pt.md` para el dosier de trabajo del que salió esta decisión, interno, solo en portugués, la misma excepción que `sources/inventory.md` ya lleva. Su texto en inglés está completo desde ese mismo día; la traducción al portugués y al español es el próximo hito de contenido del proyecto.

---

## El lector

Un ejecutivo, consejero, director de área, sucesor al frente de una empresa familiar. No es un lector técnico ni de nivel intermedio. Empresas en el rango de cien a quinientos millones de reales.

La serie existe para que esa persona pueda diagnosticar en qué etapa está, entender qué necesita construir, y conversar de igual a igual con quien lo construye.

Un personaje atraviesa la serie: una directora de operaciones de una industria mediana que arma sola una automatización para revisar facturas de flete. Está compuesta a partir de patrones recurrentes y no describe una empresa específica. En la parte 1 está en N0 y sufre un accidente estructural. En la parte 2 llega a N1 y descubre que una guía sin sensor es solo una recomendación bien escrita, y termina en N2. En la parte 3 enfrenta la primera acción irreversible. La parte 4 cierra su arco: deja de ser la constructora solitaria del agente y se convierte en la persona capaz de decirle a un consejo cuántos agentes opera la empresa, quién es dueño de cada uno, y cuáles todavía se pagan solos.

---

## Idiomas

El inglés es el idioma de producción primario de este proyecto en los dos repositorios públicos, decisión tomada el 30 de agosto de 2026. Todo contenido nuevo se escribe primero en inglés, con el portugués y el español producidos como traducciones completas a partir de él.

Tres versiones completas de cada pieza: inglés, portugués y español. Un único archivo por pieza, con selector en la esquina superior derecha, inglés como pestaña predeterminada. Una pista de idioma del navegador ofrece a los visitantes de portugués o español un cambio descartable, cuando el idioma del navegador no coincide con la pestaña activa.

Detalle técnico importante: los identificadores de ancla y los marcadores SVG llevan prefijo de idioma (`en-`, `pt-`, `es-`) para evitar colisiones entre las tres versiones dentro del mismo documento. Todo contenido nuevo debe pasar por la función `scope()` de los scripts de ensamblado.

---

## Cómo continuar

1. Lee `STANDARDS.md`. Contiene las reglas de escritura y formato que no se pueden violar, incluida la prohibición absoluta de la raya.
2. Lee `STATUS.md` para saber exactamente qué está listo.
3. Sigue `NEXT-STEPS.md` en orden.
4. Antes de citar cualquier herramienta, revisa `sources/inventory.md`. Una fuente sin verificar no entra en un documento firmado.
5. Antes de instalar cualquier skill de terceros para trabajar en este proyecto, sigue el mismo checklist que el proyecto recomienda a terceros, y registra el resultado en `TOOLS.md`.

---

## Licencia

Artículos: todos los derechos reservados, uso mediante autorización.

La skill propia del proyecto, `intake-briefing`, vive en un repositorio aparte, [github.com/tecosodreaboutdigital/intake-briefing](https://github.com/tecosodreaboutdigital/intake-briefing), MIT, en el mismo patrón que las demás skills citadas en la guía compacta.
