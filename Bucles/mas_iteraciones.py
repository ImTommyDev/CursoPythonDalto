lista = ["manzana", "pera", "uva", "naranja"]

print("Usando continue")
for fruta in lista:
    if fruta == "uva":
        continue  # Si la fruta es uva, se salta esta iteración
    print(fruta)
    
#Probando a usar break
print("Usando break")
for fruta in lista:
    if fruta == "uva":
        break  # Si la fruta es uva, se sale del bucle
    print(fruta)
    
#Multiplando valores de una lista x2
numeros = [1, 2, 3, 4, 5]
duplicados = [x*2 for x in numeros]  # Multiplica cada número por 2
print(duplicados)