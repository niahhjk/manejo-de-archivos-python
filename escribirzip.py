import zipfile

with zipfile.ZipFile('nuevo_archivo.zip', 'w') as zip_ref:
    zip_ref.write('archivo1.txt')
    zip_ref.write('archivo2.txt')
