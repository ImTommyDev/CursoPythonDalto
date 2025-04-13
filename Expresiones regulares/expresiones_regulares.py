import re

texto = "Hola amigo que tal como estas. Yo bien gracias. Y tu? mi numero es 18272347 --.- 1234567890 \n jwadbljbd"

resultado = re.findall(r"Hola", texto)
# print(resultado)  # ['Hola']

#\d = digitos del 0 al 9
resultado = re.findall(r"\d", texto)
# print(resultado)  # []

#\D = no digitos
resultado = re.findall(r"\D", texto)
# print(resultado)

#\w = letras y digitos alfanumericos a-zA-Z0-9
resultado = re.findall(r"\w", texto)
# print(resultado)

#\W = no letras y digitos alfanumericos
resultado = re.findall(r"\W", texto)
# print(resultado)

#\n = salto de linea
resultado = re.findall(r"\n", texto)
# print(resultado)  # ['\n']

#\s = espacio en blanco
resultado = re.findall(r"\s", texto)
# print(resultado)

#\S = no espacio en blanco
resultado = re.findall(r"\S", texto)
# print(resultado)

#. = cualquier caracter
resultado = re.findall(r".", texto)
# print(resultado)

#\ = cancelar caracteres especiales, todos los que no son alfanumericos
resultado = re.findall(r"\.", texto)
# print(resultado)  # ['.']

