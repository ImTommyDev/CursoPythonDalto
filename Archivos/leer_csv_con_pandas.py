import pandas as pd

# Leyendo un archivo CSV con pandas y especificando los nombres de las columnas
df = pd.read_csv('Archivos\\archivo.csv')#,names=['name','lastname','age'])#Al añadir names las columnas que antes tenia como encabezado, pasan a ser una fila mas del dataframe, por lo que se recomienda usar el parametro header=None para evitar esto.

# print(df)

#Ordenando valores
df_ordenado = df.sort_values("edad")

# print(df_ordenado)

#Ordenandolo de forma descendente
df_ordenado_desc = df.sort_values("edad", ascending=False)
# print(df_ordenado_desc)

#Obteniendo la columna nombre
nombres = df['nombre']

# print(nombres)

#Concatenando los 2 dataframes
df_concatenado = pd.concat([df, df_ordenado])
# print(df_concatenado)

#Accediendo a la primera fila con head()
primera_fila = df.head(1)
#print(primera_fila)

encabezado = df.head(0)
#print(encabezado) 

#Accediendo a la ultima fila con tail()
ultima_fila = df.tail(1)
#print(ultima_fila)

#Accediendo a las ultimas 3 filas
ultimas_filas = df.tail(3)
#print(ultimas_filas)

#Accediendo a la cantidad de filas y columnas con shape
# filas_y_columnas = df.shape
# print(filas_y_columnas) #Es una tupla
# filas_totales = filas_y_columnas[0]
# columnas_totales = filas_y_columnas[1]
# print(filas_totales)
# print(columnas_totales)

#Desempaquetando con shape
filas_totales, columnas_totales = df.shape
# print(filas_totales)
# print(columnas_totales)

#Obteniendo datos estadisticos con describe()
df_info = df.describe()
# print(df_info)

#Accediendo a un elemento especifico con loc[]
elemento_especifico = df.loc[0, 'nombre'] #Accediendo a la fila 0 y columna nombre
# print(elemento_especifico)

#Accediendo a la edad de la fila 4 con iloc
elemento_con_iloc = df.iloc[3,2]
# print(elemento_con_iloc)

#Accediendo a tosas las filas de una columna
nombres = df.iloc[:,1]
# print(nombres)

#Accediendo a la fila 2 con todos los datos
fila = df.iloc[1,:]
# print(fila)

#Accediendo a filas con edad > 20
filas_edad_mayor_20 = df.loc[df["edad"] > 20,:]
print(filas_edad_mayor_20)

#Practicando con slicing
cadena = "0123456789"
# print(cadena[0:3])#Imprime 123
# print(cadena[1:3]) #La posición de final no se incluye