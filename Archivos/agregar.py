#Agregando lineas con "a" (append) al final del archivo
with open("Archivos\\archivo.txt","a",encoding="utf-8") as archivo:
    archivo.write("\nSoy un archivo de texto\n")
    archivo.write("Estoy aprendiendo a escribir en archivos de texto\n")
    archivo.write("¡Hasta luego!\n")