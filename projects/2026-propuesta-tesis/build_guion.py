#!/usr/bin/env python3
"""Genera el guion de reunión en .docx sin dependencias externas."""
import zipfile, os, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "Guion_reunion_Catedra_UNESCO.docx")

def esc(t):
    return html.escape(t, quote=False)

def runs(text, bold=False, italic=False, color=None, size=None):
    """Soporta **negrita** dentro del texto."""
    out = []
    parts = text.split("**")
    for i, part in enumerate(parts):
        if part == "":
            continue
        b = bold or (i % 2 == 1)
        rpr = "<w:rPr>"
        if b: rpr += "<w:b/>"
        if italic: rpr += "<w:i/>"
        if color: rpr += f'<w:color w:val="{color}"/>'
        if size: rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/>'
        rpr += "</w:rPr>"
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    return "".join(out)

def p(text="", style=None, space_before=0, space_after=120, italic=False,
      color=None, size=None, border=False, indent=0, bullet=False):
    # El esquema OOXML fija el orden dentro de w:pPr:
    # pStyle, numPr, pBdr, spacing, ind, outlineLvl. Word rechaza otro orden.
    ppr = "<w:pPr>"
    if style:
        ppr += f'<w:pStyle w:val="{style}"/>'
    if bullet:
        ppr += '<w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
    if border:
        ppr += ('<w:pBdr><w:bottom w:val="single" w:sz="4" w:space="1" '
                'w:color="BFC9C2"/></w:pBdr>')
    ppr += f'<w:spacing w:before="{space_before}" w:after="{space_after}" w:line="264" w:lineRule="auto"/>'
    if indent:
        ppr += f'<w:ind w:left="{indent}"/>'
    ppr += "</w:pPr>"
    return f"<w:p>{ppr}{runs(text, italic=italic, color=color, size=size)}</w:p>"

def note_lines(n=3):
    """Renglones en blanco con línea inferior para escribir a mano o teclear."""
    return "".join(p("", space_after=200, border=True) for _ in range(n))

body = []
A = body.append

# ---------- Portada / cabecera ----------
A(p("Guion de reunión", style="Title", space_after=40))
A(p("Cátedra UNESCO de Educación Ambiental y Desarrollo Sostenible — UNED",
    style="Subtitle", space_after=40))
A(p("Janire Sánchez · agosto de 2026", italic=True, color="5F6F66", size="20",
    space_after=240, border=True))

# ---------- 1. Quién soy ----------
A(p("1. Quién soy", style="Heading1", space_before=240))
A(p("Ambientóloga (UAM, 2016-2021) y máster en Gestión del Turismo Sostenible "
    "(UPM, 2021-2023). Responsable de Educación y Sensibilización en Fundación "
    "Renovables."))
A(p("Diseño e imparto talleres en centros educativos. En el curso 2025/2026, el "
    "primero del programa, hemos realizado **diecisiete**. Los de Secundaria, FP "
    "y Bachillerato abordan la crisis climática desde la perspectiva de la "
    "**transición justa** —incluyendo pobreza energética y afectación desigual— "
    "e incorporan una dinámica propia de **verificación de información climática**."))
A(p("Publiqué como primera autora en Diversity (Q2, Biodiversity Conservation) un "
    "estudio sobre el impacto del ecoturismo en el comportamiento de Cebus "
    "imitator. Aquel trabajo concluía recomendando programas de educación "
    "ambiental con participación comunitaria: esta propuesta continúa esa línea "
    "desde el lado educativo."))
A(p("Llego por sugerencia de Rubén Díaz Sierra."))

# ---------- 2. La idea ----------
A(p("2. La idea, en una frase", style="Heading1", space_before=240))
A(p("¿Forma el currículo verde una conciencia verde?", style="Quote",
    space_after=120))
A(p("Qué nivel de alfabetización ecosocial —incluida la capacidad de detectar "
    "desinformación climática— presenta el alumnado de Secundaria, FP y "
    "Bachillerato, y en qué medida se explica por el tipo de currículo cursado "
    "y por el contexto territorial del centro."))
A(p("Diseño factorial 2×2: currículo (con o sin contenido ambiental) × "
    "territorio (rural o urbano). Cuestionario CAFTÁN adaptado, con un bloque "
    "nuevo sobre desinformación, más grupos de discusión."))

# ---------- 3. Los huecos ----------
A(p("3. Los tres huecos que ocupo", style="Heading1", space_before=240))
A(p("**Población.** El trabajo de la Cátedra se ha centrado en la formación "
    "inicial del profesorado. Hay mucha menos evidencia sobre el alumnado, y "
    "prácticamente ninguna sobre FP, pese a que los ciclos de renovables y "
    "eficiencia forman a quienes ejecutarán la transición.", bullet=True))
A(p("**Constructo.** El CAFTÁN mide conocimientos, actitudes y comportamientos, "
    "pero no la capacidad de discriminar desinformación climática. Cook, "
    "Lewandowsky y Ecker (2017) muestran que reconocer una técnica argumentativa "
    "engañosa funciona incluso sin aportar la información correcta: son "
    "capacidades distintas.", bullet=True))
A(p("**Método.** Su catálogo combina encuestas amplias, comparación entre "
    "territorios, trabajo conceptual y etnografía, pero no cuestionario más "
    "cualitativo en el mismo diseño.", bullet=True))

# ---------- 4. Lo que aporto ----------
A(p("4. Lo que aporto, y lo que no", style="Heading1", space_before=240))
A(p("Aporto", style="Heading2", space_before=120, space_after=60))
A(p("**Acceso directo al campo.** Los talleres son de diseño propio y los "
    "imparto yo. No dependo de que un centro me abra la puerta ni de que otro "
    "equipo me ceda datos.", bullet=True))
A(p("**Un prototipo de instrumento ya probado en aula.** La dinámica de "
    "verificación clasifica afirmaciones reales en cinco categorías —bulo, doble "
    "bulo, alerta, necesita contexto, verdad— entregando fuentes deliberadamente "
    "mezcladas. Mide destreza, no memoria.", bullet=True))
A(p("**Contenido ya alineado con su marco.** La transición justa es clima más "
    "equidad, empleo y territorio.", bullet=True))
A(p("**Un modelo de cuatro ejes de cosmovisión ecológica, y su encuesta.** "
    "Proyecto Ecomanía, con Álvaro Francisco Gil: yo desarrollo los ejes y los "
    "instrumentos, él el software. Ejes antropocéntrico/ecocéntrico, "
    "tecnológico/suficiencia, individual/colectivo y tecnocrático/de base, "
    "derivados del NEP, del Environmental Attitudes Inventory y de la teoría "
    "cultural del riesgo. Separa qué tipo de verde de cuánto verde — que es "
    "justo el riesgo de un 2×2 donde todo el alumnado salga moderadamente "
    "verde. Le falta validación factorial sobre datos reales.", bullet=True))

A(p("No prometo", style="Heading2", space_before=180, space_after=60))
A(p("**Muestra grande.** Diecisiete talleres no dan potencia estadística. El "
    "plan realista: validar el instrumento el primer año y acumular muestra en "
    "los siguientes.", bullet=True))
A(p("**Impacto sostenido.** Sesión única de hora y media: permite pre-post en la "
    "propia sesión, no efectos duraderos sin medición diferida.", bullet=True))
A(p("**Acceso rural confirmado.** Extender los talleres a Segovia y La Rioja es "
    "una vía que quiero abrir con mi organización. A día de hoy no está cerrada.",
    bullet=True))
A(p("**Datos de Ecomanía.** El producto no está construido: no hay encuesta "
    "implementada ni respuestas recogidas. Lo que llevo es el modelo y el diseño "
    "del instrumento. Además, el modelo asume usuarios ya concienciados que se "
    "autoseleccionan; el alumnado de un instituto no lo está.", bullet=True))

# ---------- 5. Preguntas ----------
A(p("5. Preguntas que llevo", style="Heading1", space_before=280))
A(p("Espacio para anotar sus respuestas durante la conversación.", italic=True,
    color="5F6F66", size="19", space_after=200))

preguntas = [
    ("¿Cuál es la vía de acceso al programa a día de hoy, y en qué plazos?",
     "Tengo entendido que la preinscripción 2026/2027 pudo cerrar en junio. "
     "Determina si el arranque es este curso o el siguiente.", 3),
    ("¿Tendría sentido dentro de algún proyecto en marcha de la Cátedra, o como "
     "tesis independiente?", None, 3),
    ("¿Ve viable compatibilizar la tesis con un trabajo a jornada completa?",
     "En qué régimen de dedicación, y con qué ritmo esperado.", 3),
    ("¿Conviene abarcar Secundaria, FP y Bachillerato, o concentrarse en FP?",
     "Mi criterio: no cerrar puertas, por la escala actual del programa. Pero el "
     "hueco de literatura es mayor en FP.", 3),
    ("¿La desinformación climática debe ser una dimensión dentro de la "
     "alfabetización ecosocial, o tiene entidad para vertebrar la tesis?", None, 3),
    ("¿Vería publicable una validación factorial del modelo de cuatro ejes?",
     "Artículo metodológico separable de la tesis. Le ofrezco algo, no solo "
     "pido. Hablarlo antes con Álvaro.", 3),
    ("¿Qué implicaciones éticas tendría pasar un instrumento de valores a "
     "menores en centros?",
     "Dato de categoría especial, consentimiento parental, comité de ética.", 3),
    ("¿Qué le falta a esta idea para ser una tesis?", None, 4),
]

for i, (q, sub, lines) in enumerate(preguntas, 1):
    A(p(f"{i}. {q}", style="Heading2", space_before=200, space_after=40))
    if sub:
        A(p(sub, italic=True, color="5F6F66", size="19", space_after=120))
    A(note_lines(lines))

# ---------- 6. Notas libres ----------
A(p("6. Otras notas", style="Heading1", space_before=280))
A(note_lines(8))

# ---------- 7. Después ----------
A(p("7. Después de la reunión", style="Heading1", space_before=240))
A(p("Escribir a Fundación Renovables: extensión de talleres a Segovia y La "
    "Rioja, y uso del material con fines de investigación.", bullet=True))
A(p("Hablar con Álvaro sobre la validación del modelo de ejes como artículo, y "
    "sobre coautoría.", bullet=True))
A(p("Agradecer a Rubén Díaz Sierra.", bullet=True))
A(p("Actualizar el brief del proyecto en el repositorio.", bullet=True))

document = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships" xmlns:xml="http://www.w3.org/XML/1998/namespace">
<w:body>{"".join(body)}
<w:sectPr><w:pgSz w:w="11906" w:h="16838"/>
<w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1418" w:header="708" w:footer="708" w:gutter="0"/>
</w:sectPr></w:body></w:document>'''

styles = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr>
<w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/>
<w:color w:val="1F2B25"/><w:sz w:val="21"/><w:szCs w:val="21"/>
<w:lang w:val="es-ES"/></w:rPr></w:rPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal">
<w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Title">
<w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:outlineLvl w:val="0"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:b/>
<w:color w:val="14201A"/><w:sz w:val="46"/><w:szCs w:val="46"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Subtitle">
<w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/>
<w:color w:val="2C6A4C"/><w:sz w:val="24"/><w:szCs w:val="24"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1">
<w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:pBdr><w:bottom w:val="single" w:sz="6" w:space="4" w:color="2C6A4C"/></w:pBdr>
<w:outlineLvl w:val="0"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:b/>
<w:color w:val="14201A"/><w:sz w:val="28"/><w:szCs w:val="28"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2">
<w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:outlineLvl w:val="1"/></w:pPr>
<w:rPr><w:b/><w:color w:val="14201A"/><w:sz w:val="23"/><w:szCs w:val="23"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote">
<w:name w:val="Quote"/><w:basedOn w:val="Normal"/><w:qFormat/>
<w:pPr><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="2C6A4C"/></w:pBdr>
<w:ind w:left="284"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Cambria" w:hAnsi="Cambria"/><w:i/>
<w:color w:val="14201A"/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style>
<w:style w:type="numbering" w:styleId="NoList"><w:name w:val="No List"/></w:style>
</w:styles>'''

numbering = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:abstractNum w:abstractNumId="0">
<w:nsid w:val="1A2B3C4D"/><w:multiLevelType w:val="hybridMultilevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/>
<w:lvlText w:val="&#8226;"/><w:lvlJc w:val="left"/>
<w:pPr><w:ind w:left="426" w:hanging="284"/></w:pPr>
<w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:hint="default"/>
<w:color w:val="2C6A4C"/></w:rPr></w:lvl>
</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''

settings = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:settings xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:zoom w:percent="100"/><w:defaultTabStop w:val="708"/>
<w:themeFontLang w:val="es-ES"/>
</w:settings>'''

core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
<dc:title>Guion de reunion - Catedra UNESCO EADS UNED</dc:title>
<dc:creator>Janire Sanchez</dc:creator>
<cp:lastModifiedBy>Janire Sanchez</cp:lastModifiedBy>
<dcterms:created xsi:type="dcterms:W3CDTF">2026-08-23T00:00:00Z</dcterms:created>
<dcterms:modified xsi:type="dcterms:W3CDTF">2026-08-23T00:00:00Z</dcterms:modified>
</cp:coreProperties>'''

app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
<Application>Microsoft Office Word</Application>
</Properties>'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>
<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>'''

rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>'''

doc_rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
<Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/>
</Relationships>'''

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("[Content_Types].xml", content_types)
    z.writestr("_rels/.rels", rels)
    z.writestr("word/document.xml", document)
    z.writestr("word/styles.xml", styles)
    z.writestr("word/numbering.xml", numbering)
    z.writestr("word/settings.xml", settings)
    z.writestr("docProps/core.xml", core)
    z.writestr("docProps/app.xml", app)
    z.writestr("word/_rels/document.xml.rels", doc_rels)

print("escrito:", OUT, os.path.getsize(OUT), "bytes")
