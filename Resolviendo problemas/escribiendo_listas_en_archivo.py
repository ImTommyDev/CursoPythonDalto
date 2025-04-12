#Tengo dos listas, nombres y apellidos, quiero escribirlas en un arhivo txt siguendo el siguiente formato:
#Nombre: tomas
#Apellido: alvarez
#----
#Nombre: juan
#Apellido: perez

nombres = ["tomas", "juan", "maria"]
apellidos = ["alvarez", "perez", "gonzalez"]

for nombre, apellido in zip(nombres, apellidos):
    with open("Resolviendo problemas\\nombres_apellidos.txt", "a") as archivo:
        archivo.write(f"Nombre: {nombre}\n")
        archivo.write(f"Apellido: {apellido}\n")
        archivo.write("----\n")
        