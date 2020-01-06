"""
POO - Method Resolution Order - MRO

Method Resolution Order (Resoluçao de Orde de Métodos), é a Ordem de execução dos métodos (Quem vem primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3 formas:
     - Via propriedade da Classe __mro__
     - Via método mro()
     - Via help
"""

class Animal:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comprimentar(self):
        return f'Eu sou o {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'{self.nome} está nadando'

    def comprimentar(self):
        return f'Eu Sou {self.nome} do MAR'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'{self.nome} está andando'

    def comprimentar(self):
        return f'Eu Sou {self.nome} da Terra'

class Pinguim( Terrestre,Aquatico):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

tux = Pinguim('Tux')
print(tux.comprimentar())  # Eu Sou Xum da Terra / Eu Sou Tux do MAR ???? Method Resolution Order - MRO
print(tux.mro())
"""
Pinguim(Aquatico, Terrestre)
Eu Sou Tux do MAR

Pinguim( Terrestre,Aquatico)
Eu Sou Tux da Terra
"""