import json

with open('archivo.json', 'r') as file:
    data = json.load(file)
    print(data)
