from PyPDF2 import PdfReader
import pandas as pd
import re
import os

def extract_and_process_info(archivo_pdf):
    with open(archivo_pdf, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

    pattern = r'Escenarios de Estrés\s*_{5,}\s*(.*?)\s*Tasa'
    match = re.search(pattern, text, re.DOTALL)
    if match:
        extracted_text = match.group(1).strip()
    else:
        return "No se encontró la información entre Escenarios de Estrés y Tasa"
    
    lines = extracted_text.split('\n')
    lines = [line for line in lines if line.strip()]
    
    data = []
    for line in lines:
        parts = line.split()
        if all(part is not None for part in parts):
            data.append([" ".join(parts)]) 
    
    df = pd.DataFrame(data, columns=["Escenarios Estres"])
    
    nombre_base = os.path.splitext(os.path.basename(archivo_pdf))[0]
    archivo_csv = f"{nombre_base}.csv"
    
    if os.path.exists(archivo_csv):
        df_existente = pd.read_csv(archivo_csv)
        df_actualizado = pd.concat([df_existente, df], axis=1)
    else:
        df_actualizado = df

    df_actualizado.to_csv(archivo_csv, index=False)