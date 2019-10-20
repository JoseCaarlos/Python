'''
Quando uma linguagem de Programação suporte HOF (Highder Order Functions), indica que podemos ter funções
que retornamos outras funções como resultado ou mesmo que podemos passa funções
como argumentos para outras funções, e até mesmo criar variáveis do tipo de funções
nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen


# Exemplo - Definindo as Funções

def somar(a, b):
    return a + b

def diminuir(a, b):
    return  a - b

def multiplicar(a, b):
    return a * b

def dividir (a, b):
    return a / b

def calcular(num1, num2, funcao):
    return funcao(num1, num2)

#Testando todas as funções

print(calcular(4, 3, somar))

print(calcular(4, 3, diminuir))

print(calcular(4, 3, multiplicar))

print(calcular(4, 3, dividir))



# Nested Functions - Funções Aninhadas


# Em Python tbm podemos ter funções dentro de funções, que são conhecidas por
# Nested Functions ou também Inner Functions (Funções Internas).

# Exemplo

from random import choice

def comprimento(pessoa):
    def humor():
        return choice(('E ai', 'Suma daqui', 'Gosto muito de você'))
    return humor() + pessoa

print(comprimento(" José Carlos"))

print(comprimento(" Felicity"))


# Retornando funções de outras funções

from random import choice

def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkkkkkkkkk', 'yayayayayaya'))
    return rir

# Testando

rindo = faz_me_rir()
print(rindo())
'''

# Inner Functions (Funções internas / Nested Functions) podem acessar o escopo de funções mais externas.

from random import choice

def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahahahaha', 'lololololo', 'kkkkkkkkk'))
        return f'{risada} {pessoa}'
    return dando_risada

# Testando

rindo = faz_me_rir_novamente("Fernanda")

print(rindo())
print(rindo())
print(rindo())