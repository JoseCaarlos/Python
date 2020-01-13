"""
Exercicio 01
"""

class Pessoa:

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura

    def imprimir_dados(self):
        print(f'Nome: {self.__nome}'
              f'\nIdade: {self.__idade}'
              f'\nAltura: {self.__altura}')

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getIdade(self):
        return self.__idade

    def setIdade(self, idade):
        self.__idade = idade

    def getAltura(self):
        return self.__altura

    def setAltura(self, altura):
        self.__altura = altura

p1 = Pessoa("José Carlos", 20, 1.65)

# p1.imprimir_dados()


"""
Exercicio 02
"""

class Agenda:

    listaAgenda = []

    @classmethod
    def buscaPessoa(cls, nome):
        pessoa = [p for p in cls.listaAgenda if p.__nome == nome]
        index = cls.listaAgenda.index(pessoa[0])
        print(f"O Index da(a) {nome} é : {index}")

    @classmethod
    def imprimePessoa(cls, index):
        pessoa = cls.listaAgenda[index]
        print(f'Nome: {pessoa.__nome}'
              f'\nIdade: {pessoa.__idade}'
              f'\nAltura: {pessoa.__altura}\n\n')

    @classmethod
    def removePessoa(cls, nome):
        pessoa = list(filter(lambda x: x.__nome == nome, cls.listaAgenda))
        print(pessoa)
        index = cls.listaAgenda.index(pessoa[0])
        cls.listaAgenda.pop(index)
        print(f'O {nome} foi apagado com sucesso !!!')

    @classmethod
    def teste(cls):
        pessoa = [p for p in cls.listaAgenda]
        print(pessoa)
        return list(filter(lambda x: x.__nome == "José Carlos", cls.listaAgenda))

    @staticmethod
    def imprimeAgenda():
        for pessoa in Agenda.listaAgenda:
            print(f'Nome: {pessoa.__nome}'
                  f'\nIdade: {pessoa.__idade}'
                  f'\nAltura: {pessoa.__altura}\n\n')

    def __init__(self, nome, idade, altura):
        self.__nome = nome
        self.__idade = idade
        self.__altura = altura
        Agenda.listaAgenda.append(self)

p1 = Agenda('José Carlos', 20, 1.69)
p2 = Agenda('Joao Pedro', 22, 1.65)
p3 = Agenda('Gabriela', 19, 1.69)
p4 = Agenda('Alyne', 25, 1.56)
p5 = Agenda('Daniel', 23, 1.78)
p6 = Agenda('Pedro', 29, 1.80)
p7 = Agenda('Bruno', 28, 1.72)

"""
# Agenda.imprimeAgenda()
# Agenda.buscaPessoa("Alyne")

# print(Agenda.imprimi())
print(Agenda.listaAgenda)
# print(Agenda.imprimePessoa("Alyne"))
Agenda.buscaPessoa("Alyne")
Agenda.imprimePessoa(2)
Agenda.removePessoa("Alyne")

"""
Agenda.removePessoa("Alyne")