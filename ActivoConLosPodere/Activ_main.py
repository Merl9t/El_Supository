from Activ_func import venta,stockdis
poderes = {
    "Weed": [500,3000,2000],
    "Falopa":[1000,10000,5000]
}
while True:
    print("")
    print("---4CT1V0 C0N L0$ P0D3R3$---")
    print("")
    print("1.- Hacer venta")
    print("2.- Ver stock")
    print("3.- Agregar producto nuevo")
    print("4.- Recargar gramos")
    print("5.- Salir")
    print("")
    try:
        op = int(input("Ingrese opción: "))
    except ValueError:
        print("Ingrese número válido")
        continue
    if op not in [1,2,3,4,5]:
        print("Ingrese un número entre 1 y 5")
        continue
    if op == 1:
        print("")
        poderes = venta(poderes)
    elif op == 2:
        print("")
        stockdis(poderes)
    elif op == 3:
        print("agregar producto")
    elif op == 4:
        print("analisis")
    elif op == 5:
        print("Saliendo...")
        break