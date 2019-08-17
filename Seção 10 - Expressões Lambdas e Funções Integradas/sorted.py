"""
Sorted

OBS: Não confunda, apesar do nome, com a função sort(), que já estudamos em lista, 0 sort()
so funciona em lista.

Podemos utilizar o sorted() com qualquer iteravél

Como o próprio nome diz, sorted() serve para ordenar.

OBS:  O Sorted(), SEMPRE retorna uma Lista com os elementos do iteravél ordenados

# Exemplo

numeros = (6, 1, 8, 2)
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)

numeros = [6, 1, 8, 2]

# Adicionando paramêtros ao sorted()
print(numeros)
print(tuple(sorted(numeros)))
print(sorted(numeros, reverse=True))

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [

{"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
{"username": "carla", "tweets": []},
{"username": "bob123", "tweets": [], "Cor": "Amarelo"},
{"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
{"username": "gal", "tweets": []}

]
print(usuarios)

# Ordenando pelo Username - Ordem alfábetica
print(sorted(usuarios, key=lambda usuario: usuario['username'],reverse=True))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
"""


# Último exemplo

musicas = [
    {"titulo": "Thunderstruck", "tocou": 3},
    {"titulo": "Eu tem amor", "tocou": 10},
    {"titulo": "Ti love you", "tocou": 4},
    {"titulo": "Até mais", "tocou": 6},
    {"titulo": "Scrooline", "tocou": 1},
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))