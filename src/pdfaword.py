from pdf2docx import Converter
from datetime import datetime
import logging.config
import logging
import os
#Librerias necesarias para el funcionamiento del codigo

fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')
#Configuracion de los loggers

def pdfaword(input_folder , output_folder):
    """
    Convierte archivos PDF a DOCX.

    Esta función convierte todos los archivos PDF en una carpeta de entrada especificada a formato DOCX 
    y guarda los archivos convertidos en una carpeta de salida especificada.

    Args:
        input_folder (str): La ruta a la carpeta que contiene los archivos PDF.
        output_folder (str): La ruta a la carpeta donde se guardarán los archivos DOCX convertidos.

    Returns:
        None

    Raises:
        Exception: Si ocurre un error durante la conversión.
    """
    logger.info("(pdfaword) pdfaword ingreso en la funcion")
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        for filename in os.listdir(input_folder):
            if filename.endswith('.pdf'):
                pdf_file = os.path.join(input_folder, filename)
                docx_file = os.path.join(output_folder, filename.replace('.pdf', '.docx'))

                cv = Converter(pdf_file)

                cv.convert(docx_file, start=0, end=None)  
                
                cv.close()

        logger.info("(pdfaword) Conversión completa.")
    except Exception as e:
        logger.error(f"(pdfaword) pdfaword error Exception {e}")
