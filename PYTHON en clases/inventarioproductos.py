


stock = {
    "Teclado" : [5,25000]

}

nombremayor = None
mayor = 0


stock["Mouse"]= [10,15000,"hola"]
del stock["Mouse"]
for producto,datos in stock.items() :
    print(producto,datos)
    if datos[1] > mayor:
        mayor = datos[1]
        nombremayor = producto


dicc = {
    "1"
}

for datos[1] 