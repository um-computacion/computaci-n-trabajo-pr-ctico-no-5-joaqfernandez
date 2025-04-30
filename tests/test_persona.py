import unittest

class testPersona(unittest.TestCase):
    def test_persona(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        self.assertEqual(persona.nombre, "Joaquin")
        self.assertEqual(persona.apellido, "Fernandez")
        self.assertEqual(persona.edad, 21)
        self.assertEqual(persona.dni, 423312351)

    def repr_persona(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        expected_repr = "Persona: Joaquin Fernandez. Edad: 21. DNI: 423312351"
        self.assertEqual(repr(persona), expected_repr)