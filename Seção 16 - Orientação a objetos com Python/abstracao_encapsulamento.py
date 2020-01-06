"""
POO - Abstração e Encapsulamento

Grande Objeto da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -> Capsula

        Classe
----------------------
/                    /
/    Atributos       /
/    Métodos         /
_____________________

$ Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo
privado chamado __nome é um método privado
chamado __falar()

Esse elementos privados só devem/deveriam ser acessdos dentro da classe. Mas o Python não o bloqueia este acesso
fora da classe. Com python acontece o fenômeno chamado Name Manglin, que faz uma alteração na forma de se
acessar os elementos privados, conforme:

_Clase__elemento

Exemplo - Acessando elementos privados fora da classe:

instância._Pessoa__nome
instância._Pessoa__falar()

Abstração, em POO, é o fato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

print(conta1.__dict__)
conta1.depositar(-300)
print(conta1.__dict__)

conta1.sacar(2000)

"""

class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def extrato(self):
        print(f'Saldo de {self.__saldo} do titular {self.__titular} com limite de {self.__limite}')

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print('O valor precisa ser positivo')

    def sacar(self, valor):
        if valor > 0:
            if self.__saldo >= valor :
                self.__saldo -= valor
            else:
                print('O valor de saque é maior que seu SALDO DISPONIVEL')
        else:
            print('O valor precisa ser positivo')

    def transferencia(self, valor, conta):
        if valor > 0:
            if self.__saldo >= valor:
                conta.__saldo += valor
                self.__saldo -= valor

            else:
                print('O valor de transferência é maior que seu SALDO DISPONIVEL')
        else:
            print('O valor precisa ser positivo')


# Testando

conta1 = Conta('Geek', 150.00, 1500)
conta2 = Conta('Felicity', 150.00, 1500)

conta1.transferencia(100, conta2)

print(conta1.__dict__)
print(conta2.__dict__)

