"""
Preservando metadados com wraps

Metadados -> São dadas intrísecos em arquivos. (tamanho, resolução)

Wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema

def ver_log(funcao):
    def logar(*args, **kwargs):
        #Eu sou uma função (logar) dentro de outra#
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    #Soma dois números
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # Soma

print(soma.__doc__)  # Soma dois numeros
"""


# Resolução Problema

from functools import wraps

def ver_log(funcao):
    @wraps(funcao)  # Preserva os metadados da função
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra"""
        print(f'Você está chamando: {funcao.__name__}')
        print(f'Aqui a documentação: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois números"""
    return a + b


# print(soma(10, 30))

print(soma.__name__)  # Soma

print(soma.__doc__)  # Soma dois numeros

print(help(soma))

