import unittest
from src.persona import Persona

class testPersona(unittest.TestCase):
    def test_persona(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        self.assertEqual(persona.nombre, "Joaquin")
        self.assertEqual(persona.apellido, "Fernandez")
        self.assertEqual(persona.edad, 21)
        self.assertEqual(persona.dni, 423312351)
        self.assertEqual(persona.pensamiento, 0)
        self.assertEqual(persona.ultima_idea, "<Aun no piensa>")

    def test_repr_persona(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        expected_repr = "Persona: Joaquin Fernandez. Edad: 21 DNI: 423312351 Ultima idea: <Aun no piensa>"
        self.assertEqual(str(persona), expected_repr)

    def test_persona_pensante(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        persona.pensar("pienso una vez")
        self.assertEqual(persona.pensamiento, 1)
    
    def test_persona_actualiza_pensamientos(self):
        persona = Persona("Joaquin", "Fernandez", 21, 423312351)
        persona.pensar("pienso una vez")
        self.assertEqual(persona.ultima_idea, "pienso una vez")
        persona.pensar("pienso dos veces")


if __name__ == '__main__':
    unittest.main()