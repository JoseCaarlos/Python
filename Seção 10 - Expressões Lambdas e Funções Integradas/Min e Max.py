"""
Min e Max

max() -> Retorn o maior valor em um iteravel ou o maior de dois ou mais elementos

lista = [1, 8, 99, 34, 129]
print(max(lista))  # 129

tupla = 1, 8, 99, 34, 129
print(max(tupla))  # 129

conjunto = {1, 8, 99, 34, 129}
print(max(conjunto))  # 129

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(max(dict.values()))  # 129

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(max(val1, val2))

print(max('a', 'b', 'c')) # 'C'

min() -> Retorn o menor valor em um iteravel ou o menor de dois ou mais elementos
lista = [1, 8, 99, 34, 129]
print(min(lista))  # 129

tupla = 1, 8, 99, 34, 129
print(min(tupla))  # 129

conjunto = {1, 8, 99, 34, 129}
print(min(conjunto))  # 129

dict = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}

print(min(dict.values()))  # 129

# Faça um programa que receba dois valores do usuário e mostre o maior

val1 = int(input("Informe o primeiro valor: "))
val2 = int(input("Informe o segundo valor: "))
print(min(val1, val2))

print(min('a', 'b', 'c'))  # 'A'

# Outros exemplos

nome = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivader']

print(max(nome))  # Tim
print(min(nome))  # Arya

print(max(nome, key=lambda nome: len(nome)))  # Ollivader

print(min(nome, key=lambda nome: len(nome)))  # Tim
"""

# Outros exemplos

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Eu tem amor", "tocou": 10},
    {"titulo": "Ti love you", "tocou": 4},
    {"titulo": "Até mais", "tocou": 6},
    {"titulo": "Scrooline", "tocou": 1},
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['titulo']))

# DESAFIO! Imprima somente o título da música mais e menos tocada
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print(min(musicas, key=lambda musica: musica['titulo'])['titulo'])

# DESAFIO! Como encontrar a musica mais tocada e a menos sem usar max() e min ()

max = 1
for musica in musicas:
    if musica['tocou'] > max:
        max =  musica['tocou']
print(musica)

max = 99999
for musica in musicas:
    if musica['tocou'] == max:
        max =  musica['tocou']
print(musica)