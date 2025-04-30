import unittest
from src.profesor import Profesor

class testProfesor(unittest.TestCase):
    def test_profesor(self):
        profesor = Profesor("Lionel", "Messi", 37, 1290324, 500)
        self.assertEqual(profesor.nombre, "Lionel")
        self.assertEqual(profesor.apellido, "Messi")
        self.assertEqual(profesor.edad, 37)
        self.assertEqual(profesor.dni, 1290324)
        self.assertEqual(profesor.sueldo, 500)
