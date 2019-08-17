"""
ZIP

zip() -> Cria um iteravél (Zip Object) que agrega elemento de cada um dos iteravéis passados como entrada em pares


# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

zip1 = zip(lista1, lista2)

print(zip1)
print(type(zip1))

# Sempre podemos gerar uma lista, Tupla, ou Dicionario

print(list(zip1))
zip1 = zip(lista1, lista2)
print(tuple(zip1))
zip1 = zip(lista1, lista2)
print(set(zip1))
zip1 = zip(lista1, lista2)
print(dict(zip1))

# OBS: O zip() utiliza o como paramêtro o menor tamanho iteravél. Isso significa que se estiver
# trabalhando com iteravéis de tamanho diferentes, irá parar quando os elementos do menor
# iteravel acabar.

lista3 = [7, 8, 9, 10, 11]

zip1 = zip(lista1, lista2, lista3)
print(list(zip1))

# Podemos utilizar diferentes iteravéis com o zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7 ,8 , 9, 10]
dicionario = {'a': 2, 'b': 3}

zt = zip(tupla, lista, dicionario.values())

print(list(zt))

# Lista de tuplas

dados = [(0, 1), (2, 3), (4, 5)]

print(list(zip(*dados)))

"""

# Exemplo mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2]) for dado in zip(alunos, prova1, prova2)}

print(final)

# Podemos utilizar o map()

final = zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))

print(dict(final))
