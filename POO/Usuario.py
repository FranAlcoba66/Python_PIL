from xml.etree.ElementTree import tostring

class Usuario :
    def __init__(self,nombre,apellido,email,contraseña):
        self.nombre=nombre
        self.apellido=apellido
        self.email=email
        self.contraseña=contraseña
        
    def __str__ (self):
        return 'Nombre: '+ str(self.nombre)+ ', Apellido : '+ str(self.apellido)+', Email: '+ str(self.email) +', Contraseña: '+ str(self.contraseña)
    
    


    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def setNombre(self,valor):
        self.__nombre = valor
 
 
usuario1 = Usuario('francisco','alcoba','fran@fran','contraseña')
usuario2 = Usuario('ro','andrada','@rocio','ro5645')
usuario3 = Usuario('coti','cortez ','@gmail','ro5645')
print(usuario1)     
usuario1.__nombre('juan')
print(usuario1)

