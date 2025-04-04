diccionario = {
    "Nombre": "Juan",
    "Edad": 30,
    "Ciudad": "Madrid",
    "Ocupacion": "Ingeniero"    
}

#Practicando con métodos de diccionarios
# 1. Obtener las claves del diccionario
claves = diccionario.keys()
print("Claves del diccionario:", claves)
nombre = diccionario.get("Nombre")
print("Nombre:", nombre)
diccionario.pop("Edad")
print("Diccionario después de eliminar la edad:", diccionario)
diccionario_iterable = diccionario.items() #Para que puedas iterar sobre el diccionario (recorrer sus elementos)
print("Elementos del diccionario:", diccionario_iterable)
diccionario.clear()
print("Diccionario después de limpiar:", diccionario)