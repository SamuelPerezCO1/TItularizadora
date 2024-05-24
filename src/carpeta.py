from datetime import datetime
import logging.config
import logging
import shutil
import os
#Librerias necesarios para el funcionamiento del codigo

fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')

#Configuracion para los loggers

def eliminar_elementos_en_carpeta(ruta_carpeta):
    """
    Elimina todos los elementos dentro de una carpeta.

    Esta función elimina recursivamente todos los archivos y carpetas dentro de la ruta especificada.
    Si la ruta especificada no existe o no es una carpeta, no se realiza ninguna operación.

    Args:
        ruta_carpeta (str): Ruta de la carpeta de la cual se eliminarán todos los elementos.

    Returns:
        None
    """
    logger.info("(carpeta) eliminar_elementos_en_carpeta ingreso")
    try:
        if os.path.isdir(ruta_carpeta):
            for elemento in os.listdir(ruta_carpeta):
                ruta_elemento = os.path.join(ruta_carpeta, elemento)
                if os.path.isfile(ruta_elemento) or os.path.islink(ruta_elemento):
                    os.unlink(ruta_elemento)
                elif os.path.isdir(ruta_elemento):
                    shutil.rmtree(ruta_elemento)
        logger.info("(carpeta) eliminar_elementos_en_carpeta completado")
    except Exception as e:
        logger.error(f"(carpeta) eliminar_elementos_en_carpeta error Exception {e}")