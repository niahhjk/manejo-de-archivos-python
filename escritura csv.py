import csv
data = [['Nombre', 'Edad'], ['Juan', 25], ['Ana', 30]]

# Escribir en un archivo CSV
with open('nuevo_archivo.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
