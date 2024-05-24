"""
Este script procesa una serie de archivos PDF para extraer información específica y realizar varias transformaciones, 
como la conversión de PDF a Word, la conversión de Word a texto y la conversión de texto a CSV. Finalmente, elimina los archivos intermedios.
El script utiliza módulos como `pdfaword`, `saldoymora`, `txtacsv`, `extraccion_fecha`, `extraccion_titulo`, `extraccion_tips`, `extraccion_actual`,
 `extraccion_porcentajes`, `extraccion_saldoymora` y `extraccion_escenarios_estres` para llevar a cabo sus funciones.
"""
import extraccion_escenarios_estres
from datetime import datetime
import extraccion_porcentajes
import extraccion_saldoymora
import extraccion_titulo
import extraccion_actual
import extraccion_fecha
import extraccion_tips
import logging.config
import saldoymora
import pdfaword
import logging
import carpeta
import txtacsv
import time
import os
#libreias necesarias para el funcionamiento del codigo

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

carpeta_pdfs = 'C:\\Codigos\\Titularizadora\\pdfs'
carpeta_word = 'C:\\Codigos\\Titularizadora\\word'
carpeta_txt = 'C:\\Codigos\\Titularizadora\\txt'
carpeta_principal = os.path.abspath(os.path.join(carpeta_txt, os.pardir))

pdfaword.pdfaword(carpeta_pdfs , carpeta_word)
saldoymora.convertir_pdf_a_txt(output_directory=carpeta_txt , input_directory=carpeta_word)
txtacsv.convertir_txt_a_csv(ruta_txt=carpeta_txt , ruta_principal=carpeta_principal)
time.sleep(5)

for archivo_pdf in archivos_pdf:
    logger.info(f"procesando archivo {archivo_pdf}")
    extraccion_fecha.extraer_fecha(archivo_pdf)
    extraccion_titulo.extraer_titulo(archivo_pdf)
    extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
    extraccion_actual.extraer_actual(archivo_pdf)
    extraccion_porcentajes.extraer_porcentajes(archivo_pdf)
    extraccion_saldoymora.extraer_saldoymora(archivo_pdf)
    extraccion_escenarios_estres.extract_and_process_info(archivo_pdf)
    time.sleep(1)

time.sleep(5)

carpeta.eliminar_elementos_en_carpeta(carpeta_word)
time.sleep(2)
carpeta.eliminar_elementos_en_carpeta(carpeta_txt)


# archivo_pdf = "C:\\Codigos\\Titularizadora\\pdfs\\riesgocreditossubordinadostilpesosl4mar202.pdf"

# extraccion_fecha.extraer_fecha(archivo_pdf)
# extraccion_titulo.extraer_titulo(archivo_pdf)
# extraccion_tips.extraer_informacion_debajo_tips(archivo_pdf)
# extraccion_actual.extraer_actual(archivo_pdf)
# extraccion_porcentajes.extraer_porcentajes(archivo_pdf)