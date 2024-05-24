from datetime import datetime
import logging.config
import logging
import fitz
import os
#librerias necesarias para el funcionamiento del codigo

fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename': nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')
#Configuracion de los loggers

def extraer_saldoymora(archivo_pdf):

    """
    Extrae información relacionada con saldo y mora de un archivo PDF y guarda las imágenes asociadas en una carpeta.

    Esta función lee un archivo PDF y busca un área específica en cada página para extraer información relacionada con saldo y mora.
    Además de extraer el texto, guarda imágenes de esta información en una carpeta 'saldo y mora'.

    Args:
        archivo_pdf (str): Ruta del archivo PDF del cual se extraerá la información de saldo y mora.

    Returns:
        None

    Raises:
        Exception: Si ocurre un error durante la extracción o el almacenamiento de la información.
    """
    
    logger.info("(extraccion_saldoymora) extraer_saldoymora ingreso")
    
    try:
        carpeta_imagenes = "saldo y mora"
        if not os.path.exists(carpeta_imagenes):
            os.makedirs(carpeta_imagenes)

        documento = fitz.open(archivo_pdf)

        for pagina_numero in range(len(documento)):
            pagina = documento.load_page(pagina_numero)
            
            x0 = 360
            x1 = 500
            y0 = 70
            y1 = 120
            area_saldoymora = fitz.Rect(x0, y0, x1, y1)
            
            texto_saldoymora = pagina.get_text("text", clip=area_saldoymora)
            
            pix = pagina.get_pixmap(clip=area_saldoymora, dpi=300)
            nombre_imagen = f"{os.path.splitext(os.path.basename(archivo_pdf))[0]}.png"
            ruta_imagen = os.path.join(carpeta_imagenes, nombre_imagen)
            pix.save(ruta_imagen)

        logger.info("(extraccion_saldoymora) extraer_saldoymora completado")

    except Exception as e:
        logger.error(f"(extraer_saldoymora) error Exception {e}")