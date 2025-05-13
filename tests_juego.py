import unittest
from juego import comparar

class TestJuego(unittest.TestCase):

    #Empates 
    def piedra_vs_piedra(self):
        self.assertEqual(comparar("piedra", "piedra"), 0)

    def papel_vs_papel(self):
        self.assertEqual(comparar("papel", "papel"), 0)

    def tjiera_vs_tijera(self):
        self.assertEqual(comparar("tijera", "tijera"), 0)

    #Ganador humano
    def piedra_vs_tijera(self):
        self.ssertEqual(comparar("piedra", "tijera"), 1)

    def papel_vs_piedra(self):
        self.assertEqual(comparar("papel", "piedra"), 1)

    def tijera_vs_papel(self):
        self.assertEqual(comparar("tijera", "papel"), 1)

    #Ganador programa
    def piedra_vs_papel(self):
        self.assertEqual(comparar("piedra", "papel"), -1)

    def papel_vs_tijera(self):
        self.assertEqual(comparar("papel", "tijera"), -1)

    def tijera_vs_piedra(self):
        self.assertEqual(comparar("tijera", "piedra"), -1)

if __name__ == "__main__":
    unittest.main()