from ev4funciones import ingresar_usuario,buscar_usuario,eliminar_usuario


registro = {}


while True:
    print("MENU PRINCIPAL")
    print("")
    print("1.- Ingresar usuario")
    print("2.- Buscar usuario")
    print("3.- Eliminar usuario")
    print("4.- Salir")
    print("")
    try:
        op = int(input("Ingrese opción: "))
    except ValueError:
        print("ERROR ingrese opción válida")
        continue
    if op not in [1,2,3,4]:
        print("ERROR ingrese opción válida")
        continue
    elif op == 1:
        ingresar_usuario(registro)
    elif op == 2:
        buscar_usuario(registro)
    elif op == 3:
        eliminar_usuario(registro)
    elif op == 4:
        print("Saliendo...")
        break
















