"""
Utilizando Lambdas

Conhecidas por Expressões lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anôninas.

função em python

def soma(a, b):
    return a + b

# Função em Python
def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))

# Expressão Lambda

lambda x: 3 * x + 1

# E como utilizar a expressão lambda

calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

# Podemos ter expressões lambdas com múltiplas entradas


nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo(' angelina', ' JOLIE '))

# Em funçções python estudamos que podemos ter uma ou várias entrada.

amar = lambda: 'Como não amar python'

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** .5

tres = lambda x , y, z: 3 / (1 / x + 1 / y + 1 / z)

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# OBS Se passarmos mais argumentos do que parâmentros esperados esperamos teremos TYpeError


autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlen', 'Arthur C.', 'Douglas Adams',
           'H. G. Wells', 'Leigh Brackett']

print(autores)


autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)

"""

# Função Quadratica
# f(x) = a * x x ** 2 * x + c

def gera_funcao(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c   """
    return lambda x: a * x *  x ** 2 * x + c


print(gera_funcao(3, 0, 1)(2))


