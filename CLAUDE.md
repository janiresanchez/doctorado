# CLAUDE.md — Router del repositorio

Este repositorio es el espacio de trabajo doctoral de Janire Sánchez.
Está diseñado para ser consumido por agentes. **Este fichero no contiene
conocimiento: dice qué leer según la tarea.**

No hay build, ni tests, ni dependencias. Es un repositorio de texto plano
(Markdown, YAML, BibTeX) más algún script puntual de Python de la librería
estándar. Trabajar aquí es leer, escribir y commitear ficheros.

## Lectura obligatoria en toda sesión

Antes de cualquier tarea, lee siempre:

1. `context/profile.md` — quién es, afiliación, etapa, restricciones prácticas
2. `context/research-lines.md` — **las líneas de investigación. Es la base común
   de toda sesión y donde viven las decisiones ya tomadas.**
3. `context/voice.md` — cómo escribe y qué evitar (tres registros distintos)

No empieces a producir texto sin haber leído esos tres.

## Estado actual (agosto 2026)

Contexto mínimo para no reabrir decisiones cerradas ni prometer lo que no hay:

- **Etapa:** pre-doctorado. **No hay tesis ni matrícula.** Se está definiendo la
  pregunta para proponerla a la Cátedra UNESCO EADS (UNED).
- **Línea principal: C-D** — alfabetización ecosocial en Secundaria/FP/Bachillerato,
  con eje en desinformación climática y diseño factorial 2×2
  (currículo ambiental/no ambiental × territorio rural/urbano).
  C-B está **descartada**; C-A y C-C quedan debilitadas. Ver
  `context/research-lines.md` antes de proponer nada distinto.
- **Decisión cerrada (2026-08-22):** el arraigo rural es **motivación personal,
  no objeto de estudio**. No lo conviertas en constructo a medir.
- **Instrumento de referencia:** CAFTÁN (`martinezaznarAlfabetizacion2022`),
  diseñado para 4º de ESO; requiere adaptación y piloto.
- **Proyecto activo:** `projects/2026-propuesta-tesis/` — la propuesta a la
  directora. **Se escribe en español** (excepción explícita a la regla de idioma).

## Enrutado por tarea

| Si la tarea es… | Lee además… | Escribe en… |
|---|---|---|
| Escribir/avanzar un paper | `context/thesis.md`, `bibliography/library.bib`, `bibliography/notes/`, `templates/paper.md` | `projects/<slug>/sections/` |
| Redactar una propuesta o solicitud de financiación | `context/thesis.md`, `network/venues.md`, `templates/proposal.md` | `projects/<slug>/` |
| Avanzar la propuesta a la Cátedra | `projects/2026-propuesta-tesis/brief.md`, `notes.md`, `outline.md` | `projects/2026-propuesta-tesis/sections/` |
| Empezar un proyecto nuevo | skill `new-project`, `templates/project-skeleton/` | `projects/<slug>/` |
| Actualizar o generar el CV | skill `update-cv`, `cv/cv.yaml`, `templates/cv.md` | `cv/cv.yaml` (fuente) → `cv/renders/` (salida) |
| Añadir una referencia | skill `add-reference`, `bibliography/README.md` | `bibliography/reading-queue.md` + `bibliography/notes/<citekey>.md` |
| Buscar dónde publicar | `network/venues.md`, `context/research-lines.md` | `network/venues.md` |
| Contactar o mapear gente/grupos | `network/people.md`, `network/groups.md` | esos mismos ficheros |
| Escribir un email | `templates/email.md`, `network/people.md`, `context/voice.md` | `projects/<slug>/sections/` |
| Definir un término | `context/glossary.md` | `context/glossary.md` |

## Skills disponibles

En `.claude/skills/`. Invócalas cuando la tarea encaje, en vez de improvisar
el flujo:

- **`new-project`** — monta `projects/<slug>/` desde `templates/project-skeleton/`.
  Solo andamiaje: no escribe contenido.
- **`add-reference`** — da de alta una referencia y su nota de lectura a partir
  de un DOI, URL o cita.
- **`update-cv`** — añade un mérito a `cv/cv.yaml` o genera un CV/bio desde el YAML.

## Anatomía del repositorio

```
context/          Perfil, líneas de investigación, tesis, voz, glosario.
                  Cambia poco; se lee en toda sesión.
bibliography/     library.bib (exportado de Zotero) + una nota por citekey en
                  notes/ + reading-queue.md. pdfs/ existe en disco pero está
                  en .gitignore.
network/          groups.md, people.md, venues.md — mapa del campo y destinos.
projects/         Una carpeta por output. brief.md es siempre el primer fichero.
                  _ARCHIVE/ para lo cerrado.
cv/               cv.yaml (fuente única) → renders/ (generado, nunca a mano).
templates/        Esqueletos: paper, proposal, abstract, cv, email y
                  project-skeleton/ (brief, outline, notes, refs).
.claude/skills/   Flujos automatizados.
```

## Reglas duras

1. **`cv/cv.yaml` es la única fuente de verdad del CV.** Nunca edites a mano nada
   dentro de `cv/renders/`: se regenera. Un render editado se desincroniza en
   silencio y propaga datos falsos a una solicitud.
2. **Nunca inventes una cita.** Si una afirmación necesita referencia y no existe
   en `library.bib`, márcala con `[CITA PENDIENTE: descripción]` y añádela a
   `bibliography/reading-queue.md`. No fabriques DOIs, autores ni años.
3. **Los citekeys mandan.** Cita siempre con el citekey de `library.bib`
   (formato Better BibTeX: `apellidoPalabraAño`, minúsculas, sin acentos).
   Una nota por citekey en `bibliography/notes/`.
4. **`library.bib` no se edita a mano.** Lo sobrescribe Zotero (Better BibLaTeX,
   *Keep updated*). Para incorporar algo, pásalo por `reading-queue.md` y por la
   nota, y recuérdale a Janire que lo guarde en Zotero.
5. **Un proyecto = una carpeta** en `projects/`, nombrada `YYYY-<slug-corto>`,
   con `brief.md` como primer fichero. Consulta `brief.md` antes de tocar nada
   dentro de esa carpeta: fija destino, límite de palabras, coautores y estado.
6. **No versiones PDFs.** Pueden vivir en `bibliography/pdfs/`, que está
   ignorado por git: léelos desde ahí si te hacen falta, pero nunca los añadas
   al control de versiones. Ver `bibliography/README.md`.
7. **Idioma:** el contexto y las notas se escriben en español. Los papers,
   propuestas, abstracts y el CV se escriben en inglés **salvo que el brief del
   proyecto diga otra cosa** — y el de `2026-propuesta-tesis` dice español.
8. **Si falta información, pregunta.** No rellenes datos biográficos, resultados,
   cifras ni afiliaciones por inferencia. Ni cuartiles, ni factores de impacto,
   ni importes de ayudas.
9. **Los datos no verificados van marcados.** `reading-queue.md` y varias notas
   arrastran metadatos de búsquedas web sin comprobar, y `profile.md` tiene
   alertas abiertas (p. ej. el plazo de admisión UNED). Mantén esas marcas: no
   las conviertas en hechos al reescribir.

## Estado de los ficheros

Estos siguen marcados con `<!-- PLANTILLA -->` y aún no tienen contenido real:

- `context/thesis.md` — coherente con que aún no haya tesis
- `context/glossary.md`
- `network/venues.md`

Si necesitas uno de ellos y sigue en plantilla, **dilo antes de continuar** en
lugar de improvisar el contenido.

Aviso aparte: **`bibliography/library.bib` está vacío** (solo cabecera), mientras
que `bibliography/notes/` ya tiene seis notas. Los citekeys que se usan hoy
(`martinezaznarAlfabetizacion2022`, `sanchezBehavioural2026`,
`fernandezramosOasis2015`, `cookDeconstructing2018`, `cookNeutralizing2017`,
`lewandowskyClimate2021`) existen en las notas pero **no** en el `.bib`. Puedes
citarlos apoyándote en la nota, pero si vas a compilar bibliografía advierte de
que falta la exportación de Zotero.

## Convenciones de escritura

- **Registros:** `context/voice.md` define tres (académico en inglés, ensayo en
  español, divulgación institucional). **No los mezcles.** Emoji solo en el tercero.
- **Nada de relleno:** fuera *"It is important to note that"*, *"Cabe destacar
  que"*, *"En el mundo actual"*. Fuera adverbios enfáticos sin sentido estadístico.
- **Calibración:** afirma lo que el dato sostiene y marca lo plausible como tal.
- **Renders del CV:** `cv/renders/YYYY-MM_cv_<destino>.<ext>`.

## Generación de documentos

`projects/2026-propuesta-tesis/build_guion.py` genera un `.docx` escribiendo
OOXML a mano con `zipfile` (sin dependencias). Se ejecuta con `python3`.

⚠️ La constante `OUT` del script contiene una ruta absoluta de la máquina
original (`/Users/jansor17/…`). Si lo ejecutas en otro entorno, ajústala antes
—o mejor, hazla relativa al fichero. El orden de los elementos dentro de
`w:pPr` es rígido: Word rechaza el documento si se altera.

## Git

- Los `.docx` y otros binarios generados sí se versionan; los PDFs y los datos
  crudos no (ver `.gitignore`).
- Mensajes de commit en español, en imperativo y descriptivos, siguiendo los
  existentes: "Anadir literatura de desinformacion climatica y analisis del
  prototipo de instrumento". El historial mezcla mensajes con y sin acentos;
  cualquiera de las dos formas es aceptable.
