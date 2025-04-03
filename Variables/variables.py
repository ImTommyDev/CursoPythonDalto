a = 2
b = 3
c = a + b
c += 10
print(c)

bienvenida = "Hola"
nombre = "Juan"
print(bienvenida + " " + nombre)

edad = f"Tu edad es {c}?"
print(edad)

del edad # Eliminar la variable edad
#print(edad) # Esto generará un error porque la variable edad ya no existe

print("ola" in bienvenida) # Verifica si "ola" está en la variable bienvenida
print("ola" not in bienvenida) # Verifica si "ola" no está en la variable bienvenida
print("Ola" in bienvenida) # Verifica si "Ola" está en la variable bienvenida (case-sensitive)

