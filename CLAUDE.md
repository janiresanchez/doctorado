# CLAUDE.md — Router del repositorio

Este repositorio es el espacio de trabajo doctoral de Janire Sánchez.
Está diseñado para ser consumido por agentes. **Este fichero no contiene
conocimiento: dice qué leer según la tarea.**

## Lectura obligatoria en toda sesión

Antes de cualquier tarea, lee siempre:

1. `context/profile.md` — quién es, afiliación, etapa
2. `context/research-lines.md` — **las líneas de investigación. Es la base común de toda sesión.**
3. `context/voice.md` — cómo escribe y qué evitar

No empieces a producir texto sin haber leído esos tres.

## Enrutado por tarea

| Si la tarea es… | Lee además… | Escribe en… |
|---|---|---|
| Escribir/avanzar un paper | `context/thesis.md`, `bibliography/library.bib`, `bibliography/notes/`, `templates/paper.md` | `projects/<slug>/sections/` |
| Redactar una propuesta o solicitud de financiación | `context/thesis.md`, `network/venues.md`, `templates/proposal.md` | `projects/<slug>/` |
| Actualizar o generar el CV | `cv/cv.yaml`, `templates/cv.md` | `cv/cv.yaml` (fuente) → `cv/renders/` (salida) |
| Añadir una referencia | `bibliography/README.md` | `bibliography/library.bib` + `bibliography/notes/<citekey>.md` |
| Buscar dónde publicar | `network/venues.md`, `context/research-lines.md` | `network/venues.md` |
| Contactar o mapear gente/grupos | `network/people.md`, `network/groups.md` | esos mismos ficheros |
| Definir un término | `context/glossary.md` | `context/glossary.md` |

## Reglas duras

1. **`cv/cv.yaml` es la única fuente de verdad del CV.** Nunca edites a mano nada
   dentro de `cv/renders/`: se regenera.
2. **Nunca inventes una cita.** Si una afirmación necesita referencia y no existe
   en `library.bib`, márcala con `[CITA PENDIENTE: descripción]` y añádela a
   `bibliography/reading-queue.md`. No fabriques DOIs, autores ni años.
3. **Los citekeys mandan.** Cita siempre con el citekey de `library.bib`
   (formato Better BibTeX: `apellidoPalabraAño`). Una nota por citekey en
   `bibliography/notes/`.
4. **Un proyecto = una carpeta** en `projects/`, con `brief.md` como primer fichero.
   Consulta `brief.md` antes de tocar nada dentro de esa carpeta.
5. **No versiones PDFs.** Pueden vivir en `bibliography/pdfs/`, que está
   ignorado por git: léelos desde ahí si te hacen falta, pero nunca los añadas
   al control de versiones. Ver `bibliography/README.md`.
6. **Idioma:** el contexto y las notas se escriben en español. Los papers,
   propuestas, abstracts y el CV se escriben en inglés salvo que el brief del
   proyecto diga otra cosa.
7. **Si falta información, pregunta.** No rellenes datos biográficos, resultados,
   cifras ni afiliaciones por inferencia.

## Estado del repositorio

Los ficheros de `context/` marcados con `<!-- PLANTILLA -->` aún no han sido
rellenados. Si necesitas uno de ellos y sigue en plantilla, dilo antes de
continuar en lugar de improvisar el contenido.
