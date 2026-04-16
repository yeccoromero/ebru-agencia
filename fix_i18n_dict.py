import re

with open("assets/js/i18n.js", "r") as file:
    content = file.read()

# English inserts
en_inserts = """        "project.services": "Services",
        "project.year": "Year",
        "project.next": "NEXT<br>PROJECT.",
        "catleya.desc2": "We want every visit to Cattleya to be an invitation to discover, enjoy, and return, guided by its fundamental pillars: <strong>Quality, Freshness, Connection, and Experience.</strong>",
        "vixmed.desc2": "The brand needed a clear and simple identifier reflecting its values: <strong>professionalism, technological vanguard, quality, and trust.</strong> The goal was to build a highly recognizable and memorable identity in the health sector.", """
content = content.replace('"project.services": "Services"', en_inserts)

# Spanish inserts
es_inserts = """        "project.services": "Servicios",
        "project.year": "Año",
        "project.next": "SIGUIENTE<br>PROYECTO.",
        "catleya.desc2": "Queremos que cada visita a Cattleya sea una invitación a descubrir, a disfrutar y a volver, guiándonos por sus pilares fundamentales: <strong>Calidad, Frescura, Conexión y Experiencia.</strong>",
        "vixmed.desc2": "La marca necesitaba un identificador claro y simple que reflejara sus valores: <strong>profesionalismo, vanguardia tecnológica, calidad y confianza.</strong> El objetivo fue construir una identidad altamente reconocible y memorable en el sector de la salud.", """
content = content.replace('"project.services": "Servicios"', es_inserts)

with open("assets/js/i18n.js", "w") as file:
    file.write(content)
