"""
Funções com retorno

OBS:Em Python, Quando uma função não retorna nenhum valor, o retorno é None
OBS: Funções python que retornam valores, devem retornar estes valores
com a palavra reservada 'return'

# Exemplo Função

def quadrado_7():
    return 7*7

print(quadrado_7())

OBS: Sobre a palavra reservada return
1 - Ela finaliza a função, ou seja, ela sai da execução da função
2 - Podemos ter, em uma função, diferente returns;
3 - Podemos retornar qualquer tipo e até multiplos valores
"""

from random import random

def joga_moeda():
    # Gera um número pseudo-randômicos entre 0 e 1
    valor = random()
    if valor > .5:
        return "Cara"
    else:
        return "Coroa"

print(joga_moeda())