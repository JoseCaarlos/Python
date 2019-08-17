"""
Reversed

OBS: Não confunda com a função reverse() que estudamos nas listas

A função reverse() só funciona em listas

Já a função reversed() funciona com qualquer iteravél

Sua função é inverter o iteravél

A função reversed() retorna um iteravél chamado LIst Reverse Iterator


# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))

# Podemos converter o elemento retornado para uma lista, tupla e conjunto

# Lista
print(list(reversed(lista)))

# Tupla
print(tuple(reversed(lista)))

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto
print(set(reversed(lista)))

# Podemos iterar sobre o reverse()

for letra in reversed('Geek University'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Geek University'))))

# Já vimos como fazer isso mais facil com slice de string

print('Geek University'[::-1])

for v in range(9, -1, -1):
    print(v)
"""


