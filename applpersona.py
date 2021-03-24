class persona:
    
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
               
persona1=persona("carlos ortega",30)
persona2=persona("juan ortega",10)

print(persona1.nombre)
print(persona1.edad)

if persona1.edad > persona2.edad:
    print(persona1.nombre, "es mayor....")
    
