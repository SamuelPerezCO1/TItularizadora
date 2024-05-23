from datetime import datetime
import logging.config
import pandas as pd
import logging
import fitz
import os


fecha_actual = datetime.now()
mes_actual = fecha_actual.month
dia_actual = fecha_actual.day
anno_actual = fecha_actual.year

nombre_carpeta = f"{anno_actual}{mes_actual:02d}{dia_actual}"

nombre_archivo_log = f"logs/{nombre_carpeta}"
logging.config.fileConfig('logging.conf', defaults={'filename':nombre_archivo_log})
logger = logging.getLogger('TITULARIZADORA')
 
def extraer_informacion_debajo_tips(archivo_pdf):

    logger.info("(extraccion_tips) ingreso extraer_informaccion_debajo_tips")

    try:
        informacion_debajo_tips = []
    
        documento = fitz.open(archivo_pdf)
    
        for pagina_numero in range(len(documento)):
            pagina = documento.load_page(pagina_numero)
            
            palabras_tips = pagina.search_for("Saldos y cobertura _______________________________________")
    
            for palabra_tips in palabras_tips:
                x0, y0, x1, y1 = palabra_tips
                
                area_debajo_tips = fitz.Rect(x0, y1, x1 + -150, y1 + 55)
    
                texto_debajo_tips = pagina.get_text("text", clip=area_debajo_tips)
                informacion_debajo_tips.append(texto_debajo_tips)

            lista_info = []
            
            for info in informacion_debajo_tips:
                info_lines = info.strip().splitlines()
                info_stripped = [line.strip() for line in info_lines if line.strip()]
                

                lista_info.extend(info_stripped)
            
            patrones_excluir = ["Tasa", "%", "Prepago______", "1" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "0" , "Prepago" , "$" , "Saldo" ]
            
            tips_filtrados = []
            for elemento in lista_info:
                if any(elemento.startswith(patron) for patron in patrones_excluir):
                    continue
                tips_filtrados.append(elemento)

            nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
            archivo_csv = f"{nombre_base}.csv"

            titulo = tips_filtrados[0]


            tips_filtrados.pop(0)

            df_nuevo = pd.DataFrame({titulo:tips_filtrados})
            if os.path.exists(archivo_csv):
                df_existente = pd.read_csv(archivo_csv)
                df_actualizado = pd.concat([df_existente , df_nuevo] , axis=1)
            else:
                df_actualizado = df_nuevo

            df_actualizado.to_csv(archivo_csv,index=False)
    except Exception as e:
        logger.error(f"(extraer_informacion_debajo_tips) Error Exception {e}")
