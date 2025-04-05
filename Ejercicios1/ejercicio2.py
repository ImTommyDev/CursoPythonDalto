frase = input("Dime una frase y te digo cuanto tardarias si tuvieras que decirla: ")
cantidad_palabras = frase.split(" ")
cantidad_de_palabras = len(cantidad_palabras)
print(f'Dijiste {cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras / 2} segundos en decirla')
print(f'Dalto lo diria en {cantidad_de_palabras / 2 * 1.3} segundos')

if cantidad_de_palabras > 120:
    print('Tampoco te pases, eh?')