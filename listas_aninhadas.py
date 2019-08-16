"""
Listas Aninhadas (Nested Lists)

- Algumas linguagens de programação (C/JAVA) possuem uma estrutura de dados chamada de Arrays
    - Unidimensionais (Arrays / Vetores)
    - Multidimensionais (Matrizes)

Em python nós temos as Listas

numeros = [1, 'b', 3.2435, True, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?
print(listas[0][1]) # 2
print(listas[2][1]) # 8

"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Matriz 3 x 3

# Iterando com loops em uma lista aninhada

for lista in listas:
    for num in lista:
        print(num)

# List Comprehension

print([])