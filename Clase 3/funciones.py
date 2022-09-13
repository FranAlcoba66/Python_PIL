#funciones bloque de codigo reutilizable
# nombre, argumentos ,codigo y retorno




numero = 1


def sumar(a,b):
    resultado=a+b
    return resultado
#forma de printear la funcion 1
resulta_suma= sumar(2,3)
print(resulta_suma)
#forma de  funcion 2
print(sumar(3,4))


#funcion  sin parametro
def resta():    
    resultado=2-3
    return resultado

print(resta())

#funcion sin parametro 2
def resta2():
    print(2-3)
  
resta2()

def saludo(cantidad_saludos):
    """_summary_

    Args:
        cantidad_saludos (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    lista_nombres=[]
    
    for i in range(cantidad_saludos):
        
        nombre=input('Ingrese su nombre')
        print('Hola',nombre)

        lista_nombres.append(nombre)

    print(lista_nombres)  
    return lista_nombres

def orden(lista,sentido):
    lista.sort(reverse=sentido)
    return lista
    
           
nombres=saludo(int(input('Ingrese la cantidad de saludos a efectuar')))    

print(
    orden(nombres,True)
    )

 