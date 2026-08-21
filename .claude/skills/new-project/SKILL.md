---
name: new-project
description: Crea una carpeta nueva en projects/ para un paper, propuesta, capítulo o comunicación, a partir del esqueleto y del contexto del repositorio. Úsalo cuando la persona diga que va a empezar un artículo, una propuesta, un abstract o un capítulo nuevo.
---

# Nuevo proyecto

1. Lee `context/research-lines.md` y `context/thesis.md`.
2. Pregunta lo mínimo imprescindible que no puedas deducir: tipo de output,
   línea de investigación (`L1`, `L2`…), destino y deadline.
3. Elige el slug: `YYYY-<slug-corto-en-inglés>`, sin acentos ni espacios.
4. Copia `templates/project-skeleton/` a `projects/<slug>/`.
5. Copia la plantilla que corresponda (`templates/paper.md`,
   `templates/proposal.md` o `templates/abstract.md`) a
   `projects/<slug>/sections/` y renómbrala según el tipo.
6. Rellena el front-matter de `brief.md` con lo que sepas. **Deja vacío lo que
   no sepas; no lo inventes.**
7. Si el destino aparece en `network/venues.md`, arrastra a `brief.md` el límite
   de palabras y el estilo de citación. Si no aparece, añádelo allí como candidato.
8. Termina resumiendo qué falta por decidir antes de empezar a escribir.

No escribas contenido del paper en este paso. Solo se monta el andamiaje.
