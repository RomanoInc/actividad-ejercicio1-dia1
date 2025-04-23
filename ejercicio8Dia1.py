peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)
print("Tu IMC es:", imc)

if imc < 18.5:
    print("Bajo peso")
elif imc >= 18.5 and imc <= 24.9:
    print("Normal")
elif imc >= 25 and imc <= 29.9:
    print("Sobrepeso")
else:
    print("Obesidad")

