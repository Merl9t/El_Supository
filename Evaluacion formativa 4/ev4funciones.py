def ingresar_usuario(registro):
    while True:
        user = input("Ingrese nombre usuario: ")
        if user not in registro:
            break
        else:
            print("Nombre no disponible")
            continue
    while True:
        sex = input("Ingrese sexo (F/M): ").lower()
        if sex not in ["f","m"]:
            print("Ingrese opción válida")
            continue
        else:
            break
    while True:
        passwrd = input("Ingrese contraseña: ")
        con_num = False
        con_letra = False
        for letras in passwrd:
            if letras.isdigit():
                con_num = True
            if letras.isalpha():
                con_letra = True
        if len(passwrd) >= 8 and con_num and con_letra and " " not in passwrd:
            break
        else:
            print("La clave debe tener al menos 1 letra, 1 dígito y largo mínimo 8 caracteres")
            continue
    registro[user] = [sex, passwrd]
    print("Usuario agregado con éxito!")

def buscar_usuario(registro):
    busque = input("Ingrese nombre de usuario que quiere buscar: ")
    if busque not in registro:
        print("Usuario no encontrado! asegurese de haberlo escrito bien")
    else:
        print("Usuario encontrado")
        print(busque)
        print("Sexo: ", registro[busque][0])
        print("Contraseña: ",registro[busque][1])

def eliminar_usuario(registro):
    elim = input("Ingrese nombre de usuario que quiere eliminar: ")
    if elim in registro:
        del registro[elim]
        print("Eliminado!")
    else:
        print("Usuario no encontrado! asegurese de haberlo escrito bien")













