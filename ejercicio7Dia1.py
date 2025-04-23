#Pide dos números al usuario. Imprime cuál es el mayor. Si son iguales, indícalo.
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
if num1 > num2:
    print("El primer numero es mayor.")
elif num2 > num1:
    print("El segundo numero es mayor.")
else:
    print("Los dos numeros son iguales.")
