---
name: update-cv
description: Actualiza cv/cv.yaml con un mérito nuevo (publicación, congreso, beca, docencia) o genera un CV, biografía corta o sección de méritos desde el YAML. Úsalo ante cualquier tarea de CV, bio o resumen de trayectoria.
---

# CV

## Si es AÑADIR un mérito

1. Lee `cv/cv.yaml`.
2. Localiza la sección correcta y añade la entrada respetando el esquema de
   campos ya presente en los comentarios.
3. Verifica los datos: DOI, año, volumen, páginas. **Nunca rellenes cuartil,
   factor de impacto ni importe de una ayuda por estimación.** Si no lo sabes,
   deja el campo vacío y dilo.
4. Si es una publicación, enlaza su `citekey` con `bibliography/library.bib`.
5. Nunca escribas en `cv/renders/` en este flujo.

## Si es GENERAR un documento

1. Lee `cv/cv.yaml` y `context/profile.md`.
2. Usa `templates/cv.md` como orden de secciones. Omite las vacías.
3. Escribe en inglés salvo indicación contraria.
4. Guarda en `cv/renders/YYYY-MM_cv_<destino>.md`.
5. Si la convocatoria impone un límite de páginas o secciones, recorta por
   relevancia para esa convocatoria y **di explícitamente qué has dejado fuera**.
6. Solo puede aparecer en el render lo que exista en el YAML. Si el CV queda
   escaso, la solución es completar el YAML, no rellenar el documento.
