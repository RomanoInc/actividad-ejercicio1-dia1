#Pide una contraseña al usuario. Si coincide con "python123", imprime "Acceso concedido", de lo contrario, "Contraseña incorrecta".
contraseña = "python123"
contraseñaUser = input("Digite contraseña: ")

if contraseñaUser == contraseña: 
    input("acceso concedido")
else:
    print("contraseña incorrecta")
