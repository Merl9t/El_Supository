import funciones as fn
dick = {
    "Mouse": [10,15000],
    "Teclado": [5,25000],
    "Monitor": [3,180000]
}


while True:
    print("----MENU-----")
    print("")
    print("1.- Agregar Productos")
    print("2.- Mostrar Productos")
    print("3.- Buscar Productos")
    print("4.- Producto mas caro")
    print("5.- Salir")
    try:
        op = int(input("Ingrese opción: "))
    except:
        print("ERROR ingrese un número del 1 al 5")
    if op in (1,2,3,4,5):
        if op == 1:
            while True:
                producnew = input("Nombre producto: ")
                if producnew != None and producnew not in dick:
                    break
                else:
                    print("ERROR! Producto inválido, ingrese nuevamente")
            while True:
                try:
                    stocknew = int(input("Ingrese stock:"))
                except:
                    print("ERROR! Ingrese un número entero")
                if stocknew >= 0:
                        break
                else:
                    print("ERROR! Ingrese un número válido")
            while True:
                try:
                    precionew = int(input("Ingrese Valor: "))
                except:
                    print("ERROR! precio inválido")
                if precionew > 0:
                        break
                else:
                    print("ERROR! Ingrese un número válido")
            dick = fn.agregarproducto(dick,producnew,stocknew,precionew)
        if op == 2:
            Mostrar = fn.mostrarproducto(dick)
            print(Mostrar)   
    else:
        print("ERROR! Ingrese un número valido") 
        


