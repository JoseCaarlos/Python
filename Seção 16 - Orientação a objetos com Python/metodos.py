"""
POO - Métodos

Em Python, dividimos os métodos, em 2 grupos: Método de Instância
e Métodos de Classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor
e sua função é construir o objeto a partir da classe.

OBS: Todo o elemento em Python que inicia e finaliza com duplo underline
é chamado de dunder (Double underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO! Por mais que possamos nossas próprias funções utilizando o dunder (underline no inicio e no fim)
não é aconselhado. Python possui vários métodos com está forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da Linguagem. Então, evite ao maximo. De preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palabras separadas por underline

p1 = Produto('PlayStation 4', 'Video Game', 2300)
print(p1.desconto(50))

print(Produto.desconto(p1, 40))  # self, desconto

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail,com', '654321')

print(user1.nome_completo())

print(Usuario.nome_completo(user1))

print(user2.nome_completo())

print(f'Senha: {user1._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

print(f'Senha: {user2._Usuario__senha}')  # Acesso de forma errada de um atributo de classe

"""

class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

class ContaCorrente:

    contador = 1234

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero

class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor de produto com o desconto"""
        return (self.__valor * (100 - porcentagem)) / 100

from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:

    def __init__(self, nome, sobrenome, email, senha):
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.encrypt(senha, rounds=200000, salt_size=16)  # Rounds gera 200.000 embraralhamento, salt_size -> Tamanho
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

nome = input('Informe nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o e-mail: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:

    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere')
    exit(42)

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')

print(f'Senha User Criptografada: {user._Usuario__senha}')  #  Acesso Errado