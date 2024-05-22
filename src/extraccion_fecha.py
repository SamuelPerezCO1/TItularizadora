import fitz
import os
import pandas as pd

def extraer_fecha(archivo_pdf):
    fecha = []

    documento = fitz.open(archivo_pdf)

    for pagina_numero in range(len(documento)):
        pagina = documento.load_page(pagina_numero)
        
        x0 = 360
        x1 = 470
        y0 = 20
        y1 = 80
            
        area_fecha = fitz.Rect(x0, y0, x1, y1)
        texto_fecha = pagina.get_text("text", clip=area_fecha)
        fecha.append(texto_fecha)

    lista_info = []
    for info in fecha:
        info_lines = info.strip().splitlines()
        info_stripped = [line.strip() for line in info_lines if line.strip()]
        lista_info.extend(info_stripped)

    nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
    archivo_csv = f"{nombre_base}.csv"

    df_nuevo = pd.DataFrame({'Fecha': lista_info})

    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        df_actualizado = pd.concat([df_existente, df_nuevo], axis=1)
    else:
        df_actualizado = df_nuevo

    df_actualizado.to_csv(archivo_csv, index=False)
