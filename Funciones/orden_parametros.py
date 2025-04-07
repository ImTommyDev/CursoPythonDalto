#Cambiando el orden de los parámetros
def saludo(nombre, edad):
    print(f"Hola {nombre}, tienes {edad} años")
    
saludo(edad=25, nombre="Juan") # Cambiando el orden de los parámetros

#Creando la misma función pero con un parámetro opcional
def saludo(nombre, edad=18):
    print(f"Hola {nombre}, tienes {edad} años")
    
saludo("Juan") # Si no se pasa el segundo parámetro, se toma el valor por defecto
saludo("Juan", 25) # Si se pasan ambos parámetros, se usan los valores dados