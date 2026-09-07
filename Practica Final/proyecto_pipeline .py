import numpy as ny
import pandas as pd



df = pd.read_csv("Practica Final/hollywood.csv")

Columnas_necesarias = [ "Movie", "LeadStudio", "Genre", "RottenTomatoes", "AudienceScore", "WorldGross", "Budget", "Year"]

df = df[Columnas_necesarias]

# Cantidad de filas y columnas.
#print("Total de filas y columnas:",df.shape)

# Cantidad de columnas con valores nulos
#print("\nColumnas con valores nulos:")
#print(df.isnull().sum())


"""Sustituir valores nulos."""
# Textos

df ["Genre"] = df["Genre"].fillna("Desconocido")
df ["LeadStudio"] = df ["LeadStudio"].fillna("Pendiente")


#Numericos por la media de los datos en esa columna.

df ["RottenTomatoes"] = df["RottenTomatoes"].fillna(df["RottenTomatoes"].median())
df ["AudienceScore"] = df["AudienceScore"].fillna(df["AudienceScore"].median())

"""Eliminar finas"""

df = df.dropna(subset=["WorldGross", "Budget"])

#print(f"Total de filas: {len(df)}")
#print(f"Total de nulos: {df.isnull().sum().sum()}")


"""Crear una columna """

# Columna de Ganancia
df ["Ganancias"] = df["WorldGross"] - df["Budget"]

# Columna de Exitosa
df["Exitosa"] = df["RottenTomatoes"] >= 60

#print(df["Ganancias"])
#print(df["Exitosa"].value_counts())


"""Validar tipo de dato de la columna Exitota """

#print("Tipo de dato de Exitosa:",df["Exitosa"].dtype)



"""Agrupar con Groupby"""

# Por genero
Promedio_Categoria = df.groupby("Genre")["RottenTomatoes"].mean().round(1)

print(Promedio_Categoria)

# Por estudio

promedio_estudio = df.groupby("LeadStudio")["Ganancias"].mean().round(1)

print(promedio_estudio)

"""Guardar y cargar"""

df.to_csv("Hollywood_limpio.csv", index=False)

df_check = pd.read_csv("hollywood_limpio.csv")

print("Cantidad de filas y columnas:",df_check.shape)
print(df_check.isnull().sum())