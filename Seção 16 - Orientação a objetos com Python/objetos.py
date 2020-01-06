"""
POO- Objetos

Objetos -> São instâncias da classe, Ou seja, após o mapeamento do mundo real para sua representação computacionmal,
devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/intâncias de uma classe como variáveis
do tipo definido da classe

#Instância/Objetos
lamp1 = Lampada('branca', 110, 60)
print(f'A Lâmpada está ligada {lamp1._Lampada__cor}')

cc1 = ContaCorrente(5000, 2000)

nome = Usuario('Jose', 'Carlos', 'jose@gmail.com', '123456')
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
        if(self.__ligada):
            self.__ligada = false
        else:
            self.__ligada = True

class Cliente:

    def __init__(self, nome, cpf):
        self.__nome = nome
        self.__cpf = cpf

    def diz(self):
        print(f'O cliente é {self.__nome}')

class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo, cliente):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        self.__cliente = cliente
        ContaCorrente.contador = self.__numero

    def mostra_cliente(self):
        print(f'O cliente é {self.__cliente._Cliente__nome}')


class Usuario:
    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = senha

c1 = Cliente('jose', '46045792882')

cc1 = ContaCorrente(5000, 2000, c1)

cc1.mostra_cliente()
cc1._ContaCorrente__cliente.diz()
