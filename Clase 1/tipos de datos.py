# Strings
a ='ESTO es una cadena'
b ='esto es otra cadena'

print(a,type(a))
print(b,type(b))

c =str(1000)
print(c,type(c))

#len mide logituid
print(len(a))

#indices   eligen cual caracter mostrar comenzando desde el cero
print(a[0:3])
#para mostrar de atras para adelante
print(a[-1])


#Metodos
print(a.lower()) #minuscula

print(a.upper()) #mayuscula

print(a.split()) # sepera por poalabras

#List
lista_1=['hola',1,2.5,True,[1,2,3,4,],(a,b)]
print(lista_1)
print(type(lista_1))
print(len(lista_1))
print(lista_1[2])

var_1=lista_1[4]
print(var_1)
print(type(var_1))

#Metodos
lista_1.append('fran')
print(lista_1)

print (lista_1.index((a,b)))

lista_1.insert(3,'juan')
print(lista_1)

#Diccionario
usuario ={
    'nombre':'Fran',
    'apellido':'alcoba',
    'años':33,
    'hobbies':['rock', 'blues']
}

print(usuario['apellido'])
#metodos
keys_usuario= list(usuario.keys())
print(type(keys_usuario))
print(usuario.get(keys_usuario[0]))
print(usuario.values())
