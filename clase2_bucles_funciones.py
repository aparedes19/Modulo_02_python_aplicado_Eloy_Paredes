# Bucle for
#edades = [24, 31, 19, 45, 27]

#mayor_30 = 0
#for edad in edades:
   # if edad >= 30:
       # mayor_30 += 1
        #print(mayor_30)


    #suma = suma + edad

#print("suma total:", suma)
#print("promedio:", suma / len(edades))

#Número = 5
#while Número > 1:
    #print(Número)
   # Número -= 1

#print("Iniciamos")

def clasificar_imc(peso, altura):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return " Peso Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
    
print(clasificar_imc(70, 1.75))  # Normal