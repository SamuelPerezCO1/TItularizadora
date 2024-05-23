import os
import pandas as pd


# Función para convertir txt a csv
def convertir_txt_a_csv(ruta_txt, ruta_principal):
    # Iterar sobre todos los archivos en la ruta especificada
    print("ENTREEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE")
    print(ruta_txt , ruta_principal)
    for archivo_txt in os.listdir(ruta_txt):
        if archivo_txt.endswith(".txt"):
            ruta_archivo_txt = os.path.join(ruta_txt, archivo_txt)
            
            # Leer el contenido del archivo txt
            with open(ruta_archivo_txt, 'r') as file:
                contenido = file.read().splitlines()
            
            # Crear DataFrame con el contenido del txt
            df_nuevo = pd.DataFrame({"Saldoymora": contenido})
            
            # Obtener el nombre base del archivo sin extensión
            nombre_base = os.path.splitext(os.path.basename(ruta_archivo_txt))[0]
            archivo_csv = os.path.join(ruta_principal, f"{nombre_base}.csv")
            
            # Verificar si el archivo CSV ya existe
            if os.path.exists(archivo_csv):
                # Leer el CSV existente
                df_existente = pd.read_csv(archivo_csv)
                # Concatenar las nuevas filas a las existentes
                df_actualizado = pd.concat([df_existente, df_nuevo], axis=1)
            else:
                # Si no existe, el DataFrame actualizado es el nuevo DataFrame
                df_actualizado = df_nuevo
            
            # Guardar el DataFrame actualizado en el archivo CSV
            df_actualizado.to_csv(archivo_csv, index=False, encoding='utf-8')
