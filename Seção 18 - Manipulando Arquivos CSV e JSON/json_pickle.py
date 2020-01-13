"""
Json e Pickle

JSON -> Javascript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas
(Twitter, Facebook, YouTube...)

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        return self.__raca

felix = Gato("felix", "gius")

print(felix.__dict__)

ret = json.dumps(felix.__dict__)

print(ret)

Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        return self.__raca

felix = Gato("felix", "gius")

ret = jsonpickle.encode(felix)

print(ret)

# Escrevendo o arquivo JSON/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        return self.__raca

felix = Gato("felix", "gius")

with open('felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)
"""
# Lendo o arquivo JSON/pickle

import jsonpickle

class Gato:

    def __init__(self, nome, raca):
        self.__nome = nome
        self.__raca = raca

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        return self.__raca

with open('felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(ret.nome)
    print(ret.raca)