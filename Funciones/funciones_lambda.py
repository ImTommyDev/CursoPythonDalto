multiplicar_por_dos = lambda x: x * 2
#Lambda es una función anónima, no tiene nombre, se puede usar para funciones pequeñas y simples
#Ejemplo de uso
print(multiplicar_por_dos(5)) #10

#Creo una función que dice si un número es par o impar
numeros = [1, 2, 3, 4, 5]
def es_par(x):
    return x % 2 == 0

#Usando filter con una función común
numeros_pares = filter(es_par, numeros) #Está haciendo un bucle que devuelve una lista con los números que cumplen la condición
print(list(numeros_pares)) # [2, 4]

#Creando lo mismo que antes pero con lambda
numeros_pares = filter(lambda x: x % 2 == 0, numeros) 
print(list(numeros_pares)) # [2, 4]