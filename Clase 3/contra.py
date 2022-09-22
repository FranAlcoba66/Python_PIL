
def verificarContraseña():

    largo=False
    numeros=False
    mayus=False
    minus=False
    while largo==False or minus==False or numeros==False or mayus==False:
        contraseña =str(input('Ingrese contraseña: '))
        if len(contraseña) >= 6:
            largo=True
            if any(chr.isdigit() for chr in contraseña):
                numeros=True
                if any(chr.islower() for chr in contraseña ):
                    minus=True
                    if any(chr.isupper() for chr in contraseña):
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

