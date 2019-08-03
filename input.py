"""
Recebendo dados do usúario

Em Python, string é tudo que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

- Aspas simples -> 'jose'
- Aspas duplas -> "jose"
- Aspas simples triplas -> '''Jose'''
"""
# - Aspas duplas triplas """jose""""

# Entrada de Dados
# print("Digite seu nome")
# nome = input()
nome = input("Qual seu nome: ")

# print("Digite sua idade")
# age = input()

age = int(input("Digite sua idade: "))

# Print versão 2.x
# print("A %s tem %s" % (nome,age))

# Print versão 3.x
# print('A {0} tem {1}'.format(nome, age))

# Print acima 3.6 ou 3.7
print(f'O {nome.title()} tem {age} anos')
