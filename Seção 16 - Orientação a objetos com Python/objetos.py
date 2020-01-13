"""
POO - Objetos

Objetos -> Instâncias da classe. OU seja, após o mapeamento do objeto do mundo real para sua
representação computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar
nos objetos/instâncias de uma classe como variáveis do tipo definido na classe.

# Instância ou Objeto

lamp1 = Lampada('branca', 110, 60)

print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A lâmpada está ligada? {lamp1.checa_lampada()}')


cc1 = ContaCorrente(5000, 20000)

user = Usuario('jose', 'carlos', 'josecarlos10967@gmail.com', '123456')
"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True

class Cliente:


    def __init__ (self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente {self.__nome}')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__id = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__id

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha


cliente = Cliente('Jose', '46045792882')

cc1 = ContaCorrente(5000, 20000, cliente)

cc1.mostra_cliente()

cc1._ContaCorrente__cliente.diz()
