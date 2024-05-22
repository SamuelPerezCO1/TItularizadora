import pandas as pd
import fitz
import os

def extraer_porcentajes(archivo_pdf):
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
