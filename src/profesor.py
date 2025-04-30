from .persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, dni, sueldo):
        super().__init__(nombre, apellido, edad, dni)
        self.sueldo = sueldo
        
    