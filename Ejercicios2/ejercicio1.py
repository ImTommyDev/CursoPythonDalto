#Un alumno va a hacer de profesor
#Otro harás de asistente
#A -> Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenarlos por edad de mayor a menor
#B -> El mayor es el profesor y el menor el asistente, quien es quien

#Funcion que recibe la cantidad de compañeros y pregunta el nombre y la edad de cada uno
compañeros = []

def ingresa_compañeros(cantidad):
    for i in range(cantidad):
        nombre = input("Ingrese el nombre del compañero: ")
        edad = int(input("Ingrese la edad del compañero: "))
        compañeros.append((nombre, edad))
    compañeros.sort(key=lambda x: x[1], reverse=True) # Ordena la lista de compañeros por edad de mayor a menor
    asistente = compañeros[-1] #El menor es el asistente
    profesor = compañeros[0] # El mayor es el profesor
    return profesor, asistente

profesor,asistente = ingresa_compañeros(3) # Cambia el número 5 por la cantidad de compañeros que quieras ingresar
print("El profesor es:", profesor[0], "con edad", profesor[1])
print("El asistente es:", asistente[0], "con edad", asistente[1])