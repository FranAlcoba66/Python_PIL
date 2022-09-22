def err(e):
    print("Error: " + e + " !")

contrasena = str(input("Ingresa una contraseña: "))

def run(contrasena):


      if len(contrasena) >= 6:

        if any(chr.isdigit() for chr in contrasena):

          if any(chr.islower() for chr in contrasena ):

            if any(chr.isupper() for chr in contrasena):
              print("Contraseña valida")

            else:
                  err("Debe incluir al menos una mayuscula")

          else:
                err("Debe incluir al menos una minuscula")

        else:
              err("Faltan numeros")

      else:
          err("Contraseña demasiado corta")

run()