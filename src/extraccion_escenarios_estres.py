from PyPDF2 import PdfReader
import pandas as pd
import re
import os

def extract_and_process_info(archivo_pdf):
    # Abre el archivo PDF y extrae el texto
    with open(archivo_pdf, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    # Define la expresión regular para buscar el texto entre "Escenarios de Estrés" y "Tasa"
    pattern = r'Escenarios de Estrés\s*_{5,}\s*(.*?)\s*Tasa'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        extracted_text = match.group(1).strip()
    else:
        return "No se encontró la información entre Escenarios de Estrés y Tasa"
    
    # Procesa el texto extraído a DataFrame
    lines = extracted_text.split('\n')
    lines = [line for line in lines if line.strip()]
    
    # Filtrar líneas vacías o con None después del split
    data = []
    for line in lines:
        parts = line.split()
        if all(part is not None for part in parts):
            data.append([" ".join(parts)])  # Ensure each sublist has exactly one element
    
    # Crear DataFrame con las filas de datos
    df = pd.DataFrame(data, columns=["Escenarios Estres"])  # Specify one column
    
    # Asegurar que el nombre del archivo base no tenga extensiones
    nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
    archivo_csv = f"{nombre_base}.csv"
    
    if os.path.exists(archivo_csv):
        # Si el archivo CSV ya existe, cargarlo y concatenar las nuevas filas
        df_existente = pd.read_csv(archivo_csv)
        df_actualizado = pd.concat([df_existente, df], axis=1)
    else:
        # Si el archivo CSV no existe, usar el nuevo DataFrame
        df_actualizado = df

    # Guardar el DataFrame actualizado en el archivo CSV
    df_actualizado.to_csv(archivo_csv, index=False)
    print(f"Información guardada en {archivo_csv}")

# # Llamada a la función con el archivo PDF de entrada
# archivo_pdf = "riesgocreditossubordinadostilpesosl4mar202.pdf"
# extract_and_process_info(archivo_pdf)
