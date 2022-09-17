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
    
    @apellido.setter
    def apellido(self,apellido):
        self.__apellido = apellido
        
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,valor):
        self.__email = valor
        
    @property
    def contraseña(self):
        return self.__contraseña
    
    @contraseña.setter
    def contraseña(self,valor):
        self.__contraseña = valor
        
    def __str__ (self):
        return 'Nombre: '+ str(self.__nombre)+ ', Apellido : '+ str(self.__apellido)+', Email: '+ str(self.__email) +', Contraseña: '+ str(self.__contraseña)
    
 
usuario1 = Usuario('fran','alcoba','fran@fran','contraseña')

print('BIENVENIDO A LA  MATRIX \n')
print('Si toma la pildora roja podra ingresar ,si elije la azul su vida seguira normalmente')

menu=input('cual desea tomar ?: ')

    
while menu!='roja' and menu!='azul':
    print('debe tomar una decision')
    menu=input('cual desea tomar ?: ')

if menu =='roja':
    print('debe registrarse en la matrix como user')
    
              
elif menu=='azul':    
    print('continua con su vida normal')

