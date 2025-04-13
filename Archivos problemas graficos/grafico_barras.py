import pandas as pd
import matplotlib.pyplot as plt #libreria para graficar
import seaborn as sns #libreria para graficos estadisticos

df = pd.read_csv('Archivos problemas graficos\\pedos.csv')

#Creando un grafico de lineas
sns.barplot(x='fecha', y='pedos',data = df)

total_pedos = df['pedos'].sum()

#Mostrando el total
print(f'El total de pedos es de {total_pedos}')

#Mostrando el gráfico de lineas 
plt.show()