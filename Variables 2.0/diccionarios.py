diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniero",
    "hobbies": ["futbol", "lectura", "viajar"],
    "activo": True,
    "altura": 1.75,
    
}

#Para crear tuplas, listas o diccionarios vacios debo usar su respectiva funcion
# Tupla vacia: tupla = tuple()
# Lista vacia: lista = list()
# Diccionario vacio: diccionario = dict()

diccionario_con_tuplas_clave= {
    ("nombre", "edad"): ("Juan", 30),
    ("ciudad", "profesion"): ("Madrid", "Ingeniero"),
    ("hobbies", "activo"): (["futbol", "lectura", "viajar"], True),
    ("altura"): (1.75),
}

print(diccionario_con_tuplas_clave)

#Creando diccionarios solo con claves usando fromkeys
diccionario_vacio = dict.fromkeys(["nombre", "edad", "ciudad"])
print(diccionario_vacio)