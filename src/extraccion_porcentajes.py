from datetime import datetime
import logging.config
import pandas as pd
import logging
import fitz
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

def extraer_porcentajes(archivo_pdf):

    """
    Extrae los porcentajes de cobertura de un archivo PDF y los guarda en un archivo CSV.

    Esta función lee un archivo PDF y busca un área específica en cada página para extraer los porcentajes de cobertura.
    Luego, guarda los porcentajes extraídos en un archivo CSV con el mismo nombre que el archivo PDF.

    Args:
        archivo_pdf (str): Ruta del archivo PDF del cual se extraerán los porcentajes de cobertura.

    Returns:
        None

    Raises:
        Exception: Si ocurre un error durante la extracción o la escritura del archivo CSV.
    """

    logger.info("(extraccion_porcentajes) extraer_porcentajes ingreso")
        
    try:
        porcentajes = []

        documento = fitz.open(archivo_pdf)

        for pagina_numero in range(len(documento)):
            pagina = documento.load_page(pagina_numero)

            x0 = 370
            x1 = 550
            y0 = 117
            y1 = 180

            area_debajo_tips = fitz.Rect(x0, y0, x1 ,y1)

            texto_debajo_tips = pagina.get_text("text", clip=area_debajo_tips)
            porcentajes.append(texto_debajo_tips)

        contador = 0
        lista_info = []

        for info in porcentajes:
            contador += 1
            info_lines = info.strip().splitlines()
            info_stripped = [line.strip() for line in info_lines if line.strip()]

            lista_info.extend(info_stripped)

        patrones_excluir = ["MZ", "B", "A", "C", "T", "+", "_", "$", "Z", "o", "E", "l", "d", "ió", 'g', 'a', 'V', 'A', 'A +', 'A1',
                            'A2', 'A3', 'B1', 'B2', 'B3', 'B', 'C', 'C1', 'C2', 'C3', 'MZ', '+', '2 + B', '1 +']

        lista_filtrada = []
        for elemento in lista_info:
            if any(elemento.startswith(patron) for patron in patrones_excluir):
                continue
            if elemento.endswith('%'):
                lista_filtrada.append(elemento)

        nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
        archivo_csv = f"{nombre_base}.csv"

        df_nuevo = pd.DataFrame({"Cobertura V": lista_filtrada})

        if os.path.exists(archivo_csv):
            df_existente = pd.read_csv(archivo_csv)
            df_actualizado = pd.concat([df_existente, df_nuevo], axis=1)
        else:
            df_actualizado = df_nuevo

        df_actualizado.to_csv(archivo_csv, index=False)

        logger.info("(extraccion_porcentajes) extraer_porcentajes completado")

    except Exception as e:
        logger.error(f"(extraccion_porcentajes) extraer_porcentajes Error Exception {e}")
