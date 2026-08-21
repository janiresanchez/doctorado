# CV

`cv.yaml` es la **única fuente de verdad**. Cualquier CV, biografía corta,
resumen de méritos o sección de equipo de una propuesta se genera desde ahí.

`renders/` contiene las salidas (Markdown, PDF, versiones recortadas por
convocatoria). **Nunca se editan a mano**: si algo está mal, se corrige el YAML
y se vuelve a generar. Un render editado a mano se desincroniza en silencio y
acaba propagando datos falsos a una solicitud.

Convención de nombres para los renders:
`YYYY-MM_cv_<destino>.<ext>` — p.ej. `2026-09_cv_marie-curie.pdf`.
