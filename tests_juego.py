import unittest
from juego import comparar

class TestJuego(unittest.TestCase):
    def test_piedra_vs_tijera(self):
        self.assertEqual(comparar('piedra', 'tijera'), 1)

    def test_piedra_vs_papel(self):
        self.assertEqual(comparar('piedra', 'papel'), -1)

    def test_piedra_vs_piedra(self):
        self.assertEqual(comparar('piedra', 'piedra'), 0)

    def test_tijera_vs_papel(self):
        self.assertEqual(comparar('tijera', 'papel'), 1)

    def test_tijera_vs_piedra(self):
        self.assertEqual(comparar('hola', 'piedra'), -1)

    def test_tijera_vs_tijera(self):
        self.assertEqual(comparar('tijera', 'tijera'), 0)

    def test_papel_vs_piedra(self):
        self.assertEqual(comparar('papel', 'piedra'), 1)

    def test_papel_vs_tijera(self):
        self.assertEqual(comparar('papel', 'tijera'), -1)

    def test_papel_vs_papel(self):
        self.assertEqual(comparar('papel', 'papel'), 0)

if __name__ == '__main__':
    unittest.main()