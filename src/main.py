import time
import extraccion_titulo
import extraccion_fecha
import extraccion_saldoymora
import extraccion_tips
import extraccion_actual
import extraccion_porcentajes
import extraccion_escenarios_estres

import pdfaword
import saldoymora
import txtacsv

from datetime import datetime
import logging
import logging.config
import os

fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')

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

input_folder = 'C:\\Codigos\\Titularizadora\\pdfs'
output_folder = 'C:\\Codigos\\Titularizadora\\word'
output_directory = 'C:\\Codigos\\Titularizadora\\txt'
ruta_principal = os.path.abspath(os.path.join(output_directory, os.pardir))

# pdfaword.pdfaword(input_folder , output_folder)
saldoymora.funcionx(output_directory=output_directory , input_directory=output_folder)
txtacsv.convertir_txt_a_csv(ruta_txt=output_directory , ruta_principal=ruta_principal)
time.sleep(5)

for archivo_pdf in archivos_pdf:
    logger.info(f"procesando archivo {archivo_pdf}")
    extraccion_fecha.extraer_fecha(archivo_pdf)
    extraccion_titulo.extraer_titulo(archivo_pdf)
    extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
    extraccion_actual.extraer_actual(archivo_pdf)
    extraccion_porcentajes.extraer_porcentajes(archivo_pdf)
    # extraccion_saldoymora.extraer_saldoymora(archivo_pdf)
    extraccion_escenarios_estres.extract_and_process_info(archivo_pdf)
    time.sleep(1)

# archivo_pdf = "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostilpesosl4mar202.pdf"

# extraccion_fecha.extraer_fecha(archivo_pdf)
# extraccion_titulo.extraer_titulo(archivo_pdf)
# extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
# extraccion_actual.extraer_actual(archivo_pdf)
# extraccion_porcentajes.extraer_porcentajes(archivo_pdf)