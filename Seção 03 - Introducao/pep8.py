"""
PEP8 - Python Enhancement Proposal

São propostas de melhorias para a linguagem Python

The Zen of Python
import this

A ideia da PEP8 é que possamos escrever codigo python de forma Pythônica.

[1] - Utilize Camel Case para nomes de classes;


class Calculator:
    pass


class CalculatorScientific:
    pass

[2] - Utilize nomes em minúsculos, separados por underlines para funcões ou variáveis


def sum():
    pass


def sum_two():
    pass


number = 4

number_odd = 5

[3] - Utilize 4 espaços para identação !!! (NÃO use tab)(TAB configurado para 4 espaços


if 'a' in 'banana':
    print('tem')

[4] - Linhas em branco

-Separar funções e definições de classe com duas linhas em branco;
- Métodos dentro de uma classe deve ser separados com uma unica linha em branco

[5] - Imports

- Imports devem ser sempre em linhas separadas;

import sys
import os

#Não ha problemas em utilizar:

from types StringType, ListType

#Caso tenha muitos imports de um mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivos antes de quaisquer comentários e
# variaveis ou constantes


[6] - Espaços em expressões e instruções

# Não Faça

funcao ( algo[ 1 ], { outro: 2} )

#Faca
funcao(algo[1], {outro: 2})

[7] - Termine sempre uma instrução com uma nova linha

import this

"""



