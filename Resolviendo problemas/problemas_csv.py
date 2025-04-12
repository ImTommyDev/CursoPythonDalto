import pandas as pd

df = pd.read_csv("Resolviendo problemas\\archivo.csv") 
# print(df)

#Cambiar el tipo de dato de una columna
# df["edad"] = df["edad"].astype(int)
# print(df.dtypes)

#Reemplazando valores
df["nombre"].replace("carlos", "juanito", inplace=True)
# print(df)

#Eliminando filas con datos faltantes
print(df)
df = df.dropna()
# print(df)

#Eliminando filas duplicadas
df = df.drop_duplicates()
print(df)

#Creando un CSV con el dataframe limpio
df.to_csv("Resolviendo problemas\\archivo_limpio.csv", index=False)