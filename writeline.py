lineas = ["LINEA 1 .\n", "LINEA 2.\n", "LINEA 3.\n"]
with open("escribir_lineas.txt", "w") as archivo:
    archivo.writelines(lineas)
print("Líneas escritas en el archivo con writelines().")