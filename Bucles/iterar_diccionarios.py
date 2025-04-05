diccionario = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid"
}

for clave in diccionario.items():
    key = clave[0]
    value = clave[1]
    print(f"{key}: {value}")