"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsualar nesse código dentro de um grupo lógico e hierarquico utilizavel
classes.

Encapsular -> Cápsula

# Relembrando Atributos/Métodos privados em Pyhton

Imagine que temos uma classe chamada Pessoa, contendo um
atributo privado chamado __nome e um método privado
chamado __falar()

Para poder acessar fora da classe utiliza-se o comando

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe:

instancia._Pessoa__nome

instancia._Pessoa__falar()

Abstração, em POO, é o ato de expor dados relevantes de uma classe, escondendo atributos e métodos
privados de Usuário.

print(conta1.__dict__)

conta1.extrato()

print(conta1._Conta__titular)  # Name Mangling

conta1._Conta__titular = 'Angelina'

print(conta1.__dict__)

print(conta1.__dict__)

conta1.depositar(-150)

conta1.sacar(15000)

print(conta1.__dict__)

"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador + 1
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador = self.__numero

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')
    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor:
                self.__saldo -= valor
            else:
                print('Saldo insuficiente')
                print('O valor precisa ser positivo')
        else:
            print('O valor deve ser positivo')
    def transferir(self, valor, conta_destino):
        # 1 - Remover o valor da conta de origem
        self.__saldo -= valor
        self.__saldo -= 10  # Taxa de transferência paga por quem realizou a transferência


        # 2 - Adicionar o valor na conta de destino
        conta_destino.__saldo += valor

# Testando
conta1 = Conta('Geek', 150.00, 1500)
conta1.extrato()

conta2 = Conta('Felicity', 300, 2000)
conta2.extrato()

conta2.transferir(100, conta1)

conta1.extrato()
conta2.extrato()