#Agregar producto
def agregarproducto(productos):
    stocknew = 0
    valornew = 0
    while True:
        producnew = input("Ingrese nombre del producto: ")
        if producnew not in productos and producnew != "":
            print("")
            break
        else:
            print("Ingrese un producto válido")
            print("")
    while True:
        try:
            stocknew = int(input("Ingrese stock: "))
            if stocknew >= 0:
                print("")
                break
            else:
                print("Ingrese un valor válido")
                print("")
        except:
            print("Ingrese un número entero")
    while True:
        try:
            valornew = int(input("Ingrese valor: $"))
            if valornew > 0:
                print("")
                break
            else:
                print("Valor incorrecto")
                print("")
        except:
            print("Ingrese un número entero")
    productos[producnew]=[stocknew,valornew]
    return productos










