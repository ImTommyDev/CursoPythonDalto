archivo = open("Archivos/archivo.txt", encoding="UTF-8")
#Leer archivo completo
# print(archivo.read())

#Leo la primera linea
# lineas = archivo.readlines()

#Leo un numero de caracteres
linea = archivo.readline(30) #Leo 30 caracteres

#Cerramos el archivo
archivo.close() #Una vez cerrado no se puede volver a leer hasta que volvamos a abrirlo

#Imprimimos la linea leida
print(linea)

