import numpy as np

numeros = [10, 20, 30, 40, 50]
arreglo = np.array(numeros)

print(arreglo)
print(type(arreglo))

# operaciones vectorizadas

precio = np.array([50,70,100,150,500])

precio_descuento = precio*0.85
precio_final = np.round(precio_descuento,2)
print(precio_final)


"""
EJERCICIO GUIADO

1.crear su propio array, llamarlo "temperaturas_semana"
2.introducir 7 valores a su array.
3.imprimir el promedio, la maxima, la minima y la desviacion estandar
4.redondear todo los resultados a 1 decimal
"""

temperatura = np.array([23.25,30,31,40,16.50])