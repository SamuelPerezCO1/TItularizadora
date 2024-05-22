import fitz
import os
import pandas as pd

def extraer_titulo(archivo_pdf):
    titulo = []
 
    documento = fitz.open(archivo_pdf)
 
    for pagina_numero in range(len(documento)):
        pagina = documento.load_page(pagina_numero)
        
        titulos = pagina.search_for("Informe de Riesgo")
 
        for palabra_titulo in titulos:
            x0, y0, x1, y1 = palabra_titulo
            
            area_debajo_titulo = fitz.Rect(x0, y1, x1 + 150, y1 + 20)
            
            texto_debajo_titulo = pagina.get_text("text", clip=area_debajo_titulo)
            titulo.append(texto_debajo_titulo)
 
        lista_info = []
        for info in titulo:
            info_lines = info.strip().splitlines()
            info_stripped = [line.strip().replace("__", "") for line in info_lines if line.strip()]
            lista_info.extend(info_stripped)

        nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
        archivo_csv = f"{nombre_base}.csv"

        # Convertir lista_info en un DataFrame de pandas
        df_nuevo = pd.DataFrame({"Titulos":lista_info})

        if os.path.exists(archivo_csv):
            df_existente = pd.read_csv(archivo_csv)
            df_actualizado = pd.concat([df_existente , df_nuevo] , axis = 1)
        else:
            df_actualizado = df_nuevo

        df_actualizado.to_csv(archivo_csv , index=False)
