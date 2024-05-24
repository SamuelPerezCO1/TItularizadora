from datetime import datetime
from PyPDF2 import PdfReader
import logging.config
import pandas as pd
import logging
import re
import os
#Librerias necesarias para el funcionamineto del codigo


fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')
#Configuracion de los loggers

def extract_and_process_info(archivo_pdf):

    """
    Extrae y procesa la información de los escenarios de estrés de un archivo PDF y la guarda en un archivo CSV.

    Esta función lee un archivo PDF y busca la sección 'Escenarios de Estrés' seguida de un conjunto de líneas.
    Extrae el texto entre esta sección y la palabra 'Tasa', lo procesa y lo guarda en un archivo CSV.

    Args:
        archivo_pdf (str): Ruta del archivo PDF del cual se extraerá y procesará la información de los escenarios de estrés.

    Returns:
        str: Mensaje indicando si se encontró o no la información de los escenarios de estrés.

    Raises:
        Exception: Si ocurre un error durante la extracción, el procesamiento o la escritura del archivo CSV.
    """
        
    logger.info("(extraccion_escenarios_estres) extract_and_procces_info ingreso")

    try:
        with open(archivo_pdf, 'rb') as file:
            reader = PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()

        pattern = r'Escenarios de Estrés\s*_{5,}\s*(.*?)\s*Tasa'
        match = re.search(pattern, text, re.DOTALL)
        if match:
            extracted_text = match.group(1).strip()
        else:
            return "No se encontró la información entre Escenarios de Estrés y Tasa"
        
        lines = extracted_text.split('\n')
        lines = [line for line in lines if line.strip()]
        
        data = []
        for line in lines:
            parts = line.split()
            if all(part is not None for part in parts):
                data.append([" ".join(parts)]) 
        
        df = pd.DataFrame(data, columns=["Escenarios Estres"])
        
        nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
        archivo_csv = f"{nombre_base}.csv"
        
        if os.path.exists(archivo_csv):
            df_existente = pd.read_csv(archivo_csv)
            df_actualizado = pd.concat([df_existente, df], axis=1)
        else:
            df_actualizado = df

        df_actualizado.to_csv(archivo_csv, index=False)

        logger.info("(extraccion_escenarios_estres) extract_and_process_info completado")

    except Exception as e:
        logger.error(f"(extraccion_escenarios_estres) extract_and_process_info error Exception {e}")