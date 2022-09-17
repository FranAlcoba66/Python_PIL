

def run():
    contrasena = str(input("Ingresa una contraseña: "))
    while contrasena == False:
        if len(contrasena) >= 6:
            
            if any(chr.isdigit() and chr.islower() and chr.isupper() for chr in contrasena):
                return True
            else:
                print ('contrasena incorrecta')
        else:      
            print ('contrasena incorrecta')      
            
run()