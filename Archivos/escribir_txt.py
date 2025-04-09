#Practicando escribir en el archivo.txt
# #SOBREESCRIBIENDO EL ARCHIVO
# with open("Archivos/archivo.txt","w",encoding="utf-8") as archivo:
#     archivo.write("Hola mundo\n")
#     archivo.write("Soy un archivo de texto\n")
#     archivo.write("Estoy aprendiendo a escribir en archivos de texto\n")
#     archivo.write("¡Hasta luego!\n")

#No sobreescriboendo el archivo, solo añadiendo contenido al final del archivo
with open("Archivos\\archivo.txt","w",encoding="utf-8") as archivo:
    archivo.writelines(["Hola\n","Que tallll"]) #Escribo una lista de cadenas en el archivo, el metodo readlines tambien devuelve una lista, esto es lo mismo pero escribiendo
    #También está sobreescribiendo el archivo, pero cuando llamo al metodo varias veces lo que hace es añadir mas lineas
    archivo.writelines(["\nSaludos"])