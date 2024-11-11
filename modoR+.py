with open("ejem.txt", "r+") as archivo:
    contenido = archivo.read()
    print("Contenido inicial:")
    print(contenido)
    
    archivo.write("\nTexto adicional al final del archivo.")
    print("Lectura y escritura completadas.")