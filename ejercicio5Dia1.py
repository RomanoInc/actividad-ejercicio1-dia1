#Pide al usuario el total de una cuenta. Luego pregunta qué porcentaje de propina quiere dejar (10, 15 o 20). Calcula y muestra el valor de la propina.
cuenta = float(input("total de la cuenta: "))
propina = float(input("Que porentaje de propina desea dejar? 10%, 15%, 20%: "))
if propina == 10:
    propina = cuenta * propina/100
    print("propina:", propina)
elif propina == 15:
     propina = cuenta * propina/100
     print("propina:", propina)
elif propina == 20:
    propina = cuenta * propina/100
    print("propina:", propina)
