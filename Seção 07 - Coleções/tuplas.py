"""
Tuplas (Tuple)

Tuplas são bastante parecidas com listas

Existem basicamente duas diferenças básicas:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis: Isso significa que ao se criar uma tupla ela não muda. Toda
operação em tupla gera uma nova tupla

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1,2,3,4,5,6)
print(tupla1)
print(type(tupla1))

tupla2 = 1,2,3,4,5,6
print(tupla2)
print(type(tupla2))

# CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) # Isso não é uma tupla
print(tupla3)
print(type(tupla3))

tupla4 = (4,)
print(tupla4)
print(type(tupla4))

# CONCLUSÃO: Podemos concluir que são definidas pela virgula (,) e não pelo parênteses

(4) -> Não é tupla
(4,) -> É tupla
4, -> É tupla

# Podemos gerar tuplas dinâmicamente com o range tbm
tupla = tuple(range(11,20,2))
print(tupla)

# Desempacotamento de Tupla
tupla = ('Geek University','Programação em Python: Essencial')
school, curse = tupla
print(school)
print(curse)

# Método para: adição e remoção de elementos nas tuplas não existem, dado o fato que ela são imutaveis

# Soma, Valor Máximo, Valor Mínimo e Tamanho

# Se os valores forem todos inteiros ou reais

tupla = (1,2,3,4,5,6)
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

# Concatenação de tuplas

tupla1= (1,2,3,4,5,6)
tupla2 = (7,8,9,)
print(tupla1+tupla2)

tupla1 = tupla1 + tupla2 # Tuplas são imutáveis, mas podemos sobrescrever valores
print(tupla1)

#Verificar se o elemento está na tupla
tupla = (1,2,3,4,5,6)
print(3 in tupla)

# Interando tuplas
tupla = (1,2,3,4,5,6)
for i,n in enumerate(tupla):
    print(i, n)

# Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'b', 'a')
print(tupla.count('a'))


# Dicas na utilização de tuplas

# Devemos utilizar tuplas SEMPRE que não precisamos modificar os dados contidos em uma coleção

# EXEMPLO 01

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')
print(meses)

# O acesso a elementos de uma tupla também é semelhante a de uma lista
print(meses[5])

# Interação com laço
i = 0
while i < len(meses):
    print(meses[i])
    i+=1

# Vericando em qual índice um elemento esta na tupla
print(meses.index('Junho',4))

# OBS: Caso o elemento não exista, será gerado ValueError

# Slicing
# Tupla[inicio:fim:passso]
print(meses[0:10:2])

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro')


# Por quê utilizar tuplas ?
# - Tuplas são mais rápidas do que listas.
# - Tuplas deixam o código mais seguro*.

# * Isso porque trabalhar com elementos imutáveis traz mais seguranças para o código

# Copiando tupla

tupla = 1,2,3,4,5,

print(tupla)

nova = tupla # Na tupla não temos o problema de Shallow Copy

print(nova)
print(tupla)

outra = (4,5,6,)
nova = nova + outra

print(nova)
print(tupla)

"""


