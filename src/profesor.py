from .persona import Persona

class Profesor(Persona):
    def __init__(self, nombre, apellido, edad, dni, sueldo):
        super().__init__(nombre, apellido, edad, dni)
        self.sueldo = sueldo
        
    def __repr__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Edad: {self.edad}, DNI: {self.dni}, Sueldo: {self.sueldo}"