a = 7
b = 2

# Operadores matemáticos

#print(a+b)  # Suma
#print(a-b)  # Resta
#print(a*b)  # Multiplicación
#print(a/b)  # División
#print(a//b) # División entera
#print(a%b)  # Módulo
#print(a**b) # Potencia
#print(a > b)  # Mayor que
#print(a < b)  # Menor que
#print(a >= b) # Mayor o igual que
#print(a <= b) # Menor o igual que
#print(a == b) # Igual que
#print(a != b) # Diferente de


# Ejercicio

"""
Calcular cuantas vueltas completas se pueden correr con esta distancia y cuantos metros sobrantes despues de esas vueltas completas.
"""
#distancia_metros = 1500
#vuelta_metros = 400


#vueltas_completas = distancia_metros // vuelta_metros
#metros_sobrantes = distancia_metros % vuelta_metros

#print("Vueltas completas:", vueltas_completas)
#print("Metros sobrantes:", metros_sobrantes)

# # Entrada y salida de datos

#Nombre = input("Ingrese su nombre: ")
#Edad = int(input("Ingrese su edad: ")) 

#print(f"Hola {Nombre}, el año que viene tendras {Edad + 1} años.")Eloy


# Temperatura en grados Celsius

#Nombre = input("Ingrese su nombre: ")
#Temperatura = float(input("Ingrese su temperatura en celsius: ")) 
#fahrenheit = (Temperatura * 9/5) + 32

#print(f"Hola {Nombre}, la temperatura en Fahrenheit es: {fahrenheit}°F")

# Ejercicio integrador de conpectos

#Edades = [55, 27, 28, 17, 30]

#for edad in Edades:
    #if edad < 18:
        #print(f"{edad} años: Menor de edad")
    #elif edad >= 18 and edad < 65:
        #print(f"{edad} años: Adulto")
    #else:
        #print(f"{edad} años: Adulto mayor")


# 1. variables de entrada
cuenta = float(input("Ingrese el monto de la cuenta: "))
personas = int(input("Ingrese la cantidad de personas: "))

# 2. Determinación del porcentaje base
if cuenta < 20:
    porcentaje = 0.10
elif cuenta <= 50:
    porcentaje = 0.15
else:
    porcentaje = 0.20

# 3. Total de personas y ajuste del porcentaje
if personas > 4:
    porcentaje += 0.05

# 4. Cálculos
propina = cuenta * porcentaje
total = cuenta + propina
pago_por_persona = total / personas

# 5. Resultados
print(f"Propina: ${propina}")
print(f"Total a pagar: ${total}")
print(f"Cada persona paga: ${pago_por_persona}")