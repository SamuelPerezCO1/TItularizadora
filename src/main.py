import extraccion_titulo
import extraccion_fecha
"""
Aca debe de ir el import para extrar el 
saldo y mora
"""
import extraccion_tips
import extraccion_actual
import extraccion_porcentajes
"""
Aca debe de estar el import para el archivo de
escenarios de estres
"""

archivo_pdf = "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostilpesosl4mar202.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn5mar20.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn7mar20.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn13mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn14mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn15feb2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn16mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn17mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn18.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn19mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipspesosn20mar2.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipsu2mar2024.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipsu3mar2024.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostipsu4mar2024_0.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostispesosh1ma.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostispesosh2mar202.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostivv4mar2024.pdf"
# archivo_pdf = "../pdf/riesgocreditossubordinadostivv5mar2024.pdf"
# archivo_pdf = "../pdf/riesgosubordinadostilpesosl3may2023.pdf"

extraccion_fecha.extraer_fecha(archivo_pdf)
extraccion_titulo.extraer_titulo(archivo_pdf)
extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
extraccion_actual.extraer_actual(archivo_pdf)
extraccion_porcentajes.extraer_porcentajes(archivo_pdf)