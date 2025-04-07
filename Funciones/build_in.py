#encontrar el numero mayor de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_mas_grande = max(numeros)
print("El numero mas grande es:", numero_mas_grande)

#El numero menor de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_mas_pequeño = min(numeros)
print("El numero mas pequeño es:", numero_mas_pequeño)

resultado_bool = bool(0)
print(resultado_bool) # False
resultado_bool = bool(1)
print(resultado_bool) # True

resultado_all = all([123,"cxzv",0])
print(resultado_all) # False
resultado_all = all([123,"cxzv",1])
print(resultado_all) # True

sumatoria = sum([1,2,3,4,5])
print(sumatoria) # 15