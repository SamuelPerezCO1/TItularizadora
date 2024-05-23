import os
from datetime import datetime
import logging
import logging.config
from pdf2docx import Converter

fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')

"""
agregar una ruta con un archivo json para estas dos rutas
"""

# Define las rutas de las carpetas
# input_folder = 'C:\\Codigos\\prueba\\pdfs'
# output_folder = 'C:\\Codigos\\prueba\\word'

# Asegúrate de que la carpeta de salida existe
def pdfaword(input_folder , output_folder):
    logger.info("(pdfaword) pdfaword ingreso en la funcion")
    try:
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Itera sobre los archivos en la carpeta de entrada
        for filename in os.listdir(input_folder):
            # Verifica que el archivo tiene la extensión .pdf
            if filename.endswith('.pdf'):
                # Define las rutas de los archivos de entrada y salida
                pdf_file = os.path.join(input_folder, filename)
                docx_file = os.path.join(output_folder, filename.replace('.pdf', '.docx'))
                
                # Crea un objeto Converter
                cv = Converter(pdf_file)
                
                # Realiza la conversión
                cv.convert(docx_file, start=0, end=None)  # Convertir todas las páginas
                
                # Finaliza la conversión y cierra el objeto Converter
                cv.close()

        logger.info("(pdfaword) Conversión completa.")
    except Exception as e:
        logger.error(f"(pdfaword) pdfaword error Exception {e}")
