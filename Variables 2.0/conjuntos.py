conjunto = set(["dato1","dato2", "dato3"])

print(conjunto)

#Metiendo conjunto dentro de otro conjunto
conjunto1 = frozenset(["dato1","dato2", "dato3"]) #conjunto1 es un subconjunto de conjunto2 cuando decimos que conjunto2 es el conjunto
conjunto2 = {conjunto1, "dato4"} #conjunto2 es un superconjunto de conjunto1 cuando decimos que conjunto1 es el conjunto
print(conjunto2)

#Teoria de conjuntos
conjunto3 = {1,2,3,4,5}
conjunto4 = {1,2,3}
conjunto5 = {4,5,6}

print('conjunto4 es un subconjunto de conjunto3:', conjunto4.issubset(conjunto3)) #verifica si conjunto4 es un subconjunto de conjunto3
print('conjunto3 es un superconjunto de conjunto4:', conjunto3.issuperset(conjunto4)) #verifica si conjunto3 es un superconjunto de conjunto4
print('conjunto5 es un subconjunto de conjunto3:', conjunto5.issubset(conjunto3)) #verifica si conjunto5 es un subconjunto de conjunto3
print('Verificando que hay algun elemento en comun entre conjunto3 y conjunto5:', conjunto3.isdisjoint(conjunto5)) #verifica si conjunto3 y conjunto5 no tienen elementos en comun