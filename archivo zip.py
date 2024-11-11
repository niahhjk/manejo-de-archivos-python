import zipfile

with zipfile.ZipFile('archivo.zip', 'r') as zip_ref:

    zip_ref.extractall()

    print(zip_ref.namelist())
