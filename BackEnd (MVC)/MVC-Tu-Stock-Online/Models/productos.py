class Producto:
    codigo = ""
    nombre = ""
    marca = ""
    categoria = ""
    descripcion = ""
    precioDeVenta = ""
    cantidadPorBulto = ""
    fechaDeVencimiento = ""
    foto = ""

    def __init__(self, codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDeVencimiento, foto):
         self.codigo = codigo
         self.nombre = nombre
         self.marca = marca
         self.categoria = categoria
         self.descripcion = descripcion
         self.precioDeVenta = precioDeVenta
         self.cantidadPorBulto  = cantidadPorBulto
         self.fechaDeVencimiento = fechaDeVencimiento
         self.foto  = foto

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo



    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre



    def get_marca(self):
        return self.marca
   
    def set_marca(self, marca):
        self.marca = marca
     
     
    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria

        
    def get_descripcion(self):
        return self.descripcion_

    def set_descripcion(self, descripcion):
        self.descripcion = descripcion    
        
   
    def get_precioDeVenta(self):
        return self.precioDeVenta

    def set_precioDeVenta(self, precioDeVenta):
        self.precioDeVenta = precioDeVenta    
    

    def get_cantidadPorBulto(self):
        return self.cantidadPorBulto

    def set_cantidadPorBulto(self, cantidadPorBulto):
        self.cantidadPorBulto = cantidadPorBulto   

        
    def get_fechaDeVencimiento(self):
        return self.fechaDeVencimiento

    def set_fechaDeVencimiento(self, fechaDeVencimiento):
        self.fechaDeVencimiento = fechaDeVencimiento
   
        
    def get_foto(self):
        return self.foto

    def set_foto(self, foto):
        self.foto = foto
      
                     
    
    def __init__(self, codigo, nombre, marca, categoria, descripcion, precioDeVenta, cantidadPorBulto, fechaDeVencimiento, foto):
         self.codigo = codigo
         self.nombre = nombre
         self.marca = marca
         self.categoria = categoria
         self.descripcion = descripcion
         self.precioDeVenta = precioDeVenta
         self.cantidadPorBulto  = cantidadPorBulto
         self.fechaDeVencimiento = fechaDeVencimiento
         self.foto = foto


     