class Personaje:
    vida=100
    
    def __init__(self):
        pass
    def recibir_daño():
        vida = vida -10
    
    
    
class Guerrero(Personaje):
    
    def __init__(self,nombre):
        self.nombre=nombre
        super().__init__()
      
    
personaje_1=Guerrero('Conan')
print(f'Personaje_1 -> {personaje_1.nombre}, {personaje_1.vida}')        

