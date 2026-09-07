#Estudiante = {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"}

#verificar información en el diccionario
#print(Estudiante["nombre"])  # Imprime "Juan"


# modificar información en el diccionario
#Estudiante["edad"] = 21
#print(Estudiante["edad"])  # Imprime 21


#agregar nueva información al diccionario
#Estudiante["universidad"] = "Universidad Nacional"
#print(Estudiante["universidad"])  # Imprime "Universidad Nacional"

#eliminar información del diccionario
#del Estudiante["carrera"]
#print(Estudiante)  # Imprime el diccionario sin la clave "carrera"



"""
EJERCICIO PRACTICO

1.crear un diccionario llamado "producto"
2.las llaves (clave y valor) "nombre", "precio" y "stock"
3.agregar una nueva llave llamada "categoria"
4.modificar el valor de la llave "precio" sumandole 10 al valor original.
5. eliminar la llave "stock" del diccionario

"""
# crear dicionario llamado "producto"
#producto = {"nombre": "Camiseta", "precio": 500, "stock": 30}
#print(producto)

# agregar nueva llave "categoria"
#producto["categoria"] = "Ropa"
#print(producto)

# modificar el valor de la llave "precio" sumandole 10 al valor original
#producto["precio"] = producto["precio"] + 10
#print(producto)

# eliminar la llave "stock" del diccionario
#del producto["stock"]
#print(producto)


# metodo para obtener todas las llaves del diccionario metodo Keys()
 
#Estudiante = {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería"}

#print(Estudiante.keys())  # Imprime todas las llaves del diccionario
#print(Estudiante.values())  # Imprime todos los valores del diccionario
#print(Estudiante.items())  # Imprime todos los pares de llave-valor del diccionario
#print(len(Estudiante))  # Imprime la cantidad de elementos en el diccionario
#print(Estudiante.get("nombre"))  # Imprime el valor asociado a la llave "nombre"


"""
EJERCICIO PRACTICO

utilicen este dicionario: inventario = {"manzanas": 50, "peras": 30, "uvas": 88}
recorrer el dicionario con el metodo items() que se imprina(print) para cada elemento del dicionario la siguiente frase: "En el inventario hay {valor} {llave}"

suficiente = 40 o mas
pocas inventario = 40

"""
#inventario = {"manzanas": 50, "peras": 30, "uvas": 88}

#for producto, cantidad in inventario.items():
#    if cantidad >= 40:
#        print(f"{producto}: {cantidad}")
#     else:
#        print(f"En el inventario hay pocas {producto}: {cantidad}")





# conjuntos (sets) son colecciones de elementos únicos y no ordenados. Se pueden crear utilizando llaves {} o la función set().

# frutas = {"manzana", "banana", "naranja", "pera"}

#Lista_valores_repetidos = {"manzana", "banana", "manzana", "pera"} 

#nueva_frutas = set(Lista_valores_repetidos)  # convierte la lista en un conjunto, eliminando los valores duplicados

#print(nueva_frutas)  # Imprime {'manzana', 'banana', 'pera'}


# operaciones entre conjuntos

#frutas = {"manzana", "banana", "naranja", "pera"} 
#frutas_citricas = {"naranja", "limón", "mandarina"}

# Juntar conjutos sin repetir los valores que esten en los dos conjuntos
#print(frutas.union(frutas_citricas))  # Imprime {'manzana', 'banana', 'naranja', 'pera', 'limón', 'mandarina'}

# devolver  solo los valores que esten en los dos conjuntos
#print(frutas.intersection(frutas_citricas))  # Imprime {'naranja'}

# devolver los valores que estan en el primer conjunto pero no en el segundo
#print(frutas.difference(frutas_citricas))  # Imprime {'manzana', 'banana', 'pera'}  



"""
EJERCICIO GUIADO

trabajar con esta lista: "respuesta = ["python", "java", "python", "C++", "python", "java"]

1.obtener cuantas respuestas distintas hay (sin repetir)
2.imprimir el numero de elementos que no se repiten en la lista, junto con el set de opciones distintas y ordenadas alfabeticamente

pista: transformar lista a set
"""


#respuesta = ["python", "java", "python", "C++", "python", "java"]

# 1. Obtener cuantas respuestas distintas hay (sin repetir)
#respuestas_distintas = set(respuesta)

# 2. Imprimir el numero de elementos que no se repiten en la lista, junto con el set de opciones distintas y ordenadas alfabeticamente
#print(f"Numero de respuestas distintas: {len(respuestas_distintas)}")
#print(f"Opciones distintas ordenadas alfabeticamente: {sorted(respuestas_distintas))



"""INSTRUCCIÓN

  EJERCICIO TORNEO DE TRIVIA

Vas a recibir una lista de equipos, donde cada equipo es una lista con el nombre seguido de 3 puntajes de
ronda, por ejemplo: ["Los Rayos", 15, 20, 18] . Con esa lista de equipos, tu programa debe:
1. Con un for , calcular el total de puntos de cada equipo (la suma de sus 3 rondas) e imprimir, para cada
uno, su nombre, su total, y su clasificación.
2. Escribir una función clasificar_equipo(total) que devuelva "Campeón" si el total es 60 o más,
"Finalista" si es de 40 a 59, y "Participante" si es menor a 40.
3. Encontrar cuál equipo tiene el total más alto.
4. Con un while , simular una ronda bonus para ese equipo: cada vuelta suma 5 puntos extra hasta que
su total llegue o supere los 70 puntos. Contar cuántas rondas bonus tomó, e imprimir el nombre del equipo,
las rondas necesarias, y el total final tras la ronda bonus.
5. Guardar el resultado del campeonato en una tupla (nombre, clasificación) con el nombre del
equipo que tuvo el total más alto y su clasificación, e imprimirla. """


equipos = [
    ["Los Rayos", 15, 20, 18],
    ["Estrellas FC", 22, 19, 25],
    ["Team Nova", 10, 12, 8],
]

# Total de puntos
for equipo in equipos:
    nombre = equipo[0]
    total = sum(equipo[1:]) 
    
    # Clasificación equipos
    if total >= 60:
        clasificacion = "Campeón"
    elif total >= 40:
        clasificacion = "Finalista"
    else:
        clasificacion = "Participante"
        
    print(f"{nombre}: total {total}, {clasificacion}")

    # Puntaje total mas alto por equipo.

Total_equipo = [
    ["Estrellas", 66],
    ["Team nova", 30],
    ["Los Rayos", 53]
]

max_puntaje = -1
nombre_ganador = ""

for equipo in Total_equipo:
    nombre = equipo[0] 
    puntaje = equipo[1]
    
    
    if puntaje > max_puntaje:
        max_puntaje = puntaje
        nombre_ganador = nombre

print(f"Equipos puntaje mas alto: {nombre_ganador} = {max_puntaje}")


rondas = 0

while max_puntaje < 70:
    max_puntaje = max_puntaje +5
    rondas = rondas + 1

print(f"Equipo: {nombre_ganador}")
print(f"Rondas necesarias: {rondas}")
print(f"Total final tras ronda bonus: {max_puntaje}")




clasificacion = "Campeon"

resultado_campeonato = (nombre_ganador, clasificacion)

print(resultado_campeonato)

