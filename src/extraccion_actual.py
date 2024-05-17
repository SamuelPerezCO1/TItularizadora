import pandas as pd
import fitz
import os

def extraer_actual(archivo_pdf):
    actual = []

    documento = fitz.open(archivo_pdf)

    for pagina_numero in range(len(documento)):
        pagina = documento.load_page(pagina_numero)

        x0 = 197
        x1 = 250
        y0 = 100
        y1 = 210

        area_debajo_actual = fitz.Rect(x0, y0, x1 ,y1 )

        texto_actual = pagina.get_text("text", clip=area_debajo_actual)
        actual.append(texto_actual)

        contador = 0
        lista_info = []

        for info in actual:
            contador += 1
            info_lines = info.strip().splitlines()
            info_stripped = [line.strip() for line in info_lines if line.strip()]


            lista_info.extend(info_stripped)

        print(lista_info)

        patrones_excluir = ["_","P","L","a","Escenario","valoración",'Actual','-',
                            "enero","febrero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre",
                            ".","p","i","ó","Inicial","Participación","n","l","tal","era","t","c","o","m","s","E","v"]

        actual_filtrados = []
        for elemento in lista_info:
            if any(elemento.startswith(patron) for patron in patrones_excluir) or elemento.endswith('%'):
                continue
            actual_filtrados.append(elemento)
            print(elemento)

        nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
        archivo_csv = f"{nombre_base}.csv"

        df_nuevo = pd.DataFrame({"Actual":actual_filtrados})

        if os.path.exists(archivo_csv):
            df_existente = pd.read_csv(archivo_csv)
            df_actualizado = pd.concat([df_existente , df_nuevo] , axis = 1)
        else:
            df_actualizado = df_nuevo

        df_actualizado.to_csv(archivo_csv,index=False)

        print(f"Informacion Guardad en {archivo_csv}")