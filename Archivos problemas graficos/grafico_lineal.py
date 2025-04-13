import pandas as pd
import matplotlib.pyplot as plt #libreria para graficar
import seaborn as sns #libreria para graficos estadisticos

df = pd.read_csv('Archivos problemas graficos\\pedos.csv')

#Creando un grafico de lineas
sns.lineplot(x='fecha', y='pedos',data = df)

#Creando un punto en el maximo punto
plt.plot("06-01",10,"o")

#Mostrando el gráfico de lineas 
plt.show()