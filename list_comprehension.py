"""
List Comprehension

- Utilizando List Comprehension nos podemos gerar novas listas com dados processaos a partir de
de outro iteravel

# Sintaxe da List Comprehension

[ dado for dado in iterável ]

# Exemplos

numeros = [1, 2, 3, 4, 5]

resp = [numero * 10 for numero in numeros]

print(resp)

res = [numero / 2 for numero in numeros]

print(res)

Para entender o que está acontecendo devemos dividir a expressão em duas partes:

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

numeros = [1, 2, 3, 4, 5]

def potencia(numero):
    return numero**2

res = [potencia(numero) for numero in numeros]

print(res)

# List Comprehension versos Loop

# Loop

numeros = [1, 2, 3, 4, 5]

numeros_dobrados = []
for num in numeros:
    numeros_dobrado = num * 2
    numeros_dobrados.append(numeros_dobrado)
print(numeros_dobrados)

# List Comprehension

print([numero * 2 for numero in numeros])

"""
# Outros Exemplos

# 1

nome = 'Geek University'
print([letra.upper() for letra in nome])

# 2

def caixa_alt(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome

amigos = ['maria', 'julia', 'pedro', 'guilherme', 'vanessa']

print([caixa_alt(amigo) for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, 1, 3.14]])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5]])

