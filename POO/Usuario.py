from xml.etree.ElementTree import tostring

class Usuario :
    def __init__(self,nombre,apellido,email,contraseña):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__email=email
        self.__contraseña=contraseña
        
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
        
    @property
    def apellido(self):
        return self.__apellido
    
    @nombre.setter
    def apellido(self,apellido):
        self.__apellido = apellido
        
    def __str__ (self):
        return 'Nombre: '+ str(self.__nombre)+ ', Apellido : '+ str(self.__apellido)+', Email: '+ str(self.__email) +', Contraseña: '+ str(self.__contraseña)
    
 
usuario1 = Usuario('fran','alcoba','fran@fran','contraseña')

print(usuario1) 
usuario1.nombre=('juan')
usuario1.apellido=('juan')
print(usuario1) 
print(usuario1.nombre)
print(usuario1.apellido)
print(usuario1.__email)

    


