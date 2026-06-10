#Agregar producto

def agregarproducto(dick,producnew,stocknew,precionew):
        dick[producnew] = [stocknew,precionew]
        print("PRODUCTO AGREGADO!")
        return dick

#Mostrar Producto

def mostrarproducto(dick):
        for nombre,stok,val in dick.items():
                print(nombre,stok,val)
        return


#Buscar productos



#Producto mas caro




