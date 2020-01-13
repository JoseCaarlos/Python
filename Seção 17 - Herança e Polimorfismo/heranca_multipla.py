"""
POO - Herança Múltipla

# OBS: A herança múçtipla pode ser feita de duas formas:
    - Por Multiderivação direta;
    - Por Multiderivação indireta;

# Exemplo 01 - Multiderivação Direta

class Base1:
    pass

class Base2:
    pass

class Base3:
    pass

class Multiderivada(Base1, Base2):
    pass


# Exemplo 2 - Multiderivação Indireta

class Base1:
    pass

class Base2(Base1):
    pass

class Base3(Base2):
    pass

class Multiderivada(Base3):
    pass

# OBS: Não importa se a derivação é direta ou indireta. A classe que realizar a herança todos os atributos
e métodos das super classe.

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

class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)

# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.comprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.comprimentar())

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
print(tux.comprimentar())  # Eu Sou Xum da Terra / Eu Sou Tux do MAR ???? Method Resolution Order - MRO


# Objeto é instância de ...
print(f'\n\n\nTux é instância de Pinguim ? {isinstance(tux, Pinguim)}')
print(f'Tux é instância de Aquatico ? {isinstance(tux, Aquatico)}')
print(f'Tux é instância de Terreste ? {isinstance(tux, Terrestre)}')
print(f'Tux é instância de object ? {isinstance(tux, object)}')