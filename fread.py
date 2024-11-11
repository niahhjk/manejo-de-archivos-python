with open('ehh.bin', 'rb') as file:
    datos = file.read(5)  
    file.seek(2)          
    linea = file.readline()