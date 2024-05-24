from datetime import datetime
import logging.config
import pandas as pd
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

def convertir_txt_a_csv(ruta_txt, ruta_principal):

    """
    Convierte archivos de texto TXT a archivos CSV.

    Esta función toma una ruta de carpeta que contiene archivos de texto TXT y los convierte en archivos CSV.
    Cada archivo de texto se convierte en un DataFrame de pandas y luego se guarda como un archivo CSV en una
    carpeta principal especificada.

    Args:
        ruta_txt (str): Ruta de la carpeta que contiene los archivos de texto TXT a convertir.
        ruta_principal (str): Ruta de la carpeta principal donde se guardarán los archivos CSV convertidos.

    Returns:
        None
    """

    logger.info("(txtacsv) convertir_txt_a_csv ingreso")

    try:
        for archivo_txt in os.listdir(ruta_txt):
            if archivo_txt.endswith(".txt"):
                ruta_archivo_txt = os.path.join(ruta_txt, archivo_txt)
                

                with open(ruta_archivo_txt, 'r') as file:
                    contenido = file.read().splitlines()
                

                df_nuevo = pd.DataFrame({"Saldoymora": contenido})
                

                nombre_base = os.path.splitext(os.path.basename(ruta_archivo_txt))[0]
                archivo_csv = os.path.join(ruta_principal, f"{nombre_base}.csv")
                

                if os.path.exists(archivo_csv):

                    df_existente = pd.read_csv(archivo_csv)

                    df_actualizado = pd.concat([df_existente, df_nuevo], axis=1)
                else:

                    df_actualizado = df_nuevo
                

                df_actualizado.to_csv(archivo_csv, index=False, encoding='utf-8')

        logger.info("(txtacsv) convertir_txt_a_csv completado")

    except Exception as e:
        logger.error(f"(txtacsv) convertir_txt_a_csv error Exception {e}")