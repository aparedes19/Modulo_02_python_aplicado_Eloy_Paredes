import numpy as np 
import pandas as pd


df = pd.read_csv("titanic.csv")

#print(df.shape)
#print(df.isnull().sum())


# eliminar columna "Cabin" porque tiene alrededor de un 77% de casos nulos
df = df.drop(columns=["Cabin"])


#carcular la media de la columna "age"
edad_mediana = df["Age"].median()
df["Age"] = df["Age"].fillna(edad_mediana)

#Eliminar filas vacias dentro de la colunma "Embarked"
df = df.dropna(subset=["Embarked"])

print(df.shape)
print(df.isnull().sum().sum())


"""
EJERCICIO GUIADO

1.Imprimir la cantidad  de columnas que tenemos.
2. Confirmar que la columna "Age" ya que no tiene nulos

"""

print(list(df.columns))
print(df["Age"].isnull().sum())

# crear columnas nuevas atraavez "feature engineering"

df["FamiliaTotal"] = df["sibSp"] + df["Parch"] + 1
print(df[["SibSp", "Parch", "FamiliaTotal"]].head())