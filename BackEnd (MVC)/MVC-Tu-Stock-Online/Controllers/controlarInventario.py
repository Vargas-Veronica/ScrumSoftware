#Acceso rol administrador

#Ingreso producto()

def añadir_producto(self, producto, cantidad):
    if not isinstance (producto, producto):
        raise Exception("añadir_producto: producto debe ser de la clase Producto")
    
    if not isinstance (cantidad, int):
        raise Exception("añadir_producto: cantidad debe ser un numero ")

    if cantidad <= 0:
        raise Exception("añadir_producto: cantidad debe ser mayor a cero")

    if producto in self.productos :
        indice = self.producto.index(producto) 
        self.cantidadDeVentas[indice] += cantidad
    else:
        self.cantidadDeVentas.append(cantidad) 
        self.productos.append(producto)   

#Editar producto()

#Eliminar producto()

def eliminar_producto(self, producto):
    if not isinstance (producto, producto):
        raise Exception("eliminar_producto: Producto debe ser de la clase Producto")

    if producto in self.productos: 
       indice = self.productos.index(producto)
       del self.productos[indice]
       del self.cantidadDeVentas[indice]    
    else:
        raise Exception("eliminar_producto: El producto no existe") 

   


#Filtrar producto()

#Informe de inventario()






#Acceso rol administrador

#Ingreso producto()

#Editar producto()

#Eliminar producto()

#Filtrar producto()

#Informe de inventario()


