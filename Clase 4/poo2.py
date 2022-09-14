class Animal:
    
    
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad =edad
    
    def hablar(self,sonido):
        print(sonido)
    
        
    
    
    
class Perro(Animal):
    
    #Constructor
    def __init__(self,nombre,raza,especie,edad) :
    #Atruibutos de instancia(equivalente de variables locales o propias de una funcion/metodo en este caso del objeto)
        self.nombre=nombre
        self.raza=raza
        super().__init__(especie,edad)
        
    #Metodos
    def saludar(self):
        print(f'{self.nombre} dio la pata')
    
perro_1= Perro ('Juanito','bulldog','canino',5)
print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza},{perro_1.especie} ,{perro_1.edad} ')
perro_1.saludar()
perro_1.hablar('guauuu')

