from curses.ascii import isdigit
import re
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

def verificarNombre():
        largo=False
        while largo==False :
            usuario1.nombre =str(input('Ingrese nombre: '))
            if len(usuario1.nombre) >=6 and len(usuario1.nombre)<=12:
                largo=True
            else:
                print('Su nombre debe tener entre 6 y 12 caracteres ')

def verificarApellido():
        largo=False
        while largo==False :
            usuario1.apellido =str(input('Ingrese apellido: '))
            if len(usuario1.apellido) >=6 and len(usuario1.apellido)<=12:
                largo=True
            else:
                print('Su apellido debe tener entre 6 y 12 caracteres ')

def verificarContraseña():
        largo=False
        numeros=False
        mayus=False
        minus=False
        while largo==False or minus==False or numeros==False or mayus==False:
            usuario1.contraseña =str(input('Ingrese contraseña: '))
            if len(usuario1.contraseña) >= 6:
                largo=True
                if any(chr.isdigit() for chr in usuario1.contraseña):
                    numeros=True
                    if any(chr.islower() for chr in usuario1.contraseña ):
                        minus=True
                        if any(chr.isupper() for chr in usuario1.contraseña):
                            print('Contraseña correcta')
                            mayus=True
                        else:
                            print('Su contraseña debe tener al menos una mayuscula')
                    else:
                        print('Su contraseña debe tener al menos una minuscula')
                else:
                    print('Su contraseña debe tener al menos un numero')
            else:
                print('Su contraseña debe tener al menos 6 caracteres')

def validate_email(arg_email):
        EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
        is_valid = False if not EMAIL_REGEX.match(arg_email) else True
        print("Direccion de correo valida" if is_valid else "Direccion de correo invalida.")

usuario1 = Usuario('','','','')

print('BIENVENIDO A LA  MATRIX \n')
print('Si toma la pildora roja podra ingresar ,si elije la azul su vida seguira normalmente')

menu=input('cual desea tomar ?: ')


while menu!='roja' and menu!='azul':
    print('debe tomar una decision')
    menu=input('cual desea tomar ?: ')

if menu =='roja':
    print('debe registrarse en la matrix como user')

    verificarNombre()

    verificarApellido()

    usuario1.email=input('Ingrese su email: ')
    arg_email=usuario1.email
    validate_email(arg_email)


    verificarContraseña()


    print('Usuario generado correctamente :',usuario1)

elif menu=='azul':
    print('´´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶')
    print('´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´¶¶')
    print('´¶¶¶¶¶´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´¶¶')
    print('¶´´´´´¶´´´´¶¶´´´´´´¶¶´´´´¶¶´´´´´´´´´´¶¶')
    print('¶´´´´´¶´´´¶¶´´´´´´´¶¶´´´´¶¶´´´´´´´´´´´´¶¶')
    print('¶´´´´¶´´¶¶´´´´´´´´´¶¶´´´´¶¶´´´´´´´´´´´´´¶¶')
    print('¶´´´¶´´´¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶')
    print('¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶')
    print('¶´´´´´´´´´´¶´´´¶¶´´´´´´´´´´´´´´¶¶´´´´´´´´¶¶')
    print('¶¶´´´´´´´´´¶´´´´¶¶´´´´´´´´´´´´¶¶´´´´´´´´´¶¶')
    print('¶¶´´´´¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´¶¶´´´´´´´´´¶¶')
    print('¶´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶')
    print('¶¶´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶')
    print('¶¶´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´¶¶')
    print('¶¶´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶')
    print('´¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´¶¶')
    print('´´´´´´´´´´´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶)')


