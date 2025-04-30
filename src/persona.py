class Persona():
    def __init__(self, nombre, apellido, edad, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni
        
    def __repr__(self):
        return f"Persona: {self.nombre} {self.apellido}. Edad: {self.edad} DNI: {self.dni}"