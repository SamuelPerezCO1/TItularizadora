from datetime import datetime
import logging.config
import docx2txt
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

def process_and_extract_text(file_name, output_file_name):

    """
    Convierte archivos DOCX a archivos de texto TXT.

    Esta función toma una carpeta de entrada que contiene archivos DOCX y extrae el texto de cada archivo, filtrando
    solo las líneas relevantes que contienen información sobre tasas y períodos de tiempo. Luego, guarda el texto extraído
    en archivos de texto TXT en una carpeta de salida especificada.

    Args:
        output_directory (str): Ruta de la carpeta donde se guardarán los archivos de texto TXT.
        input_directory (str): Ruta de la carpeta que contiene los archivos DOCX de entrada.

    Returns:
        None
    """


    text = docx2txt.process(file_name)
    lines = text.splitlines()

    start_printing = False
    stop_printing = False
    extracted_lines = []

    for line in lines:
 
        if line.strip() and '_' not in line:
            if 'tasa' in line.lower():
                stop_printing = True
            if start_printing and not stop_printing:
                extracted_lines.append(line)
            if 'meses' in line.lower():
                start_printing = True


    with open(output_file_name, 'w', encoding='utf-8') as f:
        for line in extracted_lines:
            f.write(line + '\n')


def convertir_pdf_a_txt(output_directory , input_directory):
    os.makedirs(output_directory, exist_ok=True)

    files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.docx')]

    for file in files:
        base_name = os.path.splitext(os.path.basename(file))[0]
        output_file = os.path.join(output_directory, base_name + '.txt')
        process_and_extract_text(file_name=file,output_file_name= output_file)