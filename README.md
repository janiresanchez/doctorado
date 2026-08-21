# Doctorado

Espacio de trabajo doctoral de Janire Sánchez, diseñado para trabajar con
agentes de IA. Contexto, bibliografía, red de contactos y producción escrita
en un solo sitio, en texto plano y versionado.

## Cómo funciona

El repositorio se organiza en tres capas:

1. **Contexto** (`context/`) — quién soy, qué investigo, cómo escribo.
   Cambia poco y se lee en toda sesión.
2. **Conocimiento** (`bibliography/`, `network/`) — bibliografía, notas de
   lectura, grupos y personas. Crece de forma acumulativa.
3. **Producción** (`projects/`, `cv/`) — papers, propuestas, CV. Efímera por
   proyecto.

`CLAUDE.md` es el router: no contiene conocimiento, indica qué leer según la tarea.

## Estructura

```
context/         Perfil, líneas de investigación, tesis, voz, glosario
bibliography/    library.bib (Zotero) + una nota de lectura por citekey
network/         Grupos, personas y revistas/congresos de interés
projects/        Una carpeta por output (paper, propuesta, capítulo)
cv/              cv.yaml como fuente única + renders generados
templates/       Esqueletos en inglés: paper, propuesta, abstract, CV, email
.claude/skills/  Flujos automatizados: new-project, add-reference, update-cv
```

## Primeros pasos

1. Rellenar `context/profile.md`, `context/research-lines.md` y `context/voice.md`.
   Los ficheros marcados con `<!-- PLANTILLA -->` están vacíos a propósito.
2. Configurar la exportación automática de Zotero a `bibliography/library.bib`
   (ver `bibliography/README.md`).
3. Volcar los méritos existentes en `cv/cv.yaml`.

## Convenciones

- El contexto y las notas se escriben **en español**; los papers, propuestas y
  el CV **en inglés**.
- Los PDFs no entran en el repositorio: se quedan en Zotero.
- `cv/cv.yaml` es la única fuente de verdad del CV; `cv/renders/` se genera.
- Las citas usan el citekey de `library.bib`. Ninguna cita se inventa.
