import os
from PyPDF2 import PdfReader
import shutil

old_folder = 'sin_titulo/'
new_folder = 'con_titulo/'

# Revisa el número de Archivos que se encuentra en la carpeta de archivos sin título.
num_files_before = len(os.listdir(old_folder))

#Enumera y recorre los archivos que se encuentran en la carpeta de archivos sin título
for file_name in os.listdir(old_folder):
    # Revisa que el archivo tenga externsión .pdf
    if file_name.endswith(".pdf"):
        file_path = os.path.join(old_folder, file_name)
        with open(file_path, "rb") as f:
            # Create a PdfFileReader object to read the file
            reader = PdfReader(f)
            #Toma la página 0 del archivo, donde siempre se va a encontrar el título
            page = reader.pages[0]
            #Extrae el contenido de la primera página del archivo
            page_text = page.extract_text()
            # Revisa que en el contenido se encuentren los substrings 'Concepto 1: ' y 'Concepto 2:'
            # para tomar los índices y extraer el título
            if 'Concepto 1: ' in page_text and 'Concepto 2:' in page_text:
                idx1 = page_text.index('Concepto 1:') + 12
                idx2 = page_text.index('Concepto 2:')
                title = page_text[idx1:idx2].replace('\n', ' ').rstrip()
                #Nuevo nombre del archivo
                new_file_name = f"COMPROBANTE {title}.pdf"
                print(new_file_name)
                new_file_path = os.path.join(new_folder, new_file_name)
                # Copia el archivo con el nuevo nombre en la carpeta de archivos con título
                shutil.copyfile(file_path, new_file_path)

num_files_after = len(os.listdir(new_folder))
# Revisa que haya el mismo número de archivos en las dos carpetas
if num_files_before == num_files_after:
    print('Archivos Correctamente Copiados y Renombrados')
else:
    print('No hay el mismo número de archivos en las dos carpetas')

                
                