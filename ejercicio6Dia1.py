#Fija un número secreto (por ejemplo, 7). Pide al usuario que lo adivine. Di si su número es mayor, menor o igual al número secreto.
numero_secreto = 7
while True:
    intento = int(input("Adivina el numero secreto: "))

    if intento < numero_secreto:
        print("Tu numero es menor que el numero secreto.")
    elif intento > numero_secreto:
        print("Tu numero es mayor que el numero secreto.")
    else:
        print("Adivinaste el número secreto.")
        break
