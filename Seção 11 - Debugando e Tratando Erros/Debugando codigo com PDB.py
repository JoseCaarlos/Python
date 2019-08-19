"""
Debugando código com o PDB

PDB -> Python Debugger

Vida de Inseto -> Life's Bug
Bug -> Inseto

# OBS: A utilização de print() para debugar código é uma prática ruim

def dividir(a, b):
    print(f'a = {a}, b= {b}')
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 7))

# Existem formas mais profissionais de se fazer esse 'debug', utilizando o debugger
# Em python, podemos fazer isso em diferentes IDEs, como o pyCharm ou utilizando
# o PDB - Python Debugger


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'

print(dividir(4, 0))

# Exemplo com o PDB - Python Debbuger - Exemplo 2

# Para utilizar o python Debugger, precisamos* importar a biblioteca PDB e então utilizar a função set_trace()

# Comandos básicos do PDB
# l Listar onde estamos no código
# n próxima linha
# p imprimi variável
# c continua a execução - finalizando o debugging


import pdb

nome = 'Angelina'
sobrenome = 'Jolie'
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso ' + curso
print(final)


# Exemplo com o PDB - Python Debbuger - Exemplo 2

# Para utilizar o python Debugger, precisamos* importar a biblioteca PDB e então utilizar a função set_trace()

# Comandos básicos do PDB
# l Listar onde estamos no código
# n próxima linha
# p imprimi variável
# c continua a execução - finalizando o debugging


nome = 'Angelina'
sobrenome = 'Jolie'
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso ' + curso
print(final)


# Por que utilizar este formato?
# O debug é utilizado durante o desenvolvimento. Custumamos realizar todos os imports no inicio
# do arquivo. Por isso, ao invés de colocarmos o import pdb no inicio do arquivo,
# nós colocamos somente onde vamos debuggar, e ao finalizar já fazemos a remoção


# Exemplo com o PDB - Python Debbuger - Exemplo 3

# Para utilizar o python Debugger, precisamos* importar a biblioteca PDB e então utilizar a função set_trace()

# * A partir do Python 3.7, não é mais necessário importar a biblioteca pdb, pois o comando de debug foi
# incorporado como função built-in (integrada) chamada breakpoint()

# Comandos básicos do PDB
# l Listar onde estamos no código
# n próxima linha
# p imprimi variável
# c continua a execução - finalizando o debugging


nome = 'Angelina'
sobrenome = 'Jolie'
breakpoint()
nome_completo = nome + ' ' + sobrenome
curso = 'Programação em Python: Essencial'
final = nome_completo + 'faz o curso ' + curso
print(final)

"""

# OBS: Cuidado com o conflitos entre nomes de variáveis e os comandos pdb


def soma(l, n, p, c):
    breakpoint()
    return l + n + p + c

print(soma(1, 2, 3, 4))

# Como os nomes das variáveis são os mesmo do pdb, devemos utilizar o comando p para imprimir
# as variáveis. Ou seja: p nome_variável

# Nada de colocar nomes não representativos. Sempre optar por nomes significativos
