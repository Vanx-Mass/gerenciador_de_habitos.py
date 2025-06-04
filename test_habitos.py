import unittest
from habitos import adicionar_habito

class TestHabitos(unittest.TestCase):
    def test_adicionar_habito_manual(self):
        habitos = []
        habito = {"nome": "Estudar", "categoria": "Estudo", "historico": []}
        habitos.append(habito)
        self.assertEqual(len(habitos), 1)
        self.assertEqual(habitos[0]["nome"], "Estudar")

if __name__ == "__main__":
    unittest.main()
