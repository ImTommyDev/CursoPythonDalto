#Practicando con inputs
# 1. Solicitar al usuario su nombre y edad
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))#El input siempre devuelve un string, por eso lo convertimos a int
print(f'Nombre:" {nombre}, Edad: {edad}')