import pandas as pd
import fitz
import os

def extraer_actual(archivo_pdf):
    actual = []

    documento = fitz.open(archivo_pdf)

    for pagina_numero in range(len(documento)):
        pagina = documento.load_page(pagina_numero)
        
        palabras_actual = pagina.search_for("Actual")

        for palabra_actual in palabras_actual:
            x0, y0, x1, y1 = palabra_actual
            
            area_debajo_actual = fitz.Rect(x0 - 10, y1, x1 + 35, y1 + 55)

            texto_debajo_actual = pagina.get_text("text", clip=area_debajo_actual)
            actual.append(texto_debajo_actual)

        lista_info = []
        
        for info in actual:
            info_lines = info.strip().splitlines()
            info_stripped = [line.strip() for line in info_lines if line.strip()]

            lista_info.extend(info_stripped)
        
        porcentajes = [f"{i / 10:.1f}%" for i in range(10, 1001)]

        patrones_excluir = ["_", "P", "L", "a", "Escenario", "valoración", 'Actual',
                            "enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre",
                            ".", "p", "i", "ó", "Inicial", "Participación", "n", "l", "tal", "era", "t", "c", "o", "m", "s", "E", "v", 'A', 'B', 'C', 'A1', 'A2', 'A3',
                            'B1', 'B2', 'B3', 'C1', 'C2', 'C3', 'MZ', 'T', 'S', 'd', 'i', 'c', 'e', 'é', 'h', 'r', 'c', 'Ãº', 'ú', ' ', 'E', 'u', ':' ,'0.0%']

        patrones_excluir.extend(porcentajes)

        actual_filtrados = []
        for elemento in lista_info:
            if any(elemento.startswith(patron) for patron in patrones_excluir):
                continue

            if len(elemento) > 4 or '-' in elemento:
                actual_filtrados.append(elemento)

        nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
        archivo_csv = f"{nombre_base}.csv"

        df_nuevo = pd.DataFrame({'Actual': actual_filtrados})
        if os.path.exists(archivo_csv):
            df_existente = pd.read_csv(archivo_csv)
            df_actualizado = pd.concat([df_existente, df_nuevo], axis=1)
        else:
            df_actualizado = df_nuevo

        df_actualizado.to_csv(archivo_csv, index=False)

