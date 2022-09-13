def run():
    contrasena = str(input("Ingresa una contraseña: "))
      


    if  len(contrasena) >=6:
        print("Contraseña valida")
    else :
        print("Contraseña invalida")


if __name__ == '__main__':
    run()