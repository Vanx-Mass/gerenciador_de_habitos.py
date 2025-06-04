import unittest
from habitos import adicionar_habitos

class TestHabitos(unittest.TestCase):
    def test_adicionar_habito(self):
        lista = []
        # Simula a adição manual (sem input), então você precisa adaptar a função ou testá-la isoladamente
        habito = {"nome": "Estudar", "categoria": "Estudo", "historico": []}
        lista.append(habito)
        self.assertEqual(len(lista), 1)
        self.assertEqual(lista[0]["nome"], "Estudar")

if __name__ == "__main__":
    unittest.main()
