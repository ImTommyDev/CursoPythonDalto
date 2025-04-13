def sumar_dos ():
    n = input("Intruce un numero: ")
    n2 = input("Intruce otro numero: ")
    
    try:
        n = int(n)
        n2 = int(n2)
        
        resulado = n + n2
        print(f"El resultado es: {resulado}")
        
    except ValueError:
        print("Uno de los valores no es un numero")
        return
    
    
sumar_dos()