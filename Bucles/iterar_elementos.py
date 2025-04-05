animales = ['perro', 'gato', 'ratón', 'loro']
for animal in animales:
    print(animal)
    
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    #Sumando 10 a todos
    numero += 10
    print(numero)
    
#Iterando dos listas del mismo tamaño al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f"El {animal} tiene el número {numero}.")
    
for i in range(5,10):
    print(i)
    
for num in enumerate(numeros):
    print(type(num))
    print(num) #Son una tupla (indice, valor)
    indice = num[0]
    valor = num[1]
    print(f"El índice es {indice} y el valor es {valor}.")
    
#Usando el else
for numero in numeros:
    print(numero)
else: #Se ejecuta si no se rompe el bucle
    print("No hay más números.")