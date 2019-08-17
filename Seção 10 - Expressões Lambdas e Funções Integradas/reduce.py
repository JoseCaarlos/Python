"""
Reduce

OBS: A partir do Python3+ a função reduce() não é mais integrada (built-in). Agora temos
que importa e utlizar esta função a partir do módulo 'functools'

Guidon van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso,
99% das vezes um loop for é mais legivel.

Para enetender o reduce()

# Imagine que voce tem uma coleção de dados:

dados = [a1, a2, a3, a4]

# E que voce tem uma função que recebe dois paramêtros:

def funcao(x, y):
    return x * y

Assim como map(), a função reduce() recebe dois paramêtros: a função e o iterável

reduce(funcao, dados)

A função reduce(), funciona da sequinte forma:
    Passo 1: res1 = f(a1, a2) # aplica a função nos dois paramêtros primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo1 mais o terceiro elemento e guarda em res2

    Isso é repetido até o final.
    Passo3: f(res2, a4)
    .
    .
    .
    Passo n: f(resm, an)

Ou seja,  em cada passo ela aplica a função passandoi como primeiro arqgumento o resultado da
aplicação anterior. No final o reduce() irá retornar o resultado final.

Alternativamente poderiamos ver a função reduce como:

funcao(funcao(funcao(a1, a2), a3), a4, ...), an)

"""

# como funiona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 6, 8, 9, 4, 6]

# Para utilizar o reduce() nós precisamos de uma função que receba dois paramêtros

multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

# Utilizando um loop normal

res = 1
for n in dados:
    res = res * n
print(res)