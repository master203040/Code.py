class alumno:
    
    def __init__(self,nombre,nota):
        self.nombre=nombre
        self.nota=nota
        
    def imprir(self):
        print ("Alumno",self.nombre)
        print ("Nota",self.nota)
        print("")
        
    def resultado(self):
        if self.nota < 5:
            print("el alumno ha reprobado")
        else:
            print("el alumno ha aprobado")
            
alumno1=alumno("diego",10)
alumno2=alumno("sofia",3)

alumno1.imprir()
alumno1.resultado()

alumno2.imprir()
alumno2.resultado()
        
        
        