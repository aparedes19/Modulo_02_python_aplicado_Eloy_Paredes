frutas = ["manzana", "banana", "fresa", "naranja", "pera"]

#print(frutas[0]) 
#print(frutas[1])  
#print(frutas[-1])  # trae el último elemento de la lista
#print(frutas[1:3])
#print(len(frutas))

#agregar elementos a la lista

#frutas.append("kiwi")
#print(frutas)

#Eliminar elementos de la lista

#frutas.remove("banana")
#print(frutas)

#insertar valores en una posición específica de la lista

#insertar = frutas.insert(2, "kiwi")
#print(frutas)

# preguntar si un elemento está en la lista

#print("manzana" in frutas)
#print("kiwi" in frutas)


#numeroos = [10, 20, 30, 40, 50]

#print(numeroos[:2])
#print(numeroos[2:])
#print(numeroos[::2])

Temperaturas = [22, 25, 28, 32, 19, 27, 24]
#print(Temperaturas[:3])
#print(Temperaturas[3:])


#print(temp_max)
#print(temp_min)

# Organizar lista de menor a mayor

#Temperaturas.sort()
#print(Temperaturas)

# Organizar lista de mayor a menor

#Temperaturas.sort(reverse=True)
#print(Temperaturas)


#Tareas = ["Lavar los platos", "Hacer la cama", "Sacar la basura", "Estudiar Python"]    

# Listas aisladas 

#tablero = [
 #  [ "X", "o", "x"],
#    [ "o", "x", "o"],
#     [ "x", "o", "x"]
#]

#print(tablero[0] ) # Imprime "X"
#print(tablero[0][1]) # Imprime "o"
#print(tablero[2][2]) # Imprime "o"

# Listas aisladas con bucles
#notas_alumnos = [
  #  ["Juan", 85, 70, 90],    
  #  ["María", 90, 85, 75],
   # ["Pedro", 70, 65, 80]
#]

#for alumno in notas_alumnos:
  #  nombre = alumno[0]
  #  notas = alumno[1:]
  #  promedio = sum(notas) / len(notas)
  #  print(f"El promedio de {nombre} es: {round(promedio, 1)}")


# tuplas

#coordenadas = (19.78, -70.69)

#print(coordenadas[0])  # Imprime 19.78
#print(coordenadas[1])  # Imprime -70.69
#print(type(coordenadas))  # Imprime <class 'tuple'>

# ejercicio guiado

#punto_A = (0, 0)
#punto_B = (3, 4)


# Puntos dados
punto_a = (0, 0)
punto_b = (3, 4)

# Asignación de variables desde las tuplas
x1, y1 = punto_a[0], punto_a[1]
x2, y2 = punto_b[0], punto_b[1]

# Aplicamos la fórmula: raíz cuadrada de ((x2 - x1)² + (y2 - y1)²)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

print("La distancia es:", distancia)

punto_a = (0, 0)
punto_b = (3, 4)

x1, y1 = punto_a
x2, y2 = punto_b
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print("La distancia es:", distancia)