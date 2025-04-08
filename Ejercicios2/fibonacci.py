#Calculo la secuencia de fibonacci desde 0 hasta el numero pasado por parametro
def fibonacci(n):
    a,b = 0, 1
    lista_fibonacci = [0]
    for i in range(n):
        if b > n: return lista_fibonacci
        else: 
            lista_fibonacci.append(b)
            a,b = b, a+b
    return a+b

resultado = fibonacci(34)
print(f"{resultado}")