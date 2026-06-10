

import funcionesinv as fn


productos = {
    "Mouse": [10, 15000],
    "Teclado":[5, 25000],
    "Audifonos":[8, 30000]
}

while True:
    print("----MENU-----")
    print("")
    print("1.- Agregar Productos")
    print("2.- Mostrar Productos")
    print("3.- Buscar Productos")
    print("4.- Producto mas caro")
    print("5.- Salir")
    print("")
    try:
        op = int(input("Ingrese opción (1/5) : "))
        if op in (1,2,3,4,5):
            if op == 1:
                productos = fn.agregarproducto(productos)
        else:
            print("Ingrese opción válida")
    except:
        print("Ingrese un número entero")


























