# Proyectos

Un proyecto = un output: un artículo, una propuesta, un capítulo, una
comunicación a congreso.

## Convención de nombres

`YYYY-<slug-corto>` — p.ej. `2026-energy-poverty-index`.

El año es el de inicio y no se cambia aunque el proyecto se alargue.

## Estructura

```
YYYY-slug/
├── brief.md        # PRIMER fichero. Objetivo, destino, deadline, estado.
├── outline.md      # Esquema argumental antes de escribir prosa.
├── sections/       # Un fichero .md por sección.
├── refs.bib        # Subconjunto de bibliography/library.bib usado aquí.
├── figures/
└── notes.md        # Decisiones, feedback de directores, dudas abiertas.
```

Al cerrar un proyecto (publicado o abandonado), muévelo a `_ARCHIVE/` y anota
el resultado en `brief.md`.

## Para el agente

Lee siempre `brief.md` antes de tocar cualquier otra cosa de la carpeta: fija
el destino, el límite de palabras, los coautores y el estado real.
