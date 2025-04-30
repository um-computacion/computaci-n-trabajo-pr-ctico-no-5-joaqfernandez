import unittest
from src.alumno import Alumno

class testAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Pepe", "Ramon", 21, 421235, 123)
        self.assertEqual = alumno.nombre = "Pepe" 
        self.assertEqual = alumno.apellido = "Ramon"
        self.assertEqual = alumno.edad = 21
        self.assertEqual = alumno.dni = 421235
        self.assertEqual = alumno.legajo = 123

    