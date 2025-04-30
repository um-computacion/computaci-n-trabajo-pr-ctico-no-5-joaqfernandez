from .persona import Persona

class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, dni, legajo):
        super().__init__(nombre, apellido, edad, dni)
        self.legajo = legajo
        