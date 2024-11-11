with open("leer_linea.txt", "r") as archivo:
    linea = archivo.readline()
    while linea:
        print("Línea:", linea.strip())
        linea = archivo.readline()