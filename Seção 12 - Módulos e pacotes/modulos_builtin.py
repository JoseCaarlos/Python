"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no python)
________________________
|Python|Módulos builtin|
========================

# Utilizando alias (apelidos) para módulos/funções
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulo utilizando o *

from random import *
print(random())

# Utilizando alias (apelidos) para módulos/funções
from random import randint as rdi

print(rdi(5, 78))
https://docs.python.org/3.7/py-modindex.html

# Costumamos a utilizando tuple para colocar multiplos imports de um mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
lista = [1, 2, 6]
shuffle(lista)
print(lista)

print(choice('University'))
"""


def soma(a, b):
    return a + b


if __name__ == '__main__':
    print('Está executando')
