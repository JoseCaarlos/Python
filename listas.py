"""
Listas

Listas em python funcionam como vetores, matrizes (arrays) em outras linguagens, com diferença
de ser DINÂMICO e também podemos colocar QUALQUER TIPO DE DADOS

- Dinâmico: Não possui tamanho fixo: ou seja, criar a lista e ir adicionando elementos;
- Qualquer tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de dado

As lista em python são representadas por colchetes []


lista1.sort() # Ordena a lista
lista2.sort()

# Conta número de ocorrências em uma lista
print(lista2.count('o'))

# Adicionar elementos na lista utilizando a função a append
# Com o append nós so conseguimos adicionar um elemento por vez

print(lista1)
lista1.append(42)
print(lista1)

# Com o extend coloca cada elemento da lista como valor adicional a lista
lista1.extend([115,654,46])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição no indice
# O mesmo será deslocado para direita da lista
lista1.insert(2,'novo valor')
print(lista1)

# Podemos facilmente juntar 2 lista
lista6 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista utilizando reverse ou [::-1]
lista1.reverse()
print(lista1[::-1])

# Copia lista
lista6 = lista1.copy()
lista6.extend([11,35,16])
print(lista1)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista1))

# Podemos remover o último elemento de uma lista e retorna o elemento que foi removido
print(lista1)
lista1.pop()
print(lista1)

# Podemos remover um elemento pelo índice
# Os elementos a direita destes índice são delocados para esquerda
lista1.pop(2)
print(lista1)

# Podemos remover todos os elementos da lista
lista1.clear()
print(lista1)

# Podemos facilmente converter uma String para lista
curso = 'Programação Em Python Essencial'
curso = curso.split()
print(curso)

# Podemos facilmente converter uma Lista em String
curso = ['Programação', 'Em', 'Python', 'Essencial']
curso = 'o'.join(curso)
print(curso)

# Gerar um índice no laço FOR
for indice,cor in enumerate(cores):
    print(f"{indice} => {cor}")

# Encontrar o índice do elemento na lista, caso não exits retorna erro.
lista1 = [1,2,3,4,5,6,7,8,9]
print(lista1.index(9))

# Encontrar o índice do elemento na lista mas procura somente a partir do parâmetro passado indice 5
lista1 = [1,2,3,4,5,6,7,5,9]
print(lista1.index(5,20))
"""

lista = [1,2,3,4,5,6,7,5,9]

print(lista[::-1])





