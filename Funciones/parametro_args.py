#Función que recibe una lista de numeros y me los suma con un bucle for
def suma_numeros(numeros):
    suma = 0
    for numero in numeros:
        suma += numero
    return suma

suma = suma_numeros([1, 2, 3, 4, 5, 6, 7])
print(suma) #15

#Esto no es óptimo, lo voy a hacer utilizando el parámetro args
def suma_numeros(nombre, *numeros):
    return print(f'{nombre} la suma es: {sum(numeros)}')

suma = suma_numeros("tomas",1, 2, 3, 4, 5, 6, 7)

#Forma optima de usar args sin usarlo como parametro
def suma_total(numeros):
    return sum([*numeros])

resultado = suma_total([1, 2, 3, 4, 5, 6, 7])
print(resultado) #15