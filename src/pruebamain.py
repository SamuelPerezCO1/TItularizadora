import pdfaword
import saldoymora
import txtacsv
import os

input_folder = 'C:\\Codigos\\Titularizadora\\pdfs'
carpeta_word = 'C:\\Codigos\\Titularizadora\\word'
carpeta_txt = 'C:\\Codigos\\Titularizadora\\txt'
ruta_principal = os.path.abspath(os.path.join(carpeta_txt, os.pardir))


# pdfaword.pdfaword(input_folder , output_folder)
# saldoymora.process_and_extract_text(output_directory=output_directory , input_directory=output_folder)
saldoymora.funcionx(output_directory=carpeta_txt , input_directory=carpeta_word)
txtacsv.convertir_txt_a_csv(ruta_txt=carpeta_txt , ruta_principal=ruta_principal)