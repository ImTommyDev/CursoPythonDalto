#listas
lista = ["Tomas",21,True,22,"Carlos"]

lista.append("Juan") #Agrega un elemento al final de la lista
lista[2] = False #Modifica el elemento en la posicion 2 de la lista
print(lista[0]) #Tomas
print(lista[1]) #21
print(lista[2]) #False

#tuplas - NO MODIFICABLES
#Las tuplas son similares a las listas pero no se pueden modificar una vez creadas
tupla = ("Tomas",21,True,22,"Carlos")
print(tupla[0]) #Tomas
print(tupla[1]) #21

#Set - Conjuntos - NO MODIFICABLES (igual que las tuplas)
#Los conjuntos no permiten elementos duplicados y no tienen un orden definido, son ideales para almacenar elemento unicos
conjunto = {"Tomas",21,True,22,"Carlos"}
#Si puedo modificar el conjunto, pero no los elementos dentro de el (las tuplas igual)
conjunto = {"Tomas",21,True,22,"Carlos","Juan","Juan"}
print(conjunto) #{'Carlos', 21, 'Juan', True, 'Tomas'}
#No puedo accerder a los elementos de un conjunto por su posicion, pero si puedo verificar si un elemento esta dentro del conjunto
#print(conjunto[1]) -> Error, no puede acceder

#Diccionarios - Almacena datos en pares clave-valor, es u JSON
diccionario = {
    "Nombre": "Tomas",
    "Edad": 21,
    "Casado": True,
    "Hijos": 22,    
}

print(diccionario["Nombre"]) #Tomas
print(diccionario["Edad"]) #21