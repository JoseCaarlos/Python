"""
POO - Herança (Inheritance)


A ideia de herança é de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classes existente nós extendemos outra classe que passa a herdar os
atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome
    - cpf
    - renda

Funcionario
    - nome
    - sobrenome
    - cpf
    - matricula

Perguntar: Existe uma entidade genérica suficientes para encapsular alguns métodos e atributos


class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.__nome = nome
        self.__cpf = cpf
        self.__sobrenome = sobrenome
        self.__renda = renda

    def nome_completo(self):
        print(f'O nome completo é: {self.__nome } { self.__sobrenome}')

class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.__nome = nome
        self.__cpf = cpf
        self.__sobrenome = sobrenome
        self.__matricula = matricula

    def nome_completo(self):
        print(f'O nome completo é: {self.__nome } { self.__sobrenome}')


c1 = Cliente('Gabriela','Lopes','715-154-545-787', 5000)
f1 = Funcionario('Jose','Carlos', '460-457-928-82', 5345641)

c1.nome_completo()
f1.nome_completo()


OBS: Quando uma classe herda de outra classe ela herda todos métodos e atributos da classe herdada.

Quando uma classe herda de outra classe, a classe herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Base;
    - Classe Genérica

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente][Funcionario]
    - Sub Classe
    - Classe Filha
    - Classe Específica

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    #Cliente herda de Pessoa
    def __init__(self,nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma NÃO comum de acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa):
    #Funcionario herda de Pessoa
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar a super classe
        self.__matricula = matricula


c1 = Cliente('Gabriela','Lopes','715-154-545-787', 5000)
f1 = Funcionario('Jose','Carlos', '460-457-928-82', 5345641)

print(c1.nome_completo())
print(f1.nome_completo())

# Sobrescrita de Métodos (Overriding)

"""

class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

class Cliente(Pessoa):
    """Cliente herda de Pessoa"""
    def __init__(self,nome, sobrenome, cpf, renda):
        Pessoa.__init__(self, nome, sobrenome, cpf)  # Forma NÃO comum de acessar a super classe
        self.__renda = renda

class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""
    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)  # Forma comum de acessar a super classe
        self.__matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())
        print(self._Pessoa__cpf)
        return f'Funcionário: {self.__matricula} \nNome: {self._Pessoa__nome}'

# Sobrescrita de Métodos (Overriding)

c1 = Cliente('Gabriela','Lopes','715-154-545-787', 5000)
f1 = Funcionario('Jose','Carlos', '460-457-928-82', 5345641)

print(c1.nome_completo())
print(f1.nome_completo())