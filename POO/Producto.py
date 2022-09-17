from xml.etree.ElementTree import tostring


class Producto:
    def __init__(self,codigo,nombre,precio):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio 
        
    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,valor):
        self.__codigo = valor
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,valor):
        self.__nombre = valor 
    
    @property
    def precio(self):
        return self.__precio
    
    @precio.setter
    def precio(self,valor):
        self.__precio = valor 
    
    def __str__ (self):
        return 'Codigo: '+ str(self.__codigo)+ ', Nombre : '+ str(self.__nombre)+', Precio: '+ str(self.__precio)
    
    def calcularTotal(self,unidades):
        return self.precio*unidades 

class Pedido:
   
    
    def __init__(self,productos,cantidades) -> None:
        self.__productos =productos
        self.__cantidades=cantidades
        
    def totalPedido(self):
        total=0
        
        for (p,c) in zip(self.__productos ,self.__cantidades):
            total = total + p.calcularTotal(c)
            return total

    def mostrarPedido(self):
        for (p,c) in zip(self.__productos, self.__cantidades):
            print('Producto: ' + p.get + ', Cantidad: ' + str(c))


                  
p1 = Producto (1,'Producto1',5)
p2 = Producto (2,'Producto1',10)
p3 = Producto (3,'Producto1',20)

print(p1.nombre)
print(p2)
print(p3)

print(p1.calcularTotal(5))
print(p2.calcularTotal(5))
print(p3.calcularTotal(5))

productos =[p1,p2,p3]
cantidades =[5,2,3]

precio = (productos,cantidades)

pedido = Pedido(productos,cantidades)

print( 'El total del pedido es: '+str(pedido.totalPedido()))

print(pedido.mostrarPedido())