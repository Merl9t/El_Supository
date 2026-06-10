import time
def venta(poderes):
    while True:
        print("Productos disponibles:")
        for producto in poderes:
            print(producto)
        print("")
        compra = input("Que quiere comprar? ")
        if compra in poderes:
            print("Producto encontrado!")
            try:
                gramos = int(input("Cuantos gramos quiere comprar? (10 o +,xmayor)"))
                if gramos > 0 and gramos <= (poderes[compra][0]):
                    if gramos >= 10:
                        totalcompra = gramos*(poderes[compra][2])
                    elif gramos < 10:
                        totalcompra = gramos*(poderes[compra][1])
                    print("")
                    print("El precio seria: $",totalcompra)
                    poderes[compra][0] = (poderes[compra][0]) - gramos
                    print("gr restantes: ",(poderes[compra][0]))
                    time.sleep(3)
                    break
                elif gramos <= 0:
                    print("Cantidad muy baja")
                    continue
                elif gramos > (poderes[compra][0]):
                    print("Stock insuficiente para la venta")
                    continue
            except ValueError:
                print("Ingrese un número válido")
        else:
            print("Ese producto no existe, escribalo correctamente")
            continue
    return poderes

def stockdis(poderes):
    print("Productos disponibles:")
    for producto in poderes:
        print(producto,"-",poderes[producto][0], "gr")
    time.sleep(3)
    print("")