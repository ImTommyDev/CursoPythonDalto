#Operadores lógicos
#AND
resultado1 = True & True # True
resultado2 = True & False # False
resultado3 = False & True # False
resultado4 = False & False # False

#OR
resultado5 = True | True # True
resultado6 = True | False # True
resultado7 = False | True # True
resultado8 = False | False # False

#NOT
resultado9 = not True # False
resultado10 = not False # True

#Muestro los resultados
print("Resultados de AND:")
print("True & True:", resultado1)
print("True & False:", resultado2)
print("False & True:", resultado3)
print("False & False:", resultado4)
print("\nResultados de OR:")
print("True | True:", resultado5)
print("True | False:", resultado6)
print("False | True:", resultado7)
print("False | False:", resultado8)
print("\nResultados de NOT:")
print("not True:", resultado9)
print("not False:", resultado10)