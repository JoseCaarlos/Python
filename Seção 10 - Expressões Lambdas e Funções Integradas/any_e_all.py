"""
Any e All

all() -> Retorn True se todos os elementos do iteravél são verdadeiros ou ainda se o iteravél está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros ? False (0 é falso)

print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros ? True

print(all((0, 1, 2, 3, 4)))  # Todos os números são verdadeiros ? False

print(all({0, 1, 2, 3, 4}))  # Todos os números são verdadeiros ? False

print(all('Geek'))  # Todos os números são verdadeiros ? True

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano']

print(all([nome[0] == 'C' for nome in nomes]))

# OBS: um iteravel vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'gggg' if letra in 'aeiou']))

# Exemplo all()
print(all([num for num in [4, 2, 10, 10, 8] if num % 2 == 0 ]))

Any() -> Retorna True se qualquer elemento do iteravél for verdadeiro. Se o iteravél estiver vazio, retorna False

"""

print(any([0, 1, 2, 3, 4])) # True

print(any([0, False, {}, [], []]))

nomes = ['Carlos', 'Camila', 'Carla', 'Dassiano']

print(any([nome[0] == 'D' for nome in nomes]))




