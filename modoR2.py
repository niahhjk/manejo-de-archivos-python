try:
    with open("ejemplo.txt", "r") as archivo:
        contenido = archivo.read()
        print("Contenido del archivo:")
        print(contenido)
except FileNotFoundError:
    print("El archivo no existe.")