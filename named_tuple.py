"""
Módulo Collections - Named Tuple

Recap Tupla
tupla = (1,2,3,)
print(tupla[2])

Named Tuple -> São tuplas, diferenciadas onde, especificamos um nome para a mesma e também parâmetros.

"""

# Importando

from collections import namedtuple

# Precisamos definir o nome e parâmetros.

# Forma 1 - Declaração da Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração da Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração da Named Tuple
cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

# Acessando dados

# Forma 1
print(ray[0]) # idade
print(ray[1]) # raça
print(ray[2]) # nome

# Forma 2
print(ray.idade) # idade
print(ray.raca) # raça
print(ray.nome) # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))