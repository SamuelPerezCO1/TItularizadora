import time
import extraccion_titulo
import extraccion_fecha
import extraccion_saldoymora
import extraccion_tips
import extraccion_actual
import extraccion_porcentajes
import extraccion_escenarios_estres

archivos_pdf = ["C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostilpesosl4mar202.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn5mar20.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn7mar20.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn13mar2.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn14mar2.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn15feb2.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn16mar2.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn17mar2.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn18.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn19mar2.pdf" ,
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipspesosn20mar2.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipsu2mar2024.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipsu3mar2024.pdf" ,"C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostipsu4mar2024_0.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostispesosh1ma.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostispesosh2mar202.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostivv4mar2024.pdf" , "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostivv5mar2024.pdf",
                "C:\\Codigos\\Titularizadora\\pdfs\\riesgosubordinadostilpesosl3may2023.pdf"]

for archivo_pdf in archivos_pdf:
    extraccion_fecha.extraer_fecha(archivo_pdf)
    extraccion_titulo.extraer_titulo(archivo_pdf)
    extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
    extraccion_actual.extraer_actual(archivo_pdf)
    extraccion_porcentajes.extraer_porcentajes(archivo_pdf)
    extraccion_saldoymora.extraer_saldoymora(archivo_pdf)
    extraccion_escenarios_estres.extract_and_process_info(archivo_pdf)



# archivo_pdf = "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostilpesosl4mar202.pdf"

# extraccion_fecha.extraer_fecha(archivo_pdf)
# extraccion_titulo.extraer_titulo(archivo_pdf)
# extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
# extraccion_actual.extraer_actual(archivo_pdf)
# extraccion_porcentajes.extraer_porcentajes(archivo_pdf)