#Practicando con listas
# Definición de la lista
lista = [1, 3, 2, 4, 7, 6, 5]
# Definición de la lista de cadenas
lista_cadenas = ["Hola", "burro", "Juan"]

resultado = len(lista) # Devuelve la longitud de la lista
resultado2 = lista[0] # Devuelve el primer elemento de la lista
resultado3 = lista[-1] # Devuelve el último elemento de la lista
resultado4 = lista[1:3] # Devuelve una sublista desde el índice 1 hasta el 3 (sin incluir el 3)
resultado5 = lista.append(6) # Añade un elemento al final de la lista
resultado6 = lista.insert(2, 10) # Inserta un elemento en el índice 2
resultado7 = lista.remove(10) # Elimina el primer elemento con el valor 10
resultado8 = lista.pop(2) # Elimina el elemento en el índice 2 y lo devuelve
resultado9 = lista.index(3) # Devuelve el índice del primer elemento con el valor 3
resultado10 = lista.count(2) # Cuenta cuántas veces aparece el valor 2 en la lista
resultado11 = lista.sort() # Ordena la lista en orden ascendente
resultado12 = lista.reverse() # Invierte el orden de la lista
resultado13 = lista.copy() # Crea una copia superficial de la lista
resultado14 = lista.clear() # Elimina todos los elementos de la lista

#Muestro los resultados
print("Resultado 1:", resultado)
print("Resultado 2:", resultado2)
print("Resultado 3:", resultado3)
print("Resultado 4:", resultado4)
print("Resultado 5:", resultado5)
print("Resultado 6:", resultado6)
print("Resultado 7:", resultado7)
print("Resultado 8:", resultado8)
print("Resultado 9:", resultado9)
print("Resultado 10:", resultado10)
print("Resultado 11:", resultado11)
print("Resultado 12:", resultado12)
print("Resultado 13:", resultado13)
print("Resultado 14:", resultado14)