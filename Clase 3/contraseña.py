def err(e):
    print("Error: " + e + " !")

def run():

    contrasena = str(input("Ingresa una contraseña: "))
    # print(any(chr.islower() for chr in contrasena))#
    # numeros = False
    if len(contrasena) >= 6:
        if any(chr.isdigit() for chr in contrasena):
            if any(chr.islower() for chr in contrasena ):
              if any(chr.isupper() for chr in contrasena):
                print("tas pillo")
              else:
                err("Letras malas AAA")
            else:
              err("Letras malas aaa")
        else:
            err("Faltan numeros")
    else:
        err("Contraseña corta")

run()