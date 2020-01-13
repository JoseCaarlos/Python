import unittest

from atividades import comer, dormir, eh_engracada

# https://docs.python.org/3/library/unittest.html

class AtividadesTestes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável"""
        self.assertEqual(
            comer('quiabo', True),
            'Estou comendo quiabo por que quero manter a forma'
        )

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa"""
        self.assertEqual(
            comer(comida='pizza', saudavel=False),
            'Estou comendo pizza por que a gente só vive uma vez'
        )

    def test_dormir_pouco(self):
        """Testando o retorno com dormir pouco"""
        self.assertEqual(
            dormir(4),
            'Continuo cansado após dormir por 4 horas. :('
        )

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito"""
        self.assertEqual(
            dormir(10),
            'Putz dormir muito! Estou atrasado vou me atrasar :( '
        )

    def test_eh_engracada(self):
        """Testando o retorno eh_engracada"""
        #self.assertEqual(eh_engracada('Sergio Malandro'), False)
        self.assertFalse(eh_engracada('Sergio Malandro'))
        self.assertTrue(eh_engracada('Jim Carry'), 'Jim Carrey deveria ser engraçado')

if __name__ == '__main__':
    unittest.main()