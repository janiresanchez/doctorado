---
name: add-reference
description: Añade una referencia bibliográfica al repositorio a partir de un DOI, URL o cita, creando la nota de lectura correspondiente. Úsalo cuando la persona comparta un paper, un DOI o pida guardar una referencia.
---

# Añadir referencia

1. Lee `bibliography/README.md`.
2. Recupera los metadatos reales de la referencia (DOI, autores, año, revista).
   **Si no puedes verificarlos, no inventes: pídelos.**
3. Comprueba si el citekey ya existe en `bibliography/library.bib`.
   Si existe, actualiza su nota en lugar de duplicar.
4. Genera el citekey en formato Better BibTeX: `apellidoPalabraAño`
   (todo en minúsculas, sin acentos).
5. **No edites `library.bib` a mano**: es un fichero exportado por Zotero.
   Recuérdale a la persona que guarde la referencia en Zotero, y mientras tanto
   anótala en `bibliography/reading-queue.md`.
6. Crea `bibliography/notes/<citekey>.md` a partir de `notes/_TEMPLATE.md`.
   Rellena solo lo que puedas justificar con el texto; marca lo demás como
   pendiente de lectura y deja `read: false`.
7. Etiqueta la nota con las líneas (`lines:`) de `context/research-lines.md`
   con las que conecta, y explica en "Cómo lo uso" en qué proyecto encaja.
