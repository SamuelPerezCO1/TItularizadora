import os
import docx2txt

# Función para procesar un archivo y extraer el texto desde "meses" hasta encontrar "tasa"
def process_and_extract_text(file_name, output_file_name):
    # Extraer texto del archivo .docx
    text = docx2txt.process(file_name)
    lines = text.splitlines()

    start_printing = False
    stop_printing = False
    extracted_lines = []

    for line in lines:
        # Comprobar si la línea no está vacía o contiene solo espacios en blanco
        if line.strip() and '_' not in line:
            if 'tasa' in line.lower():
                stop_printing = True
            if start_printing and not stop_printing:
                extracted_lines.append(line)
            if 'meses' in line.lower():
                start_printing = True

    # Guardar el texto filtrado en un archivo
    with open(output_file_name, 'w', encoding='utf-8') as f:
        for line in extracted_lines:
            f.write(line + '\n')

    # Directorio donde están los archivos
    # input_directory = "C:\\Codigos\\prueba\\word"
    # # Directorio donde se guardarán los archivos de texto
    # output_directory = "C:\\Codigos\\prueba\\txt"

    # Crear el directorio de salida si no existe
def funcionx(output_directory , input_directory):
    os.makedirs(output_directory, exist_ok=True)

    # Obtener lista de archivos en el directorio de entrada
    files = [os.path.join(input_directory, file) for file in os.listdir(input_directory) if file.endswith('.docx')]

    # Procesar cada archivo
    for file in files:
        print("-" * 50)
        print(f"Procesando archivo: {file}")
        # Obtener el nombre base del archivo y cambiar la extensión a .txt
        base_name = os.path.splitext(os.path.basename(file))[0]
        output_file = os.path.join(output_directory, base_name + '.txt')
        process_and_extract_text(file_name=file,output_file_name= output_file)
        print(f"Texto filtrado guardado en: {output_file}")
        print("-" * 50)
