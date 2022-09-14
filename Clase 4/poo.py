class Animal:
    
    
    def __init__(self,especie,edad):
        self.especie=especie
        self.edad =edad
    
    def hablar(self):
        pass
    
        
    
    
    
class Perro():
    #Atributo goblal
    especie= 'mamiferos'
    
    #Constructor
    def __init__(self,nombre,raza) -> None:
        #Atruibutos de instancia(equivalente de variables locales o propias de una funcion/metodo en este caso del objeto)
        self.nombre=nombre
        self.raza=raza
    def ladrar(self):
        print('Guau')    
    def jugar(self,objeto):
        print('El perro esta jugando con',objeto)
    def saludar(self):
        print('Gauu me llamo',self.nombre)
        
    
perro_1= Perro ('Juanito','bulldog')
print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza}, {perro_1.especie}')
perro_1.ladrar
perro_1.jugar('Pelota')
perro_1.saludar()
perro_2= Perro ('Gordo','Dogo')
print(f'Perro_2 -> {perro_2.nombre}, {perro_2.raza}, {perro_2.especie}')
perro_2.saludar()

