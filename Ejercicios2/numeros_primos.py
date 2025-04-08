#Creo una función que recibe un numero y me devuelve todos los numeros primos desde el 0 hasta este numero, teniendo en cuenta este
def es_primo(n):
    for i in range(2,n-1):
        if n%i == 0: 
            return False
        return True
    
def primos_hasta(num):
    primos = []
    for i in range(2, num+1):
        resultado = es_primo(i)
        if resultado:
            primos.append(i)
    return primos
    
primos = primos_hasta(100)
print(primos)