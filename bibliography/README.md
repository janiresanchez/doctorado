# Bibliografía

## Regla principal

La bibliografía vive como **texto plano**, no como PDFs. El repositorio guarda
metadatos y notas; los PDFs se quedan en Zotero (por peso y por copyright) y
están excluidos en `.gitignore`.

## Ficheros

- **`library.bib`** — fichero maestro. **Se sobrescribe exportando desde Zotero,
  no se edita a mano.**
- **`notes/<citekey>.md`** — una nota por referencia. Esto es lo que un agente
  lee para citar con criterio; el `.bib` solo aporta los metadatos.
- **`reading-queue.md`** — por leer. Basta con un DOI o un enlace.
- **`pdfs/`** — PDFs descargados. **Está en `.gitignore`: existe en el disco pero
  nunca se sube.** Sirve para que un agente pueda leer un PDF sin salir del
  repositorio, sin que el repositorio engorde ni distribuya material con
  copyright. Nómbralos por citekey cuando puedas.

## Configurar Zotero (una vez)

1. Instala el plugin **Better BibTeX**.
2. Ajusta el patrón de citekey a `auth.lower + shorttitle(1,0) + year`
   (produce `sanchezenergy2025`).
3. Botón derecho sobre la biblioteca o colección → *Export Library* →
   formato **Better BibLaTeX**, marca **Keep updated**, y guarda como
   `bibliography/library.bib`.

Con *Keep updated* activo, Zotero reescribe el fichero solo. Tú únicamente
haces `git add`.

## Añadir una referencia

1. Guárdala en Zotero (así se actualiza `library.bib`).
2. Crea `notes/<citekey>.md` a partir de `notes/_TEMPLATE.md`.
3. Etiqueta la nota con la línea de investigación (`L1`, `L2`…).

Si no tienes acceso a Zotero en ese momento, apunta el DOI en
`reading-queue.md` y sigue.

## Para el agente

- Cita **solo** citekeys presentes en `library.bib`. Verifícalo antes de escribir.
- Si falta la referencia, escribe `[CITA PENDIENTE: qué haría falta demostrar]`
  y añade la entrada a `reading-queue.md`. **Nunca inventes una cita.**
- Prioriza las notas de `notes/` sobre el abstract: recogen la lectura crítica
  ya hecha.
