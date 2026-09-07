import pandas as pd


#Estudiantes = pd.DataFrame({

    #"nombre": ["Maria","Carlos", "Jose", "Carmen"],
    #"edad": [25, 28, 35, 27],
    #"Curso": ["Desarrollo", "Data Analyst", "Ciencia de datos", "Seguridad"]

#})

#print(Estudiantes)

df = pd.read_csv("titanic.csv")

#print(df.shape)
#print(list(df.columns))
#print(df.head()) # sin numero me descarga las primeras 3 colunna, con numero las especificas


#subset = df[["name", "age", "survived"]]

#print(subset.head(3))

# crear array de numpy con una serie (pandas)

import numpy as np

edades = df["Age"].dropna()

edades_array = edades.to_numpy()

#print(type(edades_array))


#print("promedio de edad:", round(np.mean(edades_array), 1))


"""
EJERCICIO GUIADO

1.filtrar el DataFrame para quedarse solo con los pasajeros de la columna "Pclass".
2.guardar en una variable nueva e imprimira cuantas filas tienes.
3.despues utilizara el metodo ".value_counts() sobre la columna "Pclass" del DataFrame original.

objetivo: visualizar cuantos pasajeros habia en cada clase
"""

pasajeros_primera_clase = df[df['Pclass']==1]

print(pasajeros_primera_clase.shape)

print(df["Pclass"].value_counts())