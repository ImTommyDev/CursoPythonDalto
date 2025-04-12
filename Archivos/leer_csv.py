import csv

with open("Archivos\\archivo.csv") as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila)